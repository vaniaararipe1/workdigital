"""A página de contato é sempre procurada: menu/rodapé/sitemap e visita direta a /contato e /fale-conosco."""
from wd_diag.http import Resposta
from wd_diag.pipeline import garantir_pagina_contato


class ClienteFalso:
    def __init__(self, existentes):
        self.existentes = existentes
        self.visitadas = []

    def get(self, url, **kw):
        self.visitadas.append(url)
        r = Resposta(url=url)
        if any(url.endswith(x) for x in self.existentes):
            r.status, r.url_final, r.headers = 200, url, {"content-type": "text/html"}
        else:
            r.status = 404
        return r


def test_visita_contato_mesmo_quando_menu_aponta_para_outra_pagina():
    # Caso real: menu leva a /contato1/ (sem formulário) e o formulário está em /contato/.
    cliente = ClienteFalso(["/contato/"])
    escolhidas = [{"url": "https://ex.com/contato1/", "origem": "menu"}, {"url": "https://ex.com/sobre/", "origem": "menu"}]
    ordem, busca = garantir_pagina_contato(cliente, "https://ex.com/", escolhidas)
    urls = [e["url"] for e in ordem]
    assert urls[:2] == ["https://ex.com/contato1/", "https://ex.com/contato/"]
    assert "https://ex.com/fale-conosco/" in cliente.visitadas


def test_sem_pagina_de_contato_registra_tentativas():
    cliente = ClienteFalso([])
    ordem, busca = garantir_pagina_contato(cliente, "https://ex.com/", [{"url": "https://ex.com/sobre/", "origem": "menu"}])
    assert [e["url"] for e in ordem] == ["https://ex.com/sobre/"]
    assert busca["tentativas"] == ["/contato/", "/fale-conosco/", "/contact/"]
