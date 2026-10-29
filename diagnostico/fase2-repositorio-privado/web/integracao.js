/* Liga a landing (index.html) ao diagnóstico, sem depender do visual da página.
 *
 * O que a página precisa manter (o resto pode mudar à vontade):
 *   - formulários com class="lead-form" e os campos name="nome", "email", "whatsapp", "site_url",
 *     "segmento", "cargo" e "consentimento_lgpd";
 *   - um <p class="form-status"> dentro de cada formulário;
 *   - a linha <script src="/integracao.js" defer></script>.
 *
 * A página chama window.WORK_DIAGNOSTICO_SUBMIT ao enviar. Aqui: envia ao /api/diagnostico e, com o
 * pedido aceito, leva o visitante para /relatorio?id=..., que acompanha esse mesmo pedido e mostra o
 * resultado (sem iniciar outra análise). Se o envio falhar, a pessoa fica no formulário e vê o erro.
 */
(function () {
  "use strict";
  var q = new URLSearchParams(location.search);

  // Veio do popup do RD Station (cookie wd_lead) ou de um link com site e e-mail: página de um clique.
  if ((q.get("email") && (q.get("site") || q.get("url") || q.get("site_url"))) || /(?:^|;\s*)wd_lead=/.test(document.cookie)) {
    location.replace("/relatorio" + location.search);
    return;
  }

  var inicio = Date.now();

  // A página mostra uma mensagem genérica quando o envio falha; esta troca pela mensagem do servidor.
  function erroDepois(form, msg) {
    setTimeout(function () {
      var n = form.querySelector(".form-status");
      if (n) { n.dataset.state = "error"; n.textContent = msg; }
    }, 0);
  }

  window.WORK_DIAGNOSTICO_SUBMIT = async function (dados, form, signal) {
    var corpo = {
      site: dados.site_url, email: dados.email, nome: dados.nome, whatsapp: dados.whatsapp,
      segmento: dados.segmento, cargo: dados.cargo, origem: "landing",
      consentimento: dados.consentimento_lgpd === "sim", t: inicio
    };
    var r;
    try {
      r = await fetch("/api/diagnostico", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(corpo), signal: signal });
    } catch (e) {
      if (e && e.name === "AbortError") throw e;
      erroDepois(form, "Sem conexão. Confira sua internet e tente de novo.");
      return { success: false };
    }
    var j = {};
    try { j = await r.json(); } catch (e) { /* resposta vazia */ }
    if (!r.ok || !j.id) {
      erroDepois(form, j.erro || "Não conseguimos iniciar a análise agora. Tente de novo em alguns minutos.");
      return { success: false };
    }
    location.assign("/relatorio?id=" + encodeURIComponent(j.id));
    return { success: true };
  };
})();
