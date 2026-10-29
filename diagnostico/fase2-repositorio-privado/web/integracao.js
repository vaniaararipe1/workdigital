/* Liga a landing (index.html) ao diagnóstico, sem depender do visual da página.
 *
 * O que a página precisa manter (o resto pode mudar à vontade):
 *   - formulários com class="lead-form" e os campos name="nome", "email", "whatsapp", "site_url",
 *     "segmento", "cargo" e "consentimento_lgpd";
 *   - um <p class="form-status"> dentro de cada formulário;
 *   - a linha <script src="/integracao.js" defer></script>.
 *
 * A página chama window.WORK_DIAGNOSTICO_SUBMIT ao enviar. Aqui: envia ao /api/diagnostico,
 * acompanha a análise e mostra as três notas na própria página.
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
  var PRAZO = 2;
  var WHATSAPP = "https://wa.me/5511993916363?text=" +
    encodeURIComponent("Olá! Fiz a análise do meu site pela página da Work Digital e quero conversar.");
  var NOMES = { performance: "Velocidade", ux: "Experiência e conversão", seo: "SEO e visibilidade" };

  var css = document.createElement("style");
  css.textContent =
    ".wd-res{margin-top:16px;padding:18px;border:1px solid #c9b4f04a;border-radius:12px;background:#15151b;color:#fff;font-size:14px;line-height:1.55}" +
    ".wd-res h3{font-size:19px;margin:0 0 6px}.wd-res p{margin:0 0 10px;color:#d6d1dd}" +
    ".wd-barra{height:6px;border-radius:6px;background:#2a2733;overflow:hidden;margin:12px 0 4px}" +
    ".wd-barra span{display:block;height:100%;width:5%;background:linear-gradient(90deg,#6025E1,#04CD8F);transition:width 1s}" +
    ".wd-notas{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin:12px 0}" +
    ".wd-nota{border:1px solid #ffffff22;border-radius:10px;padding:12px 4px;text-align:center}" +
    ".wd-nota b{display:block;font-family:'Space Grotesk',sans-serif;font-size:30px;line-height:1}" +
    ".wd-nota span{display:block;font-size:11.5px;color:#c1becb;margin-top:6px;line-height:1.3}" +
    ".wd-bom{color:#04CD8F}.wd-medio{color:#b79bff}.wd-ruim{color:#ff6fa3}" +
    ".wd-vania{display:flex;gap:12px;align-items:flex-start;border-top:1px solid #ffffff22;padding-top:14px;margin-top:4px}" +
    ".wd-vania img{width:56px;height:56px;border-radius:50%;border:2px solid #6025E1;flex:none;object-fit:cover}" +
    ".wd-vania a{display:inline-block;margin-top:8px;color:#04CD8F;font-weight:800;text-decoration:none}";
  document.head.appendChild(css);

  function el(html) { var d = document.createElement("div"); d.className = "wd-res"; d.setAttribute("aria-live", "polite"); d.innerHTML = html; return d; }
  function esc(t) { return String(t == null ? "" : t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

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
    acompanhar(form, j.id);
    return { success: true };
  };

  function acompanhar(form, id) {
    var caixa = el('<h3>Estamos analisando o seu site</h3><p>Leva de 3 a 6 minutos. Pode deixar esta página aberta ou fechar: o resultado também vai para o seu e-mail.</p><div class="wd-barra"><span></span></div>');
    form.appendChild(caixa);
    var barra = caixa.querySelector(".wd-barra span");
    var t0 = Date.now(), ESPERADO = 5 * 60 * 1000, LIMITE = 15 * 60 * 1000;
    var anim = setInterval(function () { barra.style.width = Math.round(5 + Math.min(0.95, (Date.now() - t0) / ESPERADO) * 90) + "%"; }, 1000);
    function fim(html) { clearInterval(anim); caixa.innerHTML = html; }
    function consultar() {
      fetch("/api/status?id=" + encodeURIComponent(id)).then(function (r) { return r.json(); }).then(function (s) {
        if (s.estado === "pronto") {
          var st = form.querySelector(".form-status");
          if (st) st.textContent = "";
          return fim(resultado(s));
        }
        if (s.estado === "limite") return fim("<h3>Já recebemos este pedido</h3><p>" + esc(s.mensagem) + '</p><p><a href="' + WHATSAPP + '" style="color:#04CD8F;font-weight:800">Falar no WhatsApp</a></p>');
        if (s.estado === "erro") return fim("<h3>Não conseguimos concluir agora</h3><p>" + esc(s.mensagem) + "</p>");
        if (Date.now() - t0 > LIMITE) return fim("<h3>Está demorando mais que o normal</h3><p>Seu pedido está na fila. Assim que a análise terminar, o resultado vai para o seu e-mail.</p>");
        setTimeout(consultar, 8000);
      }).catch(function () { setTimeout(consultar, 10000); });
    }
    setTimeout(consultar, 15000);
  }

  function resultado(s) {
    var notas = "";
    Object.keys(NOMES).forEach(function (k) {
      var n = s.notas ? s.notas[k] : null;
      var cls = n == null ? "" : (n >= 80 ? "wd-bom" : n >= 50 ? "wd-medio" : "wd-ruim");
      notas += '<div class="wd-nota"><b class="' + cls + '">' + (n == null ? "—" : esc(n)) + "</b><span>" + NOMES[k] +
        (n == null ? "<br>não foi possível medir" : "") + "</span></div>";
    });
    return "<h3>Pronto! Veja as suas notas</h3>" +
      '<div class="wd-notas">' + notas + "</div>" +
      "<p>" + (s.enviado_por_email === false ? "O relatório será enviado para o seu e-mail." : "Enviamos o resultado técnico em PDF para o seu e-mail.") +
      " Notas de 0 a 100; o relatório explica como cada uma foi calculada.</p>" +
      '<div class="wd-vania"><img src="/vania.webp" alt="Vania Araripe"><div><b>Prazer, eu sou a Vania Araripe, da Work Digital.</b> ' +
      "Cuido da gestão de projetos digitais e vou olhar o seu site pessoalmente. A avaliação completa, revisada por mim, chega em até <b>" + PRAZO +
      ' dias úteis</b>. Quer adiantar a conversa?<br><a href="' + WHATSAPP + '">Falar no WhatsApp</a></div></div>';
  }
})();
