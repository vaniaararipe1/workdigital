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
