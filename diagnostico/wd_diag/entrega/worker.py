"""Processamento automático (Fase 2). Roda no GitHub Actions do repositório privado de diagnósticos.

    python -m wd_diag.entrega.worker automatico --dados DIR --site URL --empresa "X" [--email --nome ...]
    python -m wd_diag.entrega.worker revisao --dados DIR --arquivos relatorios/<pasta>/revisao.json ...
    python -m wd_diag.entrega.worker falha --dados DIR --id ID --site URL

Estrutura em DIR (branch de dados do repositório privado):
    relatorios/<dominio>-<data>/   saída da ferramenta + lead.json + envio.json
    status/<id>.json               estado público mínimo para a página do diagnóstico (sem dados pessoais)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import secrets
import sys
import traceback
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import quote, urlsplit

from ..config import Config
from ..pipeline import executar_diagnostico, gerar_previa, gerar_revisada, nome_pasta
from ..relatorio.contexto import top3
from ..relatorio.gerar import link_whatsapp
from ..relatorio.notas import abordagens
from ..revisao import FASES, RevisaoIncompleta, aplicar_aprovacao
from ..seguranca import UrlInvalida, validar_entrada
from . import email as mail
from .email import e

ORIGENS_COM_LIMITE = ("popup", "landing", "site")
BRANCH_DADOS = os.environ.get("BRANCH_DADOS", "relatorios")
SITE = os.environ.get("SITE_DIAGNOSTICO", "https://diagnostico.workdigital.art.br").rstrip("/")


def _salvar_json(caminho: Path, dados: dict) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def status(dados: Path, id_: str | None, **campos) -> None:
    """Estado lido pela página do diagnóstico. Nunca inclui e-mail, nome ou telefone."""
    if not id_ or not re.fullmatch(r"[A-Za-z0-9-]{8,64}", id_):
        return
    _salvar_json(dados / "status" / f"{id_}.json", {"atualizado_em": datetime.now().isoformat(timespec="seconds"), **campos})


def _host(url: str) -> str:
    return (urlsplit(url).hostname or "").removeprefix("www.")


def garantir_chave(arq_revisao: Path) -> str:
    """Chave aleatória da página de revisão (só a Vania recebe o link). Fica no revisao.json do repositório privado."""
    rev = json.loads(arq_revisao.read_text(encoding="utf-8"))
    if not re.fullmatch(r"[0-9a-f]{32}", str(rev.get("chave_revisao", ""))):
        rev["chave_revisao"] = secrets.token_hex(16)
        _salvar_json(arq_revisao, rev)
    return rev["chave_revisao"]


def link_revisar(pasta: Path, chave: str) -> str:
    return f"{SITE}/revisar?p={quote(pasta.name)}&k={quote(chave)}"


NOMES_NOTA = {"performance": "Velocidade", "ux": "Experiência e conversão", "seo": "SEO e visibilidade"}
ROTULO_ORIGEM = {"popup": "popup do site", "landing": "landing page", "site": "página do diagnóstico",
                 "prospeccao": "prospecção (você mesma)"}


def _cor_nota(n) -> str:
    if n is None:
        return "#8A889A"
    return "#04A776" if n >= 80 else ("#6025E1" if n >= 50 else "#C00252")


def notas_email(notas: dict) -> list[dict]:
    return [{"nome": nome, "valor": "—" if notas.get(k) is None else notas[k], "cor": _cor_nota(notas.get(k))}
            for k, nome in NOMES_NOTA.items()]


def link_whatsapp_lead(numero: str) -> str:
    d = re.sub(r"\D", "", numero or "")
    if len(d) in (10, 11):
        d = "55" + d
    return f"https://wa.me/{d}" if 12 <= len(d) <= 15 else ""


def _primeiro_nome(nome: str) -> str:
    partes = (nome or "").split()
    return partes[0].capitalize() if partes else ""


def _sem_marca(t: str) -> str:
    return re.sub(r"^\s*\[RASCUNHO\]\s*", "", t or "", flags=re.I).strip()


def email_lead_automatico(r: dict, nome: str, prazo_dias: int) -> str:
    host = _host(r["url_final"])
    return mail.renderizar(
        "lead_automatico.html.j2", assunto=f"Seu resultado técnico: {host}", host=host,
        preheader="As notas do seu site e o relatório completo em PDF.", kicker="Resultado técnico",
        titulo=f"A análise do site {host} está pronta", primeiro_nome=_primeiro_nome(nome),
        notas=notas_email({k: v.nota for k, v in r["notas"].items()}),
        principais=top3(r["achados"]), prazo_dias=prazo_dias, whatsapp_url=link_whatsapp(r["empresa"]))


def email_lead_revisado(empresa: str, url: str, nome: str) -> str:
    host = _host(url)
    return mail.renderizar(
        "lead_revisado.html.j2", assunto=f"Sua avaliação completa: {host}", host=host,
        preheader="A avaliação completa do seu site, com o plano por onde começar.", kicker="Avaliação completa",
        titulo=f"A avaliação completa do site {host}", primeiro_nome=_primeiro_nome(nome),
        whatsapp_url=link_whatsapp(empresa))


def email_vania(r: dict, rev: dict, lead: dict, enviado: bool, rel: str) -> str:
    """O que já foi medido (resumo) e o que a Vania precisa revisar, com os rascunhos por extenso."""
    achados = r["achados"]
    medidos = [x for x in achados if x.tipo == "medido"]
    notas = notas_email({k: v.nota for k, v in r["notas"].items()})
    for n, cat in zip(notas, NOMES_NOTA):
        c = [x.situacao for x in medidos if x.categoria == cat]
        partes = [f"{c.count(s)} {rot if c.count(s) == 1 else plural}"
                  for s, rot, plural in (("ok", "ok", "ok"), ("atencao", "em atenção", "em atenção"),
                                         ("problema", "problema", "problemas")) if c.count(s)]
        n["contagem"] = " · ".join(partes) or "nada medido"
    aprovado = aplicar_aprovacao(rev, forcar=True)
    avaliacoes = [{"titulo": av.get("titulo", ""), "situacao": av.get("situacao", ""),
                   "o_que_vimos": av.get("o_que_vimos", ""), "o_que_significa": av.get("o_que_significa", ""),
                   "o_que_fazer": av.get("o_que_fazer", ""), "sinais": (av.get("sinais_coletados") or "")[:300]}
                  for av in aprovado.get("avaliacoes", [])]
    itens = aprovado.get("plano", {}).get("itens", [])
    plano = [{"nome": f, "itens": [it.get("acao", "") for it in itens if it.get("fase") == f]} for f in FASES]
    conferir = [{"titulo": x.titulo, "o_que_vimos": x.o_que_vimos, "nota_interna": x.nota_interna}
                for x in achados if x.tipo in ("nao_confirmado", "nao_medido")]
    contato = {k: lead.get(k) or "" for k in ("nome", "email", "whatsapp", "cargo", "segmento")}
    contato["whatsapp_url"] = link_whatsapp_lead(contato["whatsapp"])
    return mail.renderizar(
        "vania_pronto.html.j2", empresa=r["empresa"], url=r["url_final"], contato=contato,
        origem=ROTULO_ORIGEM.get(lead.get("origem", ""), lead.get("origem", "")), enviado=enviado,
        notas=notas, principais=top3(achados), avaliacoes=avaliacoes,
        nota_pessoal=(aprovado.get("nota_pessoal") or {}).get("texto", ""), plano=plano, plano_total=len(itens),
        conferir=conferir, abordagens=abordagens(r),
        link_revisar=link_revisar(Path(rel), rev.get("chave_revisao", "")))


def verificar_limites(dados: Path, url: str, origem: str, limite_diario: int, dias_repeticao: int = 7) -> str | None:
    """Mensagem de bloqueio, ou None. Diagnósticos de prospecção não têm limite."""
    if origem not in ORIGENS_COM_LIMITE:
        return None
    pasta = dados / "relatorios"
    if not pasta.exists():
        return None
    prefixo = nome_pasta(url, date.today()).rsplit("-", 3)[0] + "-"
    corte = date.today() - timedelta(days=dias_repeticao)
    for p in pasta.glob(prefixo + "*"):
        try:
            quando = date.fromisoformat(p.name[len(prefixo):])
        except ValueError:
            continue
        lead = p / "lead.json"
        try:
            origem_anterior = json.loads(lead.read_text(encoding="utf-8")).get("origem") if lead.exists() else None
        except ValueError:
            origem_anterior = None
        if quando >= corte and (p / "relatorio.pdf").exists() and origem_anterior in ORIGENS_COM_LIMITE:
            return "Este site já foi analisado nos últimos dias. Se o resultado não chegou, fale com a gente pelo WhatsApp."
    hoje = 0
    for lead in pasta.glob("*/lead.json"):
        try:
            info = json.loads(lead.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if info.get("recebido_em", "").startswith(date.today().isoformat()) and info.get("origem") in ORIGENS_COM_LIMITE:
            hoje += 1
    if hoje >= limite_diario:
        return "Recebemos muitos pedidos hoje. Seu diagnóstico será feito e enviado por e-mail em breve."
    return None


def cmd_automatico(a) -> int:
    dados = Path(a.dados)
    config = Config.do_ambiente()
    config.pasta_relatorios = dados / "relatorios"
    try:
        url = validar_entrada(a.site)
    except UrlInvalida as erro:
        status(dados, a.id, estado="erro", mensagem=f"Endereço não aceito: {erro}.")
        return 0
    bloqueio = verificar_limites(dados, url, a.origem, int(os.environ.get("LIMITE_DIARIO", "20")))
    if bloqueio:
        status(dados, a.id, estado="limite", mensagem=bloqueio)
        if "muitos pedidos" in bloqueio:
            mail.enviar(mail.email_aviso(), f"[Diagnóstico] limite diário atingido: {_host(url)}",
                        mail.corpo(f"O pedido de {e(a.nome or '')} &lt;{e(a.email or '')}&gt; para {e(url)} não foi processado "
                                   "porque o limite diário foi atingido. Rode manualmente pelo GitHub (Run workflow) se quiser atender."))
        return 0

    status(dados, a.id, estado="processando")
    empresa = a.empresa or _host(url)
    r = executar_diagnostico(url, empresa, config)
    pasta = Path(r["pasta"])
    _salvar_json(pasta / "lead.json", {
        "id": a.id, "nome": a.nome, "email": a.email, "whatsapp": a.whatsapp, "empresa": empresa,
        "segmento": a.segmento, "cargo": a.cargo, "origem": a.origem, "site_informado": a.site,
        "recebido_em": datetime.now().isoformat(timespec="seconds"),
    })
    notas = {k: v.nota for k, v in r["notas"].items()}
    rel = pasta.relative_to(dados).as_posix()

    garantir_chave(pasta / "revisao.json")
    try:
        previa = gerar_previa(pasta, config)
    except Exception:  # noqa: BLE001  a prévia ajuda, mas não pode impedir a entrega
        traceback.print_exc()
        previa = None

    enviado = False
    if a.email and a.enviar_ao_lead:
        mail.enviar(a.email, f"Seu resultado técnico: análise do site {_host(url)}",
                    email_lead_automatico(r, a.nome, config.prazo_revisao_dias), [pasta / "relatorio.pdf"], para_lead=True)
        enviado = True
    _salvar_json(pasta / "envio.json", {"automatica_enviada_em": datetime.now().isoformat(timespec="seconds") if enviado else None,
                                        "revisada_enviada_em": None})

    lead = json.loads((pasta / "lead.json").read_text(encoding="utf-8"))
    rev = json.loads((pasta / "revisao.json").read_text(encoding="utf-8"))
    mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa} ({_host(url)}): pronto para a sua revisão",
                email_vania(r, rev, lead, enviado, rel),
                [pasta / "relatorio.pdf"] + ([previa] if previa else []))

    status(dados, a.id, estado="pronto", notas=notas, enviado_por_email=enviado)
    print(f"ok: {rel}")
    return 0


def tentou_aprovar(rev: dict) -> bool:
    blocos = [rev.get("nota_pessoal") or {}, rev.get("plano") or {}, *(rev.get("avaliacoes") or [])]
    return rev.get("aprovar_rascunhos") is True or any(b.get("status") == "revisado" for b in blocos)


def cmd_revisao(a) -> int:
    dados = Path(a.dados)
    config = Config.do_ambiente()
    for arquivo in a.arquivos:
        pasta = (dados / arquivo).parent
        if not (pasta / "dados.json").exists():
            continue
        lead = json.loads((pasta / "lead.json").read_text(encoding="utf-8")) if (pasta / "lead.json").exists() else {}
        rev = json.loads((pasta / "revisao.json").read_text(encoding="utf-8"))
        envio_arq = pasta / "envio.json"
        envio = json.loads(envio_arq.read_text(encoding="utf-8")) if envio_arq.exists() else {}
        empresa = lead.get("empresa") or rev.get("empresa", pasta.name)
        revisar = link_revisar(pasta, rev.get("chave_revisao", ""))
        botao = f'<a href="{e(revisar)}" style="color:#6025E1;font-weight:bold">Abrir a página de revisão</a>'
        try:
            gerar_revisada(pasta, config)
        except RevisaoIncompleta as erro:
            if not tentou_aprovar(rev):
                continue  # ainda é só o rascunho da ferramenta: nada a avisar
            itens = "".join(f"<li>{e(p)}</li>" for p in erro.pendencias)
            mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: falta um detalhe na revisão", mail.corpo(
                "A versão final ainda não foi gerada porque faltou preencher:", f"<ul>{itens}</ul>", botao))
            continue
        pdf = pasta / "relatorio-revisado.pdf"
        if rev.get("enviar_ao_lead") is True and not envio.get("revisada_enviada_em"):
            if rev.get("demonstracao"):
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: NÃO enviado", mail.corpo(
                    "Este diagnóstico está marcado como demonstração. Nada foi enviado ao cliente."))
            elif not lead.get("email"):
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: relatório final pronto", mail.corpo(
                    "O relatório final está pronto (em anexo). Como este diagnóstico não tem e-mail do cliente, "
                    "é você quem envia."), [pdf])
            else:
                mail.enviar(lead["email"], f"Sua avaliação completa: site {_host(rev.get('url', ''))}",
                            email_lead_revisado(empresa, rev.get("url", ""), lead.get("nome", "")), [pdf], para_lead=True)
                envio["revisada_enviada_em"] = datetime.now().isoformat(timespec="seconds")
                _salvar_json(envio_arq, envio)
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: relatório final enviado ao cliente",
                            mail.corpo(f"O relatório final foi enviado para {e(lead['email'])}. A cópia está em anexo."), [pdf])
        else:
            mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: relatório final pronto para conferir", mail.corpo(
                "O relatório final está em anexo, do jeito que o cliente vai receber.",
                ("Ele já foi enviado ao cliente antes." if envio.get("revisada_enviada_em") else
                 f"Se estiver tudo certo, abra a página de revisão e clique em <b>Aprovar e enviar ao cliente</b>. {botao}")), [pdf])
    return 0


def cmd_falha(a) -> int:
    dados = Path(a.dados)
    status(dados, a.id, estado="erro", mensagem="Não conseguimos concluir a análise agora. Vamos verificar e te enviar por e-mail.")
    try:
        mail.enviar(mail.email_aviso(), f"[Diagnóstico] FALHA ao analisar {a.site}", mail.corpo(
            f"A análise de {e(a.site)} falhou. Veja os registros da execução: {e(a.execucao or '')}"))
    except Exception:  # noqa: BLE001
        traceback.print_exc()
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="worker")
    sub = p.add_subparsers(dest="cmd", required=True)
    au = sub.add_parser("automatico")
    au.add_argument("--dados", required=True)
    au.add_argument("--site", required=True)
    au.add_argument("--empresa", default="")
    au.add_argument("--nome", default="")
    au.add_argument("--email", default="")
    au.add_argument("--whatsapp", default="")
    au.add_argument("--segmento", default="")
    au.add_argument("--cargo", default="")
    au.add_argument("--origem", default="prospeccao")
    au.add_argument("--id", default="")
    au.add_argument("--enviar-ao-lead", action="store_true")
    rv = sub.add_parser("revisao")
    rv.add_argument("--dados", required=True)
    rv.add_argument("--arquivos", nargs="*", default=[])
    fa = sub.add_parser("falha")
    fa.add_argument("--dados", required=True)
    fa.add_argument("--id", default="")
    fa.add_argument("--site", default="")
    fa.add_argument("--execucao", default="")
    a = p.parse_args(argv)
    return {"automatico": cmd_automatico, "revisao": cmd_revisao, "falha": cmd_falha}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
