# Ajustes da página de cases (pedido: Works, sem anos/filtros, logos dos clientes, fontes e cores da Work)
import re, base64, os
def sub1(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)

def client_logos(out_img):
    h = open('/home/user/workdigital/home-final/index.html').read()
    s = h[h.index('<div class="wd-trust-marquee"'):]
    s = s[:s.index('</ul>')]
    logos = []
    for src, alt in re.findall(r'<img class="wd-trust-logo" src="data:image/png;base64,([^"]+)" alt="([^"]+)"', s):
        name = 'cliente-' + re.sub(r'[^a-z0-9]+', '-', alt.lower()).strip('-') + '.png'
        open(os.path.join(out_img, name), 'wb').write(base64.b64decode(src))
        logos.append((name, alt))
    assert len(logos) == 5, logos
    return logos

def fix(t, out_img):
    logos = client_logos(out_img)
    # ---- cores e fontes ----
    t = sub1(t, '  --muted: #8F8D96;\n', '  --muted: #CBB6FF;\n')
    t = sub1(t, '  --line: rgba(242, 240, 235, 0.14);\n', '  --line: rgba(203, 182, 255, 0.18);\n')
    t = sub1(t, '  --accent: #3D5AFE;\n', '  --accent: #6025E1;\n')
    t = sub1(t, '  --fg: #F2F0EB;\n', '  --fg: #F7F6FB;\n')
    t = sub1(t, '  --display: "Inter Tight", "Helvetica Neue", Arial, sans-serif;\n', '  --display: "Space Grotesk", Arial, sans-serif;\n  --text: "Nunito", system-ui, sans-serif;\n')
    t = sub1(t, '  --mono: "JetBrains Mono", ui-monospace, "SF Mono", Menlo, monospace;\n', '  --mono: "Space Grotesk", Arial, sans-serif;\n')
    t = t.replace('"Inter Tight", Arial, sans-serif', '"Space Grotesk", Arial, sans-serif')
    css = '''
/* ---- Works: fontes Space Grotesk (títulos) e Nunito (descritivos), paleta da Work, sem cinza ---- */
body{font-family:var(--text)}
.hero h1,.meta h2,.row .name,.num strong,.mono,.section-head{font-family:var(--display)}
.hero h1{font-weight:500;letter-spacing:-.04167em;line-height:.92}
.hero h1 .line>span{--wd-line-from:#6025e1;--wd-line-to:#cbb6ff;padding-bottom:.06em}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .hero h1 .line>span,.num strong{background:linear-gradient(90deg,var(--wd-line-from),var(--wd-line-to));background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
}
.hero h1 sup{color:#04CD8F;-webkit-text-fill-color:#04CD8F;font-family:var(--display)}
.hero-sub p{font-family:var(--text);color:#F7F6FB}
.meta h2{font-weight:500;color:#F7F6FB}
.desc{font-family:var(--text);color:#EFE7FF;margin-top:-4px}
.svc{color:#CBB6FF}
.svc span+span::before{color:#04CD8F}
.media{border-radius:16px}
.bar{border:0;justify-content:flex-end;padding-block:8px 0}
.grid[hidden],.list[hidden]{display:none!important}
.views{border-color:var(--line)}
.views .chip{font-family:var(--display);color:#EFE7FF;font-weight:500}
.views .chip:hover{color:#fff}
.views .chip[aria-pressed="true"]{background:#6025E1;color:#fff;border-color:#6025E1}
.row{border-color:var(--line)}
@media(min-width:901px){.row{grid-template-columns:1.4fr 1.6fr 40px}}
.row .name{font-weight:500;color:#F7F6FB}
.row:hover .arrow{color:#04CD8F}
.floater{border-radius:16px}
.media .tag::before{background:#04CD8F}
.cursor.big{background:linear-gradient(135deg,#6025E1,#C00252)}
.section-head{color:#CBB6FF;justify-content:center;text-align:center;letter-spacing:.2em}
.clients{border-top:0}
.marquee-track{gap:0;animation-duration:40s;align-items:center}
.marquee-logo{display:flex;align-items:center;justify-content:center;flex:0 0 220px;height:56px;padding-right:70px}
.marquee-logo img{display:block;max-width:150px;max-height:56px;width:auto;height:auto;object-fit:contain}
.num{border-top:1px solid var(--line)}
.num strong{--wd-line-from:#6025e1;--wd-line-to:#cbb6ff;font-weight:500;padding-bottom:.06em}
.num strong em{color:inherit;-webkit-text-fill-color:inherit}
.num span{color:#EFE7FF;font-family:var(--text);text-transform:none;letter-spacing:0;font-size:16px}
@media(prefers-reduced-motion:reduce){.hero h1 .line>span,.num strong{--wd-line-from:#efe7ff!important;--wd-line-to:#f5c3d8!important}}
'''
    t = sub1(t, '.hero{padding-top:clamp(150px,14vw,200px)!important}\n', '.hero{padding-top:clamp(150px,14vw,200px)!important}\n' + css)
    # ---- conteúdo ----
    t, n = re.subn(r'    <div class="hero-eyebrow mono">.*?</div>\n', '', t, count=1); assert n == 1
    t = sub1(t, '<span>Trabalhos<sup id="count">(12)</sup></span>', '<span>Works<sup id="count">(12)</sup></span>')
    # barra só com Grid / Lista (sem filtros e sem as linhas)
    t = sub1(t, '      <div class="filters" id="filters" role="group" aria-label="Filtrar por categoria"></div>\n', '')
    t = sub1(t, '<span id="cl-t">Marcas que confiam na gente</span><span>Exemplos</span>', '<span id="cl-t">Marcas que confiam na gente</span>')
    t = sub1(t, '<strong>8<em>a</em></strong><span class="mono">De estrada</span>', '<strong>6 anos</strong><span class="mono">De estrada</span>')
    # ---- anos ----
    t = sub1(t, '<div class="meta"><h2>${p.client}</h2><span class="yr mono">${p.year}</span></div>', '<div class="meta"><h2>${p.client}</h2></div>')
    t = sub1(t, 'a.setAttribute("aria-label", `${p.client}: ${p.title}, ${p.services.join(", ")}, ${p.year}`);', 'a.setAttribute("aria-label", `${p.client}: ${p.title}, ${p.services.join(", ")}`);')
    t = sub1(t, '<span class="yr mono">${p.year}</span><span class="arrow"', '<span class="arrow"')
    # ---- miniaturas com a paleta da Work (sem azul) ----
    pals = ['["#6025E1", "#121316", "#EFE7FF"]', '["#24123E", "#04CD8F", "#EFE7FF"]', '["#EFE7FF", "#6025E1", "#24123E"]',
            '["#121316", "#C00252", "#CBB6FF"]', '["#121316", "#6025E1", "#04CD8F"]', '["#C00252", "#121316", "#F7F6FB"]',
            '["#EFE7FF", "#24123E", "#ED4897"]', '["#34165B", "#F5C3D8", "#121316"]', '["#04CD8F", "#121316", "#24123E"]',
            '["#24123E", "#EFE7FF", "#ED4897"]', '["#F5C3D8", "#34165B", "#6025E1"]', '["#CBB6FF", "#24123E", "#04CD8F"]']
    old = re.findall(r'pal: (\[[^\]]+\])', t); assert len(old) == 12
    for o, nw in zip(old, pals):
        t = sub1(t, 'pal: ' + o, 'pal: ' + nw)
    # ---- sem filtros e sem alternância grade/lista ----
    t, n = re.subn(r'cats\.forEach\(\(c, i\) => \{.*?\n\}\);\n', '', t, count=1, flags=re.S); assert n == 1
    t = sub1(t, ', filters = document.getElementById("filters");', ';')
    t, n = re.subn(r'/\* ---------- Filters ---------- \*/.*?(?=/\* ---------- Grid / list)', '', t, count=1, flags=re.S); assert n == 1
    # ---- carrossel com os logos dos clientes (os mesmos da home) ----
    group = ''.join(f'<span class="marquee-logo"><img src="./img/{f}" alt="{a}" loading="lazy" decoding="async"></span>' for f, a in logos)
    t = sub1(t, 'document.getElementById("marquee").innerHTML = [...projects, ...projects].map(p => `<span>${p.client}</span>`).join("");',
             'document.getElementById("marquee").innerHTML = ' + repr(group * 2) + ' + ' + repr(group.replace('" alt="', '" aria-hidden="true" alt="') * 2) + ';')
    # ---- efeito das frases grandes da home: a cor do gradiente vai do roxo ao lilás claro ----
    js = '''
/* ---------- Gradiente das frases grandes (mesmo efeito da home) ---------- */
(function(){
  const mix=(a,b,p)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*p)).join(',')})`;
  const clamp=v=>Math.max(0,Math.min(1,v));
  const paint=(el,p)=>{el.style.setProperty('--wd-line-from',mix([96,37,225],[239,231,255],p));el.style.setProperty('--wd-line-to',mix([203,182,255],[245,195,216],p));};
  const title=document.querySelector('.hero h1 .line>span'), nums=[...document.querySelectorAll('.num strong')];
  if(reduce){paint(title,1);nums.forEach(n=>paint(n,1));return;}
  let queued=false;
  // "Works": mesmo efeito dos números — a cor vai do roxo ao lilás claro conforme a página rola
  function update(){queued=false;paint(title,clamp(scrollY/Math.max(1,innerHeight*.45)));nums.forEach((n,i)=>{const r=n.getBoundingClientRect();paint(n,clamp((innerHeight*.85-r.top)/Math.max(1,innerHeight*.35)*1.3-i*.3));});}
  addEventListener('scroll',()=>{if(!queued){queued=true;requestAnimationFrame(update);}},{passive:true});
  update();
})();
'''
    t = sub1(t, '/* Redraw once fonts arrive', js + '\n/* Redraw once fonts arrive')
    return t
