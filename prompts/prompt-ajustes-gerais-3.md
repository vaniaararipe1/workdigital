# Prompt — Ajustes gerais 3

Prévia do novo globo: `preview-globo-transformacao-v2.png` (os pontos da prévia são só teste).

## PROMPT (copie daqui para baixo)

Faça os ajustes abaixo. Altere **somente** o que está listado e devolva o código atualizado de
cada parte, organizado pelos mesmos títulos.

### GERAL
1. **Fonte dos CTAs:** todos os botões/CTAs do site (menu, seções, rodapé, botão flutuante) passam
   a usar **Space Grotesk** (Google Fonts), com o mesmo peso e `letter-spacing` em todos.
   `<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&display=swap" rel="stylesheet">`
2. **Títulos das seções padronizados:** todos os títulos principais das seções (h2) devem ter o
   **mesmo tamanho, peso, `line-height` e `letter-spacing`**. Crie uma classe única (ex.:
   `.wd-section-title`) e aplique em todas as seções.

### MENU
1. **Largura do menu:** o conteúdo do menu deve ter **a mesma largura máxima e as mesmas margens
   laterais do retângulo da seção Soluções Work**, para o logo e o CTA ficarem alinhados com as
   bordas desse retângulo. Use a mesma variável/`max-width` nos dois.
2. **Seletor de idiomas mais estreito:** reduza a largura (largura automática pelo conteúdo, com
   padding lateral de cerca de 10px, ícone do globo + "PT" + seta).
3. **Corrija o texto do menu:** "Work" → **"Works"**.

### HEADER
1. **Degradê do h1 e dos uptitles mais suave:** o degradê atual ficou forte demais. Na referência,
   o degradê é sutil: quase branco, com um leve tom lilás/rosado no final. Use este degradê no h1
   "Criação de sites profissionais" e em **todos os uptitles**, substituindo o anterior:
   ```css
   .wd-uptitle, .wd-hero-highlight{
     background: linear-gradient(90deg, #FFFFFF 0%, #EDE4FF 45%, #F7C9EC 100%);
     -webkit-background-clip: text; background-clip: text;
     -webkit-text-fill-color: transparent; color: transparent;
   }
   ```
   (use os nomes das classes que já existem no código).
2. **Aumente bastante** o tamanho da fonte de "Criação de sites profissionais" (cerca de 30% a 40%
   maior que o atual no desktop, usando `clamp()` para reduzir no celular sem quebrar o layout).

### SOLUÇÕES WORK (`#wd-explore`)
1. O retângulo da direita (o da imagem) deve ter **a mesma transparência/fundo do retângulo da
   esquerda** (o dos 3 boxes) e **sem borda**.

### TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)
A iluminação do card e as bordas do globo ainda estão diferentes da referência. **Substitua todo o
CSS do card, do brilho e do globo** por este (remova o CSS antigo dessas partes, incluindo máscaras,
`box-shadow` e `filter: blur` antigos, para não haver conflito). O brilho agora é feito só com
gradientes radiais, o que deixa a luz mais fluida e a borda do globo suave, sem linhas retas.
**Não remova o mapa de pontos com os países:** ele continua dentro de `.wd-tr-dots`; apague apenas
o `background-image` e o `background-size` de teste dessa classe.

```html
<div class="wd-tr-card">
  <div class="wd-tr-glow"></div>
  <div class="wd-tr-globe"><div class="wd-tr-dots"><!-- mapa de pontos atual --></div></div>
  <div class="wd-tr-content"><!-- EXPLORE, título, descrição e botão atuais --></div>
</div>
```

```css
.wd-tr-card{
  position:relative; overflow:hidden; isolation:isolate;
  max-width:1360px; height:600px; margin:0 auto; border-radius:16px; border:0;
  background:
    radial-gradient(60% 90% at 80% 50%, rgba(222,210,255,.60) 0%, rgba(190,170,255,.28) 38%, rgba(190,170,255,0) 72%),
    radial-gradient(55% 60% at 30% 112%, rgba(232,222,255,.42) 0%, rgba(232,222,255,0) 72%),
    radial-gradient(70% 90% at 0% 0%, rgba(18,8,44,.55) 0%, rgba(18,8,44,0) 70%),
    linear-gradient(100deg, #1f0e46 0%, #2d1569 30%, #4a2fa3 58%, #8f78e6 82%, #c9bbff 100%);
  box-shadow: 0 0 160px 20px rgba(124, 92, 255, .25);
}
.wd-tr-glow{
  position:absolute; z-index:0; pointer-events:none;
  top:50%; left:54%; height:260%; aspect-ratio:1; transform:translate(-21%, -50%);
  border-radius:50%;
  background: radial-gradient(closest-side,
    rgba(250,247,255,1) 52%, rgba(232,222,255,.85) 58%, rgba(205,188,255,.5) 68%,
    rgba(170,145,255,.18) 82%, rgba(170,145,255,0) 100%);
}
.wd-tr-globe{
  position:absolute; z-index:1; pointer-events:none;
  top:50%; left:54%; height:150%; aspect-ratio:1; transform:translateY(-50%);
  border-radius:50%;
  background:
    radial-gradient(closest-side, rgba(255,255,255,0) 80%, rgba(255,255,255,.55) 93%, rgba(250,247,255,1) 100%),
    radial-gradient(circle at 6% 50%, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 24%),
    radial-gradient(circle at 62% 82%, rgba(252,250,255,.95) 0%, rgba(252,250,255,0) 42%),
    radial-gradient(circle at 48% 22%, rgba(196,176,255,.7) 0%, rgba(196,176,255,0) 55%),
    radial-gradient(circle at 55% 50%, #ebe4ff 0%, #ddd0ff 55%, #cfbdff 100%);
}
.wd-tr-dots{
  position:absolute; inset:0; border-radius:50%;
  background-image: radial-gradient(circle, rgba(104,88,160,.72) 1.6px, transparent 2px);
  background-size: 8px 8px;
  -webkit-mask-image: radial-gradient(ellipse 75% 85% at 66% 50%, #000 50%, transparent 82%);
          mask-image: radial-gradient(ellipse 75% 85% at 66% 50%, #000 50%, transparent 82%);
}
.wd-tr-content{position:relative; z-index:2; padding:0 80px; height:100%; display:flex; flex-direction:column; justify-content:center; color:#fff; max-width:560px}
```

### RODAPÉ
1. Ordem das redes sociais: **LinkedIn / Instagram / Facebook**.

Ao final, liste em uma linha por item o que foi alterado.
