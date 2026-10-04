# Case interna: clicar numa imagem do projeto abre em tela cheia (cresce a partir da posição dela)
CSS = '''<style>
/* Tela cheia das imagens do case */
.case-lb{position:fixed;inset:0;z-index:1000;visibility:hidden;pointer-events:none}
.case-lb.open{visibility:visible;pointer-events:auto}
.case-lb-bg{position:absolute;inset:0;background:rgba(12,8,22,.94);opacity:0;transition:opacity .45s cubic-bezier(.22,1,.36,1)}
.case-lb.open .case-lb-bg{opacity:1}
.case-lb-stage{position:absolute;inset:0;overflow:hidden}
.case-lb-item{position:absolute;margin:0!important;align-self:auto;transform-origin:0 0;border-radius:16px!important;box-shadow:0 40px 120px -30px rgba(0,0,0,.7);transition:transform .55s cubic-bezier(.22,1,.36,1),opacity .35s ease}
.case-lb-ui{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s ease}
.case-lb.open.ready .case-lb-ui{opacity:1}
.case-lb-ui>*{pointer-events:auto}
.case-lb-btn{position:absolute;display:grid;place-items:center;width:52px;height:52px;border-radius:50%;border:1px solid rgba(189,164,255,.35);background:rgba(18,19,22,.6);color:#F7F6FB;font:400 22px/1 "Space Grotesk",Arial,sans-serif;transition:background .25s,border-color .25s,transform .25s}
.case-lb-btn:hover,.case-lb-btn:focus-visible{background:linear-gradient(135deg,#6025E1,#C00252);border-color:transparent}
.case-lb-btn:focus-visible{outline:2px solid #CBB6FF;outline-offset:3px}
.case-lb-close{top:24px;right:clamp(16px,3.4vw,48px)}
.case-lb-prev,.case-lb-next{top:50%;margin-top:-26px}
.case-lb-prev{left:clamp(16px,3.4vw,48px)}
.case-lb-next{right:clamp(16px,3.4vw,48px)}
.case-lb-prev:hover{transform:translateX(-3px)}.case-lb-next:hover{transform:translateX(3px)}
.case-lb-count{position:absolute;top:38px;left:clamp(16px,3.4vw,48px);color:#EFE7FF;font:500 13px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.12em}
@media(max-width:700px){.case-lb-prev,.case-lb-next{top:auto;bottom:24px;margin:0}.case-lb-btn{width:46px;height:46px}}
.m{cursor:zoom-in}
html.case-lb-on .hd,html.case-lb-on .wd-whatsapp-root,html.case-lb-on wd-whatsapp{visibility:hidden}
@media(prefers-reduced-motion:reduce){.case-lb-item,.case-lb-bg,.case-lb-ui{transition:none}}
</style>
'''
HTML = '''<div class="case-lb" id="caseLb" role="dialog" aria-modal="true" aria-label="Imagem do projeto em tela cheia" aria-hidden="true">
  <div class="case-lb-bg"></div>
  <div class="case-lb-stage"></div>
  <div class="case-lb-ui">
    <span class="case-lb-count" aria-live="polite"></span>
    <button class="case-lb-btn case-lb-close" type="button" aria-label="Fechar">✕</button>
    <button class="case-lb-btn case-lb-prev" type="button" aria-label="Imagem anterior">←</button>
    <button class="case-lb-btn case-lb-next" type="button" aria-label="Próxima imagem">→</button>
  </div>
</div>
'''
JS = '''<script>
(function(){
  const lb=document.getElementById('caseLb'), stage=lb.querySelector('.case-lb-stage'), count=lb.querySelector('.case-lb-count');
  const items=[...document.querySelectorAll('.track .m')];
  if(!items.length)return;
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let idx=-1, node=null, last=null;
  function fit(src){
    const r=src.getBoundingClientRect(), ratio=r.width/Math.max(1,r.height);
    const padX=innerWidth<=700?16:Math.max(96,innerWidth*.07), padY=innerWidth<=700?96:72;
    let w=innerWidth-padX*2, h=w/ratio;
    if(h>innerHeight-padY*2){h=innerHeight-padY*2;w=h*ratio;}
    return {r,w,h,x:(innerWidth-w)/2,y:(innerHeight-h)/2};
  }
  function build(i){
    const src=items[i], f=fit(src), el=src.cloneNode(true);
    el.removeAttribute('id');el.querySelectorAll('[id]').forEach(n=>n.removeAttribute('id'));
    el.classList.add('case-lb-item');el.setAttribute('aria-hidden','true');
    Object.assign(el.style,{left:f.x+'px',top:f.y+'px',width:f.w+'px',height:f.h+'px',aspectRatio:'auto'});
    return {el,f};
  }
  function fromRect(f){return `translate(${f.r.left-f.x}px,${f.r.top-f.y}px) scale(${f.r.width/f.w},${f.r.height/f.h})`;}
  function show(i,dir){
    i=(i+items.length)%items.length;
    const {el,f}=build(i), old=node;
    if(dir){el.style.transition='none';el.style.opacity='0';el.style.transform=`translateX(${dir*60}px)`;}
    stage.append(el);node=el;idx=i;
    count.textContent=String(i+1).padStart(2,'0')+' / '+String(items.length).padStart(2,'0');
    if(old){old.style.transform=`translateX(${-(dir||1)*60}px)`;old.style.opacity='0';setTimeout(()=>old.remove(),reduce?0:350);}
    requestAnimationFrame(()=>requestAnimationFrame(()=>{el.style.transition='';el.style.opacity='1';el.style.transform='none';}));
  }
  function open(i){
    last=document.activeElement;
    document.documentElement.classList.add('case-lb-on');
    lb.classList.add('open');lb.setAttribute('aria-hidden','false');
    const {el,f}=build(i);idx=i;node=el;
    el.style.transition='none';el.style.transform=reduce?'none':fromRect(f);
    stage.append(el);
    count.textContent=String(i+1).padStart(2,'0')+' / '+String(items.length).padStart(2,'0');
    requestAnimationFrame(()=>requestAnimationFrame(()=>{el.style.transition='';el.style.transform='none';}));
    setTimeout(()=>{lb.classList.add('ready');lb.querySelector('.case-lb-close').focus({preventScroll:true});},reduce?0:380);
  }
  function close(){
    if(!lb.classList.contains('open'))return;
    lb.classList.remove('ready');
    const el=node, f=fit(items[idx]);
    if(el&&!reduce){el.style.transform=fromRect(f);}
    lb.classList.remove('open');
    setTimeout(()=>{stage.replaceChildren();node=null;lb.setAttribute('aria-hidden','true');document.documentElement.classList.remove('case-lb-on');last&&last.focus&&last.focus({preventScroll:true});},reduce?0:550);
  }
  items.forEach((m,i)=>{
    m.setAttribute('role','button');m.tabIndex=0;m.setAttribute('aria-label','Ver imagem '+(i+1)+' em tela cheia');
    m.addEventListener('click',()=>open(i));
    m.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open(i);}});
  });
  lb.querySelector('.case-lb-close').addEventListener('click',close);
  lb.querySelector('.case-lb-bg').addEventListener('click',close);
  stage.addEventListener('click',e=>{if(e.target===stage)close();});
  lb.querySelector('.case-lb-prev').addEventListener('click',()=>show(idx-1,-1));
  lb.querySelector('.case-lb-next').addEventListener('click',()=>show(idx+1,1));
  addEventListener('keydown',e=>{
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape'){e.preventDefault();close();}
    else if(e.key==='ArrowRight'){e.preventDefault();show(idx+1,1);}
    else if(e.key==='ArrowLeft'){e.preventDefault();show(idx-1,-1);}
    else if([' ','PageDown','PageUp','ArrowDown','ArrowUp','Home','End'].includes(e.key))e.preventDefault();
    else if(e.key==='Tab'){const f=[...lb.querySelectorAll('button')];const a=f.indexOf(document.activeElement);e.preventDefault();f[(a+(e.shiftKey?-1:1)+f.length)%f.length].focus();}
  });
  // com a tela cheia aberta a página de trás não rola
  lb.addEventListener('wheel',e=>e.preventDefault(),{passive:false});
  lb.addEventListener('touchmove',e=>e.preventDefault(),{passive:false});
  // deslizar para os lados troca de imagem no celular
  let sx=null;
  lb.addEventListener('touchstart',e=>{sx=e.touches[0].clientX;},{passive:true});
  lb.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;sx=null;if(Math.abs(dx)>50)show(idx+(dx<0?1:-1),dx<0?1:-1);});
  addEventListener('resize',()=>{if(node&&lb.classList.contains('open')){const f=fit(items[idx]);Object.assign(node.style,{left:f.x+'px',top:f.y+'px',width:f.w+'px',height:f.h+'px'});}});
})();
</script>
'''
def apply(t):
    # o círculo "Ver" do cursor não aparece sobre a imagem já aberta
    a = "let label=null; for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }"
    assert t.count(a) == 1
    t = t.replace(a, "let label=null; if(!e.target.closest('.case-lb'))for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }")
    return t.rstrip() + '\n' + CSS + HTML + JS
