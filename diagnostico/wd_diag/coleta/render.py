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

# Conta elementos e texto do corpo; usado para saber quando a página parou de mudar.
ASSINATURA_DOM_JS = "() => document.getElementsByTagName('*').length + ':' + (document.body ? document.body.innerText.length : 0)"

# Marca o botão que abre formulário (achado pelo texto e href que o medir.js devolveu) para clicar nele.
MARCAR_GATILHO_JS = """(g) => {
  const vis = (el) => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    return r.width >= 2 && r.height >= 2 && s.visibility !== 'hidden' && s.display !== 'none'; };
  const texto = (el) => (el.innerText || el.value || el.getAttribute('aria-label') || el.title || '').replace(/\\s+/g, ' ').trim().slice(0, 60);
  const el = [...document.querySelectorAll('a, button, [role=button]')].filter(vis)
    .find(el => texto(el) === g.texto && (el.getAttribute('href') || '').slice(0, 80) === g.href && !el.closest('form'));
  if (!el) return false;
  el.setAttribute('data-wd-diag-gatilho', '1');
  return true;
}"""


def _tem_formulario(m: dict) -> bool:
    return bool(any(f["campos"] >= 2 for f in m.get("formularios", [])) or m.get("formularios_externos")
                or m.get("formularios_provedor") or m.get("links_formulario") or m.get("campos_soltos", 0) >= 2)

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
        self.interceptar = None   # testes: função(contexto) que registra rotas falsas

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
        if self.interceptar:
            self.interceptar(contexto)
        pagina = contexto.new_page()
        contexto.on("page", lambda nova: nova.close())  # um clique nunca abre abas novas
        pagina.set_default_timeout(self.config.timeout_pagina * 1000)
        try:
            inicio = time.monotonic()
            resposta = pagina.goto(url, wait_until="domcontentloaded", timeout=self.config.timeout_pagina * 1000)
            resultado["status"] = resposta.status if resposta else None
            resultado.update(self._esperar_carregar(pagina))
            resultado["url_final"] = pagina.url
            resultado["tempo_carregamento_ms"] = int((time.monotonic() - inicio) * 1000)
            resultado["html"] = pagina.content()
            resultado["titulo"] = pagina.title()
            if medir:
                self._voltar_ao_topo(pagina)
                resultado["medidas"] = pagina.evaluate(MEDIR_JS)
                if not _tem_formulario(resultado["medidas"]) and resultado["medidas"].get("gatilhos_formulario"):
                    resultado["cliques"] = self._abrir_gatilhos(pagina, resultado["medidas"]["gatilhos_formulario"])
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

    def _esperar_carregar(self, pagina) -> dict:
        """Espera a rede ficar ociosa e o DOM parar de mudar; rola até o fim para carregar o que é preguiçoso.

        A página é considerada completa se a rede ficou ociosa OU o DOM ficou estável.
        Sites com chat ou analytics nunca deixam a rede ociosa, por isso o segundo critério.
        """
        rede = True
        try:
            pagina.wait_for_load_state("networkidle", timeout=self.config.espera_rede_ms)
        except Exception:
            rede = False
        try:  # formulários e widgets costumam ser carregados só quando aparecem na tela
            pagina.evaluate("""async () => { const h = document.documentElement.scrollHeight;
                for (let y = 0; y < h; y += Math.max(400, innerHeight)) { scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); }
                scrollTo(0, h); }""")
        except Exception:
            pass
        pagina.wait_for_timeout(self.config.espera_extra_ms)
        estavel, anterior, iguais = False, None, 0
        limite = time.monotonic() + self.config.espera_dom_ms / 1000
        while time.monotonic() < limite:
            try:
                atual = pagina.evaluate(ASSINATURA_DOM_JS)
            except Exception:
                break
            iguais = iguais + 1 if atual == anterior else 0
            anterior = atual
            if iguais >= 2:
                estavel = True
                break
            pagina.wait_for_timeout(500)
        return {"render_completo": rede or estavel, "rede_ociosa": rede, "dom_estavel": estavel}

    def _voltar_ao_topo(self, pagina) -> None:
        """Volta ao topo sem animação e espera as posições pararem de mudar.

        Sites com rolagem suave (ScrollSmoother, Lenis, scroll-behavior: smooth) continuam
        animando depois do scrollTo; medir nesse meio tempo dá posições erradas.
        """
        pagina.evaluate("""() => { for (const el of [document.documentElement, document.body])
            if (el) el.style.scrollBehavior = 'auto'; window.scrollTo(0, 0); }""")
        anterior, iguais = None, 0
        limite = time.monotonic() + 5
        while time.monotonic() < limite:
            atual = pagina.evaluate("""() => scrollY + ':' + [...document.querySelectorAll('h1, h2, a, button')].slice(0, 25)
                .map(e => Math.round(e.getBoundingClientRect().top)).join(',')""")
            iguais = iguais + 1 if atual == anterior else 0
            anterior = atual
            if iguais >= 2 and atual.startswith("0:"):
                return
            pagina.wait_for_timeout(250)

    def _abrir_gatilhos(self, pagina, gatilhos: list, maximo: int = 2) -> list[dict]:
        """Clica em até `maximo` botões que parecem abrir formulário (sem navegar nem enviar nada).

        Depois de cada clique, mede de novo e guarda o que apareceu.
        """
        cliques = []
        for g in sorted(gatilhos, key=lambda g: not g.get("abre_dialogo"))[:maximo]:
            registro = {"texto": g.get("texto", ""), "href": g.get("href", ""), "abriu_formulario": False, "erro": None}
            try:
                if not pagina.evaluate(MARCAR_GATILHO_JS, {"texto": g.get("texto", ""), "href": g.get("href", "")}):
                    registro["erro"] = "botão não encontrado de novo"
                    cliques.append(registro)
                    continue
                antes = pagina.url.split("#")[0]
                pagina.locator("[data-wd-diag-gatilho]").first.click(timeout=3000)
                pagina.wait_for_timeout(1500)
                if pagina.url.split("#")[0] != antes:
                    registro["erro"] = "o clique levou para outra página"
                    cliques.append(registro)
                    break
                m = pagina.evaluate(MEDIR_JS)
                registro["abriu_formulario"] = _tem_formulario(m)
                registro["medidas"] = {k: m.get(k) for k in ("formularios", "formularios_externos", "formularios_provedor",
                                                              "links_formulario", "campos_soltos", "sinais_formulario")}
                pagina.evaluate("document.querySelectorAll('[data-wd-diag-gatilho]').forEach(e => e.removeAttribute('data-wd-diag-gatilho'))")
                pagina.keyboard.press("Escape")
            except Exception as e:  # noqa: BLE001
                registro["erro"] = str(e).splitlines()[0][:160]
            cliques.append(registro)
            if registro["abriu_formulario"]:
                break
        return cliques
