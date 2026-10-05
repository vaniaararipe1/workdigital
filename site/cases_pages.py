# Páginas internas dos 16 cases: uma página (case-interna) que mostra o case do endereço (#slug).
# Textos: ci/conteudo-cases.json. Artes: ci/cases/{slug}/ (copiadas sem alteração para cases/{slug}/).
import html as H, json, os, re, shutil
DIR = os.path.dirname(os.path.abspath(__file__))
CI = os.path.join(DIR, 'ci')
DATA = sorted(json.load(open(os.path.join(CI, 'conteudo-cases.json')))['cases'], key=lambda c: c['ordem'])
PROJETO = {'bacio-di-latte': 'Site institucional', 'linea-alimentos': 'Site e loja virtual', 'cbpq': 'Portal institucional',
           'stw-brasil': 'Site institucional', 'agencia-jaya': 'Site institucional', 'genera': 'Experiência interativa',
           'instituto-ricco-porto': 'Site institucional', 'instituto-long-tao': 'Site e EAD', 'ideale-treinamentos': 'Site institucional',
           'droneng': 'Site institucional', 'loren-andrade': 'Site institucional', 'ogg': 'Blog', 'oliva-pizzaria': 'Site institucional',
           'marka-contabilidade': 'Site institucional', 'berti-promocional': 'Site institucional', 'instituto-nossa-senhora-da-vitoria': 'Site institucional'}
# bloco: (arquivo, classes do .m, largura, altura, legenda?, eager?)
BLOCOS = [('01-home', 'h74 w169', 2400, 1350, True, True), ('02-key-visual', 'full w34', 1500, 2000, False, True),
          ('03-detalhe', 'h74 w11', 1600, 1600, True, False), ('04-pagina', 'h74 w169', 2400, 1350, True, False),
          ('05-mobile', 'full w45', 1600, 2000, False, False), ('06-conceito', 'full w34', 1500, 2000, False, False),
          ('07-paleta', 'h74 w34', 1500, 2000, False, False)]
ARROW = '<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.0641 1.14239L.499 12.7061M1.9673.7061h9.5726c.53 0 .9591.4291.9591.9605v9.5712" stroke="currentColor" stroke-width="1.41181"/></svg>'
e = lambda s: H.escape(s or '', quote=True)

def has(slug, f):
    return os.path.exists(os.path.join(CI, 'cases', slug, f))

def media(c):
    s, out = c['slug'], []
    for f, cls, w, h, cap, eager in BLOCOS:
        alt = c['alt'].get(f, '')
        if f == '05-mobile':
            if not (has(s, f + '.webm') or has(s, f + '.mp4')):
                continue
            poster = f' poster="./cases/{s}/{f}.webp"' if has(s, f + '.webp') else ''
            srcs = ''.join(f'<source data-src="./cases/{s}/{f}.{x}" type="video/{x}">' for x in ('webm', 'mp4') if has(s, f'{f}.{x}'))
            inner = (f'<video class="case-video" muted loop playsinline preload="none"{poster} width="{w}" height="{h}" '
                     f'aria-label="{e(alt)}">{srcs}</video>')
        else:
            if not has(s, f + '.webp'):
                continue
            inner = (f'<img src="./cases/{s}/{f}.webp" alt="{e(alt)}" width="{w}" height="{h}" decoding="async" '
                     f'loading="{"eager" if eager else "lazy"}">')
        if cap and c['legendas'].get(f):
            inner += f'<span class="cap">{e(c["legendas"][f])}</span>'
        out.append(f'<div class="m {cls}">{inner}</div>')
    return '\n        '.join(out)

def intro(c):
    btn = ''
    if c.get('link_status') == 'mostrar' and c.get('link'):
        btn = f'<a class="wd-work-cta wd-cta cta" href="{e(c["link"])}" target="_blank" rel="noopener"><span>VER PROJETO NO AR</span>{ARROW}</a>'
    serv = ''.join(f'<li>{e(x)}</li>' for x in c['servicos'])
    return (f'<div class="intro">\n          <h1 data-cliente="{e(c["titulo"])}" data-projeto="{e(PROJETO[c["slug"]])}" data-seo="{e(c["seo_title"])}">{e(c["titulo"])}</h1>\n'
            f'          <div>\n            <p>{e(c["p1"])}</p>\n            <p>{e(c["p2"])}</p>\n            {btn}\n          </div>\n'
            f'          <div>\n            <h2>Serviços</h2>\n            <ul>{serv}</ul>\n          </div>\n        </div>')

def nxt(c):
    i = [x['slug'] for x in DATA].index(c['slug'])
    return DATA[(i + 1) % len(DATA)]

def fragment(c):
    n = nxt(c)
    return (intro(c) + '\n        ' + media(c) + '\n        '
            f'<a class="next" href="#{n["slug"]}" id="next" data-slug="{n["slug"]}" aria-label="Próximo case: {e(n["titulo"])}">\n'
            f'          <div class="big">Próximo case</div>\n'
            f'          <div class="bottom"><span>{e(n["titulo"])}</span><i></i><b>→</b></div>\n        </a>')

CSS = '''<style>
/* Mídias reais dos cases: preenchem o bloco (o arredondamento e a legenda são do site) */
.m>img,.m>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.m>video{background:#120B20}
.m .cap{z-index:2}
</style>
'''

JS = r'''<script>
/* Cases: o endereço #slug escolhe o case; vídeo do bloco 5 carrega perto da tela e toca com 50% visível */
window.WD_CASES=__DATA__;
(function(){
  const C=window.WD_CASES, track=document.getElementById('track');
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches||document.documentElement.classList.contains('wd-lite');
  let ioLoad=null, ioPlay=null;
  function setMeta(sel,attr,val){let m=document.head.querySelector(sel);if(!m){m=document.createElement('meta');m.setAttribute(attr,sel.match(/"(.*)"/)[1]);document.head.append(m);}m.setAttribute('content',val);}
  function videos(){
    ioLoad&&ioLoad.disconnect(); ioPlay&&ioPlay.disconnect();
    const vs=[...track.querySelectorAll('video.case-video')]; if(still||!vs.length) return;
    const load=v=>{if(v.dataset.ld)return;v.dataset.ld=1;v.querySelectorAll('source[data-src]').forEach(s=>s.src=s.dataset.src);v.load();};
    ioLoad=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){load(en.target);ioLoad.unobserve(en.target);}}),{rootMargin:'300px'});
    ioPlay=new IntersectionObserver(es=>es.forEach(en=>{const v=en.target;if(en.intersectionRatio>=.5){load(v);const p=v.play();p&&p.catch(()=>{});}else v.pause();}),{threshold:[0,.5,1]});
    vs.forEach(v=>{ioLoad.observe(v);ioPlay.observe(v);});
  }
  function show(slug,first){
    const c=C.list.find(x=>x.slug===slug)||C.list[0];
    if(!first||c.slug!==C.list[0].slug||location.hash){ track.innerHTML=c.html; }
    document.title=c.seo_title;
    setMeta('meta[name="description"]','name',c.seo_description);
    setMeta('meta[property="og:title"]','property',c.seo_title);
    setMeta('meta[property="og:description"]','property',c.seo_description);
    setMeta('meta[property="og:image"]','property',c.og_image);
    setMeta('meta[property="og:url"]','property',c.url);
    setMeta('meta[name="twitter:title"]','name',c.seo_title);
    setMeta('meta[name="twitter:description"]','name',c.seo_description);
    setMeta('meta[name="twitter:image"]','name',c.og_image);
    const can=document.head.querySelector('link[rel="canonical"]'); can&&can.setAttribute('href',c.url);
    const ld=document.getElementById('wd-case-ld'); ld&&(ld.textContent=JSON.stringify(c.ld));
    videos();window.wdLbRefresh&&wdLbRefresh();
    if(!first){scrollTo(0,0);dispatchEvent(new Event('resize'));}
  }
  // teclado (desktop): o item focado entra na tela, rolando a página até ele
  track.addEventListener('focusin',e=>{
    if(matchMedia('(max-width:900px)').matches)return;
    const hs=document.getElementById('hs'), st=hs&&hs.querySelector('.stick'); if(!hs)return;
    if(st)st.scrollLeft=0;
    const r=e.target.getBoundingClientRect(), x=r.left-track.getBoundingClientRect().left;
    const dist=Math.max(0,track.scrollWidth-innerWidth), want=Math.min(dist,Math.max(0,x+r.width/2-innerWidth/2));
    scrollTo({top:hs.getBoundingClientRect().top+scrollY+want,behavior:'auto'});
  });
  window.wdGoCase=s=>{if(location.hash.slice(1)===s){show(s,false);}else location.hash=s;};
  show(location.hash.slice(1),true);
  addEventListener('hashchange',()=>show(location.hash.slice(1),false));
})();
</script>
'''

SITE = 'https://workdigital.art.br'
og = lambda c: SITE + f'/cases/{c["slug"]}/01-home.webp'
def case_ld(c):
    url = SITE + f'/cases/{c["slug"]}/'
    return {'@context': 'https://schema.org', '@graph': [
        {'@type': 'CreativeWork', '@id': url + '#case', 'name': c['seo_title'], 'headline': c['seo_title'],
         'description': c['seo_description'], 'url': url, 'image': og(c), 'inLanguage': 'pt-BR',
         'about': c['titulo'], 'creator': {'@type': 'Organization', 'name': 'Work Digital', 'url': SITE + '/'}},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': 'Cases', 'item': SITE + '/cases/'},
            {'@type': 'ListItem', 'position': 3, 'name': c['titulo'], 'item': url}]}]}

def apply(t, out):
    # artes: cópia exata (sem recompressão)
    for c in DATA:
        src = os.path.join(CI, 'cases', c['slug']); dst = os.path.join(out, 'cases', c['slug'])
        os.makedirs(dst, exist_ok=True)
        for f in os.listdir(src):
            if '(1)' not in f: shutil.copy(os.path.join(src, f), os.path.join(dst, f))
    first = DATA[0]
    # conteúdo do track: intro + mídias + próximo case (o case 1 já vem no HTML; os outros entram pelo #slug)
    t, n = re.subn(r'(<div class="track" id="track">).*?(</a>)(\s*</div>\s*</div>\s*</section>)',
                   lambda m: m.group(1) + '\n        ' + fragment(first) + m.group(3), t, count=1, flags=re.S)
    assert n == 1
    import a11y_seo as AS
    head = AS.meta_block(first['seo_title'], first['seo_description'], f'/cases/{first["slug"]}/', 'article', og(first)) + \
        AS.ld(case_ld(first)).replace('<script ', '<script id="wd-case-ld" ', 1) + '\n'
    head = head.replace(AS.SITE, AS.TOKEN)
    t = re.sub(r'(<title>[^<]*</title>)', lambda m: '<title>' + e(first['seo_title']) + '</title>\n' + head, t, count=1)
    data = {'list': [{'slug': c['slug'], 'seo_title': c['seo_title'], 'seo_description': c['seo_description'],
                      'og_image': og(c), 'url': SITE + f'/cases/{c["slug"]}/', 'ld': case_ld(c), 'html': fragment(c)} for c in DATA]}
    js = JS.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/').replace(SITE, '__WD_SITE__'))
    t = t.replace('</style>', CSS.replace('<style>', '').replace('</style>\n', '') + '</style>', 1)
    t = t.replace('</main>', '</main>\n' + js, 1)
    # "Próximo case": ao fim do loader, abre o próximo case
    a = "setTimeout(()=>{ loader.classList.remove('on'); bar.style.width='0'; num.textContent='000'; scrollTo({top:0}); },500);"
    assert t.count(a) == 1
    t = t.replace(a, "setTimeout(()=>{ const nx=document.getElementById('next'); window.wdGoCase&&nx&&wdGoCase(nx.dataset.slug); loader.classList.remove('on'); bar.style.width='0'; num.textContent='000'; scrollTo({top:0}); },500);")
    # o painel "Próximo case" é recriado a cada troca: o clique é ouvido no documento
    b = "document.getElementById('next').addEventListener('click',e=>{"
    assert t.count(b) == 1
    t = t.replace(b, "document.addEventListener('click',e=>{ if(!e.target.closest('#next')) return;")
    return t

def lightbox(t):
    # tela cheia: lista de blocos lida na hora (muda com o case) e o clone do bloco 5 toca o vídeo
    a = "const items=[...document.querySelectorAll('.track .m')];\n  if(!items.length)return;"
    assert t.count(a) == 1, 'lightbox items'
    t = t.replace(a, "let items=[];const refresh=()=>{items=[...document.querySelectorAll('.track .m')];};refresh();")
    b = "el.classList.add('case-lb-item');"
    assert t.count(b) == 1
    t = t.replace(b, "el.classList.add('case-lb-item');const cv=el.querySelector('video');if(cv){const ov=src.querySelector('video');cv.querySelectorAll('source').forEach(s=>{if(s.dataset.src)s.src=s.dataset.src;});cv.muted=true;cv.loop=true;cv.playsInline=true;if(!(matchMedia('(prefers-reduced-motion: reduce)').matches||document.documentElement.classList.contains('wd-lite'))){cv.preload='auto';cv.load();try{cv.currentTime=ov?ov.currentTime:0;}catch(x){}const p=cv.play();p&&p.catch(()=>{});}}")
    c = """  items.forEach((m,i)=>{
    m.setAttribute('role','button');m.tabIndex=0;m.setAttribute('aria-label','Ver imagem '+(i+1)+' em tela cheia');
    m.addEventListener('click',()=>open(i));
    m.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();open(i);}});
  });"""
    assert t.count(c) == 1, 'lightbox bind'
    t = t.replace(c, """  const prep=()=>{refresh();items.forEach((m,i)=>{m.setAttribute('role','button');m.tabIndex=0;m.setAttribute('aria-label','Ver imagem '+(i+1)+' em tela cheia');});};
  prep();window.wdLbRefresh=prep;
  document.addEventListener('click',e=>{const m=e.target.closest&&e.target.closest('.track .m');if(!m)return;refresh();open(items.indexOf(m));});
  document.addEventListener('keydown',e=>{const m=e.target.closest&&e.target.closest('.track .m');if(!m||lb.classList.contains('open'))return;if(e.key==='Enter'||e.key===' '){e.preventDefault();refresh();open(items.indexOf(m));}});""")
    return t
