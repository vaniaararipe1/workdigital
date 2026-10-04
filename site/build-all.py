import os, re, shutil
from apply_home import apply, link_pages, PAGES

OUT = 'site-build'
HOMEF = '/home/user/workdigital/home-final'
os.makedirs(OUT + '/img', exist_ok=True); os.makedirs(OUT + '/ativos-externos', exist_ok=True)
from apply_home import FOOTER_TEXT
for f in ['footer.js', 'contact.js', 'contact.css', 'whatsapp.js', 'wd-revision.js', 'wd-revision.css']:
    shutil.copy(f'{HOMEF}/{f}', f'{OUT}/{f}')
import contact_fit; contact_fit.apply(OUT)
ft = open(f'{OUT}/footer.js').read()
# o CTA do rodapé abre o popup de contato (sem link para a página de contato antiga)
assert "contact: 'https://workdigital.art.br/contato/'" in ft
ft = ft.replace("contact: 'https://workdigital.art.br/contato/'", "contact: '#contato'")
for a, c in FOOTER_TEXT:
    assert a in ft; ft = ft.replace(a, c)
LIGHT = '''
    :host([data-theme="light"]){color:#17131F}
    :host([data-theme="light"]) .wd-footer-description,:host([data-theme="light"]) .wd-footer-rights,:host([data-theme="light"]) .wd-footer-social{color:#4A4458}
    :host([data-theme="light"]) .wd-footer-social:hover,:host([data-theme="light"]) .wd-footer-social:focus-visible{color:#6025E1;background:rgba(96,37,225,.08)}
    :host([data-theme="light"]) .wd-footer-rights-brand:hover{color:#17131F}
    :host([data-theme="light"]) a:focus-visible{outline-color:#6025E1}
    :host([data-theme="light"]) .wd-footer-title{color:#4A4458}
    .wd-footer-cta{min-height:76px;padding:24px 44px;gap:24px;font-size:18px}
    .wd-footer-cta svg{width:18px;height:18px}
    @media(max-width:600px){.wd-footer-cta{min-height:62px;padding:20px 30px;font-size:16px}}
    .wd-footer-rights{flex-wrap:nowrap;white-space:nowrap}
    @media(max-width:360px){.wd-footer-rights{font-size:12px;gap:8px}}
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
ft = ft.replace(y, y + "root.querySelectorAll('.wd-footer-home,.wd-footer-rights-brand').forEach(a=>{a.target='_top';});")
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
t = sub1(t, ".words .w1{position:absolute;", ".words .w1,.words .w2{background:linear-gradient(90deg,#FFFFFF 0%,#EDE4FF 45%,#F7C9EC 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;padding:.18em 0;margin-top:-.18em}\n.words .w1{position:absolute;")
t = sub1(t, ".words .plus::before,.words .plus::after{content:\"\";position:absolute;background:#d9d3e4;", ".words .plus::before,.words .plus::after{content:\"\";position:absolute;background:#EDE4FF;")
# rodapé fluido: a bola e as palavras somem suavemente quando o rodapé chega
t = sub1(t, "document.fonts && document.fonts.ready.then(layout);\n", "document.fonts && document.fonts.ready.then(layout);\n"
         "(function(){const bgfx=document.querySelector('.bgfx');function fade(){const ft=document.querySelector('wd-footer');if(!ft)return;"
         "const r=ft.getBoundingClientRect();const p=Math.min(1,Math.max(0,(innerHeight-r.top)/(Math.min(r.height,innerHeight)*.8)));bgfx.style.opacity=p>=1?'0':String(1-p);}"
         "addEventListener('scroll',fade,{passive:true});addEventListener('resize',fade);setTimeout(fade,500);})();\n")
# cards no padrão da home: raio 32px e as cores dos cards da home (#29134d; hover #301258 → #4b247e)
# retângulos com as cores e efeitos do retângulo da seção Soluções da home (.wd-explore-layout + campo de pontos)
t = sub1(t, '--card:rgba(34,30,40,.94); --card-hover:rgba(44,38,54,.96);', '--card:linear-gradient(125deg,rgba(96,37,225,.12),rgba(49,22,78,.2)),rgba(18,19,22,.66); --card-hover:var(--card);')
t = sub1(t, '.svc{position:absolute;border-radius:8px;background:var(--card);backdrop-filter:blur(10px);overflow:hidden;',
         '.svc{position:absolute;border-radius:8px;background:var(--card);backdrop-filter:blur(22px) saturate(140%);-webkit-backdrop-filter:blur(22px) saturate(140%);overflow:hidden;isolation:isolate;border:1px solid rgba(189,164,255,.13);transition:box-shadow .7s cubic-bezier(.4,0,.2,1);')
t = sub1(t, 'height .7s var(--ease),background .3s}', 'height .7s var(--ease),background .3s,box-shadow .7s cubic-bezier(.4,0,.2,1)}')
t = sub1(t, '.svc:not(.is-open){cursor:pointer}', '''.svc:not(.is-open){cursor:pointer}
/* hover dos boxes de Soluções da home */
.svc::before{content:"";position:absolute;inset:0;border-radius:inherit;z-index:-1;background:linear-gradient(135deg,rgba(124,92,255,.38) 0%,rgba(183,155,255,.22) 45%,rgba(255,143,203,.20) 100%);box-shadow:inset 0 0 0 1px rgba(214,198,255,.35);opacity:0;transition:opacity .7s cubic-bezier(.4,0,.2,1);pointer-events:none}
.svc:hover::before,.svc:focus-within::before,.svc.is-open::before{opacity:1}
.svc:hover,.svc.is-open{box-shadow:0 20px 60px -20px rgba(124,92,255,.55)}
.svc .dots{position:absolute;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;border-radius:inherit}
.svc .head,.svc .content{position:relative;z-index:1}
@media(prefers-reduced-motion:reduce){.svc,.svc::before{transition:none}}''')
t = sub1(t, "el.innerHTML=`<div class=\"head\">", "el.innerHTML=`<canvas class=\"dots\" aria-hidden=\"true\"></canvas><div class=\"head\">")
# campo de pontos da home (mesmos valores), um por retângulo
t = sub1(t, "\nlayout();\n", '''
document.querySelectorAll('.svc').forEach(panel=>{
 const canvas=panel.querySelector('.dots'),ctx=canvas.getContext('2d'),reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let width=0,height=0,frame=0,active=false,x=-200,y=-200,strength=0;
 function draw(){frame=0;strength+=(Number(active)-strength)*.12;ctx.clearRect(0,0,width,height);ctx.fillStyle='#bda4ff';
  for(let py=12;py<height;py+=22)for(let px=12;px<width;px+=22){const dx=px-x,dy=py-y,distance=Math.hypot(dx,dy);
   const influence=Math.exp(-distance*distance/(90*90))*strength,shift=influence*10/(distance||1);
   ctx.globalAlpha=.09+influence*.35;ctx.beginPath();ctx.arc(px+dx*shift,py+dy*shift,.8+influence*.7,0,Math.PI*2);ctx.fill();}
  ctx.globalAlpha=1;if(!reduced.matches&&(active||strength>.002))frame=requestAnimationFrame(draw);}
 function request(){if(!frame)frame=requestAnimationFrame(draw)}
 function resize(){const r=panel.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);request()}
 panel.addEventListener('pointermove',e=>{if(reduced.matches||e.pointerType==='touch')return;const r=panel.getBoundingClientRect();x=e.clientX-r.left;y=e.clientY-r.top;active=true;request()},{passive:true});
 panel.addEventListener('pointerleave',()=>{active=false;request()},{passive:true});
 new ResizeObserver(resize).observe(panel);resize();
});
layout();
''')
t = sub1(t, '.svc{position:absolute;border-radius:8px;', '.svc{position:absolute;border-radius:var(--wd-panel-radius,32px);')
# cards e "SOLUÇÕES + WORK" alinhados com o retângulo do menu (mesma largura máxima e margens do menu)
t = sub1(t, '.board{position:relative;max-width:1640px;margin:0 auto 18vh;padding:0 clamp(16px,4.5vw,96px)}',
         '.board{position:relative;width:min(calc(100% - 2 * var(--wd-layout-gutter,3vw)),1440px);margin:0 auto 18vh;padding:0}')
t = sub1(t, '.words .w1{position:absolute;left:3.5vw;', '.words .w1{position:absolute;left:max(var(--wd-layout-gutter,3vw),calc((100% - 1440px) / 2));margin-left:-.045em;')
t = sub1(t, '.words .w2{position:absolute;right:4vw;', '.words .w2{position:absolute;right:max(var(--wd-layout-gutter,3vw),calc((100% - 1440px) / 2));margin-right:-.02em;')
t = sub1(t, '.words{position:absolute;inset:0;font:300 clamp(80px,15vw,250px)/.86 var(--display);', '.words{position:absolute;inset:0;font:300 clamp(48px,15vw,250px)/.86 var(--display);')
t = sub1(t, 'width:.62em;height:.62em;font-size:clamp(80px,15vw,250px)}', 'width:.62em;height:.62em;font-size:clamp(48px,15vw,250px)}')
# "+" dos cards maior, em Space Grotesk
t = sub1(t, '<button class="icon" aria-label="Abrir ${s.name}">${plusSvg}</button>', '<button class="icon" aria-label="Abrir ${s.name}"><span aria-hidden="true">+</span></button>')
t = sub1(t, '.svc .icon svg{width:20px;height:20px;stroke:var(--fg);stroke-width:1.6}',
         '.svc .icon{width:56px;height:56px;margin:-8px -8px 0 0}.svc .icon span{display:block;font:300 56px/1 var(--display);color:var(--fg);transform:translateY(-.04em)}')
# "Ver nossos works" leva para a página de cases
t = sub1(t, '<a class="see" href="#top">', '<a class="see" href="' + PAGES['cases'] + '" target="_top">')
# desempenho do fluido: densidade de pixels 1.25 (era 1.5), 12 iterações de pressão (eram 20), pausa quando a bola está escondida pelo rodapé
# modo leve (GPU fraca): sem a simulação de fluido; ficam a bola em CSS e as palavras com gradiente
t = sub1(t, "  const cv=document.getElementById('fluid'), ref=", "  if(document.documentElement.classList.contains('wd-lite')){document.getElementById('fluid').remove();return;}\n  const cv=document.getElementById('fluid'), ref=")
t = sub1(t, 'dpr=Math.min(devicePixelRatio||1,1.5);', 'dpr=Math.min(devicePixelRatio||1,1.25);')
t = sub1(t, 'for(let i=0;i<20;i++){T(pPres', 'for(let i=0;i<12;i++){T(pPres')
t = sub1(t, 'function frame(now){', "function frame(now){if(bg.style.opacity==='0'){prev=now;requestAnimationFrame(frame);return;}")
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
# cabeçalho do case: sem os botões de som / "Vamos conversar" / menu (só logo e Voltar)
import re as _re
t, _n = _re.subn(r'  <div class="right">.*?\n  </div>\n', '', t, count=1, flags=_re.S); assert _n == 1
# sem o aviso de prévia; logo da Work no lugar do texto
# "Ver projeto no ar" com o CTA padrão da Work (mesmo da seção Transformação digital da home)
t = sub1(t, '<a class="pill light cta" href="#top"><span class="dot"></span> Ver projeto no ar</a>',
         '<a class="wd-work-cta wd-cta cta" href="#top"><span>VER PROJETO NO AR</span><svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.0641 1.14239L.499 12.7061M1.9673.7061h9.5726c.53 0 .9591.4291.9591.9605v9.5712" stroke="currentColor" stroke-width="1.41181"/></svg></a>')
# sem o bloco "Links"
t = sub1(t, '            <h2>Links</h2>\n            <ul><li><a href="#top">Site no ar</a></li><li><a href="#top">Instagram</a></li></ul>\n', '')
t = sub1(t, '            <div class="note">Prévia · textos e imagens de exemplo</div>\n', '')
t = sub1(t, 'aria-label="Work Digital, início">Work Digital</a>', 'aria-label="Work Digital, início"><img class="logo-neg" src="./ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital"><img class="logo-pos" src="./img/logo-work-digital-positivo.svg" alt="" aria-hidden="true"></a>')
# verifica o que está por trás do logo e usa a versão positiva sobre fundos claros
t = t.rstrip() + '''
<script>
(function(){
  const logo=document.querySelector('.hd .logo'); if(!logo)return;
  const hd=document.querySelector('.hd');
  function lum(c){const m=c.match(/[\\d.]+/g);if(!m)return null;const a=m.length>3?+m[3]:1;if(a<.5)return null;return (0.2126*m[0]+0.7152*m[1]+0.0722*m[2])/255;}
  function bgAt(x,y){
    for(const el of document.elementsFromPoint(x,y)){
      if(hd.contains(el)||el.closest('.site-header,wd-footer,.wd-whatsapp'))continue;
      for(let n=el;n&&n!==document.documentElement;n=n.parentElement){const l=lum(getComputedStyle(n).backgroundColor);if(l!==null)return l;}
      return 0;
    }
    return 0;
  }
  function check(){
    const r=logo.getBoundingClientRect();if(!r.width)return;
    const pts=[[.15,.5],[.5,.5],[.85,.5]];let light=0;
    pts.forEach(([fx,fy])=>{if(bgAt(r.left+r.width*fx,r.top+r.height*fy)>.62)light++;});
    logo.classList.toggle('on-light',light>=2);
    // no rodapé (que já tem o logo grande e o CTA) o cabeçalho do case some para não duplicar
    const ft=document.querySelector('wd-footer');
    hd.classList.toggle('over-footer',!!ft&&ft.getBoundingClientRect().top<hd.getBoundingClientRect().bottom+24);
  }
  let busy=false;
  function req(){if(!busy){busy=true;requestAnimationFrame(()=>{busy=false;check();});}}
  addEventListener('scroll',()=>{req();clearTimeout(window.__wdLogoT);window.__wdLogoT=setTimeout(check,350);},{passive:true});
  addEventListener('resize',req,{passive:true});
  setInterval(()=>{if(!document.hidden)check();},400);
  check();
})();
</script>
'''

for a, b in [('<a class="logo" href="#top"', f'<a class="logo" href="{PAGES["home"]}"'), ('<a class="pill light back" href="#top">', f'<a class="pill light back" href="{PAGES["cases"]}">')]:
    t = sub1(t, a, b)
t = apply(t, active='Works', keep_header=True, hidden_home_header=True,
          remove_res=[r'<a class="wa".*?</a>\n'],
          extra_css='''wd-footer{position:relative;z-index:1}
/* Menu da home só como base do painel de contato (o menu antigo continua visível) */
.site-header{opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s}
.site-header.wd-contact-header-open{opacity:1;visibility:visible}
.hd{transition:opacity .3s}
body:has(.site-header.wd-contact-header-open) .hd{opacity:0;pointer-events:none}
.hd .nav-cta{display:inline-flex!important}
.wd-work-cta{display:inline-flex;align-items:center;justify-content:center;gap:16px;width:max-content;max-width:100%;min-height:54px;padding:14px 20px;border:0;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;text-transform:uppercase;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0%;transition:background-position .6s ease,color .2s ease}
.wd-work-cta:hover,.wd-work-cta:focus-visible{background-position:0% 0%;color:#24123e}
.wd-work-cta svg{width:14px;height:14px;flex:0 0 14px}
/* logo: troca para a versão positiva quando passa por cima de uma imagem clara */
.hd .logo{position:relative;display:block}
.hd .logo img{display:block;width:142px;height:auto;transition:opacity .25s ease}
.hd .logo .logo-pos{position:absolute;left:0;top:0;opacity:0}
.hd .logo.on-light .logo-neg{opacity:0}
.hd .logo.on-light .logo-pos{opacity:1}
.hd.over-footer{opacity:0!important;visibility:hidden;transition:opacity .3s ease,visibility 0s .3s}
@media(max-width:900px){.intro .cta{margin-bottom:36px}.track{height:auto}}
@media(max-width:600px){.hd .logo img{width:120px}}
/* Voltar: vidro escuro com borda (estilo do menu), para não competir com o "Solicitar proposta" */
.hd .pill.light.back{background:rgba(18,19,22,.58);color:#F7F6FB;border:1px solid rgba(189,164,255,.28);backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%)}
.hd .pill.light.back:hover{background:rgba(96,37,225,.42);border-color:rgba(189,164,255,.5)}
html.wd-lite .hd .pill.light.back{background:rgba(18,19,22,.93)}
@media(max-width:600px){.hd .nav-cta{height:42px;padding:0 14px;font-size:11px;letter-spacing:.06em}}
/* galeria: as imagens ficam entre o cabeçalho e o fim da tela (antes encostavam nos botões em telas baixas) */
@media (min-width:901px){.track{padding-top:96px;padding-bottom:28px}.intro{padding-top:0}.m.full{align-self:flex-start;height:100vh;height:100svh;margin-top:-96px}}
''')
import case_lightbox
t = case_lightbox.apply(t)
open(OUT + '/case-interna.html', 'w').write(link_pages(t))

# ---------- Blog (claro) ----------
t = open('blog-work-digital.html').read()
t = sub1(t, '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>',
         '<ul class="cats rv" id="cats" aria-label="Categorias"></ul>\n'
         '    <label class="bsearch rv"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
         '<input id="q" type="search" placeholder="Buscar artigos" aria-label="Buscar artigos"></label>')
t = re.sub(r"const srch=document\.getElementById\('srch'\).*?(?=// Reveal)",
           "const q=document.getElementById('q');\nq.addEventListener('input',()=>{term=q.value.trim().toLowerCase(); apply();});\n\n", t, count=1, flags=re.S)
t = sub1(t, 'const link=p=>p.href?`href="${p.href}" target="_blank" rel="noopener"`:\'href="#"\';', 'const link=p=>`href="' + PAGES['post'] + '" target="_top"`;')
import blog_post_fix
t = blog_post_fix.blog(t)
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
t = blog_post_fix.post(t, OUT)
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
import cases_fix
t = cases_fix.fix(t, OUT + '/img', open(OUT + '/solucoes.html').read())
t = t.replace(' filter:blur(42px);animation:lightFieldDrift', ' animation:lightFieldDrift').replace('@media(max-width:760px){.light-field-inner::before{filter:blur(28px)}}', '')
t, n = re.subn(r'  <section class="cta wrap" id="contato".*?</section>\n', '', t, count=1, flags=re.S); assert n == 1
t, n = re.subn(r'/\* ---------- Copy e-mail ---------- \*/\n.*?\n\};\n', '', t, count=1, flags=re.S); assert n == 1
t = t.replace('r.href = "#case-" + p.slug;', 'r.href = "' + PAGES['case'] + '"; r.target = "_top";')
t = sub1(t, 'a.href = "#case-" + p.slug;', 'a.href = "' + PAGES['case'] + '"; a.target = "_top";')
open(OUT + '/cases.html', 'w').write(link_pages(t))
print('cases ok')

# ---- Blog e Post: fotos embutidas (base64) viram arquivos separados, carregados sob demanda ----
import base64, hashlib
for name in ['blog', 'post']:
    p = OUT + f'/{name}.html'; t = open(p).read()
    def ext(m):
        data = base64.b64decode(m.group(2)); fn = 'img/foto-' + hashlib.md5(data).hexdigest()[:10] + '.jpg'
        open(OUT + '/' + fn, 'wb').write(data); return './' + fn
    t = re.sub(r'data:image/(jpeg|jpg);base64,([A-Za-z0-9+/=]+)', ext, t)
    open(p, 'w').write(t)
print('fotos ok')
