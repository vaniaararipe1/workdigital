"""Renderização das duas versões, rodapés e regras do revisao.json (sem rede, sem navegador)."""
import copy
import json

import pytest

from wd_diag import revisao as rv
from wd_diag.analise import performance
from wd_diag.modelos import Achado, Nota, Tecnologia
from wd_diag.relatorio import contexto, notas
from wd_diag.relatorio.gerar import renderizar_html

RODAPE_REVISADO = "Análise técnica automatizada com revisão especializada."
RODAPE_AUTOMATICO = "Análise técnica automatizada. Avaliação especializada em revisão."


def resultado():
    falha = {"ok": False, "tentativas": [{"fonte": "pagespeed", "erro": "429"}]}
    achados = [
        Achado("ux-cta-mobile", "ux", "Chamada para ação", "medido", "problema", "Sem botão <b>", evidencia="&lt;x&gt;",
               significado="Visitante não age", correcao="Pôr botão", impacto="perde contatos", prioridade="alta",
               esforco="rápido (horas)", peso=3),
        Achado("ux-proposta", "ux", "Clareza da proposta de valor", "avaliacao", "atencao", "Título genérico",
               significado="Não diz o que faz", correcao="Reescrever o título", prioridade="media", peso=0,
               nota_interna="confira"),
        Achado("ux-form", "ux", "Formulário de contato", "nao_confirmado", "na", "Há sinais de formulário", peso=2),
        Achado("seo-title", "seo", "Títulos", "medido", "ok", "Todos ok", peso=2),
        *performance.achados(falha, falha),
    ]
    return {
        "empresa": "Empresa <Teste>", "url_final": "https://ex.com/", "data": "2026-10-12",
        "data_extenso": "12 de outubro de 2026",
        "achados": achados, "metricas": performance.metricas(falha, falha), "tecnologias": [Tecnologia("WordPress", "CMS", "x")],
        "notas": {"performance": Nota("Performance", None, 0, 2), "ux": Nota("Experiência e conversão", 0, 1, 2),
                  "seo": Nota("SEO e visibilidade", 100, 1, 1)},
        "performance": {"mobile": falha, "desktop": falha, "fonte_texto": ""},
        "paginas_resumo": [{"url": "https://ex.com/", "origem": "página inicial", "situacao": "aberta (código 200)"}],
        "avisos": ["aviso de teste"],
    }


def revisao_completa(r):
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    rev["nota_pessoal"] = {"status": rv.REVISADO, "texto": "Olá! Revisei o site com carinho."}
    for av in rev["avaliacoes"]:
        av.update(status=rv.REVISADO, o_que_vimos="O título é genérico.", o_que_significa="Não diz o que a empresa faz.",
                  o_que_fazer="Reescrever o título principal.")
    rev["plano"]["status"] = rv.REVISADO
    return rev


# ---------------- versão automática ----------------

def test_automatica_nao_tem_rodape_de_revisao_nem_itens_de_especialista():
    html = renderizar_html(contexto.montar(resultado(), "automatica", prazo_dias=3))
    assert "revisão especializada" not in html
    assert RODAPE_AUTOMATICO in html
    assert "Resultado técnico" in html
    assert "chega em até 3 dias úteis" in html
    assert "Clareza da proposta de valor" not in html          # avaliação de especialista fica de fora
    assert "Por onde começar" not in html and "Vamos conversar" not in html
    assert "Pôr botão" not in html                              # sem "o que fazer" nem plano
    assert "Não foi possível confirmar" in html


def test_automatica_escapa_texto_do_site_e_mantem_contatos_fora():
    html = renderizar_html(contexto.montar(resultado(), "automatica"))
    assert "Empresa &lt;Teste&gt;" in html and "Empresa <Teste>" not in html
    assert "Sem botão &lt;b&gt;" in html
    assert "sem<br>medição" in html
    assert "Como a nota foi formada" in html


# ---------------- versão revisada ----------------

def test_revisada_tem_avaliacao_plano_nota_pessoal_e_rodape():
    r = resultado()
    rev = revisao_completa(r)
    assert rv.validar(rev) == []
    html = renderizar_html(contexto.montar(r, "revisada", rev))
    assert RODAPE_REVISADO in html and RODAPE_AUTOMATICO not in html
    assert "O título é genérico." in html and "Avaliação de especialista" in html
    assert "Por onde começar" in html and "Pôr botão" in html
    assert "Olá! Revisei o site com carinho." in html
    assert "hello@workdigital.art.br" in html and "conversa de 30 minutos" in html
    assert "Resultado técnico" not in html
    assert "Título genérico" not in html                         # o rascunho da ferramenta não aparece


def test_revisada_exige_revisao_validada():
    with pytest.raises(ValueError):
        contexto.montar(resultado(), "revisada", None)


def test_rascunho_nasce_pendente_e_e_recusado():
    r = resultado()
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    assert rev["nota_pessoal"]["status"] == rv.PENDENTE
    assert all(av["status"] == rv.PENDENTE for av in rev["avaliacoes"])
    assert rev["avaliacoes"][0]["o_que_vimos"].startswith("[RASCUNHO]")
    pendencias = rv.validar(rev)
    assert any("nota pessoal" in p for p in pendencias)
    assert any("Clareza da proposta de valor" in p for p in pendencias)
    assert any("plano" in p for p in pendencias)


@pytest.mark.parametrize("estragar", [
    lambda rev: rev["nota_pessoal"].update(texto=""),
    lambda rev: rev["nota_pessoal"].update(status=rv.PENDENTE),
    lambda rev: rev["avaliacoes"][0].update(status=rv.PENDENTE),
    lambda rev: rev["avaliacoes"][0].update(o_que_vimos="[RASCUNHO] sugestão"),
    lambda rev: rev["avaliacoes"][0].update(o_que_fazer=""),
    lambda rev: rev["avaliacoes"][0].update(situacao="talvez"),
    lambda rev: rev["plano"].update(status=rv.PENDENTE),
    lambda rev: rev.update(avaliacoes=[]),
])
def test_revisao_incompleta_e_recusada(estragar, tmp_path):
    rev = revisao_completa(resultado())
    estragar(rev)
    assert rv.validar(rev)
    arq = tmp_path / "revisao.json"
    arq.write_text(json.dumps(rev), encoding="utf-8")
    with pytest.raises(rv.RevisaoIncompleta) as erro:
        rv.carregar_validado(arq)
    assert erro.value.pendencias


def test_rascunho_nao_sobrescreve_trabalho_da_vania(tmp_path):
    arq = tmp_path / "revisao.json"
    assert rv.salvar_rascunho(arq, {"a": 1})
    assert not rv.salvar_rascunho(arq, {"a": 2})
    assert json.loads(arq.read_text())["a"] == 1


def test_gerar_revisada_recusa_com_revisao_incompleta(tmp_path, monkeypatch):
    from wd_diag import pipeline
    r = resultado()
    rev = revisao_completa(r)
    incompleta = copy.deepcopy(rev)
    incompleta["avaliacoes"][0]["status"] = rv.PENDENTE
    (tmp_path / "revisao.json").write_text(json.dumps(incompleta), encoding="utf-8")
    monkeypatch.setattr(pipeline, "carregar_resultado", lambda pasta: r)
    with pytest.raises(rv.RevisaoIncompleta):
        pipeline.gerar_revisada(tmp_path, gerar_pdf=False)
    assert not (tmp_path / "relatorio-revisado.html").exists()
    (tmp_path / "revisao.json").write_text(json.dumps(rev), encoding="utf-8")
    pipeline.gerar_revisada(tmp_path, gerar_pdf=False)
    assert RODAPE_REVISADO in (tmp_path / "relatorio-revisado.html").read_text(encoding="utf-8")


# ---------------- notas internas ----------------

def test_notas_internas_trazem_rascunhos_e_abordagem():
    r = resultado()
    rascunho = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    html = renderizar_html(notas.montar(r, rascunho), template="notas_internas.html.j2")
    assert "não enviar ao lead" in html and "aviso de teste" in html
    assert "[RASCUNHO]" in html and "pendente de revisão" in html
    assert "--versao revisada" in html
    titulos = [a["titulo"] for a in notas.abordagens(r)]
    assert "Home sem convite para ação no celular" in titulos
    assert "Sem medição de visitas detectada" in titulos


# ---------------- aprovação rápida dos rascunhos ----------------

def test_aprovar_rascunhos_aceita_os_textos_da_ferramenta(tmp_path):
    r = resultado()
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    assert rev["aprovar_rascunhos"] is False
    arq = tmp_path / "revisao.json"
    arq.write_text(json.dumps(rev), encoding="utf-8")
    with pytest.raises(rv.RevisaoIncompleta):
        rv.carregar_validado(arq)
    rev["aprovar_rascunhos"] = True
    arq.write_text(json.dumps(rev), encoding="utf-8")
    ok = rv.carregar_validado(arq)
    assert ok["nota_pessoal"]["status"] == rv.REVISADO
    ok.pop("_instrucoes")
    assert "[RASCUNHO]" not in json.dumps(ok, ensure_ascii=False)
    # o arquivo original não é reescrito: a aprovação vale só para a geração
    assert "[RASCUNHO]" in arq.read_text(encoding="utf-8")


def test_aprovar_rascunhos_ainda_exige_o_que_fazer():
    r = resultado()
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    rev["aprovar_rascunhos"] = True
    rev["avaliacoes"][0].update(situacao="problema", o_que_fazer="")
    assert any("o_que_fazer" in p for p in rv.validar(rv.aplicar_aprovacao(rev)))


def test_sem_aprovacao_nada_muda():
    r = resultado()
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    assert rv.aplicar_aprovacao(rev) is rev


def test_previa_tem_marca_de_nao_enviar():
    r = resultado()
    rev = rv.aplicar_aprovacao(rv.criar_rascunho(r, contexto.plano(r["achados"])), forcar=True)
    ctx = contexto.montar(r, "revisada", rev, prazo_dias=2)
    ctx["previa"] = True
    html = renderizar_html(ctx)
    assert "Prévia para revisão" in html
    assert "Prévia para revisão" not in renderizar_html(contexto.montar(r, "revisada", rev, prazo_dias=2))



def test_toda_referencia_tem_fonte_e_nao_atribui_o_que_nao_e_oficial():
    from wd_diag.analise.referencias import MERCADO, REFERENCIAS, referencia
    for chave, (recomendado, fonte) in REFERENCIAS.items():
        assert recomendado and fonte, chave
    # limites que não vêm de norma oficial ficam marcados como prática de mercado
    for chave in ("seo-h1", "ux-whatsapp", "ux-tel-email", "seo-links", "geo-faq"):
        assert MERCADO in REFERENCIAS[chave][1]
    assert referencia("perf-op-unused-javascript")["fonte"].startswith("Google Lighthouse")
    assert referencia("ux-social") is None  # avaliação de especialista não leva referência automática


def test_relatorio_mostra_recomendado_nos_itens_medidos():
    r = resultado()
    html = renderizar_html(contexto.montar(r, "automatica", None, prazo_dias=2))
    assert "Recomendado" in html and "Fonte:" in html
