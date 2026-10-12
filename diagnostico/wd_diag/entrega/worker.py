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
import sys
import traceback
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlsplit

from ..config import Config
from ..pipeline import executar_diagnostico, gerar_revisada, nome_pasta
from ..revisao import RevisaoIncompleta
from ..seguranca import UrlInvalida, validar_entrada
from . import email as mail
from .email import e

ORIGENS_COM_LIMITE = ("popup", "landing", "site")
REPO = os.environ.get("GITHUB_REPOSITORY", "")
BRANCH_DADOS = os.environ.get("BRANCH_DADOS", "relatorios")


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


def _link_github(caminho: str, editar: bool = False) -> str:
    if not REPO:
        return caminho
    modo = "edit" if editar else "blob"
    return f"https://github.com/{REPO}/{modo}/{BRANCH_DADOS}/{caminho}"


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

    enviado = False
    if a.email and a.enviar_ao_lead:
        mail.enviar(a.email, f"Seu resultado técnico: análise do site {_host(url)}", mail.corpo(
            f"Olá{(' ' + e(a.nome.split()[0])) if a.nome else ''}!",
            f"Segue em anexo o resultado técnico da análise do site <b>{e(url)}</b>. Ele traz o que medimos "
            "automaticamente: velocidade, experiência de quem visita e como o Google e as buscas com IA encontram o site.",
            f"A avaliação completa, revisada por mim, chega em até {config.prazo_revisao_dias} dias úteis, com as "
            "prioridades e um plano de ação.",
            "Qualquer dúvida, é só responder este e-mail.",
        ), [pasta / "relatorio.pdf"], para_lead=True)
        enviado = True
    _salvar_json(pasta / "envio.json", {"automatica_enviada_em": datetime.now().isoformat(timespec="seconds") if enviado else None,
                                        "revisada_enviada_em": None})

    contato = " · ".join(x for x in (a.nome, a.email, a.whatsapp) if x) or "sem dados de contato (prospecção)"
    mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa} ({_host(url)}) pronto para revisão", mail.corpo(
        f"<b>{e(empresa)}</b> · {e(url)}<br>Origem: {e(a.origem)} · Contato: {e(contato)}",
        f"Notas: performance {notas['performance']}, experiência e conversão {notas['ux']}, SEO e visibilidade {notas['seo']}.",
        ("A versão automática <b>já foi enviada ao lead</b>." if enviado else "A versão automática <b>não</b> foi enviada ao lead."),
        f'Para revisar: <a href="{_link_github(rel + "/revisao.json", editar=True)}">abrir o revisao.json para edição</a>. '
        "Ao salvar, a versão revisada é gerada e chega aqui para você conferir. Para enviá-la ao lead, troque "
        "<code>enviar_ao_lead</code> para <code>true</code>.",
        f'Pasta completa: <a href="{_link_github(rel)}">{e(rel)}</a>. Em anexo: versão automática e notas internas.',
    ), [pasta / "relatorio.pdf", pasta / "notas-internas.html"])

    status(dados, a.id, estado="pronto", notas=notas, enviado_por_email=enviado)
    print(f"ok: {rel}")
    return 0


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
        try:
            gerar_revisada(pasta, config)
        except RevisaoIncompleta as erro:
            itens = "".join(f"<li>{e(p)}</li>" for p in erro.pendencias)
            mail.enviar(mail.email_aviso(), f"[Diagnóstico] revisão de {empresa}: ainda falta", mail.corpo(
                "A versão revisada ainda não foi gerada. Falta:", f"<ul>{itens}</ul>",
                f'<a href="{_link_github(pasta.relative_to(dados).as_posix() + "/revisao.json", editar=True)}">Abrir o revisao.json</a>'))
            continue
        pdf = pasta / "relatorio-revisado.pdf"
        if rev.get("enviar_ao_lead") is True and not envio.get("revisada_enviada_em"):
            if rev.get("demonstracao"):
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: NÃO enviado", mail.corpo(
                    "O revisao.json está marcado como demonstração. Nada foi enviado ao lead."))
            elif not lead.get("email"):
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: sem e-mail do lead", mail.corpo(
                    "A versão revisada está pronta (em anexo), mas não há e-mail do lead. Envie você mesma."), [pdf])
            else:
                nome = (lead.get("nome") or "").split()
                mail.enviar(lead["email"], f"Sua avaliação completa: site {_host(rev.get('url', ''))}", mail.corpo(
                    f"Olá{(' ' + e(nome[0])) if nome else ''}!",
                    "Como combinado, segue em anexo a avaliação completa do seu site, revisada por mim, com as prioridades "
                    "e um plano de ação em ordem de impacto.",
                    "Se quiser, a gente conversa 30 minutos para eu te mostrar por onde começar. É só responder este e-mail "
                    "ou chamar no WhatsApp (11) 99391-6363.",
                ), [pdf], para_lead=True)
                envio["revisada_enviada_em"] = datetime.now().isoformat(timespec="seconds")
                _salvar_json(envio_arq, envio)
                mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: versão revisada enviada ao lead",
                            mail.corpo(f"Enviada para {e(lead['email'])}."), [pdf])
        else:
            mail.enviar(mail.email_aviso(), f"[Diagnóstico] {empresa}: versão revisada pronta para conferir", mail.corpo(
                "A versão revisada foi gerada (em anexo).",
                ("Ela já foi enviada ao lead antes." if envio.get("revisada_enviada_em") else
                 "Para enviá-la ao lead, troque <code>enviar_ao_lead</code> para <code>true</code> no revisao.json e salve.")), [pdf])
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
