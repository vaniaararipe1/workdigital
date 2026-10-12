"""Orquestra o diagnóstico completo. Usado pela linha de comando e, na Fase 2, pela fila."""
from __future__ import annotations

import json
import logging
import re
from dataclasses import asdict
from datetime import date, datetime
from pathlib import Path
from urllib.parse import urlsplit

from . import pontuacao
from .analise import performance as a_perf
from .analise import seo as a_seo
from .analise import tecnologias as a_tec
from .analise import ux as a_ux
from .coleta import pagespeed, site
from .coleta.render import Renderizador
from .config import Config
from .http import ClienteHTTP
from .rastreador import escolher_paginas
from .relatorio import contexto as ctx_relatorio
from .relatorio import notas as ctx_notas
from .modelos import Nota
from .relatorio.gerar import data_extenso, html_para_pdf, renderizar_html
from .seguranca import validar_entrada

log = logging.getLogger("diagnostico")
VERSAO = "1.0.0"


def nome_pasta(url: str, quando: date) -> str:
    host = (urlsplit(url).hostname or "site").removeprefix("www.")
    return re.sub(r"[^a-z0-9.-]", "-", host.lower()) + "-" + quando.isoformat()


def _json_padrao(o):
    if hasattr(o, "__dataclass_fields__"):
        return asdict(o)
    if isinstance(o, (set, tuple)):
        return list(o)
    if isinstance(o, (Path, date, datetime)):
        return str(o)
    return repr(o)


def executar_diagnostico(url: str, empresa: str, config: Config | None = None, pasta_saida: Path | None = None,
                         gerar_pdf: bool = True) -> dict:
    """Roda coleta, análise e geração dos arquivos. Retorna o resultado completo."""
    config = config or Config.do_ambiente()
    hoje = date.today()
    url = validar_entrada(url, portas=config.portas_permitidas)
    pasta = pasta_saida or (config.pasta_relatorios / nome_pasta(url, hoje))
    (pasta / "capturas").mkdir(parents=True, exist_ok=True)
    avisos: list[str] = []
    cliente = ClienteHTTP(config)

    # ---------- página inicial e robots ----------
    log.info("Acessando %s", url)
    inicial = cliente.get(url, checar_robots=False)
    url_final = inicial.url_final or url
    if inicial.erro:
        avisos.append(f"A primeira requisição HTTP falhou: {inicial.erro}.")
    elif inicial.status and inicial.status >= 400:
        avisos.append(f"A página inicial respondeu com código {inicial.status} para a requisição direta. "
                      "Pode ser bloqueio de robôs (firewall); o navegador pode ter tido resultado diferente.")
    robots = site.coletar_robots(cliente, url_final)
    pode_rastrear = robots["permite_home"]
    if not pode_rastrear:
        avisos.append("O robots.txt do site pede para robôs não acessarem a página inicial. "
                      "Respeitamos: não abrimos páginas do site; só o PageSpeed do Google foi consultado.")

    # ---------- renderização ----------
    home_d = home_m = None
    paginas: list[dict] = []
    paginas_resumo: list[dict] = []
    sitemap = {"existe": False, "url": "", "total_urls": 0, "urls": [], "tentativas": []}
    bloqueados: list[str] = []
    if pode_rastrear:
        try:
            with Renderizador(config) as rnd:
                log.info("Renderizando página inicial (computador e celular)")
                home_d = rnd.renderizar(url_final, "desktop", pasta / "capturas" / "home-computador.jpg")
                home_m = rnd.renderizar(url_final, "mobile", pasta / "capturas" / "home-celular.jpg")
                if home_d.get("url_final"):
                    validar_entrada(home_d["url_final"])  # redirecionamentos via JavaScript também são checados
                    url_final = home_d["url_final"]
                for r_, nome in ((home_d, "computador"), (home_m, "celular")):
                    if r_.get("erro"):
                        avisos.append(f"Página inicial no {nome}: {r_['erro']}.")
                paginas.append(home_d)
                paginas_resumo.append({"url": url_final, "origem": "página inicial",
                                       "situacao": home_d.get("erro") or f"aberta (código {home_d.get('status')})"})

                sitemap = site.coletar_sitemap(cliente, url_final, robots["sitemaps_declarados"])
                escolhidas = escolher_paginas(url_final, home_d.get("html", ""), sitemap["urls"],
                                              config.max_paginas_internas * 2)
                abertas = 0
                for item in escolhidas:
                    if abertas >= config.max_paginas_internas:
                        break
                    if not cliente.permitido(item["url"]):
                        paginas_resumo.append({**item, "situacao": "ignorada (robots.txt)"})
                        continue
                    log.info("Renderizando %s", item["url"])
                    rp = rnd.renderizar(item["url"], "desktop")
                    paginas_resumo.append({**item, "situacao": rp.get("erro") or f"aberta (código {rp.get('status')})"})
                    if rp.get("erro"):
                        continue
                    paginas.append(rp)
                    abertas += 1
                bloqueados = rnd.bloqueados
        except Exception as e:  # noqa: BLE001
            avisos.append(f"O navegador automatizado falhou: {str(e).splitlines()[0][:200]}.")
            log.exception("Falha no navegador")
    if bloqueados:
        avisos.append(f"{len(bloqueados)} requisições do navegador para endereços internos/privados foram bloqueadas por segurança.")

    paginas_ok = [p for p in paginas if p.get("html") and not p.get("erro")]

    # ---------- coletas HTTP ----------
    llms = site.coletar_llms(cliente, url_final)
    https = site.coletar_https(cliente, url_final)
    extraidas = [a_seo.extrair_pagina(p.get("url_final") or p["url"], p["html"]) for p in paginas_ok]
    ja_vistas = {p.get("url_final") or p["url"] for p in paginas_ok}
    candidatos_links = [l for e in extraidas for l in e["links_internos"] if l not in ja_vistas]
    links = site.verificar_links(cliente, candidatos_links, config.max_links_verificados) if pode_rastrear else {}

    # ---------- performance ----------
    if not pode_rastrear:
        config.usar_lighthouse_local = False
    log.info("Medindo performance (celular)")
    perf_m = pagespeed.extrair(pagespeed.medir(url_final, "mobile", config))
    log.info("Medindo performance (computador)")
    perf_d = pagespeed.extrair(pagespeed.medir(url_final, "desktop", config))
    for nome, p in (("celular", perf_m), ("computador", perf_d)):
        if p.get("fonte") == "lighthouse_local":
            avisos.append(f"Performance no {nome}: PageSpeed indisponível ({p['tentativas'][0]['erro']}); "
                          "usado o Lighthouse local. Os números podem diferir do PageSpeed.")

    # ---------- análise ----------
    achados = []
    achados += a_perf.achados(perf_m, perf_d)
    achados += a_ux.analisar(home_m if home_m and not home_m.get("erro") else None,
                             home_d if home_d and not home_d.get("erro") else None,
                             [p for p in paginas_ok if p.get("medidas")])
    achados_seo, _ = a_seo.analisar(paginas_ok, robots, sitemap, llms, https, inicial.redirecionamentos, links, url_final)
    achados += achados_seo

    nota_perf, n_perf, det_perf = a_perf.nota(perf_m, perf_d)
    notas = {
        "performance": Nota("Performance", nota_perf, n_perf, 2, det_perf),
        "ux": pontuacao.nota_por_criterios("Experiência e conversão", [a for a in achados if a.categoria == "ux"]),
        "seo": pontuacao.nota_por_criterios("SEO e visibilidade", [a for a in achados if a.categoria == "seo"]),
    }
    tecnologias = a_tec.detectar([p["html"] for p in paginas_ok], inicial.headers)

    resultado = {
        "versao": VERSAO,
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "empresa": empresa,
        "url_informada": url,
        "url_final": url_final,
        "data": hoje.isoformat(),
        "data_extenso": data_extenso(hoje),
        "pasta": str(pasta),
        "avisos": avisos,
        "achados": achados,
        "notas": notas,
        "metricas": a_perf.metricas(perf_m, perf_d),
        "tecnologias": tecnologias,
        "performance": {"mobile": perf_m, "desktop": perf_d,
                        "fonte_texto": a_perf.fonte_texto(perf_m, perf_d, hoje.strftime("%d/%m/%Y"))},
        "paginas_resumo": paginas_resumo,
        "captura_mobile": (home_m or {}).get("captura"),
        "coleta": {
            "requisicao_inicial": {"status": inicial.status, "erro": inicial.erro,
                                   "redirecionamentos": inicial.redirecionamentos, "cabecalhos": inicial.headers},
            "robots": robots, "sitemap": {**sitemap, "urls": sitemap.get("urls", [])[:50]},
            "llms": llms, "https": https, "links": links,
            "paginas": [{k: v for k, v in p.items() if k != "html"} for p in paginas],
            "seo_paginas": extraidas,
            "requisicoes_bloqueadas": bloqueados[:50],
            "log_http": cliente.log,
        },
    }
    gerar_arquivos(resultado, pasta, config, gerar_pdf)
    return resultado


def gerar_arquivos(resultado: dict, pasta: Path, config: Config, gerar_pdf: bool = True) -> None:
    html = renderizar_html(ctx_relatorio.montar(resultado))
    (pasta / "relatorio.html").write_text(html, encoding="utf-8")
    notas_html = renderizar_html(ctx_notas.montar(resultado), template="notas_internas.html.j2")
    (pasta / "notas-internas.html").write_text(notas_html, encoding="utf-8")
    (pasta / "dados.json").write_text(json.dumps(resultado, default=_json_padrao, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
    if gerar_pdf:
        html_para_pdf(pasta / "relatorio.html", pasta / "relatorio.pdf", config.chromium_path)


def carregar_resultado(pasta: Path) -> dict:
    """Reconstrói o resultado a partir do dados.json (para regerar os arquivos após uma edição)."""
    from .modelos import Achado, Metrica, Nota, Tecnologia
    r = json.loads((pasta / "dados.json").read_text(encoding="utf-8"))
    r["achados"] = [Achado(**a) for a in r["achados"]]
    r["metricas"] = [Metrica(**m) for m in r["metricas"]]
    r["tecnologias"] = [Tecnologia(**t) for t in r["tecnologias"]]
    r["notas"] = {k: Nota(**v) for k, v in r["notas"].items()}
    r["pasta"] = str(pasta)
    return r


def regerar(pasta: Path, config: Config | None = None, gerar_pdf: bool = True) -> dict:
    """Gera de novo relatório, notas e PDF a partir do dados.json, sem acessar o site."""
    config = config or Config.do_ambiente()
    r = carregar_resultado(pasta)
    # notas recalculadas a partir dos achados (caso algum tenha sido editado)
    r["notas"]["ux"] = pontuacao.nota_por_criterios("Experiência e conversão", [a for a in r["achados"] if a.categoria == "ux"])
    r["notas"]["seo"] = pontuacao.nota_por_criterios("SEO e visibilidade", [a for a in r["achados"] if a.categoria == "seo"])
    if r.get("captura_mobile") and not Path(r["captura_mobile"]).exists():
        r["captura_mobile"] = str(pasta / "capturas" / "home-celular.jpg")
    gerar_arquivos(r, pasta, config, gerar_pdf)
    return r
