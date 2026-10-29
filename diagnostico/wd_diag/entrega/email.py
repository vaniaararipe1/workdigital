"""Envio de e-mails pelo Gmail (SMTP com senha de app).

Variáveis de ambiente:
    GMAIL_USER          conta que envia (ex.: hello@workdigital.art.br, se for Google Workspace)
    GMAIL_APP_PASSWORD  senha de app do Google (não é a senha normal da conta)
    EMAIL_AVISO         para onde vão os avisos internos (padrão: GMAIL_USER)
    EMAIL_RESPONDER_PARA  endereço de resposta nos e-mails ao lead (padrão: hello@workdigital.art.br)

Visual: os e-mails com layout ficam em templates/ (HTML com estilos inline, que é o que os leitores de
e-mail aceitam). Logo e foto vão embutidos na mensagem (cid:logo, cid:foto), sem depender de hospedagem.
"""
from __future__ import annotations

import mimetypes
import os
import re
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr, make_msgid
from html import escape
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

AQUI = Path(__file__).parent
REMETENTE_NOME = "Vania Araripe · Work Digital"
IMAGENS = {"logo": AQUI / "assets" / "logo-branco.png", "foto": AQUI / "assets" / "foto-vania.jpg",
           "logo_cor": AQUI / "assets" / "logo-cor.png", "facebook": AQUI / "assets" / "icone-facebook.png",
           "instagram": AQUI / "assets" / "icone-instagram.png", "linkedin": AQUI / "assets" / "icone-linkedin.png"}


class ConfigEmailAusente(RuntimeError):
    pass


def _config() -> dict:
    usuario = os.environ.get("GMAIL_USER", "").strip()
    senha = os.environ.get("GMAIL_APP_PASSWORD", "").replace(" ", "").strip()
    if not usuario or not senha:
        raise ConfigEmailAusente("GMAIL_USER e GMAIL_APP_PASSWORD precisam estar configurados")
    return {
        "usuario": usuario,
        "senha": senha,
        "aviso": os.environ.get("EMAIL_AVISO", "").strip() or usuario,
        "responder_para": os.environ.get("EMAIL_RESPONDER_PARA", "").strip() or "hello@workdigital.art.br",
    }


def assinatura() -> dict:
    """Dados da assinatura. As redes sociais só aparecem quando o endereço estiver configurado."""
    env = lambda k, padrao="": os.environ.get(k, padrao).strip()  # noqa: E731
    redes = [(n, env(f"ASSINATURA_{n.upper()}")) for n in ("facebook", "instagram", "linkedin")]
    return {"nome": env("ASSINATURA_NOME", "Vania Araripe"),
            "cargo": env("ASSINATURA_CARGO", "Gestão de projetos digitais"),
            "funcao": env("ASSINATURA_FUNCAO", "Projetos"),
            "telefone": env("ASSINATURA_TELEFONE", "(11) 99391-6363"),
            "email": env("ASSINATURA_EMAIL", "vania@workdigital.art.br"),
            "redes": [{"nome": n, "url": u} for n, u in redes if u.startswith("https://")]}


def renderizar(template: str, **ctx) -> str:
    """HTML de um e-mail com layout (templates/*.html.j2). Dados do lead são escapados automaticamente."""
    env = Environment(loader=FileSystemLoader(AQUI / "templates"), autoescape=select_autoescape(["html", "j2"]),
                      trim_blocks=True, lstrip_blocks=True)
    return env.get_template(template).render(assinatura=assinatura(), **ctx)


def _texto_puro(html: str) -> str:
    t = re.sub(r"(?is)<(style|title)[^>]*>.*?</\1>", "", html)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</tr>|</h\d>|</li>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"&nbsp;", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n\n", t).strip()


def montar(para: str, assunto: str, html: str, anexos: list[Path] | None = None,
           responder_para: str | None = None, remetente: str = "") -> EmailMessage:
    from html import unescape
    msg = EmailMessage()
    msg["From"] = formataddr((REMETENTE_NOME, remetente)) if remetente else REMETENTE_NOME
    msg["To"] = para
    msg["Subject"] = assunto
    if responder_para:
        msg["Reply-To"] = responder_para
    padrao = {n: re.compile(rf"cid:{n}(?!\w)") for n in IMAGENS}  # "cid:logo" não pode casar com "cid:logo_cor"
    usadas = {n: p for n, p in IMAGENS.items() if padrao[n].search(html) and p.exists()}
    cids = {n: make_msgid(domain="workdigital.art.br") for n in usadas}
    for n, cid in cids.items():
        html = padrao[n].sub("cid:" + cid[1:-1], html)
    msg.set_content(unescape(_texto_puro(html)))
    msg.add_alternative(html, subtype="html")
    parte_html = msg.get_payload()[-1]
    for n, caminho in usadas.items():
        tipo, _ = mimetypes.guess_type(caminho.name)
        principal, sub = (tipo or "image/png").split("/", 1)
        parte_html.add_related(caminho.read_bytes(), maintype=principal, subtype=sub, cid=cids[n],
                               disposition="inline", filename=caminho.name)
    for arq in anexos or []:
        tipo, _ = mimetypes.guess_type(arq.name)
        principal, sub = (tipo or "application/octet-stream").split("/", 1)
        msg.add_attachment(arq.read_bytes(), maintype=principal, subtype=sub, filename=arq.name)
    return msg


def enviar(para: str, assunto: str, html: str, anexos: list[Path] | None = None, para_lead: bool = False) -> None:
    cfg = _config()
    msg = montar(para, assunto, html, [a for a in (anexos or []) if a.exists()],
                 cfg["responder_para"] if para_lead else None, cfg["usuario"])
    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto, timeout=60) as smtp:
        smtp.login(cfg["usuario"], cfg["senha"])
        smtp.send_message(msg)


def email_aviso() -> str:
    return _config()["aviso"]


def corpo(*paragrafos: str) -> str:
    """HTML simples para avisos internos curtos. Parágrafos já devem vir escapados."""
    p = "".join(f'<p style="margin:0 0 14px">{x}</p>' for x in paragrafos)
    return (f'<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;color:#23232B;max-width:560px">'
            f'{p}<p style="margin:22px 0 0;font-size:13px;color:#5E5D6E">Vania Araripe · Gestão de projetos digitais<br>'
            f'Work Digital · <a href="https://workdigital.art.br" style="color:#6025E1">workdigital.art.br</a> · '
            f'WhatsApp (11) 99391-6363</p></div>')


e = escape  # atalho para escapar dados vindos do formulário
