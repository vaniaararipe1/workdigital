# Thumbs reais dos projetos (pasta do Drive "thumbs-work-digital"): pôster + vídeo no hover, na página de Cases e na home
import json, os, re, shutil
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'thumbs')
DATA = json.load(open(os.path.join(SRC, 'dados-projetos.json')))
SIZE = {'grande': 'large', 'medio': 'medium', 'médio': 'medium', 'pequeno': 'small'}
DIM = {'large': (2400, 1125), 'medium': (1600, 1200), 'small': (1200, 1500)}

def sub1(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)

def copy_files(out, slugs):
    os.makedirs(out + '/thumbs', exist_ok=True)
    for s in slugs:
        for ext in ('webp', 'mp4', 'webm'):
            f = f'{SRC}/{s}.{ext}'
            if os.path.exists(f):
                shutil.copy(f, f'{out}/thumbs/{s}.{ext}')

# JS comum: liga pôster + vídeo num container; vídeo só carrega/toca com mouse (nunca no celular, modo leve ou movimento reduzido)
MEDIA_JS = r'''
const WD_CAN_PLAY = matchMedia("(hover: hover) and (pointer: fine)").matches && !matchMedia("(prefers-reduced-motion: reduce)").matches;
function wdThumb(box, slug, w, h) {
  box.innerHTML = `<img class="vm-poster" src="./thumbs/${slug}.webp" width="${w}" height="${h}" alt="" loading="lazy" decoding="async">`;
  let video = null, loaded = false, want = false;
  function load() {
    if (loaded || !WD_CAN_PLAY) return; loaded = true;
    video = document.createElement("video");
    video.className = "vm-video"; video.muted = true; video.loop = true; video.playsInline = true; video.preload = "none";
    video.setAttribute("muted", ""); video.setAttribute("playsinline", ""); video.setAttribute("aria-hidden", "true");
    video.poster = `./thumbs/${slug}.webp`;
    video.innerHTML = `<source src="./thumbs/${slug}.webm" type="video/webm"><source src="./thumbs/${slug}.mp4" type="video/mp4">`;
    box.appendChild(video);
  }
  if (WD_CAN_PLAY && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { load(); io.disconnect(); } }, { rootMargin: "200px" });
    io.observe(box);
  }
  return {
    play() { if (!WD_CAN_PLAY) return; want = true; load(); const p = video.play(); if (p) p.then(() => { if (want) box.classList.add("vm-on"); }).catch(() => {}); },
    stop() { want = false; box.classList.remove("vm-on"); if (video) { video.pause(); try { video.currentTime = 0; } catch (e) {} } },
    set(nslug, nw, nh) { this.stop(); slug = nslug; w = nw; h = nh; loaded = false; video = null; box.innerHTML = `<img class="vm-poster" src="./thumbs/${slug}.webp" alt="" decoding="async">`; }
  };
}
'''
MEDIA_CSS = '''
/* Thumbs: pôster + vídeo no hover (o vídeo aparece por cima com fade quando começa a tocar) */
.vm{position:absolute;inset:0;overflow:hidden;transition:transform 1.1s cubic-bezier(.22,1,.36,1)}
.vm img,.vm video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.vm video{opacity:0;transition:opacity .2s ease}
.vm.vm-on video{opacity:1}
'''

def cases(t, out):
    cs = sorted(DATA['cases'], key=lambda c: c['ordem'])
    copy_files(out, [c['slug'] for c in cs])
    projs, med = [], 0
    for c in cs:
        size = SIZE[c['formato']]
        off = False
        if size == 'medium':
            med += 1; off = med % 2 == 0
        projs.append({'slug': c['slug'], 'client': c['cliente'], 'title': c['frase'], 'services': c['servicos'][:3],
                      'size': size, 'offset': off, 'w': DIM[size][0], 'h': DIM[size][1], 'link': c.get('link', '')})
    i = t.index('const projects = ['); j = t.index('];', i) + 2
    t = t[:i] + 'const projects = ' + json.dumps(projs, ensure_ascii=False) + ';' + t[j:]
    # desenhos provisórios (canvas) saem; entra pôster + vídeo
    i = t.index('/* ---------- Generative thumbnails'); j = t.index('/* ---------- Render ---------- */', i)
    t = t[:i] + MEDIA_JS + '\n' + t[j:]
    t = sub1(t, '<div class="media"><canvas></canvas><span class="tag mono">Preview</span></div>', '<div class="media"><div class="vm"></div></div>')
    t = sub1(t, 'const ctl = mountCanvas(a.querySelector("canvas"), p);', 'const ctl = wdThumb(a.querySelector(".vm"), p.slug, p.w, p.h);')
    t = sub1(t, '<div class="floater" id="floater" aria-hidden="true"><canvas></canvas></div>', '<div class="floater" id="floater" aria-hidden="true"><div class="vm"></div></div>')
    t = sub1(t, 'const fctl = mountCanvas(floater.querySelector("canvas"), projects[0]);', 'const fctl = wdThumb(floater.querySelector(".vm"), projects[0].slug, projects[0].w, projects[0].h); floater.style.aspectRatio = projects[0].w + " / " + projects[0].h;')
    t = sub1(t, 'fctl.set(projects.find(p => p.slug === r.dataset.slug)); fctl.play();', 'const pr = projects.find(p => p.slug === r.dataset.slug); floater.style.aspectRatio = pr.w + " / " + pr.h; fctl.set(pr.slug, pr.w, pr.h); fctl.play();')
    t, n = re.subn(r'/\* Redraw once fonts arrive.*?\n.*?\n', '', t, count=1); assert n == 1
    t = sub1(t, '<sup id="count">(12)</sup>', f'<sup id="count">({len(projs)})</sup>')
    # zoom do hover passa do canvas para a mídia nova
    t = t.replace('.card:hover .media canvas, .card:focus-visible .media canvas { transform: scale(1.045); }',
                  '.card:hover .media .vm, .card:focus-visible .media .vm { transform: scale(1.045); }')
    t = sub1(t, '</style>', MEDIA_CSS + '.floater .vm{position:absolute}\n/* cada card mantém o formato da arte em qualquer tela (sem corte) */\n.grid .card .media{aspect-ratio:4/5}.grid .card.large .media{aspect-ratio:16/7.5}.grid .card.medium .media{aspect-ratio:4/3}\n</style>')
    return t

def home(t, out):
    # Layout original da home (Bacio alto, Linea larga, STW e CBPq quadrados).
    # As artes -home já vêm no tamanho exato de cada card: preenchem o card sem recorte.
    hs = DATA['home']
    man = {m['arquivos']['webp']['arquivo'][:-5]: m for m in json.load(open(os.path.join(SRC, 'manifesto-thumbs.json')))['home']}
    copy_files(out, [h['slug'] for h in hs])
    i = t.index('<a class="wd-works-card"'); j = t.rindex('<a class="wd-works-card"'); j = t.index('</a>', j) + 4
    cards = re.findall(r'<a class="wd-works-card".*?</a>', t[i:j], flags=re.S)
    assert len(cards) == 4
    new = []
    for c, h in zip(cards, hs):
        w, hh = man[h['slug']]['poster_px']
        c = c.replace('<a class="wd-works-card"', f'<a class="wd-works-card" style="--wd-ar:{w} / {hh}"', 1)
        c = re.sub(r'<h3>.*?</h3>', f'<h3>{h["titulo"]}</h3>', c, count=1, flags=re.S)
        c = re.sub(r'<div class="wd-works-media">.*?</div>', f'<div class="wd-works-media" data-thumb="{h["slug"]}" data-w="{w}" data-h="{hh}"><div class="vm"></div></div>', c, count=1, flags=re.S)
        c = re.sub(r'<p class="wd-works-description">.*?</p>', f'<p class="wd-works-description">{h["descricao"]}</p>', c, count=1, flags=re.S)
        new.append(c)
    t = t[:i] + '\n   '.join(new) + t[j:]
    t = t.replace('</body>', '<script>\n' + MEDIA_JS + HOME_JS + '</script>\n</body>', 1)
    t = t.replace('</head>', '<style>' + MEDIA_CSS + HOME_CSS + '</style>\n</head>', 1)
    return t

HOME_JS = r'''
document.querySelectorAll(".wd-works-card").forEach(card => {
  const m = card.querySelector(".wd-works-media"); if (!m) return;
  const ctl = wdThumb(m.querySelector(".vm"), m.dataset.thumb, +m.dataset.w, +m.dataset.h);
  card.addEventListener("mouseenter", ctl.play); card.addEventListener("mouseleave", ctl.stop);
  card.addEventListener("focus", ctl.play); card.addEventListener("blur", ctl.stop);
});
'''

# A seção Works define o CSS mais abaixo no documento, por isso os seletores levam .wd-works-section.
# Grade original: as alturas vêm da proporção das artes (Linea e os quadrados têm a mesma altura,
# e o Bacio ocupa as duas linhas), então a imagem cobre o card sem recorte visível.
HOME_CSS = r'''
.wd-works-section .wd-works-grid{grid-template-rows:auto auto}
.wd-works-section .wd-works-card:nth-child(n){min-height:0;background:#1d0f36;color:#fff}
.wd-works-section .wd-works-card:nth-child(n):not(:first-child){aspect-ratio:var(--wd-ar)}
.wd-works-section .wd-works-card:nth-child(n) .wd-works-media{position:absolute;inset:0;align-self:stretch;justify-self:stretch;height:auto;z-index:0;max-width:none;width:auto;aspect-ratio:auto;border:0;border-radius:inherit;background:#1d0f36}
.wd-works-section .wd-works-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;border-radius:inherit;background:linear-gradient(180deg,rgba(20,8,40,.62) 0%,rgba(20,8,40,0) 22%,rgba(20,8,40,0) 62%,rgba(20,8,40,.86) 100%)}
.wd-works-section .wd-works-dots{display:none}
.wd-works-section .wd-works-card h3{color:#fff;text-shadow:0 2px 18px rgba(10,4,24,.45)}
.wd-works-section .wd-works-card:nth-child(n) .wd-works-description{color:#ece8f5;max-width:34ch;text-shadow:0 1px 12px rgba(10,4,24,.5)}
.wd-works-card:hover .wd-works-media .vm,.wd-works-card:focus-visible .wd-works-media .vm{transform:scale(1.045)}
@media (max-width:1180px){.wd-works-section .wd-works-card:nth-child(n){padding:26px}.wd-works-section .wd-works-card h3{font-size:30px}.wd-works-section .wd-works-card:nth-child(n) .wd-works-description{font-size:15px}}
/* 2 colunas: mesma ideia — Bacio alto à esquerda, STW e CBPq empilhados à direita, Linea larga embaixo */
@media (max-width:991px){
 .wd-works-section .wd-works-grid{grid-template-rows:auto auto auto}
 .wd-works-section .wd-works-card:nth-child(1){grid-column:1;grid-row:1 / span 2}
 .wd-works-section .wd-works-card:nth-child(3){grid-column:2;grid-row:1}
 .wd-works-section .wd-works-card:nth-child(4){grid-column:2;grid-row:2}
 .wd-works-section .wd-works-card:nth-child(2){grid-column:1 / span 2;grid-row:3}
}
/* 1 coluna: cada card na proporção da própria arte */
@media (max-width:599px){
 .wd-works-section .wd-works-grid{grid-template-columns:minmax(0,1fr);grid-template-rows:none}
 .wd-works-section .wd-works-card:nth-child(n){grid-column:1;grid-row:auto;aspect-ratio:var(--wd-ar);padding:22px 20px}
 .wd-works-section .wd-works-card:nth-child(1){max-height:none}
 .wd-works-section .wd-works-card:nth-child(n):nth-child(2){aspect-ratio:auto;padding:0;gap:0;justify-content:flex-start}
 .wd-works-section .wd-works-card:nth-child(n):nth-child(2) .wd-works-media{flex-shrink:0;position:relative;inset:auto;order:-1;aspect-ratio:var(--wd-ar);border-radius:0}
 .wd-works-section .wd-works-card:nth-child(2) h3{position:absolute;top:18px;left:20px}
 .wd-works-section .wd-works-card:nth-child(2)::after{background:linear-gradient(180deg,rgba(20,8,40,.62) 0%,rgba(20,8,40,0) 30%)}
 .wd-works-section .wd-works-card:nth-child(2) .wd-works-description{padding:18px 20px 22px}
}
'''
