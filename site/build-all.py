import os, re, shutil
from apply_home import apply, link_pages, PAGES

OUT = 'site-build'
HOMEF = '/home/user/workdigital/home-final'
os.makedirs(OUT + '/img', exist_ok=True); os.makedirs(OUT + '/ativos-externos', exist_ok=True)
from apply_home import FOOTER_TEXT
for f in ['footer.js', 'contact.js', 'contact.css', 'whatsapp.js', 'wd-revision.js', 'wd-revision.css']:
    shutil.copy(f'{HOMEF}/{f}', f'{OUT}/{f}')
ft = open(f'{OUT}/footer.js').read()
for a, c in FOOTER_TEXT:
    assert a in ft; ft = ft.replace(a, c)
LIGHT = '''
    :host([data-theme="light"]){color:#17131F}
    :host([data-theme="light"]) .wd-footer-description,:host([data-theme="light"]) .wd-footer-rights,:host([data-theme="light"]) .wd-footer-social{color:#4A4458}
    :host([data-theme="light"]) .wd-footer-social:hover,:host([data-theme="light"]) .wd-footer-social:focus-visible{color:#6025E1;background:rgba(96,37,225,.08)}
    :host([data-theme="light"]) .wd-footer-rights-brand:hover{color:#17131F}
    :host([data-theme="light"]) a:focus-visible{outline-color:#6025E1}
  `;'''
assert ft.count('\n  `;') == 1
ft = ft.replace('\n  `;', LIGHT, 1)
# versão positiva do logo no rodapé quando data-theme="light"
x = "root.querySelector('.wd-footer-logo').src=url(values.logo,['https:','http:'])||CONFIG.logo;"
assert x in ft
ft = ft.replace(x, "root.querySelector('.wd-footer-logo').src=(this.dataset.theme==='light'&&!this.hasAttribute('logo'))?new URL('img/logo-work-digital-positivo.svg',source).href:(url(values.logo,['https:','http:'])||CONFIG.logo);")
ft = ft.replace("home: 'https://workdigital.art.br/',", "home: '" + PAGES['home'] + "',")
y = "root.querySelector('.wd-footer-rights-brand').href=home;"
assert y in ft
ft = ft.replace(y, y + "root.querySelectorAll('.wd-footer-home,.wd-footer-rights-brand').forEach(a=>{a.target='_blank';a.rel='noopener';});")
open(f'{OUT}/footer.js', 'w').write(ft)
shutil.copy(f'{HOMEF}/img/logo-work-digital.svg', f'{OUT}/img/')
logo = open(f'{HOMEF}/img/logo-work-digital.svg').read()
assert '.b{fill:#fff;}' in logo
exec(open('make-logo.py').read())  # versão positiva: mascote roxo #6025E1 + 'work DIGITAL' grafite #262626
shutil.copy(f'{HOMEF}/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg', f'{OUT}/ativos-externos/')

def sub1(t, a, b):
    assert a in t, 'missing: ' + a[:70]
    return t.replace(a, b, 1)

# ---------- Soluções ----------
t = open('solucoes-work-digital.html').read()
t = sub1(t, 'body{background:var(--bg);', 'html{background:#121316}body{background:transparent;')
# palavras abaixo do menu (o menu da home é mais alto que o antigo)
for a, b in [('top:calc(12vh + 5.5vw)', 'top:calc(12vh + 64px + 5.5vw)'), ('.words .w1{position:absolute;left:3.5vw;top:12vh;', '.words .w1{position:absolute;left:3.5vw;top:calc(12vh + 64px);'),
             ('top:calc(12vh + .9em)', 'top:calc(12vh + 64px + .9em)'), ('top:calc(12vh + 1em)', 'top:calc(12vh + 64px + 1em)'),
             ('.intro-space{height:52vh}', '.intro-space{height:calc(52vh + 64px)}'), ('.intro-space{height:44vh}', '.intro-space{height:calc(44vh + 40px)}'),
             ('.words .w1{top:14vh}.words .w2{top:calc(14vh + 1em)}.words .plus{left:6vw;top:calc(14vh + 1.05em)}',
              '.words .w1{top:calc(14vh + 40px)}.words .w2{top:calc(14vh + 40px + 1em)}.words .plus{left:6vw;top:calc(14vh + 40px + 1.05em)}')]:
    t = sub1(t, a, b)
# "SOLUÇÕES + WORK" com o degradê do título de destaque da home (#FFFFFF → #EDE4FF → #F7C9EC)
t = sub1(t, "tctx.fillText(el.textContent.toUpperCase(),", "const g=tctx.createLinearGradient(rc.left*dpr,0,rc.right*dpr,0);g.addColorStop(0,'#FFFFFF');g.addColorStop(.45,'#EDE4FF');g.addColorStop(1,'#F7C9EC');tctx.fillStyle=g;\n      tctx.fillText(el.textContent.toUpperCase(),")
t = sub1(t, "const x=rc.left*dpr,y=rc.top*dpr,w=rc.width*dpr,hh=rc.height*dpr;tctx.fillRect", "const x=rc.left*dpr,y=rc.top*dpr,w=rc.width*dpr,hh=rc.height*dpr;tctx.fillStyle='#EDE4FF';tctx.fillRect")
t = sub1(t, "vec3 tc=mix(vec3(.85,.83,.89),dark,a);", "vec3 tc=mix(texture2D(tx2,fc/res).rgb,dark,a);")
t = sub1(t, ".words .w1{position:absolute;", ".words .w1,.words .w2{background:linear-gradient(90deg,#FFFFFF 0%,#EDE4FF 45%,#F7C9EC 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}\n.words .w1{position:absolute;")
t = sub1(t, ".words .plus::before,.words .plus::after{content:\"\";position:absolute;background:#d9d3e4;", ".words .plus::before,.words .plus::after{content:\"\";position:absolute;background:#EDE4FF;")
# rodapé fluido: a bola e as palavras somem suavemente quando o rodapé chega
t = sub1(t, "document.fonts && document.fonts.ready.then(layout);\n", "document.fonts && document.fonts.ready.then(layout);\n"
         "(function(){const bgfx=document.querySelector('.bgfx');function fade(){const ft=document.querySelector('wd-footer');if(!ft)return;"
         "const r=ft.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight-r.top)/(Math.min(r.height,innerHeight)*.8)));bgfx.style.opacity=String(1-p);}"
         "addEventListener('scroll',fade,{passive:true});addEventListener('resize',fade);setTimeout(fade,500);})();\n")
t = sub1(t, "const menu=document.getElementById('menu'), mb=document.getElementById('menuBtn');\n"
            "mb.addEventListener('click',()=>{const on=menu.classList.toggle('on'); mb.setAttribute('aria-expanded',on);});\n"
            "menu.addEventListener('click',()=>{menu.classList.remove('on');mb.setAttribute('aria-expanded',false);});\n"
            "document.getElementById('yr').textContent=new Date().getFullYear();\n", '')
t = apply(t, active='Soluções', header_re=r'<header class="hd">.*?</header>\n',
          remove_res=[r'<footer id="contato">.*?</footer>\n', r'<nav class="menu" id="menu".*?</nav>\n',
                      r'<a class="wa".*?</a>\n', r'<button class="menu-btn".*?</button>\n'],
          extra_css='wd-footer{position:relative;z-index:1}\n.bgfx{transition:opacity .2s linear}\n')
open(OUT + '/solucoes.html', 'w').write(link_pages(t))

# ---------- Case interna ----------
t = open('case-work-digital.html').read()
t = sub1(t, 'body{background:var(--bg);', 'html{background:#121316}body{background:transparent;')
t = sub1(t, '<a class="pill dark" href="#top">Vamos conversar', '<a class="pill dark" href="https://workdigital.art.br/contato/">Vamos conversar')
for a, b in [('<a class="logo" href="#top"', f'<a class="logo" href="{PAGES["home"]}"'), ('<a class="pill light back" href="#top">', f'<a class="pill light back" href="{PAGES["cases"]}">')]:
    t = sub1(t, a, b)
t = apply(t, active='Works', keep_header=True,
          remove_res=[r'<a class="wa".*?</a>\n'],
          extra_css='wd-footer{position:relative;z-index:1}\n')
open(OUT + '/case-interna.html', 'w').write(link_pages(t))

# ---------- Blog (claro) ----------
t = open('blog-work-digital.html').read()
t = sub1(t, '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>',
         '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>\n'
         '    <label class="bsearch rv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
         '<input id="q" type="search" placeholder="Buscar artigos" aria-label="Buscar artigos"></label>')
t = re.sub(r"const srch=document\.getElementById\('srch'\).*?(?=// Reveal)",
           "const q=document.getElementById('q');\nq.addEventListener('input',()=>{term=q.value.trim().toLowerCase(); apply();});\n\n", t, count=1, flags=re.S)
t = sub1(t, 'const link=p=>p.href?`href="${p.href}" target="_blank" rel="noopener"`:\'href="#"\';', 'const link=p=>`href="' + PAGES['post'] + '" target="_blank" rel="noopener"`;')
t = apply(t, active='Blog', dark=False,
          header_re=r'<header class="hd" id="hd">.*?</header>\n\n<div class="drawer".*?</div>\n',
          remove_res=[r'<footer class="ft" id="contato">.*?</footer>\n', r'<a class="wa".*?</a>\n'],
          footer_slot='</main>',
          extra_css='''.bsearch{display:flex;align-items:center;gap:10px;width:min(360px,100%);height:46px;margin:18px auto 0;padding:0 18px;border:1px solid var(--line);border-radius:999px;background:rgba(255,255,255,.6);color:var(--muted);transition:border-color .25s,background .25s}
.bsearch:focus-within{border-color:#6025E1;background:#fff}
.bsearch svg{width:18px;height:18px;flex:none}
.bsearch input{flex:1;min-width:0;border:0;outline:0;background:transparent;color:var(--ink);font:500 15px var(--display)}
wd-footer{margin-top:clamp(64px,8vw,120px)}
.hero .up,.empty{font-family:var(--display)!important}
''')
open(OUT + '/blog.html', 'w').write(link_pages(t))

# ---------- Post (claro) ----------
t = open('post-work-digital.html').read()
t = re.sub(r"// Busca: abre o campo.*?(?=// Reveal)", '', t, count=1, flags=re.S)
for a, b in [('<a class="chip" href="#">', f'<a class="chip" href="{PAGES["blog"]}">'),
             ('<a href="#">Criação de Blogs da Work</a>', f'<a href="{PAGES["solucoes"]}">Criação de Blogs da Work</a>'),
             ('<a class="all" href="#">', f'<a class="all" href="{PAGES["blog"]}">')]:
    t = sub1(t, a, b)
t = t.replace('<a class="card rv" href="#">', f'<a class="card rv" href="{PAGES["post"]}">')
t = apply(t, active='Blog', dark=False,
          header_re=r'<header class="hd" id="hd">.*?</header>\n\n<div class="drawer".*?</div>\n',
          remove_res=[r'<footer class="ft" id="contato">.*?</footer>\n', r'<a class="wa".*?</a>\n'],
          footer_slot='</main>',
          extra_css='''wd-footer{margin-top:clamp(80px,9vw,120px)}
.card .d,.ph .dek{font-family:var(--body)}
.card .d{font-family:var(--display)!important}
''')
t = sub1(t, '<a class="nav-link" href="#" aria-current="page">Blog', '<a class="nav-link" href="' + PAGES['blog'] + '" aria-current="page">Blog')
open(OUT + '/post.html', 'w').write(link_pages(t))
print('ok')

# ---------- Cases (já com o menu/fundo/rodapé; remove o bloco final que agora está no rodapé) ----------
t = open('cases-site/cases.html').read()
t, n = re.subn(r'  <section class="cta wrap" id="contato".*?</section>\n', '', t, count=1, flags=re.S); assert n == 1
t, n = re.subn(r'/\* ---------- Copy e-mail ---------- \*/\n.*?\n\};\n', '', t, count=1, flags=re.S); assert n == 1
t = sub1(t, 'a.href = "#case-" + p.slug;', 'a.href = "' + PAGES['case'] + '"; a.target = "_blank"; a.rel = "noopener";')
open(OUT + '/cases.html', 'w').write(link_pages(t))
print('cases ok')
