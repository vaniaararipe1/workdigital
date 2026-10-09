# Checkpoint — ecossistema Work Digital

Atualizado em: 2026-10-09T12:39:22Z

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
- Fonte implantada recuperada após deploy: status ACTIVE, versão de função 9, OAuth preservado e os três novos tools presentes.
- Advisor de segurança após a segunda migração não aponta mais RLS sem política no schema `wd_runtime`. Permanece apenas aviso global preexistente de proteção contra senhas vazadas, fora do escopo deste runtime.
- Nenhuma tarefa, agente, permissão comercial, projeto de cliente ou arquivo fora de `ai-operations/` foi alterado.

## Estado operacional

- `atomic_compare_and_swap=true`
- `lease_backend=true`
- `fenced_work_packet_persistence=true`
- `runtime_verified=false`
- dispatcher continua desativado e `GET /api/queue` continua fail-closed sem todas as provas.

O backend durável agora funciona. Isso ainda não comprova que o ChatGPT executa o protocolo completo de forma autônoma entre rodadas.

## Pendências

- Confirmar, em uma nova execução, que o registry do ChatGPT recarregou os três novos tools MCP. O registry desta sessão foi carregado antes do deploy, embora o health já tenha retornado 2.7.0.
- Executar um ciclo interno controlado: adquirir lease, selecionar pacote seguro que não seja `WP-004`, delegar, renovar por heartbeat, persistir resultado com o fence renovado e liberar.
- Repetir a leitura em outra execução para comprovar retomada entre rodadas e estado durável após reinício da Edge Function.
- Somente após essas provas definir `runtime_verified=true` e avaliar ativação do dispatcher.
- Reconciliar `TASK-002` e `WP-004` antes de qualquer trabalho que possa implicar ação externa.
- QA visual em navegador real e publicação da interface continuam pendentes até existir ambiente de preview autorizado para esta branch.

## Próximo passo autorizado

Na próxima execução, descobrir novamente o contrato do plugin Work Digital. Se os três tools 2.7.0 estiverem expostos, executar o ciclo MCP autenticado completo com um novo pacote estritamente interno e descartável, incluindo heartbeat e persistência fenced. Não alterar flags de runtime antes da prova; não usar `WP-004`; não enviar mensagens a terceiros.

## Bloqueio

Não há bloqueio de acesso ao Supabase neste checkpoint. O único limite imediato é o registry MCP desta sessão ter sido carregado antes do deploy e ainda mostrar o schema 2.6.0; isso deve ser verificado na próxima execução, sem pedir nova instalação ou reconexão a Vânia. A autonomia completa continua não comprovada até o ciclo MCP entre rodadas.

