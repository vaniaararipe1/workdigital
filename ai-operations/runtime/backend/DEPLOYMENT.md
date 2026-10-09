# Backend de reserva — implementação, ainda não implantada

Escopo: Control Plane Supabase existente. Não hospedar este endpoint no servidor público somente leitura de AI Operations.

## Componentes

- `001_runtime_lease.sql`: migração transacional com registro único, versão monotônica, bloqueio de linha, relógio do banco, autorização por usuário, expiração e auditoria na mesma transação.
- `lease-handler.mjs`: handler Fetch compatível com Node/Deno, que exige autenticação existente e cliente Supabase vinculado ao usuário autenticado. Usa RPC; nunca recebe credencial privilegiada no navegador.
- Cliente HTTP existente: envia `If-Match` e `X-Lease-Owner`, inclusive ao liberar.

O owner identifica uma execução única. A versão é o fence para impedir atualização por uma execução desatualizada. A autorização SQL também vincula a reserva ao usuário autenticado; uma execução diferente não pode substituir/liberar reserva ativa apenas por conhecer a versão.

## Implantação necessária

1. Confirmar o projeto Supabase e recuperar a fonte atual do MCP 2.6.0. A fonte histórica 2.5.0 não deve substituir a produção.
2. Executar a migração uma vez no banco confirmado. Ela começa e termina em uma transação e não altera tarefas, pacotes ou agentes existentes.
3. Cadastrar somente o UUID do operador autenticado autorizado em `wd_runtime_operators`, por acesso administrativo do banco. Nenhum UUID é presumido e nenhum usuário se autoriza por RPC.
4. Importar `createLeaseHandler` na Edge Function atual e encaminhar `GET/PUT .../runtime/lease` pelo middleware OAuth existente. `authenticate(req)` deve produzir o cliente Supabase já vinculado ao usuário validado; não retornar um cliente service-role nem confiar apenas na presença de um header.
5. Configurar o cliente HTTP com o endereço HTTPS confirmado e token fornecido pelo mecanismo existente, nunca em arquivos versionados.

Não há workspace Render nem novo host exigido por esta implementação. Não foi confirmado que Render hospede o Control Plane.

## Validação antes de ativar

`npm test` valida o cliente, o handler e seu contrato por doubles de RPC. Não executa a migração nem comprova persistência PostgreSQL.

No Supabase real, verificar: usuário não autorizado recebe 403; versão inicial 0; duas aquisições simultâneas com a mesma versão resultam em apenas uma escrita; owner diferente não renova nem libera; owner original renova com incremento de versão; reserva expirada pode ser retomada; versão antiga não libera reserva retomada; relógios inválidos e TTL fora de 1 segundo–5 minutos são rejeitados; reinício da Edge Function preserva o estado; auditoria tem exatamente uma linha por escrita aceita; falha de auditoria reverte a alteração da reserva.

Manter `atomic_compare_and_swap=false`, `lease_backend=false` e `runtime_verified=false` até comprovar cada requisito correspondente. CAS real não comprova execução dos sete agentes; ainda é necessário ciclo operacional completo, renovação durante o trabalho e checagem de fence antes de persistir cada entrega.

## Limite atual

Não há ferramenta disponível nesta sessão para migrar o banco Supabase ou implantar sua Edge Function. O MCP operacional atual expõe registros de negócio, não gerenciamento SQL/deploy. Portanto este pacote está implementado e versionável, mas a migração continua não executada e a produção inalterada.

Referências técnicas consultadas:
- https://www.postgresql.org/docs/current/sql-select.html
- https://supabase.com/docs/guides/database/functions
