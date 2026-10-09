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
`runtime/lease.js` implementa aquisição, heartbeat, verificação de fence e liberação otimistas por versão e só produz um plano de despacho quando o chamador apresenta lease ativo do mesmo owner, projeção ao vivo e runtime verificado. O módulo não contém armazenamento local disfarçado de persistência e não executa modelo nem altera Work Packet.
O teste em memória comprova a máquina de estados. As migrações Supabase e a Edge Function MCP 2.7.1 fornecem o adapter de produção: CAS transacional durável e persistência de entrega na mesma transação que bloqueia e verifica o lease. O comando legado de atualização não aceita mais `result` ou `completed_at`, impedindo bypass do fence.
`runtime/control-plane-capabilities.json` registra as capacidades implantadas e verificadas. `GET /api/runtime-readiness` publica cada requisito separadamente; `GET /api/queue` continua respondendo `503 runtime-not-ready` enquanto estado ao vivo, identidade, lease ativo e `runtime_verified` não forem apresentados juntos.

A interface só aceita uma projeção como estado ao vivo quando o endpoint usa HTTPS, existe token Bearer, o snapshot tem no máximo dois minutos, o Control Plane declara estado online/banco conectado e o registro contém exatamente os sete agentes autorizados. A aplicação nunca converte localmente um snapshot histórico em vivo; qualquer inconsistência cai para a projeção histórica e mantém a fila fail-closed.
`runtime/http-lease-store.js` já implementa o lado cliente do contrato HTTPS + ETag/`If-Match`. O requisito de backend está definido em `runtime/CONTROL_PLANE_LEASE_API.md`; nenhuma URL ou credencial foi presumida.

## Projeção autenticada implementada
O servidor MCP disponível possui tools; não foi confirmado endpoint REST /snapshot. CONTROL_PLANE_API_URL é apenas um contrato existente e não deve receber o URL MCP assumindo equivalência.
`runtime/projection.js` valida health, registro exato dos sete agentes e coleções do Control Plane, remove registros técnicos de teste e produz uma projeção somente leitura. `scripts/refresh-projection.js` grava o snapshot de forma atômica; a tarefa nativa do ChatGPT faz as leituras MCP e alimenta esse script.
A interface retorna `live:false` e identifica a fonte como `chatgpt-control-plane-projection`, com data e hora. `/api/queue` continua respondendo 503 sem fonte ao vivo e não despacha trabalho. Projeção agendada não é streaming nem prova de runtime autônomo dos sete agentes.
Próximo: em uma nova sessão com o schema MCP atualizado, executar aquisição → trabalho interno controlado → heartbeat → persistência fenced → liberação; depois validar retomada em outra execução. Somente então habilitar o dispatcher.
Nenhum host/modelo adicional contratado. Nenhuma credencial API necessária para continuar os testes internos atuais.

## Documentação verificada em 09/10/2026
- https://learn.chatgpt.com/docs/automations — tarefas Work web usam ferramentas/skills/plugins; arquivos locais não persistem entre execuções.
- A página documenta execução agendada em background e retomada no mesmo chat, mas não garante serialização de rodadas sobrepostas; por isso esta implementação não infere exclusão mútua da agenda.
- https://learn.chatgpt.com/docs/agent-configuration/subagents — delegação especializada; configuração de agentes personalizados em TOML descrita para clientes locais.
- https://learn.chatgpt.com/docs/dots — produto always-on documentado; disponibilidade/configuração nesta conta ainda não comprovadas.
