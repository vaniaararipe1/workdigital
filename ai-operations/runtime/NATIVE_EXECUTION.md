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
3. Antes de cada despacho, reler pacote/tarefa/operação e restrições. Um único dispatcher. MCP observado não expõe lease/CAS; horário recebido não é trava atômica. Não ativar dispatchers paralelos.
4. Fornecer ao especialista contrato, contexto completo, decisões, referências e restrições do pacote. Delegação efetiva depende das ferramentas da sessão; não confundir registro de agente com execução.
5. Registrar received_at real somente quando o especialista iniciar. Preservar result e histórico; pacotes já recebidos nunca são automaticamente reiniciados.
6. Especialista produz resultado interno, registra result, completed_at real e next_action e devolve REVIEW. Não executar efeito externo, gasto, contato ou aprovação em nome de Vânia.
7. Patrícia revisa a entrega; solicita revisão independente quando o pacote exigir (ex.: Clara revisa Larissa no WP-004). A CEO recebe decisões indispensáveis e entregas verificáveis.
8. Persistir checkpoint ao concluir a sessão. Esta automação de construção não deve ser transformada silenciosamente em rotina de operação comercial.

## Integração ainda pendente
O servidor MCP disponível possui tools; não foi confirmado endpoint REST /snapshot. CONTROL_PLANE_API_URL é apenas um contrato existente e não deve receber o URL MCP assumindo equivalência.
A interface retorna live:false com dados históricos quando o adapter está ausente. /api/queue responde 503 sem fonte ao vivo; não despacha trabalho.
Próximo: implementar/testar adapter MCP ou projeção autenticada e UI com estado atual, recuperar vídeo, validar delegação nativa e teste operacional completo com pacotes dedicados.
Nenhum host/modelo adicional contratado. Nenhuma credencial API necessária para continuar os testes internos atuais.

## Documentação verificada em 08/10/2026
- https://learn.chatgpt.com/docs/automations — tarefas Work web usam ferramentas/skills/plugins; arquivos locais não persistem entre execuções.
- https://learn.chatgpt.com/docs/agent-configuration/subagents — delegação especializada; configuração de agentes personalizados em TOML descrita para clientes locais.
- https://learn.chatgpt.com/docs/dots — produto always-on documentado; disponibilidade/configuração nesta conta ainda não comprovadas.
