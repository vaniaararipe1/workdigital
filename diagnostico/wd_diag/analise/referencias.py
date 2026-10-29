"""Recomendação e fonte de cada critério medido.

Regra de integridade: só citamos um órgão quando a recomendação é dele, de fato. Quando o limite usado pela
ferramenta não vem de uma norma oficial, a fonte diz isso ("boa prática de mercado"), sem atribuir a ninguém.
Os números aqui são os mesmos usados nas regras de análise (ver CRITERIOS.md).
"""
from __future__ import annotations

MERCADO = "boa prática de mercado (não há norma oficial)"

# id do critério → (recomendado, fonte)
REFERENCIAS: dict[str, tuple[str, str]] = {
    "perf-lcp": ("mostrar o conteúdo principal em até 2,5 s", "Google, Core Web Vitals"),
    "perf-cls": ("índice de estabilidade visual (CLS) de até 0,1", "Google, Core Web Vitals"),
    "perf-op": ("corrigir os itens que a medição aponta como oportunidade de ganho de velocidade",
                "Google Lighthouse (PageSpeed Insights)"),
    "ux-viewport": ("página que se ajusta à largura da tela do celular (design responsivo)",
                    "Google Search Central, guia de indexação para celular"),
    "ux-toque": ("botões e links com pelo menos 24×24 px; o ideal é 44×44 px",
                 "W3C, WCAG 2.2 (critérios 2.5.8 e 2.5.5)"),
    "ux-leitura": ("texto com pelo menos 12 px no celular", "Google Lighthouse, auditoria de tamanho de fonte legível"),
    "ux-form": ("rótulo visível em cada campo (W3C, WCAG 2.2, critério 3.3.2) e poucos campos, até 6",
                "W3C para os rótulos; o número de campos é " + MERCADO),
    "ux-whatsapp": ("botão de WhatsApp visível na página inicial", MERCADO),
    "ux-tel-email": ("telefone e e-mail clicáveis", MERCADO),
    "ux-cta-mobile": ("um botão de ação visível já na primeira tela do celular", MERCADO),
    "ux-cta-desktop": ("um botão de ação visível já na primeira tela do computador", MERCADO),
    "seo-title": ("um título único e descritivo por página; até cerca de 60 caracteres para não ser cortado",
                  "Google Search Central (título único e descritivo); o limite de caracteres é " + MERCADO),
    "seo-title-dup": ("um título diferente para cada página", "Google Search Central"),
    "seo-desc": ("uma descrição própria para cada página; de 50 a 160 caracteres",
                 "Google Search Central (descrição própria); o tamanho é " + MERCADO),
    "seo-h1": ("um título principal (H1) claro em cada página; usar um só é o mais comum",
               MERCADO + "; o Google aceita mais de um H1"),
    "seo-hierarquia": ("subtítulos em ordem, sem pular níveis (H2, depois H3)", "W3C, tutorial de acessibilidade sobre títulos"),
    "seo-canonical": ("indicar o endereço oficial de cada página (canonical)", "Google Search Central"),
    "seo-noindex": ("páginas importantes sem o bloqueio “noindex”", "Google Search Central"),
    "seo-robots": ("robots.txt que não bloqueie as páginas que devem aparecer nas buscas",
                   "Google Search Central e norma RFC 9309"),
    "seo-sitemap": ("ter um sitemap.xml e informá-lo ao Google", "Google Search Central e protocolo sitemaps.org"),
    "seo-https": ("site inteiro em HTTPS", "Google Search Central (experiência na página)"),
    "seo-redirect": ("chegar à página inicial sem cadeia de redirecionamentos", "Google Lighthouse"),
    "seo-urls": ("endereços simples e legíveis, com palavras", "Google Search Central, estrutura de URLs"),
    "seo-alt": ("texto alternativo em todas as imagens com conteúdo", "W3C, WCAG 2.2 (critério 1.1.1) e Google Search Central"),
    "seo-links": ("nenhum link interno levando a página de erro", MERCADO),
    "seo-schema": ("dados estruturados que descrevem a empresa e o conteúdo", "Google Search Central e schema.org"),
    "geo-org": ("dados estruturados de organização (nome, logo, contatos)", "Google Search Central e schema.org"),
    "geo-faq": ("conteúdo que responde às perguntas frequentes dos clientes", MERCADO),
    "seo-og": ("título, descrição e imagem de 1200×630 px para a prévia de compartilhamento",
               "protocolo Open Graph (ogp.me) e Meta"),
    "geo-llms": ("arquivo llms.txt com um resumo do site para IAs", "proposta llmstxt.org (ainda não é padrão oficial)"),
}


def referencia(achado_id: str) -> dict | None:
    """{"recomendado", "fonte"} do critério, ou None quando não há referência cadastrada."""
    chave = "perf-op" if achado_id.startswith("perf-op-") else achado_id
    ref = REFERENCIAS.get(chave)
    return {"recomendado": ref[0], "fonte": ref[1]} if ref else None
