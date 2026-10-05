# SEO e acessibilidade em todas as páginas (Fase 1):
# idioma, link "Pular para o conteúdo", anel de foco, botão "Pausar animações", meta description,
# canonical, Open Graph, Twitter, JSON-LD, largura/altura das imagens e títulos.
import html as H, json, os, re, subprocess
SITE = 'https://workdigital.art.br'          # domínio final (endereços abaixo são os previstos para o site publicado)
LOGO = SITE + '/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg'
SOCIAL = ['https://www.instagram.com/workdigitalbr/', 'https://www.facebook.com/workdigital.global', 'https://www.linkedin.com/company/workdigitalbr']
ORG = {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'Work Digital', 'url': SITE + '/', 'logo': LOGO,
       'sameAs': SOCIAL, 'telephone': '+55 11 99391-6363', 'areaServed': 'BR',
       'contactPoint': {'@type': 'ContactPoint', 'telephone': '+55 11 99391-6363', 'contactType': 'sales', 'availableLanguage': ['pt-BR']}}
PAGES = {
    'home.html': ('/', 'website', 'Criação de sites profissionais, blogs, landing pages e lojas virtuais sob medida. A Work Digital cria sites rápidos, bonitos e prontos para vender.'),
    'solucoes.html': ('/solucoes/', 'website', 'Sites, blogs, landing pages e lojas virtuais sob medida. Conheça os planos da Work Digital: blog de conteúdo, site por assinatura e site personalizado.'),
    'cases.html': ('/cases/', 'website', 'Cases da Work Digital: sites, portais, lojas virtuais e blogs criados para marcas como Bacio di Latte, Linea Alimentos e CBPq.'),
    'blog.html': ('/blog/', 'website', 'Blog da Work: ideias práticas sobre criação de sites, lojas virtuais, SEO, performance e tráfego para quem quer vender mais na internet.'),
}
OG_IMG = SITE + '/media/servico-sites.jpg'
# marcador do domínio: protege canonical/og/JSON-LD da troca de links das prévias (link_pages); vira SITE no fim do build
TOKEN = '__WD_SITE__'

e = lambda s: H.escape(s or '', quote=True)
def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def meta_block(title, desc, path, typ, img):
    url = SITE + path
    return (f'<meta name="description" content="{e(desc)}">\n<link rel="canonical" href="{url}">\n'
            f'<meta name="robots" content="index,follow,max-image-preview:large">\n'
            f'<meta property="og:locale" content="pt_BR">\n<meta property="og:site_name" content="Work Digital">\n'
            f'<meta property="og:type" content="{typ}">\n<meta property="og:url" content="{url}">\n'
            f'<meta property="og:title" content="{e(title)}">\n<meta property="og:description" content="{e(desc)}">\n'
            f'<meta property="og:image" content="{img}">\n<meta name="twitter:card" content="summary_large_image">\n'
            f'<meta name="twitter:title" content="{e(title)}">\n<meta name="twitter:description" content="{e(desc)}">\n'
            f'<meta name="twitter:image" content="{img}">\n')

CSS = '''<style id="wd-a11y">
/* Acessibilidade: pular para o conteúdo, foco visível, texto só para leitores de tela, pausa das animações */
.wd-sr{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
.wd-skip{position:fixed;left:16px;top:-80px;z-index:100000;padding:12px 18px;border-radius:12px;background:#F7F6FB;color:#24123e;font:600 15px/1.2 "Space Grotesk",Arial,sans-serif;text-decoration:none;box-shadow:0 10px 30px -10px rgba(0,0,0,.5);transition:top .2s}
.wd-skip:focus{top:16px;outline:3px solid #6025E1;outline-offset:2px}
:where(a,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--wd-focus,#CBB6FF)!important;outline-offset:3px!important}
.wd-pause{position:fixed;left:16px;bottom:16px;z-index:9990;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 12px;border-radius:999px;border:1px solid rgba(189,164,255,.35);background:rgba(18,19,22,.78);color:#F7F6FB;font:500 12px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);opacity:.82;transition:opacity .2s,background .2s}
.wd-pause:hover,.wd-pause:focus-visible{opacity:1;background:rgba(96,37,225,.85)}
.wd-pause svg{width:14px;height:14px;flex:none}
.wd-pause .on{display:none}html.wd-paused .wd-pause .on{display:inline}html.wd-paused .wd-pause .off{display:none}
@media(max-width:700px){.wd-pause{width:40px;padding:0;justify-content:center}.wd-pause .t{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}}
html.wd-paused *,html.wd-paused *::before,html.wd-paused *::after{animation-play-state:paused!important}
html.wd-paused .particle-art canvas,html.wd-paused .native-particles canvas,html.wd-paused #fluid,html.wd-paused #cfluid{visibility:hidden!important}
</style>
'''
PAUSE_BTN = ('<button class="wd-pause" type="button" aria-pressed="false" data-wd-pause>'
             '<svg class="off" viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="2" width="3.5" height="12" rx="1" fill="currentColor"/><rect x="9.5" y="2" width="3.5" height="12" rx="1" fill="currentColor"/></svg>'
             '<svg class="on" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2.5v11l9-5.5z" fill="currentColor"/></svg>'
             '<span class="t"><span class="off">Pausar animações</span><span class="on">Retomar animações</span></span></button>\n')
JS = '''<script>
/* Pausar animações (WCAG 2.2.2): para animações em CSS, esconde as animações em canvas e pausa os vídeos automáticos */
(function(){
  const root=document.documentElement, btn=document.querySelector('[data-wd-pause]');
  let on=false; try{on=localStorage.getItem('wdPaused')==='1';}catch(e){}
  const auto=v=>!v.classList.contains('vm-video')&&!v.closest('.case-lb');
  function apply(){root.classList.toggle('wd-paused',on);btn&&btn.setAttribute('aria-pressed',String(on));
    if(on)document.querySelectorAll('video').forEach(v=>{if(auto(v))v.pause();});}
  document.addEventListener('play',e=>{if(on&&e.target.tagName==='VIDEO'&&auto(e.target))e.target.pause();},true);
  btn&&btn.addEventListener('click',()=>{on=!on;try{localStorage.setItem('wdPaused',on?'1':'0');}catch(e){}apply();});
  window.wdIsPaused=()=>on;
  apply();
})();
</script>
'''

def img_dims(out):
    cache = {}
    def dims(src):
        p = os.path.join(out, src.lstrip('./'))
        if p in cache: return cache[p]
        r = None
        if os.path.exists(p) and not p.endswith('.svg'):
            o = subprocess.run(['identify', '-format', '%w %h', p + '[0]'], capture_output=True, text=True).stdout.split()
            if len(o) == 2: r = o
        cache[p] = r; return r
    def fix(m):
        tag = m.group(0)
        if re.search(r'\swidth=', tag): return tag
        s = re.search(r'\ssrc="(\./[^"]+)"', tag)
        d = s and dims(s.group(1))
        return tag[:-1].rstrip('/').rstrip() + f' width="{d[0]}" height="{d[1]}">' if d else tag
    return fix

def common(t, fname, out):
    if 'id="wd-a11y"' in t: return t
    # idioma
    t = re.sub(r'(<meta charset[^>]*>)', r'\1\n<script>document.documentElement.lang="pt-BR"</script>', t, count=1)
    # "pular para o conteúdo" + botão de pausa logo no início do corpo
    m = re.search(r'<main\b([^>]*)>', t)
    if m:
        idm = re.search(r'\sid="([^"]+)"', m.group(1))
        mid = idm.group(1) if idm else 'conteudo'
        newm = m.group(0) if idm else m.group(0)[:-1] + ' id="conteudo">'
        if 'tabindex' not in newm: newm = newm[:-1] + ' tabindex="-1">'
        t = t[:m.start()] + newm + t[m.end():]
        skip = f'<a class="wd-skip" href="#{mid}">Pular para o conteúdo</a>\n' + PAUSE_BTN
        nb = t.find('<!-- End Google Tag Manager (noscript) -->')
        pos = nb + len('<!-- End Google Tag Manager (noscript) -->\n') if nb >= 0 else m.start()
        t = t[:pos] + skip + t[pos:]
    light = fname in ('blog.html', 'post.html')
    css = CSS.replace('var(--wd-focus,#CBB6FF)', 'var(--wd-focus,#6025E1)') if light else CSS
    # páginas escuras: fundo escuro garantido por baixo das animações (contraste mesmo com as animações pausadas)
    if not light: css = css.replace('</style>', 'html{background-color:#0B0B0C}\n</style>')
    t = t.replace('</title>', '</title>\n' + css, 1)
    t = t.replace('</body>', JS + '</body>', 1) if '</body>' in t else t + JS
    # largura/altura nas imagens estáticas (evita a página "pular" enquanto carrega)
    t = re.sub(r'<img\b[^>]*>', img_dims(out), t)
    # Google Fonts: uma chamada só por página (havia famílias repetidas)
    fonts = re.findall(r'<link[^>]+href="https://fonts\.googleapis\.com/css2\?[^"]+"[^>]*>', t)
    if len(fonts) > 1:
        fams = {}
        for f in fonts:
            for fam in re.findall(r'family=([^&"]+)', H.unescape(f)):
                n, _, w = fam.partition(':wght@')
                fams.setdefault(n, set()).update(w.split(';') if w else [])
        q = '&'.join('family=' + n + (':wght@' + ';'.join(sorted(ws, key=int)) if ws else '') for n, ws in fams.items())
        link = f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{q}&display=swap">'
        t = t.replace(fonts[0], link, 1)
        for f in fonts[1:]: t = t.replace(f, '', 1)
    return t

def seo_static(t, fname):
    if fname not in PAGES or 'rel="canonical"' in t: return t
    path, typ, desc = PAGES[fname]
    title = re.search(r'<title>([^<]*)</title>', t).group(1)
    graph = [ORG, {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'Work Digital', 'inLanguage': 'pt-BR', 'publisher': {'@id': SITE + '/#org'}}]
    if fname == 'solucoes.html':
        graph.append({'@type': 'Service', 'name': 'Criação de sites', 'provider': {'@id': SITE + '/#org'}, 'areaServed': 'BR',
                      'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Contrate um site profissional', 'itemListElement': [
                          {'@type': 'Offer', 'name': 'Blog de conteúdo', 'price': '995.00', 'priceCurrency': 'BRL', 'description': 'Pagamento único'},
                          {'@type': 'Offer', 'name': 'Site profissional por assinatura', 'priceCurrency': 'BRL',
                           'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': '590.00', 'priceCurrency': 'BRL', 'unitText': 'MONTH'},
                           'description': 'Suporte + hospedagem mensal'},
                          {'@type': 'Offer', 'name': 'Site profissional personalizado', 'description': 'Sob consulta'}]}})
    if fname in ('solucoes.html', 'cases.html', 'blog.html'):
        nome = {'solucoes.html': 'Soluções', 'cases.html': 'Cases', 'blog.html': 'Blog'}[fname]
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': nome, 'item': SITE + path}]})
    block = meta_block(title, desc, path, typ, OG_IMG) + ld({'@context': 'https://schema.org', '@graph': graph}) + '\n'
    return re.sub(r'(<title>[^<]*</title>)', lambda m: m.group(1) + '\n' + block, t, count=1)

# hierarquia de títulos (H1 → H2 → H3, sem saltos) e H1 legíveis por leitores de tela
HEADINGS = {
    'solucoes.html': [('<span class="big">${s.name}</span>', '<h2 class="big">${s.name}</h2>'),
                      ('.svc .big{display:block;', '.svc .big{margin:0;display:block;')],
    'post.html': [('.end h5{', '.end .end-title{'), ('<h5>', '<h2 class="end-title">'), ('</h5>', '</h2>'),
                  ('<aside class="end rv">', '<aside class="end rv" role="region" aria-label="Sobre o blog da Work">'),
                  ('<img src="${p.img}" alt="" loading="lazy">', '<img src="${p.img}" alt="" loading="lazy" decoding="async" width="1600" height="900">')],
    'home.html': [('<span>Criação de sites</span><br><span>profissionais</span>', '<span>Criação de sites</span> <br><span>profissionais</span>')],
    'blog.html': [('<img src="${IMG[FEATURED.img]}" alt="">', '<img src="${IMG[FEATURED.img]}" alt="" width="1600" height="900">'),
                  ('<img src="${IMG[p.img]}" alt="" loading="lazy">', '<img src="${IMG[p.img]}" alt="" loading="lazy" decoding="async" width="1600" height="900">')],
    'cases.html': [('<span>Works<sup id="count">(16)</sup></span>',
                    '<span>Works<sup id="count" aria-hidden="true">(16)</sup><span class="wd-sr"> — cases de criação de sites da Work Digital</span></span>')],
}
def headings(t, fname):
    for a, b in HEADINGS.get(fname, []):
        t = t.replace(a, b)
    return t

def run(out):
    for f in ('home.html', 'solucoes.html', 'cases.html', 'case-interna.html', 'blog.html', 'post.html'):
        p = os.path.join(out, f)
        if not os.path.exists(p): continue
        t = open(p).read().replace(TOKEN, SITE)
        t = seo_static(t, f)
        t = headings(t, f)
        t = common(t, f, out)
        open(p, 'w').write(t)
