# CSS do globo — seção Transformação digital (`#wd-transformacao`)

Recriado a partir dos prints da referência (Auros), nas cores da Work Digital.
Prévia: `preview-globo-transformacao.png` (os pontos da prévia são só um padrão de teste).

## PROMPT (copie daqui para baixo)

Substitua a iluminação do card e do globo da seção "Transformação digital" (`#wd-transformacao`)
por este HTML e CSS. **Não remova o mapa de pontos com os países/continentes que já existe:**
coloque-o dentro de `.wd-tr-dots`, no lugar do comentário. O `background-image` e o
`background-size` de `.wd-tr-dots` são só um padrão de teste: apague essas duas linhas e use o mapa
atual. Mantenha textos, botão e responsivo como estão. Remova o CSS antigo do card, do globo e do brilho, para não haver
conflito.

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
  max-width:1360px; height:600px; margin:0 auto; border-radius:16px;
  background:
    radial-gradient(55% 75% at 78% 50%, rgba(214,200,255,.55) 0%, rgba(214,200,255,0) 70%),
    radial-gradient(45% 55% at 38% 105%, rgba(226,214,255,.38) 0%, rgba(226,214,255,0) 70%),
    linear-gradient(90deg, #24104f 0%, #34187a 35%, #5a3db8 62%, #a993f5 100%);
  box-shadow: 0 0 140px 10px rgba(124, 92, 255, .28);
}
.wd-tr-glow{
  position:absolute; z-index:0; pointer-events:none;
  top:50%; left:42%; width:70%; aspect-ratio:1; transform:translateY(-50%);
  border-radius:50%;
  background: radial-gradient(circle, rgba(238,230,255,.85) 0%, rgba(205,188,255,.45) 40%, rgba(205,188,255,0) 70%);
  filter: blur(70px);
}
.wd-tr-globe{
  position:absolute; z-index:1; pointer-events:none;
  top:50%; left:54%; height:150%; aspect-ratio:1; transform:translateY(-50%);
  border-radius:50%;
  background:
    radial-gradient(circle at 4% 50%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 18%),
    radial-gradient(circle at 62% 82%, rgba(252,250,255,.95) 0%, rgba(252,250,255,0) 42%),
    radial-gradient(circle at 48% 22%, rgba(196,176,255,.75) 0%, rgba(196,176,255,0) 55%),
    radial-gradient(circle at 55% 50%, #e9e1ff 0%, #ddd0ff 55%, #cfbdff 100%);
  box-shadow:
    inset 24px 0 40px rgba(255,255,255,.85),
    inset 70px 0 120px rgba(255,255,255,.45),
    0 0 40px 8px rgba(245,240,255,.9),
    0 0 120px 30px rgba(214,198,255,.65),
    0 0 240px 60px rgba(170,145,255,.35);
}
.wd-tr-dots{
  position:absolute; inset:0; border-radius:50%;
  /* mantenha aqui o mapa de pontos que já existe; este padrão é só para teste */
  background-image: radial-gradient(circle, rgba(104,88,160,.72) 1.6px, transparent 2px);
  background-size: 8px 8px;
  -webkit-mask-image: radial-gradient(ellipse 75% 85% at 66% 50%, #000 50%, transparent 82%);
          mask-image: radial-gradient(ellipse 75% 85% at 66% 50%, #000 50%, transparent 82%);
}
.wd-tr-content{position:relative; z-index:2; padding:0 80px; height:100%; display:flex; flex-direction:column; justify-content:center; color:#fff; max-width:560px}
```

No celular (até 768px), reduza o globo (`height: 90%`, `left: 40%`), deixe o texto por cima com
o fundo do card escurecido atrás dele, e mantenha tudo sem rolagem horizontal.
