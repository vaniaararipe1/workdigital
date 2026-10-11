"""Coleta via HTTP: robots.txt, sitemap, llms.txt, HTTPS, redirecionamentos e links quebrados."""
from __future__ import annotations

import re
from urllib.parse import urlsplit, urlunsplit

from ..http import ClienteHTTP
from ..rastreador import urls_do_sitemap


def _base(url: str) -> str:
    p = urlsplit(url)
    return f"{p.scheme}://{p.netloc}"


def coletar_robots(cliente: ClienteHTTP, url: str) -> dict:
    parser = cliente.robots(url)
    r = cliente.resposta_robots(url)
    eh_texto = r.ok and "html" not in r.headers.get("content-type", "").lower()
    sitemaps = re.findall(r"(?im)^\s*sitemap:\s*(\S+)", r.texto) if eh_texto else []
    return {
        "url": _base(url) + "/robots.txt",
        "status": r.status,
        "erro": r.erro,
        "existe": bool(eh_texto),
        "sitemaps_declarados": sitemaps,
        "bloqueia_buscadores": bool(parser is not None and not parser.can_fetch("Googlebot", _base(url) + "/")),
        "permite_home": cliente.permitido(url),
        "conteudo": r.texto[:3000] if eh_texto else "",
    }


def coletar_sitemap(cliente: ClienteHTTP, url: str, declarados: list[str]) -> dict:
    tentativas = list(dict.fromkeys(declarados + [_base(url) + "/sitemap.xml", _base(url) + "/sitemap_index.xml"]))
    for alvo in tentativas[:4]:
        r = cliente.get(alvo, checar_robots=False, max_bytes=3 * 1024 * 1024)
        if not (r.ok and "<loc>" in r.texto.lower()):
            continue
        urls = urls_do_sitemap(r.texto)
        filhos = [u for u in urls if re.search(r"sitemap.*\.xml", u, re.I)]
        paginas = [u for u in urls if u not in filhos]
        for filho in filhos[:3]:
            rf = cliente.get(filho, checar_robots=False, max_bytes=3 * 1024 * 1024)
            if rf.ok:
                paginas += [u for u in urls_do_sitemap(rf.texto) if not u.lower().endswith(".xml")]
        return {"existe": True, "url": alvo, "total_urls": len(paginas), "urls": paginas[:500],
                "erro": None}
    return {"existe": False, "url": tentativas[0], "total_urls": 0, "urls": [], "erro": None,
            "tentativas": tentativas[:4]}


def coletar_llms(cliente: ClienteHTTP, url: str) -> dict:
    alvo = _base(url) + "/llms.txt"
    r = cliente.get(alvo, checar_robots=False, max_bytes=512 * 1024)
    existe = bool(r.ok and "html" not in r.headers.get("content-type", "").lower() and r.texto.strip())
    return {"url": alvo, "existe": existe, "status": r.status, "erro": r.erro}


def coletar_https(cliente: ClienteHTTP, url_final: str) -> dict:
    """Verifica se a versão http:// redireciona para https://."""
    p = urlsplit(url_final)
    http_url = urlunsplit(("http", p.netloc, "/", "", ""))
    r = cliente.get(http_url, checar_robots=False, metodo="GET", max_bytes=256 * 1024)
    destino = r.url_final or ""
    return {
        "url_testada": http_url,
        "redireciona_para_https": destino.startswith("https://"),
        "destino": destino,
        "redirecionamentos": r.redirecionamentos,
        "erro": r.erro,
    }


def verificar_links(cliente: ClienteHTTP, links: list[str], maximo: int) -> dict:
    """Confere até `maximo` links internos. Usa HEAD e, se o servidor recusar, GET."""
    unicos = list(dict.fromkeys(links))
    verificados, quebrados, falhas = [], [], []
    for link in unicos[:maximo]:
        r = cliente.get(link, metodo="HEAD")
        if r.status in (405, 403, 501) or (r.erro and "robots" not in r.erro):
            r = cliente.get(link, max_bytes=64 * 1024)
        if r.erro and "robots" in r.erro:
            continue
        verificados.append({"url": link, "status": r.status, "erro": r.erro})
        if r.status in (404, 410):
            quebrados.append({"url": link, "status": r.status})
        elif r.erro or (r.status and r.status >= 500):
            falhas.append({"url": link, "status": r.status, "erro": r.erro})
    return {"total_encontrados": len(unicos), "verificados": len(verificados),
            "quebrados": quebrados, "falhas": falhas}
