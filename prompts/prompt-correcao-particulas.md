# Prompt — Correção da área das partículas

Use na mesma conversa do ChatGPT. Anexe um print mostrando a área das partículas como está hoje.

---

## PROMPT (copie daqui para baixo)

A área com o efeito de partículas está ocupando espaço vertical demais na página. Faça
**somente** esta correção, sem mexer no resto, e devolva o código atualizado das partes alteradas.

**Reduzir a altura da área das partículas para cerca de metade**
- Diminua a altura do container das partículas (e do `canvas`) para **aproximadamente 50% da
  altura atual**. Exemplo: se hoje está com `100vh`, passe para cerca de `50vh`. Se for um valor
  fixo, como `800px`, passe para cerca de `400px`. Use `clamp()` para não ficar pequeno demais em
  telas baixas nem grande demais em telas altas (ex.: `height: clamp(280px, 50vh, 520px);`).
- Reduza junto os espaçamentos (`padding`/`margin`) acima e abaixo da área, para não sobrar um
  vazio no lugar do espaço retirado. A seção seguinte deve subir junto.
- O `canvas` precisa acompanhar a nova altura: recalcule `canvas.width`/`canvas.height` a partir
  do tamanho real do container (considerando `devicePixelRatio`) no carregamento e no `resize`,
  para as partículas não ficarem esticadas, borradas ou cortadas.
- Ajuste a **quantidade de partículas** proporcionalmente à nova área (cerca de metade), para a
  densidade visual continuar a mesma, e garanta que elas fiquem dentro dos novos limites
  (sem nascer nem "quicar" fora da área visível).
- Se houver texto, título ou botão sobre as partículas, mantenha esses elementos centralizados e
  inteiros na nova altura, sem cortes nem sobreposição com a seção seguinte.
- Mantenha o fundo em gradiente contínuo do site: a redução não pode criar faixas, emendas ou
  cortes de cor entre esta área e as seções vizinhas.
- No celular, a área também fica com cerca de metade da altura atual, sem rolagem horizontal.

Ao final, informe em uma linha a altura antiga e a nova (desktop e celular) e a quantidade de
partículas antes e depois.
