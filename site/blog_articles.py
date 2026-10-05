# 20 artigos do Blog da Work: listagem (blog.html) e página do artigo (post.html#slug)
import html as H, json, os, re, shutil
DIR = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(DIR, 'blog-artigos')
IMGS = os.path.join(DIR, 'blogimg')
POST_URL = 'https://claude.ai/artifact/FtXL4pXoAfAXYYKwcxV1w8'
MES = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

# slug, categoria, data (retroativa), imagem: chave existente do blog (p1..p8) ou None (foto nova em img/blog/{slug}.jpg)
META = [
    ('site-lento-custa-caro', 'Performance', '2026-09-28', None),
    ('landing-page-ou-site-institucional', 'Criação de sites', '2026-09-21', None),
    ('erros-checkout-loja-virtual', 'Lojas virtuais', '2026-09-14', None),
    ('seo-2026-o-que-funciona', 'SEO', '2026-09-05', None),
    ('plataforma-loja-virtual', 'Lojas virtuais', '2026-08-29', None),
    ('design-que-converte', 'Criação de sites', '2026-08-20', None),
    ('trafego-pago-sem-bom-site', 'Tráfego', '2026-08-12', None),
    ('metricas-do-site', 'Performance', '2026-08-04', None),
    ('whatsapp-no-site', 'Tráfego', '2026-07-22', None),
    ('quanto-custa-um-site-profissional', 'Criação de sites', '2026-05-06', None),
    ('perfil-da-empresa-no-google', 'SEO', '2026-02-17', None),
    ('site-responsivo-celular', 'Performance', '2025-11-25', None),
    ('fotos-de-produto-loja-virtual', 'Lojas virtuais', '2025-09-02', None),
    ('site-por-assinatura-ou-personalizado', 'Criação de sites', '2025-06-10', None),
    ('palavras-chave-o-que-seu-cliente-pesquisa', 'SEO', '2025-03-18', None),
    ('instagram-e-site-juntos', 'Tráfego', '2024-12-03', None),
    ('frete-prazo-confianca-compra-online', 'Lojas virtuais', '2024-09-10', None),
    ('hospedagem-e-manutencao-de-site', 'Performance', '2024-06-04', None),
    ('checklist-site-antes-de-ir-ao-ar', 'Criação de sites', '2024-03-12', None),
    ('lgpd-no-site', 'Negócios', '2023-11-21', None),
]

def fmt(iso):
    y, m, d = iso.split('-'); return f'{int(d)} {MES[int(m) - 1]} {y}'

def words(h):
    return len(re.sub(r'<[^>]+>', ' ', h).split())

def load(blog_img):
    fotos = json.load(open(os.path.join(IMGS, 'fotos.json'))) if os.path.exists(os.path.join(IMGS, 'fotos.json')) else {}
    out = []
    for slug, cat, iso, key in META:
        a = json.load(open(os.path.join(ART, slug + '.json')))
        img = blog_img[key] if key else f'./img/blog/{slug}.jpg'
        alt = (fotos.get(slug) or {}).get('alt', '') if not key else ''
        out.append({'slug': slug, 'cat': cat, 'iso': iso, 'date': fmt(iso), 'img': img, 'alt': alt,
                    'title': a['title'], 'dek': a['dek'], 'excerpt': a['excerpt'], 'lead': a['lead'], 'body': a['body'],
                    'min': max(3, round((words(a['body']) + words(a['lead'])) / 200))})
    return out

def copy_images(out):
    os.makedirs(out + '/img/blog', exist_ok=True)
    for slug, _, _, key in META:
        f = os.path.join(IMGS, slug + '.jpg')
        if not key and os.path.exists(f):
            shutil.copy(f, f'{out}/img/blog/{slug}.jpg')

def js_str(o):
    return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')

# ---------------- Listagem ----------------
PAG_JS = r'''
// Filtro por categoria + busca + paginação (8 artigos por página)
let cat="Todos", term="", page=1; const PER=8;
const pag=document.getElementById('pag');
const arr=d=>`<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6"><path d="${d}"/></svg>`;
function apply(){
  const match=el=>(cat==="Todos"||el.dataset.cat===cat)&&(!term||el.dataset.t.includes(term));
  feat.hidden=!(page===1&&match(feat));
  const rows=[...list.querySelectorAll('.row')], ok=rows.filter(match), pages=Math.max(1,Math.ceil(ok.length/PER));
  if(page>pages) page=pages;
  rows.forEach(r=>r.hidden=true);
  ok.slice((page-1)*PER,page*PER).forEach(r=>{r.hidden=false;r.classList.add('in');});
  document.getElementById('empty').hidden=ok.length>0||match(feat);
  if(pages<2){pag.hidden=true;return;}
  pag.hidden=false;
  let h=`<a href="#" data-p="${page-1}" class="${page===1?'off':''}" aria-label="Página anterior">${arr('M10 3 5 8l5 5')}</a>`;
  for(let i=1;i<=pages;i++) h+=`<a href="#" data-p="${i}"${i===page?' aria-current="page"':''}>${i}</a>`;
  h+=`<a href="#" data-p="${page+1}" class="${page===pages?'off':''}" aria-label="Próxima página">${arr('m6 3 5 5-5 5')}</a>`;
  pag.innerHTML=h;
}
pag.addEventListener('click',e=>{const a=e.target.closest('a[data-p]');if(!a)return;e.preventDefault();page=+a.dataset.p;apply();document.querySelector('.hero .rule').scrollIntoView({behavior:'smooth',block:'start'});});
document.getElementById('cats').addEventListener('click',e=>{
  const b=e.target.closest('button'); if(!b) return;
  document.querySelectorAll('#cats button').forEach(x=>x.setAttribute('aria-pressed',x===b)); cat=b.textContent; page=1; apply();
});
const q=document.getElementById('q');
q.addEventListener('input',()=>{term=q.value.trim().toLowerCase(); page=1; apply();});
apply();

'''

def blog(t):
    m = re.search(r'const IMG = (\{.*?\});', t)
    blog_img = json.loads(m.group(1))
    arts = load(blog_img)
    img = dict(blog_img)
    posts = []
    for a in arts:
        k = a['slug'] if a['img'].startswith('./img/blog/') else next(x for x, v in blog_img.items() if v == a['img'])
        img[k] = a['img']
        posts.append({'cat': a['cat'], 'date': a['date'], 'min': a['min'], 'img': k, 'title': a['title'], 'slug': a['slug']})
    # destaque = artigo mais recente; o destaque antigo (blog marketing, 2022) entra na lista e abre a página padrão do post
    arts_sorted = sorted(arts, key=lambda a: a['iso'], reverse=True)
    top = arts_sorted[0]
    posts = [x for x in posts if x['slug'] != top['slug']]
    featured = {'cat': top['cat'], 'date': top['date'], 'min': top['min'], 'img': next(x for x in img if img[x] == top['img']),
                'title': top['title'], 'excerpt': top['excerpt'], 'slug': top['slug']}
    t, n = re.subn(r'const FEATURED = \{.*?\n\};', lambda _: 'const FEATURED = ' + js_str(featured) + ';', t, count=1, flags=re.S); assert n == 1
    posts.append({'real': True, 'cat': 'Negócios', 'date': '7 jun 2022', 'min': 4, 'img': 'feat',
                  'title': 'Como potencializar a sua marca com o blog marketing'})
    posts.append({'real': True, 'cat': 'Negócios', 'date': '16 mai 2022', 'min': 6, 'img': 'p9',
                  'title': '6 motivos que mostram a importância de ter um site para o seu negócio',
                  'href': 'https://workdigital.art.br/6-motivos-que-mostram-a-importancia-de-ter-um-site-para-o-seu-negocio/'})
    t = t.replace(m.group(0), 'const IMG = ' + js_str(img) + ';', 1)
    t, n = re.subn(r'const POSTS = \[.*?\n\];', lambda _: 'const POSTS = ' + js_str(posts) + ';', t, count=1, flags=re.S); assert n == 1
    t, n = re.subn(r'const link=p=>[^\n]*', lambda _: 'const link=p=>p.slug?`href="' + POST_URL + '#${p.slug}" target="_top"`:p.href?`href="${p.href}" target="_blank" rel="noopener"`:`href="' + POST_URL + '" target="_top"`;', t, count=1); assert n == 1
    t, n = re.subn(r'<nav class="pag".*?</nav>', '<nav class="pag" id="pag" aria-label="Paginação"></nav>', t, count=1, flags=re.S); assert n == 1
    t, n = re.subn(r'// Filtro por categoria \+ busca\n.*?(?=// Reveal)', lambda _: PAG_JS, t, count=1, flags=re.S); assert n == 1
    return t

# ---------------- Artigo ----------------
RENDER_JS = r'''<script>
/* Artigos do blog: o endereço post#slug mostra o artigo correspondente */
window.WD_POSTS=__DATA__;
(function(){
  const D=window.WD_POSTS, BASE="__URL__";
  const $=s=>document.querySelector(s), esc=s=>s.replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
  const body=document.getElementById('body'), rel=$('.rel .cards');
  const card=p=>`<a class="card rv in" href="#${p.slug}"><div class="im"><img src="${p.img}" alt="" loading="lazy"></div><p class="d">Publicado em ${p.date}</p><h3>${esc(p.title)}</h3><div class="by"><span class="au"><span class="av" aria-hidden="true">W</span>Equipe Work Digital</span><span class="rt">${p.min} min</span></div></a>`;
  function related(slug,cat){
    const all=D.list.filter(p=>p.slug!==slug), same=all.filter(p=>p.cat===cat), rest=all.filter(p=>p.cat!==cat);
    rel.innerHTML=[...same,...rest].slice(0,3).map(card).join('');
  }
  function render(first){
    const s=location.hash.slice(1), p=D.list.find(x=>x.slug===s);
    if(!p){related('','Negócios');return;}
    const chip=$('.ph .top .chip'); chip.textContent=p.cat;
    $('.ph .top span').textContent='Publicado em '+p.date;
    $('.ph h1').textContent=p.title; $('.ph .dek').textContent=p.dek; $('.ph .by .rt').textContent=p.min+' min';
    const hero=$('.hero-img img'); hero.src=p.img; hero.alt=p.alt||'';
    const end=body.querySelector('.share-end');
    while(body.firstChild&&body.firstChild!==end) body.firstChild.remove();
    end.insertAdjacentHTML('beforebegin','<p class="lead">'+esc(p.lead)+'</p>'+p.body);
    document.querySelectorAll('.share').forEach(b=>b.dataset.url=encodeURIComponent(BASE+'#'+p.slug));
    document.title=p.title+' - Work Digital';
    related(p.slug,p.cat);
    document.querySelectorAll('.ph .rv,.hero-img.rv').forEach(el=>el.classList.add('in'));
    if(!first){window.wdShare&&window.wdShare();scrollTo(0,0);}
  }
  render(true);
  addEventListener('hashchange',()=>render(false));
})();
</script>
'''

def post(t, out):
    src = open(os.path.join(DIR, 'blog-work-digital.html')).read()
    blog_img = json.loads(re.search(r'const IMG = (\{.*?\});', src).group(1))
    # o blog original guarda as fotos em base64; as extraídas ficam em img/foto-*.jpg com o mesmo nome no blog publicado
    built = open(os.path.join(out, 'blog.html')).read()
    blog_img = json.loads(re.search(r'const IMG = (\{.*?\});', built).group(1))
    arts = load(blog_img)
    copy_images(out)
    data = {'list': [{k: a[k] for k in ('slug', 'cat', 'date', 'min', 'img', 'alt', 'title', 'dek', 'lead', 'body')} for a in arts]}
    js = RENDER_JS.replace('__DATA__', js_str(data)).replace('__URL__', POST_URL)
    t = t.replace('</main>', '</main>\n' + js, 1)
    # compartilhar: refeito a cada troca de artigo, lendo o endereço na hora do clique
    t = t.replace("(function(){\n  const title=document.querySelector('.ph h1')?.textContent.trim()||document.title;",
                  "window.wdShare=function(){\n  const title=document.querySelector('.ph h1')?.textContent.trim()||document.title;", 1)
    t = t.replace("    copy.addEventListener('click',async()=>{const url=decodeURIComponent(u);",
                  "    if(copy.dataset.on)return;copy.dataset.on=1;\n    copy.addEventListener('click',async()=>{const url=decodeURIComponent(box.dataset.url);", 1)
    t = t.replace("      tip.textContent=ok?'Link copiado':'Não foi possível copiar';tip.classList.add('on');setTimeout(()=>tip.classList.remove('on'),1800);});\n  });\n})();",
                  "      tip.textContent=ok?'Link copiado':'Não foi possível copiar';tip.classList.add('on');setTimeout(()=>tip.classList.remove('on'),1800);});\n  });\n};\nwdShare();", 1)
    assert 'window.wdShare=function' in t and 'wdShare();' in t
    return t

# ---------------- Home: sempre os 3 artigos mais recentes ----------------
MES_LONGO = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
ARROW = '<svg viewBox="0 0 14 14" fill="none"><path d="M12.065 1.142L.5 12.706M1.968 .706h9.573c.53 0 .959.429.959.961v9.571" stroke="currentColor" stroke-width="1.412"/></svg>'
HOME_CSS = '''<style>
/* Blog da home: 3 artigos mais recentes */
@media (max-width:991px) and (min-width:700px){.wd-blog-section .wd-blog-list{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.wd-blog-section .wd-blog-link{padding:18px 18px 32px;gap:24px 12px}}
</style>
'''
def home(t, out):
    built = open(os.path.join(out, 'blog.html')).read()
    blog_img = json.loads(re.search(r'const IMG = (\{.*?\});', built).group(1))
    arts = sorted(load(blog_img), key=lambda a: a['iso'], reverse=True)[:3]
    items = []
    for a in arts:
        y, m, d = a['iso'].split('-')
        longa = f'{int(d)} de {MES_LONGO[int(m) - 1]} de {y}'
        src = a['img']
        if src.startswith('data:'):  # foto ainda embutida no blog: grava como arquivo para a home
            import base64, hashlib
            raw = base64.b64decode(src.split(',', 1)[1]); fn = 'img/foto-' + hashlib.md5(raw).hexdigest()[:10] + '.jpg'
            open(os.path.join(out, fn), 'wb').write(raw); src = './' + fn
        items.append(f'''      <article class="wd-blog-item">
        <a class="wd-blog-link" href="{POST_URL}#{a['slug']}" target="_top">
          <img class="wd-blog-image" loading="lazy" decoding="async" width="900" height="500" src="{src}" alt="{H.escape(a['alt'] or a['title'])}">
          <div class="wd-blog-content">
            <h3 class="wd-blog-article-title">{H.escape(a['title'])}</h3>
            <p class="wd-blog-excerpt">{H.escape(a['excerpt'])}</p>
            <div class="wd-blog-meta">
              <time datetime="{a['iso']}">{longa}</time>
              <span class="wd-blog-category">{H.escape(a['cat'])}</span>
            </div>
          </div>
          <span class="wd-blog-arrow" aria-hidden="true">
            {ARROW}
          </span>
        </a>
      </article>''')
    t, n = re.subn(r'(<div class="wd-blog-list">).*?(\n    </div>\n\n    <div class="wd-blog-footer">)',
                   lambda m: m.group(1) + '\n' + '\n'.join(items) + m.group(2), t, count=1, flags=re.S)
    assert n == 1
    return t.replace('</head>', HOME_CSS + '</head>', 1)
