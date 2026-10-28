"""Envio de e-mails pelo Gmail (SMTP com senha de app).

Variáveis de ambiente:
    GMAIL_USER          conta que envia (ex.: hello@workdigital.art.br, se for Google Workspace)
    GMAIL_APP_PASSWORD  senha de app do Google (não é a senha normal da conta)
    EMAIL_AVISO         para onde vão os avisos internos (padrão: GMAIL_USER)
    EMAIL_RESPONDER_PARA  endereço de resposta nos e-mails ao lead (padrão: hello@workdigital.art.br)
"""
from __future__ import annotations

import mimetypes
import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from html import escape
from pathlib import Path

REMETENTE_NOME = "Vania Araripe · Work Digital"


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


def montar(para: str, assunto: str, html: str, anexos: list[Path] | None = None,
           responder_para: str | None = None, remetente: str = "") -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = formataddr((REMETENTE_NOME, remetente)) if remetente else REMETENTE_NOME
    msg["To"] = para
    msg["Subject"] = assunto
    if responder_para:
        msg["Reply-To"] = responder_para
    texto = (html.replace("<br>", "\n").replace("</p>", "\n\n").replace("</li>", "\n"))
    import re
    msg.set_content(re.sub(r"<[^>]+>", "", texto))
    msg.add_alternative(html, subtype="html")
    for arq in anexos or []:
        tipo, _ = mimetypes.guess_type(arq.name)
        principal, sub = (tipo or "application/octet-stream").split("/", 1)
        msg.add_attachment(arq.read_bytes(), maintype=principal, subtype=sub, filename=arq.name)
    return msg


def enviar(para: str, assunto: str, html: str, anexos: list[Path] | None = None, para_lead: bool = False) -> None:
    cfg = _config()
    msg = montar(para, assunto, html, anexos, cfg["responder_para"] if para_lead else None, cfg["usuario"])
    contexto = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto, timeout=60) as smtp:
        smtp.login(cfg["usuario"], cfg["senha"])
        smtp.send_message(msg)


def email_aviso() -> str:
    return _config()["aviso"]


def corpo(*paragrafos: str) -> str:
    """HTML simples e legível em qualquer leitor de e-mail. Parágrafos já devem vir escapados."""
    p = "".join(f'<p style="margin:0 0 14px">{x}</p>' for x in paragrafos)
    return (f'<div style="font-family:Arial,Helvetica,sans-serif;font-size:15px;line-height:1.55;color:#23232B;max-width:560px">'
            f'{p}<p style="margin:22px 0 0;font-size:13px;color:#5E5D6E">Vania Araripe · Gestão de projetos digitais<br>'
            f'Work Digital · <a href="https://workdigital.art.br" style="color:#6025E1">workdigital.art.br</a> · '
            f'WhatsApp (11) 99391-6363</p></div>')


e = escape  # atalho para escapar dados vindos do formulário
