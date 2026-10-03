/* MENU: destinos oficiais de idioma. */
(() => {
 const language=document.getElementById('wd-language-select');
 language?.addEventListener('change',()=>{location.href=language.value==='en'?'https://workdigital.art.br/en/':'https://workdigital.art.br/';});
})();
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
/* Vídeos: reproduzem no hover/foco e respeitam redução de movimento. */
(() => {
 const root=document.getElementById('wd-explore');if(!root)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),mobile=matchMedia('(max-width:991px)');
 const fallback=root.querySelector('.wd-explore-photo video');
 const cards=[...root.querySelectorAll('.wd-explore-card')];let current=null;
 function play(v){if(v&&!reduced.matches)v.play().catch(()=>{});}
 function sync(){
  root.querySelectorAll('video').forEach(v=>{v.muted=true;v.pause();});
  if(reduced.matches)return;
  if(mobile.matches)root.querySelectorAll('video').forEach(play);
  else if(current)play(current.querySelector('video'));else play(fallback);
 }
 cards.forEach(card=>{
  const enter=()=>{current=card;sync();},leave=()=>{if(current===card){current=null;sync();}};
  card.addEventListener('mouseenter',enter);card.addEventListener('focusin',enter);
  card.addEventListener('mouseleave',leave);card.addEventListener('focusout',leave);
 });
 reduced.addEventListener('change',sync);mobile.addEventListener('change',sync);
 new IntersectionObserver(entries=>{if(entries[0].isIntersecting)sync();else root.querySelectorAll('video').forEach(v=>v.pause());}).observe(root);
 sync();
})();
/* MENU mobile: navegação e SOLUÇÕES com toque e teclado. */
(() => {
 const nav=document.querySelector('.site-nav'),toggle=nav?.querySelector('.mobile-toggle');if(!toggle)return;
 const links=nav.querySelector('.nav-links'),solutions=nav.querySelector('.nav-item'),trigger=solutions?.querySelector('.nav-trigger');
 links.id='wd-nav-links';toggle.setAttribute('aria-controls',links.id);toggle.setAttribute('aria-expanded','false');
 function setOpen(open){nav.classList.toggle('wd-nav-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Fechar menu':'Abrir menu');}
 toggle.addEventListener('click',()=>setOpen(!nav.classList.contains('wd-nav-open')));
 trigger?.addEventListener('click',()=>{if(innerWidth>980)return;const open=solutions.classList.toggle('wd-solutions-open');trigger.setAttribute('aria-expanded',String(open));});
 nav.addEventListener('keydown',event=>{if(event.key==='Escape'){setOpen(false);solutions?.classList.remove('wd-solutions-open');toggle.focus();}});
 links.addEventListener('click',event=>{if(event.target.closest('a'))setOpen(false)});
})();
