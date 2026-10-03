
(()=>{
 const root=document.getElementById('wd-trust');
 if(!root||root.dataset.initialized)return;
 root.dataset.initialized='true';
 const LOGO_SPEED=11.25; // pixels per second, measured on the Auros partner marquee.
 const track=root.querySelector('.wd-trust-track');
 const marquee=root.querySelector('.wd-trust-marquee');
 const group=root.querySelector('.wd-trust-logo-group');
 const grid=root.querySelector('.wd-trust-grid');
 const cards=[...root.querySelectorAll('.wd-trust-card')];
 const previous=root.querySelector('[data-wd-trust-prev]');
 const next=root.querySelector('[data-wd-trust-next]');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let inView=false;
 function motion(){track.style.animationPlayState=!reduced.matches&&inView&&!document.hidden?'running':'paused';}
 function resize(){track.style.setProperty('--wd-trust-duration',`${group.getBoundingClientRect().width/LOGO_SPEED}s`);navigation();}
 function navigation(){const max=grid.scrollWidth-grid.clientWidth;previous.disabled=grid.scrollLeft<=2;next.disabled=grid.scrollLeft>=max-2;}
 function move(direction){
  const current=cards.reduce((best,card,i)=>Math.abs(card.offsetLeft-grid.offsetLeft-grid.scrollLeft)<Math.abs(cards[best].offsetLeft-grid.offsetLeft-grid.scrollLeft)?i:best,0);
  const target=cards[Math.max(0,Math.min(cards.length-1,current+direction))];
  grid.scrollTo({left:target.offsetLeft-cards[0].offsetLeft,behavior:reduced.matches?'instant':'smooth'});
 }
 previous.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));
 grid.addEventListener('scroll',navigation,{passive:true});
 grid.addEventListener('keydown',event=>{if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();move(event.key==='ArrowRight'?1:-1);}});
 if('IntersectionObserver'in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;motion();},{threshold:0}).observe(marquee);
 else {inView=true;motion();}
 if('ResizeObserver'in window)new ResizeObserver(resize).observe(group);
 window.addEventListener('resize',resize,{passive:true});
 reduced.addEventListener('change',()=>{resize();motion();});
 document.addEventListener('visibilitychange',motion);
 resize();motion();
})();
