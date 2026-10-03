# Prompt — Ajustes gerais 2

## PROMPT (copie daqui para baixo)

Faça os ajustes abaixo. Altere **somente** o que está listado e devolva o código atualizado de
cada parte, organizado pelos mesmos títulos.

### GERAL
1. **Degradê dos uptitles não foi aplicado.** Ele só aparece no "EXPLORE". Aplique em **todos os
   uptitles do site** e deixe o degradê **mais forte e saturado** que o atual. Use uma única classe
   e confira cada seção para garantir que todos os uptitles usam essa classe:
   ```css
   .wd-uptitle{
     background: linear-gradient(90deg, #B79BFF 0%, #E58BFF 50%, #FF8FCB 100%);
     -webkit-background-clip: text; background-clip: text;
     -webkit-text-fill-color: transparent; color: transparent;
   }
   ```
   Se algum uptitle tiver `color` ou `-webkit-text-fill-color` definido em outra regra, remova,
   para não sobrescrever o degradê.
2. **Botão flutuante do WhatsApp:** remova o contorno (stroke) preto da bolinha de notificação
   (retire `border`, `outline` ou `box-shadow` escuros dela).
3. **Botão flutuante do WhatsApp — links:** cada botão/opção dentro do widget deve abrir o WhatsApp
   com o seu próprio link (`https://wa.me/NUMERO?text=MENSAGEM`, com a mensagem codificada por
   `encodeURIComponent`), em nova aba. Deixe número e mensagem de cada botão em variáveis no topo
   do código, com valores provisórios, para eu trocar depois.

### MENU
1. O **dropdown do seletor de idiomas** deve ser **igual ao dropdown de SOLUÇÕES** (mesmo
   componente, fundo, borda, sombra, fonte, espaçamento, animação de abertura e hover). Troque o
   `<select>` nativo por esse dropdown, mantendo o ícone de globo ao lado.
2. **Layout do menu:** logo à esquerda, **links do menu centralizados** e **seletor de idiomas +
   CTA à direita**. Use `display: grid; grid-template-columns: 1fr auto 1fr;`, com o grupo da
   direita alinhado com `justify-self: end`.

### HEADER
1. O texto **"Criação de sites profissionais"** ainda não está com o degradê. Aplique a mesma
   classe `.wd-uptitle` (ou o mesmo degradê) nele e remova a cor que está sobrescrevendo.

### SOLUÇÕES WORK (`#wd-explore`)
1. **Imagem dentro de um retângulo:** coloque cada imagem dentro de um retângulo com o mesmo
   estilo dos boxes (mesmo fundo, borda, `border-radius` e espaçamento interno), para combinar com
   eles.
2. **Imagem cortada:** as imagens já estão em **900 × 1100 px (proporção 9:11)** e mesmo assim
   aparecem cortadas. Isso acontece porque o espaço da imagem não tem a proporção 9:11: ele estica
   para a altura dos boxes e a largura da coluna, e o `object-fit: cover` corta o que sobra.
   - Primeiro, me diga a largura e a altura reais (em px, no desktop 1440px) do espaço da imagem,
     **descontando padding e borda do retângulo**, e explique o que está causando o corte (proporção
     do container, `transform: scale` no hover, `padding`, `overflow: hidden` de um elemento pai etc.).
   - Corrija fazendo o espaço da imagem ter **exatamente a proporção 9:11**, com a **largura
     calculada a partir da altura** dos boxes, para a imagem encaixar inteira:
     ```css
     .wd-explore-grid{ display:grid; grid-template-columns: 1fr auto; align-items: stretch; }
     .wd-explore-media{ height:100%; aspect-ratio: 9 / 11; width:auto; box-sizing:border-box; }
     .wd-explore-media img{ display:block; width:100%; height:100%; object-fit: cover; }
     ```
     (ajuste os nomes das classes para os que já existem no código). O retângulo em volta da imagem
     fica **fora** desse espaço (padding no elemento pai), para não alterar a proporção.
   - Se houver `transform: scale()` na imagem no hover, retire ou deixe no máximo `1.02`.
   - No tablet e no celular, a imagem vai para baixo dos boxes com `width:100%; height:auto;
     aspect-ratio: 9 / 11`.
3. **Partículas duplicadas:** existem duas camadas de partículas no fundo (uma animada e outra
   parada). **Remova a camada estática** e mantenha só a animada.

### TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)
1. **Borda do globo com blur:** na referência, a borda do globo é suave e desfocada, não uma linha
   nítida. Aplique o mesmo efeito, mantendo o brilho atual:
   ```css
   .wd-tr-globe{
     -webkit-mask-image: radial-gradient(closest-side, #000 93%, transparent 100%);
             mask-image: radial-gradient(closest-side, #000 93%, transparent 100%);
   }
   ```
   Se o brilho externo (`box-shadow`) for cortado pela máscara, mova esse brilho para a camada
   `.wd-tr-glow`, que fica atrás do globo, sem máscara.

Ao final, liste em uma linha por item o que foi alterado.
