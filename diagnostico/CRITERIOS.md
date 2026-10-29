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
  - **Avaliação de especialista:** depende de julgamento humano (prova social, clareza da proposta de valor). **A ferramenta nunca preenche:** ela só sugere rascunhos no `revisao.json`, e o item aparece apenas na versão revisada, com o texto da Vania. **Nunca entra na nota.**
  - **Não foi possível medir:** a coleta falhou (site bloqueou, página não abriu, API fora do ar). **Sai do cálculo**, e o relatório mostra quantos critérios foram realmente medidos (por exemplo, "7 de 9 critérios medidos").
  - **Não foi possível confirmar:** há sinais contraditórios (por exemplo, código de formulário do RD Station sem formulário visível). **Sai do cálculo.**
- Cada seção do relatório traz uma linha "Como a nota foi formada", resumindo a regra abaixo.
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
| Resposta ao toque (INP) | até 200 ms | até 500 ms | acima de 500 ms | **só dados reais** (Chrome UX Report); sem dados, o cartão é omitido |
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
| Link de WhatsApp | 3 | link `wa.me`/`api.whatsapp` na home do celular, visível na primeira tela ou fixo | existe, mas fora da primeira tela ou só em páginas internas | não existe em nenhuma página analisada |
| Telefone e e-mail clicáveis | 1 | `tel:` e `mailto:` presentes | só um dos dois | nenhum |
| Formulário de contato | 2 | até 6 campos, todos com rótulo (ou formulário externo incorporado) | 7 a 9 campos, campos sem rótulo, ou nenhum formulário quando há outro contato clicável | mais de 9 campos, ou nenhum formulário e nenhum contato clicável |
| Site adaptado ao celular | 2 | viewport `width=device-width` e sem rolagem lateral | conteúdo mais largo que a tela | sem meta viewport |
| Botões e links fáceis de tocar | 1 | até 10% dos alvos menores que 24×24 px | até 30% | mais de 30% |
| Leitura confortável no celular | 1 | até 10% do texto abaixo de 12 px | até 40% | mais de 40% |

**Formulário de contato: quando dizemos "não há".** Antes de afirmar que não há formulário (MEDIDO), a ferramenta:
1. espera a página terminar de carregar (rede ociosa e mais 3 segundos);
2. procura `<form>` visível, `iframe` de formulário (RD Station, HubSpot, Typeform, Google Forms, Jotform, Calendly...) e código de formulários carregados por script (RD Station, HubSpot, Typeform, Google Forms, Elementor, Contact Form 7, WPForms, Gravity Forms, Calendly);
3. procura botões que parecem abrir formulário em janela (modal/pop-up) e, se nenhum formulário estiver visível, **clica em no máximo um** desses botões (de preferência na página de contato) para abrir a janela, **sem preencher nem enviar nada**. Se o clique levar para outra página, o resultado é descartado;
4. inclui a página de contato entre as analisadas: do menu, do rodapé ou do sitemap, ou tentando `/contato` e `/fale-conosco`.

Quando o formulário é encontrado, o relatório diz onde: a página, ou o botão que abre a janela.

Se houver qualquer sinal (passos 2 e 3) sem formulário visível, ou se a página de contato ou outra página não abrir, o item fica como **Não foi possível confirmar**. Só fica como MEDIDO quando nada foi encontrado em nenhuma das buscas.

**A mesma cautela vale para as outras ausências de Experiência e conversão.** "Não há WhatsApp", "não há telefone/e-mail clicável" e "não há botão de ação" só saem como MEDIDO depois da renderização completa e da busca nas páginas-chave. Se alguma página não abriu, se a página de contato ficou inacessível, se há código de botão de WhatsApp sem link visível ou se a página não mostrou nenhum elemento clicável, o item fica como **Não foi possível confirmar**.

Ficam **fora da nota** por serem avaliação de especialista (preenchidos só pela Vania):
- **Prova social visível:** busca por palavras-chave e blocos de depoimentos.
- **Clareza da proposta de valor:** leitura do H1. Títulos genéricos, como "Bem-vindo", ou com até 2 palavras são sinalizados para revisão.

**Notas técnicas:**
- "Chamada para ação" é um link ou botão com aparência de botão (fundo ou borda e preenchimento) e texto com verbo de ação, como contato, orçamento, comprar, agendar ou WhatsApp.
- Botões de cookies, idioma, menu e links de acessibilidade são ignorados.
- Links no meio de parágrafos não contam como alvo de toque, seguindo a exceção da WCAG 2.5.8.

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
| Prévia de compartilhamento (Open Graph) na home | 0,5 | og:title, og:description e og:image | algum ausente | (não se aplica) |
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

Aparecem nas duas versões. São escolhidos entre os itens **medidos** com problema, ou com atenção e prioridade alta, desde que tenham impacto de negócio descrito. A ordem é:
1. prioridade (alta, média, baixa);
2. gravidade;
3. categoria (conversão, depois performance, depois SEO);
4. peso.

Entra no máximo um item de performance, para evitar repetição. Avaliações de especialista nunca entram no resumo.

## Versão automática e versão revisada

| | Automática | Revisada |
|---|---|---|
| Quando | Na hora | Depois da revisão da Vania |
| Itens medidos, velocidade, SEO, tecnologias | Sim ("o que vimos" e "o que significa") | Sim, mais "o que fazer", prioridade e esforço |
| Avaliação de especialista | Não | Sim, com o texto da Vania |
| Plano "Por onde começar" | Não | Sim, revisado pela Vania |
| Nota pessoal e página de próximo passo | Não | Sim |
| Etiqueta na capa | "Resultado técnico" | (sem etiqueta) |
| Rodapé | "Análise técnica automatizada. Avaliação especializada em revisão." | "Análise técnica automatizada com revisão especializada." |

As **notas são as mesmas** nas duas versões: avaliações de especialista nunca mudam a nota. A versão revisada só é gerada quando o `revisao.json` tem nota pessoal, todas as avaliações e o plano marcados como `"revisado"`, com texto e sem a marcação `[RASCUNHO]`.

## Recomendação e fonte de cada critério

Todo item medido mostra, no relatório e nos e-mails, o valor recomendado e de onde ele vem (ex.: "mostrar o conteúdo principal em até 2,5 s · Fonte: Google, Core Web Vitals"). A lista fica em `wd_diag/analise/referencias.py`.

Regra: só citamos um órgão (Google, W3C, Meta etc.) quando a recomendação é dele de fato. Quando o limite usado pela ferramenta não vem de norma oficial (por exemplo, até 6 campos no formulário, um único H1, botão de WhatsApp), a fonte diz "boa prática de mercado (não há norma oficial)". Avaliações de especialista não recebem referência automática.
