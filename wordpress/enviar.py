#!/usr/bin/env python3
"""Envia o site para um WordPress pela internet (sem SSH), usando uma senha de aplicativo.

Uso:
  WD_SENHA_APP='xxxx xxxx xxxx xxxx xxxx xxxx' python3 wordpress/enviar.py https://workdigital.art.br login

Antes: tema Work Digital instalado e ativo. O Yoast é instalado e ativado por este script.
Pode rodar de novo: arquivos e textos já enviados são reaproveitados (nada é duplicado).
"""
import hashlib, json, os, sys, time
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
site, user = sys.argv[1].rstrip('/'), sys.argv[2]
pw = os.environ.get('WD_SENHA_APP') or sys.exit('Defina WD_SENHA_APP com a senha de aplicativo.')
S = requests.Session(); S.auth = (user, pw); S.headers['User-Agent'] = 'WorkDigital-Envio/1.0'

def call(method, path, tries=4, params=None, **kw):
    # ?rest_route= funciona com qualquer configuração de links permanentes (inclusive numa instalação nova)
    q = dict(params or {}); q['rest_route'] = path
    for i in range(tries):
        try:
            r = S.request(method, site + '/', params=q, timeout=180, **kw)
            if r.status_code < 500 and r.status_code != 429: return r
        except requests.RequestException as e:
            r = e
        time.sleep(2 * (i + 1))
    return r

def ok(r, what):
    if isinstance(r, Exception) or r.status_code >= 300:
        msg = r if isinstance(r, Exception) else f'{r.status_code} {r.text[:300]}'
        sys.exit(f'Falhou: {what}: {msg}')
    return r.json()

data = json.load(open(os.path.join(ROOT, 'wordpress', 'importacao', 'conteudo.json')))

# 1. acesso e tema
r = call('GET', '/wd/v1/import/ping')
if isinstance(r, Exception) or r.status_code == 404:
    sys.exit('O tema Work Digital não está ativo (ou a API do WordPress está bloqueada).')
if r.status_code in (401, 403):
    sys.exit(f'Acesso negado ({r.status_code}): confira o login e a senha de aplicativo. Se persistir, a hospedagem pode estar removendo o cabeçalho de autenticação.')
info = ok(r, 'verificação'); print('Conectado:', info)

# 2. Yoast
if not info['yoast']:
    r = call('POST', '/wp/v2/plugins', json={'slug': 'wordpress-seo', 'status': 'active'})
    if isinstance(r, Exception) or r.status_code >= 300:  # já instalado (inativo) ou sem download: tenta só ativar
        r = call('POST', '/wp/v2/plugins/wordpress-seo/wp-seo', json={'status': 'active'})
    if isinstance(r, Exception) or r.status_code >= 300:
        print('Aviso: não consegui instalar o Yoast; instale pelo painel (Plugins › Adicionar novo) e rode de novo.')
    else:
        print('Yoast ativo.')

# 3. páginas e categorias
print('Páginas:', ok(call('POST', '/wd/v1/import/setup', json={'pages': data['pages'], 'categories': data['categories']}), 'páginas')['paginas'])

# 4. arquivos
cache = {}
def media(f):
    rel = f['file']
    if rel in cache: return cache[rel]
    path = os.path.join(ROOT, rel)
    h = hashlib.md5(open(path, 'rb').read()).hexdigest()
    found = ok(call('GET', '/wd/v1/import/media', params={'src': rel, 'hash': h}), 'consulta ' + rel)['id']
    if not found:
        name = (os.path.basename(os.path.dirname(path)) + '-' + os.path.basename(path)) if '/cases/' in rel else os.path.basename(path)
        with open(path, 'rb') as fh:
            found = ok(call('POST', '/wd/v1/import/media', files={'file': (name, fh)}, data={'src': rel, 'hash': h, 'alt': f.get('alt', ''), 'name': name}), 'envio ' + rel)['id']
        print('  enviado', rel, '->', found)
    cache[rel] = found
    return found

kw = {}
for fn in os.listdir(os.path.join(ROOT, 'site', 'blog-artigos')):
    j = json.load(open(os.path.join(ROOT, 'site', 'blog-artigos', fn))); kw[fn[:-5]] = (j.get('keywords') or [''])[0]

# 5. artigos
for p in data['posts']:
    img = media(p['image'])
    res = ok(call('POST', '/wd/v1/import/post', json={'post': p, 'image_id': img, 'keyword': kw.get(p['slug'], '')}), 'artigo ' + p['slug'])
    print('Artigo:', res['url'])

# 6. cases
for c in data['cases']:
    files = {k: media(f) for k, f in c['files'].items()}
    ok(call('POST', '/wd/v1/import/case', json={'case': c, 'files': files}), 'case ' + c['slug'])
    print('Case:', c['title'])

# 7. endereços e Yoast
print('Finalização:', ok(call('POST', '/wd/v1/import/finish', json=data['settings']), 'finalização'))
print('Pronto:', site)
