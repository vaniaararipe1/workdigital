# Popup de contato: nunca forma barra de rolagem — fica mais compacto em telas baixas e, se ainda não couber, reduz o conteúdo proporcionalmente
CSS = '''
/* Telas baixas: espaçamentos menores para o formulário caber inteiro */
@media(min-width:769px) and (max-height:780px){
 .wd-contact{padding:28px 28px 22px}
 .wd-contact .wd-contact-uptitle.wd-uptitle{margin-bottom:8px}
 .wd-contact-title{font-size:26px;margin-bottom:20px}
 .wd-contact-field{margin-bottom:18px}
}
@media(min-width:769px) and (max-height:640px){
 .wd-contact{padding:22px 26px 18px}
 .wd-contact .wd-contact-uptitle.wd-uptitle{margin-bottom:6px;font-size:14px}
 .wd-contact-title{font-size:22px;margin-bottom:14px}
 .wd-contact-field{margin-bottom:12px}
 .wd-contact .wd-contact-input{min-height:31px;height:31px;padding-bottom:8px}
 .wd-contact textarea.wd-contact-input{max-height:56px}
}
@media(max-width:768px) and (max-height:700px){
 .wd-contact{padding:20px 20px 18px}
 .wd-contact-title{font-size:21px;margin-bottom:16px}
 .wd-contact-field{margin-bottom:14px}
}
/* Ajuste final automático (contact.js): o conteúdo encolhe até caber, sem barra de rolagem */
.wd-contact>*{zoom:var(--wd-fit,1)}
.wd-contact,.wd-contact.is-on{scrollbar-width:none}
.wd-contact::-webkit-scrollbar{display:none}
'''
JS = '''
/* Popup de contato sempre inteiro na tela: se o conteúdo passar da altura disponível, ele é reduzido proporcionalmente. */
(() => {
 function boxEl(){return document.querySelector('.wd-contact');}
 let busy=false;
 function fit(){
  const box=boxEl();if(!box||box.dataset.open!=='true')return;
  box.style.setProperty('--wd-fit','1');
  let s=1;
  for(let i=0;i<4;i++){
   const avail=box.clientHeight,need=box.scrollHeight;
   if(!avail||need<=avail+1)break;
   s=Math.max(.55,s*avail/need*.995);box.style.setProperty('--wd-fit',s.toFixed(3));
  }
 }
 function req(){if(busy)return;busy=true;requestAnimationFrame(()=>{busy=false;fit();});}
 function watch(){
  const box=boxEl();if(!box){setTimeout(watch,300);return;}
  new MutationObserver(req).observe(box,{attributes:true,attributeFilter:['class','data-open','style']});
  new ResizeObserver(req).observe(box);
  box.addEventListener('input',req);
  addEventListener('resize',req,{passive:true});
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',watch,{once:true});else watch();
})();
'''
def apply(out):
    p = out + '/contact.css'; c = open(p).read()
    if 'wd-fit' not in c: open(p, 'w').write(c.rstrip() + '\n' + CSS)
    p = out + '/contact.js'; j = open(p).read()
    if 'wd-fit' not in j: open(p, 'w').write(j.rstrip() + '\n' + JS)
