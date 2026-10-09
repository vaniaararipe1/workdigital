# Checkpoint — ecossistema Work Digital

Atualizado em: 2026-10-09T05:34:10Z

Escopo preservado: `vaniaararipe1/workdigital`, branch `ai-operations-v1`, somente `ai-operations/`. Históricos de 26/09/2026 orientam a recuperação, mas não são prova do estado atual.

## Decisões preservadas

- Vânia delegou implementação e testes internos sem aprovação por etapa.
- Destino e motor: ChatGPT/Work. Claude Projects, Anthropic e credenciais Claude foram abandonados por decisão de 08/10/2026.
- Sem contratação, gasto adicional, credenciais de API ou efeitos comerciais externos autorizados.
- Os sete agentes e o Control Plane permanecem: Patrícia orquestra; Felipe comercial; Larissa lidera Brand & Marketing; Clara é especialista digital; Bruno conteúdo; Marcelo direção de arte; Gabriel UX/UI.
- D-10 prevalece sobre D-08 para a relação Larissa/Clara. Cadastro, contratos e interface não contam como prova de runtime autônomo.

## Trabalho concluído

- Reconciliado o estado atual com o Control Plane: serviço online, banco conectado, versão 2.6.0, sete agentes cadastrados e duas operações registradas.
- Substituída a tela estática anterior por uma interface navegável de AI Operations, restrita a `ai-operations/`, com Agent Space, Operações, Tarefas e Work Packets.
- Adaptado o comportamento do vídeo de referência: Patrícia no centro, seis especialistas em órbita, conexões visuais, cartão de atividade e transição para listas operacionais. A identidade visual foi recriada com a paleta Work Digital, sem copiar a identidade do vídeo.
- Persistida uma fotografia verificável do Control Plane em `snapshot.json`; a interface a identifica como histórico e não como atualização ao vivo.
- Preservados os sete contratos nativos para ChatGPT Work em `runtime/agents.json`; Claude/Anthropic não integra esta implementação.
- Endurecido o planejador da fila: ações externas classificadas exigem permissão do agente e linguagem externa sem classificação falha de forma fechada.
- Adicionados testes para bloqueio por permissão e por ação externa não classificada.
- Revisão nativa executada por Felipe: confirmou limites comerciais e identificou a lacuna de permissão da fila, agora corrigida.
- Alterações remotas confirmadas na branch autorizada pelo commit `b460588cf4762d81db9c611a27ffdc29a78af108`; nenhum arquivo fora de `ai-operations/` foi modificado.
- Implementada projeção autenticada e fail-closed do Control Plane: valida health e os sete agentes, exclui registros de teste, grava snapshot atomicamente e mantém `/api/queue` indisponível sem fonte realmente ao vivo.
- Clara executou revisão nativa da interface; seu achado sobre linguagem de “execução agora” foi incorporado. A tela agora usa “Estado operacional registrado”, mostra data/hora da projeção e mantém aviso permanente de execução autônoma não verificada.
- Fechado e persistido no Control Plane um circuito atual Patrícia → Clara → Control Plane → Patrícia: `OP-ECO-TEST-20261008-2130`, `TASK-ECO-TEST-CLARA-001` e `WP-ECO-TEST-CLARA-001`, todos concluídos sem ação externa.
- Projeção, revisão de Clara, teste operacional e 15 testes persistidos na branch pelo commit `bd6cf75b49bc8374394211b8351c0f29b4faee8f`.
- Circuitos nativos sequenciais concluídos e persistidos para Bruno, Marcelo, Gabriel, Larissa e Felipe. Somados ao circuito de Clara, todos os seis especialistas executaram sob orquestração da Patrícia nesta construção.
- Bruno corrigiu microcopy, nomes e estados; Marcelo condicionou todo movimento visual a `runtime_verified`; Gabriel incorporou diálogo acessível, foco, navegação semântica e renderização segura; Larissa formalizou a matriz D-10 e governança; Felipe endureceu a classificação de ações externas e o contrato comercial.
- Permissão ambígua `prospect` de Felipe foi desativada no código e no Control Plane; estratégia e pesquisa interna agora usam `prospecting_strategy` e `lead_research`, mantendo `external_contact=false`.
- Handoffs dos seis especialistas, melhorias de interface, matriz D-10, contrato comercial e 18 testes persistidos no commit `794b83812ccf7ed3ba54807d8154cef448ac4107`.
- Implementado contrato fail-closed de claim/lease em `runtime/lease.js`: aquisição otimista versionada, expiração, liberação exclusiva pelo owner e bloqueio de despacho sem estado ao vivo, `runtime_verified=true` e lease ativo do mesmo runtime.
- O contrato não usa arquivo local como falsa persistência e exige adapter durável com `read` + `compareAndSwap`; portanto preserva a distinção entre máquina de estados testada e runtime de produção.
- Contrato, seis novos testes e documentação persistidos na branch autorizada pelo commit `99690dcdf472818ba0b71ba7b5d4767a0c3bb159`.
- Revalidado o Control Plane 2.6.0: online, banco conectado e escrita por chave disponível, porém sem `expected_version`, compare-and-swap ou claim atômico nos contratos MCP observados.
- Adicionada matriz verificável em `GET /api/runtime-readiness`; `GET /api/queue` agora falha com `503 runtime-not-ready` quando faltar qualquer requisito, inclusive se existir leitura ao vivo sem lease atômico.
- Capacidades observadas, endpoint de prontidão e bloqueio da fila persistidos no commit `b05d831242582c2b930bd03b2418d0de89013d64`; evidência `E-ECO-20261009-0230` registrada no Control Plane.
- Implementado o adapter cliente de produção para lease via HTTPS + ETag/`If-Match`, com Bearer token, timeout e tratamento explícito de disputa 409/412. O contrato mínimo do endpoint do Control Plane foi documentado, sem presumir URL ou credencial.
- Adapter e especificação persistidos no commit `63c86cc6659a417d10b31c1fd5ac8282c254c2fd`.

## Evidência e validação

- `npm test`: 30/30 testes aprovados.
- `node --check public/app.js` e `node --check server.js`: aprovados.
- QA estrutural: quatro áreas navegáveis, sete agentes, responsividade, preferência de movimento reduzido, permissões e `next_action` presentes. Teste também impede regressão para o rótulo “AGORA” enquanto o runtime não for comprovado.
- Planejamento atual: nenhum pacote liberado; `WP-004` bloqueado por `action-classification-required`, `agent-permission-denied` e `constraint-reconciliation-required`. O texto contém intenção externa/vedações e a restrição legada “Não executar ainda”; o fail-closed é deliberado.
- Testes de concorrência comprovam que um segundo owner não adquire lease ativo, que lease expirado pode ser retomado, que somente o owner libera e que o plano de despacho bloqueia sem as três provas de runtime. O armazenamento usado no teste é deliberadamente apenas um double em memória.
- Testes de prontidão comprovam que estado ao vivo isolado não ativa o dispatcher, que projeção histórica permanece bloqueada e que todos os requisitos precisam ser verdadeiros simultaneamente.
- O servidor é somente leitura: serve a interface e o snapshot, recusa escrita e travessia de diretório.
- A interface usa estado cinza para agente apenas cadastrado; vinho indica trabalho associado e roxo identifica Patrícia. Nenhum ponto verde representa presença online sem prova.

## Teste multiagente nativo

- Colaboração nativa sequencial comprovada para Patrícia + seis especialistas: Felipe, Clara, Bruno, Marcelo, Gabriel e Larissa receberam pacotes internos, devolveram achados próprios, tiveram resultados persistidos e foram revisados pela Patrícia.
- Esta execução também comprova retomada agendada da construção sem presença da CEO. Não comprova dispatcher contínuo ou concorrente: os testes foram deliberadamente sequenciais e isolados.

## Pendências

- Conectar o contrato de lease a uma primitiva CAS durável do Control Plane; sem esse adapter o dispatcher permanece desligado.
- Transformar a sequência validada em protocolo repetível para trabalho interno não-test, sem liberar `WP-004` enquanto houver divergências.
- A projeção atual é renovável pela tarefa nativa e verificável, mas não é streaming ao vivo. Um adapter REST ao vivo continua condicionado a endpoint e autenticação próprios, ainda não disponíveis.
- Reconciliar a divergência de `TASK-002` com sua proveniência antes de qualquer despacho.
- Validar visualmente em navegador real e publicar somente se houver ambiente autorizado para esta branch.
- Comprovar um runtime independente da presença da CEO. Cadastro de agentes, tela e planejador não são essa prova.

## Próximo passo autorizado

Conectar e validar o adapter assim que o Control Plane expuser `GET/PUT /runtime/lease` com CAS transacional. Em paralelo, validar visualmente a interface em navegador real quando existir ambiente autorizado. Não usar `WP-004` como smoke test. Para implementar o endpoint agora falta acesso ao código/host do Control Plane; não presumir essa autoridade.

## Bloqueio

O contrato de lease existe e está testado, mas o MCP atual do Control Plane não expõe backend CAS durável; por isso execução contínua segue desativada. Para eliminar esse bloqueio será necessário acesso ao código/host do Control Plane ou a publicação de uma primitiva atômica equivalente. Permanecem também a ausência de endpoint autenticado para streaming ao vivo e de ambiente autorizado para QA visual/publicação. Nenhum gasto, contratação ou credencial foi assumido.
