# Prompt: Área de contato no menu (referência: Otherlife)

Referência: https://www.otherlife.xyz/. Clique em "CONTACT US", no canto superior direito.
Análise feita no código do site: a animação usa GSAP, e os valores abaixo são os da referência.

## PROMPT (copie daqui para baixo)

Crie a **área de contato** do site da Work Digital igual à do site https://www.otherlife.xyz/.
Na referência, o botão de contato do menu **se expande e vira o formulário**: a caixa do botão
cresce até virar um painel com o formulário dentro, sem abrir outra página nem um modal separado.
Use as fontes da Work: Space Grotesk nos títulos e botões, Nunito nos textos. Use também as cores
da Work: #7C5CFF, #C4A8FF e #FF8FCB.

### 1. Estado fechado (no cabeçalho, à direita)
- Uma caixa de **207 × 60 px**, com fundo claro (`#F5F3FA`), `border-radius: 10px`,
  `overflow: hidden` e `padding: 3px`. Ela fica fixa no topo, a 50px do topo e 50px da direita.
- Dentro da caixa há 2 botões lado a lado:
  - **Esquerda (35% da largura):** ícone de menu com 3 linhas de 20 × 2 px, com 4px de espaço entre
    elas, na cor escura `#17131F`.
  - **Direita (65% da largura):** o botão **ENTRE EM CONTATO**, que ocupa toda a altura.
    - Fundo `#7C5CFF`, texto branco, 12px, maiúsculas, Space Grotesk, `border-radius: 8px`.
    - No hover, o fundo muda para `#17131F` com `transition: background-color .3s`.
- Esse conjunto substitui o botão de CTA atual do menu. O seletor de idiomas continua ao lado.

### 2. Abertura (ao clicar em ENTRE EM CONTATO)
Use **GSAP** (`https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js`) com uma timeline. A sequência
é exatamente esta, e cada passo dura 0,5s (padrão do GSAP):
1. A caixa cresce **na largura** até **477px**. Ela cresce para a esquerda, porque está presa à
   direita.
2. Ao mesmo tempo, os 2 botões deslizam **135px para a direita** (`right: -135px`). O botão
   ENTRE EM CONTATO sai de vista e fica só o ícone de menu no canto superior direito. Esse ícone
   passa a servir para **fechar**: as 3 linhas viram um **X**.
3. Depois, a caixa cresce **na altura** até **671px**, e a faixa dos botões mantém 60px de altura.
4. Junto com a altura, aparece o título **"Vamos trabalhar juntos."**, com `opacity` de 0 a 1.
5. Os campos aparecem **um por um**, com `opacity` de 0 a 1 e `stagger: 0.18`. Eles começam 1,5s
   antes do fim da etapa anterior (`"-=1.5"`), então aparecem enquanto a caixa ainda está crescendo.
6. Por último aparece a linha de baixo, com o aviso de privacidade e o botão Enviar.

Código de referência da timeline (ajuste os seletores aos seus nomes de classe):
```js
function abrirContato(){
  const box=document.querySelector('.wd-contact'), bts=document.querySelector('.wd-contact-buttons'),
        cta=document.querySelector('.wd-contact-cta'), title=document.querySelector('.wd-contact-title'),
        fields=document.querySelectorAll('.wd-contact-form .wd-field'), foot=document.querySelector('.wd-contact-foot');
  gsap.set([fields,foot],{opacity:0});
  return gsap.timeline()
    .to(box,{width:477})
    .to([bts,cta],{right:-135},'<')
    .to(box,{height:671})
    .to(bts,{height:60},'<')
    .to(title,{opacity:1},'<')
    .to(fields,{opacity:1,stagger:.18},'-=1.5')
    .to(foot,{opacity:1});
}
function fecharContato(){
  return gsap.timeline()
    .to('.wd-contact',{height:60})
    .to('.wd-contact-title',{opacity:0},'<')
    .to('.wd-contact',{width:207})
    .to(['.wd-contact-buttons','.wd-contact-cta'],{right:0},'<');
}
```
- O **fechamento** é a abertura ao contrário: primeiro a altura volta para 60px e o título some,
  depois a largura volta para 207px e os botões voltam para o lugar.
- Feche ao clicar no X, ao apertar **Esc** e ao clicar fora da caixa.

### 3. Painel aberto (conteúdo)
- **Título** "Vamos trabalhar juntos.":
  - posição absoluta, a 20px do topo e 25px da esquerda (alinhado com os botões no topo);
  - Space Grotesk 24px, peso 400, `line-height: 105%`, cor `#17131F`;
  - começa com `opacity: 0`.
- **Formulário:** começa 100px abaixo do topo, com 25px de margem nas laterais. Não há caixas nos
  campos, só uma **linha embaixo**:
  - `background: transparent; border: 0; border-bottom: 1px solid #BDBDBD;`
  - `padding-bottom: 14px; margin-bottom: 40px; font: 300 24px/105% "Nunito";`
  - texto em `#17131F`;
  - placeholder em cinza (`#9A94A8`), na fonte Space Grotesk;
  - no **hover** e no **foco**, a linha fica `#3C3C3C` e o placeholder escurece para `#3C3C3C`;
  - sem `outline` no foco.
- **Campos** (cada um com um `<label class="sr-only">` para acessibilidade):
  1. Nome completo
  2. E-mail (`type="email"`)
  3. Empresa ou site
  4. Qual é a sua ideia? Como podemos ajudar?
  5. Como você conheceu a Work?
- **Linha de baixo:** `display: flex; justify-content: space-between; align-items: center`.
  - À esquerda, o texto pequeno (12px, peso 300, `#3C3C3C`, `max-width: 200px`): "Ao enviar, você
    concorda que seus dados serão tratados de acordo com a nossa **Política de Privacidade**". O link
    fica sublinhado.
  - À direita, o botão **Enviar**: 125 × 55 px, borda de 1px `#17131F`, fundo transparente, texto
    `#17131F`, `border-radius: 10px`. No hover, o fundo fica `#7C5CFF` e o texto fica branco, com
    `transition: all .3s`.

### 4. Envio
- **Validação:** se um campo obrigatório (nome e e-mail) estiver vazio ou errado, a linha e o
  placeholder ficam vermelhos (`#E5484D`).
- **Enviando:** troque o texto "Enviar" por um ícone de carregamento girando (SVG com
  `animateTransform` de rotação de 0,75s).
- **Sucesso:** o formulário some com fade e aparece no centro do painel, também com fade:
  - título "Obrigado pelo contato!": Space Grotesk 32px, peso 500, `letter-spacing: -0.96px`,
    `#3C3C3C`, 32px de margem embaixo;
  - texto (18px): "Recebemos sua mensagem e nossa equipe já está analisando. Em breve entraremos em
    contato.";
  - botão escuro **Fechar**, que fecha o painel.
- **Erro:** mesma estrutura, com o texto "Não foi possível enviar sua mensagem agora. Tente
  novamente mais tarde." e o botão **Fechar**.
- Deixe o envio em uma função `enviarFormulario(dados)` com um `fetch` para uma URL em variável no
  topo do código (provisória), para eu ligar depois ao meu serviço de e-mail.

### 5. Celular (até 768px)
- No cabeçalho, o botão ENTRE EM CONTATO fica dentro do menu do celular, como um botão grande de
  largura total.
- Ao tocar, o formulário abre **em tela cheia** com:
  - fundo `#F5F3FA`;
  - 100px de espaço no topo e 20px nas laterais;
  - campos com 16px de fonte e 30px entre eles.
- O título e a linha de baixo continuam iguais. A linha de baixo pode quebrar em 2 linhas.
- Sem rolagem horizontal. Use `100dvh` na altura.

### 6. Técnico
- HTML, CSS e JS puro com GSAP. Use classes com o prefixo `wd-contact-`.
- Enquanto o painel estiver aberto, a página atrás não rola (bloqueie o scroll do `body`).
- O foco vai para o primeiro campo quando o painel termina de abrir e volta para o botão
  ENTRE EM CONTATO ao fechar.
- Coloque `aria-expanded` no botão e `aria-label="Fechar contato"` no X.
- Com `prefers-reduced-motion`, abra e feche sem animação, só com fade rápido.

Devolva o HTML, o CSS e o JS completos da área de contato e explique em poucas linhas onde
colar cada parte.
