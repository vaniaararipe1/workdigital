"""Fase 2: limites de uso, status sem dados pessoais e montagem de e-mail (sem rede)."""
import json
from datetime import date, timedelta

from wd_diag.entrega import email as mail
from wd_diag.entrega import worker


def criar_pasta(dados, host, quando, origem, pdf=True):
    p = dados / "relatorios" / f"{host}-{quando.isoformat()}"
    p.mkdir(parents=True)
    (p / "lead.json").write_text(json.dumps({"origem": origem, "recebido_em": quando.isoformat() + "T10:00:00"}))
    if pdf:
        (p / "relatorio.pdf").write_bytes(b"%PDF")
    return p


def test_mesmo_site_em_7_dias_e_bloqueado_para_leads(tmp_path):
    criar_pasta(tmp_path, "ex.com.br", date.today() - timedelta(days=3), "landing")
    assert worker.verificar_limites(tmp_path, "https://www.ex.com.br/", "popup", 20)
    assert worker.verificar_limites(tmp_path, "https://ex.com.br/", "prospeccao", 20) is None


def test_prospeccao_anterior_nao_bloqueia_lead(tmp_path):
    criar_pasta(tmp_path, "ex.com.br", date.today(), "prospeccao")
    assert worker.verificar_limites(tmp_path, "https://ex.com.br/", "landing", 20) is None


def test_analise_antiga_nao_bloqueia(tmp_path):
    criar_pasta(tmp_path, "ex.com.br", date.today() - timedelta(days=10), "landing")
    assert worker.verificar_limites(tmp_path, "https://ex.com.br/", "landing", 20) is None


def test_limite_diario(tmp_path):
    for i in range(3):
        criar_pasta(tmp_path, f"site{i}.com.br", date.today(), "landing")
    assert "muitos pedidos" in worker.verificar_limites(tmp_path, "https://novo.com.br/", "landing", 3)
    assert worker.verificar_limites(tmp_path, "https://novo.com.br/", "landing", 4) is None


def test_status_nao_aceita_id_estranho_e_nao_tem_dados_pessoais(tmp_path):
    worker.status(tmp_path, "../../etc/passwd", estado="pronto")
    assert not (tmp_path / "status").exists()
    worker.status(tmp_path, "abc12345-def", estado="pronto", notas={"seo": 90})
    dados = json.loads((tmp_path / "status" / "abc12345-def.json").read_text())
    assert dados["estado"] == "pronto" and "email" not in dados


def test_email_com_anexo_e_resposta_para(tmp_path):
    pdf = tmp_path / "relatorio.pdf"
    pdf.write_bytes(b"%PDF-1.4")
    msg = mail.montar("lead@ex.com", "Assunto", mail.corpo("Olá <b>x</b>"), [pdf], "hello@workdigital.art.br", "envio@ex.com")
    assert msg["Reply-To"] == "hello@workdigital.art.br"
    assert any(p.get_filename() == "relatorio.pdf" for p in msg.iter_attachments())
    assert "Vania Araripe" in msg["From"]


def test_emails_do_lead_tem_layout_apresentacao_e_escapam_dados():
    from tests.test_relatorio import resultado
    r = resultado()
    html = worker.email_lead_automatico(r, "<script>Ana</script> Souza", 2)
    assert "<script>Ana" not in html and "&lt;script&gt;" in html
    assert "Prazer, eu sou a Vania Araripe" in html
    assert html.index("Prazer, eu sou a") < html.index("revisada por mim")
    assert "cid:logo" in html and "cid:foto" in html
    assert "não foi possível medir" in html  # performance sem medição aparece como tal, sem nota inventada
    rev = worker.email_lead_revisado(r["empresa"], r["url_final"], "Ana")
    assert "Olá, Ana!" in rev and "30 minutos" in rev


def test_imagens_vao_embutidas_na_mensagem(tmp_path):
    from tests.test_relatorio import resultado
    msg = mail.montar("lead@ex.com", "A", worker.email_lead_automatico(resultado(), "Ana", 2))
    tipos = [p.get_content_type() for p in msg.walk()]
    assert "multipart/related" in tipos and "image/png" in tipos and "image/jpeg" in tipos
    html = next(p for p in msg.walk() if p.get_content_type() == "text/html").get_content()
    assert "cid:logo" not in html  # trocado pelo Content-ID real


def test_email_da_vania_separa_medido_do_que_revisar():
    from tests.test_relatorio import resultado
    from wd_diag import revisao as rv
    from wd_diag.relatorio import contexto
    r = resultado()
    rev = rv.criar_rascunho(r, contexto.plano(r["achados"]))
    lead = {"nome": "Ana", "email": "ana@ex.com", "whatsapp": "(11) 98888-7777", "origem": "landing"}
    html = worker.email_vania(r, rev, lead, True, "relatorios/ex.com-2026-10-12")
    assert html.index("O que já foi analisado") < html.index("O que você precisa analisar")
    assert "Clareza da proposta de valor" in html and "[RASCUNHO]" not in html
    assert "aprovar_rascunhos" in html and "https://wa.me/5511988887777" in html
    assert "Formulário de contato" in html  # item não confirmado vai para "vale conferir"


def test_link_whatsapp_do_lead():
    assert worker.link_whatsapp_lead("(11) 98888-7777") == "https://wa.me/5511988887777"
    assert worker.link_whatsapp_lead("+55 11 98888-7777") == "https://wa.me/5511988887777"
    assert worker.link_whatsapp_lead("123") == ""
