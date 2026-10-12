"""Renderiza o relatório (HTML e PDF) a partir de um contexto já calculado."""
from __future__ import annotations

import base64
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

AQUI = Path(__file__).parent
ASSETS = AQUI / "assets"

MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


def data_extenso(d: date) -> str:
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def _data_uri(caminho: Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(caminho.read_bytes()).decode()


def assets_embutidos() -> dict:
    """Logo e mascote embutidos no HTML, para o arquivo funcionar sozinho."""
    return {
        "logo_branco": _data_uri(ASSETS / "logo-workdigital-branco.svg", "image/svg+xml"),
        "logo": _data_uri(ASSETS / "logo-workdigital.svg", "image/svg+xml"),
        "mascote_svg": (ASSETS / "mascote.svg").read_text(),
        "foto": _data_uri(ASSETS / "foto-assinatura.webp", "image/webp"),
    }


WHATSAPP_NUMERO = "5511993916363"


def link_whatsapp(empresa: str | None) -> str:
    from urllib.parse import quote
    msg = (f"Olá! Recebi o diagnóstico do site da {empresa} e quero conversar sobre os próximos passos."
           if empresa else "Olá! Recebi o diagnóstico do meu site e quero conversar sobre os próximos passos.")
    return f"https://wa.me/{WHATSAPP_NUMERO}?text={quote(msg)}"


def qr_svg(url: str) -> str | None:
    """QR code em SVG (para quem lê o PDF impresso). Retorna None se a biblioteca não estiver instalada."""
    try:
        import qrcode
        import qrcode.image.svg
    except ImportError:
        return None
    img = qrcode.make(url, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=1)
    svg = img.to_string(encoding="unicode")
    return svg[svg.index("<svg"):]


def _env() -> Environment:
    return Environment(
        loader=FileSystemLoader(AQUI / "templates"),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def renderizar_html(contexto: dict, template: str = "relatorio.html.j2") -> str:
    import os
    ctx = {"assets": assets_embutidos(), "exemplo": False,
           "assinatura": {"nome": os.environ.get("ASSINATURA_NOME", "Vania Araripe").strip(),
                          "cargo": os.environ.get("ASSINATURA_CARGO", "Gestão de projetos digitais").strip()},
           **contexto}
    if "whatsapp_url" not in ctx:
        ctx["whatsapp_url"] = link_whatsapp(ctx.get("empresa"))
        ctx["qr_svg"] = qr_svg(ctx["whatsapp_url"])
    return _env().get_template(template).render(**ctx)


def html_para_pdf(caminho_html: Path, caminho_pdf: Path, executavel: str | None = None) -> None:
    """Imprime o HTML em PDF A4 com o Chromium do Playwright (tema claro via @media print)."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=executavel) if executavel else p.chromium.launch()
        try:
            page = browser.new_page()
            page.goto(caminho_html.resolve().as_uri(), wait_until="networkidle", timeout=60_000)
            page.evaluate("document.fonts.ready")
            page.emulate_media(media="print")
            page.pdf(path=str(caminho_pdf), format="A4", print_background=True,
                     prefer_css_page_size=True)
        finally:
            browser.close()
