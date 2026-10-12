"""Renderização dos templates com um resultado sintético (sem rede, sem navegador)."""
from wd_diag.modelos import Achado, Nota, Tecnologia
from wd_diag.analise import performance
from wd_diag.relatorio import contexto, notas
from wd_diag.relatorio.gerar import renderizar_html


def resultado():
    falha = {"ok": False, "tentativas": [{"fonte": "pagespeed", "erro": "429"}]}
    achados = [
        Achado("ux-cta-mobile", "ux", "Chamada para ação", "medido", "problema", "Sem botão <b>", evidencia="&lt;x&gt;",
               correcao="Pôr botão", impacto="perde contatos", prioridade="alta", esforco="rápido (horas)", peso=3),
        Achado("ux-proposta", "ux", "Proposta", "avaliacao", "atencao", "Título genérico", peso=0,
               nota_interna="confira"),
        Achado("seo-title", "seo", "Títulos", "medido", "ok", "Todos ok", peso=2),
        *performance.achados(falha, falha),
    ]
    return {
        "empresa": "Empresa <Teste>", "url_final": "https://ex.com/", "data_extenso": "11 de outubro de 2026",
        "achados": achados, "metricas": performance.metricas(falha, falha), "tecnologias": [Tecnologia("WordPress", "CMS", "x")],
        "notas": {"performance": Nota("Performance", None, 0, 2), "ux": Nota("Experiência e conversão", 0, 1, 1),
                  "seo": Nota("SEO e visibilidade", 100, 1, 1)},
        "performance": {"mobile": falha, "desktop": falha, "fonte_texto": ""},
        "paginas_resumo": [{"url": "https://ex.com/", "origem": "página inicial", "situacao": "aberta"}],
        "avisos": ["aviso de teste"],
    }


def test_relatorio_renderiza_com_dados_faltando_e_escapa_texto():
    html = renderizar_html(contexto.montar(resultado()))
    assert "Empresa &lt;Teste&gt;" in html and "Empresa <Teste>" not in html
    assert "Sem botão &lt;b&gt;" in html
    assert "sem<br>medição" in html                     # nota de performance ausente
    assert "Não foi possível medir" in html
    assert "hello@workdigital.art.br" in html and "(11) 99391-6363" in html
    assert "© Work Digital 2026" in html
    assert "Avaliação de especialista" in html


def test_notas_internas_trazem_julgamento_e_abordagem():
    r = resultado()
    html = renderizar_html(notas.montar(r), template="notas_internas.html.j2")
    assert "não enviar ao lead" in html and "confira" in html and "aviso de teste" in html
    titulos = [a["titulo"] for a in notas.abordagens(r)]
    assert "Home sem convite para ação no celular" in titulos
    assert "Sem medição de visitas detectada" in titulos
