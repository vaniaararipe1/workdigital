# Uma página por artigo (artigo-{slug}.html): mesma página do post, com título, descrição, prévia e JSON-LD do artigo
# já no HTML publicado — o título da aba e a prévia do link mostram o artigo certo.
import html as H, json, os, re
import a11y_seo as AS

def run(out):
    t = open(os.path.join(out, 'post.html')).read()
    data = json.loads(re.search(r'window\.WD_POSTS=(\{.*?\});\n', t).group(1).replace('<\\/', '</'))
    e = lambda s: H.escape(s, quote=True)
    for p in data['list']:
        slug, title = p['slug'], p['title'] + ' - Work Digital'
        url, img = f'{AS.SITE}/blog/{slug}/', f'{AS.SITE}/img/blog/{slug}.jpg'
        u = t.replace('<title>', '<title>', 1)
        u = re.sub(r'<title>[^<]*</title>', '<title>' + e(title) + '</title>', u, count=1)
        for attr, key, val in [('name', 'description', p['excerpt']), ('property', 'og:url', url), ('property', 'og:title', title),
                               ('property', 'og:description', p['excerpt']), ('property', 'og:image', img),
                               ('name', 'twitter:title', title), ('name', 'twitter:description', p['excerpt']), ('name', 'twitter:image', img)]:
            u, n = re.subn(rf'(<meta {attr}="{re.escape(key)}" content=")[^"]*"', lambda m: m.group(1) + e(val) + '"', u, count=1)
            assert n == 1, key
        u, n = re.subn(r'(<link rel="canonical" href=")[^"]*"', lambda m: m.group(1) + url + '"', u, count=1); assert n == 1
        ld = {'@context': 'https://schema.org', '@graph': [
            {'@type': 'BlogPosting', 'headline': p['title'], 'description': p['excerpt'], 'image': img, 'datePublished': p['iso'],
             'inLanguage': 'pt-BR', 'articleSection': p['cat'], 'url': url, 'mainEntityOfPage': url,
             'author': {'@type': 'Organization', 'name': 'Equipe Work Digital', 'url': AS.SITE + '/'},
             'publisher': {'@type': 'Organization', 'name': 'Work Digital', 'logo': {'@type': 'ImageObject', 'url': AS.LOGO}}},
            {'@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': AS.SITE + '/'},
                {'@type': 'ListItem', 'position': 2, 'name': 'Blog', 'item': AS.SITE + '/blog/'},
                {'@type': 'ListItem', 'position': 3, 'name': p['title'], 'item': url}]}]}
        u, n = re.subn(r'<script[^>]*id="wd-ld-post"[^>]*>.*?</script>',
                       lambda _: AS.ld(ld).replace('<script ', '<script id="wd-ld-post" ', 1), u, count=1, flags=re.S); assert n == 1
        # texto do artigo no HTML (antes do script): título e linha fina
        u, n = re.subn(r'(<h1 class="rv">)[^<]*(</h1>)', lambda m: m.group(1) + e(p['title']) + m.group(2), u, count=1); assert n == 1
        u = re.sub(r'(<p class="dek[^"]*">)[\s\S]*?(</p>)', lambda m: m.group(1) + e(p['dek']) + m.group(2), u, count=1)
        u = u.replace('window.WD_POSTS=', f'window.WD_POST_DEFAULT="{slug}";window.WD_POSTS=', 1)
        open(os.path.join(out, f'artigo-{slug}.html'), 'w').write(u)
