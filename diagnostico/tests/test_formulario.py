"""Detecção de formulário de contato: nunca afirmar 'não há formulário' sem ter procurado tudo."""
from wd_diag.analise import ux

from .test_analise import medidas

HTML_RD = """<html><body><div id="contato-site-123"></div>
<script type="text/javascript" src="https://d335luupugsy2.cloudfront.net/js/rdstation-forms/stable/rdstation-forms.min.js"></script>
<script>new RDStationForms('contato-site-123', 'UA-1').createForm();</script></body></html>"""


def pagina(url, html="<html></html>", **kw):
    return {"url": url, "html": html, "medidas": medidas(**kw)}


def test_sinais_de_formulario_por_script():
    assert ux.sinais_formulario(HTML_RD) == ["RD Station"]
    assert "HubSpot" in ux.sinais_formulario('<script src="//js.hsforms.net/forms/v2.js"></script>')
    assert "Contact Form 7" in ux.sinais_formulario('<div class="wpcf7">')
    assert ux.sinais_formulario("<p>Fale conosco pelo telefone</p>") == []


def test_formulario_rd_carregado_por_script_e_nao_confirmado():
    a = ux.formulario([pagina("https://ex.com/"), pagina("https://ex.com/contato", HTML_RD)], True,
                      {"url": "https://ex.com/contato", "tentativas": [], "erro": None})
    assert a.tipo == "nao_confirmado" and a.situacao == "na"
    assert "RD Station" in a.evidencia
    assert not a.conta_na_nota()


def test_botao_que_abre_modal_e_nao_confirmado():
    a = ux.formulario([pagina("https://ex.com/", botoes_modal=["Solicitar proposta"])], True,
                      {"url": "https://ex.com/contato", "tentativas": [], "erro": None})
    assert a.tipo == "nao_confirmado" and "Solicitar proposta" in a.evidencia


def test_pagina_de_contato_inacessivel_e_nao_confirmado():
    a = ux.formulario([pagina("https://ex.com/")], True, {"url": None, "tentativas": [], "erro": "tempo esgotado"})
    assert a.tipo == "nao_confirmado"
    falhou = {"url": "https://ex.com/contato", "erro": "tempo esgotado"}
    b = ux.formulario([pagina("https://ex.com/"), falhou], True, {"url": None, "tentativas": [], "erro": None})
    assert b.tipo == "nao_confirmado"


def test_sem_nenhum_sinal_e_medido():
    a = ux.formulario([pagina("https://ex.com/"), pagina("https://ex.com/contato")], True,
                      {"url": "https://ex.com/contato", "tentativas": [], "erro": None})
    assert a.tipo == "medido" and a.situacao == "atencao"
    assert "/contato" in a.evidencia


def test_formulario_visivel_tem_prioridade_sobre_sinais():
    form = {"campos": 4, "com_rotulo": 4, "com_placeholder": 0}
    a = ux.formulario([pagina("https://ex.com/contato", HTML_RD, formularios=[form])], True, {})
    assert a.tipo == "medido" and a.situacao == "ok"


def test_iframe_de_formulario_externo_conta_como_existente():
    a = ux.formulario([pagina("https://ex.com/contato", formularios_externos=["https://forms.gle/abc"])], False, {})
    assert a.tipo == "medido" and a.situacao == "ok" and a.confianca == "baixa"


def test_formulario_rd_renderizado_por_script_e_detectado_com_local_e_ferramenta():
    # Depois da renderização completa, o script do RD Station injeta um <form> com campos visíveis.
    form = {"campos": 3, "com_rotulo": 3, "com_placeholder": 0}
    a = ux.formulario([pagina("https://ex.com/"), pagina("https://ex.com/contato/", HTML_RD, formularios=[form])], True,
                      {"url": "https://ex.com/contato/", "tentativas": [], "erro": None})
    assert a.tipo == "medido" and a.situacao == "ok"
    assert "/contato/" in a.evidencia and "RD Station" in a.evidencia


# ---------------- mesma cautela para WhatsApp, botão de ação e telefone/e-mail ----------------

def test_whatsapp_ausente_com_pagina_que_falhou_e_nao_confirmado():
    falhou = {"url": "https://ex.com/contato", "erro": "tempo esgotado"}
    a = ux.whatsapp(medidas(), [pagina("https://ex.com/"), falhou])
    assert a.tipo == "nao_confirmado"


def test_whatsapp_ausente_com_widget_no_codigo_e_nao_confirmado():
    a = ux.whatsapp(medidas(), [pagina("https://ex.com/", '<div class="joinchat joinchat--right"></div>')])
    assert a.tipo == "nao_confirmado" and "WhatsApp" in a.evidencia


def test_whatsapp_ausente_sem_sinais_e_medido():
    a = ux.whatsapp(medidas(), [pagina("https://ex.com/"), pagina("https://ex.com/contato")],
                    {"url": "https://ex.com/contato", "tentativas": [], "erro": None})
    assert a.tipo == "medido" and a.situacao == "problema"


def test_botao_de_acao_sem_nenhum_clicavel_e_nao_confirmado():
    a = ux.cta_dobra(medidas(alvos_total=0), "mobile")
    assert a.tipo == "nao_confirmado"
    b = ux.cta_dobra(medidas(alvos_total=12), "mobile")
    assert b.tipo == "medido" and b.situacao == "problema"


def test_telefone_email_ausente_com_contato_inacessivel_e_nao_confirmado():
    a = ux.telefone_email([pagina("https://ex.com/")], {"url": None, "tentativas": [], "erro": "erro 500"})
    assert a.tipo == "nao_confirmado"


def test_formulario_em_janela_aberta_por_botao_e_medido_com_local():
    janela = {"url": "https://ex.com/contato/", "botao": "Solicitar proposta", "navegou": False,
              "formularios": [{"campos": 5, "com_rotulo": 5, "com_placeholder": 0}]}
    a = ux.formulario([pagina("https://ex.com/", HTML_RD, botoes_modal=["Solicitar proposta"])], True,
                      {"url": "https://ex.com/contato/", "tentativas": [], "erro": None, "janela": janela})
    assert a.tipo == "medido" and a.situacao == "ok"
    assert "Solicitar proposta" in a.evidencia and "/contato/" in a.evidencia


def test_janela_que_navega_para_outra_pagina_nao_conta():
    janela = {"url": "https://ex.com/", "botao": "Orçamento", "navegou": True,
              "formularios": [{"campos": 5, "com_rotulo": 5, "com_placeholder": 0}]}
    a = ux.formulario([pagina("https://ex.com/", botoes_modal=["Orçamento"])], True,
                      {"url": "https://ex.com/contato", "tentativas": [], "erro": None, "janela": janela})
    assert a.tipo == "nao_confirmado"
