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
open(OUT+'/home.html','w').write(t)
os.makedirs(OUT+'/media',exist_ok=True)
for f in os.listdir(H+'/media'): shutil.copy(H+'/media/'+f, OUT+'/media/'+f)
for f in os.listdir(H+'/ativos-externos'): shutil.copy(H+'/ativos-externos/'+f, OUT+'/ativos-externos/'+f)
print(len(t)); print(sorted(set(re.findall(r'(?:src|href|poster)="(\./[^"]+)"',t))))
