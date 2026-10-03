# Contato expansível — Work Digital

Incluído globalmente pelo footer.js. Inclusão independente: `<script src="/contact.js" defer></script>`.

Configurar no topo de contact.js:
- `URL_ENVIO`: endpoint HTTPS que aceita POST JSON com nome, email, empresa, ideia, origem.
- `URL_PRIVACIDADE`: link oficial, ainda não identificado nos arquivos atuais. O texto aparece, mas o link só fica habilitado com uma URL real.

Também pode definir `window.WD_CONTACT_CONFIG = { endpoint: "...", privacyUrl: "..." }` antes do script. Não coloque credenciais secretas no navegador.

GSAP é carregado pela CDN solicitada. Se falhar, o painel abre sem animação.

O envio não é simulado. Sem endpoint, aparece o estado de erro com a pendência explicada. Com endpoint HTTP 2xx, aparece a confirmação; HTTP de erro ou timeout mostra erro. Nenhuma mensagem foi enviada durante a validação.

Menu original preservado: SOLICITAR PROPOSTA abre o painel de contato 477×671; telas baixas permitem rolar o conteúdo dentro do painel. Mobile até 768px: painel 100dvh, com rolagem interna quando necessário.

API opcional: `WorkDigitalContact.abrirContato(trigger)`, `.fecharContato()`, `.enviarFormulario(dados)`.
