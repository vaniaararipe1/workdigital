"""Testes das funções de análise com dados sintéticos (sem rede)."""
from wd_diag.analise import performance, seo, tecnologias, ux
from wd_diag.coleta.pagespeed import extrair
from wd_diag.modelos import Achado
from wd_diag.pontuacao import nota_por_criterios
from wd_diag.rastreador import escolher_paginas, urls_do_sitemap
from wd_diag.relatorio.contexto import plano, top3


# ---------------- UX ----------------

def medidas(**kw):
    base = {
        "viewport": {"largura": 390, "altura": 844}, "meta_viewport": "width=device-width, initial-scale=1",
        "largura_documento": 390, "ctas_dobra": [], "ctas_fortes_dobra": [], "primeiro_cta": None,
        "contato_direto": [], "formularios": [], "formularios_externos": [], "texto_total_chars": 1000,
        "texto_pequeno_chars": 0, "alvos_total": 20, "alvos_pequenos": [], "alvos_pequenos_total": 0,
        "h1s": [], "primeiro_titulo": None, "sinais_prova_social": [], "widgets_prova_social": 0,
    }
    base.update(kw)
    return base


def cta(texto, topo, botao=True, chave=True, fixo=False):
    return {"texto": texto, "href": "#", "topo": topo, "largura": 200, "altura": 48, "botao": botao,
            "palavra_chave": chave, "fixo": fixo}


def test_cta_ok_quando_ha_botao_de_acao_na_dobra():
    m = medidas(ctas_dobra=[cta("Peça um orçamento", 400)], ctas_fortes_dobra=[cta("Peça um orçamento", 400)])
    a = ux.cta_dobra(m, "mobile")
    assert a.situacao == "ok" and a.tipo == "medido"
    assert "400 px" in a.evidencia


def test_cta_problema_quando_primeiro_botao_abaixo_da_dobra():
    m = medidas(primeiro_cta=cta("Fale conosco", 1240))
    a = ux.cta_dobra(m, "mobile")
    assert a.situacao == "problema" and a.prioridade == "alta"
    assert "1240 px" in a.evidencia and "844 px" in a.evidencia


def test_cta_nao_medido_sem_dados():
    a = ux.cta_dobra(None, "desktop")
    assert a.tipo == "nao_medido" and not a.conta_na_nota()


def test_contato_direto_whatsapp_visivel_na_dobra():
    m = medidas(contato_direto=[{"tipo": "whatsapp", "href": "https://wa.me/5511999999999", "visivel": True,
                                 "fixo": True, "topo": 2000, "texto": ""}])
    a = ux.whatsapp(m, [{"url": "https://ex.com/", "medidas": m}])
    assert a.situacao == "ok"


def test_contato_direto_ausente_em_todas_as_paginas():
    m = medidas()
    a = ux.whatsapp(m, [{"url": "https://ex.com/", "medidas": m}, {"url": "https://ex.com/contato", "medidas": m}])
    assert a.situacao == "problema" and "2 páginas" in a.evidencia


def test_telefone_e_email_clicaveis():
    tel = {"tipo": "telefone", "href": "tel:+551199999", "visivel": True, "fixo": False, "topo": 900, "texto": ""}
    mail = {"tipo": "email", "href": "mailto:oi@ex.com", "visivel": True, "fixo": False, "topo": 900, "texto": ""}
    assert ux.telefone_email([{"url": "https://ex.com/", "medidas": medidas(contato_direto=[tel, mail])}]).situacao == "ok"
    assert ux.telefone_email([{"url": "https://ex.com/", "medidas": medidas(contato_direto=[tel])}]).situacao == "atencao"
    assert ux.telefone_email([{"url": "https://ex.com/", "medidas": medidas()}]).situacao == "problema"


def test_formulario_longo_e_sem_rotulo():
    form = {"campos": 11, "com_rotulo": 11, "com_placeholder": 0}
    a = ux.formulario([{"url": "https://ex.com/contato", "medidas": medidas(formularios=[form])}], True)
    assert a.situacao == "problema"
    form = {"campos": 4, "com_rotulo": 1, "com_placeholder": 4}
    a = ux.formulario([{"url": "https://ex.com/contato", "medidas": medidas(formularios=[form])}], True)
    assert a.situacao == "atencao" and "sem rótulo" in a.o_que_vimos


def test_formulario_externo_conta_como_existente_com_baixa_confianca():
    m = medidas(formularios_externos=["https://forms.rdstation.com.br/x"])
    a = ux.formulario([{"url": "https://ex.com/contato", "medidas": m}], False)
    assert a.situacao == "ok" and a.confianca == "baixa"


def test_viewport_e_rolagem_lateral():
    assert ux.viewport(medidas(meta_viewport=None)).situacao == "problema"
    assert ux.viewport(medidas(largura_documento=600)).situacao == "atencao"
    assert ux.viewport(medidas()).situacao == "ok"


def test_legibilidade_e_toque_por_faixas():
    assert ux.legibilidade(medidas(texto_pequeno_chars=50)).situacao == "ok"
    assert ux.legibilidade(medidas(texto_pequeno_chars=300)).situacao == "atencao"
    assert ux.legibilidade(medidas(texto_pequeno_chars=500)).situacao == "problema"
    assert ux.alvos_toque(medidas(alvos_pequenos_total=8)).situacao == "problema"


def test_julgamento_nunca_entra_na_nota():
    a = ux.proposta_valor(medidas(h1s=[{"texto": "Bem-vindo ao nosso site", "visivel": True, "topo": 100}]))
    assert a.tipo == "avaliacao" and a.situacao == "atencao" and not a.conta_na_nota()
    b = ux.prova_social([{"url": "https://ex.com/", "medidas": medidas()}])
    assert b.tipo == "avaliacao" and not b.conta_na_nota()


def test_texto_do_site_e_escapado_na_evidencia():
    m = medidas(sinais_prova_social=["<script>alert(1)</script> depoimentos"])
    a = ux.prova_social([{"url": "https://ex.com/", "medidas": m}])
    assert "<script>" not in a.evidencia and "&lt;script&gt;" in a.evidencia


# ---------------- SEO ----------------

HTML_BOM = """<html><head><title>Padaria Exemplo | Pães artesanais em Pinheiros</title>
<meta name="description" content="Pães de fermentação natural, bolos e encomendas para festas em Pinheiros, São Paulo. Peça pelo WhatsApp.">
<link rel="canonical" href="https://ex.com/">
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"Bakery","name":"Padaria"},{"@type":"FAQPage"}]}</script>
</head><body><h1>Pães artesanais</h1><h2>Quanto custa?</h2><h3>x</h3><img src="a.jpg" alt="pão"><a href="/contato">c</a></body></html>"""

HTML_RUIM = """<html><head><title>Home</title><meta name="robots" content="noindex"></head>
<body><h2>a</h2><h4>b</h4><img src="x.jpg"><img src="y.jpg"></body></html>"""


def test_extrair_pagina():
    p = seo.extrair_pagina("https://ex.com/", HTML_BOM)
    assert p["titulo"].startswith("Padaria Exemplo")
    assert p["h1"] == ["Pães artesanais"]
    assert "Bakery" in p["schema_tipos"] and "FAQPage" in p["schema_tipos"]
    assert p["links_internos"] == ["https://ex.com/contato"]
    assert p["perguntas_em_titulos"] == ["Quanto custa?"]
    r = seo.extrair_pagina("https://ex.com/x", HTML_RUIM)
    assert r["saltos_hierarquia"] == ["h2→h4"] and len(r["imagens_sem_alt"]) == 2 and "noindex" in r["meta_robots"]


def test_seo_criterios_principais():
    bom = seo.extrair_pagina("https://ex.com/", HTML_BOM)
    ruim = seo.extrair_pagina("https://ex.com/sobre", HTML_RUIM)
    assert seo.indexacao([bom, ruim]).situacao == "problema"
    assert seo.h1([bom, ruim]).situacao == "atencao"
    assert seo.h1([ruim, bom]).situacao == "problema"          # home sem H1
    assert seo.imagens_alt([bom, ruim]).situacao == "problema"   # 2 de 3 sem alt
    org, faq = seo.dados_estruturados([bom])[1:]
    assert org.situacao == "ok" and faq.situacao == "ok"
    org_r = seo.dados_estruturados([ruim])[1]
    assert org_r.situacao == "problema"


def test_titulos_duplicados():
    a = seo.extrair_pagina("https://ex.com/", HTML_RUIM)
    b = seo.extrair_pagina("https://ex.com/sobre", HTML_RUIM)
    _, dup = seo.titulos([a, b])
    assert dup.situacao == "problema" and "2 páginas" in dup.o_que_vimos
    _, unico = seo.titulos([a])
    assert unico.tipo == "nao_medido"


def test_https_e_redirecionamentos():
    assert seo.https("http://ex.com/", {}).situacao == "problema"
    assert seo.https("https://ex.com/", {"redireciona_para_https": True, "url_testada": "http://ex.com/",
                                         "destino": "https://ex.com/"}).situacao == "ok"
    assert seo.https("https://ex.com/", {"redireciona_para_https": False, "url_testada": "http://ex.com/",
                                         "destino": "http://ex.com/"}).situacao == "atencao"
    cadeia = [(301, "http://ex.com/", "https://ex.com/"), (301, "https://ex.com/", "https://www.ex.com/"),
              (302, "https://www.ex.com/", "https://www.ex.com/home")]
    assert seo.redirecionamentos(cadeia).situacao == "problema"
    assert seo.redirecionamentos([]).situacao == "ok"


def test_links_quebrados_sem_verificacao_e_nao_medido():
    assert seo.links_quebrados({}).tipo == "nao_medido"
    r = seo.links_quebrados({"verificados": 10, "quebrados": [{"url": "https://ex.com/x", "status": 404}], "falhas": []})
    assert r.situacao == "atencao"


# ---------------- Performance ----------------

def lhr(score=0.42, lcp=6400, cls=0.02, peso=5_000_000):
    return {"fonte": "pagespeed", "estrategia": "mobile", "tentativas": [], "campo": {}, "lhr": {
        "lighthouseVersion": "13.0.0", "categories": {"performance": {"score": score}},
        "audits": {
            "largest-contentful-paint": {"numericValue": lcp}, "cumulative-layout-shift": {"numericValue": cls},
            "total-byte-weight": {"numericValue": peso, "score": 0.2},
            "image-delivery-insight": {"score": 0, "title": "Melhorar a entrega de imagens",
                                       "details": {"overallSavingsMs": 1500, "overallSavingsBytes": 3_000_000}},
            "unused-css-rules": {"score": 1, "details": {"overallSavingsMs": 0}},
        }}}


def test_extrair_pagespeed():
    e = extrair(lhr())
    assert e["ok"] and e["nota"] == 42 and e["lcp_ms"] == 6400 and e["inp_ms_campo"] is None
    assert [o["id"] for o in e["oportunidades"]] == ["image-delivery-insight"]
    assert extrair({"erro": "PageSpeed respondeu 429"})["ok"] is False


def test_metricas_e_frases():
    e = extrair(lhr())
    ms = {m.id: m for m in performance.metricas(e, {"ok": False})}
    assert ms["lcp"].valor == "6,4" and ms["lcp"].status == "ruim"
    assert ms["cls"].status == "bom"
    assert "inp" not in ms   # sem dado de visitantes reais, o cartão é omitido
    assert ms["bytes"].valor == "4,8" and ms["bytes"].status == "ruim"


def test_falha_total_de_performance_vira_nao_medido():
    falha = {"ok": False, "tentativas": [{"fonte": "pagespeed", "erro": "429"}]}
    assert all(m.tipo == "nao_medido" for m in performance.metricas(falha, falha))
    assert performance.achados(falha, falha)[0].tipo == "nao_medido"
    assert performance.nota(falha, falha)[0] is None


def test_nota_performance_ponderada():
    m, d = extrair(lhr(score=0.40)), extrair(lhr(score=0.80))
    assert performance.nota(m, d)[0] == 52          # 0,7*40 + 0,3*80
    assert performance.nota(m, {"ok": False})[0] == 40


def test_oportunidade_traduzida_e_priorizada():
    acs = performance.achados(extrair(lhr()), {"ok": False})
    op = next(a for a in acs if a.id == "perf-op-image-delivery-insight")
    assert op.titulo == "Imagens mais pesadas do que o necessário" and op.prioridade == "alta"
    assert any(a.id == "perf-lcp" and not a.secao for a in acs)


# ---------------- Pontuação, resumo e plano ----------------

def ach(id_, situacao, peso=1, tipo="medido", prioridade="", impacto="", correcao="", categoria="seo"):
    return Achado(id_, categoria, id_, tipo, situacao, "x", peso=peso, prioridade=prioridade, impacto=impacto,
                  correcao=correcao, esforco="rápido (horas)")


def test_nota_ponderada_ignora_avaliacao_e_nao_medido():
    n = nota_por_criterios("SEO", [ach("a", "ok", 2), ach("b", "problema", 1), ach("c", "atencao", 1),
                                   ach("d", "na", 3, tipo="nao_medido"), ach("e", "atencao", 0, tipo="avaliacao")])
    assert n.nota == round(100 * (2 + 0 + 0.5) / 4)
    assert n.criterios_medidos == 3 and n.criterios_total == 4


def test_nota_sem_criterios_medidos_e_none():
    n = nota_por_criterios("UX", [ach("d", "na", 3, tipo="nao_medido")])
    assert n.nota is None and n.rotulo == "Não foi possível medir"


def test_top3_prioriza_alta_e_exige_impacto():
    acs = [ach("baixa", "problema", prioridade="baixa", impacto="i"),
           ach("alta", "problema", prioridade="alta", impacto="i", categoria="ux"),
           ach("sem-impacto", "problema", prioridade="alta"),
           ach("media", "problema", prioridade="media", impacto="i"),
           ach("julgamento", "atencao", tipo="avaliacao", prioridade="alta", impacto="i")]
    assert [t["titulo"] for t in top3(acs)] == ["alta", "media", "baixa"]


def test_plano_agrupa_por_prioridade_sem_duplicar():
    acs = [ach("a", "problema", prioridade="alta", correcao="Fazer X"),
           ach("b", "problema", prioridade="alta", correcao="Fazer X"),
           ach("c", "atencao", prioridade="baixa", correcao="Fazer Y"),
           ach("d", "ok", prioridade="alta", correcao="Nada")]
    fases = {f["chave"]: [i["acao"] for i in f["itens"]] for f in plano(acs)}
    assert fases == {"alta": ["Fazer X"], "media": [], "baixa": ["Fazer Y"]}


# ---------------- Rastreador e tecnologias ----------------

def test_escolher_paginas_prioriza_menu_e_palavras_relevantes():
    html = """<header><nav><a href="/">Home</a><a href="/servicos/">Serviços</a><a href="/contato">Contato</a>
    <a href="/blog/">Blog</a></nav></header><a href="/wp-admin/">admin</a><a href="https://outro.com/x">x</a>
    <a href="/arquivo.pdf">pdf</a><a href="/politica-de-privacidade">p</a>"""
    sitemap = ["https://ex.com/sobre/", "https://ex.com/tag/x/"]
    urls = [p["url"] for p in escolher_paginas("https://ex.com/", html, sitemap, 4)]
    assert urls[:2] == ["https://ex.com/contato", "https://ex.com/servicos/"]
    assert "https://ex.com/sobre/" in urls
    assert not any("wp-admin" in u or "outro.com" in u or ".pdf" in u or "tag/" in u or "politica" in u for u in urls)


def test_urls_do_sitemap():
    assert urls_do_sitemap("<urlset><url><loc> https://ex.com/a </loc></url><url><loc>https://ex.com/b</loc></url></urlset>") == [
        "https://ex.com/a", "https://ex.com/b"]


def test_tecnologias_detecta_so_com_assinatura_inequivoca():
    html = ('<link href="/wp-content/themes/x/style.css"><div class="elementor-kit-12"></div>'
            '<script src="https://www.googletagmanager.com/gtag/js?id=G-ABC123"></script>'
            '<p>Somos parceiros RD Station e usamos Wix no passado.</p>')
    nomes = {t.nome for t in tecnologias.detectar([html], {"server": "cloudflare"})}
    assert {"WordPress", "Elementor", "Google Analytics 4", "Cloudflare"} <= nomes
    assert "RD Station" not in nomes and "Wix" not in nomes


def test_pixel_de_rastreamento_nao_conta_como_imagem_sem_alt():
    html = ('<img src="a.jpg" alt="x"><noscript><img src="https://www.facebook.com/tr?id=1"></noscript>'
            '<img src="p.gif" width="1" height="1">')
    p = seo.extrair_pagina("https://ex.com/", html)
    assert p["imagens"] == 1 and p["imagens_sem_alt"] == []


def test_concordancia_no_plural():
    pags = [seo.extrair_pagina(f"https://ex.com/{i}", HTML_RUIM) for i in range(2)]
    assert "2 páginas pulam" in seo.hierarquia(pags).o_que_vimos
    assert "1 página pula" in seo.hierarquia(pags[:1]).o_que_vimos
