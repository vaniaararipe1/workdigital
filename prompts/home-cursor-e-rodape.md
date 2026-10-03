# Prompt: Cursor personalizado e texto do rodapé na home

As páginas internas (Cases, Soluções, Case interna, Blog e Post) já usam este cursor e este texto
de rodapé. Este prompt aplica os mesmos dois ajustes na home.

## PROMPT (copie daqui para baixo)

Faça **só** os dois ajustes abaixo na home. Não altere mais nada.

### 1. Cursor personalizado (igual ao das páginas internas)
O cursor do navegador vira uma **bolinha clara de 12px** que segue o mouse com um leve atraso.
Sobre os cards de cases e de artigos, ela cresce para um **círculo roxo de 96px** com uma palavra
dentro. O cursor fica **acima de tudo**, inclusive do menu, do painel de contato e do WhatsApp.

HTML (antes do `</body>`):
```html
<div class="wd-cursor" id="wdCursor" aria-hidden="true" hidden><b></b></div>
```

CSS:
```css
.wd-cursor{position:fixed;left:0;top:0;z-index:2147483000;pointer-events:none;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#F2EEF8;mix-blend-mode:difference;display:grid;place-items:center;
  transition:width .4s cubic-bezier(.22,1,.36,1),height .4s cubic-bezier(.22,1,.36,1),margin .4s cubic-bezier(.22,1,.36,1),background .3s}
.wd-cursor b{font:500 11px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#fff;opacity:0;transition:opacity .2s;white-space:nowrap}
.wd-cursor.link{width:40px;height:40px;margin:-20px 0 0 -20px}
.wd-cursor.big{width:96px;height:96px;margin:-48px 0 0 -48px;background:#6025E1;mix-blend-mode:normal}
.wd-cursor.big b{opacity:1}
@media (hover:hover) and (pointer:fine){.has-wd-cursor,.has-wd-cursor a,.has-wd-cursor button{cursor:none}}
```

JS:
```js
(function(){
  if(!matchMedia('(hover: hover) and (pointer: fine)').matches||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c=document.getElementById('wdCursor'), lb=c.querySelector('b'); c.hidden=false; document.body.classList.add('has-wd-cursor');
  const LABELS=[['.wd-works-card','Ver case'],['.wd-blog-link','Ler']];
  let mx=innerWidth/2,my=innerHeight/2,x=mx,y=my;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;},{passive:true});
  document.addEventListener('mouseover',e=>{
    let label=null; for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }
    c.classList.toggle('big',!!label); if(label) lb.textContent=label;
    c.classList.toggle('link',!label && !!e.target.closest('a,button,input,textarea'));
  });
  document.addEventListener('mouseleave',()=>c.classList.remove('big','link'));
  (function tick(){x+=(mx-x)*.18;y+=(my-y)*.18;c.style.transform=`translate(${x}px,${y}px)`;requestAnimationFrame(tick);})();
})();
```
- **Tamanhos:**
  - normal: bolinha de 12px;
  - sobre links e botões: círculo de 40px;
  - sobre os cards de cases (`.wd-works-card`): círculo roxo de 96px escrito **VER CASE**;
  - sobre os artigos do blog (`.wd-blog-link`): círculo roxo de 96px escrito **LER**.
- **Celular, tablet e `prefers-reduced-motion`:** o cursor personalizado não aparece e fica o
  cursor normal.
- Nos campos do painel de contato, o cursor de texto (a barra de digitação) continua aparecendo
  normalmente.

### 2. Texto do rodapé (`footer.js`)
- Troque **"Como podemos te ajudar?"** por **"Tem um projeto em mente?"**.
- Troque **"ENTRE EM CONTATO"** por **"FALE COM A GENTE"**.
- O botão continua abrindo o painel de contato do menu. Nada mais muda no rodapé.

Ao final, liste em uma linha por item o que foi alterado.
