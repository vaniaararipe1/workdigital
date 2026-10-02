# Prompt — Iluminação do globo e do fundo (`#wd-transformacao`)

Anexe o print atual do site da Work e o print da referência (Auros, NETWORK / Global presence).

## PROMPT (copie daqui para baixo)

A estrutura da seção "Transformação digital" (`#wd-transformacao`) está certa. Agora ajuste
**somente a iluminação do globo e do fundo do card**, comparando com a referência (prints em
anexo). Hoje o globo está chapado, o brilho é fraco e aparece cortado. Mantenha textos, botão,
layout e as cores da Work Digital (roxo/lilás no lugar do verde-azulado). Devolva o código
atualizado das partes alteradas.

**1. Globo com volume (sombras internas)**
Hoje o globo é uma cor lilás chapada. Na referência ele tem profundidade. Monte o preenchimento
com camadas de gradiente:
- um `radial-gradient` principal com o ponto mais claro (quase branco) perto da borda esquerda,
  passando para lilás claro no meio e um lilás/roxo um pouco mais escuro na borda direita;
- um segundo `radial-gradient` suave no topo, para dar a sensação de luz vindo de cima;
- uma sombra interna (`box-shadow: inset ...`) em roxo, com bastante blur, na borda direita e na
  parte de baixo, para o globo parecer redondo e não um disco plano.

**2. Brilho da borda esquerda mais forte e mais difuso**
- O brilho da borda esquerda do globo precisa ser **mais intenso e com muito mais blur**, como na
  referência, espalhando luz sobre o fundo do card (não só uma linha fina na borda).
- Faça o brilho em uma camada separada (pseudo-elemento ou `div`) atrás do globo, maior que ele,
  com `filter: blur(60px a 100px)` e cor branco-lilás com opacidade alta, e se precisar
  `mix-blend-mode: screen`.
- Combine com `box-shadow` externos em camadas no próprio globo
  (ex.: `0 0 40px`, `0 0 120px`, `0 0 240px` em lilás/branco com opacidades diferentes).

**3. Brilho sem cortes**
- Hoje o brilho aparece cortado. Nenhum elemento intermediário (wrapper do globo, máscara,
  `overflow: hidden`) pode cortar o glow. Só o **card** tem `overflow: hidden`.
- O brilho precisa se dissolver suavemente dentro do card, sem linhas retas, bordas visíveis ou
  "degraus". Se o corte vier de `mask-image` ou de um retângulo com blur, troque por gradientes
  radiais que terminam em transparente.

**4. Luz espalhada no fundo do card**
- Na referência, a luz do globo ilumina o fundo do card: a área entre o texto e o globo, e
  principalmente a parte de baixo, fica mais clara. Adicione um `radial-gradient` grande, em lilás
  claro com opacidade média, saindo da região do globo em direção ao centro e à base do card.
- Mantenha o lado esquerdo, onde está o texto, mais escuro, para o texto branco continuar legível
  (contraste AA).

**5. Brilho em volta do card**
- Aumente o halo externo em volta do card (`box-shadow` grande e difuso em roxo/lilás, ex.:
  `0 0 120px` a `0 0 200px`), como o brilho verde em volta do card da referência, sem criar
  faixas no fundo da página.

**6. Mapa de pontos integrado à luz**
- Os pontos devem **sumir suavemente perto da borda esquerda iluminada** e nas bordas do globo,
  como na referência. Use `mask-image: radial-gradient(...)` na camada dos pontos.
- Mantenha os pontos discretos (lilás-acinzentado, opacidade baixa).

Ao final, confirme em uma linha cada um dos 6 itens.
