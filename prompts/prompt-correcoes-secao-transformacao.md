# Prompt — Correções da seção "Transformação digital" (`#wd-transformacao`)

Anexe os dois prints: como está hoje no site da Work e a referência da Auros (NETWORK / Global presence).

## PROMPT (copie daqui para baixo)

Compare a seção "Transformação digital" (`#wd-transformacao`) com a referência da Auros
(prints em anexo: o 1º é o nosso site, o 2º é a referência). Faça as correções abaixo, mantendo
os textos e as cores da Work Digital (roxo/violeta no lugar do verde-azulado da referência).
Devolva o código completo atualizado da seção.

**1. Conteúdo dentro de um card, não em tela cheia**
- Hoje a seção ocupa a largura inteira. Na referência, todo o conteúdo fica dentro de **um card
  retangular centralizado**, com margens nas laterais e em cima/embaixo.
- Card: largura máxima de cerca de 1360px (aprox. 75% da tela no desktop), altura de cerca de
  600px, `border-radius` de cerca de 16px e `overflow: hidden`.
- Em volta do card, um **brilho suave** na cor da marca (ex.: `box-shadow` grande e difuso em
  roxo com baixa opacidade), como o halo verde em volta do card da referência.
- O fundo da seção continua `transparent`, com o gradiente do site contínuo. Hoje aparece uma
  área preta no canto superior direito: remova.

**2. Fundo do card**
- Gradiente horizontal: roxo escuro à esquerda, clareando em direção ao globo, à direita.
- No canto inferior esquerdo, uma luz suave e clara (como o tom bege/acinzentado da referência),
  usando um `radial-gradient` com baixa opacidade.

**3. Globo**
- O globo fica **dentro do card**, cortado pelas bordas de cima, de baixo e da direita
  (`overflow: hidden` do card). Hoje ele sai da área e está grande demais.
- A borda esquerda do globo começa por volta de 55% da largura do card, com um **brilho difuso
  e claro** (glow) nessa borda, como na referência.
- O globo é claro e luminoso (branco com leve tom lilás), sem a borda vermelha/magenta que
  aparece hoje no lado direito.
- **Remova as faixas horizontais retangulares** que aparecem em cima e embaixo do globo (parecem
  vir de uma máscara ou `filter: blur` aplicado em um retângulo). A transição do globo para o
  fundo tem que ser suave, sem cantos nem linhas retas visíveis.
- Mapa de pontos: pontos **menores e mais claros** (cinza-lilás, com opacidade de cerca de
  40% a 60%), discretos sobre o globo, como na referência. Hoje estão escuros e chamam atenção
  demais.

**4. Textos**
- Bloco de texto alinhado à esquerda, com recuo interno de cerca de 80px da borda esquerda do card,
  centralizado na vertical.
- "EXPLORE": mantenha como está (maiúsculas, espaçamento entre letras, branco).
- "Transformação digital": no desktop, em **uma linha só**, como "Global presence" na
  referência (tamanho em torno de 56px, peso semibold/bold, `letter-spacing` levemente negativo).
  Ajuste a largura do bloco de texto para caber em uma linha.
- Descrição: **branca** (não cinza/lilás), com tamanho em torno de 18px, `line-height` em torno de
  1.5 e largura máxima de cerca de 540px. Continua em Nunito.
- Confira se a frase "Quem não é encontrado, não é escolhido." está na mesma posição e estilo
  em que "Helping institutions operate with confidence." aparece na referência.

**5. Botão "SOLICITE PROPOSTA"**
- Igual ao "JOIN OUR TEAM" da referência: texto em maiúsculas com **espaçamento entre letras**
  (`letter-spacing` em torno de 0.1em), tamanho em torno de 14px, ícone de seta ↗ à direita do
  texto, `border-radius` de cerca de 4px.
- Fundo em gradiente horizontal nas cores da Work (roxo mais claro à esquerda, mais escuro à
  direita). Mantenha o hover já definido para os CTAs do site.

**6. Responsivo**
- No tablet e no celular, o card ocupa a largura disponível com margem lateral de 16px, o texto
  fica em cima e o globo embaixo (ou atrás do texto, com opacidade menor), sem rolagem
  horizontal. No celular, o título pode quebrar em duas linhas.

Ao final, confirme em uma linha cada um dos 6 itens.
