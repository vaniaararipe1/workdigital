"""Monta o contexto dos templates (relatório do lead e notas internas) a partir do resultado."""
from __future__ import annotations

import base64
from dataclasses import asdict
import re
from pathlib import Path

from ..analise.referencias import referencia
from ..modelos import ESFORCO_MEDIO, ESFORCO_PROJETO, ESFORCO_RAPIDO, Achado, Nota

ORDEM_PRIORIDADE = {"alta": 0, "media": 1, "baixa": 2, "": 3}
ORDEM_SITUACAO = {"problema": 0, "atencao": 1, "na": 2, "ok": 3}
ORDEM_ESFORCO = {ESFORCO_RAPIDO: 0, ESFORCO_MEDIO: 1, ESFORCO_PROJETO: 2, "": 3}
PESO_CATEGORIA = {"ux": 0, "performance": 1, "seo": 2}
AREA_PADRAO = {"performance": "Performance", "ux": "Conversão", "seo": "SEO"}


def _sem_recomendacao_antiga(texto: str) -> str:
    """Relatórios antigos traziam "O recomendado ..." dentro do texto; agora a recomendação tem campo próprio."""
    return re.sub(r"\s*O recomendado[^.]*\.\s*$", "", texto or "")


def _nota_ctx(n: Nota, cobertura: str) -> dict:
    return {"categoria": n.categoria, "nota": n.nota, "faixa": n.faixa, "rotulo": n.rotulo, "cobertura": cobertura}


def top3(achados: list[Achado]) -> list[dict]:
    candidatos = [a for a in achados if a.tipo == "medido" and a.impacto
                  and (a.situacao == "problema" or (a.situacao == "atencao" and a.prioridade == "alta"))]
    candidatos.sort(key=lambda a: (ORDEM_PRIORIDADE[a.prioridade], ORDEM_SITUACAO[a.situacao],
                                   PESO_CATEGORIA[a.categoria], -a.peso))
    escolhidos, ids = [], set()
    for a in candidatos:
        # evita dois itens de performance quase iguais (ex.: LCP e uma oportunidade)
        chave = a.categoria if a.categoria == "performance" else a.id
        if chave in ids:
            continue
        ids.add(chave)
        ref = referencia(a.id)
        escolhidos.append({"titulo": a.titulo, "o_que_vimos": _sem_recomendacao_antiga(a.o_que_vimos) if ref else a.o_que_vimos,
                           "impacto": a.impacto, "prioridade": a.prioridade or "media", "referencia": ref})
        if len(escolhidos) == 3:
            break
    return escolhidos


def plano(achados: list[Achado]) -> list[dict]:
    fases = [
        {"nome": "Fazer primeiro", "cor": "#C00252", "chave": "alta", "itens": []},
        {"nome": "Em seguida", "cor": "#6025E1", "chave": "media", "itens": []},
        {"nome": "Quando possível", "cor": "#04CD8F", "chave": "baixa", "itens": []},
    ]
    vistos = set()
    for a in sorted(achados, key=lambda a: (ORDEM_PRIORIDADE[a.prioridade], ORDEM_ESFORCO.get(a.esforco, 3),
                                            PESO_CATEGORIA[a.categoria], -a.peso)):
        if not a.correcao or a.situacao not in ("problema", "atencao") or not a.prioridade:
            continue
        if a.correcao in vistos:
            continue
        vistos.add(a.correcao)
        fase = next(f for f in fases if f["chave"] == a.prioridade)
        fase["itens"].append({"acao": a.correcao, "area": a.area or AREA_PADRAO[a.categoria],
                              "esforco": a.esforco, "avaliacao": a.tipo == "avaliacao"})
    return fases


def _ordenar_itens(itens: list[Achado]) -> list[dict]:
    out = []
    for a in sorted(itens, key=lambda a: (ORDEM_SITUACAO[a.situacao], ORDEM_PRIORIDADE[a.prioridade])):
        ref = referencia(a.id) if a.tipo == "medido" else None
        d = a.to_dict()
        if ref:
            d["o_que_vimos"] = _sem_recomendacao_antiga(d["o_que_vimos"])
        out.append({**d, "referencia": ref})
    return out


def _data_uri(caminho: str | None) -> str | None:
    if not caminho or not Path(caminho).exists():
        return None
    return "data:image/jpeg;base64," + base64.b64encode(Path(caminho).read_bytes()).decode()


RODAPE = {
    "automatica": "Análise técnica automatizada. Avaliação especializada em revisão.",
    "revisada": "Análise técnica automatizada com revisão especializada.",
}

FORMULA = {
    "performance": "Como a nota foi formada: 70% da nota de velocidade do Google no celular e 30% no computador.",
    "criterios": ("Como a nota foi formada: média ponderada dos {n} critérios medidos nesta área "
                  "(ok vale 100, atenção vale 50, problema vale 0). Itens não medidos, não confirmados "
                  "ou de avaliação de especialista ficam fora da conta."),
}


def montar(r: dict, versao: str = "automatica", revisao: dict | None = None, prazo_dias: int = 2) -> dict:
    """`r` é o resultado do pipeline. `versao`: "automatica" ou "revisada" (exige `revisao` validada)."""
    from .. import revisao as rv
    if versao not in RODAPE:
        raise ValueError(f"versão desconhecida: {versao}")
    if versao == "revisada" and revisao is None:
        raise ValueError("a versão revisada exige um revisao.json validado")

    medidos = [a for a in r["achados"] if a.tipo != "avaliacao"]
    achados = medidos + (rv.avaliacoes_como_achados(revisao) if versao == "revisada" else [])
    notas: dict[str, Nota] = r["notas"]
    perf_m, perf_d = r["performance"]["mobile"], r["performance"]["desktop"]

    disp = [n for n, p in (("celular", perf_m), ("computador", perf_d)) if p.get("ok")]
    cob_perf = ("Medido no " + " e no ".join(disp)) if disp else "Não foi possível medir"
    notas_ctx = [
        _nota_ctx(notas["performance"], cob_perf),
        _nota_ctx(notas["ux"], f"{notas['ux'].criterios_medidos} de {notas['ux'].criterios_total} critérios medidos"),
        _nota_ctx(notas["seo"], f"{notas['seo'].criterios_medidos} de {notas['seo'].criterios_total} critérios medidos"),
    ]

    por_cat = {c: [a for a in achados if a.categoria == c and a.secao] for c in ("performance", "ux", "seo")}
    dispositivos = [{"nome": n.capitalize(), "nota": p["nota"]} for n, p in (("celular", perf_m), ("computador", perf_d))
                    if p.get("ok") and p.get("nota") is not None]
    secoes = [
        {"id": "performance", "kicker": "Performance", "titulo": "Velocidade do site",
         "intro": "Quanto tempo o visitante espera até ver e usar a página. Sites lentos perdem visitas e ficam atrás no Google.",
         "formula": FORMULA["performance"],
         "dispositivos": dispositivos, "fonte": r["performance"]["fonte_texto"],
         "metricas": [asdict(m) for m in r["metricas"]], "titulo_itens": "Principais oportunidades",
         "itens": _ordenar_itens(por_cat["performance"])},
        {"id": "ux", "kicker": "Experiência e conversão", "titulo": "O site ajuda o visitante a virar cliente?",
         "intro": "Verificamos se quem chega entende o que você oferece e consegue falar com você sem esforço, no celular e no computador.",
         "formula": FORMULA["criterios"].format(n=notas["ux"].criterios_medidos),
         "itens": _ordenar_itens(por_cat["ux"])},
        {"id": "seo", "kicker": "SEO e visibilidade", "titulo": "Como o Google e as IAs encontram você",
         "intro": "Itens técnicos que ajudam o site a aparecer nas buscas do Google e nas respostas de assistentes como ChatGPT e Gemini.",
         "formula": FORMULA["criterios"].format(n=notas["seo"].criterios_medidos),
         "itens": _ordenar_itens(por_cat["seo"])},
    ]
    ctx = {
        "exemplo": False,
        "versao": versao,
        "rodape_texto": RODAPE[versao],
        "prazo_dias": prazo_dias,
        "empresa": r["empresa"],
        "url": r["url_final"],
        "data_extenso": r["data_extenso"],
        "captura_mobile": _data_uri(r.get("captura_mobile")),
        "notas": notas_ctx,
        "top3": top3(medidos),
        "secoes": secoes,
        "tecnologias": [asdict(t) for t in r["tecnologias"]],
        "paginas": [p for p in r.get("paginas_resumo", []) if str(p.get("situacao", "")).startswith("aberta")],
        "plano": [],
        "nota_pessoal": "",
        "demonstracao": False,
    }
    if versao == "revisada":
        ctx["plano"] = rv.plano_revisado(revisao)
        ctx["nota_pessoal"] = revisao["nota_pessoal"]["texto"].strip()
        ctx["demonstracao"] = bool(revisao.get("demonstracao"))
    return ctx
