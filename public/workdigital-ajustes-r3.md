# Work Digital — ajustes de tipografia, alinhamento e iluminação

Código aplicado à homepage de preview. O ZIP inclui o HTML completo, componentes globais, estilos, scripts e ativos. Os pesos 500 e 600 de Space Grotesk já são carregados pelo Google Fonts junto dos pesos usados anteriormente; os demais textos mantêm as fontes existentes.

## GERAL

### 1. Fonte dos CTAs

Space Grotesk, peso 500 e letter-spacing .1em em menu, seções, rodapé e widget. A classe `.wd-cta` e as duas variáveis também são utilizadas pelos componentes com Shadow DOM.

```html
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">
```

```css
/* GERAL — uma tipografia para CTAs e uma escala para títulos principais. */
:root{--wd-layout-max:1440px;--wd-layout-gutter:3vw;--wd-cta-weight:500;--wd-cta-letter-spacing:.1em}
.wd-cta,button{font-family:"Space Grotesk",system-ui,sans-serif;font-weight:var(--wd-cta-weight);letter-spacing:var(--wd-cta-letter-spacing)}
.wd-section-title{font-size:clamp(36px,4.34vw,64px);font-weight:500;line-height:1.05;letter-spacing:-.041em}
```
### 2. Títulos principais das seções

A classe `.wd-section-title` é usada em Soluções Work, WORKS, Transformação digital, Insights e perspectivas e O que nossos clientes dizem. Os uptitles e as frases de destaque não são títulos principais dessas seções, e mantêm suas funções visuais. Regras antigas de tamanho, peso, line-height e letter-spacing desses cinco títulos foram removidas do HTML.

```html
<h2 class="wd-explore-subtitle wd-section-title">Soluções Work</h2>
<h2 class="wd-works-title wd-section-title" id="wd-works-title">WORKS</h2>
<h2 id="wd-transformacao-title" class="wd-transformacao-title wd-section-title">Transformação digital</h2>
<h2 id="wd-blog-title" class="wd-blog-title wd-section-title">Insights e perspectivas</h2>
<h2 class="wd-trust-title wd-section-title" id="wd-trust-title">O que nossos clientes dizem</h2>
```
## MENU

### 1. Largura compartilhada

`--wd-layout-max: 1440px` e `--wd-layout-gutter` são usados pelo menu e pelo retângulo de Soluções Work.

### 2 e 3. Idiomas e Works

PT ocupa somente a largura do conteúdo, com padding de 10px, globo e seta. As opções e destinos oficiais continuam iguais.

```html
<nav class="site-nav" aria-label="Navegação principal">
    <a class="brand" href="#hero" aria-label="Work Digital — Home">
      <img src="https://workdigital.art.br/wp-content/uploads/2022/05/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital">
    </a>
    <div class="nav-links">
      <a class="nav-link" href="#hero">Home</a>
      <div class="nav-item">
        <button class="nav-trigger wd-cta" type="button" aria-haspopup="true">Soluções
          <svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.25 6 7.75l3.5-3.5" stroke="currentColor" stroke-width="1.2"/></svg>
        </button>
        <div class="dropdown">
          <a href="https://workdigital.art.br/criacao-de-site/"><span class="drop-copy"><strong>Criação de Sites</strong><small>Sites em WordPress de alta performance</small></span></a>
          <a href="https://workdigital.art.br/criacao-de-blog/"><span class="drop-copy"><strong>Criação de Blogs</strong><small>Conteúdo, autoridade e audiência</small></span></a>
          <a href="https://workdigital.art.br/criacao-de-landing-pages/"><span class="drop-copy"><strong>Landing Pages</strong><small>Páginas focadas em conversão</small></span></a>
        </div>
      </div>
      <a class="nav-link" href="https://workdigital.art.br/cases/">Works</a>
      <a class="nav-link" href="https://workdigital.art.br/blog/">Blog</a>
    </div>
    <div class="wd-nav-actions">
      <div class="nav-item wd-language">
        <button class="nav-trigger wd-language-trigger wd-cta" type="button" aria-label="Idioma do site: Português" aria-haspopup="true" aria-expanded="false" aria-controls="wd-language-dropdown"><svg class="wd-language-globe" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/><ellipse cx="12" cy="12" rx="4" ry="9" stroke="currentColor" stroke-width="1.5"/><path d="M3 12h18" stroke="currentColor" stroke-width="1.5"/></svg>PT<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.25 6 7.75l3.5-3.5" stroke="currentColor" stroke-width="1.2"/></svg></button>
        <div class="dropdown" id="wd-language-dropdown">
          <a href="https://workdigital.art.br/" lang="pt-BR" aria-current="true"><span class="drop-copy"><strong>Português</strong></span></a>
          <a href="https://workdigital.art.br/en/" lang="en"><span class="drop-copy"><strong>English</strong></span></a>
        </div>
      </div>
      <a class="nav-cta wd-cta" href="https://workdigital.art.br/contato/">SOLICITAR PROPOSTA <span>↗</span></a>
      <button class="mobile-toggle" type="button" aria-label="Abrir menu"><i></i></button>
    </div>
  </nav>
```

```css
/* MENU — mesma largura e margens do retângulo de Soluções Work. */
.site-header{padding-inline:var(--wd-layout-gutter)}
.site-nav,#wd-explore .wd-explore-layout{width:100%;max-width:var(--wd-layout-max)}
#wd-explore{padding-inline:var(--wd-layout-gutter)}
.wd-language .nav-trigger{width:auto;padding-inline:10px;white-space:nowrap}
@media(max-width:991px){:root{--wd-layout-gutter:24px}}
@media(max-width:479px){:root{--wd-layout-gutter:16px}}
```
## HEADER

### 1. Degradê suave

```css
:root{--wd-uptitle-gradient:linear-gradient(90deg,#FFFFFF 0%,#EDE4FF 45%,#F7C9EC 100%)}
.wd-uptitle{background:var(--wd-uptitle-gradient);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}
```
### 2. H1 maior

No desktop 1440px: **65,52px → 88,452px (+35%)**. Em celulares, o clamp específico evita ampliar a fonte na mesma proporção e quebrar o layout.

```html
<h1 class="intro-title wd-uptitle"><span>Criação de sites</span><span>profissionais</span></h1>
```

```css
/* HEADER — 35% maior no desktop; limite próprio no celular. */
.intro .intro-title{font-size:clamp(72px,6.1425vw,130px)}
@media(max-width:980px){.intro .intro-title{font-size:clamp(42px,10.6vw,68px)}}
```
## SOLUÇÕES WORK (`#wd-explore`)

### 1. Fundo da imagem

O fundo é exatamente o mesmo gradiente transparente do painel dos três boxes, sem borda. O espaço interno continua 9:11. Como a borda de 1px foi removida, o cálculo passa a descontar apenas 40px de padding.

```css
/* SOLUÇÕES WORK — transparência igual à esquerda, sem borda. */
#wd-explore .wd-explore-body .wd-explore-photo{background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%);border:0}
```

```js
function resize(){if(stacked.matches)return;const h=list.getBoundingClientRect().height;const inner=Math.max(0,h-40);body.style.setProperty("--wd-panel-height",h+"px");body.style.setProperty("--wd-media-height",inner+"px");body.style.setProperty("--wd-media-width",(inner*9/11)+"px");}
```
## TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)

O CSS anterior de `.wd-tr-card`, `.wd-tr-glow`, `.wd-tr-globe`, `.wd-tr-dots` e `.wd-tr-content` foi removido, incluindo as variações antigas nas media queries. A camada adicional `.wd-tr-glow-rim` foi removida do HTML. O mapa SVG dos países permanece byte a byte dentro de `.wd-tr-dots`, sem o background-image/background-size de teste.

O desktop usa os gradientes, tamanhos e posicionamentos fornecidos. Apenas o encaixe responsivo é acrescentado: tablet com texto em cima e globo embaixo, e celular com globo atrás e proteção de contraste no texto.

```html
<div class="wd-tr-card">
  <div class="wd-tr-glow" aria-hidden="true"></div>
  <div class="wd-tr-globe" aria-hidden="true">
    <div class="wd-tr-dots"><!-- mapa SVG original preservado no index.html completo --></div>
  </div>
  <div class="wd-tr-content"><!-- conteúdo existente preservado no index.html completo --></div>
</div>
```

```css
/* TRANSFORMAÇÃO DIGITAL — substituição integral pelo CSS enviado. */
.wd-tr-card{position:relative;overflow:hidden;isolation:isolate;width:calc(100% - 64px);max-width:1360px;height:600px;margin:0 auto;border-radius:16px;border:0;background:radial-gradient(60% 90% at 80% 50%,rgba(222,210,255,.60) 0%,rgba(190,170,255,.28) 38%,rgba(190,170,255,0) 72%),radial-gradient(55% 60% at 30% 112%,rgba(232,222,255,.42) 0%,rgba(232,222,255,0) 72%),radial-gradient(70% 90% at 0% 0%,rgba(18,8,44,.55) 0%,rgba(18,8,44,0) 70%),linear-gradient(100deg,#1f0e46 0%,#2d1569 30%,#4a2fa3 58%,#8f78e6 82%,#c9bbff 100%);box-shadow:0 0 160px 20px rgba(124,92,255,.25)}
.wd-tr-glow{position:absolute;z-index:0;pointer-events:none;top:50%;left:54%;height:260%;aspect-ratio:1;transform:translate(-21%,-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(250,247,255,1) 52%,rgba(232,222,255,.85) 58%,rgba(205,188,255,.5) 68%,rgba(170,145,255,.18) 82%,rgba(170,145,255,0) 100%)}
.wd-tr-globe{position:absolute;z-index:1;pointer-events:none;top:50%;left:54%;height:150%;aspect-ratio:1;transform:translateY(-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,0) 80%,rgba(255,255,255,.55) 93%,rgba(250,247,255,1) 100%),radial-gradient(circle at 6% 50%,rgba(255,255,255,1) 0%,rgba(255,255,255,0) 24%),radial-gradient(circle at 62% 82%,rgba(252,250,255,.95) 0%,rgba(252,250,255,0) 42%),radial-gradient(circle at 48% 22%,rgba(196,176,255,.7) 0%,rgba(196,176,255,0) 55%),radial-gradient(circle at 55% 50%,#ebe4ff 0%,#ddd0ff 55%,#cfbdff 100%)}
.wd-tr-dots{position:absolute;inset:0;border-radius:50%;-webkit-mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%);mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%)}
.wd-tr-dots>svg{display:block;position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.wd-tr-content{position:relative;z-index:2;padding:0 80px;height:100%;display:flex;flex-direction:column;justify-content:center;color:#fff;max-width:560px}
.wd-tr-content .wd-transformacao-content{width:100%;max-width:none;padding:0}
.wd-tr-content .wd-transformacao-cta{margin-left:0}
/* Ajustes de encaixe e leitura mantêm o responsivo atual. */
.wd-tr-content .wd-transformacao-title{white-space:normal;text-wrap:balance}
@media(min-width:769px) and (max-width:991px){
 .wd-tr-card{width:calc(100% - 32px);height:auto;min-height:0;padding-bottom:420px}
 .wd-tr-content{padding:48px 32px;height:auto;max-width:none}
 .wd-tr-globe{height:420px;top:auto;bottom:0;left:calc(50% - 110px);transform:none}
 .wd-tr-glow{height:728px;top:auto;bottom:-154px;left:calc(50% - 110px);transform:translateX(-21%)}
}
@media(max-width:768px){
 .wd-tr-card{width:calc(100% - 32px);height:auto;min-height:600px}
 .wd-tr-globe{height:90%;left:40%}
 .wd-tr-glow{height:156%;left:40%}
 .wd-tr-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse 140% 110% at 0% 8%,rgba(31,14,70,.96) 0%,rgba(31,14,70,.88) 45%,rgba(31,14,70,.75) 66%,rgba(31,14,70,0) 100%)}
 .wd-tr-content{padding:48px 32px;height:auto;min-height:600px;max-width:none}
}
@media(max-width:600px){.wd-tr-content{padding:40px 24px}}
```
## RODAPÉ

### 1. Ordem das redes sociais

LinkedIn / Instagram / Facebook. Segue o componente completo atualizado, incluindo a tipografia padronizada do CTA.

```js
/* Work Digital — rodapé global.
 * Incluir em qualquer página: <script src="/footer.js" defer></script>
 * O script insere <wd-footer> automaticamente quando ele não existe.
 * Use data-manual no script para escolher a posição com <wd-footer>.
 * Redes sem URL (string vazia) são removidas da interface.
 */
(() => {
  const script = document.currentScript;
  const source = new URL(script?.src || '/footer.js', document.baseURI);
  const CONFIG = {
    logo: new URL('img/logo-work-digital.svg', source).href,
    home: 'https://workdigital.art.br/',
    contact: 'https://workdigital.art.br/contato/',
    instagram: 'https://www.instagram.com/workdigitalbr/',
    linkedin: 'https://www.linkedin.com/company/workdigitalbr',
    facebook: 'https://www.facebook.com/workdigital.global',
    whatsapp: '',
    email: ''
  };
  const CSS = `
    :host{display:block;min-width:0;scroll-margin-top:110px;color:#f7f6fb;font-family:"Space Grotesk",Arial,sans-serif}
    *,*::before,*::after{box-sizing:border-box}
    .wd-footer-root{background:transparent;padding:140px clamp(20px,5.3vw,84px) 80px}
    .wd-footer-inner{max-width:1440px;margin:0 auto;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:140px 80px}
    .wd-footer-brand{min-width:0}
    .wd-footer-home{display:block;width:min(400px,100%);border-radius:4px}
    .wd-footer-logo{display:block;width:100%;height:auto;aspect-ratio:4340/1340;object-fit:contain}
    .wd-footer-description{max-width:430px;margin:28px 0 0;color:#e1d7ee;font:400 18px/1.6 "Nunito",system-ui,sans-serif;text-wrap:pretty}
    .wd-footer-contact{display:flex;flex-direction:column;align-items:flex-end;gap:24px;min-width:0}
    .wd-footer-title{margin:0;font-size:38px;font-weight:400;line-height:1.3;letter-spacing:-.025em;text-align:right;text-wrap:balance}
    .wd-footer-cta{display:flex;align-items:center;justify-content:center;gap:20px;min-height:54px;max-width:100%;padding:18px 20px;border-radius:6px;color:#fff;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0;text-decoration:none;font-size:14px;font-family:"Space Grotesk",system-ui,sans-serif;font-weight:var(--wd-cta-weight,500);line-height:1;letter-spacing:var(--wd-cta-letter-spacing,.1em);transition:background-position 600ms ease,color 200ms ease}
    .wd-footer-cta svg{flex:none;width:14px;height:14px}
    .wd-footer-cta:hover,.wd-footer-cta:focus-visible{background-position:0 0;color:#2b1450}
    .wd-footer-rights{display:flex;flex-wrap:wrap;align-items:center;align-self:center;gap:8px 16px;color:#e1d7ee;font-size:14px;line-height:1.4;margin:0}
    .wd-footer-rights-brand{color:inherit;text-decoration:none;transition:color .2s ease}
    .wd-footer-divider{display:inline;color:inherit}
    .wd-footer-socials{display:flex;flex-wrap:wrap;justify-content:flex-end;align-items:center;gap:16px}
    .wd-footer-social{display:flex;justify-content:center;align-items:center;flex:none;width:44px;height:44px;color:#e1d7ee;text-decoration:none;border-radius:50%;transition:color .2s ease,background-color .2s ease}
    .wd-footer-social svg{display:block;width:40px;height:40px}
    .wd-footer-social:hover,.wd-footer-social:focus-visible{color:#fff;background:rgba(203,182,255,.12)}
    .wd-footer-rights-brand:hover{color:#fff}
    a:focus-visible{outline:2px solid #e7dcff;outline-offset:5px}
    @media(max-width:991px){
      .wd-footer-root{padding:80px 40px 64px}
      .wd-footer-inner{gap:96px 40px}
      .wd-footer-title{font-size:32px}
      .wd-footer-rights{font-size:14px}
      .wd-footer-socials{gap:10px}
    }
    @media(max-width:600px){
      .wd-footer-root{padding:64px 20px 40px}
      .wd-footer-inner{grid-template-columns:minmax(0,1fr);gap:40px}
      .wd-footer-home{width:100%;max-width:400px}
      .wd-footer-description{font-size:17px;margin-top:24px}
      .wd-footer-contact{align-items:flex-start}
      .wd-footer-title{text-align:left;font-size:32px}
      .wd-footer-rights{font-size:13px;gap:8px 12px}
      .wd-footer-socials{justify-content:flex-start;gap:16px}
    }
    @media(prefers-reduced-motion:reduce){a{transition:none!important}}
  `;
  const ICONS = {
    instagram: '<rect x="11" y="11" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="20" cy="20" r="4.5" fill="none" stroke="currentColor" stroke-width="1.7"/><circle cx="25.6" cy="14.5" r="1.2" fill="currentColor"/>',
    linkedin: '<rect x="11" y="11" width="18" height="18" rx="1.5" fill="currentColor"/><circle cx="15" cy="15" r="1.3" fill="var(--wd-footer-icon-cutout,#301258)"/><path d="M15 18v7M19 25v-7m0 3c0-4 6-4 6 0v4" fill="none" stroke="var(--wd-footer-icon-cutout,#301258)" stroke-width="2.3"/>',
    facebook: '<path d="M22 30V21h3l.5-4H22v-2c0-1.2.5-2 2-2h2V9.5c-.8-.1-1.8-.2-3-.2-3.5 0-5.5 2-5.5 5.8V17H14v4h3.5v9Z" fill="currentColor"/>',
    whatsapp: '<path d="M11 29l1.5-5a9 9 0 1 1 3.5 3.5Z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M16 14.5c.5-.3.9.1 1.5 1.7.3.7 0 1-.6 1.6.8 1.9 2.2 3.2 4.1 4 .6-.7.9-1.1 1.6-.7l1.7.9c.6.3.6.8.4 1.3-.4 1-1.4 1.5-2.4 1.3-4.8-.9-8.7-4.7-9-8-.1-.9.4-1.7 1.2-2.1.6-.3 1-.2 1.5 0Z" fill="currentColor"/>',
    email: '<rect x="10" y="13" width="20" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m11 14 9 7 9-7" fill="none" stroke="currentColor" stroke-width="1.5"/>'
  };
  const LABELS = {instagram:'Instagram',linkedin:'LinkedIn',facebook:'Facebook',whatsapp:'WhatsApp',email:'E-mail'};
  const arrow = '<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.065 1.142L.5 12.706M1.968 .706h9.573c.53 0 .959.429.959.961v9.571" stroke="currentColor" stroke-width="1.412"/></svg>';
  function url(value, protocols = ['https:','http:','mailto:']) {
    if (!value?.trim()) return null;
    try { const u = new URL(value,document.baseURI); return protocols.includes(u.protocol) ? u.href : null; }
    catch { return null; }
  }
  class WDFooter extends HTMLElement {
    static get observedAttributes(){return ['logo','home','contact','instagram','linkedin','facebook','whatsapp','email'];}
    constructor(){super();this.attachShadow({mode:'open'});}
    connectedCallback(){this.render();}
    attributeChangedCallback(){if(this.isConnected)this.render();}
    render(){
      const values = {...CONFIG};
      for (const key of Object.keys(values)) if(this.hasAttribute(key)) values[key]=this.getAttribute(key);
      this.shadowRoot.innerHTML = `<style>${CSS}</style><footer class="wd-footer-root" aria-label="Rodapé Work Digital"><div class="wd-footer-inner"><div class="wd-footer-brand"><a class="wd-footer-home"><img class="wd-footer-logo" alt="Work Digital" width="4340" height="1340" decoding="async"></a><p class="wd-footer-description">Criação de sites e lojas virtuais de alta performance e focados em conversão.</p></div><div class="wd-footer-contact"><p class="wd-footer-title">Como podemos te ajudar?</p><a class="wd-footer-cta wd-cta"><span>ENTRE EM CONTATO</span>${arrow}</a></div><p class="wd-footer-rights"><a class="wd-footer-rights-brand">Work Digital © <span class="wd-footer-year"></span></a> <span class="wd-footer-divider" aria-hidden="true">|</span> <span>Todos os direitos reservados</span></p><nav class="wd-footer-socials" aria-label="Redes sociais e canais de contato"></nav></div></footer>`;
      const root=this.shadowRoot;
      const home=url(values.home,['https:','http:'])||CONFIG.home;
      root.querySelector('.wd-footer-home').href=home;
      root.querySelector('.wd-footer-rights-brand').href=home;
      root.querySelector('.wd-footer-logo').src=url(values.logo,['https:','http:'])||CONFIG.logo;
      root.querySelector('.wd-footer-cta').href=url(values.contact,['https:','http:'])||CONFIG.contact;
      root.querySelector('.wd-footer-year').textContent=new Date().getFullYear();
      for(const key of ['linkedin','instagram','facebook']){
        const icon=ICONS[key];
        if(key==='whatsapp'||key==='email')continue;
        const href=url(values[key]);if(!href)continue;
        const a=document.createElement('a');
        a.className='wd-footer-social';a.href=href;a.target='_blank';a.rel='noopener';
        a.setAttribute('aria-label',LABELS[key]);
        a.innerHTML=`<svg viewBox="0 0 40 40" fill="none" aria-hidden="true" focusable="false"><circle cx="20" cy="20" r="19.4" stroke="currentColor" stroke-width="1.14"/>${icon}</svg>`;
        root.querySelector('.wd-footer-socials').append(a);
      }
      if(!root.querySelector('.wd-footer-social'))root.querySelector('.wd-footer-socials').remove();
    }
  }
  if(!customElements.get('wd-footer'))customElements.define('wd-footer',WDFooter);
  // Fontes compartilhadas: uma única inclusão, caso a página não as carregue.
  if(!document.querySelector('link[href*="family=Space+Grotesk"],link[href*="family=Space%20Grotesk"],link[data-wd-footer-fonts]')){
    const link=document.createElement('link');link.rel='stylesheet';link.dataset.wdFooterFonts='';
    link.href='https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&family=Space+Grotesk:wght@400;500;600&display=swap';
    document.head.append(link);
  }
  if(!document.querySelector('script[src*="/whatsapp.js"]')){
    const widget=document.createElement('script');widget.src=new URL('whatsapp.js?v=20261003-r6',source).href;widget.defer=true;document.head.append(widget);
  }
  if(!document.querySelector('link[href*="/wd-revision.css"]')){
    const styles=document.createElement('link');styles.rel='stylesheet';styles.href=new URL('wd-revision.css?v=20261003-r6',source).href;document.head.append(styles);
  }
  if(!document.querySelector('link[href*="family=Nunito"]')){
    const font=document.createElement('link');font.rel='stylesheet';font.href='https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&display=swap';document.head.append(font);
  }
  function mount(){
    if(script?.hasAttribute('data-manual')||document.querySelector('wd-footer'))return;
    const footer=document.createElement('wd-footer');footer.id='wd-footer';document.body.append(footer);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',mount,{once:true});else mount();
})();
```
## Arquivos completos alterados

Substitua os arquivos pelos correspondentes do ZIP. O index.html já está sem as regras antigas conflitantes.

### public/wd-revision.css

```css
/* GERAL */
:root{--wd-uptitle-gradient:linear-gradient(90deg,#FFFFFF 0%,#EDE4FF 45%,#F7C9EC 100%);--wd-description-font:"Nunito",system-ui,sans-serif;--wd-article-hover:linear-gradient(0deg,#301258,#4b247e)}
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
@media(min-width:992px){}
@media(min-width:769px) and (max-width:991px){}
@media(max-width:768px){
 #wd-transformacao{padding-top:24px}
}
@media(max-width:600px){}
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
}
@media(max-width:768px){
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
#wd-explore .wd-explore-photo{position:relative;box-sizing:border-box;width:calc(var(--wd-media-width,520px) + 40px);height:var(--wd-panel-height,auto);padding:20px;border:0;border-radius:12px;aspect-ratio:auto;background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%);overflow:hidden}
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
@media(min-width:769px) and (max-width:991px){}
@media(max-width:768px){}
@media(prefers-reduced-motion:reduce){#wd-explore .wd-explore-media{transition:none}}

/* GERAL — uma tipografia para CTAs e uma escala para títulos principais. */
:root{--wd-layout-max:1440px;--wd-layout-gutter:3vw;--wd-cta-weight:500;--wd-cta-letter-spacing:.1em}
.wd-cta,button{font-family:"Space Grotesk",system-ui,sans-serif;font-weight:var(--wd-cta-weight);letter-spacing:var(--wd-cta-letter-spacing)}
.wd-section-title{font-size:clamp(36px,4.34vw,64px);font-weight:500;line-height:1.05;letter-spacing:-.041em}
/* MENU — mesma largura e margens do retângulo de Soluções Work. */
.site-header{padding-inline:var(--wd-layout-gutter)}
.site-nav,#wd-explore .wd-explore-layout{width:100%;max-width:var(--wd-layout-max)}
#wd-explore{padding-inline:var(--wd-layout-gutter)}
.wd-language .nav-trigger{width:auto;padding-inline:10px;white-space:nowrap}
@media(max-width:991px){:root{--wd-layout-gutter:24px}}
@media(max-width:479px){:root{--wd-layout-gutter:16px}}
/* HEADER — 35% maior no desktop; limite próprio no celular. */
.intro .intro-title{font-size:clamp(72px,6.1425vw,130px)}
@media(max-width:980px){.intro .intro-title{font-size:clamp(42px,10.6vw,68px)}}
/* SOLUÇÕES WORK — transparência igual à esquerda, sem borda. */
#wd-explore .wd-explore-body .wd-explore-photo{background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%);border:0}
/* TRANSFORMAÇÃO DIGITAL — substituição integral pelo CSS enviado. */
.wd-tr-card{position:relative;overflow:hidden;isolation:isolate;width:calc(100% - 64px);max-width:1360px;height:600px;margin:0 auto;border-radius:16px;border:0;background:radial-gradient(60% 90% at 80% 50%,rgba(222,210,255,.60) 0%,rgba(190,170,255,.28) 38%,rgba(190,170,255,0) 72%),radial-gradient(55% 60% at 30% 112%,rgba(232,222,255,.42) 0%,rgba(232,222,255,0) 72%),radial-gradient(70% 90% at 0% 0%,rgba(18,8,44,.55) 0%,rgba(18,8,44,0) 70%),linear-gradient(100deg,#1f0e46 0%,#2d1569 30%,#4a2fa3 58%,#8f78e6 82%,#c9bbff 100%);box-shadow:0 0 160px 20px rgba(124,92,255,.25)}
.wd-tr-glow{position:absolute;z-index:0;pointer-events:none;top:50%;left:54%;height:260%;aspect-ratio:1;transform:translate(-21%,-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(250,247,255,1) 52%,rgba(232,222,255,.85) 58%,rgba(205,188,255,.5) 68%,rgba(170,145,255,.18) 82%,rgba(170,145,255,0) 100%)}
.wd-tr-globe{position:absolute;z-index:1;pointer-events:none;top:50%;left:54%;height:150%;aspect-ratio:1;transform:translateY(-50%);border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,0) 80%,rgba(255,255,255,.55) 93%,rgba(250,247,255,1) 100%),radial-gradient(circle at 6% 50%,rgba(255,255,255,1) 0%,rgba(255,255,255,0) 24%),radial-gradient(circle at 62% 82%,rgba(252,250,255,.95) 0%,rgba(252,250,255,0) 42%),radial-gradient(circle at 48% 22%,rgba(196,176,255,.7) 0%,rgba(196,176,255,0) 55%),radial-gradient(circle at 55% 50%,#ebe4ff 0%,#ddd0ff 55%,#cfbdff 100%)}
.wd-tr-dots{position:absolute;inset:0;border-radius:50%;-webkit-mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%);mask-image:radial-gradient(ellipse 75% 85% at 66% 50%,#000 50%,transparent 82%)}
.wd-tr-dots>svg{display:block;position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.wd-tr-content{position:relative;z-index:2;padding:0 80px;height:100%;display:flex;flex-direction:column;justify-content:center;color:#fff;max-width:560px}
.wd-tr-content .wd-transformacao-content{width:100%;max-width:none;padding:0}
.wd-tr-content .wd-transformacao-cta{margin-left:0}
/* Ajustes de encaixe e leitura mantêm o responsivo atual. */
.wd-tr-content .wd-transformacao-title{white-space:normal;text-wrap:balance}
@media(min-width:769px) and (max-width:991px){
 .wd-tr-card{width:calc(100% - 32px);height:auto;min-height:0;padding-bottom:420px}
 .wd-tr-content{padding:48px 32px;height:auto;max-width:none}
 .wd-tr-globe{height:420px;top:auto;bottom:0;left:calc(50% - 110px);transform:none}
 .wd-tr-glow{height:728px;top:auto;bottom:-154px;left:calc(50% - 110px);transform:translateX(-21%)}
}
@media(max-width:768px){
 .wd-tr-card{width:calc(100% - 32px);height:auto;min-height:600px}
 .wd-tr-globe{height:90%;left:40%}
 .wd-tr-glow{height:156%;left:40%}
 .wd-tr-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;background:radial-gradient(ellipse 140% 110% at 0% 8%,rgba(31,14,70,.96) 0%,rgba(31,14,70,.88) 45%,rgba(31,14,70,.75) 66%,rgba(31,14,70,0) 100%)}
 .wd-tr-content{padding:48px 32px;height:auto;min-height:600px;max-width:none}
}
@media(max-width:600px){.wd-tr-content{padding:40px 24px}}
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
 function resize(){if(stacked.matches)return;const h=list.getBoundingClientRect().height;const inner=Math.max(0,h-40);body.style.setProperty('--wd-panel-height',h+'px');body.style.setProperty('--wd-media-height',inner+'px');body.style.setProperty('--wd-media-width',(inner*9/11)+'px');}
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
### public/whatsapp.js

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
 const CSS=`:host{position:fixed;bottom:20px;right:20px;z-index:100;display:flex;flex-direction:column;align-items:flex-end;font-family:"Nunito",system-ui,sans-serif;color:#e4e4e7}*{box-sizing:border-box}button,a{font:inherit}button{cursor:pointer}button:focus-visible,a:focus-visible{outline:2px solid #fff;outline-offset:4px}.wd-whatsapp-toggle{position:relative;display:flex;align-items:center;justify-content:center;width:64px;height:64px;padding:16px;background:#059669;color:white;border:2px solid #34d39980;border-radius:50%;box-shadow:0 25px 50px -12px #05966966;transition:transform .3s,background .3s}.wd-whatsapp-toggle:hover{background:#10b981;transform:scale(1.05)}.wd-whatsapp-toggle:active{transform:scale(.95)}.wd-whatsapp-toggle svg{position:relative;width:28px;height:28px;z-index:1}.wd-whatsapp-pulse{position:absolute;inset:-4px;border-radius:50%;background:#10b981;opacity:.4;animation:wdWhatsappPing 1s cubic-bezier(0,0,.2,1) infinite;pointer-events:none}.wd-whatsapp-badge{position:absolute;right:-4px;top:-4px;padding:2px 8px;font:800 10px/1.5 system-ui;color:white;background:#f97316;border:0;outline:0;box-shadow:none;border-radius:99px}.wd-whatsapp-panel{width:384px;max-width:calc(100vw - 40px);margin-bottom:12px;border-radius:24px;border:1px solid #10b98166;background:#09090b;box-shadow:0 25px 50px -12px #0008;overflow:hidden;animation:wdWhatsappEnter .45s ease-out}.wd-whatsapp-panel[hidden]{display:none}.wd-whatsapp-heading{display:flex;align-items:center;gap:12px;padding:16px;background:linear-gradient(90deg,#059669,#0f766e);color:white}.wd-whatsapp-avatar{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:#fff3;font-weight:700;flex:none}.wd-whatsapp-avatar svg{width:24px;height:24px}.wd-whatsapp-title{margin:0;font-family:"Space Grotesk",system-ui,sans-serif;font-size:14px;font-weight:700;line-height:1.3}.wd-whatsapp-status{font-size:11px;color:#d1fae5}.wd-whatsapp-close{margin-left:auto;border:0;border-radius:8px;background:none;color:white;width:28px;height:28px;font-size:24px}.wd-whatsapp-close:hover{background:#fff3}.wd-whatsapp-body{padding:16px;background:#18181b}.wd-whatsapp-greeting{padding:14px;border:1px solid #27272a;border-radius:16px;background:#09090b;font-size:12px;line-height:1.625;margin:0 0 12px}.wd-whatsapp-topics{font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#a1a1aa;margin:0 0 12px}.wd-whatsapp-actions{display:grid;gap:8px}.wd-whatsapp-action{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px;border:1px solid #27272a;border-radius:12px;background:#09090b;color:#d4d4d8;text-decoration:none;font-size:12px;transition:background .3s,border-color .3s}.wd-whatsapp-action:hover{border-color:#10b981;background:#022c2222;color:#fff}.wd-whatsapp-footer{padding:12px;border-top:1px solid #27272a}.wd-whatsapp-open{width:100%;padding:12px;display:flex;gap:8px;align-items:center;justify-content:center;border:0;border-radius:12px;background:#059669;color:#fff;font-size:12px;font-weight:700;text-decoration:none}.wd-whatsapp-open svg{width:20px;height:20px}.wd-whatsapp-notice{font-size:11px;line-height:1.5;margin:8px 0 0;color:#d4d4d8}.wd-whatsapp-action[aria-disabled=true],.wd-whatsapp-open[aria-disabled=true]{opacity:.65;cursor:default}button,.wd-whatsapp-action,.wd-whatsapp-open{font-family:"Space Grotesk",system-ui,sans-serif;font-weight:var(--wd-cta-weight,500);letter-spacing:var(--wd-cta-letter-spacing,.1em)}@keyframes wdWhatsappPing{75%,100%{transform:scale(2);opacity:0}}@keyframes wdWhatsappEnter{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}@media(max-width:639px){.wd-whatsapp-panel{width:320px}}@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}}`;
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
## Alterações — uma linha por item

- **GERAL 1:** CTAs em Space Grotesk, peso 500 e letter-spacing .1em, incluindo os componentes globais.
- **GERAL 2:** Cinco títulos principais padronizados pela classe .wd-section-title.
- **MENU 1:** Mesma largura máxima e mesmas margens laterais do retângulo de Soluções Work.
- **MENU 2:** Seletor compacto com globo, PT, seta e padding de 10px.
- **MENU 3:** Work alterado para Works.
- **HEADER 1:** Degradê branco → lilás → rosa suave aplicado ao h1 e a todos os uptitles.
- **HEADER 2:** H1 aumentado em 35% no desktop, com clamp próprio para celular.
- **SOLUÇÕES WORK 1:** Moldura da imagem com o mesmo fundo/transparência do painel esquerdo e sem borda.
- **TRANSFORMAÇÃO DIGITAL:** CSS antigo substituído pelos gradientes enviados; mapa preservado, sem padrão de teste.
- **RODAPÉ 1:** Redes ordenadas como LinkedIn / Instagram / Facebook.
