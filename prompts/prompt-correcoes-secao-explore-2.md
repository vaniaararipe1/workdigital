# Prompt — Correções 2 da seção "Aceite o desafio do novo"

Use na mesma conversa do ChatGPT. Anexe:
- print do topo do preview atual (header + seção), mostrando onde o fundo preto quebra o gradiente;
- print ou gravação de tela do hover do botão "PARTNER WITH US" na Auros.

---

## PROMPT (copie daqui para baixo)

Ainda há ajustes na seção "Aceite o desafio do novo" (`#wd-explore`). Preview atual:
https://workdigital-hero-preview.onrender.com/?v=3f101bd2#wd-explore

Faça **somente** as correções abaixo, sem mexer no resto, e devolva o código completo atualizado
(HTML + CSS + JS) das partes alteradas.

**1. Primeiro card: selecionado só na primeira vez**
Eu me expressei mal antes: o card **Criação de Sites** não deve ficar sempre selecionado. Siga
a mesma lógica da referência (Auros):
- Ao carregar a página, o 1º card aparece selecionado (classe `is-active`).
- Assim que o usuário passar o mouse (ou focar pelo teclado) em **qualquer** card, remova o
  `is-active` do 1º card. A partir daí, o visual de selecionado aparece só no card que está
  com hover/foco, como na referência.
- Ao tirar o mouse da área dos cards, o 1º card **não** volta a ficar selecionado.
- Implemente com um pequeno JS (`mouseenter`/`focusin` uma única vez, com `{ once: true }`
  ou flag), sem bibliotecas.

**2. Hover do CTA "SOLICITE UMA PROPOSTA" igual à referência**
O hover do botão ainda está diferente do "PARTNER WITH US" da Auros (veja o print/gravação em
anexo). Antes de corrigir, liste em 3 linhas o que muda no botão da referência no hover
(cor de fundo, cor do texto, borda, seta/ícone, direção do preenchimento, velocidade) e o que
está diferente no seu. Depois reproduza o mesmo efeito, usando as cores da Work Digital, e
aplique o mesmo efeito também no `:focus-visible`.

**3. Fonte dos textos descritivos: Nunito, um pouco menor**
- Troque a fonte **apenas dos textos descritivos dos cards** para **Nunito** (Google Fonts).
  Carregue com:
  `<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600&display=swap" rel="stylesheet">`
  e use `font-family: "Nunito", system-ui, sans-serif;`.
- Diminua um pouco o tamanho: cerca de 10% a 15% menor que o atual (ex.: de 18px para 16px no
  desktop e de 16px para 14–15px no celular), mantendo `line-height` em torno de 1.6 para a
  leitura continuar confortável.
- Títulos dos cards, título da seção e CTA continuam com a fonte atual.

**4. Fundo em gradiente contínuo (sem fundo preto na seção)**
Você colocou um `background` preto nesta nova seção, e isso cria um corte visível entre o
header/hero e a seção, quebrando o visual. O fundo em gradiente do site precisa ser
**contínuo**, como se header, hero e esta seção estivessem sobre o mesmo fundo:
- Remova o fundo sólido de `#wd-explore` (e de qualquer wrapper, `::before` ou `::after` dela
  que pinte o fundo inteiro): deixe `background: transparent`.
- Aplique o gradiente em um **único elemento pai** que envolva header, hero e esta seção (ou no
  `body`), para que ele corra sem emendas. Se precisar estender o gradiente, use as mesmas cores
  e a mesma direção do gradiente atual do header/hero, com a última cor do hero continuando na
  seção.
- Confira se não sobrou nenhuma faixa ou linha entre as seções (margens, `border`, `box-shadow`
  ou `overflow` que revelem outra cor).
- O **retângulo atrás dos 3 cards continua** existindo, com as cores da Work Digital; só o fundo
  da seção inteira é que deixa de ser preto.

Ao final, confirme em uma linha cada um dos 4 itens.
