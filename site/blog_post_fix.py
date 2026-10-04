# Blog e Post: ajustes pedidos (título do blog, CTA final do post no estilo da Work, compartilhamento)
import re, shutil
from urllib.parse import quote
def sub1(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)

def blog(t):
    # cor de destaque (hover dos títulos dos posts etc.): roxo da Work
    t = sub1(t, '--accent:#7C5CFF;', '--accent:#6025E1;')
    t = sub1(t, '<title>Blog Work Digital</title>', '<title>Blog da Work</title>')
    # post em destaque: sem sublinhado; no hover o título fica no roxo da Work, igual aos outros
    t = sub1(t, '.feat:hover h2 a{background-size:100% 2px}', '.feat h2 a{background-image:none!important;text-decoration:none!important;transition:color .3s}\n.feat:hover h2 a,.feat h2 a:focus-visible{color:var(--accent)}')
    t = sub1(t, '<h1 class="rv">Blog Work Digital</h1>', '<h1 class="rv">Blog da Work</h1>')
    t = sub1(t, '.hero h1{margin:0;font:600 clamp(56px,11.2vw,164px)/.92 var(--display);letter-spacing:-.055em}',
             '.hero h1{margin:0;font:600 clamp(44px,8vw,120px)/.94 var(--display);letter-spacing:-.05em}')
    return t

POST_URL = 'https://workdigital.art.br/como-potencializar-a-sua-marca-com-o-blog-marketing/'
ICONS = {
 'linkedin': '<path d="M4.5 9h3v10h-3zM6 4.2a1.8 1.8 0 1 1 0 3.6 1.8 1.8 0 0 1 0-3.6zM10 9h2.9v1.4c.4-.8 1.4-1.6 3-1.6 3.1 0 3.6 2 3.6 4.7V19h-3v-4.8c0-1.2 0-2.6-1.6-2.6s-1.9 1.2-1.9 2.5V19H10z" fill="currentColor"/>',
 'x': '<path d="M17.5 4h2.8l-6.1 7 7.2 9h-5.6l-4.4-5.6L6.3 20H3.5l6.5-7.5L3.1 4h5.7l4 5.1zm-1 14.4h1.6L7.6 5.5H5.9z" fill="currentColor"/>',
 'facebook': '<path d="M13.5 20v-7h2.4l.4-2.9h-2.8V8.3c0-.8.3-1.4 1.4-1.4h1.5V4.3c-.3 0-1.1-.1-2.1-.1-2.2 0-3.6 1.3-3.6 3.7v2.2H8.3V13h2.4v7z" fill="currentColor"/>',
 'whatsapp': '<path d="M12 3.5a8.4 8.4 0 0 0-7.2 12.8L3.7 20.5l4.3-1.1A8.4 8.4 0 1 0 12 3.5zm0 15.3c-1.3 0-2.6-.4-3.7-1l-.3-.2-2.5.7.7-2.4-.2-.3A6.9 6.9 0 1 1 12 18.8zm3.8-5.2c-.2-.1-1.2-.6-1.4-.7-.2-.1-.3-.1-.5.1l-.6.8c-.1.1-.2.2-.4.1a5.6 5.6 0 0 1-2.8-2.4c-.2-.4.2-.4.6-1.2.1-.1 0-.3 0-.4l-.6-1.5c-.2-.4-.3-.3-.5-.3h-.4a.8.8 0 0 0-.6.3 2.4 2.4 0 0 0-.7 1.8c0 1 .8 2.1.9 2.2.1.1 1.5 2.4 3.7 3.3 1.4.6 1.9.6 2.6.5.4-.1 1.2-.5 1.4-1 .2-.5.2-.9.1-1z" fill="currentColor"/>',
 'email': '<rect x="3.5" y="5.5" width="17" height="13" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m4.5 7 7.5 6 7.5-6" fill="none" stroke="currentColor" stroke-width="1.6"/>',
 'link': '<path d="M10.6 13.4a3.5 3.5 0 0 0 5 0l3-3a3.5 3.5 0 0 0-5-5l-1 1M13.4 10.6a3.5 3.5 0 0 0-5 0l-3 3a3.5 3.5 0 0 0 5 5l1-1" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>',
}
NAMES = [('linkedin','LinkedIn'),('x','X (Twitter)'),('facebook','Facebook'),('whatsapp','WhatsApp'),('email','E-mail')]
def share_bar(label, cls):
    items = ''.join(f'<a class="sh-btn" data-net="{k}" href="#" target="_blank" rel="noopener" aria-label="Compartilhar no {n}" title="{n}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[k]}</svg></a>' for k, n in NAMES)
    items += f'<button class="sh-btn sh-copy" type="button" aria-label="Copiar link do artigo" title="Copiar link"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS["link"]}</svg><span class="sh-tip" role="status"></span></button>'
    return f'<div class="share {cls}" data-url="{quote(POST_URL, safe="")}"><span class="sh-l">{label}</span><div class="sh-list">{items}</div></div>'

CSS = '''
/* Compartilhar (início e fim do post) */
.share{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.share .sh-l{font:500 13px/1 var(--display);letter-spacing:.08em;text-transform:uppercase;color:#4A4458}
.share .sh-list{display:flex;gap:8px;flex-wrap:wrap}
.share .sh-btn{position:relative;display:grid;place-items:center;width:40px;height:40px;border-radius:50%;border:1px solid rgba(23,19,31,.14);background:rgba(255,255,255,.55);color:#2B2533;padding:0;cursor:pointer;text-decoration:none!important;transition:background .3s,color .3s,border-color .3s,transform .3s}
.share .sh-btn svg{width:18px;height:18px}
.share .sh-btn:hover,.share .sh-btn:focus-visible{background:linear-gradient(135deg,#6025E1,#C00252) border-box;border-color:transparent;color:#fff;transform:translateY(-2px)}
.share .sh-btn:focus-visible{outline:2px solid #6025E1;outline-offset:3px}
.share .sh-tip{position:absolute;bottom:calc(100% + 8px);left:50%;transform:translateX(-50%);white-space:nowrap;padding:6px 10px;border-radius:8px;background:#17131F;color:#fff;font:500 12px/1 var(--display);opacity:0;pointer-events:none;transition:opacity .2s}
.share .sh-tip.on{opacity:1}
.share-top{justify-content:center;margin-top:22px}
.share-end{margin:48px 0 0;padding-top:28px;border-top:1px solid rgba(23,19,31,.10)}
@media(max-width:900px){.share-top{justify-content:flex-start}}
/* CTA no fim do post: mesma estética do site (vidro roxo, CTA da Work, imagem no estilo fotográfico da Work) */
.end{margin:40px 0 0!important;display:grid;grid-template-columns:1.05fr 1fr;border-radius:32px;overflow:hidden;min-height:340px;background:radial-gradient(120% 90% at 0% 0%,#4B247E 0%,#34165B 45%,#1E0F36 100%);box-shadow:0 30px 80px -30px rgba(52,22,91,.55);isolation:isolate}
.end .l{background:transparent;color:#fff;padding:40px;display:flex;flex-direction:column;justify-content:space-between;gap:28px}
.end .lgw{display:block;width:132px;height:auto}
.end h5{margin:0;font:500 clamp(26px,2.5vw,36px)/1.1 var(--display);letter-spacing:-.03em;color:#F7F6FB;text-wrap:balance}
.end .wd-work-cta{display:inline-flex;align-self:flex-start;align-items:center;gap:16px;min-height:54px;padding:14px 22px;border:0;border-radius:9999px;cursor:pointer;color:#fff;font:500 14px/1 var(--display);letter-spacing:.1em;text-transform:uppercase;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0;transition:background-position .6s ease,color .2s ease}
.end .wd-work-cta:hover,.end .wd-work-cta:focus-visible{background-position:0 0;color:#24123e}
.end .wd-work-cta svg{width:14px;height:14px}
.end .r{background:transparent;position:relative;padding:20px}
.end .r img{position:static;display:block;width:100%;height:100%;min-height:300px;object-fit:cover;object-position:50% 40%;border-radius:20px}
@media(max-width:760px){.end{grid-template-columns:1fr}.end .l{padding:32px 26px}.end .r{padding:0 20px 20px}.end .r img{min-height:240px;max-height:320px}}
'''
JS = '''<script>
/* Compartilhar: links das redes e copiar o endereço do artigo */
(function(){
  const title=document.querySelector('.ph h1')?.textContent.trim()||document.title;
  document.querySelectorAll('.share').forEach(box=>{
    const u=box.dataset.url, t=encodeURIComponent(title);
    const map={linkedin:`https://www.linkedin.com/sharing/share-offsite/?url=${u}`,x:`https://twitter.com/intent/tweet?url=${u}&text=${t}`,
      facebook:`https://www.facebook.com/sharer/sharer.php?u=${u}`,whatsapp:`https://api.whatsapp.com/send?text=${t}%20${u}`,
      email:`mailto:?subject=${t}&body=${t}%0A%0A${u}`};
    box.querySelectorAll('[data-net]').forEach(a=>{a.href=map[a.dataset.net];if(a.dataset.net==='email')a.removeAttribute('target');});
    const copy=box.querySelector('.sh-copy'),tip=copy.querySelector('.sh-tip');
    copy.addEventListener('click',async()=>{const url=decodeURIComponent(u);let ok=false;
      try{await navigator.clipboard.writeText(url);ok=true;}catch(e){try{const i=document.createElement('textarea');i.value=url;document.body.append(i);i.select();ok=document.execCommand('copy');i.remove();}catch(x){}}
      tip.textContent=ok?'Link copiado':'Não foi possível copiar';tip.classList.add('on');setTimeout(()=>tip.classList.remove('on'),1800);});
  });
})();
</script>
'''
ARROW = '<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.0641 1.14239L.499 12.7061M1.9673.7061h9.5726c.53 0 .9591.4291.9591.9605v9.5712" stroke="currentColor" stroke-width="1.41181"/></svg>'
def post(t, out):
    t = sub1(t, '--accent:#7C5CFF;', '--accent:#6025E1;')
    shutil.copy(out + '/media/servico-blog.jpg', out + '/img/servico-blog.jpg')
    # compartilhar no início (abaixo do autor) e no fim (antes do CTA)
    t, n = re.subn(r'(    <div class="by rv">.*?\n    </div>\n)', lambda m: m.group(1) + '    ' + share_bar('Compartilhar', 'share-top rv') + '\n', t, count=1, flags=re.S); assert n == 1
    t, n = re.subn(r'      <aside class="end rv">.*?</aside>\n',
        '      ' + share_bar('Gostou? Compartilhe', 'share-end rv') + '\n'
        '      <aside class="end rv">\n'
        '        <div class="l">\n'
        '          <img class="lgw" src="./img/logo-work-digital.svg" alt="Work Digital" width="132" height="41">\n'
        '          <h5>Um blog que trabalha pela sua marca 24 horas por dia</h5>\n'
        '          <button class="wd-work-cta wd-cta" type="button" data-wd-contact><span>Solicitar proposta</span>' + ARROW + '</button>\n'
        '        </div>\n'
        '        <div class="r"><img src="./img/servico-blog.jpg" alt="Monitor de vidro com o mascote da Work e páginas de blog flutuando, em luz roxa e rosa" loading="lazy" decoding="async"></div>\n'
        '      </aside>\n', t, count=1, flags=re.S); assert n == 1
    t = sub1(t, '</style>', CSS + '</style>')
    return t.rstrip() + '\n' + JS
