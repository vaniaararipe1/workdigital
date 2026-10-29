# Diagnóstico Gratuito de Site · Work Digital

Ferramenta de linha de comando que analisa o site de um lead e gera o relatório em duas versões, com a marca da Work Digital e em linguagem de dono de negócio:

- **Automática:** só dados medidos, pode ser enviada na hora.
- **Revisada:** acrescenta a avaliação da especialista, o plano de ação, a nota pessoal e o convite para conversa. Só é gerada depois que a Vania preenche o `revisao.json`.

```bash
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X" --versao automatica
# ...a Vania edita relatorios/<pasta>/revisao.json...
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X" --versao revisada
```

Saída em `relatorios/<dominio>-<data>/`:

| Arquivo | Para quem | O que é |
|---|---|---|
| `relatorio.pdf` / `.html` | Lead | **Versão automática** ("Resultado técnico"): dados medidos, sem avaliação de especialista nem plano |
| `relatorio-revisado.pdf` / `.html` | Lead | **Versão revisada**: tudo da automática mais avaliações, plano "Por onde começar", nota pessoal e próximo passo |
| `revisao.json` | Só você | Rascunhos para revisar. Tudo nasce "pendente de revisão" |
| `notas-internas.html` | Só você | O que foi medido, achados para abrir a conversa, rascunhos, baixa confiança, abordagem comercial e cálculo das notas |
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
| `ASSINATURA_NOME` / `ASSINATURA_CARGO` | Não | Nome e cargo na página final (padrão: Vania Araripe, Gestão de projetos digitais). |
| `PRAZO_REVISAO_DIAS` | Não | Prazo citado na versão automática (padrão: 2 dias úteis). |
| `PASTA_RELATORIOS` | Não | Onde salvar os relatórios (padrão: `./relatorios`). |

**Como criar a chave do PageSpeed:**
1. Em console.cloud.google.com, crie um projeto.
2. Em APIs e serviços, depois Biblioteca, ative a **PageSpeed Insights API**.
3. Em Credenciais, crie uma **Chave de API**.
4. Restrinja a chave à PageSpeed Insights API.
5. A cota gratuita é de 25 mil consultas por dia.

## Como rodar

```bash
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X"                      # versão automática (padrão)
python diagnostico.py https://site-do-lead.com.br --nome "Empresa X" --versao revisada    # depois da revisão
python diagnostico.py site-do-lead.com.br --nome "Empresa X" --sem-pdf                    # só HTML e JSON
python diagnostico.py https://... --nome "..." --saida /caminho/da/pasta                  # pasta específica
python diagnostico.py --regerar relatorios/<pasta>                                        # refaz a automática sem acessar o site
```

A versão automática leva de 2 a 4 minutos, e a maior parte do tempo é a medição de velocidade. A versão revisada não acessa o site: ela usa os dados já coletados, que ficam no `dados.json` mais recente daquele domínio, e leva poucos segundos.

**Fluxo de revisão:**
1. Rode a versão automática e envie o `relatorio.pdf` ao lead, se quiser. Ele avisa que a avaliação completa chega em até `PRAZO_REVISAO_DIAS` dias úteis.
2. Abra `notas-internas.html`. Lá estão o que foi medido, os achados para abrir a conversa e os rascunhos das avaliações e do plano.
3. Edite o `revisao.json`. Há dois caminhos:
   - **rápido:** leia a prévia (`relatorio-revisado-previa.pdf`, marcada "Prévia para revisão: não enviar"), ajuste os textos que quiser e troque `"aprovar_rascunhos"` para `true`. Os rascunhos passam a valer como texto revisado por você;
   - **detalhado:** reescreva ou aceite cada rascunho, apagando a marcação `[RASCUNHO]`, e troque cada `"pendente de revisão"` por `"revisado"`.

   Nos dois casos, avaliação com situação "atencao" ou "problema" continua exigindo o campo `o_que_fazer`.
4. Rode com `--versao revisada`. Se faltar algo, a ferramenta **recusa** e lista exatamente o que falta.
5. Confira e envie o `relatorio-revisado.pdf`.

**E-mails (Fase 2):** o visual fica em `wd_diag/entrega/templates/` (`lead_automatico`, `lead_revisado`, `vania_pronto`, com a moldura comum em `base_lead`). São HTML com estilos inline, que é o que os leitores de e-mail aceitam. O logo e a foto vão embutidos na mensagem (`wd_diag/entrega/assets/`). O e-mail interno separa "O que já foi analisado" (medido, entra na nota) de "O que você precisa analisar" (rascunhos por extenso, itens não confirmados e o caminho para aprovar), com a prévia da versão completa em anexo.

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
  revisao.py                rascunho e validação do revisao.json (regra de integridade da versão revisada)
  entrega/                  interface da Fase 2 (webhook, e-mail): só assinaturas, ainda não implementada
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
- Vídeos e áudios não são baixados. Nenhum formulário é preenchido ou enviado e nenhum dado pessoal é coletado. O único clique é para abrir a janela de contato, quando o formulário não está visível.

## Fase 2: integração com RD Station (projeto, ainda não construído)

**Objetivo:** o lead preenche o formulário (popup do RD Station, landing em WordPress ou prospecção feita pela Vania), recebe na hora a **versão automática** e, depois da revisão, a **versão revisada**.

```
Formulário (RD Station / landing)
   │  webhook de conversão (POST JSON)
   ▼
API pequena ── valida token, extrai nome, e-mail, empresa e site  → wd_diag.entrega.receber_lead()
   │  enfileira
   ▼
Fila (tabela SQLite ou GitHub Actions para começar)
   │  worker pega 1 tarefa por vez
   ▼
wd_diag.pipeline.executar_diagnostico(url, empresa)   ← versão automática + revisao.json (já pronto)
   │
   ├─► wd_diag.entrega.enviar_automatica()  → lead recebe relatorio.pdf na hora
   └─► wd_diag.entrega.avisar_revisao()     → Vania recebe link para revisao.json e notas internas
          │  Vania revisa
          ▼
wd_diag.pipeline.gerar_revisada(pasta)   ← recusa se o revisao.json estiver incompleto (já pronto)
   ▼
wd_diag.entrega.enviar_revisada()        → lead recebe relatorio-revisado.pdf
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
- **Variação entre medições:** notas de velocidade mudam alguns pontos a cada execução, inclusive no PageSpeed. Em testes, a mesma home variou de 60 a 70 com o Lighthouse local. Use os números como ordem de grandeza, não como valor exato.
- **Firewalls e proteção anti-robô** (Cloudflare e similares) podem bloquear a ferramenta. O relatório registra a falha e as notas internas avisam.
- **Conteúdo que só aparece depois de um clique:** a ferramenta clica em no máximo um botão que abre janela de contato, para confirmar o formulário, sem preencher nem enviar. Menus, abas e outros pop-ups não são explorados. Quando há sinal de formulário que não deu para abrir, o item sai como "Não foi possível confirmar", nunca como ausência.
- **Prova social e proposta de valor** são detectadas por palavras-chave e precisam de revisão humana. Por isso estão marcadas como avaliação de especialista.
- **Detecção de tecnologias** é conservadora de propósito: ferramentas carregadas só após consentimento de cookies podem não aparecer.
- **DNS rebinding:** a URL é validada antes de cada requisição, mas um domínio malicioso pode trocar o IP entre a validação e a conexão. Na Fase 2, rode o worker numa rede sem acesso a serviços internos.
