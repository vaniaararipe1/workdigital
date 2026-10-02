# Prompt — Seção "Insights" (blog) da home

Referência: seção **INSIGHTS** da home de https://www.auros.global/ (e a frase que vem antes dela).
Anexe um print da frase + da seção INSIGHTS da Auros.

Se o ChatGPT não conseguir abrir o site atual (https://workdigital.art.br/), preencha a tabela do
item 3 com os artigos (título, resumo, data, imagem e link).

## PROMPT (copie daqui para baixo)

Crie as **próximas partes da home**, logo abaixo da seção "Transformação digital", **visualmente
iguais à referência da Auros** (print em anexo): mesma estrutura, grade, proporções, tipografia,
espaçamentos, hover e animações. Use as cores da Work Digital e o mesmo padrão das seções
anteriores.

**1. Frase antes da seção**
Na referência, antes da seção INSIGHTS existe uma frase em destaque. Coloque, no mesmo lugar e no
mesmo estilo:

**Site, blog e landing page trabalhando antes do cliente procurar.**

Use `id="wd-statement-2"` e o mesmo estilo de animação da frase "Onde você está quando seu
cliente NÃO procura por você?", se a referência também for animada.

**2. Seção Insights → Blog**

| Na referência | Na Work Digital |
|---|---|
| **INSIGHTS** | **BLOG** |
| Título da seção | **Insights e perspectivas** |
| Texto descritivo (se houver) | Explore ideias, tendências do digital e o que aprendemos criando sites, blogs e landing pages. |
| Botão/link para todos os artigos (se houver) | **VER TODOS OS ARTIGOS** (link para o blog em https://workdigital.art.br/) |

- "BLOG" no mesmo estilo de "INSIGHTS"; "Insights e perspectivas" com o mesmo gradiente de texto
  usado nos títulos das seções anteriores, se o título da referência tiver gradiente.

**3. Artigos**
Use os artigos que aparecem hoje na home do site atual da Work Digital, na área do blog
("Visite o blog"): https://workdigital.art.br/

Abra o site, copie os dados reais de cada artigo (não invente títulos nem resumos) e pegue a **mesma quantidade de artigos que a referência mostra**, os mais recentes, com título,
imagem de capa, data, categoria (se houver) e link para o artigo original. Se não conseguir
acessar o site, use a tabela abaixo:

| # | Título | Resumo | Data | Categoria | Imagem | Link |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

- Cada card de artigo deve ficar **igual ao card da referência**: mesma posição da imagem,
  título, data/categoria e seta/link, mesmo arredondamento, borda e hover.
- Imagens com proporção fixa e `object-fit: cover`, `loading="lazy"` e `alt` com o título do artigo.
- Os links abrem o artigo no blog da Work.
- Deixe os artigos em um array JS ou em blocos HTML marcados com comentários (`<!-- ARTIGO 1 -->`),
  fáceis de editar.

**4. CSS**
- `background: transparent`: o gradiente do site continua contínuo, sem fundo preto e sem faixas
  entre as seções.
- Títulos na mesma fonte das seções anteriores; textos de apoio e resumos em **Nunito**, no
  mesmo tamanho dos descritivos já usados.
- Responsivo: mesma grade da referência no desktop, 2 colunas no tablet e 1 no celular (ou
  carrossel com arraste, se a referência usar carrossel), sem rolagem horizontal da página.
- Classes com prefixo `wd-blog-` e `id="wd-blog"` na seção. Foco visível no teclado e animações
  desligadas com `prefers-reduced-motion`.

Devolva só o código dessas duas partes (HTML + CSS + JS, se precisar), pronto para colar abaixo
de `#wd-transformacao`.
