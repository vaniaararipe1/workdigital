import re
S='work-digital-work.html'; H='/home/user/workdigital/home-final/index.html'
t=open(S).read(); h=open(H).read().split('\n')
hdr_css='\n'.join(h[28:59])+'\n'+'\n'.join(h[97:103])+'\n}\n'+'\n'.join(h[192:196])
light_css='''/* Fundo da home: camada de luz fixa (copiada da home) */
body{isolation:isolate}
.light-field{position:fixed;inset:0;z-index:-1;pointer-events:none}
.light-field-inner{position:absolute;inset:0;height:100%;overflow:hidden;background:#121316}
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
home_vars=':root{--purple:#6025E1;--green:#04CD8F;--wine:#C00252}\n'
# fonts + home css links in head
head_add='''<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Nunito:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./wd-revision.css">
<link rel="stylesheet" href="./contact.css">
'''

# page bg -> transparent so light field shows; remove old header/footer css
t=t.replace('body { background: var(--bg);','body { background: transparent;',1)
t=re.sub(r'/\* Header \*/.*?(?=/\* Hero \*/)','',t,flags=re.S)
t=re.sub(r'/\* Footer \*/.*?(?=/\* Responsive \*/)','',t,flags=re.S)
t=re.sub(r'/\* Preview banner \*/\n\.note[^\n]*\n','',t)
for sel in ['  .nav { display: none; }\n','  .burger { display: block; }\n','  .foot-cols { grid-template-columns: 1fr 1fr; }\n','  .foot-cols > div:first-child { grid-column: 1 / -1; }\n']:
  t=t.replace(sel,'')
# hero spacing below fixed menu
t=t.replace('</style>',home_vars+'/* MENU (copiado da home) */\n'+hdr_css+'\n'+light_css+'.hero{padding-top:clamp(150px,14vw,200px)!important}\n</style>\n'+head_add,1)
# markup
new_header='\n'.join(h[245:269]).replace('href="#hero" aria-label','href="https://workdigital-hero-preview.onrender.com/" aria-label')
new_header=new_header.replace('<a class="nav-link" href="#hero">Home</a>','<a class="nav-link" href="https://workdigital-hero-preview.onrender.com/">Home</a>')
new_header=new_header.replace('href="#wd-explore">Soluções','href="https://workdigital-hero-preview.onrender.com/#wd-explore">Soluções')
new_header=new_header.replace('<a class="nav-link" href="https://workdigital.art.br/cases/">Works</a>','<a class="nav-link" href="#topo" aria-current="page">Works</a>')
new_header=new_header.replace('https://workdigital.art.br/wp-content/uploads/2022/05/logo-work-digital-branco-criacao-de-site-sp.svg','./ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg')
t=re.sub(r'<div class="note mono">.*?</div>\n\n','',t,flags=re.S)
t=re.sub(r'<header class="header".*?</header>\n\n<div class="overlay".*?</div>\n</div>\n',  '<div class="light-field" aria-hidden="true"><div class="light-field-inner"></div></div>\n'+new_header+'\n',t,flags=re.S)
t=re.sub(r'<footer class="footer">.*?</footer>\n','',t,flags=re.S)
# JS: drop header/menu/clock
t=re.sub(r'/\* ---------- Header: solid on scroll.*?(?=/\* ---------- Copy e-mail)','',t,flags=re.S)
t=re.sub(r'/\* ---------- Live clock ---------- \*/\n.*?setInterval\(tickClock, 15000\);\n','',t,flags=re.S)
t=t.rstrip()+'\n<script src="./footer.js" defer></script>\n<script src="./wd-revision.js" defer></script>\n'
t='<meta name="viewport" content="width=device-width,initial-scale=1">\n'+t
open('cases-site/cases.html','w').write(t)
print(len(t), 'header' in t and t.count('site-header'), t.count('class="footer"'), t.count('overlay'), t.count('clock'))
