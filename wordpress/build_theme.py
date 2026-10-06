# Gera o tema WordPress (wordpress/theme/workdigital) a partir das páginas prontas em site/.
# As páginas viram modelos PHP: o visual, o CSS e os scripts continuam os mesmos; as partes que mudam
# (cases, artigos, links, títulos e SEO) passam a vir do WordPress.
import base64, hashlib, json, os, re, shutil, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
SRC = os.path.join(ROOT, 'wordpress', 'theme-src')
OUT = os.path.join(ROOT, 'wordpress', 'theme', 'workdigital')
sys.path.insert(0, SITE)

A = 'https://claude.ai/artifact/'
PAGES = {'home': 'K3DaWGpPSDzZs2TZpjwHjw', 'solucoes': 'Y2eQb4LZVTwWfbNdqz7nbi', 'cases': 'JRyLZxgMsFFUnvkSMXaiZ1',
         'case': '3Fh9si9SLB3sa15y3GoaKC', 'blog': '2p828J4i2F3ekJZAnydNYc', 'post': 'FtXL4pXoAfAXYYKwcxV1w8'}
POST_URLS = json.load(open(os.path.join(SITE, 'post-urls.json')))
OLD_POST = 'como-potencializar-a-sua-marca-com-o-blog-marketing'

def php_url(path):
    return "<?php echo esc_url(wd_url('" + path + "')); ?>"

def links(t):
    t = re.sub(re.escape(A + PAGES['case']) + r'#([a-z0-9-]+)', lambda m: php_url('cases/' + m.group(1) + '/'), t)
    for slug, url in POST_URLS.items():
        t = t.replace(url, php_url('blog/' + slug + '/'))
    t = re.sub(re.escape(A + PAGES['post']) + r'#([a-z0-9-]+)', lambda m: php_url('blog/' + m.group(1) + '/'), t)
    t = t.replace(A + PAGES['post'], php_url('blog/' + OLD_POST + '/'))
    for k, path in (('home', ''), ('solucoes', 'solucoes/'), ('cases', 'cases/'), ('case', 'cases/'), ('blog', 'blog/')):
        t = t.replace(A + PAGES[k], php_url(path))
    t = t.replace('https://workdigital.art.br/6-motivos-que-mostram-a-importancia-de-ter-um-site-para-o-seu-negocio/',
                  php_url('blog/6-motivos-que-mostram-a-importancia-de-ter-um-site-para-o-seu-negocio/'))
    t = t.replace(' target="_top"', '')
    return t

def inline_data(t, out_assets):
    os.makedirs(os.path.join(out_assets, 'img', 'inline'), exist_ok=True)
    def rep(m):
        mime, data = m.group(1), m.group(2)
        ext = {'image/png': 'png', 'image/jpeg': 'jpg', 'image/webp': 'webp', 'image/svg+xml': 'svg', 'image/gif': 'gif',
               'font/woff2': 'woff2', 'font/woff': 'woff', 'application/font-woff2': 'woff2'}.get(mime)
        if not ext: return m.group(0)
        raw = base64.b64decode(data)
        name = hashlib.md5(raw).hexdigest()[:12] + '.' + ext
        open(os.path.join(out_assets, 'img', 'inline', name), 'wb').write(raw)
        return '<?php echo WD_URI; ?>/img/inline/' + name
    return re.sub(r'data:([a-z0-9/+.-]+);base64,([A-Za-z0-9+/=]+)', rep, t)

STRIP = [r'<title>[^<]*</title>\s*', r'<meta (?:name|property)="(?:description|robots|og:[^"]*|twitter:[^"]*)"[^>]*>\s*',
         r'<link rel="canonical"[^>]*>\s*', r'<script[^>]*type="application/ld\+json"[^>]*>.*?</script>\s*',
         r'<script>document\.documentElement\.lang="pt-BR"</script>\s*',
         r'<!-- Google Tag Manager \(noscript\) -->.*?<!-- End Google Tag Manager \(noscript\) -->\s*',
         r'<!-- Google Tag Manager -->.*?<!-- End Google Tag Manager -->\s*',
         r'<meta charset[^>]*>\s*', r'<meta name="viewport"[^>]*>\s*', r'<meta http-equiv="Content-Type"[^>]*>\s*']

def split(t):
    if '<head>' in t:
        head = t[t.index('<head>') + 6:t.index('</head>')]
        b = re.search(r'<body[^>]*>', t)
        body = t[b.end():t.rindex('</body>')]
    else:
        i = t.index('<!-- Google Tag Manager (noscript) -->')
        head, body = t[:i], t[i:]
    return head, body

# sem o botão "Pausar animações" (pedido da Work); quem prefere menos movimento continua atendido pelo ajuste do sistema
NO_PAUSE = [r'<button class="wd-pause"[^>]*>.*?</button>\s*', r'<script>\s*/\* Pausar animações.*?</script>\s*']

def clean(t):
    for p in STRIP + NO_PAUSE: t = re.sub(p, '', t, flags=re.S)
    return t

def paths(t):
    t = re.sub(r'`\./thumbs/\$\{slug\}\.([a-z.]+)`', r'`${wdT(slug,"\1")}`', t)
    t = re.sub(r'\./thumbs/\$\{slug\}\.([a-z.]+)', r'${wdT(slug,"\1")}', t)
    t = re.sub(r'(?<=["\'(`,\s])\./(?=[A-Za-z0-9_-])', '<?php echo WD_URI; ?>/', t)
    return t

DOC_OPEN = '''<?php if (!defined('ABSPATH')) exit; ?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
'''
DOC_HEAD_END = '\n<?php wp_head(); ?>\n</head>\n<body <?php body_class(); ?>>\n<?php wp_body_open(); ?>\n'
DOC_CLOSE = '\n<?php wp_footer(); ?>\n</body>\n</html>\n'

def page(name, out_assets, fix=None):
    t = open(os.path.join(SITE, name + '.html')).read()
    t = inline_data(t, out_assets)
    head, body = split(t)
    head, body = clean(head), clean(body)
    if fix: head, body = fix(head, body)
    head, body = paths(links(head)), paths(links(body))
    return DOC_OPEN + head.strip() + DOC_HEAD_END + body.strip() + DOC_CLOSE

def sub1(pattern, repl, t, flags=re.S):
    n = re.subn(pattern, repl, t, count=1, flags=flags)
    assert n[1] == 1, 'não achou: ' + pattern[:80]
    return n[0]

# ---------- ajustes de cada página ----------
def fix_home(head, body):
    i = body.index('<a class="wd-works-card"'); j = body.rindex('<a class="wd-works-card"'); j = body.index('</a>', j) + 4
    body = body[:i] + "<?php get_template_part('parts/home-works'); ?>" + body[j:]
    body = sub1(r'<div class="wd-blog-list">.*?\n    </div>\n', "<div class=\"wd-blog-list\">\n<?php get_template_part('parts/home-blog'); ?>\n    </div>\n", body)
    return head, body

def fix_cases(head, body):
    body = sub1(r'const projects = \[.*?\];\n', 'const projects = <?php echo wp_json_encode(wd_projects(), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES); ?>;\n', body)
    body = body.replace('a.href = "' + A + PAGES['case'] + '#" + p.slug;', 'a.href = p.url;')
    body = body.replace('a.href = "<?php echo esc_url(wd_url(\'cases/\')); ?>#" + p.slug;', 'a.href = p.url;')
    body = re.sub(r'<sup id="count" aria-hidden="true">\(\d+\)</sup>', '<sup id="count" aria-hidden="true">(<?php echo count(wd_cases()); ?>)</sup>', body)
    return head, body

CASE_JS = r'''<script>
/* Case: vídeo do bloco 5 carrega perto da tela e toca com 50% visível; o item focado pelo teclado entra na tela */
(function(){
  const track=document.getElementById('track'); if(!track) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches||document.documentElement.classList.contains('wd-lite');
  const vs=[...track.querySelectorAll('video.case-video')];
  if(!still&&vs.length){
    const load=v=>{if(v.dataset.ld)return;v.dataset.ld=1;v.querySelectorAll('source[data-src]').forEach(s=>s.src=s.dataset.src);v.load();};
    const ioLoad=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){load(en.target);ioLoad.unobserve(en.target);}}),{rootMargin:'300px'});
    const ioPlay=new IntersectionObserver(es=>es.forEach(en=>{const v=en.target;if(en.intersectionRatio>=.5){load(v);const p=v.play();p&&p.catch(()=>{});}else v.pause();}),{threshold:[0,.5,1]});
    vs.forEach(v=>{ioLoad.observe(v);ioPlay.observe(v);});
  }
  track.addEventListener('focusin',e=>{
    if(matchMedia('(max-width:900px)').matches)return;
    const hs=document.getElementById('hs'), st=hs&&hs.querySelector('.stick'); if(!hs)return;
    if(st)st.scrollLeft=0;
    const r=e.target.getBoundingClientRect(), x=r.left-track.getBoundingClientRect().left;
    const dist=Math.max(0,track.scrollWidth-innerWidth), want=Math.min(dist,Math.max(0,x+r.width/2-innerWidth/2));
    scrollTo({top:hs.getBoundingClientRect().top+scrollY+want,behavior:'auto'});
  });
})();
</script>'''

def fix_case(head, body):
    body = sub1(r'(<div class="track" id="track">).*?(</a>)(\s*</div>\s*</div>\s*</section>)', r"\1\n<?php get_template_part('parts/case-track'); ?>\3", body)
    body = sub1(r'<script>\s*/\* Cases: o endereço #slug.*?</script>', CASE_JS, body)
    body = sub1(r'<script>\(function\(\)\{var h=document\.querySelector\(\'\.intro h1\'\).*?</script>\s*', '', body)
    # "Próximo case": ao fim da animação de carregamento, abre a página do próximo case
    body = body.replace("const nx=document.getElementById('next'); window.wdGoCase&&nx&&wdGoCase(nx.dataset.slug); loader.classList.remove('on');",
                        "const nx=document.getElementById('next'); if(nx){location.href=nx.href;return;} loader.classList.remove('on');")
    assert 'location.href=nx.href' in body
    return head, body

def fix_blog(head, body):
    body = sub1(r'const IMG = \{.*?\};', 'const IMG = <?php $wd_b = wd_blog_data(); echo wp_json_encode($wd_b[\'img\'], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES); ?>;', body)
    body = sub1(r'const CATS = \[.*?\];', 'const CATS = <?php echo wp_json_encode($wd_b[\'cats\'], JSON_UNESCAPED_UNICODE); ?>;', body)
    body = sub1(r'const FEATURED = \{.*?\};', 'const FEATURED = <?php echo wp_json_encode($wd_b[\'featured\'], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES); ?>;', body)
    body = sub1(r'const POSTS = \[.*?\];', 'const POSTS = <?php echo wp_json_encode($wd_b[\'posts\'], JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES); ?>;', body)
    body = sub1(r'const PURL=\{.*?\};const link=p=>[^\n]*', 'const link=p=>`href="${p.url}"`;', body)
    # links para quem não roda JavaScript (e para os buscadores)
    body = sub1(r'(<ul class="list" id="list"[^>]*>)(</ul>)', r"\1<?php foreach ($wd_b['posts'] as $p) : ?><li class=\"row\"><a href=\"<?php echo esc_url($p['url']); ?>\"><h3><?php echo esc_html($p['title']); ?></h3></a></li><?php endforeach; ?>\2", body)
    return head, body

def fix_post(head, body):
    body = sub1(r'<header class="ph wrap">.*?</main>', "<?php get_template_part('parts/single-post'); ?>\n</main>", body)
    body = sub1(r'<script>\s*/\* Artigos do blog.*?</script>\s*', '', body)
    return head, body

def main_swap(part):
    def f(head, body):
        body = sub1(r'(<main[^>]*>).*?(</main>)', r"\1\n<?php get_template_part('parts/" + part + r"'); ?>\n\2", body)
        # sem listagem nesta página: sai o script da listagem do blog (fica o resto: animação de entrada e cursor)
        i = body.index('// Conteúdo: troque os artigos aqui.'); j = body.index('// Reveal', i)
        body = body[:i] + body[j:]
        return head, body
    return f


def gen_single_post(assets):
    t = open(os.path.join(SITE, 'post.html')).read()
    share_top = re.search(r'<div class="share share-top rv".*?</div></div>', t, re.S).group(0)
    share_end = re.search(r'<div class="share share-end rv".*?</div></div>', t, re.S).group(0)
    end = re.search(r'<aside class="end rv".*?</aside>', t, re.S).group(0)
    rt_svg = re.search(r'<span class="rt">(<svg.*?</svg>)', t).group(1)
    data = '<?php echo esc_attr(rawurlencode(get_permalink())); ?>'
    share_top = re.sub(r'data-url="[^"]*"', 'data-url="' + data + '"', share_top, count=1)
    share_end = re.sub(r'data-url="[^"]*"', 'data-url="' + data + '"', share_end, count=1)
    import seo_extras
    svc = {k: list(v) for k, v in seo_extras.SVC.items()}
    php = """<?php
/* Artigo: cabeçalho, imagem, texto, próximos passos, compartilhar e relacionados */
if (!defined('ABSPATH')) exit;
the_post();
$post = get_post();
$cat = wd_post_cat($post);
$author = get_userdata($post->post_author);
$photo = $author ? wd_user_img($author, 'wd_foto', 'thumbnail') : '';
$sign = $author ? wd_user_img($author, 'wd_assinatura', 'medium') : '';
$name = $author ? $author->display_name : 'Work Digital';
$next = """ + "json_decode('" + json.dumps(svc, ensure_ascii=False).replace("'", "\\'") + "', true)" + """;
$nx = $next[$cat ? $cat->name : ''] ?? $next['Negócios'];
$thumb = get_post_thumbnail_id($post);
?>
  <header class="ph wrap">
    <div class="top rv"><?php if ($cat) : ?><a class="chip" href="<?php echo esc_url(get_category_link($cat)); ?>"><?php echo esc_html($cat->name); ?></a><?php endif; ?><span>Publicado em <time datetime="<?php echo esc_attr(get_the_date('c')); ?>"><?php echo esc_html(wd_date($post)); ?></time></span></div>
    <h1 class="rv"><?php the_title(); ?></h1>
    <p class="dek rv"><?php echo esc_html(wd_dek($post)); ?></p>
    <div class="by rv">
      <a class="au" href="<?php echo esc_url(wd_bio_url()); ?>" rel="author"><?php if ($photo) : ?><img class="av" src="<?php echo esc_url($photo); ?>" alt="" width="32" height="32" style="object-fit:cover"><?php else : ?><span class="av" aria-hidden="true"><?php echo esc_html(mb_substr($name, 0, 1)); ?></span><?php endif; ?><?php echo esc_html($name); ?></a>
      <span class="rt">""" + rt_svg + """<?php echo (int) wd_reading_time($post); ?> min</span>
    </div>
    """ + share_top + """
  </header>
  <div class="wrap">
    <?php if ($thumb) : ?><figure class="hero-img rv" style="margin-left:auto;margin-right:auto"><?php echo wp_get_attachment_image($thumb, 'full', false, ['loading' => 'eager', 'fetchpriority' => 'high', 'sizes' => '(max-width: 1100px) 100vw, 1100px']); ?></figure><?php endif; ?>

    <article class="body" id="body">
      <?php the_content(); ?>
      <aside class="wd-next" aria-label="Próximos passos"><h2><?php echo esc_html($nx[0]); ?></h2><p><?php echo esc_html($nx[1]); ?></p><p class="l"><a href="<?php echo esc_url(wd_url('solucoes/')); ?>">Conheça as soluções e os planos</a><a href="<?php echo esc_url(wd_url('cases/')); ?>">Veja os cases da Work</a></p></aside>
      <?php if ($author) : ?><div class="wd-sign"><?php if ($sign) : ?><img src="<?php echo esc_url($sign); ?>" alt="Assinatura de <?php echo esc_attr($name); ?>" loading="lazy"><?php endif; ?><p>Por <a href="<?php echo esc_url(wd_bio_url()); ?>" rel="author"><?php echo esc_html($name); ?></a><?php $cargo = get_user_meta($author->ID, 'wd_cargo', true); if ($cargo) echo ', ' . esc_html($cargo); ?></p></div><?php endif; ?>
      """ + share_end + """
      """ + end + """
    </article>

    <section class="rel" aria-labelledby="rel-t">
      <div class="hd2"><h2 id="rel-t" class="rv">Artigos relacionados</h2><a class="all" href="<?php echo esc_url(get_permalink(get_option('page_for_posts')) ?: wd_url('blog/')); ?>">Ver todos os artigos <svg viewBox="0 0 10 10"><path d="M3 1.5 7 5 3 8.5z" fill="currentColor"/></svg></a></div>
      <div class="cards">
        <?php foreach (wd_related($post) as $r) : ?><a class="card rv in" href="<?php echo esc_url(get_permalink($r)); ?>"><div class="im"><img src="<?php echo esc_url(wd_post_img($r, 'wd-card')); ?>" alt="" loading="lazy" decoding="async" width="1600" height="900"></div><p class="d">Publicado em <?php echo esc_html(wd_date($r)); ?></p><h3><?php echo esc_html(get_the_title($r)); ?></h3><div class="by"><span class="au"><span class="av" aria-hidden="true"><?php echo esc_html(mb_substr($name, 0, 1)); ?></span><?php echo esc_html($name); ?></span><span class="rt"><?php echo (int) wd_reading_time($r); ?> min</span></div></a><?php endforeach; ?>
      </div>
    </section>
  </div>
"""
    php = paths(links(php))
    open(os.path.join(OUT, 'parts', 'single-post.php'), 'w').write(php)

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns('assets-extra'))
    assets = os.path.join(OUT, 'assets')
    os.makedirs(assets, exist_ok=True)
    for f in ['app.js', 'contact.css', 'contact.js', 'wd-revision.css', 'wd-revision.js', 'whatsapp.js', 'favicon.svg']:
        shutil.copy(os.path.join(SITE, f), assets)
    shutil.copy(os.path.join(SRC, 'assets-extra', 'wd-theme.css'), assets)
    ft = open(os.path.join(SITE, 'footer.js')).read().replace("home: '" + A + PAGES['home'] + "'", "home: '/'")
    open(os.path.join(assets, 'footer.js'), 'w').write(ft)
    for d in ['media', 'ativos-externos']:
        shutil.copytree(os.path.join(SITE, d), os.path.join(assets, d))
    shutil.copytree(os.path.join(SITE, 'img'), os.path.join(assets, 'img'), ignore=shutil.ignore_patterns('blog'))
    tpl = {'front-page.php': page('home', assets, fix_home),
           'page-solucoes.php': page('solucoes', assets),
           'archive-case.php': page('cases', assets, fix_cases),
           'single-case.php': page('case-interna', assets, fix_case),
           'home.php': page('blog', assets, fix_blog),
           'single.php': page('post', assets, fix_post),
           'page-bio.php': page('blog', assets, main_swap('bio')),
           'page.php': page('blog', assets, main_swap('page')),
           '404.php': page('blog', assets, main_swap('404')),
           'index.php': page('blog', assets, main_swap('page'))}
    for name, t in tpl.items():
        assert '<?' not in t.replace('<?php', ''), name
        open(os.path.join(OUT, name), 'w').write(t)
    # FAQ de Soluções (mesmo conteúdo da página) para os dados estruturados
    import seo_extras
    faq = 'function wd_faq() { return ' + json.dumps(seo_extras.FAQ, ensure_ascii=False).replace('[[', '[[').replace('$', '\\$') + '; }\n'
    with open(os.path.join(OUT, 'inc', 'data.php'), 'a') as f: f.write('\n' + faq)
    gen_single_post(assets)
    print('tema gerado em', OUT)

if __name__ == '__main__':
    build()
