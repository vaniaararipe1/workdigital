# Prompt — Correções 3 da seção "Aceite o desafio do novo" (retângulos, foto e partículas)

Anexe um print da seção EXPLORE da Auros mostrando os dois retângulos e as bolinhas no fundo.

## PROMPT (copie daqui para baixo)

Faça estas correções na seção "Aceite o desafio do novo" (`#wd-explore`). Não altere textos,
fontes, hover, CTA nem a lógica do 1º card. Devolva o código atualizado das partes alteradas.

**1. Dois retângulos, como na referência**
Na referência existem **dois retângulos**, e no nosso site só foi criado um:
- **Retângulo maior (externo):** ocupa a largura da área da seção, indo das laterais esquerda à
  direita, com o mesmo arredondamento, borda, espaçamento interno e posição da referência. Ele
  envolve todo o conteúdo: o retângulo menor e o espaço da foto.
- **Retângulo menor (interno):** é o que já existe e envolve **apenas os 3 boxes** de serviço.
  Ele fica do lado esquerdo, dentro do retângulo maior.
- Use as cores da Work Digital nos dois, com o maior um pouco mais sutil que o menor, para manter
  a mesma hierarquia da referência.

**2. Espaço para foto do lado direito**
- Dentro do retângulo maior, do **lado direito** do retângulo menor, crie um espaço para foto.
- A foto ocupa **toda a altura do retângulo menor (o da esquerda)**: o topo e a base dos dois ficam
  alinhados. Use CSS Grid com duas colunas e `align-items: stretch`, e na imagem
  `width: 100%; height: 100%; object-fit: cover;`, com cantos arredondados iguais aos do
  retângulo menor.
- Deixe um placeholder (`https://picsum.photos/900/1100?random=21`) com `alt` descritivo, em um
  ponto fácil de trocar no código.
- No tablet e no celular, a foto vai para baixo dos 3 boxes, com largura total e proporção fixa
  (ex.: `aspect-ratio: 4 / 3`).

**3. Partículas/bolinhas no fundo do retângulo maior**
- Como na referência, preencha o fundo de **todo o retângulo maior** com pequenas
  partículas/bolinhas, com o mesmo tamanho, densidade, opacidade e movimento da referência
  (se estiverem paradas na referência, deixe paradas).
- Use as cores da Work Digital, com opacidade baixa, para não atrapalhar a leitura dos boxes.
- As partículas ficam **atrás** do retângulo menor e da foto (`z-index` menor) e não podem
  receber cliques (`pointer-events: none`).
- Se for animado, use um `canvas` que acompanha o tamanho do retângulo maior no `resize`
  (considerando `devicePixelRatio`) e pare a animação com `prefers-reduced-motion`.

**4. Manter**
- O fundo da seção continua `transparent`, com o gradiente do site contínuo. Só o retângulo maior
  tem cor própria.
- Sem rolagem horizontal em nenhuma largura de tela.

Ao final, confirme em uma linha cada um dos 4 itens.
