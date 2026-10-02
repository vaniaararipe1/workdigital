# Prompt — Página de Portfolio "Work" da Work Digital

Referência de estrutura: https://www.otherlife.xyz/work (agência criativa Otherlife).

> **Dica:** antes de colar o prompt no ChatGPT, anexe 2 ou 3 prints da página de
> referência (topo, grid de projetos, rodapé). Assim o modelo segue o layout com mais precisão.
> Substitua tudo que estiver entre `[colchetes]`.

---

## PROMPT (copie daqui para baixo)

Você é um desenvolvedor front-end sênior e diretor de arte de uma agência digital premiada
(nível Awwwards / FWA). Crie a página **"Work" (portfolio de cases)** da agência **Work Digital**,
com a mesma estrutura e linguagem visual da página https://www.otherlife.xyz/work, mas com
identidade, textos e projetos da Work Digital. Não copie textos, logos nem imagens da Otherlife:
replique só a **arquitetura da página, o ritmo visual e as interações**.

### 1. Contexto da marca
- **Nome:** Work Digital
- **O que fazemos:** [ex.: agência de branding, sites, conteúdo e performance digital]
- **Posicionamento em uma frase:** [ex.: "Construímos marcas e experiências digitais que geram resultado."]
- **Cidade/país:** [ex.: Brasil]
- **Tom de voz:** confiante, direto, contemporâneo, frases curtas, sem jargão.
- **Idioma da página:** português do Brasil (labels de navegação podem ficar em inglês, como "Work", se fizer sentido para a marca).
- **Cores da marca:** [cor principal] / [cor de destaque]. Se não houver, use fundo quase preto (#0B0B0C), texto off-white (#F2F0EB) e uma cor de destaque vibrante [ex.: #3D5AFE].
- **Tipografia:** sans grotesca de display em tamanhos muito grandes (ex.: "Inter Tight", "Space Grotesk" ou "Neue Montreal"-like via Google Fonts) + uma mono pequena para metadados (ex.: "JetBrains Mono" / "IBM Plex Mono").

### 2. Estrutura da página (de cima para baixo)

**2.1 Header fixo (sticky), minimalista**
- Logo/wordmark "Work Digital" à esquerda.
- Menu à direita: **Work** (ativo), **Agência**, **Serviços**, **Contato** + botão CTA "Vamos conversar".
- Header transparente sobre o hero que ganha fundo sólido/blur ao rolar; some ao rolar para baixo e reaparece ao rolar para cima.
- No mobile: menu hambúrguer que abre um overlay em tela cheia com links em tipografia gigante.

**2.2 Hero da página Work**
- Título enorme ocupando quase a largura toda, ex.: **"Work"** ou **"Trabalhos selecionados"**, com contador de projetos sobrescrito (ex.: "(12)").
- Subtítulo curto (1–2 linhas): [ex.: "Uma seleção de marcas, sites e campanhas que tiramos do papel."].
- Animação de entrada: letras/linhas sobem com máscara (reveal) em sequência.

**2.3 Barra de filtros por categoria**
- Filtros em linha (pills ou texto com sublinhado): **Todos · Branding · Website · Motion/3D · Conteúdo · Performance** [ajuste às categorias reais].
- Opcional: alternância de visualização **Grid / Lista** à direita.
- Ao filtrar, os cards saem/entram com fade + leve deslocamento (sem recarregar a página).

**2.4 Grid de projetos (núcleo da página)**
- Grid assimétrico/editorial: alternar cards grandes (largura total ou 2/3) com cards médios (1/2 ou 1/3), criando ritmo, não um grid uniforme.
- Cada card contém:
  - Mídia grande (imagem 16:10 ou 4:5) com cantos levemente arredondados; **no hover toca um vídeo curto em loop (mp4, mudo)** ou faz zoom suave (scale 1.03–1.05).
  - **Nome do cliente/projeto** em destaque.
  - Linha de metadados em fonte mono, pequena e em caixa alta: categorias/serviços (ex.: "BRANDING — WEBSITE — 3D") e ano.
  - Opcional: uma frase curta de descrição do case.
- Cursor customizado: ao passar sobre um card, o cursor vira um círculo com o texto "Ver case" (ou "View") que segue o mouse com easing.
- Cards aparecem com reveal ao entrar na viewport (fade + translateY + clip-path).
- Cada card é um link para `/work/[slug-do-projeto]`.

**2.5 Visualização em Lista (se ativada)**
- Tabela/lista de linhas largas: Cliente | Serviços | Ano | seta →.
- No hover de cada linha, uma miniatura do projeto aparece flutuando e seguindo o cursor.

**2.6 Seção de prova social (opcional, entre o grid e o CTA)**
- Faixa com logos de clientes em marquee horizontal infinito (pausa no hover), em monocromático.
- Opcional: 3 números de impacto (ex.: "+120 projetos", "+8 anos", "+40 marcas").

**2.7 CTA final de grande impacto**
- Frase gigante tipo **"Tem um projeto em mente?"** / **"Vamos construir o próximo?"**
- Link/botão grande "Fale com a gente →" com animação de sublinhado ou seta que desliza no hover.
- E-mail de contato clicável: [contato@workdigital.com.br].

**2.8 Footer**
- Colunas: Navegação (Work, Agência, Serviços, Contato) · Redes sociais (Instagram, LinkedIn, Behance) · Contato/Endereço.
- Wordmark "Work Digital" gigante ocupando a largura inteira no rodapé.
- Linha final: © [ano] Work Digital · horário local da cidade ao vivo (ex.: "São Paulo 14:32") · link "Voltar ao topo".

### 3. Projetos (dados de exemplo)
Monte os cards a partir de um array JSON fácil de editar, assim:

```js
const projects = [
  { slug: "[cliente-1]", client: "[Cliente 1]", title: "[Nome do projeto]", services: ["Branding", "Website"], year: 2025, image: "/img/[cliente-1].jpg", video: "/video/[cliente-1].mp4", size: "large" },
  { slug: "[cliente-2]", client: "[Cliente 2]", title: "[Nome do projeto]", services: ["Motion", "3D"], year: 2025, image: "/img/[cliente-2].jpg", video: "", size: "medium" },
  // ... de 8 a 12 projetos, alternando size: "large" | "medium" | "small"
];
```
Enquanto não houver imagens reais, use placeholders de https://picsum.photos com a proporção certa.

### 4. Motion e interações (essencial para chegar no mesmo "feel")
- Scroll suave com **Lenis**.
- Animações com **GSAP + ScrollTrigger**: reveal de texto por linha (SplitText ou split manual), parallax leve nas imagens dos cards, transição de entrada da página.
- Easing padrão: `cubic-bezier(0.22, 1, 0.36, 1)`; durações de 0.6s a 1.2s.
- Cursor customizado em desktop (desativar em touch).
- Respeitar `prefers-reduced-motion`: desligar parallax, vídeos automáticos e scroll suave.

### 5. Requisitos técnicos
- Entregar **HTML + CSS + JavaScript puros em um único arquivo `work.html`** (bibliotecas via CDN: GSAP, ScrollTrigger, Lenis). [Alternativa: "Next.js 14 + Tailwind + Framer Motion, com componentes separados".]
- Mobile-first e totalmente responsivo (breakpoints: 390px, 768px, 1024px, 1440px). No mobile o grid vira uma coluna e o hover vira toque.
- Variáveis CSS para cores, fontes e espaçamentos (`:root`).
- HTML semântico (`header`, `main`, `section`, `article`, `footer`), `alt` em todas as imagens, foco visível no teclado, contraste AA.
- Performance: `loading="lazy"` nas imagens, vídeos com `preload="none"` que só carregam no hover/viewport, fontes com `display=swap`.
- SEO: `<title>Work — Work Digital</title>`, meta description, Open Graph.

### 6. Formato da resposta
1. Primeiro, um resumo curto da estrutura e das decisões de design (máx. 10 linhas).
2. Depois, o código completo, pronto para salvar e abrir no navegador, sem trechos omitidos ("..." não é permitido).
3. No final, uma lista de onde trocar textos, cores, projetos e mídias.

---

## Sugestões de follow-up (para enviar depois da primeira versão)
- "Agora crie o template da página interna de um case (`/work/[slug]`): hero com mídia em tela cheia, ficha técnica (cliente, ano, serviços), desafio / solução / resultados, galeria em grid editorial e 'Próximo projeto' em destaque no final."
- "Deixe o grid mais editorial: varie mais os tamanhos e adicione espaçamentos assimétricos."
- "Revise a versão mobile: menu overlay, tamanhos de fonte e área de toque dos filtros."
