# Monta importacao/conteudo.json: cases, artigos, páginas e configurações do site, com os caminhos dos arquivos.
# O importador (importar.php) lê este arquivo e envia os arquivos para a Biblioteca de mídia do WordPress.
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site')
sys.path.insert(0, SITE)
import a11y_seo as AS, blog_articles as BA
rel = lambda p: os.path.relpath(p, ROOT)

def ex(p):
    assert os.path.exists(p), p
    return rel(p)

# ---------- cases ----------
CI = json.load(open(os.path.join(SITE, 'cases', 'conteudo-cases.json')))['cases']
DP = {c['slug']: c for c in json.load(open(os.path.join(SITE, 'dados-projetos.json')))['cases']}
HOME = [h['slug'].replace('-home', '') for h in json.load(open(os.path.join(SITE, 'dados-projetos.json')))['home']]
HOME_DESC = {h['slug'].replace('-home', ''): h['descricao'] for h in json.load(open(os.path.join(SITE, 'dados-projetos.json')))['home']}
import ast
_src = open(os.path.join(SITE, 'cases_pages.py')).read()
PROJETO = ast.literal_eval(re.search(r'PROJETO = (\{.*?\})\n', _src, re.S).group(1))
BLOCK = {'01': '01-home', '02': '02-key-visual', '03': '03-detalhe', '04': '04-pagina', '05': '05-mobile', '06': '06-conceito', '07': '07-paleta'}
cases = []
for c in sorted(CI, key=lambda c: c['ordem']):
    s = c['slug']; d = DP[s]; cdir = os.path.join(SITE, 'cases', s); tdir = os.path.join(SITE, 'thumbs')
    files = {}
    for n, f in BLOCK.items():
        files['m' + n] = {'file': ex(os.path.join(cdir, f + '.webp')), 'alt': c['alt'].get(f, '')}
    for x in ('mp4', 'webm'):
        p = os.path.join(cdir, '05-mobile.' + x)
        if os.path.exists(p): files['v05_' + x] = {'file': rel(p)}
    for pre, suf in (('thumb', ''), ('home', '-home')):
        if pre == 'home' and s not in HOME: continue
        for k, ext in (('webp', 'webp'), ('mp4', 'mp4'), ('webm', 'webm'), ('anim', 'anim.webp')):
            p = os.path.join(tdir, s + suf + '.' + ext)
            if os.path.exists(p): files[pre + '_' + k] = {'file': rel(p), 'alt': (c['titulo'] + ' — prévia do site') if ext == 'webp' else ''}
    meta = {'projeto': PROJETO.get(s, ''), 'p1': c['p1'], 'p2': c['p2'], 'servicos': '\n'.join(c['servicos']),
            'link': c.get('link') or d.get('link') or '', 'link_mostrar': '1' if c.get('link_status') == 'mostrar' else '',
            'legenda_01': c['legendas'].get('01-home', ''), 'legenda_03': c['legendas'].get('03-detalhe', ''), 'legenda_04': c['legendas'].get('04-pagina', ''),
            'frase': d['frase'], 'formato': d['formato'], 'home_slot': str(HOME.index(s) + 1) if s in HOME else '0',
            'home_desc': HOME_DESC.get(s, ''), 'frase_conceito': c.get('frase_conceito', '')}
    cases.append({'slug': s, 'title': c['titulo'], 'order': c['ordem'], 'meta': meta, 'files': files,
                  'seo_title': c['seo_title'], 'seo_desc': c['seo_description']})

# ---------- artigos ----------
fotos = json.load(open(os.path.join(SITE, 'img', 'blog', 'fotos.json')))
posts = []
for slug, cat, iso, _ in BA.META:
    a = json.load(open(os.path.join(SITE, 'blog-artigos', slug + '.json')))
    posts.append({'slug': slug, 'title': a['title'], 'date': iso + ' 09:00:00', 'cat': cat, 'excerpt': a['excerpt'], 'dek': a['dek'],
                  'content': '<p class="lead">' + a['lead'] + '</p>\n' + a['body'],
                  'image': {'file': ex(os.path.join(SITE, 'img', 'blog', slug + '.jpg')), 'alt': fotos.get(slug, {}).get('alt', '')},
                  'seo_desc': a['excerpt']})
# artigos que já existiam no site antigo
t = open(os.path.join(SITE, 'post.html')).read()
body = t[t.index('<article class="body" id="body">') + len('<article class="body" id="body">'):t.index('<div class="share share-end')]
body = body.replace('https://claude.ai/artifact/Y2eQb4LZVTwWfbNdqz7nbi', '/solucoes/').replace(' target="_top"', '').strip()
dek = re.sub(r'<[^>]+>', '', re.search(r'<p class="dek[^"]*">(.*?)</p>', t, re.S).group(1)).strip()
posts.append({'slug': 'como-potencializar-a-sua-marca-com-o-blog-marketing', 'title': 'Como potencializar a sua marca com o blog marketing',
              'date': '2022-06-07 09:00:00', 'cat': 'Negócios', 'excerpt': dek, 'dek': dek, 'content': body,
              'image': {'file': ex(os.path.join(SITE, 'img', 'foto-3dbce2d9fa.jpg')), 'alt': 'Mulher sorrindo olhando o celular, cercada de ícones de redes sociais, mensagens e vídeo'},
              'seo_desc': dek})
seis = open(os.path.join(ROOT, 'wordpress', 'importacao', 'extra', '6-motivos.html')).read()
d6 = 'Ter um site não é um luxo, é necessidade. Veja 6 motivos que mostram a importância de ter um site para o seu negócio.'
posts.append({'slug': '6-motivos-que-mostram-a-importancia-de-ter-um-site-para-o-seu-negocio', 'title': '6 motivos que mostram a importância de ter um site para o seu negócio',
              'date': '2022-05-16 23:52:37', 'cat': 'Negócios', 'excerpt': d6, 'dek': d6, 'content': seis,
              'image': {'file': ex(os.path.join(ROOT, 'wordpress', 'importacao', 'extra', '6-motivos-que-mostram-a-importancia-de-ter-um-site-para-o-seu-negocio.jpg')), 'alt': 'Notebook com um site aberto sobre a mesa'},
              'seo_desc': d6})

# ---------- páginas e configurações ----------
P = AS.PAGES
pages = [
    {'slug': 'home', 'title': 'Home', 'seo_title': 'Work Digital - Criação de Sites Profissionais', 'seo_desc': P['home.html'][2], 'content': ''},
    {'slug': 'solucoes', 'title': 'Soluções', 'seo_title': 'Work Digital - Soluções para o seu negócio', 'seo_desc': P['solucoes.html'][2], 'content': ''},
    {'slug': 'blog', 'title': 'Blog', 'seo_title': 'Work Digital - Blog da Work', 'seo_desc': P['blog.html'][2], 'content': ''},
    {'slug': 'bio', 'title': 'Bio', 'seo_title': '', 'seo_desc': 'Conheça quem escreve os artigos do Blog da Work.', 'content': ''},
    {'slug': 'contato', 'title': 'Contato', 'seo_title': 'Contato - Work Digital', 'seo_desc': 'Fale com a Work Digital e peça uma proposta para o seu site, blog, landing page ou loja virtual.',
     'content': '<p>Conte para a gente o que você precisa. Respondemos rápido.</p>\n<p><button class="wd-work-cta wd-cta" type="button" data-wd-contact><span>Solicitar proposta</span></button></p>\n<p>Se preferir, fale pelo WhatsApp: <a href="https://wa.me/5511993916363">(11) 99391-6363</a>.</p>'},
    {'slug': 'politica-de-privacidade', 'title': 'Política de privacidade', 'status': 'draft', 'seo_title': '', 'seo_desc': 'Como a Work Digital trata os dados pessoais de quem visita o site.',
     'content': open(os.path.join(ROOT, 'wordpress', 'importacao', 'politica-de-privacidade.html')).read()},
]
settings = {
    'cases_archive_title': 'Work Digital - Cases da Work', 'cases_archive_desc': P['cases.html'][2],
    'company_name': 'Work Digital', 'company_logo': ex(os.path.join(SITE, 'ativos-externos', 'logo-work-digital-branco-criacao-de-site-sp.svg')),
    'social': AS.SOCIAL, 'site_icon': ex(os.path.join(SITE, 'favicon.svg')),
}
cats = ['Criação de sites', 'Lojas virtuais', 'SEO', 'Performance', 'Tráfego', 'Negócios']
json.dump({'cases': cases, 'posts': posts, 'pages': pages, 'categories': cats, 'settings': settings},
          open(os.path.join(ROOT, 'wordpress', 'importacao', 'conteudo.json'), 'w'), ensure_ascii=False, indent=1)
print(len(cases), 'cases;', len(posts), 'artigos;', len(pages), 'páginas;', sum(len(c['files']) for c in cases), 'arquivos de cases')
