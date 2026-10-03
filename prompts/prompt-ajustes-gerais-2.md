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
2. **Imagem cortada:** a imagem não pode cortar a altura. Defina o espaço da imagem com
   **proporção fixa de 9:11 (`aspect-ratio: 9 / 11`)**, ocupando toda a altura do retângulo dos
   3 boxes, com `width: 100%; height: 100%; object-fit: cover;`. As imagens serão exportadas em
   **900 × 1100 px** (ou 1800 × 2200 px para telas retina), na mesma proporção, para encaixar sem
   cortes. Me diga qual é o tamanho final em px que o espaço da imagem ocupa no desktop (1440px),
   para eu conferir.
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
