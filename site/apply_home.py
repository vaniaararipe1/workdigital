"""Apply the final home's menu, background, footer and contact panel to an inner page.
The home files are used as-is (copied next to each page); only the page HTML changes."""
import re

HOME = '/home/user/workdigital/home-final/index.html'
_h = open(HOME).read().split('\n')
HEADER_CSS = '\n'.join(_h[28:59]) + '\n' + '\n'.join(_h[97:103]) + '\n}\n' + '\n'.join(_h[192:196])
HEADER_HTML = '\n'.join(_h[245:269])
HOME_URL = 'https://workdigital-hero-preview.onrender.com/'

LIGHT_LAYER = '''.light-field-inner{position:absolute;inset:0;height:100%;overflow:hidden;background:#121316}
.light-field-inner::before{content:"";position:absolute;inset:-20%;background:
 radial-gradient(ellipse at 24% 42%,rgba(96,37,225,.92),transparent 44%),
 radial-gradient(ellipse at 78% 60%,rgba(237,72,151,.82),transparent 40%),
 radial-gradient(ellipse at 60% 84%,rgba(4,205,143,.32),transparent 34%),
 radial-gradient(ellipse at 42% 68%,rgba(150,72,253,.48),transparent 45%);
 animation:lightFieldDrift 22s ease-in-out infinite alternate;will-change:transform}
.light-field-inner::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 24%,rgba(18,19,22,.26),transparent 63%)}
@keyframes lightFieldDrift{from{transform:translate3d(-4%,-3%,0) scale(1)}to{transform:translate3d(5%,4%,0) scale(1.10)}}
@media(prefers-reduced-motion:reduce){.light-field-inner::before{animation:none}}
'''
FIXED_FIELD = '''/* Fundo da home: camada de luz fixa (copiada da home) */
body{isolation:isolate}
.light-field{position:fixed;inset:0;z-index:-1;pointer-events:none}
''' + LIGHT_LAYER
DARK_BAND = '''/* Rodapé da home numa faixa escura, com a mesma luz da home (páginas claras) */
.wd-dark-band{position:relative;isolation:isolate;overflow:hidden;background:#121316;color:#f7f6fb}
.wd-dark-band > wd-footer{position:relative;z-index:1}
.wd-dark-band > .light-field-inner{z-index:0}
''' + LIGHT_LAYER

LINKS = '''<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./wd-revision.css">
<link rel="stylesheet" href="./contact.css">
<style>
/* Botões da página mantêm o próprio estilo; o padrão global de botão da home vale só para os CTAs .wd-cta */
button:where(:not(.wd-cta)){font-family:inherit;font-weight:inherit;letter-spacing:inherit}
</style>
'''
SCRIPTS = '<script src="./footer.js" defer></script>\n<script src="./wd-revision.js" defer></script>\n'
VIEWPORT = '<meta name="viewport" content="width=device-width,initial-scale=1">\n'


FOOTER_TEXT = [('Como podemos te ajudar?', 'Tem um projeto em mente?'), ('ENTRE EM CONTATO', 'FALE COM A GENTE')]


POSITIVE_LOGO = './img/logo-work-digital-positivo.svg'
POSITIVE_CSS = """<style>
/* Versão positiva (páginas claras): menu, painel de contato e rodapé em tons claros */
.site-nav{border-color:transparent;box-shadow:0 18px 55px rgba(23,19,31,.10)}
.site-nav::before{background:rgba(255,255,255,.74)}
.nav-item,.nav-link,.nav-trigger{color:#17131F}
.dropdown{background:rgba(255,255,255,.86)!important;border-color:rgba(23,19,31,.10)!important;box-shadow:0 22px 60px rgba(23,19,31,.14)!important}
.dropdown a{color:#17131F}
.dropdown a:hover,.dropdown a:focus-visible{background:rgba(96,37,225,.07)}
.mobile-toggle{border-color:rgba(23,19,31,.14);background:rgba(23,19,31,.04);color:#17131F}
.mobile-toggle i,.mobile-toggle i:before,.mobile-toggle i:after{background:#17131F}
.site-nav.wd-contact-open .mobile-toggle i{background:transparent}
@media(max-width:980px){.site-nav.wd-nav-open .nav-links{background:rgba(255,255,255,.95);border-color:rgba(96,37,225,.16)}}
.nav-cta,.wd-contact .nav-cta.wd-cta{background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365)!important;background-size:280% 100%!important;background-position:100% 0!important;color:#fff!important;transition:background-position .6s ease,color .2s ease!important}
.nav-cta:hover,.nav-cta:focus-visible,.wd-contact .nav-cta.wd-cta:hover,.wd-contact .nav-cta.wd-cta:focus-visible{background-position:0 0!important;color:#2b1450!important}
.site-nav.wd-contact-open .wd-contact-close-trigger{background:none!important;color:#17131F!important}
.wd-contact-glass{background:rgba(255,255,255,.80)}
.wd-contact-stroke{stroke:rgba(23,19,31,.10)}
.wd-contact-shadow{fill:rgba(23,19,31,.12)}
.wd-contact-backdrop{background:rgba(244,243,236,.45)}
.wd-contact,.wd-contact-title,.wd-contact-result-title{color:#17131F}
.wd-contact .wd-contact-uptitle.wd-uptitle{background:linear-gradient(90deg,#6025E1,#A23FC9 55%,#D9467F)!important;-webkit-background-clip:text!important;background-clip:text!important}
.wd-contact .wd-contact-input{color:#17131F;border-bottom-color:rgba(23,19,31,.18)}
.wd-contact .wd-contact-input:hover{border-color:rgba(23,19,31,.42)}
.wd-contact .wd-contact-input::placeholder{color:#6B6578}
.wd-contact .wd-contact-input:focus,.wd-contact .wd-contact-input:focus-visible{caret-color:#17131F}
.wd-contact-field::after{background:linear-gradient(90deg,#6025E1,#A23FC9,#D9467F)}
.wd-contact .wd-contact-input[aria-invalid="true"]{border-color:#C9184A}
.wd-contact .wd-contact-input[aria-invalid="true"]::placeholder,.wd-contact-field-error{color:#C9184A}
.wd-contact-privacy,.wd-contact-result-text,.wd-contact-result-note{color:#6B6578}
.wd-contact-privacy a{color:#17131F}
wd-cursor-fix{}
.wd-cursor:not(.big){background:#17131F;box-shadow:0 0 0 1px rgba(255,255,255,.6)}
wd-footer{--wd-footer-icon-cutout:#F4F3EC;border-top:1px solid rgba(23,19,31,.10)}
</style>
"""


def _important(css):
    def fix(m):
        decls=[d.strip() for d in m.group(1).split(';') if d.strip()]
        return '{'+';'.join(d if d.endswith('!important') else d+'!important' for d in decls)+'}'
    return re.sub(r'\{([^{}]*)\}', fix, css)
POSITIVE_CSS = _important(POSITIVE_CSS)


def header(active):
    """active: one of Home, Soluções, Works, Blog."""
    h = HEADER_HTML
    h = h.replace('https://workdigital.art.br/wp-content/uploads/2022/05/logo-work-digital-branco-criacao-de-site-sp.svg',
                  './ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg')
    h = h.replace('<a class="brand" href="#hero"', f'<a class="brand" href="{HOME_URL}"')
    links = {'Home': HOME_URL, 'Soluções': HOME_URL + '#wd-explore',
             'Works': 'https://workdigital.art.br/cases/', 'Blog': 'https://workdigital.art.br/blog/'}
    h = re.sub(r'<a class="nav-link" href="[^"]*">(Home|Soluções|Works|Blog)</a>',
               lambda m: f'<a class="nav-link" href="{"#" if m.group(1) == active else links[m.group(1)]}"' +
               (' aria-current="page"' if m.group(1) == active else '') + f'>{m.group(1)}</a>', h)
    return h


def apply(t, *, active, dark=True, band=False, keep_header=False, hidden_home_header=False, extra_css='', header_re=None, remove_res=(), footer_slot=None):
    """dark=True: fixed light field behind the page. dark=False: page keeps its light background and
    the home footer goes in a dark band (footer_slot = text after which the band is inserted)."""
    css = 'body{margin:0}\n:root{--purple:#6025E1;--green:#04CD8F;--wine:#C00252}\n/* MENU (copiado da home) */\n' + HEADER_CSS + '\n'
    css += FIXED_FIELD if dark else DARK_BAND
    if dark and band:
        css += DARK_BAND.split('*/',1)[1].split('.light-field-inner{')[0]
    css += extra_css
    # page's own style ends at its last </style> before the body markup
    i = t.index('</style>')
    t = t[:i] + css + '\n</style>\n' + LINKS + t[i + len('</style>'):]
    new_header = ('<div class="light-field" aria-hidden="true"><div class="light-field-inner"></div></div>\n' if dark else '') + header(active)
    if keep_header:
        t = t.replace('<main', new_header.split('\n')[0] + '\n<main', 1) if dark else t
        if hidden_home_header:
            t = t.replace('<main', header(active) + '\n<main', 1)
    else:
        t, n = re.subn(header_re, lambda m: new_header + '\n', t, count=1, flags=re.S)
        assert n == 1, 'header not found'
    for rx in remove_res:
        t, n = re.subn(rx, '', t, count=1, flags=re.S)
        assert n == 1, 'pattern not found: ' + rx[:60]
    # custom cursor above everything (menu, contact panel)
    t = re.sub(r'(\.wd-cursor\{position:fixed;left:0;top:0;)z-index:\d+;', r'\1z-index:2147483000;', t)
    if not dark:
        t = t.replace('</style>\n' + LINKS, '</style>\n' + LINKS + POSITIVE_CSS, 1)
        t = t.replace('./ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg', POSITIVE_LOGO)
        foot = '<wd-footer id="wd-footer" data-theme="light"></wd-footer>\n'
        assert footer_slot in t
        t = t.replace(footer_slot, footer_slot + '\n' + foot, 1)
    if band:
        band = '<div class="wd-dark-band"><div class="light-field-inner" aria-hidden="true"></div><wd-footer id="wd-footer"></wd-footer></div>\n'
        assert footer_slot in t
        t = t.replace(footer_slot, footer_slot + '\n' + band, 1)
    t = VIEWPORT + t.rstrip() + '\n' + SCRIPTS
    return t


# ---------- Links entre as páginas (prévias publicadas) ----------
PAGES = {
    'home': 'https://claude.ai/artifact/K3DaWGpPSDzZs2TZpjwHjw',
    'solucoes': 'https://claude.ai/artifact/Y2eQb4LZVTwWfbNdqz7nbi',
    'cases': 'https://claude.ai/artifact/JRyLZxgMsFFUnvkSMXaiZ1',
    'case': 'https://claude.ai/artifact/3Fh9si9SLB3sa15y3GoaKC',
    'blog': 'https://claude.ai/artifact/2p828J4i2F3ekJZAnydNYc',
    'post': 'https://claude.ai/artifact/FtXL4pXoAfAXYYKwcxV1w8',
}


TICK_OLD = '(function tick(){x+=(mx-x)*.18;y+=(my-y)*.18;c.style.transform=`translate(${x}px,${y}px)`;requestAnimationFrame(tick);})();'
TICK_NEW = '(function tick(){const dx=mx-x,dy=my-y;if(Math.abs(dx)+Math.abs(dy)>.1){x+=dx*.18;y+=dy*.18;c.style.transform=`translate(${x}px,${y}px)`;}requestAnimationFrame(tick);})();'
PERF = [  # desempenho: aplicado em todas as páginas
    (TICK_OLD, TICK_NEW),
    # o círculo com texto (VER CASE / ABRIR / LER) esconde o cursor do sistema só enquanto aparece
    ("c.classList.toggle('big',!!label);", "c.classList.toggle('big',!!label);document.documentElement.classList.toggle('wd-big',!!label);"),
    ('grid.addEventListener("mouseover", e => cursor.classList.toggle("big", !!e.target.closest("[data-cursor]")));',
     'grid.addEventListener("mouseover", e => { const on = !!e.target.closest("[data-cursor]"); cursor.classList.toggle("big", on); document.documentElement.classList.toggle("wd-big", on); });'),
    ('grid.addEventListener("mouseleave", () => cursor.classList.remove("big"));',
     'grid.addEventListener("mouseleave", () => { cursor.classList.remove("big"); document.documentElement.classList.remove("wd-big"); });'),
    # cursor acompanha o mouse na hora (sem o atraso de 18% por quadro)
    ("addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;},{passive:true});",
     "addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;c.style.transform=`translate(${mx}px,${my}px)`;},{passive:true});"),
    (TICK_NEW, ''),
    ('(function tick() { cx += (mx - cx) * 0.18; cy += (my - cy) * 0.18;', '(function tick() { cx = mx; cy = my;'),
    # fundo de luz desenhado em 1/4 do tamanho e ampliado 4x (degradê suave: visual igual, 16x menos pixels para a GPU)
    ('.light-field-inner::before{content:"";position:absolute;inset:-20%;background:',
     '.light-field-inner::before{content:"";position:absolute;left:-20%;top:-20%;width:35%;height:35%;transform-origin:0 0;transform:scale(4);background:'),
    ('@keyframes lightFieldDrift{from{transform:translate3d(-4%,-3%,0) scale(1)}to{transform:translate3d(5%,4%,0) scale(1.10)}}',
     '@keyframes lightFieldDrift{from{transform:scale(4) translate3d(-4%,-3%,0) scale(1)}to{transform:scale(4) translate3d(5%,4%,0) scale(1.10)}}'),
    # cursor sem modo de mistura (mix-blend-mode obriga a recompor a página inteira a cada movimento)
    ('background:#F2EEF8;mix-blend-mode:difference;', 'background:#F2EEF8;box-shadow:0 0 0 1px rgba(18,19,22,.35);'),
    ('background: var(--fg); mix-blend-mode: difference;', 'background: var(--fg); box-shadow: 0 0 0 1px rgba(11,11,12,.35);'),
]


def _svg_cursor(svg):
    from urllib.parse import quote
    return 'url("data:image/svg+xml,' + quote(svg) + '")'
DOT_DARK = _svg_cursor('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><circle cx="8" cy="8" r="5.5" fill="#F2EEF8" stroke="#121316" stroke-opacity=".45"/></svg>')
# anel sobre links: gradiente da Work (roxo #6025E1 -> vinho #C00252), o mesmo do círculo "Ver case"
RING_DARK = _svg_cursor('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6025E1"/><stop offset="1" stop-color="#C00252"/></linearGradient></defs><circle cx="20" cy="20" r="19.3" fill="none" stroke="#fff" stroke-opacity=".55" stroke-width="1"/><circle cx="20" cy="20" r="17.8" fill="url(#g)" fill-opacity=".45" stroke="url(#g)" stroke-width="2"/><circle cx="20" cy="20" r="3" fill="#F7F6FB"/></svg>')
DOT_LIGHT = _svg_cursor('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><circle cx="8" cy="8" r="5.5" fill="#17131F" stroke="#fff" stroke-opacity=".7"/></svg>')
RING_LIGHT = _svg_cursor('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6025E1"/><stop offset="1" stop-color="#C00252"/></linearGradient></defs><circle cx="20" cy="20" r="18.5" fill="url(#g)" fill-opacity=".28" stroke="url(#g)" stroke-width="2"/><circle cx="20" cy="20" r="3" fill="url(#g)"/></svg>')
def cursor_css(light):
    dot, ring = (DOT_LIGHT, RING_LIGHT) if light else (DOT_DARK, RING_DARK)
    return ('<style>/* Cursor desenhado pelo sistema (sem atraso). O círculo com texto continua só sobre os cards. */\n'
            '@media (hover:hover) and (pointer:fine){'
            f'html,html body,html body *{{cursor:{dot} 8 8,auto!important}}'
            f'html body a,html body a *,html body button,html body button *,html body [role=button],html body label,html body .svc:not(.is-open),html body .svc:not(.is-open) *{{cursor:{ring} 20 20,pointer!important}}'
            'html body input,html body textarea{cursor:text!important}'
            'html.wd-big,html.wd-big body,html.wd-big body *{cursor:none!important}}'
            '.wd-cursor:not(.big),.cursor:not(.big){opacity:0!important}'
            '.wd-cursor.big,.cursor.big{background:linear-gradient(135deg,#6025E1,#C00252)!important;color:#fff!important;box-shadow:none!important;border:0!important;outline:0!important}'
            '</style>\n')



# Modo leve: liga sozinho em placas de vídeo fracas (ex.: Intel HD Graphics 2000-4000) ou sem aceleração.
# Em máquinas mais fortes nada muda.
LITE_JS = ('<script>/* wd-lite */(function(){var lite=false;try{if(/[?&]lite=1/.test(location.search))lite=true;'
           'if(!/[?&]lite=0/.test(location.search)){var cv=document.createElement("canvas"),g=cv.getContext("webgl");'
           'var e=g&&g.getExtension("WEBGL_debug_renderer_info"),r=e?String(g.getParameter(e.UNMASKED_RENDERER_WEBGL)):"";'
           'if(!g||/SwiftShader|llvmpipe|softpipe|Basic Render|Intel\\(R\\) (HD Graphics( [2-5]\\d{3})?|Q?G\\d+)\\b|GMA/i.test(r))lite=true;'
           'var lc=g&&g.getExtension("WEBGL_lose_context");lc&&lc.loseContext();'
           'if((navigator.hardwareConcurrency||8)<=2)lite=true;}}catch(x){}'
           'if(lite)document.documentElement.classList.add("wd-lite");window.WD_LITE=lite;})();'
           # toda página abre no topo (o navegador não restaura uma posição antiga de rolagem), exceto quando o link aponta para uma seção (#)
           '(function(){try{if(!location.hash){history.scrollRestoration="manual";var top=function(){scrollTo(0,0)};top();addEventListener("DOMContentLoaded",top,{once:true});addEventListener("load",function(){requestAnimationFrame(top)},{once:true});}}catch(e){}'
           # item do menu da própria página (e logo que aponta para a própria página) sobe suavemente até o topo
           'document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(".site-nav a[href=\'#\'],.site-nav a[href=\'#topo\'],.site-nav a[href=\'#top\'],.site-nav a[href=\'#hero\']");if(!a)return;e.preventDefault();scrollTo({top:0,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});try{history.replaceState(null,"",location.pathname+location.search)}catch(x){}});})();</script>\n')
def lite_css(light):
    if light:
        nav, dd, mob, glass = 'rgba(255,255,255,.96)', 'rgba(255,255,255,.98)', 'rgba(255,255,255,.98)', 'rgba(255,255,255,.97)'
    else:
        nav, dd, mob, glass = 'rgba(18,19,22,.93)', 'rgba(28,22,42,.97)', 'rgba(36,18,62,.97)', 'rgba(18,19,22,.95)'
    return ('<style>/* Modo leve (GPU fraca): sem desfoque por trás dos painéis — fundos mais opacos no lugar; luz de fundo parada */\n'
            'html.wd-lite *,html.wd-lite *::before,html.wd-lite *::after{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}'
            f'html.wd-lite .site-nav::before{{background:{nav}!important}}'
            f'html.wd-lite .dropdown{{background:{dd}!important}}'
            f'html.wd-lite .site-nav.wd-nav-open .nav-links{{background:{mob}!important}}'
            f'html.wd-lite .wd-contact-glass{{background:{glass}!important}}'
            'html.wd-lite .wd-contact-backdrop{background:rgba(10,10,14,.55)!important}'
            'html.wd-lite .light-field-inner::before,html.wd-lite .light-field-inner::after,html.wd-lite .light-field-inner{animation:none!important}'
            'html.wd-lite .svc{--card:linear-gradient(125deg,rgba(96,37,225,.16),rgba(49,22,78,.26)),rgba(20,20,26,.94)}'
            'html.wd-lite .orb,html.wd-lite .orb2,html.wd-lite .orb::after{animation:none!important}'
            '</style>\n')
# favicon: mascote da Work; escuro quando o navegador está claro e claro quando está escuro (automático, pelo próprio SVG)
import base64 as _b64
FAVICON = ('<link rel="icon" type="image/svg+xml" href="data:image/svg+xml;base64,'
           + _b64.b64encode(open(__import__('os').path.join(__import__('os').path.dirname(__file__), 'favicon.svg'), 'rb').read()).decode() + '">\n')
RESP_CSS = ('<style>/* Responsivo (todas as páginas) */\n'
  # nenhuma página rola para os lados, mesmo que um elemento decorativo passe alguns pixels da tela
  'html,body{overflow-x:clip}'
  # menu entre 981 e 1180px: logo | links | ações, sem os links encostarem no seletor de idioma
  '@media(min-width:981px) and (max-width:1180px){.site-header .site-nav{grid-template-columns:auto minmax(0,1fr) auto;gap:16px}.site-header .nav-links{gap:clamp(14px,2.1vw,28px)}.site-header .wd-nav-actions{gap:14px}}'
  '</style>\n')
def add_lite(t):
    if '/* wd-lite */' in t:
        return t
    t = re.sub(r'<link[^>]*rel="(?:shortcut )?icon"[^>]*>\\n?', '', t)
    light = 'data-theme="light"' in t
    if '<head>' in t:
        i = t.index('<head>') + len('<head>')
        t = t[:i] + '\n' + FAVICON + LITE_JS + t[i:]
    else:
        t = ('' if 'charset=' in t[:400] else '<meta charset="utf-8">\n') + FAVICON + LITE_JS + t
    return t.rstrip() + '\n' + lite_css(light) + RESP_CSS
    # (não usado)
    return t.rstrip() + '\n' + lite_css(light)

def link_pages(t):
    for a, b in PERF:
        t = t.replace(a, b)
    if 'cursor_css_done' not in t:
        t = t.rstrip() + '\n<!-- cursor_css_done -->' + cursor_css('data-theme="light"' in t) + '\n'
    t = add_lite(t)
    P = PAGES
    for a, b in [('https://workdigital-hero-preview.onrender.com/#wd-explore', P['solucoes']),
                 ('https://workdigital-hero-preview.onrender.com/', P['home']),
                 ('https://workdigital.art.br/cases/', P['cases']),
                 ('https://workdigital.art.br/blog/', P['blog']),
                 ('https://workdigital.art.br/como-potencializar-a-sua-marca-com-o-blog-marketing/', P['post']),
                 ('<a class="nav-link" href="#wd-explore">', f'<a class="nav-link" href="{P["solucoes"]}">')]:
        t = t.replace(a, b)
    # cada prévia é uma página separada: os links abrem a página correspondente na mesma aba (_top sai do quadro da prévia)
    def tgt(m):
        tag = m.group(0)
        if 'target=' in tag:
            return re.sub(r'target="[^"]*"', 'target="_top"', tag)
        return tag[:-1] + ' target="_top">'
    t = re.sub(r'<a [^>]*href="https://claude\.ai/artifact/[^"]+"[^>]*>', tgt, t)
    return t
