# Prompt — Página de detalhe de projeto (case)

Referência: https://lusion.co/projects/oryzo_ai (gravação de tela enviada pela cliente)
Prévia: https://claude.ai/artifact/3Fh9si9SLB3sa15y3GoaKC
Anexe a gravação de tela da página da Lusion junto com o prompt.

## PROMPT (copie daqui para baixo)

Crie o **modelo de página de detalhe de projeto (case)** do site da Work Digital, igual à página de
projeto da Lusion (https://lusion.co/projects/oryzo_ai, gravação em anexo). Use o conteúdo, as
fontes (Space Grotesk nos títulos e botões, Nunito nos textos) e as cores da Work Digital, além do
botão flutuante do WhatsApp.

### Como a página funciona (igual à referência)
- A página **rola na horizontal**: o usuário rola o mouse/trackpad para baixo e o conteúdo anda
  para a esquerda, de forma suave.
- Técnica: uma `section` com altura = altura da tela + largura total da faixa; dentro dela, um
  container `position: sticky; top: 0; height: 100vh; overflow: hidden` com uma faixa
  `display: flex` que recebe `transform: translateX(-progresso)` calculado pela rolagem. Use uma
  interpolação suave (lerp ~0.12 por frame com `requestAnimationFrame`) para o movimento ficar
  fluido. Recalcule tudo no `resize`.
- Sem `prefers-reduced-motion`: sem suavização, o movimento acompanha a rolagem direto.
- **No celular (até 900px)** a página vira rolagem vertical normal: painel de texto em cima e as
  mídias empilhadas, todas com cantos arredondados.

### Cabeçalho fixo (sobre o conteúdo, sem fundo)
- Esquerda: logo **WORK DIGITAL** em maiúsculas, na cor de destaque (lilás).
- Centro: pílula branca **← VOLTAR** (volta para a página Works).
- Direita: botão redondo branco (som/menu reduzido), pílula escura **VAMOS CONVERSAR •** e pílula
  branca **MENU ••**. Pílulas com 42px de altura, texto 13px em maiúsculas, leve zoom no hover.

### Painel de texto (primeiro item da faixa, à esquerda)
- Nome do projeto em fonte **leve (peso 400)** e grande (~72px), sem degradê.
- Duas colunas: à esquerda, 2 parágrafos curtos (14–15px) sobre o projeto, com **palavras-link na
  cor de destaque**; abaixo, pílula branca **● VER PROJETO NO AR**. À direita, listas com rótulos
  pequenos em maiúsculas na cor de destaque: **SERVIÇOS** (lista) e **LINKS** (lista).

### Faixa de mídias (depois do texto)
- Imagens e vídeos lado a lado, separados por ~40px, com tamanhos variados como na referência:
  - algumas com **74% da altura da tela** e cantos arredondados (12px), em 16:9, 1:1 ou 3:4;
  - outras com **100% da altura da tela**, sem cantos arredondados, em 3:4 ou 4:5.
- Aceitar imagem (`<img>`) e vídeo em loop (`<video autoplay muted loop playsinline>`).
- Legenda opcional pequena, em pílula translúcida, no canto inferior esquerdo da mídia.

### Próximo projeto (último item da faixa)
- Painel claro (lilás bem claro), com 100% da altura, com uma mancha suave de cor ao fundo.
- Nome do próximo case **muito grande, peso leve, em cinza-lilás**, podendo ser cortado pela
  borda direita; no hover fica escuro e desliza levemente.
- Embaixo: **PRÓXIMO PROJETO ———— →**; no hover a linha aumenta.
- Ao clicar: tela preta de transição com a palavra **CARREGANDO** em fonte pixelada (Google Fonts
  "Silkscreen"), uma barrinha de progresso e um contador grande de 000 a 100; depois abre o
  próximo case.

### Conteúdo editável
Todo o conteúdo (nome, textos, links, serviços, links externos, lista de mídias com tipo, arquivo,
proporção e altura, e o próximo case) deve vir de um **objeto JS no topo do arquivo**
(`const CASE = {...}`), para eu criar um case novo trocando só esse objeto. Use o case
**Vice Versa Estamparia** como exemplo, com textos provisórios.

### Técnico
- HTML + CSS + JS puro, sem bibliotecas. Classes com prefixo `wd-case-`.
- `alt` em todas as imagens, `loading="lazy"` nas mídias fora da primeira tela, foco visível nos
  links e botões, sem rolagem horizontal da página no celular.

Devolva o arquivo completo `case.html` e explique em poucas linhas como criar um case novo.
