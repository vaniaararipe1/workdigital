
// Anchor the particle viewport below the portfolio CTA, including after font loading.
(()=>{
 const hero=document.querySelector('.hero-sticky'),cta=document.querySelector('.hero-cta'),wrap=document.querySelector('.canvas-wrap');
 function place(){
  const mobile=innerWidth<=760,gap=mobile?8:12;
  const height=innerHeight*1.7;
  // Overlap only the transparent canvas margins with the adjacent sections.
  // Preserve the canvas dimensions, particle scale and simulation unchanged.
  const trimTop=height*(mobile?.33:.23);
  const trimBottom=height*(mobile?.35:.25);
  const top=cta.getBoundingClientRect().bottom-hero.getBoundingClientRect().top+gap-trimTop;
  wrap.style.top=`${top}px`;wrap.style.height=`${height}px`;
  document.querySelector('.intro').style.minHeight=`${top+height-trimBottom+(mobile?10:12)}px`;
 }

 new ResizeObserver(place).observe(document.querySelector('.intro-block'));
 addEventListener('resize',place,{passive:true});
 document.fonts.ready.then(place);place();
})();

// Matches the reference's geometry: start "top 90%", end "bottom top".
// Typography motion stays independent of WebGL / CDN availability.
(()=>{
 const section=document.getElementById('statement');
 const lines=[...section.querySelectorAll('.statement-line > span')];
 const copy=document.querySelector('.payoff-copy');
 const colorLines=[...copy.children];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const clamp=x=>Math.min(1,Math.max(0,x));
 const blend=(a,b,p)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*p)).join(',')})`;
 let queued=false;
 function update(){
  queued=false;
  if(reduced.matches){lines.forEach(el=>el.style.transform='none');return;}
  const vw=document.documentElement.clientWidth,vh=innerHeight;
  const rect=section.getBoundingClientRect();
  const progress=clamp((vh*.9-rect.top)/(vh*.9+rect.height));
  lines.forEach((el,i)=>{
   const w=el.offsetWidth;
   const edge=Math.max(16,vw-w-16);
   const from=i===0?edge:16;
   const to=i===0?16:edge;
   el.style.transform=`translate3d(${from+(to-from)*progress}px,0,0)`;
  });
  const cr=copy.getBoundingClientRect();
  const p=clamp((vh*.6-cr.top)/cr.height);
  colorLines.forEach((el,i)=>{
   const t=clamp(p*1.6-i*.3);
   el.style.setProperty('--from',blend([96,37,225],[246,246,248],t));
   el.style.setProperty('--to',blend([4,205,143],[150,72,253],t));
  });
 }
 function request(){if(!queued){queued=true;requestAnimationFrame(update);}}
 addEventListener('scroll',request,{passive:true});
 addEventListener('resize',request,{passive:true});
 reduced.addEventListener('change',request);
 document.fonts.ready.then(request);
 update();
})();
