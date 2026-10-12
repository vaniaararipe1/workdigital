# Critérios de pontuação

Este documento explica como cada nota do Diagnóstico Gratuito de Site é calculada.
Não existe nota "mágica": toda nota vem dos critérios abaixo, e cada critério aponta
para um dado coletado (que fica registrado em `dados.json`).

## Regras gerais

- Cada categoria recebe uma nota de **0 a 100**.
- Faixas usadas no relatório:
  - **80 a 100:** Bom
  - **50 a 79:** Precisa melhorar
  - **0 a 49:** Crítico
- Quatro tipos de item:
  - **Medido:** dado coletado por ferramenta. É o único tipo que entra na nota.
  - **Avaliação de especialista:** depende de julgamento, como prova social ou clareza da proposta de valor. Aparece no relatório com selo próprio, **nunca entra na nota** e vai para as notas internas para revisão.
  - **Não foi possível medir:** a coleta falhou (site bloqueou, página não abriu, API fora do ar). **Sai do cálculo**, e o relatório mostra quantos critérios foram realmente medidos (por exemplo, "7 de 8 critérios medidos").
  - **Não foi possível confirmar:** não encontramos o item, mas há sinal de que ele pode existir (script de formulário ou de WhatsApp, botão que pode abrir um pop-up, página de contato que não abriu, página que não terminou de carregar). **Sai do cálculo** e não afirma o problema.
- **Ausência só é afirmada como Medido** (por exemplo, "não há formulário" ou "não há WhatsApp") depois de: carregar cada página até o fim, visitar as páginas de contato e não encontrar nenhum sinal. Na dúvida, o item sai como "Não foi possível confirmar". Detalhes em "Como procuramos formulários e contato".
- Se nenhum critério de uma categoria puder ser medido, a nota aparece como "sem medição", e não como zero.

## Performance

**Nota = 70% da nota de performance do Lighthouse no celular + 30% da nota no computador.**

- A nota do Lighthouse (0 a 100) é calculada pelo próprio Google a partir de LCP, CLS, TBT, FCP e Speed Index.
- Se só um dos dispositivos for medido, a nota é a dele.
- O celular pesa mais porque a maior parte do tráfego de pequenos negócios vem do celular.

**Fontes, em ordem de preferência:**
1. **Google PageSpeed Insights (API v5).** É a mesma medição que o lead encontra se pesquisar, e traz dados de visitantes reais quando o site tem volume.
2. **Lighthouse local, versão 13.5.0.** Usado só se o PageSpeed falhar. O relatório informa a fonte de cada número.

**Cartões de métricas** (referência principal: celular):

| Métrica | Bom | Precisa melhorar | Ruim | Origem |
|---|---|---|---|---|
| Tempo até o conteúdo principal (LCP) | até 2,5 s | até 4 s | acima de 4 s | laboratório |
| Estabilidade visual (CLS) | até 0,1 | até 0,25 | acima de 0,25 | laboratório |
| Resposta ao toque (INP) | até 200 ms | até 500 ms | acima de 500 ms | **só dados reais** (Chrome UX Report); sem dados, aparece "não foi possível medir" |
| Peso da página | até 2 MB | até 4 MB | acima de 4 MB | laboratório |

**Oportunidades:** itens do Lighthouse com nota abaixo de 0,9 e economia estimada maior que zero, ordenados pela economia de tempo. Entram as 4 maiores. A prioridade segue a economia estimada:
- **alta:** 1 s ou mais;
- **média:** 0,3 s ou mais, ou pelo menos 500 KB;
- **baixa:** abaixo disso.

## Experiência e conversão

Média ponderada: **ok vale 100, atenção vale 50, problema vale 0.**

| Critério | Peso | Ok | Atenção | Problema |
|---|---|---|---|---|
| Chamada para ação na primeira tela, celular (390×844) | 3 | botão com verbo de ação visível sem rolar | só elementos clicáveis sem convite claro | nenhum botão de ação antes de rolar |
| Chamada para ação na primeira tela, computador (1366×768) | 2 | idem | idem | idem |
| WhatsApp ou telefone clicável | 3 | link `wa.me`/`api.whatsapp`/`tel:` na home do celular, visível na primeira tela ou fixo | existe, mas fora da primeira tela ou só em páginas internas | não existe em nenhuma página analisada |
| Formulário de contato | 2 | até 6 campos, todos com rótulo (ou formulário externo incorporado) | 7 a 9 campos, campos sem rótulo, ou nenhum formulário quando há WhatsApp | mais de 9 campos, ou nenhum formulário e nenhum contato direto |
| Site adaptado ao celular | 2 | viewport `width=device-width` e sem rolagem lateral | conteúdo mais largo que a tela | sem meta viewport |
| Botões e links fáceis de tocar | 1 | até 10% dos alvos menores que 24×24 px | até 30% | mais de 30% |
| Leitura confortável no celular | 1 | até 10% do texto abaixo de 12 px | até 40% | mais de 40% |

Ficam **fora da nota** por serem avaliação de especialista:
- **Prova social visível:** busca por palavras-chave e blocos de depoimentos.
- **Clareza da proposta de valor:** leitura do H1. Títulos genéricos, como "Bem-vindo", ou com até 2 palavras são sinalizados para revisão.

**Notas técnicas:**
- "Chamada para ação" é um link ou botão com aparência de botão (fundo ou borda e preenchimento) e texto com verbo de ação, como contato, orçamento, comprar, agendar ou WhatsApp.
- Botões de cookies, idioma, menu e links de acessibilidade são ignorados.
- Links no meio de parágrafos não contam como alvo de toque, seguindo a exceção da WCAG 2.5.8.

### Como procuramos formulários e contato

1. **Carregamento completo.** Cada página espera a rede ficar ociosa (até 15 s), é rolada até o fim para carregar o que é preguiçoso, espera mais 2,5 s e espera o DOM parar de mudar (até 8 s). A página conta como completa se a rede ficou ociosa ou o DOM ficou estável.
2. **O que conta como formulário:**
   - `<form>` com 2 ou mais campos, **inclusive escondido** (dentro de pop-up, painel ou gaveta fechada);
   - campos de contato montados por script sem `<form>`;
   - formulários e widgets de RD Station (`bricks-form`, `rd-form`, scripts `rdstation`), HubSpot, Typeform, Google Forms, Elementor, Contact Form 7, WPForms, Gravity Forms, Calendly, Jotform, Tally e Leadster, em DOM ou iframe;
   - link para formulário externo (Google Forms, Typeform, Calendly, Tally, Jotform);
   - formulário que aparece depois de clicar num botão de contato. A ferramenta clica em até 2 botões que não mudam de página (texto como "Fale conosco", "Pedir orçamento" ou `aria-haspopup=dialog`). Ela nunca preenche nem envia nada e fecha qualquer aba nova.
3. **Onde procuramos:** a página inicial, as páginas internas analisadas, os links de contato do menu e do rodapé (até 3), e os endereços padrão `/contato/` e `/fale-conosco/`.
4. **Etiquetas:**
   - formulário encontrado: **Medido**, dizendo em qual página e como (visível, em pop-up, depois de um clique, de uma ferramenta incorporada);
   - nada encontrado, mas com script de formulário, botão não testado, página de contato inacessível ou página que não terminou de carregar: **Não foi possível confirmar**;
   - nada encontrado e nenhum sinal, com todas as buscas feitas: **Medido** (ausência).
5. **WhatsApp e botão de ação** seguem a mesma regra. Widget de WhatsApp sem link legível (Joinchat, Click to Chat, GetButton, número no código) e página inicial que não terminou de carregar levam a "Não foi possível confirmar".

## SEO e visibilidade

Mesma regra: ok vale 100, atenção vale 50, problema vale 0, média ponderada. A análise usa a home e até 4 páginas internas.

| Critério | Peso | Ok | Atenção | Problema |
|---|---|---|---|---|
| Páginas liberadas para o Google (sem `noindex`) | 3 | nenhuma com noindex | (não se aplica) | alguma página com noindex |
| Título das páginas | 2 | todas com título de 10 a 65 caracteres | algum fora do tamanho | alguma sem título |
| Títulos repetidos entre páginas | 1,5 | todos diferentes | (não se aplica) | 2 ou mais iguais |
| Meta description | 1,5 | todas com 50 a 160 caracteres e únicas | algumas ausentes, fora do tamanho ou repetidas | todas ausentes |
| H1 único | 1,5 | exatamente 1 por página | alguma página sem H1 ou com vários | home sem H1 |
| Hierarquia de títulos | 0,5 | sem saltos | salto de nível (por exemplo, H2 para H4) | (não se aplica) |
| Canonical | 1 | todas com canonical | alguma sem | canonical apontando para outro domínio |
| HTTPS | 2 | HTTPS e http redireciona | HTTPS sem redirecionar o http | sem HTTPS |
| Redirecionamentos até a home | 0,5 | 0 a 1 | 2 | 3 ou mais |
| robots.txt | 1 | existe e libera a home | não existe | bloqueia o Googlebot na home |
| sitemap.xml | 1 | encontrado (declarado no robots, `/sitemap.xml` ou `/sitemap_index.xml`) | não encontrado | (não se aplica) |
| URLs legíveis | 0,5 | sem `?p=123`, maiúsculas, `_` ou mais de 115 caracteres | algum endereço assim | (não se aplica) |
| Imagens com texto alternativo | 1 | até 10% sem atributo `alt` | até 30% | mais de 30% |
| Links internos quebrados | 1,5 | nenhum 404/410 | 1 a 2 | 3 ou mais |
| Dados estruturados (schema.org) | 1 | algum JSON-LD ou microdata | (não se aplica) | nenhum |
| Empresa identificada para IA | 1 | tipo Organization, LocalBusiness ou subtipo | (não se aplica) | ausente |
| Conteúdo que responde perguntas | 0,5 | FAQPage ou 3 ou mais subtítulos em forma de pergunta | 1 a 2 perguntas, ou nenhuma | (não se aplica) |
| llms.txt | 0,25 | existe | não existe | (não se aplica) |

**Notas técnicas:**
- **Imagens:** `alt=""` é considerado correto (imagem decorativa). Só conta como falha a ausência do atributo.
- **Links internos:** até 40 links únicos são verificados, com HEAD e, se recusado, GET. Timeouts e erros 5xx não contam como quebrados e vão para as notas internas.
- **llms.txt:** tem peso baixo de propósito, porque o padrão ainda é pouco adotado.

## Prioridade e esforço

- **Prioridade alta:** afeta diretamente o contato ou a visibilidade, como CTA no celular, WhatsApp, noindex, HTTPS ou LCP acima de 4 s.
- **Prioridade média:** afeta a experiência ou o SEO de forma relevante.
- **Prioridade baixa:** ajuste fino.
- **Esforço:**
  - **rápido (horas):** configuração ou conteúdo;
  - **médio (dias):** ajuste técnico ou de layout;
  - **projeto (semanas):** reconstrução.

## Os 3 achados mais importantes (resumo executivo)

São escolhidos entre os itens **medidos** com problema, ou com atenção e prioridade alta, desde que tenham impacto de negócio descrito. A ordem é:
1. prioridade (alta, média, baixa);
2. gravidade;
3. categoria (conversão, depois performance, depois SEO);
4. peso.

Entra no máximo um item de performance, para evitar repetição. Avaliações de especialista nunca entram no resumo.
