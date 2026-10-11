# Work Digital — execução nativa no ChatGPT
Decisão de destino: Vânia, 08/10/2026. Claude/Anthropic não são destino nem motor.
Este contrato descreve a implementação em curso; não atesta agentes instalados ou runtime funcional.

## Arquitetura selecionada
ChatGPT Work executa trabalho com ferramentas conectadas. O Control Plane mantém tarefas, Work Packets e resultados. A interface lê esse estado; não chama modelos diretamente.
Os sete contratos estão em agents.json, reconciliados com cadastro atual e D-10. Clara é especialista em Brand & Marketing Digital; Larissa lidera a disciplina de Brand & Marketing.
Não criar GPTs/Projects como prova de autonomia, nem instalar runtime API com cobrança separada sem decisão explícita.
Não presumir que arquivos TOML do Codex local sejam automaticamente instalados no ChatGPT web.

## Protocolo do dispatcher Patrícia
1. Ler health, agentes, operações, tarefas, pacotes e decisões vigentes via ferramentas conectadas.
2. Excluir testes e trabalho concluído. Usar queue.js para planejamento conservador. Reconciliar divergências com proveniência; restrições textuais não podem ser ignoradas automaticamente.
3. Antes de cada despacho, reler pacote/tarefa/operação e restrições. Um único dispatcher. `lease.js` exige armazenamento persistente com compare-and-swap, identidade da execução, estado ao vivo e `runtime_verified=true`; sem essas quatro condições, falha fechado. O backend durável existe, mas `runtime_verified` continua falso até o ciclo MCP completo.
4. Fornecer ao especialista contrato, contexto completo, decisões, referências e restrições do pacote. Delegação efetiva depende das ferramentas da sessão; não confundir registro de agente com execução.
5. Registrar received_at real somente quando o especialista iniciar. Preservar result e histórico; pacotes já recebidos nunca são automaticamente reiniciados.
6. Especialista produz resultado interno. O runtime renova a reserva, usa a nova versão como fence e persiste result, completed_at real, next_action e REVIEW exclusivamente por `persist_work_packet_fenced`. Não executar efeito externo, gasto, contato ou aprovação em nome de Vânia.
7. Patrícia revisa a entrega; solicita revisão independente quando o pacote exigir (ex.: Clara revisa Larissa no WP-004). A CEO recebe decisões indispensáveis e entregas verificáveis.
8. Persistir checkpoint ao concluir a sessão. Esta automação de construção não deve ser transformada silenciosamente em rotina de operação comercial.

## Matriz de roteamento Brand & Marketing (D-10)
- Escopo amplo de marca, mercado, posicionamento, proposta de valor, governança e integração entre disciplinas: Larissa lidera.
- Escopo especializado digital — aquisição, jornada digital, lifecycle, SEO/AEO/GEO, CRO, CRM, automação, analytics e experimentação: Clara pode receber diretamente da Patrícia.
- Escopo misto: Larissa lidera a síntese; Clara recebe Work Packet delimitado para a dimensão digital. As contribuições e divergências são preservadas.
- Revisão independente pode ser recíproca: Clara pode revisar tecnicamente uma entrega digital de Larissa; isso não altera a liderança disciplinar ampla de Larissa. Larissa pode revisar integração estratégica de uma entrega da Clara sem eliminar sua autonomia técnica.
- Patrícia roteia pelo resultado esperado e pelas permissões, não por hierarquia genérica. Impasse relevante retorna à Patrícia; decisão de negócio ou ação externa retorna a Vânia.

## Prova nativa atual
Em 08/10/2026, uma execução agendada do ChatGPT orquestrou sequencialmente Work Packets isolados para Felipe, Clara, Bruno, Marcelo, Gabriel e Larissa. Cada especialista recebeu contexto e restrições, devolveu revisão própria, teve o resultado persistido no Control Plane e passou pela revisão da Patrícia. Os achados foram incorporados ao código e validados.
Isso comprova colaboração nativa sequencial e retomada da construção sem presença da CEO. Em 09/10/2026, o backend persistente de lease, heartbeat e fencing foi implantado e validado no Supabase. Ainda não comprova um dispatcher contínuo: `runtime_verified` permanece falso até um ciclo MCP autenticado completo usar os novos tools durante uma entrega interna controlada.

## Contrato de concorrência
`runtime/lease.js` implementa aquisição, heartbeat, verificação de fence e liberação otimistas por versão e só produz um plano de despacho quando o chamador apresenta lease ativo do mesmo owner, projeção ao vivo e runtime verificado. Seus limites de owner, versão e TTL correspondem ao contrato PostgreSQL: owner de 1 a 200 caracteres, versão inteira segura e TTL entre 1 segundo e 5 minutos. O módulo não contém armazenamento local disfarçado de persistência e não executa modelo nem altera Work Packet.
O teste em memória comprova a máquina de estados. As migrações Supabase e a Edge Function MCP 2.8.1 fornecem o adapter de produção: CAS transacional durável e persistência de entrega na mesma transação que bloqueia e verifica o lease. O comando legado de atualização não aceita mais `result` ou `completed_at`, impedindo bypass do fence.
`runtime/control-plane-capabilities.json` registra as capacidades implantadas e verificadas. `GET /api/runtime-readiness` publica cada requisito separadamente; `GET /api/queue` continua respondendo `503 runtime-not-ready` enquanto estado ao vivo, identidade, lease ativo, `runtime_verified`, versão esperada, CAS, backend de lease, persistência fenced e bloqueio das escritas legadas não forem apresentados juntos. Uma alegação de runtime verificado nunca substitui as provas de segurança da entrega. O helper interno `planLeasedDispatch` chama o mesmo avaliador e não pode ativar um plano com um subconjunto dessas condições.

A interface só aceita uma projeção como estado ao vivo quando o endpoint usa HTTPS, existe token Bearer, o snapshot declara `schema_version=2`, tem no máximo dois minutos, o Control Plane declara estado online/banco conectado, a versão coincide com a capacidade implantada e o registro contém exatamente uma ocorrência de cada um dos sete agentes autorizados. Nome, função, especialidade e permissões de cada agente precisam coincidir com `runtime/agents.json`; uma chave correta com papel trocado ou permissão ampliada também é rejeitada. Agentes, operações, tarefas e Work Packets precisam ter IDs e chaves únicos; registros técnicos são rejeitados; tarefa órfã ou pacote ligado a tarefa de outra operação invalida a projeção inteira. Campos canônicos e aliases do MCP precisam coincidir quando ambos aparecem; a normalização não pode esconder divergências entre `*_key`/`key`, `owner_agent`/`owner`, coordenador ou destino. Dependências e parents de tarefas precisam resolver sem ambiguidade por ID/chave, pertencer à mesma operação e formar grafos acíclicos; duplicação, autorreferência, referência ausente, campo ID contendo uma chave ou par ID/chave divergente falha fechado. Coordenador, owner, origem e destino, quando preenchidos, precisam apontar para os sete agentes aceitos. A aplicação nunca converte localmente um snapshot histórico em vivo e ignora qualquer alegação `runtime_verified=true` recebida por esse canal; essa prova precisa ser independente, vinculada à identidade da execução e ao lease. Qualquer inconsistência cai para a projeção histórica e mantém a fila fail-closed.
`runtime/http-lease-store.js` já implementa o lado cliente do contrato HTTPS + ETag/`If-Match`. O requisito de backend está definido em `runtime/CONTROL_PLANE_LEASE_API.md`; nenhuma URL ou credencial foi presumida.

## Projeção autenticada implementada
A Edge Function 2.8.1 fornece `/snapshot` somente leitura sob o mesmo OAuth/RLS do MCP. A resposta remove registros técnicos `*-TEST-*` e descarta tarefas/pacotes cujas relações não pertençam ao snapshot. `CONTROL_PLANE_API_URL` deve apontar para a URL HTTPS base da função (`.../functions/v1/work-digital-mcp-v2`); o servidor preserva esse caminho e acrescenta `/snapshot`. O cliente não segue redirecionamentos, exige JSON e limita a resposta a 1 MiB. Essa configuração só pode existir em host autorizado que mantenha o token no servidor; o token nunca deve ser enviado ao navegador ou versionado.
`runtime/projection.js` valida health, registro exato dos sete agentes e coleções do Control Plane, remove registros técnicos de teste e produz uma projeção somente leitura. `scripts/refresh-projection.js` grava o snapshot de forma atômica; a tarefa nativa do ChatGPT faz as leituras MCP e alimenta esse script.
A interface retorna `live:false` e identifica a fonte como `chatgpt-control-plane-projection`, com data e hora. O fallback força `live=false` e `runtime_verified=false` independentemente das flags gravadas no arquivo histórico, cobrindo indisponibilidade, token ausente e configuração ausente. `/api/queue` continua respondendo 503 sem fonte ao vivo e não despacha trabalho. Projeção agendada não é streaming nem prova de runtime autônomo dos sete agentes.
Próximo: em uma nova sessão com o schema MCP atualizado, executar aquisição → trabalho interno controlado → heartbeat → persistência fenced → liberação; depois validar retomada em outra execução. Somente então habilitar o dispatcher.
Nenhum host/modelo adicional contratado. Nenhuma credencial API necessária para continuar os testes internos atuais.

## Documentação verificada em 09/10/2026
- https://learn.chatgpt.com/docs/automations — tarefas Work web usam ferramentas/skills/plugins; arquivos locais não persistem entre execuções.
- A página documenta execução agendada em background e retomada no mesmo chat, mas não garante serialização de rodadas sobrepostas; por isso esta implementação não infere exclusão mútua da agenda.
- https://learn.chatgpt.com/docs/agent-configuration/subagents — delegação especializada; configuração de agentes personalizados em TOML descrita para clientes locais.
- https://learn.chatgpt.com/docs/dots — produto always-on documentado; disponibilidade/configuração nesta conta ainda não comprovadas.
