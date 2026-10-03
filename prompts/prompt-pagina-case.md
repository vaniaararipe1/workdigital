# Prompt — Página de detalhe de projeto (case)

Referência de estrutura: https://lusion.co/projects/oryzo_ai
Prévia criada a partir deste prompt: https://claude.ai/artifact/3Fh9si9SLB3sa15y3GoaKC
Anexe prints da página da Lusion (topo, meio e final) junto com o prompt.

## PROMPT (copie daqui para baixo)

Crie o **modelo de página de detalhe de projeto (case)** do site da Work Digital, seguindo a mesma
estrutura das páginas de projeto da Lusion (https://lusion.co/projects/oryzo_ai, prints em anexo):
título enorme, linha de informações do projeto, mídia em destaque, texto editorial, galeria e
"próximo projeto" no final. Use **o mesmo padrão visual da home que já criamos** (cores, fundo em
degradê contínuo, uptitles com degradê, Space Grotesk nos títulos e CTAs, Nunito nos textos), o
**menu e o rodapé globais** e o **botão flutuante do WhatsApp**.

### Estrutura (de cima para baixo)
1. **Menu global** (o mesmo da home, com "Works" ativo).
2. **Topo do case**
   - Link "← Todos os works" (volta para a página Works).
   - Uptitle com a categoria (ex.: "CASE · WEBSITE").
   - **Nome do projeto em tamanho muito grande** (cerca de 160px no desktop, com `clamp()`),
     podendo quebrar em 2 linhas; a segunda palavra pode ter o degradê dos uptitles.
   - **Linha de informações** com divisória em cima, em 4 colunas: Cliente · Serviços · Ano ·
     Site (link "Ver site no ar ↗", abrindo em nova aba).
   - **Mídia principal** em largura total do container, cantos arredondados (16px), proporção
     16:8, aceitando imagem ou vídeo em loop (mudo, `playsinline`).
3. **O projeto**: grade de 12 colunas; uptitle "O PROJETO" à esquerda (3 colunas) e, à direita
   (8 colunas), um parágrafo de abertura grande (cerca de 36px, Space Grotesk) seguido de duas
   colunas: **Desafio** e **Solução** (uptitle + subtítulo + texto em Nunito).
4. **Galeria**: blocos alternando 2 imagens lado a lado (proporção 4:5) e 1 imagem em largura
   total (proporção 21:9), com legenda pequena opcional em cada mídia. Aceita imagens e vídeos.
5. **Resultados**: uptitle "RESULTADOS", parágrafo grande e 3 números em destaque com legenda.
   Se o case não tiver números, a seção pode ser escondida.
6. **Ficha técnica**: 3 colunas (Entregas · Tecnologia · Equipe).
7. **Próximo projeto**: uptitle "PRÓXIMO PROJETO", nome do próximo case em tamanho muito grande e um
   círculo com seta em degradê. No hover, o nome desliza levemente para a direita e a seta gira
   -45°. O bloco inteiro é um link para o próximo case.
8. **Rodapé global** e **botão flutuante do WhatsApp**.

### Conteúdo editável
- Todo o conteúdo do case (nome, categoria, cliente, serviços, ano, link, textos, imagens, vídeos,
  números, ficha técnica e próximo projeto) deve vir de um **objeto JS no topo do arquivo**
  (ex.: `const CASE = {...}`), para eu criar um case novo trocando só esse objeto.
- Use como exemplo o case **Vice Versa Estamparia** (site institucional, 2026) com textos e
  números provisórios, que vou substituir.

### Animações (no estilo da Lusion, sem exagero)
- Título e mídia principal entram com subida suave ao carregar.
- Imagens da galeria entram com fade + leve subida ao entrar na tela (Intersection Observer), a
  partir de um estado visível (sem deixar a página em branco se o JS falhar).
- Tudo desligado com `prefers-reduced-motion`.

### Técnico
- HTML + CSS + JS puro, reaproveitando os arquivos/variáveis globais do site (menu, rodapé,
  fontes, cores). Classes com prefixo `wd-case-`.
- Responsivo: no celular, a linha de informações vira 2 colunas, as colunas de texto e a galeria
  ficam em 1 coluna, sem rolagem horizontal.
- `alt` em todas as imagens, `loading="lazy"` na galeria, foco visível e contraste AA.

Devolva o arquivo completo da página `case.html` e explique em poucas linhas como criar um case novo.
