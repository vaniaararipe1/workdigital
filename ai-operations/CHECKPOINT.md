# Checkpoint — ecossistema Work Digital

Atualizado em: 2026-10-11T18:26:42Z

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
- Edge Function implantada inicialmente como versão 9 / aplicação 2.7.0, preservando OAuth existente e acrescentando:
  - `read_runtime_lease`
  - `cas_runtime_lease`
  - `persist_work_packet_fenced`
- Health MCP pós-deploy respondeu online, database connected e versão 2.7.0.
- Edge Function endurecida e reimplantada como versão 10 / aplicação 2.7.1: `update_work_packet` rejeita `result` e `completed_at`; entregas precisam obrigatoriamente passar por `persist_work_packet_fenced`.
- Código, migrações e documentação persistidos na branch pelo commit `9030fa0a729898e152426d28fdb40acd849d1700`.
- Ciclo técnico interno concluído com `WP-RUNTIME-FENCE-TEST-001`: Patrícia criou o pacote pelo MCP atual, Gabriel produziu a entrega, o backend executou aquisição, heartbeat e persistência fenced, Patrícia revisou o resultado e encerrou pacote, tarefa e operação.
- A retomada em outra execução encontrou o lease anterior expirado, assumiu-o legalmente com novo owner e liberou o singleton na versão 7. Isso comprova recuperação após expiração sem deixar owner pendente.
- Evidência `E-ECO-20261009-1230-FENCE-E2E` registrada como VERIFIED no Control Plane.
- Inspeção do gerenciador de plugins confirmou que Work Digital Control Plane é um app personalizado, não uma release pública atualizável pelo diretório. Nenhuma permissão foi alterada e nenhuma reconexão foi solicitada.
- A ingestão de estado ao vivo da interface foi endurecida: não promove mais uma resposta arbitrária de `/snapshot` para `live=true`. Agora exige endpoint HTTPS (HTTP apenas em loopback para testes), token Bearer, timestamp com no máximo dois minutos, Control Plane online/banco conectado e o registro exato dos sete agentes. Qualquer falha retorna à projeção histórica e mantém a fila bloqueada.
- A Edge Function foi implantada como versão 11 / aplicação 2.8.0 com a rota somente leitura `/snapshot`, protegida pelo mesmo OAuth e contexto RLS do MCP. A resposta usa `no-store`, agrega agentes/operações/tarefas/pacotes e mantém `runtime_verified=false` por construção.
- A projeção histórica embarcada na interface foi regenerada a partir do MCP 2.8.0: sete agentes, 2 operações, 4 tarefas e 2 Work Packets válidos; registros `*-TEST-*` foram removidos e `live=false`/`runtime_verified=false` preservados.
- A rota ao vivo foi corrigida na Edge Function versão 12 / aplicação 2.8.1: o backend agora remove registros `*-TEST-*` e relações órfãs antes de responder, em vez de depender apenas do filtro da interface.
- O servidor da interface passou a aplicar uma fronteira de segurança uniforme em páginas e APIs: CSP restritiva, bloqueio de framing e MIME sniffing, isolamento de opener, política mínima de permissões e ausência de referrer. Assets estáticos usam revalidação e respostas operacionais continuam `no-store`.
- A montagem da URL do snapshot foi corrigida: ao receber a URL real da Edge Function, a interface agora preserva `/functions/v1/work-digital-mcp-v2` e acrescenta `/snapshot` ao final. Query, fragmento e credenciais embutidas são removidos/rejeitados antes de qualquer requisição.
- A ingestão da interface deixou de confiar na flag `runtime_verified` enviada pelo snapshot. Mesmo um snapshot fresco e saudável que se autodeclare verificado é normalizado para `runtime_verified=false`; a prova do runtime precisa vir de um canal independente com identidade e lease válidos.
- A validação ao vivo agora exige exatamente uma ocorrência de cada um dos sete agentes e a mesma versão do Control Plane registrada nas capacidades implantadas. Agentes duplicados ou backend incompatível fazem a interface retornar à projeção histórica e manter a fila fechada.
- O cliente do snapshot deixou de seguir redirecionamentos e passou a exigir MIME JSON e corpo limitado a 1 MiB. Isso impede que o Bearer token seja reutilizado em destino redirecionado e faz respostas inesperadas falharem para a projeção histórica.
- A interface agora também valida a integridade relacional de todo snapshot ao vivo: exige IDs e chaves não vazios e únicos, rejeita registros `*-TEST-*`, tarefas sem operação válida e Work Packets cujo par tarefa/operação não seja consistente. O filtro do backend deixou de ser a única barreira contra uma projeção corrompida.
- O contrato ao vivo passou a exigir `schema_version=2`, IDs únicos também no registro de agentes e referências de coordenador, owner, origem e destino limitadas aos sete agentes válidos. Schema futuro incompatível ou agente inexistente derruba a projeção para histórico em vez de contaminar a fila.
- O fallback histórico deixou de confiar até nas flags do arquivo embarcado: `historicalState` força `live=false` e `runtime_verified=false` em código para estados indisponível, sem token e não configurado. Um snapshot local alterado incorretamente não consegue mais se apresentar como prova de execução.
- A validação ao vivo agora ancora o cadastro nos contratos de `runtime/agents.json`: nome, função, especialidade e mapa completo de permissões precisam coincidir para cada chave. Isso impede troca silenciosa de identidade e escalada de poderes externos no snapshot.
- O grafo de tarefas do snapshot ao vivo agora é validado antes de alimentar a fila: dependências e parents precisam existir, permanecer na mesma operação e formar grafos acíclicos; referências duplicadas, autorreferentes ou com `task_id`/`task_key` divergentes são rejeitadas.
- A normalização do snapshot deixou de ocultar contradições entre campos canônicos e aliases do MCP. Pares como `agent_key`/`key`, `owner_agent`/`owner` e `destination_agent`/`destination` precisam coincidir, e um `task_id` não pode ser resolvido silenciosamente como `task_key`.
- O gate de readiness do dispatcher agora exige, além de estado ao vivo, identidade, lease e CAS, as três provas de segurança da entrega: versão esperada, persistência fenced e bloqueio das escritas legadas. Marcar o runtime como verificado e apresentar lease ativo não contorna mais uma dessas proteções ausente.

## Evidência e validação

- `npm test`: 61/61 testes aprovados.
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
- Health após o hardening: online, banco conectado, aplicação 2.7.1. Teste pelo comando legado retornou `runtime-delivery-requires-fence` e não executou escrita.
- Health reconfirmado em 09/10/2026 às 20:35Z: online, banco conectado, aplicação 2.7.1. Leitura direta do lease confirmou versão 7, owner/principal nulos e nenhuma expiração pendente.
- Testes novos comprovam rejeição de snapshot antigo, não-live, não saudável, com agentes incompletos, endpoint remoto sem HTTPS e configuração sem token.
- Fonte implantada da versão 11 recuperada e comparada: rota `/snapshot`, OAuth/RLS, `no-store` e bloqueio de `runtime_verified` presentes. Health MCP retornou online, banco conectado e aplicação 2.8.0.
- As quatro coleções usadas pelo snapshot foram lidas pelo mesmo MCP autenticado: sete agentes exatos, 7 operações, 12 tarefas e 15 Work Packets. O lease permaneceu livre na versão 7.
- Teste de regressão agora exige que a projeção embarcada acompanhe a versão do Control Plane, contenha exatamente os sete agentes e não inclua registros técnicos.
- A fonte da versão 12 foi recuperada após o deploy com `index.ts` e `snapshot-filter.mjs`; status ACTIVE e autenticação customizada preservados. O health retornou 2.8.1.
- Validação sobre o PostgreSQL atual confirmou 7/12/15 registros brutos e exatamente 2/4/2 operações, tarefas e Work Packets após o mesmo filtro relacional aplicado pela rota.
- Teste HTTP dedicado confirmou a fronteira de segurança tanto em `/` quanto em `/api/control-plane`, incluindo `frame-ancestors 'none'`, `object-src 'none'`, `X-Frame-Options: DENY` e `Permissions-Policy` sem câmera, geolocalização, microfone ou pagamentos.
- Regressão dedicada confirmou que `https://example.supabase.co/functions/v1/work-digital-mcp-v2` produz exatamente `.../work-digital-mcp-v2/snapshot`; URLs já finalizadas em `/snapshot` permanecem idempotentes.
- Regressão dedicada apresentou um snapshot ao vivo com `runtime_verified=true`, identidade e lease aparentes; a interface zerou a alegação e o readiness permaneceu bloqueado por `runtime-verified-required`.
- O contrato de ingestão rejeitou tanto um oitavo registro duplicado de agente quanto um snapshot saudável declarado como 2.8.0 diante da capacidade implantada 2.8.1. A suíte permaneceu em 53/53 testes aprovados.
- Um servidor de teste tentou redirecionar `/snapshot`; a interface não seguiu o destino nem reenviou a credencial. Uma resposta `text/html` contendo JSON também foi rejeitada. Ambos os casos retornaram `live=false` e `connection_status=unavailable`.
- Regressão dedicada apresentou registros duplicados, operação técnica, tarefa órfã e Work Packet ligado a tarefa de outra operação; os quatro cenários foram rejeitados antes de qualquer estado ser tratado como ao vivo.
- Em 11/10/2026 às 12:26Z, o conector Supabase finalmente ficou disponível nesta sessão. A listagem confirmou apenas o projeto `Work Digital Control Plane` saudável; a Edge Function `work-digital-mcp-v2` permaneceu ACTIVE na versão 12, e sua fonte recuperada confirmou aplicação 2.8.1 e os três comandos de runtime implantados. O catálogo do app Work Digital, verificado separadamente na mesma execução, ainda não expôs esses comandos.
- Regressão dedicada confirmou rejeição de schema 3, ID duplicado entre agentes, task com owner inexistente e Work Packet com destino inexistente. O health permaneceu online, banco conectado e versão 2.8.1 após a validação.
- Regressão dedicada injetou `live=true` e `runtime_verified=true` em uma cópia da projeção histórica; o fallback zerou ambas as flags e preservou o motivo `connection_status=unavailable`.
- O cadastro atual foi relido pelo MCP e comparado aos sete contratos versionados; nome, função, especialidade e permissões coincidiram. Regressões que transformaram Gabriel em Direção de Arte e habilitaram contato externo para Felipe foram rejeitadas.
- Regressão dedicada confirmou que dependência inexistente, par ID/chave divergente, dependência entre operações e ciclos de dependência ou parent invalidam o snapshot ao vivo. A fila não recebe um grafo parcial ou ambíguo.
- Regressão dedicada confirmou rejeição de aliases contraditórios em agentes, operações, tarefas e Work Packets, além de referência de chave inserida indevidamente no campo `task_id`.
- Regressão dedicada apresentou estado ao vivo, `runtime_verified=true`, identidade e lease ativo, removendo separadamente `expected_version`, persistência fenced e bloqueio de escrita legada; nos três casos o readiness permaneceu falso e o dispatcher desativado.
- Advisor de segurança após a segunda migração não aponta mais RLS sem política no schema `wd_runtime`. Permanece apenas aviso global preexistente de proteção contra senhas vazadas, fora do escopo deste runtime.
- Nenhuma tarefa, agente, permissão comercial, projeto de cliente ou arquivo fora de `ai-operations/` foi alterado.

## Estado operacional

- `atomic_compare_and_swap=true`
- `lease_backend=true`
- `fenced_work_packet_persistence=true`
- `legacy_delivery_writes_blocked=true`
- `runtime_verified=false`
- dispatcher continua desativado e `GET /api/queue` continua fail-closed sem todas as provas.

O backend durável, a retomada entre rodadas, a persistência fenced e o bloqueio do bypass legado agora funcionam. Isso ainda não comprova a invocação nativa dos três novos tools pelo catálogo do ChatGPT, porque o registry continua expondo apenas o contrato anterior.

## Pendências

- Confirmar em execução futura que o registry do ChatGPT recarregou `read_runtime_lease`, `cas_runtime_lease` e `persist_work_packet_fenced`. A verificação de 11/10/2026 às 18:26Z continuou sem os três comandos, embora a fonte ativa recuperada diretamente do Supabase os contenha.
- Conectar a interface publicada à rota `/snapshot` com um token OAuth de servidor somente quando existir ambiente autorizado; nenhuma credencial foi criada, exposta ou solicitada no chat.
- Somente após essas provas definir `runtime_verified=true` e avaliar ativação do dispatcher.
- Reconciliar `TASK-002` e `WP-004` antes de qualquer trabalho que possa implicar ação externa.
- QA visual em navegador real e publicação da interface continuam pendentes até existir ambiente de preview autorizado para esta branch.

## Próximo passo autorizado

Na próxima execução, descobrir novamente o contrato do plugin Work Digital. Se os três tools 2.7+ estiverem expostos, repetir uma aquisição e liberação inteiramente pelo MCP nativo e então avaliar `runtime_verified`. Se continuarem ausentes, não alterar permissões nem sobrecarregar tools existentes: continuar QA e integração interna que não dependam desse catálogo, especialmente o preview visual autorizado e o contrato de configuração da interface publicada. Não usar `WP-004`; não enviar mensagens a terceiros.

## Bloqueio

Não há bloqueio de acesso ao Supabase. O limite imediato é o registry MCP do ChatGPT continuar sem os três tools, apesar do health 2.8.1 e da fonte implantada. O app é personalizado e não tem release pública atualizável pelo diretório. Não pedir nova instalação ou reconexão a Vânia e não alterar permissões globais. A rota `/snapshot` não pôde ser invocada com OAuth bruto porque o conector não expõe o token; foram validados a fonte ativa, o health e as coleções subjacentes, inclusive as contagens filtradas. O QA visual local foi tentado novamente em 11/10/2026 às 14:34Z, mas o navegador remoto retornou `ERR_CONNECTION_REFUSED` para `127.0.0.1`; ainda falta um preview autorizado desta branch.

