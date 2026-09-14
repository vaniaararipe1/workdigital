---
name: gerar-proposta
description: Gera uma proposta comercial da Work Digital (modelo simples ou completo) em PPTX e PDF a partir dos dados do cliente, sem alterar o design original dos templates. Use quando o usuário pedir para "gerar proposta", "criar orçamento", "montar proposta comercial" para um cliente.
---

# Gerar Proposta Comercial (Work Digital)

Este skill automatiza a criação de propostas comerciais, substituindo o
processo manual de duplicar o Google Slides e editar campo a campo. Os
templates originais (design, cores, imagens, fontes) **nunca são
alterados** — o script apenas substitui o texto dos campos variáveis,
preservando 100% da formatação.

## Passo a passo

1. **Pergunte ao usuário qual modelo usar**, se ainda não disse:
   - `simples` — proposta curta (4 slides): capa, dados do cliente,
     escopo/prazo/valor, encerramento.
   - `completa` — proposta detalhada (21 slides): as mesmas informações
     do modelo simples, mais detalhes do projeto, módulos inclusos/não
     inclusos, investimento e observações.

2. **Colete os dados necessários** conversando com o usuário. Os campos
   de cada modelo estão descritos em:
   - `scripts/schema_simples.json`
   - `scripts/schema_completa.json`

   Cada campo tem `chave`, `descricao` e se é `obrigatorio`. Campos com
   `padrao` podem ser omitidos (o script usa o texto original do
   template). Use os exemplos em `exemplos/dados_simples.exemplo.json` e
   `exemplos/dados_completa.exemplo.json` como referência de formato —
   principalmente os campos do tipo lista (`escopo`, `modulos_inclusos`,
   `modulos_nao_inclusos`, `investimento`, `observacoes`), onde cada item
   da lista vira um parágrafo/bullet no slide (comece cada item com
   `"- "` quando fizer sentido, seguindo o padrão do template).

   Pergunte também a **data da proposta** (`data`, formato `dd-mm-yyyy`;
   se o usuário não informar, usa a data de hoje).

3. **Monte um JSON de dados** em um arquivo temporário (ex:
   `/tmp/dados_proposta.json`) com as respostas do usuário.

4. **Rode o gerador**:
   ```bash
   python3 scripts/gerar_proposta.py --tipo <simples|completa> --dados /tmp/dados_proposta.json
   ```
   Isso cria dois arquivos em `propostas/`:
   ```
   <Cliente> Modelo de proposta comercial <simples|completa> (dd-mm-yyyy).pptx
   <Cliente> Modelo de proposta comercial <simples|completa> (dd-mm-yyyy).pdf
   ```
   O script instala automaticamente as fontes do template (Nunito e
   Space Grotesk Medium, em `fonts/`) antes de exportar o PDF, para o
   resultado sair visualmente idêntico ao Google Slides original. Ambos
   os arquivos ficam bem abaixo do limite de 5 MB (o maior caso, modelo
   completo, normalmente fica ~1,5 MB).

5. **Entregue os dois arquivos ao usuário** (PPTX e PDF) — no Claude Code
   use a ferramenta de envio de arquivo para mandar os dois.

## Observações importantes

- O nome do arquivo usa `dd-mm-yyyy` (traço) em vez de `dd/mm/yyyy`,
  porque `/` não é um caractere válido em nomes de arquivo. Avise o
  usuário dessa pequena adaptação se ele perguntar pelo padrão exato.
- Se o usuário pedir para adicionar/mudar um campo editável ou criar um
  novo modelo de proposta no futuro, veja `README.md` na raiz do
  repositório — a seção "Como adicionar ou ajustar campos" explica como
  mapear um novo campo do template (`shape_id` do PowerPoint) sem
  precisar reescrever o script.
- Nunca edite os arquivos em `templates/` diretamente — eles são a fonte
  do design. Qualquer atualização visual deve ser feita no Google Slides
  original e depois re-exportada (veja README.md).
