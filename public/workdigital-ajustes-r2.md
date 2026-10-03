# Work Digital — ajustes solicitados

Código aplicado ao preview. O ZIP contém a homepage completa e todos os arquivos necessários, sem incluir páginas de verificação. Somente os pontos solicitados foram alterados.

## GERAL

### 1. Degradê único

A classe está no header e nos quatro uptitles: ACEITE O DESAFIO DO NOVO, EXPLORE, BLOG e CONFIANÇA. Removidos `background`, `color` e `-webkit-text-fill-color` das regras antigas que competiam com o degradê. A tipografia grande do header foi preservada.

```css
:root{--wd-uptitle-gradient:linear-gradient(90deg,#B79BFF 0%,#E58BFF 50%,#FF8FCB 100%)}
.wd-uptitle{background:var(--wd-uptitle-gradient);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
.wd-uptitle:not(.intro-title){font-family:"Space Grotesk",system-ui,sans-serif;font-size:20px;font-weight:500;line-height:1.4;letter-spacing:.2em;text-transform:uppercase}
@media(max-width:991px){.wd-uptitle:not(.intro-title){font-size:16px}}
```
### 2 e 3. Notificação e links do WhatsApp

`whatsapp.js` completo abaixo. Cada opção e o botão principal têm número e mensagem próprios no topo. Troque os quatro números provisórios por números com DDI e DDD. O endereço de cada opção usa `encodeURIComponent` e `target="_blank"`. Enquanto o número for provisório, o clique informa a pendência e não abre um contato inválido. O contorno escuro da notificação foi removido.

```js
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
 const CSS=`:host{position:fixed;bottom:20px;right:20px;z-index:100;display:flex;flex-direction:column;align-items:flex-end;font-family:"Nunito",system-ui,sans-serif;color:#e4e4e7}*{box-sizing:border-box}button,a{font:inherit}button{cursor:pointer}button:focus-visible,a:focus-visible{outline:2px solid #fff;outline-offset:4px}.wd-whatsapp-toggle{position:relative;display:flex;align-items:center;justify-content:center;width:64px;height:64px;padding:16px;background:#059669;color:white;border:2px solid #34d39980;border-radius:50%;box-shadow:0 25px 50px -12px #05966966;transition:transform .3s,background .3s}.wd-whatsapp-toggle:hover{background:#10b981;transform:scale(1.05)}.wd-whatsapp-toggle:active{transform:scale(.95)}.wd-whatsapp-toggle svg{position:relative;width:28px;height:28px;z-index:1}.wd-whatsapp-pulse{position:absolute;inset:-4px;border-radius:50%;background:#10b981;opacity:.4;animation:wdWhatsappPing 1s cubic-bezier(0,0,.2,1) infinite;pointer-events:none}.wd-whatsapp-badge{position:absolute;right:-4px;top:-4px;padding:2px 8px;font:800 10px/1.5 system-ui;color:white;background:#f97316;border:0;outline:0;box-shadow:none;border-radius:99px}.wd-whatsapp-panel{width:384px;max-width:calc(100vw - 40px);margin-bottom:12px;border-radius:24px;border:1px solid #10b98166;background:#09090b;box-shadow:0 25px 50px -12px #0008;overflow:hidden;animation:wdWhatsappEnter .45s ease-out}.wd-whatsapp-panel[hidden]{display:none}.wd-whatsapp-heading{display:flex;align-items:center;gap:12px;padding:16px;background:linear-gradient(90deg,#059669,#0f766e);color:white}.wd-whatsapp-avatar{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:#fff3;font-weight:700;flex:none}.wd-whatsapp-avatar svg{width:24px;height:24px}.wd-whatsapp-title{margin:0;font-family:"Space Grotesk",system-ui,sans-serif;font-size:14px;font-weight:700;line-height:1.3}.wd-whatsapp-status{font-size:11px;color:#d1fae5}.wd-whatsapp-close{margin-left:auto;border:0;border-radius:8px;background:none;color:white;width:28px;height:28px;font-size:24px}.wd-whatsapp-close:hover{background:#fff3}.wd-whatsapp-body{padding:16px;background:#18181b}.wd-whatsapp-greeting{padding:14px;border:1px solid #27272a;border-radius:16px;background:#09090b;font-size:12px;line-height:1.625;margin:0 0 12px}.wd-whatsapp-topics{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#a1a1aa;margin:0 0 12px}.wd-whatsapp-actions{display:grid;gap:8px}.wd-whatsapp-action{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px;border:1px solid #27272a;border-radius:12px;background:#09090b;color:#d4d4d8;text-decoration:none;font-size:12px;transition:background .3s,border-color .3s}.wd-whatsapp-action:hover{border-color:#10b981;background:#022c2222;color:#fff}.wd-whatsapp-footer{padding:12px;border-top:1px solid #27272a}.wd-whatsapp-open{width:100%;padding:12px;display:flex;gap:8px;align-items:center;justify-content:center;border:0;border-radius:12px;background:#059669;color:#fff;font-size:12px;font-weight:700;text-decoration:none}.wd-whatsapp-open svg{width:20px;height:20px}.wd-whatsapp-notice{font-size:11px;line-height:1.5;margin:8px 0 0;color:#d4d4d8}.wd-whatsapp-action[aria-disabled=true],.wd-whatsapp-open[aria-disabled=true]{opacity:.65;cursor:default}@keyframes wdWhatsappPing{75%,100%{transform:scale(2);opacity:0}}@keyframes wdWhatsappEnter{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}@media(max-width:639px){.wd-whatsapp-panel{width:320px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}`;
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
```
## MENU

### HTML

O grupo direito contém idiomas, CTA e controle mobile. SOLUÇÕES e idiomas usam `.nav-item`, `.nav-trigger`, `.dropdown` e `.drop-copy`, com os mesmos estilos e comportamento.

```html
<nav class="site-nav" aria-label="Navegação principal">
    <a class="brand" href="#hero" aria-label="Work Digital — Home">
      <img src="https://workdigital.art.br/wp-content/uploads/2022/05/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital">
    </a>
    <div class="nav-links">
      <a class="nav-link" href="#hero">Home</a>
      <div class="nav-item">
        <button class="nav-trigger" type="button" aria-haspopup="true">Soluções
          <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.25 6 7.75l3.5-3.5" stroke="currentColor" stroke-width="1.2"/></svg>
        </button>
        <div class="dropdown">
          <a href="https://workdigital.art.br/criacao-de-site/"><span class="drop-copy"><strong>Criação de Sites</strong><small>Sites em WordPress de alta performance</small></span></a>
          <a href="https://workdigital.art.br/criacao-de-blog/"><span class="drop-copy"><strong>Criação de Blogs</strong><small>Conteúdo, autoridade e audiência</small></span></a>
          <a href="https://workdigital.art.br/criacao-de-landing-pages/"><span class="drop-copy"><strong>Landing Pages</strong><small>Páginas focadas em conversão</small></span></a>
        </div>
      </div>
      <a class="nav-link" href="https://workdigital.art.br/cases/">Work</a>
      <a class="nav-link" href="https://workdigital.art.br/blog/">Blog</a>
    </div>
    <div class="wd-nav-actions">
      <div class="nav-item wd-language">
        <button class="nav-trigger wd-language-trigger" type="button" aria-label="Idioma do site: Português" aria-haspopup="true" aria-expanded="false" aria-controls="wd-language-dropdown"><svg class="wd-language-globe" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/><ellipse cx="12" cy="12" rx="4" ry="9" stroke="currentColor" stroke-width="1.5"/><path d="M3 12h18" stroke="currentColor" stroke-width="1.5"/></svg>Português<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.25 6 7.75l3.5-3.5" stroke="currentColor" stroke-width="1.2"/></svg></button>
        <div class="dropdown" id="wd-language-dropdown">
          <a href="https://workdigital.art.br/" lang="pt-BR" aria-current="true"><span class="drop-copy"><strong>Português</strong></span></a>
          <a href="https://workdigital.art.br/en/" lang="en"><span class="drop-copy"><strong>English</strong></span></a>
        </div>
      </div>
      <a class="nav-cta" href="https://workdigital.art.br/contato/">SOLICITAR PROPOSTA <span>↗</span></a>
      <button class="mobile-toggle" type="button" aria-label="Abrir menu"><i></i></button>
    </div>
  </nav>
```
### CSS alterado

```css
/* MENU — três grupos; SOLUÇÕES e idiomas usam o mesmo componente. */
.site-nav{display:grid;grid-template-columns:1fr auto 1fr;gap:20px;padding-left:14px;padding-right:14px}
.site-nav .brand{margin-right:0;justify-self:start}
.site-nav .nav-links{justify-self:center}
.wd-nav-actions{display:flex;align-items:center;justify-self:end;gap:24px;min-width:0}
.wd-language .nav-trigger{display:flex;align-items:center;gap:7px}
.wd-language .wd-language-globe{width:18px;height:18px;transform:none!important}
.wd-language .dropdown{left:auto;right:0;transform:translateY(12px) scale(.985)}
.wd-language:hover .dropdown,.wd-language:focus-within .dropdown,.wd-language.wd-dropdown-open .dropdown{transform:translateY(0) scale(1)}
.nav-item.wd-dropdown-open .dropdown{opacity:1;visibility:visible}
.nav-item.wd-dropdown-dismissed .dropdown{opacity:0;visibility:hidden}
.dropdown a:focus-visible{background:rgba(255,255,255,.075);transform:translateX(2px);outline:2px solid #bda4ff;outline-offset:-2px}
@media(max-width:980px){
 .site-nav{grid-template-columns:1fr auto;gap:16px}.wd-nav-actions{gap:16px}
 .wd-language{height:64px}.wd-language .dropdown{width:min(390px,calc(100vw - 48px));top:62px}
 .site-nav.wd-nav-open .nav-links .nav-item.wd-dropdown-open .dropdown{display:block}
}
@media(max-width:600px){.wd-nav-actions{gap:10px}.wd-language .nav-trigger{font-size:11px;letter-spacing:0;gap:4px}.wd-language .wd-language-globe{width:16px;height:16px}}
```
### JS alterado

```js
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
```
## HEADER

A fonte, tamanho e quebras existentes permanecem; apenas a classe do degradê foi acrescentada.

```html
<h1 class="intro-title wd-uptitle"><span>Criação de sites</span><span>profissionais</span></h1>
```
## SOLUÇÕES WORK (`#wd-explore`)

### Medição e causa do corte

Em uma janela desktop de **1440px** (1425px úteis após a barra de rolagem), a área antiga da imagem mede **626,3125 × 735,171875px**. Padding e borda antigos são **0px**. A proporção é aproximadamente **0,852**, enquanto o arquivo 900 × 1100 tem proporção **0,818**. `object-fit: cover` fazia a altura da mídia superar a área visível e recortava topo/base. O `scale(1.05)` dos vídeos agravava esse recorte. `overflow: hidden` exibia apenas a parte que cabia.

Área nova útil: **567,140625 × 693,171875px**, aproximadamente 9:11, com erro menor que 0,01px devido ao arredondamento do navegador. Moldura externa: **609,140625 × 735,171875px**, com padding 20px e borda 1px em cada lado. O topo e a base da moldura se alinham ao painel dos boxes. `ResizeObserver` calcula a largura útil como `(altura dos boxes - 42) * 9 / 11`; o padding e a borda ficam fora da área da mídia. Não há zoom na imagem.

Tablet/celular empilham a mídia abaixo dos boxes e preservam a proporção 9:11. Apenas o canvas interativo permanece; o padrão estático de bolinhas foi apagado do CSS original. A seleção inicial do primeiro card continua com a lógica existente.
### HTML completo atualizado

```html
<section class="wd-explore-section" id="wd-explore" aria-labelledby="wd-explore-heading">
 <div class="wd-explore-layout">
  <canvas class="wd-explore-dots" aria-hidden="true"></canvas>
  <div class="wd-explore-header">
   <div class="wd-explore-intro">
   <h2 class="wd-explore-heading wd-uptitle" id="wd-explore-heading">Aceite o desafio do novo</h2>
   <h2 class="wd-explore-subtitle">Soluções Work</h2>
   </div>
   <a class="wd-explore-cta" href="#contato" data-wd-explore-url="https://workdigital.art.br/contato/">SOLICITE UMA PROPOSTA <svg class="wd-explore-cta-icon" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12 1 1 12M2 1h10v10" stroke="currentColor" stroke-width="1.4"/></svg></a>
  </div>
  <div class="wd-explore-body">
   <div class="wd-explore-list">
   <a class="wd-explore-card is-active" href="#criacao-de-sites" data-wd-explore-url="https://workdigital.art.br/criacao-de-site/">
    <div class="wd-explore-card-title"><h3>Criação de Sites</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Sites profissionais, personalizados, otimizados, de fácil gerenciamento, tornando o seu negócio visível para milhares de clientes e valorizando sua marca.</p>
   </a>
   <a class="wd-explore-card" href="#criacao-de-blogs" data-wd-explore-url="https://workdigital.art.br/criacao-de-blog/">
    <div class="wd-explore-card-title"><h3>Criação de Blogs</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Criação de blogs profissionais para sua marca acessar todo o poder do marketing de conteúdo. Construa sua audiência na web e seja autoridade em sua área de atuação.</p>
   </a>
   <a class="wd-explore-card" href="#criacao-de-landing-pages" data-wd-explore-url="https://workdigital.art.br/criacao-de-landing-pages/">
    <div class="wd-explore-card-title"><h3>Criação de Landing pages</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Atrair não é o suficiente. É preciso conquistar seu visitante no momento em que ele chega a sua página de vendas. Criamos Landing Pages que convertem e alavancam seus resultados.</p>
   </a>
   </div>
   <figure class="wd-explore-photo" aria-label="Imagens das soluções Work Digital">
    <div class="wd-explore-media is-visible" data-wd-service="0"><video class="wd-explore-video" autoplay muted loop playsinline preload="metadata" poster="/media/servico-sites.jpg" aria-label="Animação de Criação de Sites"><source src="/media/criacao-de-sites-servico-sites.webm" type="video/webm"></video></div>
    <div class="wd-explore-media" data-wd-service="1"><video class="wd-explore-video" autoplay muted loop playsinline preload="metadata" poster="/media/servico-blog.jpg" aria-label="Animação de Criação de Blogs"><source src="/media/criacao-de-sites-servico-blog.webm" type="video/webm"></video></div>
    <div class="wd-explore-media" data-wd-service="2"><video class="wd-explore-video" autoplay muted loop playsinline preload="metadata" poster="/media/servico-landing-page.jpg" aria-label="Animação de Criação de Landing pages"><source src="/media/criacao-de-sites-servico-landing-page.webm" type="video/webm"></video></div>
   </figure>
  </div>
 </div>
</section>
```
### CSS alterado

```css
/* SOLUÇÕES WORK — a moldura fica fora da área 9:11. */
#wd-explore .wd-explore-body{grid-template-columns:minmax(0,1fr) auto;align-items:stretch}
#wd-explore .wd-explore-photo{position:relative;box-sizing:border-box;width:calc(var(--wd-media-width,520px) + 42px);height:var(--wd-panel-height,auto);padding:20px;border:1px solid rgba(189,164,255,.2);border-radius:12px;aspect-ratio:auto;background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%);overflow:hidden}
#wd-explore .wd-explore-media{position:absolute;top:20px;left:20px;height:var(--wd-media-height,600px);width:auto;aspect-ratio:9/11;box-sizing:border-box;border-radius:8px;overflow:hidden;opacity:0;visibility:hidden;transition:opacity .6s var(--wd-explore-ease);pointer-events:none}
#wd-explore .wd-explore-media.is-visible{opacity:1;visibility:visible}
#wd-explore .wd-explore-media .wd-explore-video{display:block;position:static;width:100%;height:100%;object-fit:cover;transform:none}
#wd-explore .wd-explore-dots{background:none;background-image:none}
@media(max-width:1199px){
 #wd-explore .wd-explore-body{grid-template-columns:minmax(0,1fr)}
 #wd-explore .wd-explore-photo{width:100%;height:auto;padding:20px;aspect-ratio:auto}
 #wd-explore .wd-explore-media{position:absolute;inset:20px;height:auto;width:calc(100% - 40px);aspect-ratio:9/11}
 #wd-explore .wd-explore-media.is-visible{position:relative;inset:auto;width:100%;height:auto;aspect-ratio:9/11}
}
```
### JS alterado

```js
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
 function show(index){current=index;media.forEach((el,i)=>{const visible=i===index;el.classList.toggle('is-visible',visible);const v=el.querySelector('video');v.pause();if(visible&&!reduced.matches)v.play().catch(()=>{});});}
 cards.forEach((card,i)=>{card.addEventListener('mouseenter',()=>show(i));card.addEventListener('focusin',()=>show(i));card.addEventListener('mouseleave',()=>show(0));card.addEventListener('focusout',()=>show(0));});
 function resize(){if(stacked.matches)return;const h=list.getBoundingClientRect().height;const inner=Math.max(0,h-42);body.style.setProperty('--wd-panel-height',h+'px');body.style.setProperty('--wd-media-height',inner+'px');body.style.setProperty('--wd-media-width',(inner*9/11)+'px');}
 new ResizeObserver(resize).observe(list);stacked.addEventListener('change',resize);reduced.addEventListener('change',()=>show(current));
 new IntersectionObserver(entries=>{if(entries[0].isIntersecting)show(current);else media.forEach(el=>el.querySelector('video').pause());}).observe(root);
 resize();show(0);
})();
```
## TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)

O mapa SVG original permanece byte a byte dentro de `.wd-tr-dots`. Textos, CTA e posicionamento do card foram preservados. A máscara atua só na esfera. O halo externo está no elemento adicional sem máscara, atrás dela.

### HTML — início do card atualizado

```html
<div class="wd-tr-card">
  <div class="wd-tr-glow" aria-hidden="true"></div>
  <div class="wd-tr-glow wd-tr-glow-rim" aria-hidden="true"></div>
  <!-- .wd-tr-globe, mapa SVG e .wd-tr-content permanecem como no index.html completo. -->
```
### CSS alterado

```css
/* TRANSFORMAÇÃO DIGITAL — máscara apenas na esfera; halo fica sem máscara. */
.wd-tr-globe{-webkit-mask-image:radial-gradient(closest-side,#000 93%,transparent 100%);mask-image:radial-gradient(closest-side,#000 93%,transparent 100%);box-shadow:inset 24px 0 40px rgba(255,255,255,.85),inset 70px 0 120px rgba(255,255,255,.45)}
.wd-tr-glow-rim{left:54%;height:150%;width:auto;aspect-ratio:1;background:none;filter:blur(28px);box-shadow:0 0 40px 8px rgba(245,240,255,.9),0 0 120px 30px rgba(214,198,255,.65),0 0 240px 60px rgba(170,145,255,.35);-webkit-mask-image:none;mask-image:none}
@media(min-width:769px) and (max-width:991px){.wd-tr-glow-rim{height:420px;left:calc(50% - 110px);top:auto;bottom:0;transform:none}}
@media(max-width:768px){.wd-tr-glow-rim{height:90%;left:40%;width:auto;filter:blur(28px)}}
@media(prefers-reduced-motion:reduce){#wd-explore .wd-explore-media{transition:none}}
```
## Arquivos completos

Use `index.html` completo do ZIP; os estilos antigos conflitantes já foram removidos dele. Não coloque somente o CSS novo por cima de outra versão antiga do HTML. O restante do site está preservado.

### public/wd-revision.css

```css
/* GERAL */
:root{--wd-uptitle-gradient:linear-gradient(90deg,#B79BFF 0%,#E58BFF 50%,#FF8FCB 100%);--wd-description-font:"Nunito",system-ui,sans-serif;--wd-article-hover:linear-gradient(0deg,#301258,#4b247e)}
p:not(.payoff-copy):not(.wd-transformacao-closing-text):not(.wd-works-eyebrow):not(.wd-transformacao-eyebrow):not(.wd-blog-eyebrow):not(.wd-trust-eyebrow),blockquote,.drop-copy small{font-family:var(--wd-description-font)}
.wd-uptitle:not(.intro-title){font-family:"Space Grotesk",system-ui,sans-serif;font-size:20px;font-weight:500;line-height:1.4;letter-spacing:.2em;text-transform:uppercase}
.wd-section-desc,.intro .wd-section-desc,#wd-works .wd-section-desc,#wd-transformacao .wd-section-desc,#wd-blog .wd-section-desc{font-family:var(--wd-description-font);font-size:18px;font-weight:400;line-height:1.6}
.wd-uptitle{background:var(--wd-uptitle-gradient);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
/* MENU */
.wd-sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}
.dropdown .drop-copy strong{font-size:16px}
.dropdown .drop-copy small{font-size:15px;line-height:1.5}
/* HEADER */
body .payoff{padding-bottom:40px}
#wd-explore{padding-top:40px;padding-bottom:56px}
/* SOLUÇÕES WORK */
#wd-explore .wd-explore-dots{display:block;width:100%;height:100%;background:none;border-radius:inherit;pointer-events:none;z-index:0}
.wd-explore-video{display:block;width:100%;height:100%;object-fit:cover}
.wd-explore-photo>.wd-explore-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}

.wd-explore-card:hover .wd-explore-video,.wd-explore-card:focus-visible .wd-explore-video{transform:scale(1)}
#wd-explore .wd-explore-card.is-active,#wd-explore .wd-explore-card:hover,#wd-explore .wd-explore-card:focus-visible{background:var(--wd-article-hover)}
/* WORKS E FRASE */
#wd-works{padding-top:56px;padding-bottom:48px}
#wd-works .wd-works-header{max-width:1080px;margin-inline:auto}
#wd-works .wd-works-intro{max-width:1000px;margin-inline:auto;text-wrap:balance}
#wd-statement{min-height:0;padding-top:64px;padding-bottom:64px}
#wd-statement .wd-statement-inner{max-width:1360px}
/* CERTIFICAÇÕES — substituem a frase após o card. */
.wd-certifications{width:min(1360px,calc(100% - 64px));display:grid;grid-template-columns:repeat(6,minmax(0,1fr));align-items:center;gap:40px;margin:64px auto 40px}
.wd-certifications img{display:block;width:100%;height:42px;object-fit:contain;filter:brightness(0) invert(1);opacity:.85}
/* CONFIANÇA */
#wd-trust .wd-trust-card:last-child::after{display:none}
#wd-trust .wd-trust-quote{font-family:var(--wd-description-font);font-size:16px;line-height:1.6}
#wd-trust .wd-trust-logo-item{flex-basis:260px;width:260px;height:76px;padding-right:60px}
#wd-trust .wd-trust-logo{max-width:200px;max-height:76px}
@media(max-width:991px){
 .wd-uptitle:not(.intro-title){font-size:16px}
 .wd-section-desc,.intro .wd-section-desc,#wd-works .wd-section-desc,#wd-transformacao .wd-section-desc,#wd-blog .wd-section-desc{font-size:16px}
 #wd-statement .wd-statement-line{white-space:normal}
 
 .wd-certifications{width:calc(100% - 32px);gap:24px;margin-top:48px}
 .wd-certifications img{height:32px}
 
 #wd-trust .wd-trust-quote{font-size:16px}
}
@media(max-width:600px){
 .wd-section-desc,.intro .wd-section-desc,#wd-works .wd-section-desc,#wd-transformacao .wd-section-desc,#wd-blog .wd-section-desc{font-size:15px}
 body .payoff{padding-bottom:24px}#wd-explore{padding-top:24px;padding-bottom:32px}
 #wd-works{padding-top:32px;padding-bottom:32px}#wd-statement{padding-top:40px;padding-bottom:40px}#wd-transformacao{padding-top:24px}
 .wd-certifications{grid-template-columns:repeat(3,minmax(0,1fr));gap:24px 20px;margin:40px auto 24px}.wd-certifications img{height:30px}
 #wd-trust .wd-trust-quote{font-size:15px}
 #wd-trust .wd-trust-logo-item{flex-basis:220px;width:220px;height:66px;padding-right:40px}#wd-trust .wd-trust-logo{max-width:180px;max-height:66px}
}
@media(prefers-reduced-motion:reduce){.wd-explore-image>.wd-explore-video{transform:none;transition:none}}
/* TRANSFORMAÇÃO DIGITAL — HTML/CSS fornecido pela Vânia substitui a iluminação anterior. */
#wd-transformacao{padding-top:32px}
.wd-tr-card{position:relative;overflow:hidden;isolation:isolate;width:calc(100% - 64px);max-width:1360px;height:600px;margin:0 auto;border-radius:16px;background:radial-gradient(55% 75% at 78% 50%,rgba(214,200,255,.55) 0%,rgba(214,200,255,0) 70%),radial-gradient(45% 55% at 38% 105%,rgba(226,214,255,.38) 0%,rgba(226,214,255,0) 70%),linear-gradient(90deg,#24104f 0%,#34187a 35%,#5a3db8 62%,#a993f5 100%);box-shadow:0 0 140px 10px rgba(124,92,255,.28)}
.wd-tr-glow{position:absolute;z-index:0;pointer-events:none;top:50%;left:42%;width:70%;aspect-ratio:1;transform:translateY(-50%);border-radius:50%;background:radial-gradient(circle,rgba(238,230,255,.85) 0%,rgba(205,188,255,.45) 40%,rgba(205,188,255,0) 70%);filter:blur(70px)}
.wd-tr-globe{position:absolute;z-index:1;pointer-events:none;top:50%;left:54%;height:150%;aspect-ratio:1;transform:translateY(-50%);border-radius:50%;background:radial-gradient(circle at 4% 50%,rgba(255,255,255,.95) 0%,rgba(255,255,255,0) 18%),radial-gradient(circle at 62% 82%,rgba(252,250,255,.95) 0%,rgba(252,250,255,0) 42%),radial-gradient(circle at 48% 22%,rgba(196,176,255,.75) 0%,rgba(196,176,255,0) 55%),radial-gradient(circle at 55% 50%,#e9e1ff 0%,#ddd0ff 55%,#cfbdff 100%);box-shadow:inset 24px 0 40px rgba(255,255,255,.85),inset 70px 0 120px rgba(255,255,255,.45),0 0 40px 8px rgba(245,240,255,.9),0 0 120px 30px rgba(214,198,255,.65),0 0 240px 60px rgba(170,145,255,.35)}
.wd-tr-dots{position:absolute;inset:0;border-radius:50%;background-image:none;-webkit-mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%);mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%)}
.wd-tr-dots>svg{display:block;position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.wd-tr-content{position:relative;z-index:2;padding:0 80px;height:100%;display:flex;flex-direction:column;justify-content:center;color:#fff;max-width:560px}
/* Retém a largura de leitura, o botão e o título atuais dentro do novo wrapper. */
.wd-tr-content .wd-transformacao-content{width:100%;max-width:none;padding:0}
.wd-tr-content .wd-transformacao-cta{margin-left:0}
@media(min-width:992px){.wd-tr-content{max-width:740px}.wd-tr-content .wd-transformacao-description{max-width:540px}}
@media(min-width:769px) and (max-width:991px){.wd-tr-card{width:calc(100% - 32px)}.wd-tr-content{padding:48px 32px;max-width:600px}}
@media(max-width:768px){
 #wd-transformacao{padding-top:24px}.wd-tr-card{width:calc(100% - 32px);height:auto;min-height:600px}
 .wd-tr-globe{height:90%;left:40%}
 .wd-tr-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse 105% 90% at 5% 30%,rgba(36,16,79,.92) 0%,rgba(36,16,79,.75) 40%,rgba(36,16,79,0) 90%)}
 .wd-tr-content{padding:48px 32px;height:auto;min-height:600px;max-width:none}
 .wd-tr-content .wd-transformacao-description{max-width:620px}
 .wd-tr-glow{filter:blur(55px)}
}
@media(max-width:600px){.wd-tr-content{padding:40px 24px}.wd-tr-content .wd-transformacao-title{white-space:normal}}
/* O seletor também permanece acessível no menu mobile. */
@media(max-width:980px){
 .site-nav.wd-nav-open .nav-links{display:flex;position:absolute;top:76px;left:0;right:0;flex-direction:column;align-items:stretch;gap:0;padding:16px;border:1px solid #bda4ff33;border-radius:16px;background:#24123edb;backdrop-filter:blur(30px)}
 .site-nav.wd-nav-open .nav-links .nav-link,.site-nav.wd-nav-open .nav-links .nav-item,.site-nav.wd-nav-open .nav-links .nav-trigger{height:auto;min-height:44px;width:100%}
 .site-nav.wd-nav-open .nav-links .nav-item{flex-wrap:wrap}
 .site-nav.wd-nav-open .nav-links .dropdown{position:static;display:none;transform:none!important;opacity:1;visibility:visible;width:100%;background:transparent;box-shadow:none;border:0;backdrop-filter:none}
 .site-nav.wd-nav-open .nav-links .nav-item.wd-solutions-open .dropdown{display:block}
}
@media(max-width:600px){.site-nav{gap:8px;padding-left:12px}.site-nav .brand img{width:108px}}
@media(max-width:360px){.site-nav .brand img{width:92px}}
/* Tablet mantém texto acima e globo abaixo; celular preserva contraste sobre o globo. */
@media(min-width:769px) and (max-width:991px){
 .wd-tr-card{height:auto;min-height:0;padding-bottom:420px}
 .wd-tr-content{height:auto;max-width:none}
 .wd-tr-globe{height:420px;top:auto;bottom:0;left:calc(50% - 110px);transform:none}
 .wd-tr-glow{top:auto;bottom:-60px;left:32%;width:75%;transform:none}
}
@media(max-width:768px){
 .wd-tr-card::after{background:radial-gradient(ellipse 140% 110% at 0% 8%,rgba(36,16,79,.96) 0%,rgba(36,16,79,.88) 45%,rgba(36,16,79,.75) 66%,rgba(36,16,79,0) 100%)}
}

/* MENU — três grupos; SOLUÇÕES e idiomas usam o mesmo componente. */
.site-nav{display:grid;grid-template-columns:1fr auto 1fr;gap:20px;padding-left:14px;padding-right:14px}
.site-nav .brand{margin-right:0;justify-self:start}
.site-nav .nav-links{justify-self:center}
.wd-nav-actions{display:flex;align-items:center;justify-self:end;gap:24px;min-width:0}
.wd-language .nav-trigger{display:flex;align-items:center;gap:7px}
.wd-language .wd-language-globe{width:18px;height:18px;transform:none!important}
.wd-language .dropdown{left:auto;right:0;transform:translateY(12px) scale(.985)}
.wd-language:hover .dropdown,.wd-language:focus-within .dropdown,.wd-language.wd-dropdown-open .dropdown{transform:translateY(0) scale(1)}
.nav-item.wd-dropdown-open .dropdown{opacity:1;visibility:visible}
.nav-item.wd-dropdown-dismissed .dropdown{opacity:0;visibility:hidden}
.dropdown a:focus-visible{background:rgba(255,255,255,.075);transform:translateX(2px);outline:2px solid #bda4ff;outline-offset:-2px}
@media(max-width:980px){
 .site-nav{grid-template-columns:1fr auto;gap:16px}.wd-nav-actions{gap:16px}
 .wd-language{height:64px}.wd-language .dropdown{width:min(390px,calc(100vw - 48px));top:62px}
 .site-nav.wd-nav-open .nav-links .nav-item.wd-dropdown-open .dropdown{display:block}
}
@media(max-width:600px){.wd-nav-actions{gap:10px}.wd-language .nav-trigger{font-size:11px;letter-spacing:0;gap:4px}.wd-language .wd-language-globe{width:16px;height:16px}}
/* SOLUÇÕES WORK — a moldura fica fora da área 9:11. */
#wd-explore .wd-explore-body{grid-template-columns:minmax(0,1fr) auto;align-items:stretch}
#wd-explore .wd-explore-photo{position:relative;box-sizing:border-box;width:calc(var(--wd-media-width,520px) + 42px);height:var(--wd-panel-height,auto);padding:20px;border:1px solid rgba(189,164,255,.2);border-radius:12px;aspect-ratio:auto;background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%);overflow:hidden}
#wd-explore .wd-explore-media{position:absolute;top:20px;left:20px;height:var(--wd-media-height,600px);width:auto;aspect-ratio:9/11;box-sizing:border-box;border-radius:8px;overflow:hidden;opacity:0;visibility:hidden;transition:opacity .6s var(--wd-explore-ease);pointer-events:none}
#wd-explore .wd-explore-media.is-visible{opacity:1;visibility:visible}
#wd-explore .wd-explore-media .wd-explore-video{display:block;position:static;width:100%;height:100%;object-fit:cover;transform:none}
#wd-explore .wd-explore-dots{background:none;background-image:none}
@media(max-width:1199px){
 #wd-explore .wd-explore-body{grid-template-columns:minmax(0,1fr)}
 #wd-explore .wd-explore-photo{width:100%;height:auto;padding:20px;aspect-ratio:auto}
 #wd-explore .wd-explore-media{position:absolute;inset:20px;height:auto;width:calc(100% - 40px);aspect-ratio:9/11}
 #wd-explore .wd-explore-media.is-visible{position:relative;inset:auto;width:100%;height:auto;aspect-ratio:9/11}
}
/* TRANSFORMAÇÃO DIGITAL — máscara apenas na esfera; halo fica sem máscara. */
.wd-tr-globe{-webkit-mask-image:radial-gradient(closest-side,#000 93%,transparent 100%);mask-image:radial-gradient(closest-side,#000 93%,transparent 100%);box-shadow:inset 24px 0 40px rgba(255,255,255,.85),inset 70px 0 120px rgba(255,255,255,.45)}
.wd-tr-glow-rim{left:54%;height:150%;width:auto;aspect-ratio:1;background:none;filter:blur(28px);box-shadow:0 0 40px 8px rgba(245,240,255,.9),0 0 120px 30px rgba(214,198,255,.65),0 0 240px 60px rgba(170,145,255,.35);-webkit-mask-image:none;mask-image:none}
@media(min-width:769px) and (max-width:991px){.wd-tr-glow-rim{height:420px;left:calc(50% - 110px);top:auto;bottom:0;transform:none}}
@media(max-width:768px){.wd-tr-glow-rim{height:90%;left:40%;width:auto;filter:blur(28px)}}
@media(prefers-reduced-motion:reduce){#wd-explore .wd-explore-media{transition:none}}
```
### public/wd-revision.js

```js
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
 function show(index){current=index;media.forEach((el,i)=>{const visible=i===index;el.classList.toggle('is-visible',visible);const v=el.querySelector('video');v.pause();if(visible&&!reduced.matches)v.play().catch(()=>{});});}
 cards.forEach((card,i)=>{card.addEventListener('mouseenter',()=>show(i));card.addEventListener('focusin',()=>show(i));card.addEventListener('mouseleave',()=>show(0));card.addEventListener('focusout',()=>show(0));});
 function resize(){if(stacked.matches)return;const h=list.getBoundingClientRect().height;const inner=Math.max(0,h-42);body.style.setProperty('--wd-panel-height',h+'px');body.style.setProperty('--wd-media-height',inner+'px');body.style.setProperty('--wd-media-width',(inner*9/11)+'px');}
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
```
## Alterações — uma linha por item

- **GERAL 1:** Degradê saturado único aplicado aos cinco textos, sem regras antigas sobrescrevendo.
- **GERAL 2:** Borda, outline e sombra da notificação do WhatsApp removidos.
- **GERAL 3:** Links individuais do WhatsApp com números/mensagens editáveis, encodeURIComponent e nova aba.
- **MENU 1:** Select nativo substituído pelo mesmo componente de dropdown de SOLUÇÕES, com globo.
- **MENU 2:** Logo à esquerda, links exatamente centralizados e grupo de idioma/CTA à direita com grid 1fr auto 1fr.
- **HEADER 1:** Criação de sites profissionais usa .wd-uptitle com fonte e dimensões preservadas.
- **SOLUÇÕES WORK 1:** As três mídias usam a mesma moldura com fundo, borda, cantos e padding.
- **SOLUÇÕES WORK 2:** Área interna 9:11 calculada pela altura dos boxes, sem scale e responsiva abaixo deles.
- **SOLUÇÕES WORK 3:** Camada estática removida; permanece apenas o canvas interativo.
- **TRANSFORMAÇÃO DIGITAL 1:** Borda da esfera suavizada com máscara 93%–100%, e brilho externo sem máscara.
