
(()=>{
 const section=document.getElementById('wd-works');
 if(!section||section.dataset.wdWorksReady)return;
 section.dataset.wdWorksReady='true';
 const cards=[...section.querySelectorAll('.wd-works-card')];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let entrance;
 if('IntersectionObserver' in window&&!reduced.matches){
  entrance=new IntersectionObserver(entries=>entries.forEach(entry=>{
   if(entry.isIntersecting){entry.target.classList.add('wd-works-visible');entrance.unobserve(entry.target)}
  }),{threshold:.08});
  cards.forEach((card,index)=>{card.style.setProperty('--wd-works-delay',`${index*100}ms`);card.classList.add('wd-works-entering');entrance.observe(card)});
 }
 cards.forEach((card,index)=>{
  const canvas=document.createElement('canvas');canvas.className='wd-works-dots';canvas.setAttribute('aria-hidden','true');card.append(canvas);
  const ctx=canvas.getContext('2d');if(!ctx)return;
  let width=0,height=0,frame=0,active=false,inView=true,x=-200,y=-200,strength=0;
  function draw(){
   frame=0;strength+=(Number(active)-strength)*.12;
   ctx.clearRect(0,0,width,height);ctx.fillStyle=index===0?'#514261':'#bda4ff';
   for(let py=12;py<height;py+=22)for(let px=12;px<width;px+=22){
    const dx=px-x,dy=py-y,distance=Math.hypot(dx,dy);
    const influence=Math.exp(-distance*distance/(90*90))*strength;
    const shift=influence*10/(distance||1);
    ctx.globalAlpha=.09+influence*.35;
    ctx.beginPath();ctx.arc(px+dx*shift,py+dy*shift,.8+influence*.7,0,Math.PI*2);ctx.fill();
   }
   ctx.globalAlpha=1;
   if(!reduced.matches&&inView&&(active||strength>.002))frame=requestAnimationFrame(draw);
  }
  function request(){if(!frame)frame=requestAnimationFrame(draw)}
  function resize(){const r=card.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);request()}
  card.addEventListener('pointermove',event=>{if(reduced.matches||event.pointerType==='touch')return;const r=card.getBoundingClientRect();x=event.clientX-r.left;y=event.clientY-r.top;active=true;request()},{passive:true});
  card.addEventListener('pointerleave',()=>{active=false;request()},{passive:true});
  if('ResizeObserver' in window)new ResizeObserver(resize).observe(card);
  addEventListener('resize',resize,{passive:true});
  if('IntersectionObserver' in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;if(inView)request();else{cancelAnimationFrame(frame);frame=0}}).observe(card);
  reduced.addEventListener('change',()=>{active=false;strength=0;request()});resize();
 });
 reduced.addEventListener('change',()=>{if(reduced.matches){entrance?.disconnect();cards.forEach(card=>card.classList.add('wd-works-visible'))}});
})();
