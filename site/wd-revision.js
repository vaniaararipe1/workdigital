/* SOLUÇÕES WORK: mesmo campo de pontos dos cases, incluindo seus valores. */
(() => {
 const panel=document.querySelector('#wd-explore .wd-explore-layout');
 const canvas=panel?.querySelector('.wd-explore-dots');const ctx=canvas?.getContext('2d');if(!ctx)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let width=0,height=0,frame=0,active=false,inView=true,x=-200,y=-200,strength=0;
 function draw(){
  frame=0;strength+=(Number(active)-strength)*.12;
  ctx.clearRect(0,0,width,height);ctx.fillStyle='#bda4ff';
  for(let py=12;py<height;py+=22)for(let px=12;px<width;px+=22){
   const dx=px-x,dy=py-y,distance=Math.hypot(dx,dy);
   const influence=Math.exp(-distance*distance/(90*90))*strength,shift=influence*10/(distance||1);
   ctx.globalAlpha=.09+influence*.35;
   ctx.beginPath();ctx.arc(px+dx*shift,py+dy*shift,.8+influence*.7,0,Math.PI*2);ctx.fill();
  }
  ctx.globalAlpha=1;
  if(!reduced.matches&&inView&&(active||strength>.002))frame=requestAnimationFrame(draw);
 }
 function request(){if(!frame)frame=requestAnimationFrame(draw)}
 function resize(){const r=panel.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);request()}
 panel.addEventListener('pointermove',e=>{if(reduced.matches||e.pointerType==='touch')return;const r=panel.getBoundingClientRect();x=e.clientX-r.left;y=e.clientY-r.top;active=true;request()},{passive:true});
 panel.addEventListener('pointerleave',()=>{active=false;request()},{passive:true});
 new ResizeObserver(resize).observe(panel);
 new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;if(inView)request();else{cancelAnimationFrame(frame);frame=0}}).observe(panel);
 reduced.addEventListener('change',()=>{active=false;strength=0;request()});resize();
})();
/* SOLUÇÕES WORK — moldura com conteúdo 9:11 e vídeos dos três serviços. */
(() => {
 const root=document.getElementById('wd-explore');if(!root)return;
 const body=root.querySelector('.wd-explore-body'),list=root.querySelector('.wd-explore-list');
 const cards=[...root.querySelectorAll('.wd-explore-card')],media=[...root.querySelectorAll('.wd-explore-media')];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),stacked=matchMedia('(max-width:1199px)');
 let current=0;
 const pauseTimers=new Map();
 function show(index){current=index;media.forEach((el,i)=>{const visible=i===index;clearTimeout(pauseTimers.get(el));pauseTimers.delete(el);el.classList.toggle('is-visible',visible);const v=el.querySelector('video');if(visible){if(reduced.matches)v.pause();else v.play().catch(()=>{});}else if(reduced.matches)v.pause();else pauseTimers.set(el,setTimeout(()=>{if(!el.classList.contains('is-visible'))v.pause();pauseTimers.delete(el);},900));});}
 cards.forEach((card,i)=>{card.addEventListener('mouseenter',()=>show(i));card.addEventListener('focusin',()=>show(i));card.addEventListener('mouseleave',()=>show(0));card.addEventListener('focusout',()=>show(0));});
 function resize(){if(stacked.matches)return;const h=list.getBoundingClientRect().height;const inner=Math.max(0,h-40);body.style.setProperty('--wd-panel-height',h+'px');body.style.setProperty('--wd-media-height',inner+'px');body.style.setProperty('--wd-media-width',(inner*9/11)+'px');}
 new ResizeObserver(resize).observe(list);stacked.addEventListener('change',resize);reduced.addEventListener('change',()=>show(current));
 new IntersectionObserver(entries=>{if(entries[0].isIntersecting)show(current);else media.forEach(el=>el.querySelector('video').pause());}).observe(root);
 resize();show(0);
})();
/* MENU mobile: navegação e SOLUÇÕES com toque e teclado. */
(() => {
 const nav=document.querySelector('.site-nav'),toggle=nav?.querySelector('.mobile-toggle');if(!toggle)return;
 const links=nav.querySelector('.nav-links'),solutions=links.querySelector('.nav-item');
 links.id='wd-nav-links';toggle.setAttribute('aria-controls',links.id);toggle.setAttribute('aria-expanded','false');
 function setOpen(open){nav.classList.toggle('wd-nav-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Fechar menu':'Abrir menu');}
 toggle.addEventListener('click',()=>setOpen(!nav.classList.contains('wd-nav-open')));
 nav.addEventListener('keydown',event=>{if(event.key==='Escape'){setOpen(false);solutions?.classList.remove('wd-solutions-open');toggle.focus();}});
 links.addEventListener('click',event=>{if(event.target.closest('a'))setOpen(false)});
})();

/* MENU — mesmo comportamento para SOLUÇÕES e idiomas: mouse, toque, teclado. */
(() => {
 const nav=document.querySelector('.site-nav');if(!nav)return;
 const items=[...nav.querySelectorAll('.nav-item')];
 function close(item,dismiss=false){item.classList.remove('wd-dropdown-open','wd-solutions-open');item.classList.toggle('wd-dropdown-dismissed',dismiss);item.querySelector('.nav-trigger').setAttribute('aria-expanded','false');}
 items.forEach((item,i)=>{
  const trigger=item.querySelector('.nav-trigger'),panel=item.querySelector('.dropdown');if(!trigger||!panel)return;
  panel.id=panel.id||'wd-nav-dropdown-'+i;trigger.setAttribute('aria-controls',panel.id);trigger.setAttribute('aria-expanded','false');
  const open=()=>{items.forEach(other=>{if(other!==item)close(other,true)});item.classList.remove('wd-dropdown-dismissed');item.classList.add('wd-dropdown-open');trigger.setAttribute('aria-expanded','true');};
  item.addEventListener('mouseenter',()=>{if(innerWidth>980||item.classList.contains('wd-language'))open();});
  item.addEventListener('mouseleave',()=>{if(!item.contains(document.activeElement))close(item);});
  trigger.addEventListener('click',()=>{if(item.classList.contains('wd-dropdown-open'))close(item,true);else open();});
  item.addEventListener('focusin',event=>{if(event.target!==trigger)open();});
  item.addEventListener('focusout',event=>{if(!item.contains(event.relatedTarget))close(item);});
  trigger.addEventListener('keydown',event=>{if(event.key==='ArrowDown'){event.preventDefault();open();requestAnimationFrame(()=>panel.querySelector('a').focus());}});
  item.addEventListener('keydown',event=>{if(event.key==='Escape'){event.stopPropagation();close(item,true);trigger.focus();}if(event.key==='ArrowDown'||event.key==='ArrowUp'){const links=[...panel.querySelectorAll('a')],index=links.indexOf(document.activeElement);if(index>=0){event.preventDefault();links[(index+(event.key==='ArrowDown'?1:-1)+links.length)%links.length].focus();}}});
 });
 document.addEventListener('pointerdown',event=>{items.forEach(item=>{if(!item.contains(event.target))close(item,true);});});
})();
