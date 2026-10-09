# Backend de reserva — implantado e validado

Escopo: Control Plane Supabase existente. Não hospedar este endpoint no servidor público somente leitura de AI Operations.

## Componentes

- `001_runtime_lease.sql`: migração transacional com registro único, versão monotônica, bloqueio de linha, relógio do banco, autorização por usuário, expiração e auditoria na mesma transação.
- `002_runtime_private_rls.sql`: políticas explícitas de negação para as tabelas privadas.
- `work-digital-mcp-v2/index.ts`: fonte 2.6.0 recuperada da produção e estendida como 2.7.0 com leitura, CAS e persistência fenced.
- `lease-handler.mjs`: handler Fetch compatível com Node/Deno, que exige autenticação existente e cliente Supabase vinculado ao usuário autenticado. Usa RPC; nunca recebe credencial privilegiada no navegador.
- Cliente HTTP existente: envia `If-Match` e `X-Lease-Owner`, inclusive ao liberar.

O owner identifica uma execução única. A versão é o fence para impedir atualização por uma execução desatualizada. A autorização SQL também vincula a reserva ao usuário autenticado; uma execução diferente não pode substituir/liberar reserva ativa apenas por conhecer a versão.

## Implantação realizada em 09/10/2026

1. Projeto confirmado: `Work Digital Control Plane` (`jegzhawblljpngbkaoqx`), PostgreSQL 17.
2. Migrações `create_work_digital_runtime_lease` e `document_runtime_private_rls` aplicadas.
3. O único usuário autenticado existente foi cadastrado como operador por seleção no banco, sem UUID versionado.
4. A Edge Function `work-digital-mcp-v2` foi atualizada para a versão implantada 9, aplicação 2.7.0, preservando OAuth e `verify_jwt=false` porque a autenticação customizada existente continua no corpo.
5. O health MCP respondeu online, banco conectado e versão 2.7.0.

Não há workspace Render nem novo host exigido por esta implementação. Não foi confirmado que Render hospede o Control Plane.

## Validação concluída e limite de ativação

`npm test` valida cliente, heartbeat, handler, contrato SQL e integração da fonte MCP. A suíte atual possui 44 testes aprovados. O PostgreSQL real também foi exercitado.

No Supabase real foram comprovados: versão inicial 0; aquisição do owner; rejeição de owner concorrente; heartbeat com incremento de versão; rejeição de fence antigo (`40001`); liberação pelo owner; auditoria com três escritas aceitas; e estado final sem owner na versão 3. O advisor deixou de apontar tabelas RLS sem políticas após a segunda migração.

As capacidades `atomic_compare_and_swap`, `lease_backend` e `fenced_work_packet_persistence` agora estão verdadeiras. `runtime_verified` e o dispatcher permanecem falsos: CAS real não comprova sozinho execução autônoma dos sete agentes. Ainda é necessário o ciclo MCP autenticado completo, em nova sessão que carregue os novos tools, com renovação durante o trabalho e persistência fenced de uma entrega interna controlada.

## Limite atual

O registry de tools carregado no início desta sessão ainda mostra o contrato 2.6.0, embora o health já responda 2.7.0 e a fonte implantada contenha os três novos tools. Não ativar o dispatcher apenas com prova de deploy; a próxima sessão deve confirmar que o ChatGPT recebeu `read_runtime_lease`, `cas_runtime_lease` e `persist_work_packet_fenced`, então executar um smoke test interno sem usar `WP-004`.

Referências técnicas consultadas:
- https://www.postgresql.org/docs/current/sql-select.html
- https://supabase.com/docs/guides/database/functions

