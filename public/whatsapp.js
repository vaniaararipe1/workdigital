/* GERAL — WhatsApp global. Edite somente estas variáveis para configurar. */
const NUMERO_WHATSAPP = 'NUMERO_WHATSAPP';
const MENSAGEM_INICIAL = 'MENSAGEM_INICIAL';
const NUMERO_WHATSAPP_SITES = 'NUMERO_WHATSAPP_SITES';
const MENSAGEM_WHATSAPP_SITES = 'Olá! Quero conversar sobre Criação de Sites.';
const NUMERO_WHATSAPP_BLOGS = 'NUMERO_WHATSAPP_BLOGS';
const MENSAGEM_WHATSAPP_BLOGS = 'Olá! Quero conversar sobre Criação de Blogs.';
const NUMERO_WHATSAPP_LANDING = 'NUMERO_WHATSAPP_LANDING';
const MENSAGEM_WHATSAPP_LANDING = 'Olá! Quero conversar sobre Criação de Landing pages.';
const BOTOES_WHATSAPP = [
 {texto:'Criação de Sites',numero:NUMERO_WHATSAPP_SITES,mensagem:MENSAGEM_WHATSAPP_SITES},
 {texto:'Criação de Blogs',numero:NUMERO_WHATSAPP_BLOGS,mensagem:MENSAGEM_WHATSAPP_BLOGS},
 {texto:'Criação de Landing pages',numero:NUMERO_WHATSAPP_LANDING,mensagem:MENSAGEM_WHATSAPP_LANDING}
];
const TEXTOS_WHATSAPP = {
 titulo:'Work Digital — Atendimento',status:'Como podemos te ajudar?',
 saudacao:'Olá! Bem-vindo à Work Digital. Como podemos te ajudar hoje?',
 assuntos:'Escolha um assunto rápido:',opcoes:['Criação de Sites','Criação de Blogs','Criação de Landing pages'],
 abrir:'Abrir conversa no WhatsApp',pendente:'Número do WhatsApp aguardando configuração.'
};
(() => {
 const CONFIG={numero:NUMERO_WHATSAPP,mensagem:MENSAGEM_INICIAL,textos:TEXTOS_WHATSAPP,botoes:BOTOES_WHATSAPP,...window.WD_WHATSAPP_CONFIG};
 const icon='<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.48 2 2 6.48 2 12c0 1.82.49 3.53 1.35 5L2 22l5.25-1.38c1.43.82 3.09 1.38 4.75 1.38 5.52 0 10-4.48 10-10S17.52 2 12 2zm0 18c-1.5 0-2.98-.39-4.28-1.15l-.31-.18-3.17.83.85-3.09-.2-.32C4.08 14.78 3.6 13.41 3.6 12c0-4.63 3.77-8.4 8.4-8.4s8.4 3.77 8.4 8.4-3.77 8.4-8.4 8.4zm4.59-6.28c-.25-.13-1.48-.73-1.71-.81-.23-.08-.4-.13-.57.13-.17.25-.65.81-.8 1-.15.18-.3.2-.55.08-.25-.13-1.06-.39-2.02-1.25-.75-.67-1.26-1.5-1.41-1.75-.15-.25-.02-.38.11-.5.11-.11.25-.29.38-.44.13-.15.17-.25.25-.42.08-.17.04-.31-.02-.44-.06-.13-.57-1.37-.78-1.88-.2-.5-.41-.43-.57-.44l-.49-.01c-.17 0-.44.06-.67.31-.23.25-.89.87-.89 2.12 0 1.25.91 2.46 1.03 2.63.13.17 1.79 2.73 4.34 3.83.61.26 1.08.42 1.45.54.61.19 1.17.17 1.61.1.49-.07 1.48-.61 1.69-1.2.21-.59.21-1.09.15-1.2-.06-.11-.23-.18-.48-.31z"/></svg>';
 const CSS=`:host{position:fixed;bottom:20px;right:20px;z-index:100;display:flex;flex-direction:column;align-items:flex-end;font-family:"Nunito",system-ui,sans-serif;color:#e4e4e7}*{box-sizing:border-box}button,a{font:inherit}button{cursor:pointer}button:focus-visible,a:focus-visible{outline:2px solid #fff;outline-offset:4px}.wd-whatsapp-toggle{position:relative;display:flex;align-items:center;justify-content:center;width:64px;height:64px;padding:16px;background:#059669;color:white;border:2px solid #34d39980;border-radius:50%;box-shadow:0 25px 50px -12px #05966966;transition:transform .3s,background .3s}.wd-whatsapp-toggle:hover{background:#10b981;transform:scale(1.05)}.wd-whatsapp-toggle:active{transform:scale(.95)}.wd-whatsapp-toggle svg{position:relative;width:28px;height:28px;z-index:1}.wd-whatsapp-pulse{position:absolute;inset:-4px;border-radius:50%;background:#10b981;opacity:.4;animation:wdWhatsappPing 1s cubic-bezier(0,0,.2,1) infinite;pointer-events:none}.wd-whatsapp-badge{position:absolute;right:-4px;top:-4px;padding:2px 8px;font:800 10px/1.5 system-ui;color:white;background:#f97316;border:0;outline:0;box-shadow:none;border-radius:99px}.wd-whatsapp-panel{width:384px;max-width:calc(100vw - 40px);margin-bottom:12px;border-radius:24px;border:1px solid #10b98166;background:#09090b;box-shadow:0 25px 50px -12px #0008;overflow:hidden;animation:wdWhatsappEnter .45s ease-out}.wd-whatsapp-panel[hidden]{display:none}.wd-whatsapp-heading{display:flex;align-items:center;gap:12px;padding:16px;background:linear-gradient(90deg,#059669,#0f766e);color:white}.wd-whatsapp-avatar{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:#fff3;font-weight:700;flex:none}.wd-whatsapp-avatar svg{width:24px;height:24px}.wd-whatsapp-title{margin:0;font-family:"Space Grotesk",system-ui,sans-serif;font-size:14px;font-weight:700;line-height:1.3}.wd-whatsapp-status{font-size:11px;color:#d1fae5}.wd-whatsapp-close{margin-left:auto;border:0;border-radius:8px;background:none;color:white;width:28px;height:28px;font-size:24px}.wd-whatsapp-close:hover{background:#fff3}.wd-whatsapp-body{padding:16px;background:#18181b}.wd-whatsapp-greeting{padding:14px;border:1px solid #27272a;border-radius:16px;background:#09090b;font-size:12px;line-height:1.625;margin:0 0 12px}.wd-whatsapp-topics{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#a1a1aa;margin:0 0 12px}.wd-whatsapp-actions{display:grid;gap:8px}.wd-whatsapp-action{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px;border:1px solid #27272a;border-radius:var(--wd-cta-radius,9999px);background:#09090b;color:#d4d4d8;text-decoration:none;font-size:12px;transition:background .3s,border-color .3s}.wd-whatsapp-action:hover{border-color:#10b981;background:#022c2222;color:#fff}.wd-whatsapp-footer{padding:12px;border-top:1px solid #27272a}.wd-whatsapp-open{width:100%;padding:12px;display:flex;gap:8px;align-items:center;justify-content:center;border:0;border-radius:var(--wd-cta-radius,9999px);background:#059669;color:#fff;font-size:12px;font-weight:700;text-decoration:none}.wd-whatsapp-open svg{width:20px;height:20px}.wd-whatsapp-notice{font-size:11px;line-height:1.5;margin:8px 0 0;color:#d4d4d8}.wd-whatsapp-action[aria-disabled=true],.wd-whatsapp-open[aria-disabled=true]{opacity:.65;cursor:default}button,.wd-whatsapp-action,.wd-whatsapp-open{font-family:"Space Grotesk",system-ui,sans-serif;font-weight:var(--wd-cta-weight,500);letter-spacing:var(--wd-cta-letter-spacing,.1em)}@keyframes wdWhatsappPing{75%,100%{transform:scale(2);opacity:0}}@keyframes wdWhatsappEnter{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}@media(max-width:639px){.wd-whatsapp-panel{width:320px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}`;
 class WDWhatsApp extends HTMLElement{
  constructor(){super();this.attachShadow({mode:'open'});}
  connectedCallback(){
   const root=this.shadowRoot;root.innerHTML=`<style>${CSS}</style><section class="wd-whatsapp-panel" id="wd-whatsapp-panel" aria-label="Atendimento Work Digital" hidden><header class="wd-whatsapp-heading"><span class="wd-whatsapp-avatar">${icon}</span><div><h2 class="wd-whatsapp-title"></h2><span class="wd-whatsapp-status"></span></div><button class="wd-whatsapp-close" type="button" aria-label="Fechar atendimento">×</button></header><div class="wd-whatsapp-body"><p class="wd-whatsapp-greeting"></p><p class="wd-whatsapp-topics"></p><div class="wd-whatsapp-actions"></div></div><div class="wd-whatsapp-footer"><a class="wd-whatsapp-open">${icon}<span></span></a><p class="wd-whatsapp-notice" role="status" hidden></p></div></section><button class="wd-whatsapp-toggle" type="button" aria-expanded="false" aria-controls="wd-whatsapp-panel" aria-label="Atendimento via WhatsApp"><span class="wd-whatsapp-pulse"></span><span class="wd-whatsapp-badge">1</span>${icon}</button>`;
   const texts=CONFIG.textos;for(const [selector,key] of [['.wd-whatsapp-title','titulo'],['.wd-whatsapp-status','status'],['.wd-whatsapp-greeting','saudacao'],['.wd-whatsapp-topics','assuntos'],['.wd-whatsapp-open span','abrir']])root.querySelector(selector).textContent=texts[key];
   let pending=false;
   function configure(a,number,message){
    const raw=String(number).trim(),digits=raw.replace(/\D/g,''),placeholder=raw.startsWith('NUMERO_WHATSAPP');
    a.href=`https://wa.me/${placeholder?raw:digits}?text=${encodeURIComponent(message)}`;a.target='_blank';a.rel='noopener';
    const valid=!placeholder&&/^\d{10,15}$/.test(digits);
    if(!valid){pending=true;a.dataset.pending='true';}
    a.addEventListener('click',event=>{if(!valid){event.preventDefault();const notice=root.querySelector('.wd-whatsapp-notice');notice.hidden=false;notice.textContent=texts.pendente;}});
   }
   CONFIG.botoes.forEach(button=>{const a=document.createElement('a');a.className='wd-whatsapp-action';a.textContent=button.texto;const arrow=document.createElement('span');arrow.textContent='↗';arrow.setAttribute('aria-hidden','true');a.append(arrow);configure(a,button.numero,button.mensagem);root.querySelector('.wd-whatsapp-actions').append(a);});
   configure(root.querySelector('.wd-whatsapp-open'),CONFIG.numero,CONFIG.mensagem);
   if(pending){const notice=root.querySelector('.wd-whatsapp-notice');notice.hidden=false;notice.textContent=texts.pendente;}
   const toggle=root.querySelector('.wd-whatsapp-toggle'),panel=root.querySelector('.wd-whatsapp-panel'),close=root.querySelector('.wd-whatsapp-close');
   const setOpen=open=>{panel.hidden=!open;toggle.setAttribute('aria-expanded',String(open));root.querySelector('.wd-whatsapp-badge').hidden=true;(open?close:toggle).focus();};
   toggle.addEventListener('click',()=>setOpen(panel.hidden));close.addEventListener('click',()=>setOpen(false));
   root.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden){e.preventDefault();setOpen(false);}});
  }
 }
 if(!customElements.get('wd-whatsapp'))customElements.define('wd-whatsapp',WDWhatsApp);
 if(!document.querySelector('wd-whatsapp'))document.body.append(document.createElement('wd-whatsapp'));
})();
