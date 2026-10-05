# Google Tag Manager (GTM-592RCDK9) em todas as páginas: script no topo do <head> e noscript logo após a abertura do <body>
import glob, os, re
ID = 'GTM-592RCDK9'
HEAD = f'''<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{ID}');</script>
<!-- End Google Tag Manager -->
'''
BODY = f'''<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
'''
def fix_text(t):
    if ID in t:
        return t
    # topo do <head>: logo depois do <head> (ou do charset, que precisa vir primeiro), senão no início do arquivo
    m = re.search(r'<head(?:\s[^>]*)?>\s*(<meta charset[^>]*>\s*)?', t, re.I) or re.match(r'\s*(<meta charset[^>]*>\s*)?', t, re.I)
    t = t[:m.end()] + HEAD + t[m.end():]
    # logo após a abertura do <body>; as páginas sem <body> (o artifact cria o skeleton) recebem antes do primeiro elemento visível
    mb = re.search(r'<body(?:\s[^>]*)?>\s*', t, re.I)
    if not mb:
        mb = re.search(r'</head>\s*', t, re.I) or re.search(r'(?=<(header|main|div|section|nav)\b)', t)
    pos = mb.end() if mb.group(0) else mb.start()
    return t[:pos] + BODY + t[pos:]
def run(out):
    for p in glob.glob(os.path.join(out, '*.html')):
        t = open(p).read(); n = fix_text(t)
        if n != t: open(p, 'w').write(n)
