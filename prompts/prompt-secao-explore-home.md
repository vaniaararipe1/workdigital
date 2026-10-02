# Prompt — Seção "Aceite o desafio do novo" (home)

Referência de estrutura: seção **EXPLORE** da home de https://www.auros.global/

> **Importante:** antes de colar o prompt no ChatGPT, tire um print da seção EXPLORE do site
> da Auros e anexe junto. O prompt pede que o ChatGPT siga o print à risca, então o layout final
> depende dele.

---

## PROMPT (copie daqui para baixo)

Você é um desenvolvedor front-end sênior especializado em sites institucionais premium.
Crie **uma seção da home** do site da agência **Work Digital**, replicando **exatamente a mesma
estrutura, layout, proporções, espaçamentos, hierarquia tipográfica e interações** da seção
**"EXPLORE"** da home de https://www.auros.global/ (veja o print em anexo). Troque apenas os
textos pelos que estão abaixo e adicione o comportamento de imagem no hover descrito no item 3.
Não use logos, marcas nem imagens da Auros.

### 1. Conteúdo (substituições exatas)

| Na referência | Na Work Digital |
|---|---|
| Título da seção: **EXPLORE** | **Aceite o desafio do novo** |
| Card 1: **Explore Auros** | **Criação de Sites** |
| Card 2: **Liquidity Solutions** | **Criação de Blogs** |
| Card 3: **Careers** | **Criação de Landing pages** |
| CTA: **PARTNER WITH US** | **SOLICITE UMA PROPOSTA** |

**Textos descritivos de cada card (use exatamente estes):**

- **Criação de Sites:** Sites profissionais, personalizados, otimizados, de fácil gerenciamento, tornando o seu negócio visível para milhares de clientes e valorizando sua marca.
- **Criação de Blogs:** Criação de blogs profissionais para sua marca acessar todo o poder do marketing de conteúdo. Construa sua audiência na web e seja autoridade em sua área de atuação.
- **Criação de Landing pages:** Atrair não é o suficiente. É preciso conquistar seu visitante no momento em que ele chega a sua página de vendas. Criamos Landing Pages que convertem e alavancam seus resultados.

Mantenha a mesma caixa (maiúsculas/minúsculas) usada na referência para cada tipo de texto:
se o título da seção é todo em maiúsculas na Auros, deixe "ACEITE O DESAFIO DO NOVO" em
maiúsculas via CSS (`text-transform`), sem mudar o texto no HTML.

### 2. Estrutura (igual à referência)
- Mesmo fundo, mesma grade e mesmo alinhamento da seção original.
- Título da seção na mesma posição, tamanho e peso.
- Os **3 cards na mesma disposição** da referência (mesma ordem, mesmas larguras, mesmas
  divisórias/bordas, mesma numeração ou ícone de seta, se houver).
- Cada card contém: título do serviço, texto descritivo e o mesmo elemento de link/seta da
  referência. O card inteiro é clicável (links: `#criacao-de-sites`, `#criacao-de-blogs`,
  `#criacao-de-landing-pages`).
- O CTA **"SOLICITE UMA PROPOSTA"** fica no mesmo lugar e com o mesmo estilo de botão do
  "PARTNER WITH US" (inclusive o hover do botão). Link: `#contato`.

### 3. Hover com imagem em cada card (novo)
- Ao passar o mouse sobre um card, aparece **um espaço para imagem** dentro dele.
- A imagem surge com animação suave (fade + leve zoom de 1.05 para 1, ou revelação com
  `clip-path` de baixo para cima), duração de 0.5s a 0.7s, easing `cubic-bezier(0.22, 1, 0.36, 1)`.
- O texto continua legível sobre ou ao lado da imagem: use um overlay escuro em gradiente se
  a imagem ficar atrás do texto.
- O espaço da imagem tem proporção fixa (ex.: 4:3 ou 16:10) para o card não "pular" de altura
  no hover.
- Deixe a imagem configurável por card, com um placeholder enquanto não houver a definitiva:
  ```html
  <img src="img/criacao-de-sites.jpg" alt="Exemplo de site criado pela Work Digital" loading="lazy">
  ```
  Use imagens de placeholder (ex.: `https://picsum.photos/800/600?random=1`, `=2`, `=3`) até eu trocar.
- **Acessibilidade:** a mesma revelação acontece no foco do teclado (`:focus-visible` /
  `:focus-within`).
- **Celular e tablet (sem hover):** a imagem aparece sempre visível acima do título do card,
  ou é revelada quando o card entra na tela.
- Respeite `prefers-reduced-motion`: sem animação, só troca de opacidade.

### 4. Requisitos técnicos
- Entregue **HTML + CSS + JavaScript puro** (JS só se for necessário) em um único bloco,
  pronto para colar na home. Prefixe as classes com `wd-explore-` para não conflitar com o
  resto do site.
- Use variáveis CSS no topo (`:root` ou no seletor da seção) para cores, fontes e espaçamentos,
  com os valores extraídos da referência. Se não for possível identificar a fonte exata, sugira
  a alternativa mais próxima do Google Fonts.
- Responsivo: desktop (1440px), notebook (1280px), tablet (768px) e celular (390px). No
  celular, os cards ficam empilhados em uma coluna.
- HTML semântico (`section`, `h2`, `h3`, `a`), foco visível e contraste AA.

### 5. Formato da resposta
1. Em até 5 linhas, descreva o que você identificou na seção de referência (layout, cores,
   fontes, interações).
2. Depois, o código completo, sem trechos omitidos.
3. No final, diga onde trocar as imagens, os links e as cores.
