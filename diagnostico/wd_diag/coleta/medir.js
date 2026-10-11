// Executado dentro da página renderizada. Só lê o DOM: não clica, não envia formulários.
() => {
  const vw = window.innerWidth, vh = window.innerHeight;
  const CTA_RE = /(contato|contrat|orçamento|orcamento|fale|whats|comprar|compre|agend|agende|peça|peca|solicit|quero|assine|assinar|cadastr|ligue|reserv|convers|começar|comecar|encomend|baixe|baixar|inscrev|matricul|saiba mais|ver planos|ver produtos|experiment|teste grátis|teste gratis|chamar|pedido|pedir|cotação|cotacao|simul|get started|contact|buy|book|start)/i;
  const WA_RE = /(wa\.me\/|api\.whatsapp\.com|web\.whatsapp\.com|whatsapp:\/\/|chat\.whatsapp\.com)/i;

  const visivel = (el) => {
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return false;
    const s = getComputedStyle(el);
    return s.visibility !== 'hidden' && s.display !== 'none' && parseFloat(s.opacity || '1') > 0.05;
  };
  const texto = (el) => (el.innerText || el.value || el.getAttribute('aria-label') || el.title || '').replace(/\s+/g, ' ').trim();
  const topoAbs = (el) => el.getBoundingClientRect().top + window.scrollY;
  const fixo = (el) => { for (let e = el; e && e !== document.body; e = e.parentElement) { const p = getComputedStyle(e).position; if (p === 'fixed' || p === 'sticky') return true; } return false; };
  const corOpaca = (c) => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return false; const p = m[1].split(',').map(x => parseFloat(x)); return p.length < 4 || p[3] > 0.1; };
  const pareceBotao = (el) => {
    if (el.tagName === 'BUTTON' || el.getAttribute('role') === 'button' || el.tagName === 'INPUT') return true;
    const s = getComputedStyle(el);
    const fundo = corOpaca(s.backgroundColor) && s.backgroundColor !== getComputedStyle(document.body).backgroundColor;
    const borda = parseFloat(s.borderTopWidth) > 0 && parseFloat(s.borderRadius) > 0;
    const pad = parseFloat(s.paddingLeft) >= 8 && parseFloat(s.paddingTop) >= 4;
    return (fundo || borda) && pad;
  };

  // ---------- chamadas para ação ----------
  const clicaveis = [...document.querySelectorAll('a[href], button, input[type=submit], input[type=button], [role=button]')].filter(visivel);
  const ctas = [];
  for (const el of clicaveis) {
    const t = texto(el).slice(0, 80);
    const href = el.getAttribute('href') || '';
    const botao = pareceBotao(el);
    const contatoDireto = WA_RE.test(href) || href.toLowerCase().startsWith('tel:');
    const chave = CTA_RE.test(t) || contatoDireto;
    const noMenu = !!el.closest('nav, [role=navigation]');
    if (!t && !chave) continue;
    if (/^(pular|ir) para|^skip to/i.test(t) || topoAbs(el) < 0) continue;  // links de acessibilidade
    if (/^(aceitar|aceito|recusar|rejeitar|concordo|entendi|ok|fechar|close|accept|reject|prefer[êe]ncias|configurar cookies|abrir menu|menu|fechar menu|alternar menu|toggle menu|pt|en|es)$/i.test(t)) continue;
    if (/(previous|next|anterior|pr[óo]ximo) slide|go to slide|^slide \d|carousel|carrossel/i.test(t) || el.closest('.swiper-pagination, .slick-dots, .owl-dots, .carousel-indicators, .flickity-page-dots')) continue;
    if (el.closest('[id*=cookie i], [class*=cookie i], [id*=consent i], [class*=consent i], [class*=lgpd i]')) continue;
    if (!botao && !chave) continue;
    if (noMenu && !botao) continue;
    const r = el.getBoundingClientRect();
    ctas.push({ texto: t, href: href.slice(0, 200), topo: Math.round(topoAbs(el)), largura: Math.round(r.width), altura: Math.round(r.height),
                botao, palavra_chave: chave, contato: contatoDireto, fixo: fixo(el) });
  }
  const ctasDobra = ctas.filter(c => c.topo < vh || c.fixo);
  const ctaForte = ctasDobra.filter(c => c.palavra_chave && (c.botao || (c.contato && c.texto.length >= 8)));

  // ---------- contato direto ----------
  const contato = [...document.querySelectorAll('a[href]')].map(a => {
    const href = a.getAttribute('href') || '';
    const tipo = WA_RE.test(href) ? 'whatsapp' : href.toLowerCase().startsWith('tel:') ? 'telefone' : null;
    if (!tipo) return null;
    const vis = visivel(a);
    return { tipo, href: href.slice(0, 200), visivel: vis, fixo: vis && fixo(a), topo: vis ? Math.round(topoAbs(a)) : null, texto: texto(a).slice(0, 60) };
  }).filter(Boolean);

  // ---------- formulários ----------
  const formularios = [...document.querySelectorAll('form')].map(f => {
    const campos = [...f.querySelectorAll('input, select, textarea')].filter(i => {
      const t = (i.getAttribute('type') || 'text').toLowerCase();
      return !['hidden', 'submit', 'button', 'reset', 'image'].includes(t) && i.getAttribute('aria-hidden') !== 'true' && visivel(i);
    });
    const busca = f.getAttribute('role') === 'search' || campos.some(i => (i.type === 'search' || ['s', 'q', 'search', 'busca'].includes(i.name))) && campos.length <= 2;
    const senha = campos.some(i => i.type === 'password');
    const comRotulo = campos.filter(i => {
      if (i.getAttribute('aria-label') || i.getAttribute('aria-labelledby') || i.title) return true;
      if (i.id && document.querySelector(`label[for="${CSS.escape(i.id)}"]`)) return true;
      return !!i.closest('label');
    }).length;
    const soPlaceholder = campos.filter(i => i.placeholder).length;
    return { campos: campos.length, com_rotulo: comRotulo, com_placeholder: soPlaceholder, busca, login: senha,
             visivel: visivel(f) || campos.length > 0, topo: Math.round(topoAbs(f)),
             nomes: campos.map(i => i.name || i.id || i.type).slice(0, 15) };
  }).filter(f => f.campos > 0 && !f.busca && !f.login);

  const FORM_EXT = /(rdstation|hsforms|hubspot|typeform|forms\.gle|docs\.google\.com\/forms|jotform|tally\.so|formstack|leadster|cognitoforms)/i;
  const formulariosExternos = [...document.querySelectorAll('iframe[src]')].map(f => f.getAttribute('src')).filter(s => FORM_EXT.test(s)).map(s => s.slice(0, 160));

  // ---------- leitura no celular ----------
  let totalChars = 0, pequenos = 0;
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = walker.nextNode())) {
    const t = n.textContent.trim();
    if (!t || !n.parentElement || !visivel(n.parentElement)) continue;
    const tag = n.parentElement.tagName;
    if (['SCRIPT', 'STYLE', 'NOSCRIPT'].includes(tag)) continue;
    const fs = parseFloat(getComputedStyle(n.parentElement).fontSize);
    totalChars += t.length;
    if (fs < 12) pequenos += t.length;
  }

  // ---------- alvos de toque ----------
  const alvos = clicaveis.filter(el => {
    const pai = el.parentElement;
    if (el.tagName === 'A' && pai && ['P', 'LI', 'SPAN', 'TD'].includes(pai.tagName) && (pai.innerText || '').trim().length > texto(el).length + 15) return false; // link no meio do texto
    return true;
  });
  const pequenosAlvos = alvos.filter(el => { const r = el.getBoundingClientRect(); return r.width < 24 || r.height < 24; })
    .map(el => ({ texto: texto(el).slice(0, 40), largura: Math.round(el.getBoundingClientRect().width), altura: Math.round(el.getBoundingClientRect().height) }));

  // ---------- títulos ----------
  const h1s = [...document.querySelectorAll('h1')].map(h => ({ texto: texto(h).slice(0, 200), visivel: visivel(h), topo: Math.round(topoAbs(h)) }));
  const primeiroTitulo = [...document.querySelectorAll('h1, h2')].filter(visivel).map(h => ({ tag: h.tagName.toLowerCase(), texto: texto(h).slice(0, 200), topo: Math.round(topoAbs(h)) }))[0] || null;

  // ---------- prova social (sinais textuais; julgamento humano) ----------
  const corpo = (document.body.innerText || '').replace(/\s+/g, ' ');
  const SOCIAL = [/depoimentos?/i, /o que (nossos )?clientes (dizem|falam)/i, /avaliaç(ão|ões)/i, /nossos clientes/i, /clientes atendidos/i, /\bcases?\b/i, /quem confia/i, /parceiros/i, /★|⭐/, /estrelas/i, /testemunhos?/i, /google reviews?/i];
  const sinaisSociais = [];
  for (const re of SOCIAL) { const m = corpo.match(re); if (m) { const i = Math.max(0, m.index - 40); sinaisSociais.push(corpo.slice(i, m.index + m[0].length + 40).trim()); } }
  const widgetsSociais = [...document.querySelectorAll('[class*=testimonial i], [class*=depoimento i], [class*=review i], [class*=trustindex i], [class*=elfsight i]')].filter(visivel).length;

  const meta = document.querySelector('meta[name=viewport]');
  return {
    viewport: { largura: vw, altura: vh },
    meta_viewport: meta ? meta.getAttribute('content') : null,
    largura_documento: document.documentElement.scrollWidth,
    altura_documento: document.documentElement.scrollHeight,
    ctas_total: ctas.length,
    ctas_dobra: ctasDobra.slice(0, 8),
    ctas_fortes_dobra: ctaForte.slice(0, 8),
    primeiro_cta: ctas.filter(c => c.palavra_chave).sort((a, b) => a.topo - b.topo)[0] || null,
    contato_direto: contato.slice(0, 20),
    formularios,
    formularios_externos: formulariosExternos,
    texto_total_chars: totalChars,
    texto_pequeno_chars: pequenos,
    alvos_total: alvos.length,
    alvos_pequenos: pequenosAlvos.slice(0, 30),
    alvos_pequenos_total: pequenosAlvos.length,
    h1s,
    primeiro_titulo: primeiroTitulo,
    sinais_prova_social: sinaisSociais.slice(0, 6),
    widgets_prova_social: widgetsSociais,
  };
}
