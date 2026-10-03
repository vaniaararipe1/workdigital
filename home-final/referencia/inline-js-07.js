
// Shared timing and size settings for both particle renderers.
const PARTICLE_SPEED = 1; // Reference rate. 0.8 = slower; 1.2 = faster.
const PARTICLE_COUNT = 40960;
const PARTICLE_SIZE = 0.01; // World units, as in the reference.
const PARTICLE_FIXED_STEP = 1 / 60;
const PARTICLE_POINTER_RESPONSE = -60 * Math.log(1 - 0.07);
// Compatible renderer retains the supplied artwork; GPU uses the fluid solver.
(()=>{
 const art=document.querySelector('.particle-art'),image=art.querySelector('img');
 const canvas=document.createElement('canvas');canvas.setAttribute('aria-hidden','true');art.append(canvas);
 const ctx=canvas.getContext('2d',{alpha:true});if(!ctx)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let particles=[],width=1,height=1,raf=0,last=0,time=0,visible=true,ready=false;
 let mx=0,my=0,tx=0,ty=0,pointerActive=false;
 let randomSeed=921;const random=()=>{randomSeed=(Math.imul(randomSeed,1664525)+1013904223)>>>0;return randomSeed/4294967296;};
 function resize(){const r=art.getBoundingClientRect();width=r.width;height=r.height;const d=devicePixelRatio||1;canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);start();}
 function setup(){
  if(ready)return;
  const source=document.createElement('canvas');source.width=image.naturalWidth;source.height=image.naturalHeight;
  const g=source.getContext('2d',{willReadFrequently:true});g.drawImage(image,0,0);
  const pixels=g.getImageData(0,0,source.width,source.height).data;
  const candidates=[];
  for(let y=330;y<980;y+=2)for(let x=480;x<1100;x+=2){
   const i=(y*source.width+x)*4,brightness=Math.max(pixels[i],pixels[i+1],pixels[i+2]);
   if(brightness<48)continue;
   const px=(x-785)/302,py=(y-650)/335,rr=px*px+py*py;
   if(rr>1.18)continue;
   candidates.push({sx:x,sy:y,x:px,y:py,z:Math.sqrt(Math.max(.015,1-Math.min(.985,rr))),brightness});
  }
  const count=PARTICLE_COUNT;
  // Samples retain the real glyph fragments and luminous variation of the supplied art.
  for(let i=0;i<count;i++){
   const p=candidates[Math.floor(random()*candidates.length)];
   particles.push({...p,z:p.z*(random()<.55?1:-1),phase:random()*6.283,size:.75+random()*.5});
  }
  ready=true;art.classList.add('has-live-particles');resize();start();
 }
 function draw(stamp){
  raf=0;if(!ready||!visible||document.hidden||art.classList.contains("has-native-particles"))return;
  const dt=last?Math.max(0,(stamp-last)/1000):0;last=stamp;
  if(!reduced.matches)time+=dt*PARTICLE_SPEED;
  const smoothing=1-Math.exp(-PARTICLE_POINTER_RESPONSE*dt);
  mx+=(tx-mx)*smoothing;my+=(ty-my)*smoothing;
  ctx.clearRect(0,0,width,height);
  const radius=Math.min(width*.36,height*.225),cx=width*.5,cy=height*.5;
  // One-second opening sweep, then ambient movement after ten seconds.
  const ambient=Math.max(0,time-10);
  const cycle=Math.floor(ambient/6.5);
  const progress=time<1?time:time<10?1:Math.min(1,(ambient%6.5)/6);
  const path=(time<10?7:[7,2,8,3,6,1,9,4][cycle%8])*Math.PI/5;
  const ease=progress<.5?2*progress*progress:1-Math.pow(-2*progress+2,2)/2;
  const travel=-.5+1.5*ease,ax=Math.cos(path)*travel,ay=Math.sin(path)*travel;
  const visibleCount=particles.length;
  for(let particleIndex=0;particleIndex<visibleCount;particleIndex++){
   const p=particles[particleIndex];
   let x=p.x,y=p.y,z=p.z;
   // A travelling pressure field advects independent points; the cloud does not rotate as a rigid object.
   const distance=(x-ax)*(x-ax)+(y-ay)*(y-ay);
   const pressure=Math.exp(-distance*3.8);
   const ripple=Math.sin(x*4+y*3+z*2-time*.7);
   x+=Math.cos(path)*pressure*.19+Math.sin(y*5+z*3-time*.48)*.035;
   y+=Math.sin(path)*pressure*.19+Math.cos(x*4-z*4+time*.42)*.035;
   z+=pressure*.13*ripple;
   const perspective=4.5/(4.5-z),front=(z+1)*.5;
   let dx=cx+x*radius*perspective,dy=cy+y*radius*1.08*perspective;
   if(pointerActive&&!reduced.matches){const vx=dx-mx,vy=dy-my,d=Math.sqrt(vx*vx+vy*vy);const force=Math.exp(-d*d/(radius*radius*.04))*12;dx+=vx/(d+1)*force;dy+=vy/(d+1)*force;}
   const size=(radius*PARTICLE_SIZE/.4)*p.size*perspective;
   dx=Math.max(size/2,Math.min(width-size/2,dx));
   dy=Math.max(size/2,Math.min(height-size/2,dy));
   ctx.globalAlpha=.26+.64*front;
   ctx.drawImage(image,p.sx-3,p.sy-3,6,6,dx-size/2,dy-size/2,size,size);
  }
  ctx.globalAlpha=1;
  if(!reduced.matches)raf=requestAnimationFrame(draw);
 }
 art.addEventListener("nativeparticlesready",()=>{cancelAnimationFrame(raf);raf=0;});
 art.addEventListener("nativeparticlesfailed",()=>start());
 function start(){if(!raf&&ready&&visible&&!document.hidden){last=0;raf=requestAnimationFrame(draw);}}
 new IntersectionObserver(es=>{visible=es[0].isIntersecting;if(visible)start();else{cancelAnimationFrame(raf);raf=0;}},{rootMargin:'100px'}).observe(art);
 new ResizeObserver(resize).observe(art);
 addEventListener('resize',resize,{passive:true});
 addEventListener('pointermove',e=>{const r=art.getBoundingClientRect();tx=e.clientX-r.left;ty=e.clientY-r.top;pointerActive=true;},{passive:true});
 document.addEventListener('pointerleave',()=>{pointerActive=false;});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(raf);raf=0;}else start();});
 reduced.addEventListener('change',()=>{cancelAnimationFrame(raf);raf=0;start();});
 if(image.complete&&image.naturalWidth)setup();else image.addEventListener('load',setup,{once:true});
})();

