
(()=>{
 const root=document.getElementById('wd-transformacao');
 if(!root||root.dataset.wdInitialized)return;
 root.dataset.wdInitialized='true';
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const titles=[document.getElementById('wd-statement-title'),root.querySelector('.wd-transformacao-closing-text')].filter(Boolean);
 const measurement=document.createElement('canvas').getContext('2d');
 const originals=titles.map(el=>el.getAttribute('aria-label'));
 const clamp=x=>Math.min(1,Math.max(0,x));
 const color=(a,b,p)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*p)).join(',')})`;
 let queued=false;
 function split(el,text){
  const twoLines=el.id==='wd-statement-title';
  if(twoLines)el.style.fontSize='';
  const css=getComputedStyle(el),width=el.clientWidth;
  if(!measurement||width<=0)return;
  measurement.font=`${css.fontWeight} ${css.fontSize} ${css.fontFamily}`;
  let spacing=parseFloat(css.letterSpacing)||0;
  const measure=text=>measurement.measureText(text).width+spacing*Math.max(0,text.length-1);
  const lines=[];let line='';
  for(const word of text.split(/\s+/)){
   const candidate=line?`${line} ${word}`:word;
   if(line&&measure(candidate)>width){lines.push(line);line=word;}else line=candidate;
  }
  if(line)lines.push(line);
  if(twoLines && innerWidth>991){
   lines.splice(0,lines.length,'Onde você está','quando seu cliente','NÃO procura por você?');
  }
  const fragment=document.createDocumentFragment();
  lines.forEach((text,i)=>{
   const span=document.createElement('span');span.className=el.id==='wd-statement-title'?'wd-statement-line':'wd-transformacao-line';span.setAttribute('aria-hidden','true');
   const words=text.split(/(NÃO)/);
   words.forEach(word=>{
    if(word==='NÃO'){const strong=document.createElement('strong');strong.className='wd-statement-emphasis';strong.textContent=word;span.append(strong);}else span.append(document.createTextNode(word));
   });
   if(i<lines.length-1)span.append(document.createTextNode(' '));
   fragment.append(span);
  });
  el.replaceChildren(fragment);
 }
 function update(){
  queued=false;
  titles.forEach(el=>{
   const rect=el.getBoundingClientRect(),lines=[...el.children];
   // Auros: top 60% -> bottom 60%, scrubbed color, 0.3 stagger.
   const progress=reduced.matches?1:clamp((innerHeight*.6-rect.top)/Math.max(1,rect.height));
   const duration=1+.3*Math.max(0,lines.length-1);
   lines.forEach((line,i)=>{
    const p=clamp(progress*duration-i*.3);
    line.style.setProperty('--wd-line-from',color([96,37,225],[239,231,255],p));
    line.style.setProperty('--wd-line-to',color([203,182,255],[245,195,216],p));
   });
  });
 }
 function request(){if(!queued){queued=true;requestAnimationFrame(update);}}
 function resize(){titles.forEach((el,i)=>split(el,originals[i]));request();}
 addEventListener('scroll',request,{passive:true});
 addEventListener('resize',resize,{passive:true});
 reduced.addEventListener('change',request);
 document.fonts.ready.then(resize);resize();

})();
