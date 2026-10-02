# Prompt — Correção do globo (`#wd-transformacao`)

Anexe os dois recortes do globo: o atual da Work (roxo) e o da referência (Auros, verde-azulado).

## PROMPT (copie daqui para baixo)

O globo da seção "Transformação digital" (`#wd-transformacao`) ainda está muito diferente da
referência (prints em anexo: o 1º é o nosso, o 2º é a referência). Corrija **somente o globo e o
brilho dele**, sem mexer em textos, botão e layout do card. Use as cores da Work Digital
(lilás/roxo no lugar do verde-azulado). Devolva o código atualizado das partes alteradas.

**O que está errado hoje e como deve ficar**

**1. Cor do globo: está desbotado e acinzentado**
- Hoje o globo é quase branco, lavado, com tons de cinza. Na referência ele tem **cor**: um tom
  claro e saturado (verde-água claro), que no nosso caso deve ser **lilás/lavanda claro e
  saturado** (ex.: entre `#D8CCFF` e `#EEE8FF`), e não branco.
- Distribuição de luz igual à referência: mais colorido na parte de cima e no centro, ficando
  mais claro (quase branco) em direção à parte de baixo e à direita.
- **Não use preto, cinza ou branco puro misturado nos gradientes do globo.** Use só tons de
  lilás, lavanda e branco-lilás, para não ficar sujo.

**2. Remova a faixa cinza perto da borda esquerda**
- Hoje aparece uma faixa/anel cinza dentro do globo, perto da borda esquerda. Na referência ela
  não existe. Remova qualquer `box-shadow: inset`, `radial-gradient` ou camada que esteja criando
  essa faixa.

**3. Borda e brilho**
- Na referência, a borda esquerda do globo é uma **linha de luz muito clara** (quase branca), e
  logo fora dela há um **brilho forte e difuso** que se espalha pelo fundo do card.
- Faça a borda com um brilho branco-lilás intenso e o glow externo em lilás claro, com bastante
  blur (60px a 120px), clareando o fundo do card perto do globo, sem tons de cinza.

**4. Mapa de pontos: está quase invisível**
- Hoje os pontos são minúsculos, muito claros e espaçados demais, e o mapa quase não aparece.
- Na referência os pontos são **maiores (cerca de 3px a 4px de diâmetro)**, em uma **grade mais
  densa (espaçamento de cerca de 7px a 8px)** e com **mais contraste**: cinza-azulado médio com
  opacidade de cerca de 70%. No nosso, use um roxo-acinzentado médio (ex.: `#7A6E9E` a 70%), para
  os continentes ficarem bem legíveis.
- Os pontos perto da borda esquerda iluminada ficam mais claros e suaves (somem dentro do brilho),
  como na referência.

**5. Enquadramento do mapa**
- Na referência o mapa é **maior** e mostra as Américas grandes e centralizadas, com a Groenlândia
  e parte da Europa no topo à direita e parte da África na borda direita.
- Aumente a escala do mapa e ajuste a posição para ter o mesmo enquadramento.

**6. Canto inferior direito**
- Hoje o canto inferior direito do globo escurece para roxo. Na referência essa região é a mais
  clara do globo. Remova o escurecimento.

Ao final, confirme em uma linha cada um dos 6 itens.
