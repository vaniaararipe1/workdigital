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
    .wd-footer-cta{display:flex;align-items:center;justify-content:center;gap:20px;min-height:54px;max-width:100%;padding:18px 20px;border-radius:6px;color:#fff;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0;text-decoration:none;font-size:14px;font-weight:400;line-height:1;letter-spacing:.1em;transition:background-position 600ms ease,color 200ms ease}
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
      this.shadowRoot.innerHTML = `<style>${CSS}</style><footer class="wd-footer-root" aria-label="Rodapé Work Digital"><div class="wd-footer-inner"><div class="wd-footer-brand"><a class="wd-footer-home"><img class="wd-footer-logo" alt="Work Digital" width="4340" height="1340" decoding="async"></a><p class="wd-footer-description">Criação de sites e lojas virtuais de alta performance e focados em conversão.</p></div><div class="wd-footer-contact"><p class="wd-footer-title">Como podemos te ajudar?</p><a class="wd-footer-cta"><span>ENTRE EM CONTATO</span>${arrow}</a></div><p class="wd-footer-rights"><a class="wd-footer-rights-brand">Work Digital © <span class="wd-footer-year"></span></a><span class="wd-footer-divider" aria-hidden="true">|</span><span>Todos os direitos reservados</span></p><nav class="wd-footer-socials" aria-label="Redes sociais e canais de contato"></nav></div></footer>`;
      const root=this.shadowRoot;
      const home=url(values.home,['https:','http:'])||CONFIG.home;
      root.querySelector('.wd-footer-home').href=home;
      root.querySelector('.wd-footer-rights-brand').href=home;
      root.querySelector('.wd-footer-logo').src=url(values.logo,['https:','http:'])||CONFIG.logo;
      root.querySelector('.wd-footer-cta').href=url(values.contact,['https:','http:'])||CONFIG.contact;
      root.querySelector('.wd-footer-year').textContent=new Date().getFullYear();
      for(const [key,icon] of Object.entries(ICONS)){
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
    link.href='https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&family=Space+Grotesk:wght@400;500&display=swap';
    document.head.append(link);
  }
  if(!document.querySelector('script[src$="/whatsapp.js"]')){
    const widget=document.createElement('script');widget.src=new URL('whatsapp.js',source).href;widget.defer=true;document.head.append(widget);
  }
  if(!document.querySelector('link[href$="/wd-revision.css"]')){
    const styles=document.createElement('link');styles.rel='stylesheet';styles.href=new URL('wd-revision.css',source).href;document.head.append(styles);
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
