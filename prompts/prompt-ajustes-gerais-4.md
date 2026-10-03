# Prompt — Ajustes gerais 4

Prévia da nova iluminação do card: `preview-globo-transformacao-v3.png`.

## PROMPT (copie daqui para baixo)

Faça os ajustes abaixo. Alguns itens já foram pedidos e **não foram aplicados**. Antes de corrigir
esses itens, encontre no CSS **todas as regras que estão sobrescrevendo** (cor, largura, fundo,
`::before`/`::after`, estilos inline, regras de media query ou de outras seções) e me diga em uma
linha qual regra estava impedindo a mudança. Altere **somente** o que está listado e devolva o
código atualizado de cada parte.

### GERAL
1. **"Criação de sites profissionais" em 2 linhas e maior:**
   - Quebra fixa em 2 linhas no desktop: `Criação de sites<br>profissionais`.
   - Mesmo tamanho de fonte da frase "Onde você está quando seu cliente NÃO procura por você?".
     Use a **mesma variável** nos dois, por exemplo:
     ```css
     :root{ --wd-display-size: clamp(40px, 6vw, 88px); }
     .wd-hero-title, .wd-statement-text{ font-size: var(--wd-display-size); line-height: 1.05; }
     ```
     (use o valor que a frase "Onde você está..." já tem hoje).
   - Garanta que **não quebre em 3 linhas** no desktop: o container do título precisa ter largura
     suficiente (`max-width: none` ou largura maior), e `white-space: nowrap` em cada linha se
     precisar. No celular, pode quebrar naturalmente.
2. **Largura do dropdown do seletor de idiomas (ainda não resolvido):** o dropdown herdou a
   largura do dropdown de SOLUÇÕES. Mantenha o mesmo estilo visual, mas com **largura própria**:
   ```css
   .wd-lang{ width:auto; min-width:0; }
   .wd-lang-menu{ width:max-content; min-width:120px; max-width:160px; }
   ```
   (use os nomes das classes que existem no código e remova qualquer `width`/`min-width` herdado
   do dropdown de SOLUÇÕES).
3. **Degradê dos uptitles (ainda não aparece):** liste todos os uptitles da página (seletor e
   texto de cada um) e confirme que todos usam a classe `.wd-uptitle`. O degradê só funciona se o
   elemento tiver o fundo em degradê **e** o texto transparente; qualquer `color`,
   `-webkit-text-fill-color`, `background` ou animação de cor em outra regra anula o efeito.
   Use:
   ```css
   .wd-uptitle{
     display:inline-block;
     background: linear-gradient(90deg, #FFFFFF 0%, #EDE4FF 45%, #F7C9EC 100%) !important;
     -webkit-background-clip: text !important; background-clip: text !important;
     -webkit-text-fill-color: transparent !important; color: transparent !important;
   }
   ```

### SOLUÇÕES WORK (`#wd-explore`)
1. **Inverta a transparência do retângulo das fotos:** hoje a parte transparente está do lado
   esquerdo. Inverta o degradê do fundo desse retângulo para que a parte **transparente fique do
   lado direito** (sólido/translúcido à esquerda → transparente à direita).
2. **Hover dos boxes com degradê:** ao passar o mouse, o box ganha um degradê suave nas cores da
   Work, com transição. Como `background` em degradê não anima, use um pseudo-elemento:
   ```css
   .wd-explore-card{ position:relative; isolation:isolate; }
   .wd-explore-card::before{
     content:""; position:absolute; inset:0; border-radius:inherit; z-index:-1;
     background: linear-gradient(135deg, rgba(124,92,255,.38) 0%, rgba(183,155,255,.22) 45%, rgba(255,143,203,.20) 100%);
     opacity:0; transition: opacity .45s cubic-bezier(.22,1,.36,1);
   }
   .wd-explore-card:hover::before, .wd-explore-card.is-active::before{ opacity:1; }
   .wd-explore-card:hover{ box-shadow: 0 0 0 1px rgba(214,198,255,.35), 0 20px 60px -20px rgba(124,92,255,.55); }
   ```
   (use a classe que já existe nos boxes; mantenha a lógica do 1º box ativo só no carregamento).

### TRANSFORMAÇÃO DIGITAL (`#wd-transformacao`)
1. **Iluminação do fundo do card:** as cores não precisam ser as da referência, mas a iluminação
   precisa seguir o mesmo estilo: o lado do texto em um roxo médio (não quase preto), clareando em
   direção ao globo, uma área grande de luz espalhada em volta do globo e uma luz clara e suave no
   canto inferior esquerdo. Substitua **apenas** o `background` de `.wd-tr-card` por este, e remova
   qualquer outro fundo, overlay ou `::before`/`::after` do card que esteja escurecendo:
   ```css
   .wd-tr-card{
     background:
       radial-gradient(50% 70% at 72% 55%, rgba(226,216,255,.55) 0%, rgba(190,170,255,.25) 45%, rgba(190,170,255,0) 75%),
       radial-gradient(60% 55% at 22% 108%, rgba(240,228,246,.55) 0%, rgba(220,205,240,.22) 45%, rgba(220,205,240,0) 75%),
       radial-gradient(55% 70% at 8% 10%, rgba(30,14,70,.45) 0%, rgba(30,14,70,0) 70%),
       linear-gradient(100deg, #3a1d86 0%, #4526a0 28%, #5a3bbd 52%, #8d76e8 76%, #cfc2ff 100%);
   }
   ```

Ao final, liste em uma linha por item o que foi alterado.
