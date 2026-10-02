# Prompt — Seção "Works" (cases) da home

Referência de estrutura: seção **STATS | AUROS IN NUMBERS** da home de https://www.auros.global/

> Antes de colar no ChatGPT, anexe um print da seção STATS da Auros (e, se houver animação
> nos números ou hover nos blocos, uma gravação de tela).

## Sugestões para o texto "STATS" (escolha uma e troque no prompt, se quiser)
- **CASES** (usada no prompt)
- **PORTFÓLIO**
- **NOSSOS CASES**
- **NA PRÁTICA**

## Sugestões de descritivo (escolha uma)
1. Alguns dos projetos que tiramos do papel. Sites, blogs e landing pages feitos sob medida para marcas de diferentes segmentos, cada um pensado para o negócio do cliente. **(usada no prompt)**
2. Cada projeto começa com uma conversa sobre o negócio do cliente. Veja alguns sites, blogs e landing pages que criamos e o que eles mudaram para quem confiou na Work.
3. Marcas de vários segmentos já contaram com a Work para aparecer melhor na internet. Conheça alguns desses projetos.

---

## PROMPT (copie daqui para baixo)

Crie a **próxima seção da home** da Work Digital, logo abaixo da seção "Aceite o desafio do
novo". Replique **exatamente a mesma estrutura, layout, proporções, espaçamentos, hierarquia
tipográfica e animações** da seção **"STATS | AUROS IN NUMBERS"** da home de
https://www.auros.global/ (veja o print em anexo), trocando o conteúdo conforme abaixo.
Não use logos, marcas nem imagens da Auros.

### 1. Textos (substituições exatas)

| Na referência | Na Work Digital |
|---|---|
| **STATS** | **CASES** |
| **AUROS IN NUMBERS** | **WORKS** |
| Texto descritivo da seção | Alguns dos projetos que tiramos do papel. Sites, blogs e landing pages feitos sob medida para marcas de diferentes segmentos, cada um pensado para o negócio do cliente. |

- Mantenha no "CASES" o mesmo estilo que o "STATS" tem na referência (posição, tamanho, cor).
- Se o título da referência tiver cor em gradiente, aplique o mesmo gradiente em "WORKS", com as
  cores da Work Digital, como fizemos em "ACEITE O DESAFIO DO NOVO".

### 2. Os 4 blocos viram 4 cases
Os 4 blocos da referência (que hoje mostram números) passam a mostrar **4 cases** da Work Digital.
Mantenha a mesma grade, ordem, tamanhos, bordas, divisórias e espaçamentos dos blocos da
referência. Em cada bloco:
- **Espaço para imagem** do case, com proporção fixa (ex.: 16:10) e `object-fit: cover`, para
  eu trocar depois. Use placeholders (`https://picsum.photos/800/500?random=11`, `=12`, `=13`,
  `=14`) e `alt` descritivo.
- **Título** do case no lugar onde a referência mostra o número/destaque, com o mesmo peso
  visual.
- **Descrição** curta no lugar do texto de apoio da referência, com o mesmo posicionamento.

Conteúdo provisório (vou substituir pelos cases reais):

| Bloco | Título | Descrição |
|---|---|---|
| 1 | [Nome do case 1] | [Tipo de projeto e o que foi feito, em até 2 linhas.] |
| 2 | [Nome do case 2] | [Tipo de projeto e o que foi feito, em até 2 linhas.] |
| 3 | [Nome do case 3] | [Tipo de projeto e o que foi feito, em até 2 linhas.] |
| 4 | [Nome do case 4] | [Tipo de projeto e o que foi feito, em até 2 linhas.] |

Deixe os 4 cases em um array JS ou em blocos HTML bem marcados com comentários
(`<!-- CASE 1 -->`), para eu editar título, descrição, imagem e link com facilidade.
Cada bloco é um link para `#case-1`, `#case-2`, `#case-3` e `#case-4`.

Se a referência tiver animação de entrada (ex.: contagem dos números ou blocos surgindo ao rolar),
reproduza o mesmo tipo de entrada nos cases (fade/subida dos blocos ao entrar na tela). Se os
blocos da referência tiverem hover, reproduza o mesmo hover.

### 3. Manter o padrão das seções anteriores
- **Fundo:** sem fundo próprio (`background: transparent`). O gradiente do site continua
  contínuo, sem faixas ou emendas entre esta seção e a anterior.
- **Fontes:** títulos com a mesma fonte dos títulos da seção "Aceite o desafio do novo";
  descrições em **Nunito** (Google Fonts), no mesmo tamanho dos descritivos dos cards da seção
  anterior.
- **Cores:** as da Work Digital já usadas no site.
- Prefixe as classes com `wd-works-` para não conflitar com o resto do código.

### 4. Requisitos técnicos
- HTML + CSS + JS puro (JS só se necessário), pronto para colar abaixo da seção `#wd-explore`.
  Use `id="wd-works"` na seção.
- Responsivo: no desktop, mesma grade da referência; no tablet, 2 colunas; no celular, 1 coluna.
  Sem rolagem horizontal.
- HTML semântico (`section`, `h2`, `h3`, `article`, `a`), foco visível no teclado, contraste AA,
  `loading="lazy"` nas imagens e animações desligadas com `prefers-reduced-motion`.

### 5. Formato da resposta
1. Em até 5 linhas, descreva o que você identificou na seção de referência.
2. O código completo da seção, sem trechos omitidos.
3. No final, diga onde trocar títulos, descrições, imagens e links dos cases.
