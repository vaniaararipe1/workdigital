"""Detecção conservadora de ferramentas e tecnologias.

Cada assinatura exige um padrão inequívoco no HTML ou nos cabeçalhos HTTP.
Na dúvida, a tecnologia não é listada.
"""
from __future__ import annotations

import re

from ..modelos import Tecnologia

# (nome, categoria, regex sobre o HTML)
ASSINATURAS_HTML = [
    ("WordPress", "Gerenciador de conteúdo", r"/wp-content/|/wp-includes/|<meta[^>]+generator[^>]+WordPress"),
    ("Wix", "Construtor de sites", r"static\.wixstatic\.com|<meta[^>]+generator[^>]+Wix\.com"),
    ("Squarespace", "Construtor de sites", r"static1\.squarespace\.com|<!-- This is Squarespace"),
    ("Webflow", "Construtor de sites", r"data-wf-page=|assets\.website-files\.com|cdn\.prod\.website-files\.com"),
    ("Framer", "Construtor de sites", r"framerusercontent\.com|<meta[^>]+generator[^>]+Framer"),
    ("Shopify", "Loja virtual", r"cdn\.shopify\.com|Shopify\.theme"),
    ("Nuvemshop", "Loja virtual", r"d26lpennugtm8s\.cloudfront\.net|cdn\.nuvemshop\.com|mitiendanube\.com"),
    ("WooCommerce", "Loja virtual", r"/plugins/woocommerce/|class=\"[^\"]*woocommerce"),
    ("Wix Studio / Editor X", "Construtor de sites", r"<meta[^>]+generator[^>]+Wix Studio"),
    ("Elementor", "Construtor de páginas", r"/plugins/elementor/|elementor-kit-\d+|class=\"[^\"]*elementor-section"),
    ("Divi", "Construtor de páginas", r"/themes/Divi/|et_pb_section"),
    ("WPBakery", "Construtor de páginas", r"/plugins/js_composer/|vc_row wpb_row"),
    ("Next.js", "Tecnologia do site", r"id=\"__NEXT_DATA__\"|/_next/static/"),
    ("Google Analytics 4", "Análise de visitas", r"googletagmanager\.com/gtag/js\?id=G-|gtag\(\s*['\"]config['\"]\s*,\s*['\"]G-"),
    ("Google Tag Manager", "Gerenciador de tags", r"googletagmanager\.com/gtm\.js|GTM-[A-Z0-9]{4,}"),
    ("Google Ads (conversões)", "Anúncios", r"gtag/js\?id=AW-|['\"]AW-\d{6,}"),
    ("Meta Pixel", "Anúncios", r"connect\.facebook\.net/[^\"']+/fbevents\.js|fbq\(\s*['\"]init"),
    ("TikTok Pixel", "Anúncios", r"analytics\.tiktok\.com/i18n/pixel"),
    ("LinkedIn Insight", "Anúncios", r"snap\.licdn\.com/li\.lms-analytics"),
    ("Hotjar", "Análise de comportamento", r"static\.hotjar\.com|hjid\s*:"),
    ("Microsoft Clarity", "Análise de comportamento", r"clarity\.ms/tag"),
    ("RD Station", "Automação de marketing", r"<script[^>]+src=[\"'][^\"']*(?:d335luupugsy2\.cloudfront\.net|rdstation)|RDStationForms\("),
    ("HubSpot", "Automação de marketing", r"js\.hs-scripts\.com|js\.hsforms\.net"),
    ("Tawk.to", "Chat", r"embed\.tawk\.to"),
    ("JivoChat", "Chat", r"code\.jivosite\.com|code\.jivo\.chat"),
    ("Zendesk Chat", "Chat", r"static\.zdassets\.com"),
    ("Intercom", "Chat", r"widget\.intercom\.io"),
    ("Crisp", "Chat", r"client\.crisp\.chat"),
    ("Joinchat (botão de WhatsApp)", "Chat", r"/plugins/creame-whatsapp-me/|class=\"[^\"]*joinchat"),
    ("Yoast SEO", "Plugin de SEO", r"Yoast SEO plugin|yoast-schema-graph"),
    ("Rank Math", "Plugin de SEO", r"rank-math-schema|class=\"rank-math"),
    ("reCAPTCHA", "Proteção de formulário", r"google\.com/recaptcha/"),
]

ASSINATURAS_CABECALHO = [
    ("Cloudflare", "Rede de entrega (CDN)", "server", r"^cloudflare$"),
    ("Vercel", "Hospedagem", "server", r"^Vercel$"),
    ("Netlify", "Hospedagem", "server", r"^Netlify$"),
    ("LiteSpeed", "Servidor", "server", r"^LiteSpeed$"),
]


def detectar(htmls: list[str], cabecalhos: dict | None = None) -> list[Tecnologia]:
    texto = "\n".join(h for h in htmls if h)
    achados: dict[str, Tecnologia] = {}
    for nome, cat, padrao in ASSINATURAS_HTML:
        m = re.search(padrao, texto, re.I)
        if m:
            achados[nome] = Tecnologia(nome, cat, m.group(0)[:80])
    for nome, cat, cab, padrao in ASSINATURAS_CABECALHO:
        valor = (cabecalhos or {}).get(cab, "")
        if valor and re.search(padrao, valor.strip(), re.I):
            achados[nome] = Tecnologia(nome, cat, f"{cab}: {valor[:60]}")
    if "Wix Studio / Editor X" in achados:
        achados.pop("Wix", None)
    if "WooCommerce" in achados and "WordPress" not in achados:
        achados.pop("WooCommerce")   # assinatura só é confiável junto com WordPress
    ordem = {c: i for i, c in enumerate(dict.fromkeys(c for _, c, _ in ASSINATURAS_HTML))}
    return sorted(achados.values(), key=lambda t: (ordem.get(t.categoria, 99), t.nome))
