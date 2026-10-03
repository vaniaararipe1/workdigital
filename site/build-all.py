import os, re, shutil
from apply_home import apply

OUT = 'site-build'
HOMEF = '/home/user/workdigital/home-final'
os.makedirs(OUT + '/img', exist_ok=True); os.makedirs(OUT + '/ativos-externos', exist_ok=True)
from apply_home import FOOTER_TEXT
for f in ['footer.js', 'contact.js', 'contact.css', 'whatsapp.js', 'wd-revision.js', 'wd-revision.css']:
    shutil.copy(f'{HOMEF}/{f}', f'{OUT}/{f}')
ft = open(f'{OUT}/footer.js').read()
for a, c in FOOTER_TEXT:
    assert a in ft; ft = ft.replace(a, c)
open(f'{OUT}/footer.js', 'w').write(ft)
shutil.copy(f'{HOMEF}/img/logo-work-digital.svg', f'{OUT}/img/')
shutil.copy(f'{HOMEF}/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg', f'{OUT}/ativos-externos/')

def sub1(t, a, b):
    assert a in t, 'missing: ' + a[:70]
    return t.replace(a, b, 1)

# ---------- Soluções ----------
t = open('solucoes-work-digital.html').read()
t = sub1(t, 'body{background:var(--bg);', 'html{background:#121316}body{background:transparent;')
t = sub1(t, "const menu=document.getElementById('menu'), mb=document.getElementById('menuBtn');\n"
            "mb.addEventListener('click',()=>{const on=menu.classList.toggle('on'); mb.setAttribute('aria-expanded',on);});\n"
            "menu.addEventListener('click',()=>{menu.classList.remove('on');mb.setAttribute('aria-expanded',false);});\n"
            "document.getElementById('yr').textContent=new Date().getFullYear();\n", '')
t = apply(t, active='Soluções', band=True, footer_slot='</main>', header_re=r'<header class="hd">.*?</header>\n',
          remove_res=[r'<footer id="contato">.*?</footer>\n', r'<nav class="menu" id="menu".*?</nav>\n',
                      r'<a class="wa".*?</a>\n', r'<button class="menu-btn".*?</button>\n'],
          extra_css='.wd-dark-band{z-index:1}\n')
open(OUT + '/solucoes.html', 'w').write(t)

# ---------- Case interna ----------
t = open('case-work-digital.html').read()
t = sub1(t, 'body{background:var(--bg);', 'html{background:#121316}body{background:transparent;')
t = apply(t, active='Works', header_re=r'<header class="hd">.*?</header>\n',
          remove_res=[r'<a class="wa".*?</a>\n'],
          extra_css='wd-footer{position:relative;z-index:1}\n')
open(OUT + '/case-interna.html', 'w').write(t)

# ---------- Blog (claro) ----------
t = open('blog-work-digital.html').read()
t = sub1(t, '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>',
         '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>\n'
         '    <label class="bsearch rv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
         '<input id="q" type="search" placeholder="Buscar artigos" aria-label="Buscar artigos"></label>')
t = re.sub(r"const srch=document\.getElementById\('srch'\).*?(?=// Reveal)",
           "const q=document.getElementById('q');\nq.addEventListener('input',()=>{term=q.value.trim().toLowerCase(); apply();});\n\n", t, count=1, flags=re.S)
t = apply(t, active='Blog', dark=False,
          header_re=r'<header class="hd" id="hd">.*?</header>\n\n<div class="drawer".*?</div>\n',
          remove_res=[r'<footer class="ft" id="contato">.*?</footer>\n', r'<a class="wa".*?</a>\n'],
          footer_slot='</main>',
          extra_css='''.bsearch{display:flex;align-items:center;gap:10px;width:min(360px,100%);height:46px;margin:18px auto 0;padding:0 18px;border:1px solid var(--line);border-radius:999px;background:rgba(255,255,255,.6);color:var(--muted);transition:border-color .25s,background .25s}
.bsearch:focus-within{border-color:#6025E1;background:#fff}
.bsearch svg{width:18px;height:18px;flex:none}
.bsearch input{flex:1;min-width:0;border:0;outline:0;background:transparent;color:var(--ink);font:500 15px var(--display)}
.wd-dark-band{margin-top:clamp(64px,8vw,120px)}
.hero .up,.empty{font-family:var(--display)!important}
''')
open(OUT + '/blog.html', 'w').write(t)

# ---------- Post (claro) ----------
t = open('post-work-digital.html').read()
t = re.sub(r"// Busca: abre o campo.*?(?=// Reveal)", '', t, count=1, flags=re.S)
t = apply(t, active='Blog', dark=False,
          header_re=r'<header class="hd" id="hd">.*?</header>\n\n<div class="drawer".*?</div>\n',
          remove_res=[r'<footer class="ft" id="contato">.*?</footer>\n', r'<a class="wa".*?</a>\n'],
          footer_slot='</main>',
          extra_css='''.wd-dark-band{margin-top:clamp(80px,9vw,120px)}
.card .d,.ph .dek{font-family:var(--body)}
.card .d{font-family:var(--display)!important}
''')
open(OUT + '/post.html', 'w').write(t)
print('ok')

# ---------- Cases (já com o menu/fundo/rodapé; remove o bloco final que agora está no rodapé) ----------
t = open('cases-site/cases.html').read()
t, n = re.subn(r'  <section class="cta wrap" id="contato".*?</section>\n', '', t, count=1, flags=re.S); assert n == 1
t, n = re.subn(r'/\* ---------- Copy e-mail ---------- \*/\n.*?\n\};\n', '', t, count=1, flags=re.S); assert n == 1
open(OUT + '/cases.html', 'w').write(t)
print('cases ok')
