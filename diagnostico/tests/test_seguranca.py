import pytest

from wd_diag.seguranca import UrlInvalida, host_permitido, ip_e_publico, normalizar, validar_entrada, verificar_url


def dns_falso(tabela):
    def resolver(host):
        if host not in tabela:
            raise UrlInvalida(f"não foi possível encontrar o endereço {host}")
        return tabela[host]
    return resolver


PUBLICO = dns_falso({"exemplo.com.br": ("93.184.216.34",), "www.exemplo.com.br": ("93.184.216.34",),
                     "interno.exemplo.com": ("10.0.0.5",), "misto.exemplo.com": ("93.184.216.34", "192.168.0.1"),
                     "v6.exemplo.com": ("2606:2800:220:1::1",), "loop6.exemplo.com": ("::1",),
                     "mapeado.exemplo.com": ("::ffff:127.0.0.1",)})


def test_normaliza_sem_esquema():
    assert normalizar(" exemplo.com.br ") == "https://exemplo.com.br"


def test_aceita_url_publica():
    assert verificar_url("https://exemplo.com.br", resolver_dns=PUBLICO) == "https://exemplo.com.br/"
    assert verificar_url("http://www.exemplo.com.br/servicos?x=1#topo", resolver_dns=PUBLICO) == "http://www.exemplo.com.br/servicos?x=1"
    assert verificar_url("https://v6.exemplo.com/", resolver_dns=PUBLICO)


@pytest.mark.parametrize("url", [
    "ftp://exemplo.com.br", "file:///etc/passwd", "javascript:alert(1)", "gopher://exemplo.com.br", "data:text/html,oi",
])
def test_recusa_esquemas(url):
    with pytest.raises(UrlInvalida):
        verificar_url(url, resolver_dns=PUBLICO)


@pytest.mark.parametrize("url", [
    "http://localhost/", "http://127.0.0.1/", "http://127.1/", "http://0.0.0.0/", "http://10.1.2.3/",
    "http://172.16.0.1/", "http://192.168.1.1/", "http://169.254.169.254/latest/meta-data/", "http://[::1]/",
    "http://[fd00::1]/", "http://100.64.0.1/", "http://servidor.local/", "http://app.internal/", "http://intranet/",
    "https://interno.exemplo.com/", "https://misto.exemplo.com/", "https://loop6.exemplo.com/",
    "https://mapeado.exemplo.com/",
])
def test_recusa_rede_interna(url):
    with pytest.raises(UrlInvalida):
        verificar_url(url, resolver_dns=PUBLICO)


def test_recusa_ip_decimal_que_resolve_para_loopback():
    # "2130706433" é 127.0.0.1 em notação decimal; o resolvedor real converte.
    with pytest.raises(UrlInvalida):
        verificar_url("http://2130706433/")


def test_recusa_credenciais_e_portas():
    with pytest.raises(UrlInvalida):
        verificar_url("https://user:senha@exemplo.com.br/", resolver_dns=PUBLICO)
    with pytest.raises(UrlInvalida):
        verificar_url("https://exemplo.com.br:8080/", resolver_dns=PUBLICO)
    assert verificar_url("https://exemplo.com.br:443/", resolver_dns=PUBLICO) == "https://exemplo.com.br:443/"


def test_recusa_dominio_inexistente_e_vazio():
    with pytest.raises(UrlInvalida):
        verificar_url("https://naoexiste.exemplo.com.br/", resolver_dns=PUBLICO)
    with pytest.raises(UrlInvalida):
        validar_entrada("   ")


@pytest.mark.parametrize("ip,esperado", [
    ("8.8.8.8", True), ("10.0.0.1", False), ("127.0.0.1", False), ("169.254.169.254", False),
    ("::ffff:10.0.0.1", False), ("224.0.0.1", False), ("nao-e-ip", False),
])
def test_ip_e_publico(ip, esperado):
    assert ip_e_publico(ip) is esperado


def test_host_permitido_libera_data_e_bloqueia_interno():
    cache = {}
    assert host_permitido("data:image/png;base64,AAAA", cache)
    assert not host_permitido("http://127.0.0.1:8080/admin", cache)
    assert not host_permitido("http://localhost/", cache)
