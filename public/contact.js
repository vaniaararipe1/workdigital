/* Work Digital — painel de contato global.
 * Serviço de e-mail: preencher URL_ENVIO ou window.WD_CONTACT_CONFIG.endpoint.
 * O endpoint deve aceitar POST JSON e responder HTTP 2xx apenas após aceitar o envio.
 * Política: informe a URL oficial antes de ativar o envio.
 */
(() => {
 'use strict';
 const URL_ENVIO = ''; // Ex.: 'https://seu-servico.com/api/contato'
 const URL_PRIVACIDADE = ''; // URL oficial da Política de Privacidade
 const CONFIG = {endpoint:URL_ENVIO,privacyUrl:URL_PRIVACIDADE,...window.WD_CONTACT_CONFIG};
 if(document.querySelector('.wd-contact'))return;
 const source=new URL(document.currentScript?.src||'/contact.js',document.baseURI);
 const css=document.createElement('link');css.rel='stylesheet';css.href=new URL('contact.css?v=20261003-contact3',source).href;document.head.append(css);
 function loadGSAP(){
  if(window.gsap)return Promise.resolve(window.gsap);
  return new Promise(resolve=>{const s=document.createElement('script');s.src='https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js';s.onload=()=>resolve(window.gsap);s.onerror=()=>resolve(null);document.head.append(s)});
 }
 const animationReady=loadGSAP();
 const font=document.createElement('link');font.rel='stylesheet';font.href='https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600&family=Space+Grotesk:wght@400;500;600&display=swap';document.head.append(font);
 const nav=document.querySelector('.site-nav'),oldCTA=nav?.querySelector('.nav-cta'),links=nav?.querySelector('.nav-links');
 if(oldCTA){const slot=document.createElement('span');slot.className='wd-contact-slot';slot.setAttribute('aria-hidden','true');oldCTA.replaceWith(slot)}
 document.body.classList.add('wd-contact-installed');
 document.documentElement.classList.add('wd-contact-root');
 const box=document.createElement('section');box.className='wd-contact';box.id='wd-contact';box.dataset.open='false';box.setAttribute('aria-label','Contato Work Digital');
 box.innerHTML=`<div class="wd-contact-buttons"><button class="wd-contact-menu" type="button" aria-label="Abrir menu" aria-expanded="false"><span class="wd-contact-menu-line"></span><span class="wd-contact-menu-line"></span><span class="wd-contact-menu-line"></span></button><button class="wd-contact-cta" type="button" aria-expanded="false" aria-controls="wd-contact-body">ENTRE EM CONTATO</button></div>
 <div class="wd-contact-body" id="wd-contact-body" inert><h2 class="wd-contact-title" id="wd-contact-heading">Vamos trabalhar juntos.</h2><form class="wd-contact-form" novalidate>
 ${[['nome','Nome completo','text','name'],['email','E-mail','email','email'],['empresa','Empresa ou site','text','organization'],['ideia','Qual é a sua ideia? Como podemos ajudar?','text','off'],['origem','Como você conheceu a Work?','text','off']].map(([name,label,type,auto])=>`<div class="wd-contact-field"><label class="wd-contact-sr-only" for="wd-contact-${name}">${label}</label><input class="wd-contact-input" id="wd-contact-${name}" name="${name}" type="${type}" autocomplete="${auto}" placeholder="${label}" ${name==='nome'||name==='email'?'required':''} aria-describedby="wd-contact-${name}-error"><span class="wd-contact-field-error" id="wd-contact-${name}-error" aria-live="polite"></span></div>`).join('')}
 <div class="wd-contact-foot"><p class="wd-contact-privacy">Ao enviar, você concorda que seus dados serão tratados de acordo com a nossa <a class="wd-contact-privacy-link" target="_blank" rel="noopener">Política de Privacidade</a></p><button class="wd-contact-submit" type="submit">Enviar</button></div></form>
 <div class="wd-contact-result" role="status" aria-live="polite" hidden><h2 class="wd-contact-result-title"></h2><p class="wd-contact-result-text"></p><p class="wd-contact-result-note" hidden></p><button class="wd-contact-close" type="button">Fechar</button></div></div>`;
 document.body.append(box);
 const cta=box.querySelector('.wd-contact-cta'),menu=box.querySelector('.wd-contact-menu'),body=box.querySelector('.wd-contact-body'),bts=box.querySelector('.wd-contact-buttons'),title=box.querySelector('.wd-contact-title'),form=box.querySelector('form'),fields=[...box.querySelectorAll('.wd-contact-field')],foot=box.querySelector('.wd-contact-foot'),submit=box.querySelector('.wd-contact-submit'),result=box.querySelector('.wd-contact-result');
 const privacy=box.querySelector('.wd-contact-privacy-link');
 if(CONFIG.privacyUrl)privacy.href=CONFIG.privacyUrl;
 else {privacy.removeAttribute('target');privacy.setAttribute('aria-disabled','true');privacy.title='URL da Política de Privacidade pendente de configuração';}
 let mobileCTA;
 if(links){mobileCTA=document.createElement('button');mobileCTA.className='wd-contact-mobile-cta';mobileCTA.type='button';mobileCTA.textContent='ENTRE EM CONTATO';mobileCTA.setAttribute('aria-expanded','false');mobileCTA.setAttribute('aria-controls',body.id);links.append(mobileCTA)}
 const reduced=matchMedia('(prefers-reduced-motion: reduce)'),mobile=matchMedia('(max-width:768px)');
 let isOpen=false,closing=false,anim=null,gsapAPI=null,opener=cta,scrollY=0,bodyStyle='',inertStates=[],sending=false,requestController=null,session=0;
 animationReady.then(g=>{gsapAPI=g});
 function lockPage(){scrollY=window.scrollY;bodyStyle=document.body.getAttribute('style')||'';document.body.style.position='fixed';document.body.style.top=-scrollY+'px';document.body.style.width='100%';document.body.style.overflow='hidden';inertStates=[...document.body.children].filter(el=>el!==box&&!['SCRIPT','STYLE','LINK'].includes(el.tagName)).map(el=>[el,el.inert]);inertStates.forEach(([el])=>el.inert=true)}
 function unlockPage(){inertStates.forEach(([el,value])=>el.inert=value);inertStates=[];document.body.setAttribute('style',bodyStyle);window.scrollTo(0,scrollY)}
 function setExpanded(value){[cta,mobileCTA].filter(Boolean).forEach(el=>el.setAttribute('aria-expanded',String(value)));menu.setAttribute('aria-expanded',String(value));menu.setAttribute('aria-label',value?'Fechar contato':'Abrir menu')}
 function setFinalOpen(){box.style.width=mobile.matches?'100%':'477px';box.style.height=mobile.matches?'100dvh':'671px';bts.style.right=mobile.matches?'20px':'-135px';cta.style.right=mobile.matches?'0':'-135px';[title,...fields,foot].forEach(el=>el.style.opacity='1')}
 function resetResult(){form.hidden=false;form.style.opacity='1';result.hidden=true;result.style.opacity='0';submit.disabled=false;submit.textContent='Enviar';sending=false}
 async function abrirContato(trigger=cta){
  if(isOpen||closing)return;isOpen=true;session++;const openSession=session;opener=trigger;anim?.kill();resetResult();nav?.classList.remove('wd-nav-open','wd-contact-nav-open');const toggle=nav?.querySelector('.mobile-toggle');toggle?.setAttribute('aria-expanded','false');toggle?.setAttribute('aria-label','Abrir menu');
  box.dataset.open='true';box.setAttribute('role','dialog');box.setAttribute('aria-modal','true');box.setAttribute('aria-labelledby',title.id);body.inert=false;form.inert=true;cta.tabIndex=-1;setExpanded(true);lockPage();menu.focus({preventScroll:true});
  const g=gsapAPI||await animationReady;if(!isOpen||session!==openSession)return;
  const complete=()=>{if(isOpen){form.inert=false;form.elements.nome.focus({preventScroll:true})}};
  if(!g){setFinalOpen();complete();return}
  g.set([title,...fields,foot],{opacity:0});
  if(mobile.matches||reduced.matches){setFinalOpen();anim=g.timeline({onComplete:complete}).fromTo(body,{opacity:0},{opacity:1,duration:reduced.matches?.12:.25});return}
  anim=g.timeline({defaults:{duration:.5},onComplete:complete});
  anim.to(box,{width:477}).to([bts,cta],{right:-135},'<').to(box,{height:671}).to(bts,{height:60},'<').to(title,{opacity:1},'<');
  // Equivalente a -=1.5, limitado ao início da timeline: não desloca a abertura para tempo negativo.
  anim.to(fields,{opacity:1,stagger:.18},Math.max(0,anim.duration()-1.5)).to(foot,{opacity:1});
 }
 function fecharContato(){
  if(!isOpen)return;closing=true;isOpen=false;session++;requestController?.abort();anim?.kill();body.inert=true;setExpanded(false);
  const complete=()=>{closing=false;cta.tabIndex=0;box.dataset.open='false';box.removeAttribute('role');box.removeAttribute('aria-modal');box.removeAttribute('aria-labelledby');box.style.removeProperty('width');box.style.removeProperty('height');body.style.opacity='1';bts.style.right='0';cta.style.right='0';resetResult();unlockPage();if(opener?.isConnected){if(mobile.matches&&opener===mobileCTA){nav?.classList.add('wd-nav-open');nav?.querySelector('.mobile-toggle')?.setAttribute('aria-expanded','true');nav?.querySelector('.mobile-toggle')?.setAttribute('aria-label','Fechar menu')}opener.focus({preventScroll:true})}};
  if(!gsapAPI){complete();return}
  if(mobile.matches||reduced.matches){anim=gsapAPI.to(body,{opacity:0,duration:.12,onComplete:complete});return}
  anim=gsapAPI.timeline({defaults:{duration:.5},onComplete:complete}).to(box,{height:60}).to(title,{opacity:0},'<').to(box,{width:207}).to([bts,cta],{right:0},'<');
 }
 cta.addEventListener('click',()=>abrirContato(cta));mobileCTA?.addEventListener('click',()=>abrirContato(mobileCTA));
 menu.addEventListener('click',()=>{if(isOpen)fecharContato();else if(nav){nav.classList.toggle(innerWidth<=980?'wd-nav-open':'wd-contact-nav-open');menu.setAttribute('aria-expanded',String(nav.classList.contains('wd-nav-open')||nav.classList.contains('wd-contact-nav-open')))}});
 box.querySelector('.wd-contact-close').addEventListener('click',fecharContato);
 document.addEventListener('pointerdown',e=>{if(isOpen&&!box.contains(e.target)&&e.target!==mobileCTA)fecharContato()});
 document.addEventListener('keydown',e=>{if(!isOpen)return;if(e.key==='Escape'){e.preventDefault();e.stopPropagation();fecharContato();return}if(e.key==='Tab'){const focusable=[...box.querySelectorAll('button,a[href],input')].filter(el=>el.tabIndex>=0&&!el.disabled&&!el.closest('[inert]')&&el.getClientRects().length&&getComputedStyle(el).visibility!=='hidden');const first=focusable[0],last=focusable.at(-1);if(e.shiftKey&&(document.activeElement===first||!box.contains(document.activeElement))){e.preventDefault();last?.focus()}else if(!e.shiftKey&&document.activeElement===last){e.preventDefault();first?.focus()}}},true);
 // Os CTAs de contato existentes, inclusive no rodapé com shadow DOM, usam o mesmo painel.
 document.addEventListener('click',e=>{const link=e.composedPath().find(el=>el.tagName==='A');if(link&&(/\/contato\/?(?:$|[?#])/.test(link.href)||link.getAttribute('href')==='#contato')){e.preventDefault();abrirContato(link)}});
 mobile.addEventListener('change',()=>{if(isOpen){anim?.kill();setFinalOpen();body.style.opacity='1';form.inert=false;form.elements.nome.focus({preventScroll:true})}});
 function validate(){let valid=true;for(const name of ['nome','email']){const input=form.elements[name],ok=input.value.trim()!==''&&(name!=='email'||input.validity.valid);input.setAttribute('aria-invalid',String(!ok));box.querySelector('#wd-contact-'+name+'-error').textContent=ok?'':name==='nome'?'Informe seu nome completo.':'Informe um e-mail válido.';if(!ok&&valid){input.focus();valid=false}}return valid}
 ['nome','email'].forEach(name=>form.elements[name].addEventListener('input',()=>{form.elements[name].removeAttribute('aria-invalid');box.querySelector('#wd-contact-'+name+'-error').textContent=''}));
 async function enviarFormulario(dados){
  if(!CONFIG.endpoint){const error=new Error('Integração de e-mail pendente. Configure URL_ENVIO em contact.js.');error.configuration=true;throw error}
  requestController=new AbortController();const timer=setTimeout(()=>requestController.abort(),20000);
  try{const response=await fetch(CONFIG.endpoint,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(dados),signal:requestController.signal});if(!response.ok)throw new Error('Falha ao enviar formulário');return response}finally{clearTimeout(timer);requestController=null}
 }
 async function showResult(success,error){const thisSession=session;
  const reveal=()=>{if(!isOpen||thisSession!==session)return;form.hidden=true;result.hidden=false;result.querySelector('.wd-contact-result-title').textContent=success?'Obrigado pelo contato!':'Não foi possível enviar';result.querySelector('.wd-contact-result-text').textContent=success?'Recebemos sua mensagem e nossa equipe já está analisando. Em breve entraremos em contato.':'Não foi possível enviar sua mensagem agora. Tente novamente mais tarde.';const note=result.querySelector('.wd-contact-result-note');note.hidden=!error?.configuration;note.textContent=error?.configuration?error.message:'';if(gsapAPI&&!reduced.matches)gsapAPI.to(result,{opacity:1,duration:.3});else result.style.opacity='1';result.querySelector('button').focus({preventScroll:true})};
  if(gsapAPI&&!reduced.matches)gsapAPI.to(form,{opacity:0,duration:.25,onComplete:reveal});else reveal();
 }
 form.addEventListener('submit',async e=>{e.preventDefault();if(sending||!validate())return;sending=true;submit.disabled=true;submit.setAttribute('aria-label','Enviando mensagem');form.setAttribute('aria-busy','true');submit.innerHTML='<svg class="wd-contact-spinner" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2" opacity=".25"/><path d="M12 3a9 9 0 0 1 9 9" stroke="currentColor" stroke-width="2"><animateTransform attributeName="transform" type="rotate" from="0 12 12" to="360 12 12" dur=".75s" repeatCount="indefinite"/></path></svg>';const thisSession=session;try{await enviarFormulario(Object.fromEntries(new FormData(form)));if(isOpen&&session===thisSession){form.reset();showResult(true)}}catch(error){if(isOpen&&session===thisSession)showResult(false,error)}finally{sending=false;form.removeAttribute('aria-busy');submit.removeAttribute('aria-label')}});
 // API pública opcional para integração de outras páginas/CTAs.
 window.WorkDigitalContact={abrirContato,fecharContato,enviarFormulario};
})();
