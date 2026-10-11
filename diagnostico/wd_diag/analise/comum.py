"""Utilitários de formatação usados pelas análises."""
from __future__ import annotations

from markupsafe import escape


def esc(texto) -> str:
    """Escapa texto vindo do site analisado (nunca confiar em conteúdo de terceiros)."""
    return str(escape(str(texto)))


def code(texto, limite: int = 120) -> str:
    t = str(texto)
    if len(t) > limite:
        t = t[: limite - 1] + "…"
    return f"<code>{esc(t)}</code>"


def num(valor: float, casas: int = 1) -> str:
    """Número no formato brasileiro (vírgula decimal)."""
    s = f"{valor:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def segundos(ms: float) -> str:
    return num(ms / 1000, 1)


def megabytes(b: float) -> str:
    return num(b / (1024 * 1024), 1)


def pct(parte: float, total: float) -> int:
    return round(100 * parte / total) if total else 0


def plural(n: int, singular: str, plural_: str | None = None) -> str:
    return f"{n} {singular if n == 1 else (plural_ or singular + 's')}"


def caminho(url: str) -> str:
    from urllib.parse import urlsplit
    p = urlsplit(url)
    return (p.path or "/") + (("?" + p.query) if p.query else "")


def lista_curta(itens, limite: int = 4) -> str:
    itens = list(itens)
    mostrados = ", ".join(code(i, 60) for i in itens[:limite])
    resto = len(itens) - limite
    return mostrados + (f" e mais {resto}" if resto > 0 else "")
