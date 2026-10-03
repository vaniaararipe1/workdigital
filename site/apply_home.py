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
 filter:blur(42px);animation:lightFieldDrift 22s ease-in-out infinite alternate;will-change:transform}
.light-field-inner::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 24%,rgba(18,19,22,.26),transparent 63%)}
@keyframes lightFieldDrift{from{transform:translate3d(-4%,-3%,0) scale(1)}to{transform:translate3d(5%,4%,0) scale(1.10)}}
@media(max-width:760px){.light-field-inner::before{filter:blur(28px)}}
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
.site-nav{border-color:rgba(23,19,31,.10);box-shadow:0 18px 55px rgba(23,19,31,.10)}
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
               lambda m: f'<a class="nav-link" href="{links[m.group(1)]}"' +
               (' aria-current="page"' if m.group(1) == active else '') + f'>{m.group(1)}</a>', h)
    return h


def apply(t, *, active, dark=True, band=False, keep_header=False, extra_css='', header_re=None, remove_res=(), footer_slot=None):
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
