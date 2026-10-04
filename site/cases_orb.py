# Página de cases: o mesmo círculo de fluido da página Soluções, à direita do título "Works"
def orb_js(sol):
    i = sol.index('// Fluid orb (WebGL)')
    end = "  requestAnimationFrame(frame);\n})();"
    j = sol.index(end, i) + len(end)
    c = sol[i:j]
    def r(a, b):
        nonlocal c
        assert c.count(a) == 1, a[:60]
        c = c.replace(a, b)
    r("const cv=document.getElementById('fluid'), ref=document.getElementById('orbRef'), bg=document.querySelector('.bgfx');",
      "const cv=document.getElementById('cfluid'), ref=document.getElementById('corbRef'), bg=document.querySelector('.cfx');\n"
      "  new IntersectionObserver(es=>{bg.__off=!es[0].isIntersecting;},{rootMargin:'80px'}).observe(bg);")
    r("document.getElementById('fluid').remove();return;", "document.getElementById('cfluid').remove();return;")
    # a tela do fluido cobre só o topo da página (rola junto), não a janela inteira
    r("cv.width=innerWidth*dpr;cv.height=innerHeight*dpr;", "const cr=cv.getBoundingClientRect();cv.width=Math.round(cr.width*dpr);cv.height=Math.round(cr.height*dpr);")
    r("const o=ref.getBoundingClientRect();rad=o.width/2*dpr;cx=(o.left+o.width/2)*dpr;cy=cv.height-(o.top+o.height/2)*dpr;drawText();",
      "const o=ref.getBoundingClientRect();rad=o.width/2*dpr;cx=(o.left-cr.left+o.width/2)*dpr;cy=cv.height-(o.top-cr.top+o.height/2)*dpr;drawText();")
    r("addEventListener('pointermove',e=>{mx=e.clientX*dpr;my=cv.height-e.clientY*dpr;tmi=1;\n    const u=toUV(e.clientX,e.clientY);",
      "addEventListener('pointermove',e=>{if(bg.__off)return;const cr=cv.getBoundingClientRect(),ex=e.clientX-cr.left,ey=e.clientY-cr.top;mx=ex*dpr;my=cv.height-ey*dpr;tmi=1;\n    const u=toUV(ex,ey);")
    r("if(bg.style.opacity==='0'){", "if(bg.__off){")
    return '<script>\n' + c + '\n</script>\n'

CSS = '''
/* Círculo de fluido (o mesmo da página Soluções), à direita do título */
.hero{position:relative;isolation:isolate}
.hero>*:not(.cfx){position:relative;z-index:1}
.cfx{position:absolute;left:0;right:0;top:0;bottom:-40px;z-index:0;pointer-events:none;overflow:hidden}
.cfx .fluid{position:absolute;inset:0;width:100%;height:100%;display:block}
.cfx .orb{position:absolute;right:clamp(24px,7vw,120px);top:clamp(96px,8vw,124px);width:clamp(240px,26vw,400px);aspect-ratio:1;border-radius:50%;
  background:
    radial-gradient(circle at 62% 30%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 22%),
    radial-gradient(circle at 30% 60%, #ff5fa2 0%, rgba(255,95,162,0) 45%),
    radial-gradient(circle at 70% 70%, #7c5cff 0%, rgba(124,92,255,0) 50%),
    radial-gradient(circle at 45% 45%, #ffb3d9 0%, #c86bff 45%, #5b2fd6 75%, #2a1170 100%);
  filter:saturate(1.15);animation:cfxDrift 18s ease-in-out infinite alternate}
.cfx .orb::after{content:"";position:absolute;inset:-6%;border-radius:50%;background:radial-gradient(circle,rgba(200,140,255,.35),transparent 65%);filter:blur(40px)}
.cfx.gl .orb{visibility:hidden;animation:none}
@keyframes cfxDrift{0%{transform:translate(0,0) rotate(0)}50%{transform:translate(-1.5vw,1.5vh) rotate(20deg)}100%{transform:translate(1vw,2.5vh) rotate(-12deg)}}
@media(max-width:900px){.cfx .orb{width:min(36vw,260px);right:-4vw;top:clamp(104px,16vw,140px)}}
@media(prefers-reduced-motion:reduce){.cfx .orb{animation:none}}
'''
HTML = '<div class="cfx" aria-hidden="true"><div class="orb" id="corbRef"></div><canvas class="fluid" id="cfluid"></canvas></div>\n'
