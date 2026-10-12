"""Validação de URLs: só http/https, só hosts públicos, sem credenciais e portas estranhas.

Toda URL que a ferramenta acessa (inclusive cada salto de redirecionamento e cada
requisição feita pelo navegador) passa por `verificar_url`.
"""
from __future__ import annotations

import ipaddress
import socket
from functools import lru_cache
from urllib.parse import urlsplit, urlunsplit

ESQUEMAS = ("http", "https")
PORTAS_PADRAO = (80, 443)
HOSTS_BLOQUEADOS = {"localhost", "localhost.localdomain", "ip6-localhost", "ip6-loopback"}
SUFIXOS_BLOQUEADOS = (".localhost", ".local", ".internal", ".lan", ".home.arpa", ".intranet")


class UrlInvalida(ValueError):
    """URL recusada por formato ou por apontar para rede interna."""


def ip_e_publico(ip: str) -> bool:
    try:
        end = ipaddress.ip_address(ip)
    except ValueError:
        return False
    if isinstance(end, ipaddress.IPv6Address) and end.ipv4_mapped:
        end = end.ipv4_mapped
    return end.is_global and not end.is_multicast


@lru_cache(maxsize=512)
def resolver(host: str) -> tuple[str, ...]:
    try:
        infos = socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP)
    except socket.gaierror as e:
        raise UrlInvalida(f"não foi possível encontrar o endereço {host}") from e
    return tuple(sorted({i[4][0] for i in infos}))


def normalizar(url: str) -> str:
    """Completa o esquema (https) e remove espaços. Não faz validação de rede."""
    url = (url or "").strip()
    if not url:
        raise UrlInvalida("URL vazia")
    if "://" not in url:
        url = "https://" + url
    return url


def verificar_url(url: str, portas: tuple = PORTAS_PADRAO, resolver_dns=resolver) -> str:
    """Valida a URL e devolve a forma normalizada. Lança UrlInvalida se recusada."""
    partes = urlsplit(url)
    esquema = partes.scheme.lower()
    if esquema not in ESQUEMAS:
        raise UrlInvalida(f"apenas http e https são aceitos (recebido: {esquema or 'nenhum'})")
    if partes.username or partes.password:
        raise UrlInvalida("URLs com usuário ou senha não são aceitas")
    host = (partes.hostname or "").rstrip(".").lower()
    if not host:
        raise UrlInvalida("URL sem domínio")
    try:
        porta = partes.port
    except ValueError as e:
        raise UrlInvalida("porta inválida") from e
    if porta is not None and porta not in portas:
        raise UrlInvalida(f"porta {porta} não permitida")
    if host in HOSTS_BLOQUEADOS or host.endswith(SUFIXOS_BLOQUEADOS):
        raise UrlInvalida(f"o endereço {host} é de rede interna")

    try:
        ipaddress.ip_address(host)
        ips = (host,)
    except ValueError:
        if "." not in host:
            raise UrlInvalida(f"domínio incompleto: {host}")
        ips = resolver_dns(host)
    if not ips:
        raise UrlInvalida(f"não foi possível encontrar o endereço {host}")
    for ip in ips:
        if not ip_e_publico(ip):
            raise UrlInvalida(f"o endereço {host} aponta para rede interna ({ip})")

    netloc = host if porta is None else f"{host}:{porta}"
    return urlunsplit((esquema, netloc, partes.path or "/", partes.query, ""))


def validar_entrada(url: str, **kw) -> str:
    """Ponto de entrada para a URL informada pelo usuário/formulário."""
    return verificar_url(normalizar(url), **kw)


def host_permitido(url: str, cache: dict | None = None) -> bool:
    """Versão booleana e com cache, usada para filtrar requisições do navegador."""
    partes = urlsplit(url)
    if partes.scheme in ("data", "blob", "about"):
        return True
    chave = (partes.scheme, partes.hostname, partes.port)
    if cache is not None and chave in cache:
        return cache[chave]
    try:
        verificar_url(url)
        ok = True
    except UrlInvalida:
        ok = False
    if cache is not None:
        cache[chave] = ok
    return ok
