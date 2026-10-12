"""Descoberta das páginas internas relevantes (menu, sitemap e links da home)."""
from __future__ import annotations

import re
from urllib.parse import urljoin, urlsplit, urlunsplit

from bs4 import BeautifulSoup

PALAVRAS_RELEVANTES = {
    "contato": 10, "fale-conosco": 10, "orcamento": 9, "servico": 8, "servicos": 8,
    "solucoes": 7, "sobre": 7, "quem-somos": 7, "empresa": 5, "produto": 6, "produtos": 6,
    "portfolio": 6, "cases": 6, "clientes": 5, "precos": 6, "planos": 6, "cardapio": 6,
    "atendimento": 5, "agendamento": 6, "loja": 4, "blog": 2,
}
IGNORAR_CAMINHO = re.compile(
    r"/(wp-admin|wp-login|wp-json|login|entrar|cadastro|minha-conta|my-account|account|cart|carrinho|"
    r"checkout|finalizar|feed|tag|author|autor|category|categoria|page/\d+|search|busca|privacidade|"
    r"politica|termos|cookies|lgpd)(/|$)", re.I)
IGNORAR_EXTENSAO = re.compile(r"\.(pdf|jpe?g|png|gif|webp|svg|zip|rar|docx?|xlsx?|pptx?|mp4|mp3|xml|txt|css|js)$", re.I)


def mesmo_site(a: str, b: str) -> bool:
    ha = (urlsplit(a).hostname or "").removeprefix("www.")
    hb = (urlsplit(b).hostname or "").removeprefix("www.")
    return ha == hb and ha != ""


def limpar(url: str) -> str:
    p = urlsplit(url)
    caminho = p.path or "/"
    return urlunsplit((p.scheme, p.netloc.lower(), caminho, p.query, ""))


def chave_caminho(url: str) -> str:
    p = urlsplit(url)
    return (p.path.rstrip("/") or "/").lower() + ("?" + p.query if p.query else "")


def candidata(url: str, base: str) -> bool:
    p = urlsplit(url)
    if p.scheme not in ("http", "https") or not mesmo_site(url, base):
        return False
    if IGNORAR_CAMINHO.search(p.path) or IGNORAR_EXTENSAO.search(p.path):
        return False
    if "add-to-cart" in p.query or "replytocom" in p.query:
        return False
    return chave_caminho(url) != chave_caminho(base)


def links_do_html(html: str, base: str) -> tuple[list[str], list[str]]:
    """Retorna (links do menu/cabeçalho, demais links) já absolutos e limpos."""
    sopa = BeautifulSoup(html, "html.parser")
    menu, outros = [], []
    for a in sopa.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "whatsapp:")):
            continue
        absoluto = limpar(urljoin(base, href))
        no_menu = a.find_parent(["nav", "header"]) is not None or a.find_parent(
            attrs={"role": "navigation"}) is not None or a.find_parent(
            class_=re.compile(r"(^|[-_ ])(menu|nav|navbar|header)([-_ ]|$)", re.I)) is not None
        (menu if no_menu else outros).append(absoluto)
    return menu, outros


def urls_do_sitemap(xml: str) -> list[str]:
    return [u.strip() for u in re.findall(r"<loc>\s*(.*?)\s*</loc>", xml, re.I | re.S)]


def pontuar(url: str, no_menu: bool, no_sitemap: bool) -> float:
    caminho = urlsplit(url).path.lower()
    partes = [p for p in re.split(r"[/_.]", caminho) if p]
    pontos = 0.0
    for palavra, peso in PALAVRAS_RELEVANTES.items():
        if any(palavra == p or p.startswith(palavra) or palavra in p for p in partes):
            pontos = max(pontos, peso)
    pontos += 5 if no_menu else 0
    pontos += 1 if no_sitemap else 0
    pontos -= 0.5 * max(0, len(partes) - 1)   # prefere páginas de primeiro nível
    return pontos


def escolher_paginas(base: str, html_home: str, sitemap_urls: list[str], maximo: int = 4) -> list[dict]:
    """Escolhe até `maximo` páginas internas, com a origem de cada uma."""
    menu, outros = links_do_html(html_home, base)
    candidatos: dict[str, dict] = {}

    def registrar(url: str, origem: str):
        if not candidata(url, base):
            return
        k = chave_caminho(url)
        c = candidatos.setdefault(k, {"url": url, "origens": set()})
        c["origens"].add(origem)

    for u in menu:
        registrar(u, "menu")
    for u in sitemap_urls[:500]:
        registrar(limpar(u), "sitemap")
    for u in outros:
        registrar(u, "link")

    ordenados = sorted(
        candidatos.values(),
        key=lambda c: (-pontuar(c["url"], "menu" in c["origens"], "sitemap" in c["origens"]), len(c["url"])),
    )
    return [{"url": c["url"], "origem": ", ".join(sorted(c["origens"]))} for c in ordenados[:maximo]]


CONTATO_RE = re.compile(r"(contato|contate|fale[- ]?conosco|fale[- ]com|atendimento|or[çc]amento|contact)", re.I)
CONTATO_PADRAO = ("/contato/", "/fale-conosco/")


def paginas_de_contato(base: str, html_home: str, maximo: int = 3) -> list[dict]:
    """Páginas de contato a visitar explicitamente: links do menu e do rodapé com cara de contato,
    mais os endereços padrão /contato/ e /fale-conosco/ (que podem não existir)."""
    sopa = BeautifulSoup(html_home or "", "html.parser")
    achadas: dict[str, dict] = {}
    for a in sopa.find_all("a", href=True):
        href = a["href"].strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "whatsapp:")):
            continue
        absoluto = limpar(urljoin(base, href))
        p = urlsplit(absoluto)
        if p.scheme not in ("http", "https") or not mesmo_site(absoluto, base) or chave_caminho(absoluto) == chave_caminho(base):
            continue
        texto = a.get_text(" ", strip=True)
        if not (CONTATO_RE.search(p.path) or CONTATO_RE.search(texto)):
            continue
        local = "rodapé" if a.find_parent("footer") is not None else (
            "menu" if a.find_parent(["nav", "header"]) is not None else "link da página inicial")
        achadas.setdefault(chave_caminho(absoluto), {"url": absoluto, "origem": local})
    for caminho in CONTATO_PADRAO:
        u = limpar(urljoin(base, caminho))
        achadas.setdefault(chave_caminho(u), {"url": u, "origem": "endereço padrão"})
    return list(achadas.values())[:maximo + len(CONTATO_PADRAO)]
