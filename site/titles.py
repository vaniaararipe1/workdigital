# Títulos (<title>) das páginas. Case interno e post montam o título a partir do conteúdo da página.
import html, os, re
FIXOS = {
    'home.html': 'Work Digital - Criação de Sites Profissionais',
    'solucoes.html': 'Work Digital - Soluções para o seu negócio',
    'cases.html': 'Work Digital - Cases da Work',
    'blog.html': 'Work Digital - Blog da Work',
}
# Case interno: "Work Digital - {projeto} - {cliente}", lidos de data-projeto / data-cliente no <h1> do case
CASE_JS = '''<script>(function(){var h=document.querySelector('.intro h1');if(!h)return;if(h.dataset.seo){document.title=h.dataset.seo;return;}var c=(h.dataset.cliente||h.textContent).trim(),p=(h.dataset.projeto||'').trim();document.title='Work Digital - '+(p?p+' - ':'')+c;})();</script>'''
# Post: "{título do post} - Work Digital", lido do <h1> do post
POST_JS = '''<script>(function(){var h=document.querySelector('.ph h1');if(h&&h.textContent.trim())document.title=h.textContent.trim()+' - Work Digital';})();</script>'''

def set_title(t, title):
    return re.sub(r'<title>[^<]*</title>', '<title>' + html.escape(title, quote=False) + '</title>', t, count=1)

def h1_text(t, pat):
    m = re.search(pat, t, re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''

def run(out):
    for f, title in FIXOS.items():
        p = os.path.join(out, f)
        if os.path.exists(p):
            t = open(p).read(); open(p, 'w').write(set_title(t, title))
    p = os.path.join(out, 'case-interna.html')
    if os.path.exists(p):
        t = open(p).read()
        # projeto do case modelo; nas páginas de cada projeto vem do conteudo-cases.json
        t = t.replace('<div class="intro"> <h1>', '<div class="intro"> <h1 data-projeto="Site institucional" data-cliente="Vice Versa Estamparia">', 1) if 'data-projeto=' not in t else t
        t = re.sub(r'(<div class="intro">\s*)<h1>', r'\1<h1 data-projeto="Site institucional" data-cliente="Vice Versa Estamparia">', t, count=1) if 'data-projeto=' not in t else t
        ms = re.search(r'<h1 [^>]*data-seo="([^"]*)"', t)
        m = None if ms else re.search(r'<h1 data-projeto="([^"]*)" data-cliente="([^"]*)"', t)
        if ms:
            t = set_title(t, html.unescape(ms.group(1)))
        if m:
            t = set_title(t, 'Work Digital - ' + (html.unescape(m.group(1)) + ' - ' if m.group(1) else '') + html.unescape(m.group(2)))
        if CASE_JS not in t: t = t.replace('</body>', CASE_JS + '</body>', 1) if '</body>' in t else t + CASE_JS
        open(p, 'w').write(t)
    p = os.path.join(out, 'post.html')
    if os.path.exists(p):
        t = open(p).read()
        h = h1_text(t, r'<h1[^>]*>(.*?)</h1>')
        if h: t = set_title(t, h + ' - Work Digital')
        if POST_JS not in t: t = t.replace('</body>', POST_JS + '</body>', 1) if '</body>' in t else t + POST_JS
        open(p, 'w').write(t)
