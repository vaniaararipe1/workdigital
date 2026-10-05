# SEO, fase 2: FAQ em Soluções, links internos no fim de cada artigo e blog sem seletor de idioma (o blog é só em português)
import html as H, json, os, re
import a11y_seo as AS
from apply_home import PAGES

FAQ = [
    ('Quanto custa um site profissional?',
     'Depende do formato. O blog de conteúdo custa R$ 995 em pagamento único. O site profissional por assinatura custa R$ 590 por mês, com suporte e hospedagem. O site profissional personalizado tem orçamento sob consulta, de acordo com o número de páginas e as funções do projeto.'),
    ('Qual é a diferença entre o site por assinatura e o site personalizado?',
     'O site por assinatura usa um design padrão, via template, com até 4 páginas ou OnePage, e inclui suporte e hospedagem mensal. O site personalizado tem design exclusivo, número de páginas sob medida, formulários estratégicos e conexão com ferramentas externas, com pagamento único.'),
    ('O que está incluído na assinatura mensal?',
     'Hospedagem, 2 horas de manutenção por mês e suporte por 12 meses, além de layout responsivo, otimização SEO básica e integração com redes sociais, Google Analytics e Google Search Console.'),
    ('Vou conseguir atualizar o site sozinho?',
     'Sim. Os sites são feitos em WordPress, com gerenciador de conteúdo, para você editar textos, imagens e publicar artigos sem depender de programação.'),
    ('O site funciona bem no celular?',
     'Sim. Todos os planos têm layout responsivo: o site se adapta a celulares, tablets e computadores.'),
    ('O site já vem preparado para aparecer no Google?',
     'Sim. Todos os planos incluem otimização SEO e integração com o Google Search Console e o Google Analytics. O blog de conteúdo e o site personalizado têm otimização SEO avançada.'),
    ('O site segue a LGPD?',
     'Sim. Todos os planos são entregues em conformidade com a Lei Geral de Proteção de Dados (LGPD).'),
    ('Vocês também criam lojas virtuais e landing pages?',
     'Sim. Além de sites e blogs, a Work Digital cria lojas virtuais e landing pages focadas em conversão. Fale com a gente para receber uma proposta sob medida.'),
]

FAQ_CSS = '''
/* Perguntas frequentes (Soluções) */
.faq{position:relative;z-index:1;width:min(calc(100% - 2 * var(--wd-layout-gutter,3vw)),980px);margin:0 auto 18vh;font-family:var(--body)}
.faq h2{margin:0 0 clamp(28px,4vw,48px);text-align:center;font:500 clamp(32px,3.6vw,52px)/1.05 var(--display);letter-spacing:-.04em;background:linear-gradient(90deg,#cbb6ff 0%,#efe7ff 30%,#fffdfa 55%,#f5c3d8 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.faq details{border-bottom:1px solid rgba(189,164,255,.18)}
.faq details:first-of-type{border-top:1px solid rgba(189,164,255,.18)}
.faq summary{list-style:none;display:flex;align-items:center;justify-content:space-between;gap:24px;padding:24px 4px;cursor:pointer;font:500 clamp(18px,1.5vw,22px)/1.3 var(--display);letter-spacing:-.01em;color:#F7F6FB}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";flex:none;display:grid;place-items:center;width:36px;height:36px;border-radius:50%;border:1px solid rgba(189,164,255,.35);font-size:20px;color:#EDE4FF;transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq summary:hover{color:#fff}
.faq details p{margin:0;padding:0 56px 26px 4px;font-size:16px;line-height:1.65;color:#d9d3e6}
@media(max-width:600px){.faq details p{padding-right:4px}}
@media(prefers-reduced-motion:reduce){.faq summary::after{transition:none}}
'''

def faq(t):
    if 'class="faq"' in t: return t
    items = ''.join(f'<details><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a in FAQ)
    sec = f'\n<section class="faq" id="perguntas" aria-labelledby="faq-title">\n <h2 id="faq-title">Perguntas frequentes</h2>\n {items}\n</section>\n'
    m = re.search(r'(<section class="pricing" id="planos".*?</section>)', t, re.S)
    assert m
    t = t[:m.end()] + sec + t[m.end():]
    ld = AS.ld({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in FAQ]})
    t = t.replace('</title>', '</title>\n' + ld, 1)
    return t.replace('</style>', FAQ_CSS + '</style>', 1)

# fim de cada artigo: caminho para os serviços e para os cases (links internos)
SVC = {
    'Lojas virtuais': ('Quer uma loja virtual que vende mais?', 'A Work Digital cria lojas virtuais de alta performance, focadas em conversão.'),
    'SEO': ('Quer um site que aparece no Google?', 'Todos os nossos sites já saem com otimização SEO e integração com o Google Search Console.'),
    'Performance': ('Quer um site rápido e fácil de manter?', 'Criamos sites de alta performance, com suporte e manutenção mensal.'),
    'Tráfego': ('Quer transformar visitas em clientes?', 'Criamos sites e landing pages pensados para converter o tráfego que você já tem.'),
    'Criação de sites': ('Pronto para ter um site profissional?', 'Conheça os planos da Work Digital: blog de conteúdo, site por assinatura e site personalizado.'),
    'Negócios': ('Pronto para levar o seu negócio para a internet?', 'Conheça os planos da Work Digital: blog de conteúdo, site por assinatura e site personalizado.'),
}
REL_CSS = ('.wd-next{margin:48px 0 0;padding:28px 30px;border-radius:20px;background:#F3EFFB;display:grid;gap:10px}'
           '#body .wd-next h2{margin:0!important;padding:0;font:500 clamp(22px,2vw,28px)/1.2 var(--display);letter-spacing:-.02em;color:var(--ink)}'
           '#body .wd-next p{margin:0;color:#4a4458;line-height:1.6}'
           '#body .wd-next .l{display:flex;flex-wrap:wrap;gap:12px 24px;margin-top:6px}'
           '#body .wd-next a{font-weight:600;color:#6025E1;text-decoration:underline;text-underline-offset:3px}'
           '#body .wd-next a:hover{color:#C00252}')

def articles(t):
    if 'wdNext' in t: return t
    svc = json.dumps(SVC, ensure_ascii=False)
    fn = ("const wdNext=c=>{const s=" + svc + "[c]||" + json.dumps(SVC['Negócios'], ensure_ascii=False) + ";"
          "return '<aside class=\"wd-next\" aria-label=\"Próximos passos\"><h2>'+s[0]+'</h2><p>'+s[1]+'</p><p class=\"l\">"
          "<a href=\"" + PAGES['solucoes'] + "\" target=\"_top\">Conheça as soluções e os planos</a>"
          "<a href=\"" + PAGES['cases'] + "\" target=\"_top\">Veja os cases da Work</a></p></aside>';};\n")
    a = "end.insertAdjacentHTML('beforebegin','<p class=\"lead\">'+esc(p.lead)+'</p>'+p.body);"
    assert t.count(a) == 1
    t = t.replace(a, "end.insertAdjacentHTML('beforebegin','<p class=\"lead\">'+esc(p.lead)+'</p>'+p.body+wdNext(p.cat));")
    t = t.replace('window.WD_POSTS=', fn + 'window.WD_POSTS=', 1)
    return t.replace('</style>', REL_CSS + '</style>', 1)

def no_lang(t):
    return re.sub(r'\s*<div class="nav-item wd-language">.*?</div>\s*</div>', '', t, count=1, flags=re.S)

def run(out):
    for f, fns in (('solucoes.html', [faq]), ('blog.html', [no_lang]), ('post.html', [no_lang, articles])):
        p = os.path.join(out, f); t = open(p).read()
        for fn in fns: t = fn(t)
        open(p, 'w').write(t)
