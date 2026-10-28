// POST /api/diagnostico: recebe o pedido da página e dispara o GitHub Actions (repository_dispatch).
const crypto = require("crypto");
const { github, validarSite, texto, TOKEN } = require("./_comum");

const ORIGENS = ["popup", "landing", "site"];

module.exports = async (req, res) => {
  if (req.method !== "POST") return res.status(405).json({ erro: "método não permitido" });
  if (!TOKEN) return res.status(500).json({ erro: "servidor sem configuração" });
  const b = typeof req.body === "object" && req.body ? req.body : {};

  // Armadilhas para robôs: campo invisível preenchido ou envio rápido demais.
  if (b.website_confirm || (Number(b.t) && Date.now() - Number(b.t) < 2500)) {
    return res.status(200).json({ id: crypto.randomUUID() });
  }

  const site = validarSite(b.site);
  if (!site) return res.status(400).json({ erro: "Confira o endereço do site (ex.: suaempresa.com.br)." });
  const email = texto(b.email, 160).toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email)) {
    return res.status(400).json({ erro: "Confira o seu e-mail." });
  }
  if (b.consentimento !== true) {
    return res.status(400).json({ erro: "Precisamos do seu consentimento para enviar o resultado." });
  }

  const id = crypto.randomUUID();
  const payload = {
    id,
    site,
    email,
    nome: texto(b.nome),
    empresa: texto(b.empresa) || new URL(site).hostname.replace(/^www\./, ""),
    whatsapp: texto(b.whatsapp, 30),
    segmento: texto(b.segmento, 60),
    cargo: texto(b.cargo, 60),
    origem: ORIGENS.includes(b.origem) ? b.origem : "site",
  };
  const r = await github("/dispatches", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ event_type: "diagnostico", client_payload: payload }),
  });
  if (r.status !== 204) {
    console.error("dispatch falhou", r.status, await r.text());
    return res.status(502).json({ erro: "Não conseguimos iniciar a análise agora. Tente de novo em alguns minutos." });
  }
  return res.status(202).json({ id });
};
