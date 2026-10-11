# Diagnóstico Gratuito de Site · Work Digital

Ferramenta de linha de comando que analisa o site de um lead e gera um relatório pronto, com a marca da Work Digital, em linguagem de dono de negócio. Você revisa e envia.

```bash
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X"
```

Saída em `relatorios/<dominio>-<data>/`:

| Arquivo | Para quem | O que é |
|---|---|---|
| `relatorio.pdf` | Lead | Versão para enviar: A4, páginas internas claras, capa e página final escuras |
| `relatorio.html` | Lead | Mesma coisa em tema escuro neon, para abrir no navegador |
| `notas-internas.html` | Só você | Itens de julgamento, baixa confiança, avisos da coleta, sugestões de abordagem e cálculo das notas |
| `dados.json` | Arquivo | Todos os dados brutos coletados, para comprovar qualquer afirmação |
| `capturas/` | Você | Primeira tela da home no celular e no computador |

A pasta `relatorios/` não vai para o Git e a pasta `diagnostico/` não é publicada no Vercel (ver `.vercelignore` na raiz). Os relatórios têm dados de leads e devem ficar só com você.

## Instalação

Requisitos: Python 3.10+ e Node.js 18+. O Node só é necessário para o Lighthouse local, usado quando o PageSpeed falhar.

```bash
cd diagnostico
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
cp .env.exemplo .env                                # e preencha a chave
```

## Variáveis de ambiente (`.env`)

| Variável | Obrigatória | Para que serve |
|---|---|---|
| `PAGESPEED_API_KEY` | Recomendada | Chave da API do Google PageSpeed Insights. Sem ela, o Google limita as consultas e a ferramenta usa o Lighthouse local. |
| `USAR_LIGHTHOUSE_LOCAL` | Não | `1` (padrão) usa o Lighthouse local se o PageSpeed falhar; `0` desliga. |
| `CHROMIUM_PATH` | Não | Caminho de um Chromium já instalado, se não quiser usar o do Playwright. |
| `PASTA_RELATORIOS` | Não | Onde salvar os relatórios (padrão: `./relatorios`). |

**Como criar a chave do PageSpeed:**
1. Em console.cloud.google.com, crie um projeto.
2. Em APIs e serviços, depois Biblioteca, ative a **PageSpeed Insights API**.
3. Em Credenciais, crie uma **Chave de API**.
4. Restrinja a chave à PageSpeed Insights API.
5. A cota gratuita é de 25 mil consultas por dia.

## Como rodar

```bash
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X"
python diagnostico.py site-do-lead.com.br --nome "Empresa X" --sem-pdf    # só HTML e JSON
python diagnostico.py https://... --nome "..." --saida /caminho/da/pasta  # pasta específica
python diagnostico.py https://... --nome "..." -v                         # mostra o andamento
```

Cada diagnóstico leva de 2 a 4 minutos. A maior parte do tempo é a medição de velocidade, feita no celular e no computador.

**Fluxo de revisão sugerido:**
1. Abra `notas-internas.html` e siga a lista "Antes de enviar".
2. Confira as capturas de tela.
3. Se discordar de alguma avaliação de especialista, edite o texto em `relatorio.html` e gere o PDF de novo. Para isso, abra o HTML no Chrome e use Imprimir, depois Salvar como PDF, com "Gráficos de plano de fundo" ligado.
4. Envie o PDF ao lead.

## Como testar

```bash
python -m pytest
```

Os testes cobrem a validação de URL (esquemas, IPs privados, localhost, IP decimal, IPv6, credenciais, portas) e todas as funções de análise, pontuação, resumo e plano de ação. Eles usam dados sintéticos e não acessam a rede.

Para ver o visual do relatório sem analisar um site real:

```bash
python exemplo/gerar_exemplo.py   # gera exemplo/saida/relatorio-exemplo.{html,pdf} com dados fictícios
```

## Como funciona

```
diagnostico.py              linha de comando
wd_diag/
  config.py                 configuração e leitura do .env
  seguranca.py              validação de URL (só http/https, só IPs públicos, sem credenciais, portas 80/443)
  http.py                   cliente HTTP educado (robots.txt, intervalo, timeout, limite de tamanho, redirecionamentos validados)
  rastreador.py             escolha de até 4 páginas internas (menu, sitemap e links da home)
  coleta/
    render.py + medir.js    Playwright: HTML renderizado, medições no DOM (celular e computador), capturas
    pagespeed.py            PageSpeed Insights, com fallback para Lighthouse local
    site.py                 robots.txt, sitemap, llms.txt, HTTPS, links quebrados
  analise/                  funções puras: dados coletados → achados
    performance.py  ux.py  seo.py  tecnologias.py
  pontuacao.py              notas 0 a 100 (regras em CRITERIOS.md)
  pipeline.py               executar_diagnostico(url, empresa) → resultado + arquivos
  relatorio/
    contexto.py  notas.py   montagem dos dados para os templates
    gerar.py                HTML (Jinja2) e PDF (Chromium)
    templates/  assets/     visual e marca
```

**Regras de integridade aplicadas no código:**
- Toda afirmação do relatório vem de um `Achado` com evidência coletada, e tudo fica em `dados.json`.
- Itens de julgamento têm `tipo="avaliacao"`: aparecem com selo próprio, não entram na nota e vão para as notas internas.
- Coletas que falham viram `tipo="nao_medido"`, com o texto "Não foi possível medir", e saem do cálculo da nota.
- Texto vindo do site analisado é sempre escapado antes de entrar no relatório.

**Rastreamento educado e seguro:**
- O user-agent é identificado: `WorkDigitalDiagnostico/1.0 (+https://workdigital.art.br)`.
- O robots.txt é respeitado. Se ele bloquear a home, nenhuma página é aberta e só o PageSpeed do Google é consultado.
- Há 1 s de intervalo entre requisições, timeout de 15 s (HTTP) e 30 s (página), e limite de 5 MB por resposta.
- Cada salto de redirecionamento e cada requisição do navegador é validado: endereços privados, localhost e metadados de nuvem são bloqueados.
- Vídeos e áudios não são baixados. Nada é clicado, nenhum formulário é enviado e nenhum dado pessoal é coletado.

## Fase 2: integração com RD Station (projeto, ainda não construído)

**Objetivo:** o lead preenche o formulário da landing, o diagnóstico roda sozinho e você recebe um e-mail para revisar e enviar.

```
Formulário (RD Station)
   │  webhook de conversão (POST JSON)
   ▼
API pequena (FastAPI) ── valida assinatura/token, extrai nome, e-mail e URL do site
   │  enfileira
   ▼
Fila (Redis + RQ, ou tabela SQLite para começar)
   │  worker pega 1 tarefa por vez
   ▼
wd_diag.pipeline.executar_diagnostico(url, empresa)   ← já pronto e reutilizável
   │  salva em armazenamento privado
   ▼
E-mail para hello@workdigital.art.br com links para notas internas e PDF
   │  você revisa
   ▼
Envio ao lead (manual no começo; depois, botão "aprovar" que envia pelo RD Station ou e-mail)
```

**Passos de implementação:**
1. **Webhook RD Station.**
   - Em RD Station Marketing, vá em Integrações e configure um Webhook no evento de conversão do formulário.
   - Os campos chegam em `leads[0]`: `name`, `email`, `company` e um campo personalizado com o site (por exemplo, `cf_site`).
   - Proteja o endpoint com um token secreto na URL ou num cabeçalho, e recuse requisições sem ele.
2. **API (`wd_diag/web/api.py`).**
   - Endpoint `POST /webhook/rdstation` que valida o token.
   - Normaliza a URL com `seguranca.validar_entrada`. URLs inválidas geram uma resposta ao lead pedindo o endereço correto.
   - Deduplica pelo domínio (um diagnóstico por domínio a cada 7 dias) e enfileira.
3. **Fila e worker.**
   - Um worker processa uma tarefa por vez, para não sobrecarregar a máquina nem os sites analisados.
   - Tempo máximo de 10 minutos por diagnóstico e 1 nova tentativa em caso de falha.
   - Estados: `recebido`, `processando`, `pronto_para_revisao`, `enviado` e `falhou`.
4. **Armazenamento.**
   - Os relatórios ficam fora do site público, em bucket privado (S3, R2 ou Supabase Storage) com links assinados que expiram.
   - Se for usar Vercel, só a API fica lá. O worker precisa de uma máquina com Chromium (Railway, Fly.io, Render ou uma VPS), porque funções serverless têm limite de tempo e tamanho incompatível com o Playwright.
5. **Aviso para revisão.**
   - E-mail transacional (Resend, Postmark ou Amazon SES) para você, com o resumo das notas e os links.
   - Opcional: atualizar o lead no RD Station com um campo `diagnostico_status`.
6. **Envio ao lead.**
   - Na primeira versão, você baixa o PDF e envia.
   - Na segunda versão, um link "aprovar e enviar" no e-mail dispara o envio ao lead e registra no RD Station.

**Onde o código atual já está preparado:**
- `executar_diagnostico()` recebe URL, nome e pasta de saída e devolve um dicionário. Não depende da linha de comando.
- A configuração vem de variáveis de ambiente.
- Coleta e análise são separadas, então dá para trocar o armazenamento sem mexer na análise.

## Limitações conhecidas

- **Performance sem a chave do PageSpeed.** O Lighthouse local mede na máquina que roda a ferramenta. Os números podem diferir do PageSpeed do Google e não incluem dados de visitantes reais, então o INP aparece como "não foi possível medir".
- **Firewalls e proteção anti-robô** (Cloudflare e similares) podem bloquear a ferramenta. O relatório registra a falha e as notas internas avisam.
- **Conteúdo que só aparece depois de um clique** (formulários em pop-up, menus, abas) não é analisado, porque a ferramenta não clica em nada.
- **Prova social e proposta de valor** são detectadas por palavras-chave e precisam de revisão humana. Por isso estão marcadas como avaliação de especialista.
- **Detecção de tecnologias** é conservadora de propósito: ferramentas carregadas só após consentimento de cookies podem não aparecer.
- **DNS rebinding:** a URL é validada antes de cada requisição, mas um domínio malicioso pode trocar o IP entre a validação e a conexão. Na Fase 2, rode o worker numa rede sem acesso a serviços internos.
