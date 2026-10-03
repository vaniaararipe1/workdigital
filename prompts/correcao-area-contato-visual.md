# Prompt: Correção visual da área de contato (igual ao menu da home)

Referência visual: https://workdigital-hero-preview.onrender.com/ (menu, dropdowns e CTAs).
Os valores abaixo foram lidos do CSS publicado da home. O efeito de "mesclar" com o menu foi
testado antes em uma prévia.

## PROMPT (copie daqui para baixo)

Corrija a **área de contato** que abre ao clicar em **SOLICITAR PROPOSTA** (arquivos `contact.css`
e `contact.js`). Hoje ela é um retângulo claro (`#F5F3FA`) separado do menu, com outro estilo. Ela
precisa ter **exatamente o mesmo visual do menu da home**: o mesmo vidro escuro desfocado, as mesmas
fontes, as mesmas cores e o mesmo CTA. Ao abrir, o painel deve **sair de dentro do menu, como se o
retângulo do menu se esticasse para baixo**, formando uma peça só. Mantenha toda a lógica que já
funciona (validação, envio, mensagens de sucesso e erro, Esc, clique fora, foco e acessibilidade).
Altere só o visual e a animação.

### 1. Visual do menu que o painel deve copiar (valores atuais da home)
- **Vidro do menu** (`.site-nav::before`): `background: rgba(18,19,22,.58)`,
  `backdrop-filter: blur(22px) saturate(155%)`, borda `1px solid rgba(255,255,255,.10)`,
  sombra `0 18px 55px rgba(0,0,0,.18)`, raio `32px` (`--wd-panel-radius`), altura 72px.
- **Textos:** Space Grotesk para títulos, links e botões. Nunito para textos de apoio. Use a cor
  `#F7F6FB` para os textos e `#A9B0B0` para os secundários (a mesma do `small` do dropdown).
- **Uptitle:** o degradê dos uptitles do site (`#B79BFF → #E58BFF → #FF8FCB`) com a classe
  `.wd-uptitle`.
- **CTA:** a mesma classe do botão do menu (`.nav-cta.wd-cta`):
  - pílula de 46px de altura;
  - degradê `#CBFFFC → #EDFFFE → #FFFDFA → #FAD1FF` com `background-size: 180%`, que desliza no hover;
  - texto `#222`, 14px, peso 500, `letter-spacing: .1em`, maiúsculas;
  - seta ↗ que anda `translate(3px,-3px)` no hover;
  - o mesmo efeito de saída do mouse já aplicado aos CTAs.

### 2. Efeito "mesclado com o menu" (o mais importante)
O painel **não é uma caixa separada abaixo do menu**. O menu e o painel viram **um único formato
de vidro**: o retângulo do menu ganha uma "aba" que desce do lado direito, embaixo do CTA. No
encontro entre o menu e o painel há uma **curva côncava suave** (raio 20px), como uma gota saindo
do menu. Não pode haver vão, linha dupla nem diferença de cor entre o menu e o painel.

**Como fazer:** um único elemento de vidro recortado com `clip-path: path()` e um SVG com o mesmo
caminho para a borda e a sombra. Isso é necessário porque `backdrop-filter` não funciona bem com
duas caixas sobrepostas (o desfoque dobra e escurece).

HTML (dentro do `.site-header`, **antes** do `<nav class="site-nav">`):
```html
<div class="wd-contact-stage" aria-hidden="true">
  <svg class="wd-contact-lines"><defs><filter id="wdContactShadow" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="27"/></filter></defs><path class="wd-contact-shadow"/></svg>
  <div class="wd-contact-glass"></div>
  <svg class="wd-contact-lines"><path class="wd-contact-stroke"/></svg>
</div>
```

CSS:
```css
.site-nav{z-index:2;transition:border-color .2s,box-shadow .2s}
.site-nav::before{transition:opacity .15s}
.site-nav.wd-contact-open{border-color:transparent;box-shadow:none}
.site-nav.wd-contact-open::before{opacity:0} /* o vidro passa a ser desenhado pelo stage */
.wd-contact-stage{position:fixed;inset:0;z-index:1;pointer-events:none;visibility:hidden}
.wd-contact-stage.is-on{visibility:visible}
.wd-contact-glass{position:absolute;inset:0;background:rgba(18,19,22,.58);
  backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%)}
.wd-contact-lines{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.wd-contact-shadow{fill:rgba(0,0,0,.18);filter:url(#wdContactShadow);transform:translateY(18px)}
.wd-contact-stroke{fill:none;stroke:rgba(255,255,255,.10);stroke-width:1}
```

JS (desenha o formato a cada quadro; `W` = largura da aba e `H` = altura da aba abaixo do menu):
```js
const R=32, RI=24, FIL=20;            // raio do menu, raio interno, curva da junção
function shapePath(n,W,H){            // n = nav.getBoundingClientRect()
  const x0=n.left,y0=n.top,x1=n.right,y1=n.bottom;
  const rb=R+(RI-R)*Math.min(1,H/60), rl=Math.min(RI,H*.4), f=Math.min(FIL,H*.5), px=x1-W, yb=y1+H;
  return `M${x0+R},${y0} H${x1-R} A${R},${R} 0 0 1 ${x1},${y0+R} V${yb-rb} A${rb},${rb} 0 0 1 ${x1-rb},${yb} `+
         `H${px+rl} A${rl},${rl} 0 0 1 ${px},${yb-rl} V${y1+f} A${f},${f} 0 0 0 ${px-f},${y1} `+
         `H${x0+R} A${R},${R} 0 0 1 ${x0},${y1-R} V${y0+R} A${R},${R} 0 0 1 ${x0+R},${y0} Z`;
}
const s={W:0,H:0};
function draw(){
  const n=nav.getBoundingClientRect(), d=shapePath(n,s.W,s.H);
  glass.style.clipPath=`path("${d}")`;
  stage.querySelectorAll('path').forEach(p=>p.setAttribute('d',d));
  // o conteúdo do formulário acompanha a aba
  Object.assign(panel.style,{left:(n.right-PANEL_W)+'px',top:n.bottom+'px',width:PANEL_W+'px',height:s.H+'px'});
}
```
- Com `H = 0`, o caminho é idêntico ao menu fechado (cantos de 32px), então a troca entre o
  `::before` do menu e o vidro do stage não aparece.
- Redesenhe no `resize` enquanto estiver aberto.

### 3. Animação de abertura (GSAP, já carregado pelo `contact.js`)
`PANEL_W = 477`. A altura final é `HF = Math.min(600, innerHeight - nav.bottom - 24)`.
```js
const n=nav.getBoundingClientRect(), c=ctaMenu.getBoundingClientRect();
s.W=n.right-c.left+14; s.H=0;                  // a aba nasce do tamanho do CTA
stage.classList.add('is-on'); nav.classList.add('wd-contact-open'); draw();
tl=gsap.timeline({onReverseComplete(){ stage.classList.remove('is-on'); nav.classList.remove('wd-contact-open'); panel.classList.remove('is-on'); }})
  .to(s,{H:56,duration:.4,ease:'power3.out',onUpdate:draw})               // 1. a "gota" desce do CTA
  .to(s,{W:PANEL_W,duration:.5,ease:'power3.inOut',onUpdate:draw})        // 2. alarga para a esquerda
  .to(s,{H:HF,duration:.6,ease:'power3.inOut',onUpdate:draw},'-=.15')     // 3. desce até a altura final
  .add(()=>panel.classList.add('is-on'),'-=.4')
  .to(panel.querySelectorAll('.wd-contact-anim'),{opacity:1,y:0,stagger:.07,duration:.5,ease:'power2.out'},'-=.35');
```
- **Fechar:** `tl.timeScale(1.4).reverse()`. O formato volta para dentro do menu e, ao terminar, o
  menu volta a usar o próprio `::before`.
- **Botão do menu:** enquanto o painel estiver aberto, o CTA do menu continua no lugar e serve
  para fechar. O texto troca de **SOLICITAR PROPOSTA ↗** para **FECHAR ✕**, com um fade e um
  deslize vertical curto de .3s, mantendo o mesmo degradê. Atualize o `aria-expanded`.
- Remova o botão antigo de hambúrguer e o botão roxo (`.wd-contact-buttons`, `.wd-contact-menu` e
  `.wd-contact-cta`), porque quem abre e fecha agora é o próprio CTA do menu.
- Ao abrir, feche o dropdown de idiomas e o de Soluções, se estiverem abertos.
- Com `prefers-reduced-motion`, mostre o formato final direto e use só um fade de .2s no conteúdo.

### 4. Conteúdo do painel (`.wd-contact`)
- O painel fica **acima** do header: `position: fixed; z-index` maior que o do `.site-header`.
  Se ficar abaixo, o vidro desfoca o próprio formulário.
- Use também `box-sizing: border-box; overflow: hidden; padding: 36px 32px 28px` e fundo
  **transparente** (quem desenha o vidro é o stage).
- Cada bloco animado recebe a classe `.wd-contact-anim` e começa com `opacity: 0` e
  `transform: translateY(10px)`.
- **Uptitle** "CONTATO": `.wd-uptitle` com o degradê do site, 12px, peso 600,
  `letter-spacing: .16em`, 12px de espaço embaixo.
- **Título** "Vamos trabalhar juntos.": Space Grotesk 30px, peso 500, `line-height: 1.05`,
  `letter-spacing: -.03em`, cor `#F7F6FB`, 30px de espaço embaixo.
- **Campos:**
  - sem caixa, só a linha embaixo: `border-bottom: 1px solid rgba(255,255,255,.16)`;
  - fundo transparente, `padding: 0 0 12px`, 26px entre os campos;
  - texto `#F7F6FB` em Nunito 20px, peso 300;
  - placeholder `#A9B0B0` em Space Grotesk.
- **Linha de destaque no foco:** cada campo tem um `::after` de 1px com o degradê
  `#B79BFF → #E58BFF → #FF8FCB`. Ele começa com `scaleX(0)` e cresce da esquerda para
  `scaleX(1)` em .5s com `cubic-bezier(.22,1,.36,1)`. No hover, a linha cinza fica
  `rgba(255,255,255,.4)`.
- **Placeholders curtos para não cortar:**
  - Nome completo
  - E-mail
  - Empresa ou site
  - Qual é a sua ideia? (use um `textarea` de 1 linha que cresce até 3 linhas)
  - Como você conheceu a Work?
- **Erro:** a linha e o placeholder ficam `#FF8FA3`, e a mensagem aparece abaixo em Nunito 12px
  `#FF8FA3`.
- **Linha de baixo:**
  - à esquerda, o texto de privacidade em Nunito 12px `#A9B0B0` (`max-width: 210px`), com o link
    sublinhado em `#F7F6FB`;
  - à direita, o botão **ENVIAR ↗**, que é **o mesmo CTA do menu** (`.nav-cta.wd-cta`, 46px,
    pílula com o degradê).
- **Enviando:** o botão mantém o tamanho e troca o texto por um ícone de carregamento `#222`.
- **Sucesso e erro:**
  - título em Space Grotesk 28px, peso 500, `#F7F6FB`;
  - texto em Nunito 16px `#A9B0B0`;
  - botão **FECHAR** com o mesmo CTA de degradê.
- **Foco visível** de teclado: `outline: 2px solid #bda4ff`, como nos dropdowns.

### 5. Fundo da página
- Ao abrir, coloque uma camada fixa atrás do header, por cima da página:
  `background: rgba(10,10,14,.35); backdrop-filter: blur(6px)`, com fade de .4s.
- Clicar nela fecha o painel. Ela fica abaixo do header, para não desfocar o menu.

### 6. Celular (até 768px)
- O CTA fica dentro do menu do celular. Ao tocar, feche o menu do celular e abra o contato.
- O formato é o retângulo do menu crescendo **para baixo, na largura toda do menu**, sem a aba
  lateral. Use este caminho, com `R = 17`, o raio do menu no celular:
```js
function shapePathMobile(n,H){
  const x0=n.left,y0=n.top,x1=n.right,y1=n.bottom, r=R+(RI-R)*Math.min(1,H/60), yb=y1+H;
  return `M${x0+R},${y0} H${x1-R} A${R},${R} 0 0 1 ${x1},${y0+R} V${yb-r} A${r},${r} 0 0 1 ${x1-r},${yb} `+
         `H${x0+r} A${r},${r} 0 0 1 ${x0},${yb-r} V${y0+R} A${R},${R} 0 0 1 ${x0+R},${y0} Z`;
}
```
- A animação no celular é uma só: `H` de 0 até `innerHeight - nav.bottom - 12`, em .6s com
  `power3.inOut`. Depois o conteúdo aparece em sequência.
- O painel rola por dentro se não couber.
- No celular: título 24px, campos 16px, 22px entre os campos.
- O botão de fechar é o próprio botão do menu do celular, que vira **X**.

Ao final, liste em uma linha por item o que foi alterado em `contact.css` e `contact.js`.
