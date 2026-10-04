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
             'function resize(){const r=art.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,window.WD_LITE?1:1.5);'),
            ('  const count=PARTICLE_COUNT;\n', '  const count=Math.round(PARTICLE_COUNT*(window.WD_LITE?.2:.4));\n'),
            ('phase:random()*6.283,size:.75+random()*.5});', 'phase:random()*6.283,size:(.75+random()*.5)*(window.WD_LITE?2.1:1.5)});')]:
    assert t.count(a)==1, a[:60]
    t=t.replace(a,b)
# modo leve (GPU fraca): sem partículas na home, como na referência (auros.global) — nem animação nem imagem parada
a=" const art=document.querySelector('.particle-art'),image=art.querySelector('img');\n"
assert t.count(a)==1
t=t.replace(a," const art=document.querySelector('.particle-art'),image=art.querySelector('img');\n if(window.WD_LITE){art.remove();return;}\n")
t=t.replace('</head>','<style>html.wd-lite .particle-art{display:none!important}</style>\n</head>',1)
# modo leve: desenho alternativo a ~30 quadros por segundo
a='raf=0;if(!ready||!visible||document.hidden||art.classList.contains("has-native-particles"))return;\n'
assert t.count(a)==1
t=t.replace(a,a+'  if(window.WD_LITE&&last&&stamp-last<30&&!reduced.matches){raf=requestAnimationFrame(draw);return;}\n')
# Works da home: cada card abre a página interna do case (por enquanto a mesma para todos)
from apply_home import PAGES as _P
i=t.index('<article class="wd-works-card">');j=t.rindex('<article class="wd-works-card">');j=t.index('</article>',j)+len('</article>')
blk=t[i:j]; assert blk.count('<article class="wd-works-card">')==4 and blk.count('</article>')==4
blk=blk.replace('<article class="wd-works-card">','<a class="wd-works-card" href="'+_P['case']+'" target="_top">').replace('</article>','</a>')
t=t[:i]+blk+t[j:]
t=t.replace('</head>','<style>a.wd-works-card{color:inherit;text-decoration:none}a.wd-works-card:first-child{color:#24123e}</style>\n</head>',1)
t=link_pages(t)
# ---- carregamento em conexões lentas ----
import re, subprocess
# 1) arte das partículas: PNG embutido (957 KB em base64) -> WebP embutido (358 KB em base64)
m=re.search(r'data:image/png;base64,([A-Za-z0-9+/=]{100000,})',t); assert m
import base64 as _b64
open('/tmp/_pa.png','wb').write(_b64.b64decode(m.group(1)))
subprocess.run(['ffmpeg','-loglevel','error','-y','-i','/tmp/_pa.png','-c:v','libwebp','-quality','88','-compression_level','6',OUT+'/media/particle-art.webp'],check=True)
# fica embutida (data URI) para o canvas poder ler as cores — arquivo separado bloqueia a leitura (canvas 'tainted')
t=t[:m.start()]+'data:image/webp;base64,'+_b64.b64encode(open(OUT+'/media/particle-art.webp','rb').read()).decode()+t[m.end():]
# 2) vídeos de Soluções só baixam quando a seção aparece (o script da seção já dá play no vídeo visível)
n0=t.count('<video class="wd-explore-video" autoplay muted loop playsinline preload="metadata"')
assert n0==3
t=t.replace('<video class="wd-explore-video" autoplay muted loop playsinline preload="metadata"','<video class="wd-explore-video" muted loop playsinline preload="none"')
# 3) código 3D (1,4 MB) em arquivo separado: o HTML aparece antes e o código fica em cache
i=t.index('<script type="module">'); j=t.index('</script>',i)
app=t[i+len('<script type="module">'):j]
# se a GPU for perdida no meio da animação, o desenho alternativo assume (antes a esfera congelava)
x='experience=new Gse(host);await experience.init();'
assert app.count(x)==1
app=app.replace(x,x+"try{const dev=experience.renderer&&experience.renderer.backend&&experience.renderer.backend.device;if(dev&&dev.lost)dev.lost.then(()=>{try{experience.render(false)}catch(e){}host.remove();art.classList.remove('has-native-particles');art.dispatchEvent(new Event('nativeparticlesfailed'));});}catch(e){}")
open(OUT+'/app.js','w').write(app)
# o código 3D só é baixado quando o navegador tem WebGPU de verdade (sem isso ele não roda e o desenho alternativo assume)
t=t[:i]+'<script>(async()=>{try{if(!window.WD_LITE&&navigator.gpu&&!matchMedia("(prefers-reduced-motion: reduce)").matches&&await navigator.gpu.requestAdapter()){const s=document.createElement("script");s.type="module";s.src="./app.js";document.head.append(s);}}catch(e){}})();</script>'+t[j+len('</script>'):]
open(OUT+'/home.html','w').write(t)
# Soluções da home (telas entre 980 e 1199px): imagem com no máximo 520px e sem medidas antigas da versão larga
js=open(H+'/wd-revision.js').read()
a="function resize(){if(stacked.matches)return;"
assert a in js
# o tamanho da imagem não depende mais da altura da lista (evita o ciclo que fazia a imagem crescer sem parar)
# mesma regra da home original (imagem com a altura da lista, proporção 9:11), mas calculada em poucos passos e com limite
# de 50% da largura — na original o cálculo entrava em ciclo em telas como 1242px e a imagem crescia sem parar
js=js.replace(a,"function resize(){['--wd-panel-height','--wd-media-height','--wd-media-width'].forEach(p=>body.style.removeProperty(p));"
  "if(stacked.matches){body.style.removeProperty('--wd-photo-col');return;}"
  "const bw=body.getBoundingClientRect().width;if(!bw)return;"
  "let col=parseFloat(body.style.getPropertyValue('--wd-photo-col'))||Math.min(640,Math.max(380,bw*.475));"
  "for(let i=0;i<10;i++){body.style.setProperty('--wd-photo-col',col+'px');list.style.alignSelf='start';const h=list.getBoundingClientRect().height;list.style.alignSelf='';"
  "const next=Math.min(bw*.5,Math.max(380,(h-40)*9/11+40));if(Math.abs(next-col)<1){col=next;break;}col+=(next-col)*.7;}"
  "body.style.setProperty('--wd-photo-col',col.toFixed(1)+'px');return;")
# o primeiro vídeo só começa a baixar quando a seção Soluções aparece na tela
assert js.count(' resize();show(0);')==1
js=js.replace(' resize();show(0);'," resize();if(media[0])media[0].classList.add('is-visible');")
open(OUT+'/wd-revision.js','w').write(js)
css=open(H+'/wd-revision.css').read()
css+='''
/* Soluções lado a lado: coluna da imagem com largura fixa (47,5%, entre 380 e 640px — mesmo tamanho de antes em 1440px); a imagem 9:11 ocupa a coluna */
@media(min-width:1200px){
#wd-explore .wd-explore-layout .wd-explore-body{grid-template-columns:minmax(0,1fr) var(--wd-photo-col,clamp(380px,47.5%,640px))!important;align-items:stretch!important}
#wd-explore .wd-explore-photo{width:auto!important;height:auto!important;aspect-ratio:auto!important;padding:20px!important;display:flex;align-items:flex-start}
#wd-explore .wd-explore-photo .wd-explore-media{top:20px!important;left:20px!important;width:calc(100% - 40px)!important;height:auto!important;aspect-ratio:9/11}
#wd-explore .wd-explore-photo .wd-explore-media.is-visible{position:relative!important;top:auto!important;left:auto!important;width:100%!important}
/* a imagem ocupa a altura toda da coluna (igual à original); se a lista for mais alta que 9:11 permite, o vídeo é cortado nas laterais */
#wd-explore .wd-explore-photo{align-items:stretch}
#wd-explore .wd-explore-photo .wd-explore-media{bottom:20px!important;aspect-ratio:auto!important;min-height:0}
#wd-explore .wd-explore-photo .wd-explore-media.is-visible{bottom:auto!important;height:auto!important;align-self:stretch}
}
'''
css+='''
/* Soluções empilhado (até 1199px): imagem centralizada com no máximo 520px de largura */
@media(max-width:1199px){
#wd-explore .wd-explore-photo .wd-explore-media{left:50%!important;right:auto!important;width:min(calc(100% - 40px),520px)!important;transform:translateX(-50%)}
#wd-explore .wd-explore-photo .wd-explore-media.is-visible{left:auto!important;transform:none;margin:0 auto;width:min(100%,520px)!important}
#wd-explore .wd-explore-photo{height:auto!important;aspect-ratio:auto!important}
}
'''
open(OUT+'/wd-revision.css','w').write(css)
os.makedirs(OUT+'/media',exist_ok=True)
for f in os.listdir(H+'/media'): shutil.copy(H+'/media/'+f, OUT+'/media/'+f)
for f in os.listdir(H+'/ativos-externos'): shutil.copy(H+'/ativos-externos/'+f, OUT+'/ativos-externos/'+f)
print(len(t)); print(sorted(set(re.findall(r'(?:src|href|poster)="(\./[^"]+)"',t))))
