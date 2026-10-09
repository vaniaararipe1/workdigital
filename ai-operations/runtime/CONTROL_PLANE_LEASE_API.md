# Contrato mínimo — lease atômico do Control Plane

Este contrato é o requisito de backend para ativar o dispatcher. Implementá-lo não ativa a fila automaticamente: a validação ponta a ponta e `runtime_verified=true` continuam obrigatórios.

## Recurso

`GET /runtime/lease` retorna JSON com `version`, `owner`, `acquired_at` e `expires_at`. Um registro vazio retorna versão inteira e campos nulos. A resposta deve usar TLS e a mesma autenticação do Control Plane.

`PUT /runtime/lease` recebe o próximo documento completo e exige `If-Match: "lease-v{expectedVersion}"`.

- Se a versão persistida for igual à esperada, o servidor grava o documento e responde 200 ou 204 numa única transação.
- Se for diferente, responde 409 ou 412 sem alterar o registro.
- Nunca realiza upsert cego, last-write-wins ou comparação apenas em memória.

## Invariantes

- `version` é inteiro monotônico e incrementa exatamente uma vez por escrita aceita.
- `owner` é identidade única da execução, não nome do agente.
- O servidor valida timestamps ISO 8601 e `expires_at > acquired_at` quando houver owner.
- Um índice/chave única garante que exista um único registro de lease para o dispatcher.
- Log de auditoria preserva versão anterior, nova versão, owner e horário do servidor.
- Relógio do servidor é a autoridade para rejeitar lease já expirado; o cliente continua enviando os timestamps para auditoria.

## Integração existente

`http-lease-store.js` implementa o adapter `read` + `compareAndSwap` exigido por `lease.js`. Ele aceita somente HTTPS, suporta Bearer token, usa timeout e trata 409/412 como disputa legítima. Enquanto esse endpoint não existir e não for testado contra o Control Plane real, `control-plane-capabilities.json` deve continuar com `atomic_compare_and_swap=false` e `lease_backend=false`.
