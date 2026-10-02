# Prompt — Correção 2 das partículas (velocidade e tamanho)

Anexe uma gravação de tela de 5 a 10 segundos das partículas da referência (Auros) e um print
de como estão hoje no site da Work.

## PROMPT (copie daqui para baixo)

Ajuste a animação das partículas para ficar igual à referência (gravação em anexo). Faça
**somente** estas correções e devolva o código atualizado das partes alteradas.

**1. Velocidade**
As partículas não estão se movendo na mesma velocidade da referência. Compare com a gravação e
ajuste a velocidade de deslocamento, a aceleração/suavização e a frequência de qualquer
oscilação, para que o ritmo fique igual ao da Auros.
- Baseie o movimento no tempo real (delta time entre frames), não na quantidade de frames, para
  a velocidade ser a mesma em monitores de 60Hz, 120Hz e 144Hz.
- Deixe a velocidade em uma variável no topo do script (ex.: `const PARTICLE_SPEED = ...`) para
  eu poder ajustar depois.

**2. Tamanho igual à referência**
Deixe a área das partículas **do mesmo tamanho da referência**. Isso substitui o pedido anterior
de reduzir a altura pela metade. Ajuste também o tamanho de cada partícula, a quantidade e o
espaçamento entre elas para ficarem iguais à referência.
- O `canvas` acompanha o novo tamanho no carregamento e no `resize`, considerando
  `devicePixelRatio`, sem partículas esticadas ou borradas.
- Mantenha o fundo em gradiente contínuo do site, sem faixas ou emendas com as seções vizinhas.

Ao final, informe em uma linha os valores antigos e novos de velocidade, tamanho da área,
tamanho das partículas e quantidade.
