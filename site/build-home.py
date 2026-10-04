import re, shutil, os
H='/home/user/workdigital/home-final'; OUT='site-build'
t=open(H+'/index.html').read()
# root-absolute paths -> relative (the artifact serves files next to the page)
t=re.sub(r'(src|href|poster)="/(?!/)', r'\1="./', t)
t=re.sub(r'"/(media/[^"]+)"', r'"./\1"', t)
# images loaded from the old site -> local copies shipped with the home package
t=re.sub(r'https://workdigital\.art\.br/wp-content/uploads/\d{4}/\d{2}/([^"\'\s)]+\.(?:jpg|svg|png))', r'./ativos-externos/\1', t)
cursor_css='''<style>
/* Cursor personalizado (igual ao das páginas internas) */
.wd-cursor{position:fixed;left:0;top:0;z-index:2147483000;pointer-events:none;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#F2EEF8;mix-blend-mode:difference;display:grid;place-items:center;
  transition:width .4s cubic-bezier(.22,1,.36,1),height .4s cubic-bezier(.22,1,.36,1),margin .4s cubic-bezier(.22,1,.36,1),background .3s}
.wd-cursor b{font:500 11px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#fff;opacity:0;transition:opacity .2s;white-space:nowrap}
.wd-cursor.link{width:40px;height:40px;margin:-20px 0 0 -20px}
.wd-cursor.big{width:96px;height:96px;margin:-48px 0 0 -48px;background:#6025E1;mix-blend-mode:normal}
.wd-cursor.big b{opacity:1}
@media (hover:hover) and (pointer:fine){.has-wd-cursor,.has-wd-cursor a,.has-wd-cursor button{cursor:none}}
</style>
<div class="wd-cursor" id="wdCursor" aria-hidden="true" hidden><b></b></div>
<script>
(function(){
  if(!matchMedia('(hover: hover) and (pointer: fine)').matches||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c=document.getElementById('wdCursor'), lb=c.querySelector('b'); c.hidden=false; document.body.classList.add('has-wd-cursor');
  const LABELS=[['.wd-works-card','Ver case'],['.wd-blog-link','Ler']];
  let mx=innerWidth/2,my=innerHeight/2,x=mx,y=my;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;},{passive:true});
  document.addEventListener('mouseover',e=>{
    let label=null; for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }
    c.classList.toggle('big',!!label); if(label) lb.textContent=label;
    c.classList.toggle('link',!label && !!e.target.closest('a,button,input,textarea'));
  });
  document.addEventListener('mouseleave',()=>c.classList.remove('big','link'));
  (function tick(){x+=(mx-x)*.18;y+=(my-y)*.18;c.style.transform=`translate(${x}px,${y}px)`;requestAnimationFrame(tick);})();
})();
</script>
'''
# U+FFFD só aparece em literais de string JS de uma biblioteca embutida; o escape \\uFFFD é o mesmo valor
assert t.count('\ufffd')==5
t=t.replace('\ufffd','\\uFFFD')
i=t.rindex('</body>'); t=t[:i]+cursor_css+t[i:]
from apply_home import link_pages
# desempenho (home): sem o blur de tela cheia na camada de luz; no máximo 2 passos de simulação por quadro; densidade de pixels até 1.5
assert t.count('filter:blur(42px);')==2
t=t.replace(' filter:blur(42px);animation:lightFieldDrift',' animation:lightFieldDrift')
t=t.replace('.light-field-inner::before{filter:blur(28px)}','')
a='this.particleAccumulator+=Math.max(0,this.clock.getDelta());'
assert a in t
t=t.replace(a,'this.particleAccumulator=Math.min(this.particleAccumulator+Math.max(0,this.clock.getDelta()),PARTICLE_FIXED_STEP*2);')
a='this.renderer.setPixelRatio(window.devicePixelRatio||1),this.renderer.setSize(n,o)'
assert a in t
t=t.replace(a,'this.renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,1.5)),this.renderer.setSize(n,o)')
# desempenho (home): desenho alternativo das partículas (canvas 2D, usado quando a GPU não está disponível)
# 40% das partículas, 1.5x maiores (mesma cobertura visual) e densidade de pixels até 1.5
for a,b in [('function resize(){const r=art.getBoundingClientRect();width=r.width;height=r.height;const d=devicePixelRatio||1;',
             'function resize(){const r=art.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,1.5);'),
            ('  const count=PARTICLE_COUNT;\n', '  const count=Math.round(PARTICLE_COUNT*.4);\n'),
            ('phase:random()*6.283,size:.75+random()*.5});', 'phase:random()*6.283,size:(.75+random()*.5)*1.5});')]:
    assert t.count(a)==1, a[:60]
    t=t.replace(a,b)
t=link_pages(t)
open(OUT+'/home.html','w').write(t)
# Soluções da home (telas entre 980 e 1199px): imagem com no máximo 520px e sem medidas antigas da versão larga
js=open(H+'/wd-revision.js').read()
a="function resize(){if(stacked.matches)return;"
assert a in js
# o tamanho da imagem não depende mais da altura da lista (evita o ciclo que fazia a imagem crescer sem parar)
js=js.replace(a,"function resize(){['--wd-panel-height','--wd-media-height','--wd-media-width'].forEach(p=>body.style.removeProperty(p));return;")
open(OUT+'/wd-revision.js','w').write(js)
css=open(H+'/wd-revision.css').read()
css+='''
/* Soluções lado a lado: coluna da imagem com largura fixa (42%, entre 380 e 600px); a imagem 9:11 ocupa a coluna */
@media(min-width:1200px){
#wd-explore .wd-explore-layout .wd-explore-body{grid-template-columns:minmax(0,1fr) clamp(380px,42%,600px)!important;align-items:stretch!important}
#wd-explore .wd-explore-photo{width:auto!important;height:auto!important;aspect-ratio:auto!important;padding:20px!important;display:flex;align-items:center}
#wd-explore .wd-explore-photo .wd-explore-media{top:20px!important;left:20px!important;width:calc(100% - 40px)!important;height:auto!important;aspect-ratio:9/11}
#wd-explore .wd-explore-photo .wd-explore-media.is-visible{position:relative!important;top:auto!important;left:auto!important;width:100%!important}
}
'''
css+='''
/* Soluções empilhado (até 1199px): imagem centralizada com no máximo 520px de largura */
@media(max-width:1199px){
#wd-explore .wd-explore-photo .wd-explore-media{left:50%!important;right:auto!important;width:min(calc(100% - 40px),520px)!important;transform:translateX(-50%)}
#wd-explore .wd-explore-photo .wd-explore-media.is-visible{left:auto!important;transform:none;margin:0 auto}
#wd-explore .wd-explore-photo{height:auto!important;aspect-ratio:auto!important}
}
'''
open(OUT+'/wd-revision.css','w').write(css)
os.makedirs(OUT+'/media',exist_ok=True)
for f in os.listdir(H+'/media'): shutil.copy(H+'/media/'+f, OUT+'/media/'+f)
for f in os.listdir(H+'/ativos-externos'): shutil.copy(H+'/ativos-externos/'+f, OUT+'/ativos-externos/'+f)
print(len(t)); print(sorted(set(re.findall(r'(?:src|href|poster)="(\./[^"]+)"',t))))
