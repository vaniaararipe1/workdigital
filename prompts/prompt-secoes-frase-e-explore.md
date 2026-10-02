# Prompt — Seção de frase + seção "Explore / Transformação digital"

Referências na home de https://www.auros.global/:
- seção com a frase "We’re shaping the next generation of decentralized finance.";
- seção **NETWORK / GLOBAL presence**.

Anexe um print de cada uma (e uma gravação, se tiverem animação).

## Alternativas (troque no prompt, se preferir)
**Descrição**
1. Transformação digital é colocar a sua empresa onde o cliente já está. Organizamos sua presença online, do site às redes sociais, com processos simples de acompanhar, para você atender melhor, vender mais e decidir com base em números reais. **(usada no prompt)**
2. Não é só ter um site. É fazer o cliente encontrar, entender e escolher a sua empresa. Planejamos cada etapa da sua presença digital para que ela trabalhe pelo seu negócio todos os dias.

**Frase de impacto**
1. Quem não é encontrado, não é escolhido. **(usada no prompt)**
2. Seu próximo cliente já está online. Sua empresa precisa estar também.
3. O mercado mudou. Sua empresa pode mudar junto.

---

## PROMPT (copie daqui para baixo)

Crie as **duas próximas seções da home**, logo abaixo da seção "WORKS", seguindo a mesma
estrutura, layout, tipografia, espaçamentos e animações das seções correspondentes da Auros
(prints em anexo), com as **cores da Work Digital** e o mesmo padrão das seções anteriores.

### Seção 1 — Frase de destaque
Mesma seção da referência que tem o texto "We’re shaping the next generation of decentralized
finance.". Troque o texto por:

**Onde você está quando seu cliente NÃO procura por você?**

- Mantenha o mesmo tamanho, peso, alinhamento e animação de entrada do texto da referência.
- Dê destaque ao "NÃO" (ex.: o gradiente de texto da marca ou a cor de destaque da Work), mantendo
  o restante da frase no estilo da referência.
- Use `id="wd-statement"` e classes com prefixo `wd-statement-`.

### Seção 2 — Explore / Transformação digital
Mesma seção da referência **NETWORK / GLOBAL presence**, com estes textos:

| Na referência | Na Work Digital |
|---|---|
| **NETWORK** | **EXPLORE** |
| **GLOBAL presence** | **Transformação digital** |
| Texto descritivo | Transformação digital é colocar a sua empresa onde o cliente já está. Organizamos sua presença online, do site às redes sociais, com processos simples de acompanhar, para você atender melhor, vender mais e decidir com base em números reais. |
| CTA | **SOLICITE PROPOSTA** (link `#contato`) |
| "Helping institutions operate with confidence." | **Quem não é encontrado, não é escolhido.** |

- Mantenha a mesma posição, estilo e caixa (maiúsculas/minúsculas) de cada texto da referência.
- Se "NETWORK" ou "GLOBAL presence" tiverem gradiente de texto, use o mesmo gradiente das seções
  anteriores (como em "ACEITE O DESAFIO DO NOVO").
- O CTA usa o mesmo estilo e o mesmo hover do botão "SOLICITE UMA PROPOSTA" da seção
  "Aceite o desafio do novo".
- Se a referência tiver mapa, globo, ilustração ou animação de fundo, recrie o mesmo efeito com as
  cores da Work Digital, sem usar arquivos da Auros.
- Use `id="wd-transformacao"` e classes com prefixo `wd-transformacao-`.

### CSS (vale para as duas seções)
- `background: transparent`: o gradiente do site continua contínuo, sem fundo preto e sem faixas
  ou emendas entre as seções.
- Títulos com a mesma fonte das seções anteriores; textos descritivos em **Nunito**, no mesmo
  tamanho dos descritivos já usados.
- Responsivo (desktop, tablet e celular), sem rolagem horizontal; foco visível no teclado;
  animações desligadas com `prefers-reduced-motion`.

Devolva só o código dessas duas seções (HTML + CSS + JS, se precisar), pronto para colar abaixo
de `#wd-works`.
