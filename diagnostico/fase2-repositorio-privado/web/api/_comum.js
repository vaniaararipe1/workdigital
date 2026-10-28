// Funções compartilhadas pelas rotas da API (arquivos com "_" não viram rota no Vercel).
const REPO = process.env.GITHUB_REPO || "vaniaararipe1/workdigital-diagnosticos";
const TOKEN = process.env.GITHUB_TOKEN;

function github(caminho, opcoes = {}) {
  return fetch(`https://api.github.com/repos/${REPO}${caminho}`, {
    ...opcoes,
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      Accept: "application/vnd.github+json",
      "X-GitHub-Api-Version": "2022-11-28",
      "User-Agent": "workdigital-diagnostico",
      ...(opcoes.headers || {}),
    },
  });
}

// Validação básica do endereço. A validação completa (DNS, IPs privados, redirecionamentos) acontece no worker.
function validarSite(valor) {
  let s = String(valor || "").trim();
  if (!s || s.length > 300) return null;
  if (!/^https?:\/\//i.test(s)) s = "https://" + s;
  let u;
  try { u = new URL(s); } catch { return null; }
  if (!["http:", "https:"].includes(u.protocol) || u.username || u.password) return null;
  const h = u.hostname.toLowerCase();
  if (!h.includes(".") || h === "localhost" || h.endsWith(".local") || h.endsWith(".internal")) return null;
  if (/^\d+(\.\d+){3}$/.test(h) || h.startsWith("[")) return null; // IP direto não é aceito
  if (u.port && !["80", "443"].includes(u.port)) return null;
  return u.origin + (u.pathname === "/" ? "/" : u.pathname);
}

function texto(v, max = 120) {
  return String(v || "").replace(/[\u0000-\u001f]/g, " ").trim().slice(0, max);
}

module.exports = { github, validarSite, texto, REPO, TOKEN };
