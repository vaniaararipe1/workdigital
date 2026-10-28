// GET /api/status?id=...: estado do diagnóstico (só notas e mensagens; nada de dados pessoais).
const { github, TOKEN } = require("./_comum");

module.exports = async (req, res) => {
  const id = String((req.query && req.query.id) || "");
  if (!/^[A-Za-z0-9-]{8,64}$/.test(id)) return res.status(400).json({ erro: "id inválido" });
  if (!TOKEN) return res.status(500).json({ erro: "servidor sem configuração" });
  const r = await github(`/contents/status/${id}.json?ref=relatorios`, {
    headers: { Accept: "application/vnd.github.raw+json" },
  });
  res.setHeader("Cache-Control", "no-store");
  if (r.status === 404) return res.status(200).json({ estado: "na_fila" });
  if (!r.ok) return res.status(200).json({ estado: "na_fila" });
  let dados;
  try { dados = JSON.parse(await r.text()); } catch { return res.status(200).json({ estado: "na_fila" }); }
  const { estado, notas, mensagem, enviado_por_email } = dados;
  return res.status(200).json({ estado, notas, mensagem, enviado_por_email });
};
