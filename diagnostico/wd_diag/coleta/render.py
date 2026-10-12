"""Renderização com Playwright (Chromium): HTML final, medições no DOM e capturas de tela.

Segurança: toda requisição feita pelo navegador passa por `host_permitido`;
endereços de rede interna são abortados. Vídeos e áudios não são baixados.
"""
from __future__ import annotations

import time
from pathlib import Path

from ..config import Config
from ..seguranca import host_permitido

MEDIR_JS = (Path(__file__).parent / "medir.js").read_text(encoding="utf-8")

DESKTOP = {"viewport": {"width": 1366, "height": 768}, "device_scale_factor": 1}
MOBILE = {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 2, "is_mobile": True, "has_touch": True}
UA_CHROME_DESKTOP = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/141.0.0.0 Safari/537.36")
UA_CHROME_MOBILE = ("Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/141.0.0.0 Mobile Safari/537.36")


class Renderizador:
    """Mantém um navegador aberto durante o diagnóstico inteiro."""

    def __init__(self, config: Config):
        self.config = config
        self._pw = None
        self._browser = None
        self._cache_hosts: dict = {}
        self.bloqueados: list[str] = []
        self._ultimo = 0.0

    def __enter__(self):
        from playwright.sync_api import sync_playwright
        self._pw = sync_playwright().start()
        kw = {"executable_path": self.config.chromium_path} if self.config.chromium_path else {}
        self._browser = self._pw.chromium.launch(**kw)
        return self

    def __exit__(self, *exc):
        try:
            if self._browser:
                self._browser.close()
        finally:
            if self._pw:
                self._pw.stop()

    def _rota(self, route):
        req = route.request
        if req.resource_type in ("media", "websocket", "eventsource"):
            return route.abort()
        if not host_permitido(req.url, self._cache_hosts):
            self.bloqueados.append(req.url[:200])
            return route.abort()
        return route.continue_()

    def renderizar(self, url: str, dispositivo: str = "desktop", captura: Path | None = None,
                   medir: bool = True) -> dict:
        perfil = MOBILE if dispositivo == "mobile" else DESKTOP
        ua = (UA_CHROME_MOBILE if dispositivo == "mobile" else UA_CHROME_DESKTOP) + " " + self.config.user_agent
        espera = self.config.intervalo_requisicoes - (time.monotonic() - self._ultimo)
        if espera > 0:
            time.sleep(espera)
        self._ultimo = time.monotonic()

        resultado = {"url": url, "dispositivo": dispositivo, "erro": None}
        contexto = self._browser.new_context(user_agent=ua, locale="pt-BR", ignore_https_errors=False,
                                             java_script_enabled=True, **perfil)
        contexto.route("**/*", self._rota)
        pagina = contexto.new_page()
        pagina.set_default_timeout(self.config.timeout_pagina * 1000)
        try:
            inicio = time.monotonic()
            resposta = pagina.goto(url, wait_until="domcontentloaded", timeout=self.config.timeout_pagina * 1000)
            try:
                pagina.wait_for_load_state("networkidle", timeout=8000)
            except Exception:
                pass  # sites com conexões abertas (chat, analytics) nunca ficam "ociosos"
            pagina.wait_for_timeout(800)
            resultado["status"] = resposta.status if resposta else None
            resultado["url_final"] = pagina.url
            resultado["tempo_carregamento_ms"] = int((time.monotonic() - inicio) * 1000)
            resultado["html"] = pagina.content()
            resultado["titulo"] = pagina.title()
            if medir:
                pagina.evaluate("window.scrollTo(0, 0)")
                resultado["medidas"] = pagina.evaluate(MEDIR_JS)
            if captura:
                captura.parent.mkdir(parents=True, exist_ok=True)
                pagina.screenshot(path=str(captura), type="jpeg", quality=72)
                resultado["captura"] = str(captura)
        except Exception as e:  # noqa: BLE001 - o relatório precisa registrar qualquer falha
            msg = str(e).splitlines()[0][:200]
            resultado["erro"] = "tempo esgotado ao abrir a página" if "Timeout" in msg else f"falha ao abrir a página: {msg}"
        finally:
            contexto.close()
        return resultado
