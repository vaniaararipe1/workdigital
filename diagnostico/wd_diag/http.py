"""Cliente HTTP educado: user-agent identificado, intervalo entre requisições,
timeout, limite de tamanho e validação de cada salto de redirecionamento."""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from urllib.parse import urljoin, urlsplit
from urllib.robotparser import RobotFileParser

import requests

from .config import Config
from .seguranca import UrlInvalida, verificar_url


@dataclass
class Resposta:
    url: str
    url_final: str | None = None
    status: int | None = None
    headers: dict = field(default_factory=dict)
    texto: str = ""
    redirecionamentos: list = field(default_factory=list)   # [(status, url_origem, url_destino)]
    erro: str | None = None
    truncado: bool = False
    tempo_ms: int | None = None

    @property
    def ok(self) -> bool:
        return self.erro is None and self.status is not None and 200 <= self.status < 300


class ClienteHTTP:
    def __init__(self, config: Config):
        self.config = config
        self.sessao = requests.Session()
        self.sessao.headers.update({
            "User-Agent": config.user_agent,
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.5",
        })
        self._ultimo: dict[str, float] = {}
        self._robots: dict[str, RobotFileParser | None] = {}
        self.log: list[dict] = []

    # ---------- educação ----------
    def _aguardar(self, host: str) -> None:
        anterior = self._ultimo.get(host)
        if anterior is not None:
            espera = self.config.intervalo_requisicoes - (time.monotonic() - anterior)
            if espera > 0:
                time.sleep(espera)
        self._ultimo[host] = time.monotonic()

    def robots(self, url: str) -> RobotFileParser | None:
        """Retorna o robots.txt do site (ou None se não existe/indisponível)."""
        p = urlsplit(url)
        base = f"{p.scheme}://{p.netloc}"
        if base not in self._robots:
            r = self.get(base + "/robots.txt", checar_robots=False)
            parser = None
            if r.ok and "html" not in r.headers.get("content-type", "").lower():
                parser = RobotFileParser()
                parser.parse(r.texto.splitlines())
            self._robots[base] = parser
            self._robots[base + "#resposta"] = r  # type: ignore[assignment]
        return self._robots[base]

    def resposta_robots(self, url: str) -> Resposta:
        p = urlsplit(url)
        self.robots(url)
        return self._robots[f"{p.scheme}://{p.netloc}#resposta"]  # type: ignore[return-value]

    def permitido(self, url: str) -> bool:
        parser = self.robots(url)
        if parser is None:
            return True
        return parser.can_fetch(self.config.user_agent, url)

    # ---------- requisição ----------
    def get(self, url: str, checar_robots: bool = True, metodo: str = "GET",
            max_bytes: int | None = None) -> Resposta:
        resp = Resposta(url=url)
        limite = max_bytes or self.config.max_bytes_resposta
        atual = url
        inicio = time.monotonic()
        try:
            if checar_robots and not self.permitido(url):
                resp.erro = "bloqueado pelo robots.txt do site"
                return resp
            for _ in range(self.config.max_redirecionamentos + 1):
                verificar_url(atual, portas=self.config.portas_permitidas)
                self._aguardar(urlsplit(atual).netloc)
                r = self.sessao.request(metodo, atual, allow_redirects=False, stream=True,
                                        timeout=self.config.timeout_http)
                if r.is_redirect and r.headers.get("location"):
                    destino = urljoin(atual, r.headers["location"])
                    resp.redirecionamentos.append((r.status_code, atual, destino))
                    r.close()
                    atual = destino
                    continue
                resp.status = r.status_code
                resp.url_final = atual
                resp.headers = {k.lower(): v for k, v in r.headers.items()}
                if metodo != "HEAD":
                    corpo = bytearray()
                    for bloco in r.iter_content(64 * 1024):
                        corpo.extend(bloco)
                        if len(corpo) > limite:
                            resp.truncado = True
                            break
                    r.close()
                    resp.texto = bytes(corpo[:limite]).decode(r.encoding or "utf-8", errors="replace")
                else:
                    r.close()
                break
            else:
                resp.erro = "redirecionamentos demais"
        except UrlInvalida as e:
            resp.erro = f"endereço recusado: {e}"
        except requests.Timeout:
            resp.erro = "tempo esgotado"
        except requests.RequestException as e:
            resp.erro = f"falha de conexão: {type(e).__name__}"
        resp.tempo_ms = int((time.monotonic() - inicio) * 1000)
        self.log.append({"url": url, "metodo": metodo, "status": resp.status,
                         "erro": resp.erro, "ms": resp.tempo_ms})
        return resp
