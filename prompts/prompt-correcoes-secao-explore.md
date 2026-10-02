# Prompt — Correções da seção "Aceite o desafio do novo"

Use na mesma conversa do ChatGPT em que a seção foi gerada, anexando de novo o print da seção
EXPLORE de https://www.auros.global/ (de preferência dois prints: um sem hover e outro com o
mouse sobre um card, para mostrar a cor do hover).

---

## PROMPT (copie daqui para baixo)

Faça as correções abaixo na seção "Aceite o desafio do novo" que você criou. Use o print em
anexo da seção EXPLORE da Auros como referência visual. Não altere nada além destes pontos e
devolva o código completo da seção atualizado.

**1. Texto "Explore Auros" → "Soluções Work"**
Na referência existe o texto **"Explore Auros"**. Substitua por **"Soluções Work"**, mantendo
a mesma posição, tamanho, peso e estilo do original.
Os cards de serviço continuam na mesma ordem: o 1º card (que na referência é
"Proprietary Trading") é **Criação de Sites**, o 2º é **Criação de Blogs** e o 3º é
**Criação de Landing pages**.

**2. Título com gradiente**
Na referência, a palavra **"EXPLORE"** tem cor em gradiente. Aplique o mesmo efeito em
**"ACEITE O DESAFIO DO NOVO"**: mesma direção e mesma suavidade do gradiente da referência,
usando as cores da Work Digital. Use `background: linear-gradient(...)`,
`-webkit-background-clip: text`, `background-clip: text` e `color: transparent`, com uma cor
sólida de fallback para navegadores sem suporte.

**3. Primeiro card sempre selecionado**
Na referência, o 1º card (Proprietary Trading) fica sempre no estado selecionado/ativo. Faça
igual com o card **Criação de Sites**: ao carregar a página ele já aparece com o mesmo visual
de selecionado da referência (mesma cor de fundo, borda, cor do texto e seta).
Os outros dois cards se comportam exatamente como na referência quando recebem o mouse.

**4. Retângulo no fundo dos 3 cards**
Na referência, a área com os 3 blocos de serviço tem um retângulo no fundo. Faça igual: mesma
posição, tamanho, proporção, cantos e espaçamento em relação aos cards. Use as **cores da Work
Digital** no retângulo, não as cores da Auros. No celular, o retângulo acompanha os cards
empilhados sem causar rolagem horizontal.

**5. Cor do hover igual à referência**
A cor do hover dos cards está diferente da referência. Copie o comportamento do hover da Auros
(o que muda de cor: fundo, texto, borda e seta; e a velocidade da transição). Se a cor exata
da Auros conflitar com a identidade visual, use o tom equivalente da paleta da Work Digital,
mantendo o mesmo contraste e o mesmo efeito. A imagem que aparece no hover continua
funcionando como antes.

Ao final, liste em poucas linhas o que mudou em cada um dos 5 itens.
