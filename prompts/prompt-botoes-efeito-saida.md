# Prompt — Efeito dos botões ao tirar o mouse

Grave a tela (5 a 10 segundos) passando o mouse sobre um botão da Auros e tirando, devagar,
2 ou 3 vezes. Anexe a gravação junto com o prompt.

## PROMPT (copie daqui para baixo)

Nos botões da referência (Auros), quando o mouse **sai** de cima do botão acontece um efeito de
saída bonito e suave (veja a gravação em anexo). Nos nossos botões isso não acontece: o efeito
some de uma vez ou só volta ao normal invertendo o hover. Preciso do **mesmo efeito de saída**.

**1. Analise antes de codar**
Assista à gravação e descreva em até 5 linhas o que acontece no botão da referência:
- na **entrada** do mouse (o que muda, de onde para onde, em quanto tempo);
- na **saída** do mouse (o preenchimento continua andando para o outro lado, recolhe, desbota?
  a seta/ícone se move? há atraso? qual a duração e a curva de aceleração?).

**2. Implemente entrada e saída separadas**
- A saída **não pode ser só o hover ao contrário**. Use transições diferentes para entrar e sair:
  defina a transição de saída na regra base do botão e a de entrada no `:hover`/`:focus-visible`,
  ou use uma classe (ex.: `.is-leaving`) aplicada no `mouseleave` e removida no fim da animação
  (`animationend`/`transitionend`).
- Se o efeito for um preenchimento que "atravessa" o botão (entra por um lado e sai pelo outro),
  use um pseudo-elemento (`::before`) com `transform: scaleX()` e troque o `transform-origin`
  entre a entrada e a saída.
- Se a seta/ícone sair por um lado e voltar pelo outro, faça com duas cópias da seta ou com
  `@keyframes`, como na referência.
- Copie a duração e a curva de aceleração da referência (ex.: `cubic-bezier(0.22, 1, 0.36, 1)`
  entre 0.4s e 0.7s, ajustando ao que aparece na gravação).
- Se o mouse entrar de novo no meio da saída, a animação não pode "pular" nem travar.

**3. Aplique em todos os botões do site**
- Crie o efeito em uma **classe única e reutilizável** (ex.: `.wd-btn`) e aplique em todos os CTAs:
  "SOLICITE UMA PROPOSTA", "SOLICITE PROPOSTA", "VER TODOS OS ARTIGOS", "ENTRE EM CONTATO" e o
  botão do header, se houver.
- Mantenha as cores atuais da Work Digital em cada botão.
- O mesmo efeito vale para o foco do teclado (`:focus-visible` e saída do foco).
- Com `prefers-reduced-motion`, troque a animação por uma mudança simples de cor, sem movimento.

Devolva o CSS (e o JS, se precisar) do botão e indique em quais elementos a classe foi aplicada.
