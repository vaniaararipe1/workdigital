# Prompt — Seção "Works" (cases) da home

Referência: seção **STATS | AUROS IN NUMBERS** da home de https://www.auros.global/
Anexe um print dessa seção junto com o prompt.

## PROMPT (copie daqui para baixo)

Agora crie a próxima seção da home, logo abaixo de "Aceite o desafio do novo", seguindo a
mesma estrutura da seção **"STATS | AUROS IN NUMBERS"** da Auros (print em anexo), com o mesmo
padrão visual que já usamos nas seções anteriores.

**Textos**
- "STATS" → **CASES**
- "AUROS IN NUMBERS" → **WORKS**
- Descritivo: **Alguns dos projetos que tiramos do papel. Sites, blogs e landing pages feitos sob medida para marcas de diferentes segmentos, cada um pensado para o negócio do cliente.**

**Os 4 blocos**
Os 4 blocos da referência viram **4 cases**. Mantenha a mesma disposição da referência e, em
cada bloco, coloque:
- um **espaço para imagem** (vou inserir as imagens depois; use um placeholder);
- **título** e **descrição**, nas mesmas posições e estilos da referência.

Use textos provisórios ("Nome do case 1" / "Descrição do case 1", e assim por diante), que vou
substituir pelos cases reais.

**CSS (seguir o padrão das seções anteriores)**
- Fundo: `background: transparent` na seção. O gradiente do site continua contínuo, sem fundo preto e sem faixas ou emendas com a seção anterior.
- "WORKS" com o mesmo gradiente de texto usado em "ACEITE O DESAFIO DO NOVO"; "CASES" com o mesmo estilo que "STATS" tem na referência.
- Títulos dos cases na mesma fonte dos títulos dos cards de "Aceite o desafio do novo"; descrições em **Nunito**, no mesmo tamanho dos descritivos desses cards.
- Imagem com proporção fixa (ex.: `aspect-ratio: 16 / 10; object-fit: cover;`), para os blocos ficarem com a mesma altura.
- Reproduza o hover e a animação de entrada dos blocos da referência, se houver, e desligue as animações com `prefers-reduced-motion`.
- Responsivo: mesma grade da referência no desktop, 2 colunas no tablet e 1 no celular, sem rolagem horizontal.
- Classes com o prefixo `wd-works-` e `id="wd-works"` na seção, para não conflitar com o resto do código.

Devolva só o código desta nova seção (HTML + CSS + JS, se precisar), pronto para colar abaixo de `#wd-explore`.
