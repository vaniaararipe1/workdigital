// GET  /api/revisao?p=PASTA&k=CHAVE  → pontos pendentes de um diagnóstico, para a página de revisão
// POST /api/revisao                  → salva a revisão aprovada no revisao.json (branch relatorios)
// O link (com a chave aleatória de 32 caracteres) só vai no e-mail interno da Vania.
const crypto = require("crypto");
const { github, TOKEN } = require("./_comum");

const SITUACOES = ["ok", "atencao", "problema"];
const FASES = ["Fazer primeiro", "Em seguida", "Quando possível"];
const MAX = 3000;

function semMarca(t) { return String(t || "").replace(/^\s*\[RASCUNHO\]\s*/i, "").trim(); }
function limpo(t) { return String(t == null ? "" : t).replace(/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/g, "").trim().slice(0, MAX); }

function chaveConfere(esperada, recebida) {
  const a = Buffer.from(String(esperada || "")), b = Buffer.from(String(recebida || ""));
  return a.length === 32 && a.length === b.length && crypto.timingSafeEqual(a, b);
}

async function lerJson(caminho) {
  const r = await github(`/contents/${caminho}?ref=relatorios`);
  if (r.status === 404) return null;
  if (!r.ok) throw new Error("github " + r.status);
  const j = await r.json();
  return { dados: JSON.parse(Buffer.from(j.content, "base64").toString("utf8")), sha: j.sha };
}

async function carregar(p, k) {
  if (!/^[a-z0-9.-]{3,120}-\d{4}-\d{2}-\d{2}$/.test(p || "") || !/^[0-9a-f]{32}$/.test(k || "")) return null;
  const rev = await lerJson(`relatorios/${p}/revisao.json`);
  if (!rev || !chaveConfere(rev.dados.chave_revisao, k)) return null;
  return rev;
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  if (!TOKEN) return res.status(500).json({ erro: "servidor sem configuração" });
  try {
    if (req.method === "GET") return await mostrar(req, res);
    if (req.method === "POST") return await aprovar(req, res);
    return res.status(405).json({ erro: "método não permitido" });
  } catch (e) {
    console.error(e);
    return res.status(502).json({ erro: "Não conseguimos falar com o servidor agora. Tente de novo em alguns minutos." });
  }
};

async function mostrar(req, res) {
  const q = req.query || {};
  const rev = await carregar(String(q.p || ""), String(q.k || ""));
  if (!rev) return res.status(404).json({ erro: "Link de revisão inválido ou expirado." });
  const p = String(q.p);
  const lead = (await lerJson(`relatorios/${p}/lead.json`)) || { dados: {} };
  const envio = (await lerJson(`relatorios/${p}/envio.json`)) || { dados: {} };
  const d = rev.dados;
  return res.status(200).json({
    empresa: d.empresa, url: d.url, data: d.data_analise,
    contato: { nome: lead.dados.nome || "", email: lead.dados.email || "" },
    ja_enviada: !!envio.dados.revisada_enviada_em,
    nota_pessoal: semMarca((d.nota_pessoal || {}).texto),
    avaliacoes: (d.avaliacoes || []).map((a) => ({
      id: a.id, titulo: a.titulo, situacao: a.situacao, o_que_vimos: semMarca(a.o_que_vimos),
      o_que_significa: semMarca(a.o_que_significa), o_que_fazer: semMarca(a.o_que_fazer),
      encontrado: String(a.sinais_coletados || "").slice(0, 600),
    })),
    plano: ((d.plano || {}).itens || []).map((it, i) => ({ i, fase: it.fase, acao: semMarca(it.acao) })),
  });
}

async function aprovar(req, res) {
  const b = typeof req.body === "object" && req.body ? req.body : {};
  const p = String(b.p || "");
  const rev = await carregar(p, String(b.k || ""));
  if (!rev) return res.status(404).json({ erro: "Link de revisão inválido ou expirado." });
  const d = rev.dados;
  const faltas = [];

  const nota = limpo(b.nota_pessoal);
  if (!nota) faltas.push("Escreva a nota pessoal.");

  const recebidas = Array.isArray(b.avaliacoes) ? b.avaliacoes : [];
  const avaliacoes = (d.avaliacoes || []).map((a) => {
    const n = recebidas.find((x) => x && x.id === a.id) || {};
    const situacao = SITUACOES.includes(n.situacao) ? n.situacao : a.situacao;
    const novo = { ...a, status: "revisado", situacao,
      o_que_vimos: limpo(n.o_que_vimos), o_que_significa: limpo(n.o_que_significa), o_que_fazer: limpo(n.o_que_fazer) };
    if (!novo.o_que_vimos) faltas.push(`"${a.titulo}": preencha o que vimos.`);
    if (situacao !== "ok" && !novo.o_que_fazer) faltas.push(`"${a.titulo}": preencha o que fazer (obrigatório quando pode melhorar ou é problema).`);
    return novo;
  });

  const antigos = (d.plano || {}).itens || [];
  const itens = (Array.isArray(b.plano) ? b.plano : []).slice(0, 40).map((x) => {
    const base = Number.isInteger(x && x.i) && antigos[x.i] ? antigos[x.i] : { area: "", esforco: "" };
    return { ...base, fase: FASES.includes(x && x.fase) ? x.fase : "Em seguida", acao: limpo(x && x.acao) };
  }).filter((x) => x.acao);
  if (!itens.length) faltas.push("O plano precisa de pelo menos uma ação.");

  if (faltas.length) return res.status(400).json({ erro: "Falta preencher:", faltas });

  const novo = {
    ...d,
    aprovar_rascunhos: true,
    enviar_ao_lead: b.acao === "aprovar_enviar" ? true : !!d.enviar_ao_lead,
    nota_pessoal: { status: "revisado", texto: nota },
    avaliacoes,
    plano: { status: "revisado", itens },
  };
  const r = await github(`/contents/relatorios/${p}/revisao.json`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      message: `Revisão aprovada: ${p}${novo.enviar_ao_lead ? " (enviar ao cliente)" : ""}`,
      content: Buffer.from(JSON.stringify(novo, null, 2), "utf8").toString("base64"),
      sha: rev.sha, branch: "relatorios",
    }),
  });
  if (r.status === 409 || r.status === 422) {
    return res.status(409).json({ erro: "Este diagnóstico mudou enquanto você revisava. Recarregue a página e tente de novo." });
  }
  if (!r.ok) throw new Error("github put " + r.status + " " + (await r.text()));
  return res.status(200).json({ ok: true, enviar: novo.enviar_ao_lead });
}
