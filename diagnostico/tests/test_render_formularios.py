"""Formulários de verdade num navegador: páginas falsas servidas pelo próprio Playwright (sem rede).

Pulados se o Playwright ou o Chromium não estiverem instalados.
"""
import pytest

from wd_diag.analise import ux
from wd_diag.config import Config

playwright = pytest.importorskip("playwright.sync_api")

BASE = "https://exemplo-diagnostico.com.br"

# Imita o embed do RD Station: o script chega depois e só então monta o formulário (div.bricks-form).
RD_SCRIPT = """
setTimeout(function () {
  var alvo = document.getElementById('form-proposta-1a2b3c');
  alvo.innerHTML = '<div class="bricks-form"><form action="https://www.rdstation.com.br/api/1.3/conversions">' +
    '<label for="nome">Nome</label><input id="nome" name="name" type="text">' +
    '<label for="email">E-mail</label><input id="email" name="email" type="email">' +
    '<label for="msg">Mensagem</label><textarea id="msg" name="mensagem"></textarea>' +
    '<button type="submit">Enviar</button></form></div>';
}, 1200);
"""

PAGINAS = {
    "/rd/": """<!doctype html><html><head><title>Com RD</title></head><body><h1>Empresa</h1>
        <div role="main" id="form-proposta-1a2b3c"></div>
        <script src="https://d335luupugsy2.cloudfront.net/js/rdstation-forms/stable/rdstation-forms.min.js"></script>
        </body></html>""",
    "/vazia/": """<!doctype html><html><head><title>Sem formulário</title></head><body><h1>Empresa</h1>
        <p>Somos uma empresa. Ligue para nós.</p></body></html>""",
    # script de formulário presente, mas o formulário nunca aparece (ex.: bloqueado ou com erro)
    "/ambigua/": """<!doctype html><html><head><title>Ambígua</title></head><body><h1>Empresa</h1>
        <div id="form-proposta-9z"></div>
        <script src="https://d335luupugsy2.cloudfront.net/js/rdstation-forms/stable/quebrado.js"></script>
        </body></html>""",
    # formulário que só existe depois de clicar no botão (pop-up)
    "/popup/": """<!doctype html><html><head><title>Pop-up</title></head><body><h1>Empresa</h1>
        <button type="button" aria-haspopup="dialog" id="abrir">Pedir orçamento</button>
        <script>document.getElementById('abrir').addEventListener('click', function () {
          var d = document.createElement('div'); d.setAttribute('role', 'dialog');
          d.innerHTML = '<form><input name="nome" aria-label="Nome"><input name="email" type="email" aria-label="E-mail"></form>';
          document.body.appendChild(d); });</script></body></html>""",
}
SCRIPTS = {
    "rdstation-forms.min.js": RD_SCRIPT,
    "quebrado.js": "/* não monta nada */",
}


def _interceptar(contexto):
    def responder(route):
        url = route.request.url
        for nome, codigo in SCRIPTS.items():
            if url.endswith(nome):
                return route.fulfill(status=200, content_type="application/javascript", body=codigo)
        caminho = url.removeprefix(BASE)
        if caminho in PAGINAS:
            return route.fulfill(status=200, content_type="text/html; charset=utf-8", body=PAGINAS[caminho])
        return route.fulfill(status=404, content_type="text/html", body="<h1>404</h1>")
    contexto.route("**/*", responder)


@pytest.fixture(scope="module")
def rnd():
    from wd_diag.coleta.render import Renderizador
    config = Config.do_ambiente()
    config.intervalo_requisicoes = 0
    config.espera_rede_ms = 5000
    try:
        r = Renderizador(config).__enter__()
    except Exception as e:  # noqa: BLE001
        pytest.skip(f"Chromium indisponível: {e}")
    r.interceptar = _interceptar
    yield r
    r.__exit__(None, None, None)


BUSCA = {"contato": [{"url": BASE + "/contato/", "origem": "endereço padrão", "situacao": "nao_existe", "detalhe": "código 404"}],
         "paginas_contato": [], "falhas": []}


def _analisar(rnd, caminho):
    p = rnd.renderizar(BASE + caminho, "desktop")
    assert p["erro"] is None and p["render_completo"]
    return p, ux.formulario([p], tem_contato_direto=True, busca=BUSCA)


def test_formulario_rd_station_carregado_por_script_e_detectado(rnd):
    p, a = _analisar(rnd, "/rd/")
    assert any(f["campos"] == 3 for f in p["medidas"]["formularios"])
    assert any(s["provedor"] == "RD Station" for s in p["medidas"]["sinais_formulario"])
    assert a.tipo == "medido" and a.situacao == "ok"


def test_pagina_sem_formulario_e_sem_sinal_e_ausencia_medida(rnd):
    p, a = _analisar(rnd, "/vazia/")
    assert not p["medidas"]["sinais_formulario"] and not p["medidas"]["gatilhos_formulario"]
    assert a.tipo == "medido" and a.situacao == "atencao"
    assert "Não encontramos formulário" in a.o_que_vimos


def test_script_de_formulario_sem_formulario_renderizado_nao_e_confirmado(rnd):
    p, a = _analisar(rnd, "/ambigua/")
    assert not p["medidas"]["formularios"]
    assert a.tipo == "nao_confirmado" and a.situacao == "na" and not a.conta_na_nota()
    assert "RD Station" in a.evidencia


def test_formulario_em_popup_e_aberto_pelo_botao(rnd):
    p, a = _analisar(rnd, "/popup/")
    assert p["cliques"] and p["cliques"][0]["abriu_formulario"]
    assert a.tipo == "medido" and a.situacao == "ok" and "Pedir orçamento" in a.evidencia
