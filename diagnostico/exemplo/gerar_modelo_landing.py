"""Relatório MODELO para a landing page: versão revisada completa, com dados 100% fictícios.

Empresa, site, notas, achados, textos de revisão e captura de tela são inventados para ilustração.
O domínio usa o sufixo reservado ".example" (RFC 2606), que não pode existir na internet.

Uso: python exemplo/gerar_modelo_landing.py
Saída: exemplo/modelo-landing/ (PDF, HTML e PNGs)
"""
from __future__ import annotations

import base64
import glob
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from wd_diag import pontuacao  # noqa: E402
from wd_diag.modelos import ESFORCO_MEDIO, ESFORCO_RAPIDO, Achado, Metrica, Nota, Tecnologia  # noqa: E402
from wd_diag.relatorio import contexto  # noqa: E402
from wd_diag.relatorio.gerar import html_para_pdf, renderizar_html  # noqa: E402

SAIDA = RAIZ / "exemplo" / "modelo-landing"
EMPRESA = "Casa Aurora"
URL = "https://www.casaaurora.example/"
DATA_EXTENSO = "12 de outubro de 2026"

SITE_FICTICIO = """<!doctype html><html><head><meta name=viewport content="width=device-width">
<style>body{margin:0;font-family:Georgia,serif;background:#faf6f0;color:#3b2f2a}
nav{display:flex;justify-content:space-between;align-items:center;background:#fff;padding:14px 16px;border-bottom:1px solid #eadfd3}
nav b{font-size:18px;letter-spacing:.04em}.menu{font-size:22px}
.hero{height:420px;background:linear-gradient(160deg,#e8c9a0,#b98a63 60%,#8d6248);color:#fff;padding:26px 18px;position:relative}
.hero h1{font-size:28px;margin:170px 0 10px;line-height:1.15}.hero p{font-size:14px;opacity:.9;margin:0}
.cards{padding:18px}.c{background:#fff;height:110px;margin-bottom:14px;border-radius:8px;box-shadow:0 1px 3px rgba(0,0,0,.08)}</style>
</head><body><nav><b>CASA AURORA</b><span class=menu>&#9776;</span></nav>
<div class=hero><h1>Bem-vindo à Casa Aurora</h1><p>Decoração e objetos para casa</p></div>
<div class=cards><div class=c></div><div class=c></div></div></body></html>"""


def _exe():
    achados = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))
    return achados[-1] if achados else None


def captura_ficticia(exe) -> str:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": 390, "height": 760}, device_scale_factor=2)
        pg.set_content(SITE_FICTICIO)
        png = pg.screenshot(type="jpeg", quality=82)
        b.close()
    return "data:image/jpeg;base64," + base64.b64encode(png).decode()


def A(id_, cat, titulo, situacao, vimos, peso, **kw) -> Achado:
    return Achado(id_, cat, titulo, kw.pop("tipo", "medido"), situacao, vimos, peso=peso, **kw)


def achados_ficticios() -> list[Achado]:
    r, m = ESFORCO_RAPIDO, ESFORCO_MEDIO
    return [
        # ---------------- Performance ----------------
        A("perf-lcp", "performance", "O site leva 5,8 s para mostrar o conteúdo principal no celular", "problema",
          "O conteúdo principal da página inicial só fica visível depois de 5,8 s. O recomendado pelo Google é até 2,5 s.", 0,
          impacto="parte dos visitantes que chegam pelo Google ou por anúncios desiste antes de ver o que você oferece.",
          correcao="Reduzir o peso da primeira tela (imagens, scripts e fontes).", prioridade="alta", esforco=m,
          area="Performance", secao=False),
        A("perf-op-image-delivery-insight", "performance", "Imagens mais pesadas do que o necessário", "problema",
          "A ferramenta de medição apontou este item na versão para celular.", 0,
          evidencia="economia estimada de <code>2,1 s</code>; redução estimada de <code>2,4 MB</code>.",
          significado="As fotos e imagens são a parte mais pesada da página e atrasam a primeira impressão.",
          correcao="Comprimir as imagens, usar formatos modernos (WebP ou AVIF) e enviar tamanhos menores para o celular.",
          prioridade="alta", esforco=r, area="Performance"),
        A("perf-op-render-blocking-insight", "performance", "Arquivos que travam o início do carregamento", "problema",
          "A ferramenta de medição apontou este item na versão para celular.", 0,
          evidencia="economia estimada de <code>0,9 s</code>.",
          significado="A tela fica em branco enquanto o navegador espera alguns arquivos de estilo e código.",
          correcao="Adiar ou carregar de forma assíncrona os arquivos que não são essenciais para a primeira tela.",
          prioridade="media", esforco=m, area="Performance"),
        A("perf-op-unused-javascript", "performance", "Código que é baixado mas não é usado", "problema",
          "A ferramenta de medição apontou este item na versão para celular.", 0,
          evidencia="redução estimada de <code>0,6 MB</code>.",
          significado="O visitante baixa programação que a página não utiliza, geralmente de plugins e ferramentas externas.",
          correcao="Remover plugins sem uso e carregar scripts só nas páginas que precisam deles.",
          prioridade="baixa", esforco=m, area="Performance"),
        # ---------------- Experiência e conversão ----------------
        A("ux-cta-mobile", "ux", "Chamada para ação na primeira tela (celular)", "problema",
          "No celular, nenhum botão de ação aparece antes de rolar a página.", 3,
          evidencia="primeiro botão de ação (<code>Ver coleção</code>) a 1.180 px do topo; a tela tem 844 px de altura.",
          significado="O visitante não recebe um convite claro para agir na primeira impressão.",
          correcao="Colocar um botão de destaque (por exemplo, \"Comprar pelo WhatsApp\") logo abaixo do título.",
          impacto="quem chega com intenção de compra precisa procurar como falar com você, e parte desiste.",
          prioridade="alta", esforco=r, area="Conversão"),
        A("ux-cta-desktop", "ux", "Chamada para ação na primeira tela (computador)", "ok",
          "Há um botão de ação visível sem precisar rolar a página no computador.", 2,
          evidencia="<code>Ver coleção</code> a 520 px do topo; a tela tem 768 px de altura.", area="Conversão"),
        A("ux-whatsapp", "ux", "Link de WhatsApp", "atencao",
          "A página inicial no celular tem link de WhatsApp, mas ele só aparece depois de rolar a página.", 3,
          evidencia="<code>https://wa.me/55000000000</code> a 2.640 px do topo; presente em 3 páginas das 5 analisadas.",
          significado="O caminho mais curto até a conversa fica escondido para quem não rola a página.",
          correcao="Adicionar um botão de WhatsApp fixo no canto da tela do celular.",
          impacto="parte dos visitantes não encontra o jeito mais rápido de falar com você.",
          prioridade="media", esforco=r, area="Conversão"),
        A("ux-tel-email", "ux", "Telefone e e-mail clicáveis", "ok", "O site tem telefone e e-mail clicáveis.", 1,
          evidencia="encontrados: telefone <code>tel:+550000000000</code>; e-mail <code>mailto:contato@casaaurora.example</code>.",
          area="Conversão"),
        A("ux-form", "ux", "Formulário de contato", "atencao",
          "O formulário principal tem 8 campos e 3 campos sem rótulo (só com texto de exemplo dentro do campo, que some ao digitar).", 2,
          evidencia="encontrado na página <code>/contato/</code>: 8 campos, 5 com rótulo identificável.",
          significado="Rótulos claros e poucos campos facilitam o preenchimento, inclusive para leitores de tela.",
          correcao="Manter até 6 campos e colocar um rótulo visível acima de cada um.",
          prioridade="baixa", esforco=r, area="Conversão"),
        A("ux-viewport", "ux", "Site adaptado ao celular", "ok", "A página se ajusta à largura do celular, sem rolagem lateral.", 2,
          area="Experiência"),
        A("ux-toque", "ux", "Botões e links fáceis de tocar", "atencao",
          "18% dos botões e links da página inicial são pequenos demais para tocar com o dedo.", 1,
          evidencia="7 de 39 elementos clicáveis com menos de <code>24×24 px</code>.",
          significado="Alvos pequenos causam toques errados, principalmente para pessoas com mais idade.",
          correcao="Aumentar a área de toque de ícones e links para pelo menos 44 px.", prioridade="baixa", esforco=r,
          area="Experiência"),
        A("ux-leitura", "ux", "Leitura confortável no celular", "ok",
          "4% do texto da página inicial no celular está com letra menor que 12 px.", 1, area="Experiência"),
        # ---------------- SEO e visibilidade ----------------
        A("seo-noindex", "seo", "Páginas liberadas para o Google", "ok",
          "Nenhuma página analisada pede ao Google para não aparecer nas buscas.", 3),
        A("seo-title", "seo", "Título das páginas no Google", "ok", "Todas as 5 páginas analisadas têm título com tamanho adequado.", 2),
        A("seo-title-dup", "seo", "Títulos repetidos entre páginas", "ok", "Cada uma das 5 páginas tem um título diferente.", 1.5),
        A("seo-desc", "seo", "Descrição das páginas (meta description)", "atencao", "2 de 5 páginas não têm descrição.", 1.5,
          evidencia="sem descrição: <code>/sobre/</code>, <code>/contato/</code>.",
          significado="É o texto que costuma aparecer abaixo do título no Google. Sem ela, o Google escolhe um trecho qualquer da página.",
          correcao="Escrever uma frase de até 155 caracteres para cada página, com um convite para clicar.",
          prioridade="baixa", esforco=r),
        A("seo-h1", "seo", "Título principal único em cada página (H1)", "ok", "Todas as 5 páginas têm exatamente um título principal (H1).", 1.5),
        A("seo-hierarquia", "seo", "Hierarquia de títulos", "ok", "Os títulos e subtítulos seguem uma ordem lógica.", 0.5),
        A("seo-canonical", "seo", "Endereço oficial das páginas (canonical)", "ok", "Todas as páginas indicam o próprio endereço oficial (canonical).", 1),
        A("seo-https", "seo", "Endereço seguro (HTTPS)", "ok", "O site usa HTTPS e redireciona a versão sem segurança para a segura.", 2),
        A("seo-redirect", "seo", "Redirecionamentos até a página inicial", "ok", "O endereço informado abre direto, sem redirecionamentos.", 0.5),
        A("seo-robots", "seo", "Arquivo de instruções para buscadores (robots.txt)", "ok", "O arquivo robots.txt existe e permite o acesso dos buscadores.", 1),
        A("seo-sitemap", "seo", "Mapa do site (sitemap.xml)", "ok", "O mapa do site existe e lista 38 endereços.", 1),
        A("seo-urls", "seo", "Endereços das páginas legíveis", "ok", "Os endereços das páginas são curtos e legíveis.", 0.5),
        A("seo-alt", "seo", "Imagens com texto alternativo", "atencao", "11 de 52 imagens não têm texto alternativo.", 1,
          significado="O texto alternativo descreve a imagem para o Google e para pessoas com deficiência visual que usam leitores de tela.",
          correcao="Descrever brevemente cada imagem importante (produtos, ambientes, equipe).", prioridade="baixa", esforco=r),
        A("seo-links", "seo", "Links internos quebrados", "ok", "Verificamos 40 links internos e todos funcionam.", 1.5),
        A("seo-og", "seo", "Prévia ao compartilhar o link (Open Graph)", "ok",
          "A página inicial tem título, descrição e imagem para a prévia de compartilhamento.", 0.5),
        A("seo-schema", "seo", "Dados estruturados (schema.org)", "ok", "O site usa dados estruturados: BreadcrumbList, WebPage, WebSite.", 1),
        A("geo-org", "seo", "Identificação da empresa para buscas com IA", "problema",
          "Não há dados estruturados que identifiquem a empresa (schema.org Organization ou LocalBusiness).", 1,
          significado="Assistentes como ChatGPT, Gemini e a busca com IA do Google usam essas informações para citar e recomendar empresas.",
          correcao="Adicionar o bloco Organization ou LocalBusiness com nome, logo, telefone e redes sociais.",
          prioridade="media", esforco=r, area="SEO e IA"),
        A("geo-faq", "seo", "Conteúdo que responde perguntas diretas", "atencao",
          "Encontramos 1 subtítulo em formato de pergunta, mas não há seção de perguntas frequentes.", 0.5,
          significado="Buscas com IA priorizam conteúdo que responde perguntas de forma direta, como \"qual o prazo de entrega\".",
          correcao="Criar uma seção de perguntas frequentes com as dúvidas reais dos clientes.", prioridade="baixa", esforco=r,
          area="SEO e IA"),
        A("geo-llms", "seo", "Arquivo de orientação para IAs (llms.txt)", "atencao", "O site não tem arquivo llms.txt.", 0.25,
          significado="O llms.txt é um padrão recente que resume o site para assistentes de IA. Ainda é pouco adotado, por isso tem peso baixo.",
          correcao="Criar um llms.txt com a descrição da empresa, produtos e páginas principais.", prioridade="baixa", esforco=r,
          area="SEO e IA"),
    ]


def metricas_ficticias() -> list[Metrica]:
    return [
        Metrica("lcp", "Tempo até o conteúdo principal aparecer", "Maior elemento visível carregado (LCP)", "5,8", "s", "ruim",
                "medido", "Bom: até 2,5 s · Ruim: acima de 4 s",
                "No celular: O visitante olha para uma tela incompleta por tempo demais. Muita gente desiste e volta para a busca antes de ver a sua oferta."),
        Metrica("cls", "Estabilidade da página enquanto carrega", "Mudança inesperada de layout (CLS)", "0,06", "", "bom", "medido",
                "Bom: até 0,1 · Ruim: acima de 0,25", "Os elementos ficam no lugar enquanto a página carrega. Ponto positivo."),
        Metrica("inp", "Resposta ao toque e ao clique", "Interação até a próxima pintura (INP), dado de visitantes reais", "240", "ms",
                "medio", "medido", "Bom: até 200 ms · Ruim: acima de 500 ms", "Há um pequeno atraso entre o toque e a resposta da página."),
        Metrica("bytes", "Peso da página inicial", "Total transferido para abrir a página", "3,9", "MB", "medio", "medido",
                "Referência: até 2 MB", "Página um pouco pesada para conexões móveis."),
    ]


def revisao_ficticia() -> dict:
    return {
        "demonstracao": False,
        "nota_pessoal": {"status": "revisado", "texto": (
            "Olá, equipe da Casa Aurora! Revisei o site de vocês com calma. A vitrine é bonita e o conteúdo está bem "
            "organizado para o Google, o que é um ótimo ponto de partida. O que mais pesa hoje é o celular: a página "
            "demora para aparecer e o visitante não encontra um convite claro para comprar ou chamar no WhatsApp. São "
            "ajustes rápidos, com efeito direto nas vendas. Separei abaixo um plano em ordem de impacto.")},
        "avaliacoes": [
            {"id": "ux-proposta", "titulo": "Clareza da proposta de valor no título principal", "status": "revisado",
             "situacao": "atencao", "o_que_vimos": "O título principal é “Bem-vindo à Casa Aurora”.",
             "o_que_significa": "A frase é acolhedora, mas não diz o que a loja vende nem por que comprar ali. Quem chega pelo Google decide em poucos segundos se ficou no lugar certo.",
             "o_que_fazer": "Trocar por um título que diga o que é e o diferencial, como “Decoração artesanal com entrega para todo o Brasil”.",
             "prioridade": "alta", "esforco": ESFORCO_RAPIDO},
            {"id": "ux-social", "titulo": "Prova social visível", "status": "revisado", "situacao": "atencao",
             "o_que_vimos": "Há avaliações de clientes, mas só na página de cada produto. A página inicial não mostra nenhuma.",
             "o_que_significa": "Quem ainda não conhece a loja procura sinais de confiança logo de início. Hoje eles estão escondidos.",
             "o_que_fazer": "Levar 3 avaliações curtas, ou a nota média dos clientes, para a primeira metade da página inicial.",
             "prioridade": "media", "esforco": ESFORCO_RAPIDO},
        ],
        "plano": {"status": "revisado", "itens": [
            {"fase": "Fazer primeiro", "acao": "Botão de WhatsApp fixo no celular e chamada para ação logo abaixo do título", "area": "Conversão", "esforco": ESFORCO_RAPIDO},
            {"fase": "Fazer primeiro", "acao": "Comprimir e converter as imagens da página inicial", "area": "Performance", "esforco": ESFORCO_RAPIDO},
            {"fase": "Fazer primeiro", "acao": "Reescrever o título principal com o que a loja vende e o diferencial", "area": "Conversão", "esforco": ESFORCO_RAPIDO},
            {"fase": "Em seguida", "acao": "Adiar os arquivos que travam o início do carregamento", "area": "Performance", "esforco": ESFORCO_MEDIO},
            {"fase": "Em seguida", "acao": "Mostrar avaliações de clientes na página inicial", "area": "Conversão", "esforco": ESFORCO_RAPIDO},
            {"fase": "Em seguida", "acao": "Dados estruturados de empresa para buscas com IA", "area": "SEO e IA", "esforco": ESFORCO_RAPIDO},
            {"fase": "Quando possível", "acao": "Formulário com até 6 campos e rótulos visíveis", "area": "Conversão", "esforco": ESFORCO_RAPIDO},
            {"fase": "Quando possível", "acao": "Descrições das páginas e textos alternativos das imagens", "area": "SEO", "esforco": ESFORCO_RAPIDO},
            {"fase": "Quando possível", "acao": "Seção de perguntas frequentes", "area": "SEO e IA", "esforco": ESFORCO_RAPIDO},
        ]},
    }


def resultado_ficticio(captura: str | None) -> dict:
    achados = achados_ficticios()
    notas = {
        "performance": Nota("Performance", 38, 2, 2, [{"criterio": "Nota Lighthouse (Celular)", "valor": 31, "peso": 0.7},
                                                       {"criterio": "Nota Lighthouse (Computador)", "valor": 55, "peso": 0.3}]),
        "ux": pontuacao.nota_por_criterios("Experiência e conversão", [a for a in achados if a.categoria == "ux"]),
        "seo": pontuacao.nota_por_criterios("SEO e visibilidade", [a for a in achados if a.categoria == "seo"]),
    }
    return {
        "empresa": EMPRESA, "url_final": URL, "data": "2026-10-12", "data_extenso": DATA_EXTENSO,
        "achados": achados, "metricas": metricas_ficticias(), "notas": notas,
        "tecnologias": [Tecnologia("WordPress", "Gerenciador de conteúdo", "-"), Tecnologia("WooCommerce", "Loja virtual", "-"),
                        Tecnologia("Elementor", "Construtor de páginas", "-"), Tecnologia("Google Analytics 4", "Análise de visitas", "-"),
                        Tecnologia("Meta Pixel", "Anúncios", "-")],
        "performance": {"mobile": {"ok": True, "nota": 31}, "desktop": {"ok": True, "nota": 55},
                        "fonte_texto": "Fonte: Google PageSpeed Insights. Valores ilustrativos deste exemplo."},
        "paginas_resumo": [{"url": URL + p, "situacao": "aberta (código 200)"} for p in ("", "colecoes/", "sobre/", "contato/", "entregas/")],
        "captura_mobile": captura,
    }


def main() -> None:
    exe = _exe()
    SAIDA.mkdir(parents=True, exist_ok=True)
    captura = captura_ficticia(exe)
    r = resultado_ficticio(None)
    ctx = contexto.montar(r, "revisada", revisao_ficticia())
    ctx.update(captura_mobile=captura, exemplo_ilustrativo=True,
               whatsapp_url="https://wa.me/5511993916363?text=Ol%C3%A1!%20Vi%20o%20exemplo%20de%20diagn%C3%B3stico%20e%20quero%20o%20meu.")
    print("Notas:", {k: v.nota for k, v in r["notas"].items()})
    html = renderizar_html(ctx)
    caminho_html = SAIDA / "modelo-diagnostico-work-digital.html"
    caminho_html.write_text(html, encoding="utf-8")
    html_para_pdf(caminho_html, SAIDA / "modelo-diagnostico-work-digital.pdf", exe)
    print("Gerado em", SAIDA)


if __name__ == "__main__":
    main()
