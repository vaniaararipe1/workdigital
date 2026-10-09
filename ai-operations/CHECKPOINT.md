# Checkpoint — ecossistema Work Digital

Atualizado em: 2026-10-09T15:31:09Z

Escopo preservado: `vaniaararipe1/workdigital`, branch `ai-operations-v1`, somente `ai-operations/`. Históricos de 26/09/2026 orientam a recuperação, mas não são prova do estado atual.

## Decisões preservadas

- Vânia delegou implementação e testes internos sem aprovação por etapa.
- Destino e motor: ChatGPT/Work. Claude Projects, Anthropic e credenciais Claude foram abandonados por decisão de 08/10/2026.
- Sem contratação, gasto adicional, credenciais de API ou efeitos comerciais externos autorizados.
- Os sete agentes e o Control Plane permanecem: Patrícia orquestra; Felipe comercial; Larissa lidera Brand & Marketing; Clara é especialista digital; Bruno conteúdo; Marcelo direção de arte; Gabriel UX/UI.
- D-10 prevalece sobre D-08 para a relação Larissa/Clara.
- Cadastro, contratos, interface, testes unitários e deploy isolado não contam como prova de runtime autônomo.
- `WP-004` permanece fora dos smoke tests enquanto suas restrições e proveniência não forem reconciliadas.

## Trabalho concluído

- Interface navegável de AI Operations implementada somente em `ai-operations/`, conforme comportamento do vídeo de referência e identidade Work Digital.
- Sete contratos nativos preservados em `runtime/agents.json`; fila fail-closed, regras de permissão, classificação externa e matriz D-10 implementadas.
- Colaboração nativa sequencial comprovada para Patrícia e os seis especialistas, com resultados internos revisados e persistidos.
- Planejador de fila, projeção autenticada, readiness e bloqueio do dispatcher implementados.
- Contrato de lease com versão monotônica, owner, expiração, heartbeat, liberação e verificação de fence implementado.
- Projeto Supabase correto confirmado: `Work Digital Control Plane` (`jegzhawblljpngbkaoqx`), PostgreSQL 17, estado saudável.
- Fonte atual da Edge Function `work-digital-mcp-v2` 2.6.0 recuperada antes de qualquer alteração; a fonte histórica não foi usada para substituir produção.
- Migração `create_work_digital_runtime_lease` aplicada: schema privado `wd_runtime`, operador autorizado, singleton de lease, auditoria, CAS transacional e persistência fenced de Work Packet.
- Migração `document_runtime_private_rls` aplicada com políticas explícitas de negação nas três tabelas privadas.
- Edge Function implantada como versão 9 / aplicação 2.7.0, preservando OAuth existente e acrescentando:
  - `read_runtime_lease`
  - `cas_runtime_lease`
  - `persist_work_packet_fenced`
- Health MCP pós-deploy respondeu online, database connected e versão 2.7.0.
- Código, migrações e documentação persistidos na branch pelo commit `9030fa0a729898e152426d28fdb40acd849d1700`.
- Ciclo técnico interno concluído com `WP-RUNTIME-FENCE-TEST-001`: Patrícia criou o pacote pelo MCP atual, Gabriel produziu a entrega, o backend executou aquisição, heartbeat e persistência fenced, Patrícia revisou o resultado e encerrou pacote, tarefa e operação.
- A retomada em outra execução encontrou o lease anterior expirado, assumiu-o legalmente com novo owner e liberou o singleton na versão 7. Isso comprova recuperação após expiração sem deixar owner pendente.
- Evidência `E-ECO-20261009-1230-FENCE-E2E` registrada como VERIFIED no Control Plane.

## Evidência e validação

- `npm test`: 44/44 testes aprovados.
- `node --experimental-strip-types --check runtime/backend/work-digital-mcp-v2/index.ts`: aprovado.
- PostgreSQL real:
  - leitura inicial: versão 0, sem owner;
  - aquisição `validation-run-20261009`: aplicada, versão 1;
  - owner concorrente: rejeitado sem escrita;
  - heartbeat do owner: aplicado, versão 2;
  - persistência com fence antigo 1: rejeitada com SQLSTATE `40001`;
  - liberação pelo owner: aplicada, versão 3;
  - estado final: sem owner e sem expiração;
  - auditoria: três linhas, exatamente uma por escrita aceita.
- Ciclo ponta a ponta controlado:
  - pacote `WP-RUNTIME-FENCE-TEST-001` criado com classificação interna, sem publicação e sem `WP-004`;
  - aquisição do runtime aplicada na versão 4;
  - heartbeat aplicado na versão 5;
  - resultado próprio de Gabriel persistido pela função `wd_persist_work_packet_fenced` com fence 5 e estado `REVIEW`;
  - Patrícia revisou o pacote para `DONE`; tarefa e operação também terminaram;
  - execução posterior comprovou estado durável, recuperação do lease expirado na versão 6 e liberação na versão 7;
  - estado final do lease: owner nulo, sem expiração.
- Fonte implantada recuperada após deploy: status ACTIVE, versão de função 9, OAuth preservado e os três novos tools presentes.
- Advisor de segurança após a segunda migração não aponta mais RLS sem política no schema `wd_runtime`. Permanece apenas aviso global preexistente de proteção contra senhas vazadas, fora do escopo deste runtime.
- Nenhuma tarefa, agente, permissão comercial, projeto de cliente ou arquivo fora de `ai-operations/` foi alterado.

## Estado operacional

- `atomic_compare_and_swap=true`
- `lease_backend=true`
- `fenced_work_packet_persistence=true`
- `runtime_verified=false`
- dispatcher continua desativado e `GET /api/queue` continua fail-closed sem todas as provas.

O backend durável, a retomada entre rodadas e a persistência fenced agora funcionam. Isso ainda não comprova a invocação nativa dos três novos tools pelo catálogo do ChatGPT, porque o registry continua expondo apenas o contrato anterior.

## Pendências

- Confirmar em execução futura que o registry do ChatGPT recarregou `read_runtime_lease`, `cas_runtime_lease` e `persist_work_packet_fenced`. Duas execuções após o deploy ainda não os exibiram.
- Somente após essas provas definir `runtime_verified=true` e avaliar ativação do dispatcher.
- Reconciliar `TASK-002` e `WP-004` antes de qualquer trabalho que possa implicar ação externa.
- QA visual em navegador real e publicação da interface continuam pendentes até existir ambiente de preview autorizado para esta branch.

## Próximo passo autorizado

Na próxima execução, descobrir novamente o contrato do plugin Work Digital. Se os três tools 2.7.0 estiverem expostos, repetir uma aquisição e liberação inteiramente pelo MCP nativo e então avaliar `runtime_verified`. Se continuarem ausentes, não alterar permissões nem sobrecarregar tools existentes: continuar QA e integração interna que não dependam desse catálogo. Não usar `WP-004`; não enviar mensagens a terceiros.

## Bloqueio

Não há bloqueio de acesso ao Supabase. O limite imediato é o registry MCP do ChatGPT continuar sem os três tools 2.7.0, apesar do health 2.7.0 e da fonte implantada. Não pedir nova instalação ou reconexão a Vânia e não alterar permissões globais. O QA visual local também não pôde ser concluído: não há navegador headless no workspace e o navegador remoto não alcança `localhost`; ainda falta um preview autorizado desta branch.

