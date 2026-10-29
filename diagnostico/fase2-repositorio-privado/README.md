# workdigital-diagnosticos (PRIVADO)

Automação do **Diagnóstico Gratuito de Site** da Work Digital. **Este repositório contém dados de leads: mantenha-o privado.**

A ferramenta de análise fica no repositório público `vaniaararipe1/workdigital` (pasta `diagnostico/`). Aqui ficam só:

| Pasta / branch | O que é |
|---|---|
| `web/` (branch `main`) | Landing, página de um clique e API. Publicada no Vercel em `diagnostico.workdigital.art.br` |
| `.github/workflows/diagnostico.yml` | Roda a versão automática: envia o PDF ao lead e avisa a Vania |
| `.github/workflows/revisao.yml` | Quando a Vania salva um `revisao.json`, gera a versão revisada e, se pedido, envia ao lead |
| branch `relatorios` | Os relatórios: `relatorios/<site>-<data>/` e `status/<id>.json` |
| `docs/integracao-formularios.md` | Como ligar o popup do RD Station e a landing à página |

## As páginas

| Arquivo | Endereço | Para quê |
|---|---|---|
| `web/index.html` | `/` | **Landing** (visual e textos feitos no ChatGPT). Os dois formulários disparam a análise e mostram as notas na tela |
| `web/integracao.js` | | Liga a landing ao diagnóstico. **Não precisa mexer.** Toda nova versão da landing precisa manter a linha `<script src="/integracao.js" defer></script>`, a classe `lead-form` dos formulários, um `<p class="form-status">` em cada um e os nomes dos campos (`nome`, `email`, `whatsapp`, `site_url`, `segmento`, `cargo`, `consentimento_lgpd`) |
| `web/relatorio.html` | `/relatorio` | Página de um clique ("Pegue seu relatório") para quem já deu os dados no popup do RD. Quem chega em `/` com o cookie do popup ou com `site` e `email` no endereço é levado para cá automaticamente |

## Como funciona

```
Popup RD / landing / página → /api/diagnostico (Vercel) → GitHub Actions "Diagnóstico automático"
   → lead recebe relatorio.pdf (resultado técnico) e a Vania recebe o aviso com o link para revisar
   → o e-mail da Vania traz o que já foi medido, o que ela precisa revisar (rascunhos por extenso) e a prévia em PDF
   → a Vania ajusta o que quiser e troca "aprovar_rascunhos" para true no revisao.json (pelo GitHub, até no celular)
   → "Revisão" gera relatorio-revisado.pdf e manda para a Vania conferir
   → com "enviar_ao_lead": true, o lead recebe a versão revisada (uma única vez)
```

## Configuração (uma vez)

### 1. Branch de dados
Crie o branch `relatorios` a partir do `main`: na página do repositório, abra o seletor de branch, digite `relatorios` e clique em "Create branch". Ele precisa ter os mesmos arquivos de `.github/workflows`.

### 2. Segredos do GitHub
Em **Settings → Secrets and variables → Actions → New repository secret**, crie:

| Nome | Valor |
|---|---|
| `PAGESPEED_API_KEY` | a chave do PageSpeed (a mesma do Google Cloud) |
| `GMAIL_USER` | o e-mail que envia (ex.: hello@workdigital.art.br) |
| `GMAIL_APP_PASSWORD` | a senha de app do Google (16 letras) |
| `EMAIL_AVISO` | onde você quer receber os avisos de revisão |

Em **Variables** (opcional):
- `LIMITE_DIARIO`: padrão 20;
- `PRAZO_REVISAO_DIAS`: padrão 2;
- `FERRAMENTA_REF`: branch da ferramenta; o padrão é o branch principal do repositório público.

### 3. Token para o Vercel conversar com o GitHub
1. Acesse **GitHub → Settings (do seu perfil) → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Em **Repository access**, escolha "Only select repositories" → `workdigital-diagnosticos`.
3. Em **Permissions**, marque **Contents: Read and write**. A permissão de Metadata fica automática.
4. Copie o token. Ele vai no passo 4.

### 4. Vercel
1. **Add New → Project →** importe `workdigital-diagnosticos`.
2. **Root Directory:** `web`. Framework: **Other**. Não há comando de build.
3. **Environment Variables:**
   - `GITHUB_TOKEN` = o token do passo 3;
   - `GITHUB_REPO` = `vaniaararipe1/workdigital-diagnosticos`.
4. Clique em Deploy. Depois, em **Settings → Domains**, adicione `diagnostico.workdigital.art.br` e crie no seu DNS o registro **CNAME** `diagnostico` → `cname.vercel-dns.com`, ou o valor que o Vercel mostrar.

### 5. Teste
1. Abra `https://diagnostico.workdigital.art.br/?site=workdigital.art.br&email=SEU_EMAIL&nome=Teste`.
2. Clique em **Pegue seu relatório**.
3. Em 5 a 8 minutos devem chegar dois e-mails: o resultado técnico, como lead, e o aviso de revisão.

## Rotina da Vania
1. Chega o e-mail **"[Diagnóstico] Empresa pronto para revisão"**, com o PDF automático e as notas internas.
2. Clique em **"abrir o revisao.json para edição"**:
   - revise os textos e apague as marcações `[RASCUNHO]`;
   - troque cada `"pendente de revisão"` por `"revisado"`;
   - clique em **Commit changes**.
3. Chega **"versão revisada pronta para conferir"**, com o PDF. Se faltar algo, chega a lista do que falta.
4. Para enviar ao lead: no mesmo `revisao.json`, troque `"enviar_ao_lead": false` para `true` e salve.

**Prospecção:** vá em **Actions → Diagnóstico automático → Run workflow**.

## Custos e limites
- **GitHub Actions:** gratuito até 2.000 minutos por mês em repositório privado. Cada diagnóstico usa de 6 a 8 minutos, o que dá cerca de 250 a 300 por mês.
- **Vercel:** plano gratuito.
- **Gmail:** até cerca de 500 e-mails por dia.
- **Proteções:**
  - 1 diagnóstico por site a cada 7 dias para pedidos de leads;
  - limite diário configurável;
  - campo invisível e tempo mínimo de preenchimento contra robôs.
