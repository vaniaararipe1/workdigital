"""Configuração central. Valores podem ser sobrescritos por variáveis de ambiente ou .env."""
from __future__ import annotations

import glob
import os
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

USER_AGENT = "WorkDigitalDiagnostico/1.0 (+https://workdigital.art.br)"


def carregar_env(caminho: Path = RAIZ / ".env") -> None:
    """Lê um .env simples (CHAVE=valor) sem sobrescrever variáveis já definidas."""
    if not caminho.exists():
        return
    for linha in caminho.read_text(encoding="utf-8").splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("#") or "=" not in linha:
            continue
        chave, valor = linha.split("=", 1)
        os.environ.setdefault(chave.strip(), valor.strip().strip('"').strip("'"))


def _chromium_padrao() -> str | None:
    if os.environ.get("CHROMIUM_PATH"):
        return os.environ["CHROMIUM_PATH"]
    achados = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))
    return achados[-1] if achados else None


@dataclass
class Config:
    pagespeed_api_key: str | None = None
    chromium_path: str | None = None
    usar_lighthouse_local: bool = True
    max_paginas_internas: int = 4
    intervalo_requisicoes: float = 1.0      # segundos entre requisições ao mesmo site
    timeout_http: float = 15.0              # segundos por requisição HTTP
    timeout_pagina: float = 30.0            # segundos para renderizar uma página
    timeout_pagespeed: float = 120.0
    max_bytes_resposta: int = 5 * 1024 * 1024
    max_redirecionamentos: int = 5
    max_links_verificados: int = 40
    portas_permitidas: tuple = (80, 443)
    user_agent: str = USER_AGENT
    prazo_revisao_dias: int = 2             # "chega em até X dias úteis" na versão automática
    pasta_relatorios: Path = field(default_factory=lambda: RAIZ / "relatorios")

    @classmethod
    def do_ambiente(cls) -> "Config":
        carregar_env()
        return cls(
            pagespeed_api_key=os.environ.get("PAGESPEED_API_KEY") or None,
            chromium_path=_chromium_padrao(),
            usar_lighthouse_local=os.environ.get("USAR_LIGHTHOUSE_LOCAL", "1") != "0",
            pasta_relatorios=Path(os.environ.get("PASTA_RELATORIOS", RAIZ / "relatorios")),
            prazo_revisao_dias=int(os.environ.get("PRAZO_REVISAO_DIAS", "2")),
        )
