# Tabela de preços "Contrate um site profissional" na página Soluções (mesmo visual dos painéis da página)
import html as H
PLANOS = [
    {'nome': 'Blog de conteúdo', 'moeda': 'R$', 'preco': '995', 'nota': 'Pagamento único',
     'itens': ['Modelo padrão', 'Customização total de cores do tema', 'Layout responsivo', 'Otimização SEO avançada (Google)',
               'Google friendly', 'Gerenciador de conteúdo', 'Integração com as redes sociais', 'Integração com Google Analytics',
               'Integração com Google Search Console', 'WordPress', 'Conformidade com a LGPD']},
    {'nome': 'Site profissional por assinatura', 'moeda': 'R$', 'preco': '590', 'nota': 'Suporte + hospedagem mensal',
     'itens': ['Até 4 páginas ou OnePage', 'Design padrão, via template', 'Layout responsivo', '2 horas de manutenção mensal',
               'Suporte por 12 meses', 'Otimização SEO básica (Google)', 'Integração com as redes sociais', 'Integração com Google Analytics',
               'Integração com Google Search Console', 'WordPress', 'Conformidade com a LGPD']},
    {'nome': 'Site profissional personalizado', 'moeda': '', 'preco': 'Consulte', 'nota': 'Pagamento único',
     'itens': ['Nº personalizado de páginas', 'Design personalizado', 'Layout responsivo', 'Alta performance',
               'Otimização SEO avançada (Google)', 'Google friendly', 'Formulários estratégicos', 'Gerenciador de conteúdo',
               'Conexão com ferramentas externas', 'Integração com as redes sociais', 'Integração com Google Analytics',
               'Integração com Google Search Console', 'WordPress', 'Conformidade com a LGPD']},
]
CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3.5 8.4l2.9 2.8 6.1-6.4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def section():
    cards = []
    for i, p in enumerate(PLANOS):
        val = (f'<span class="pr-cur">{p["moeda"]}</span>' if p['moeda'] else '') + f'<span class="pr-num{" pr-word" if not p["moeda"] else ""}">{H.escape(p["preco"])}</span>'
        itens = ''.join(f'<li>{CHECK}<span>{H.escape(x)}</span></li>' for x in p['itens'])
        cards.append(f'''<article class="pr-card" aria-labelledby="pr-t{i}">
  <canvas class="pr-dots" aria-hidden="true"></canvas>
  <header class="pr-head"><h3 id="pr-t{i}">{H.escape(p["nome"])}</h3><p class="pr-price">{val}</p><p class="pr-note">{H.escape(p["nota"])}</p></header>
  <ul class="pr-list">{itens}</ul>
  <button class="wd-work-cta wd-cta pr-cta" data-wd-contact type="button"><span>Contratar agora</span><span aria-hidden="true">↗</span></button>
</article>''')
    return f'''<section class="pricing" id="planos" aria-labelledby="pr-title">
 <h2 class="pr-title" id="pr-title">Contrate um site profissional</h2>
 <div class="pr-grid">{''.join(cards)}</div>
</section>
'''

CSS = '''
/* Tabela de preços (Contrate um site profissional) */
.pricing{position:relative;z-index:1;width:min(calc(100% - 2 * var(--wd-layout-gutter,3vw)),1440px);margin:-6vh auto 18vh;font-family:var(--body)}
.pr-title{margin:0 0 clamp(36px,5vw,64px);text-align:center;font:500 clamp(36px,4.34vw,64px)/1.05 var(--display);letter-spacing:-.041em;text-wrap:balance;background:linear-gradient(90deg,#cbb6ff 0%,#efe7ff 26%,#fffdfa 48%,#f5c3d8 89%);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent;padding-bottom:.08em}
.pr-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;align-items:stretch}
.pr-card{position:relative;isolation:isolate;overflow:hidden;min-width:0;display:flex;flex-direction:column;gap:28px;padding:clamp(28px,2.6vw,40px);border-radius:var(--wd-panel-radius,32px);background:linear-gradient(125deg,rgba(96,37,225,.12),rgba(49,22,78,.2)),rgba(18,19,22,.66);border:1px solid rgba(189,164,255,.13);backdrop-filter:blur(22px) saturate(140%);-webkit-backdrop-filter:blur(22px) saturate(140%);transition:box-shadow .7s cubic-bezier(.4,0,.2,1),transform .7s cubic-bezier(.22,1,.36,1)}
.pr-card::before{content:"";position:absolute;inset:0;border-radius:inherit;z-index:-1;background:linear-gradient(135deg,rgba(124,92,255,.38) 0%,rgba(183,155,255,.22) 45%,rgba(255,143,203,.20) 100%);box-shadow:inset 0 0 0 1px rgba(214,198,255,.35);opacity:0;transition:opacity .7s cubic-bezier(.4,0,.2,1);pointer-events:none}
.pr-card:hover::before,.pr-card:focus-within::before{opacity:1}
.pr-card:hover{box-shadow:0 20px 60px -20px rgba(124,92,255,.55);transform:translateY(-4px)}
.pr-dots{position:absolute;inset:0;width:100%;height:100%;z-index:-1;pointer-events:none;border-radius:inherit}
.pr-head{display:grid;gap:10px;text-align:center;padding-bottom:26px;border-bottom:1px solid rgba(189,164,255,.16)}
.pr-head h3{margin:0;font:500 clamp(22px,1.75vw,28px)/1.15 var(--display);letter-spacing:-.02em;color:#04CD8F;text-wrap:balance;min-height:2.3em;display:flex;align-items:center;justify-content:center}
.pr-price{margin:6px 0 0;display:flex;justify-content:center;align-items:center;min-height:clamp(60px,5.4vw,86px);gap:6px;color:#fff;font-family:var(--display);font-variant-numeric:tabular-nums}
.pr-cur{align-self:flex-start;font-size:clamp(16px,1.25vw,20px);font-weight:500;margin-top:.55em;color:#EDE4FF}
.pr-num{font-size:clamp(56px,5vw,80px);font-weight:400;line-height:1;letter-spacing:-.04em;background:linear-gradient(90deg,#FFFFFF 0%,#EDE4FF 45%,#F7C9EC 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.pr-num.pr-word{font-size:clamp(44px,3.9vw,64px)}
.pr-note{margin:0;font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:#bdb3d6}
.pr-list{list-style:none;margin:0;padding:0;display:grid;gap:0;flex:1 1 auto;align-content:start}
.pr-list li{display:flex;align-items:flex-start;gap:12px;padding:12px 0;border-bottom:1px solid rgba(189,164,255,.1);font-size:16px;line-height:1.45;color:#d9d3e6}
.pr-list li:last-child{border-bottom:0}
.pr-list svg{flex:0 0 20px;width:20px;height:20px;margin-top:1px;padding:3px;border-radius:50%;color:#fff;background:linear-gradient(135deg,#6025E1,#C00252)}
.pr-cta{align-self:center;border-radius:9999px;cursor:pointer;font-family:var(--display)}
.pricing .wd-work-cta{display:inline-flex;align-items:center;justify-content:center;gap:16px;width:max-content;max-width:100%;min-height:54px;padding:14px 26px;border:0;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;text-transform:uppercase;letter-spacing:.1em;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0%;transition:background-position .6s ease,color .2s ease}
.pricing .wd-work-cta:hover,.pricing .wd-work-cta:focus-visible{background-position:0% 0%;color:#24123e}
.pricing .wd-work-cta:focus-visible{outline:2px solid #EDE4FF;outline-offset:3px}
@media(max-width:1100px){.pr-grid{grid-template-columns:minmax(0,1fr);max-width:620px;margin:0 auto}.pr-head h3{min-height:0}.pricing{margin-top:0}}
@media(max-width:600px){.pr-card{padding:26px 20px;gap:22px}.pr-list li{font-size:15px;padding:11px 0}}
@media(prefers-reduced-motion:reduce){.pr-card,.pr-card::before{transition:none}.pr-card:hover{transform:none}}
html.wd-lite .pr-card{background:linear-gradient(125deg,rgba(96,37,225,.16),rgba(49,22,78,.26)),rgba(20,20,26,.94)}
'''

# campo de pontos que reage ao mouse (o mesmo dos painéis de serviços)
JS = '''<script>
document.querySelectorAll('.pr-card').forEach(panel=>{
 const canvas=panel.querySelector('.pr-dots'),ctx=canvas.getContext('2d');
 let width=0,height=0,frame=0,active=false,x=-200,y=-200,strength=0;
 function draw(){frame=0;strength+=(Number(active)-strength)*.12;ctx.clearRect(0,0,width,height);ctx.fillStyle='#bda4ff';
  for(let py=12;py<height;py+=22)for(let px=12;px<width;px+=22){const dx=px-x,dy=py-y,distance=Math.hypot(dx,dy);
   const influence=Math.exp(-distance*distance/(90*90))*strength,shift=influence*10/(distance||1);
   ctx.globalAlpha=.07+influence*.35;ctx.beginPath();ctx.arc(px+dx*shift,py+dy*shift,.8+influence*.7,0,Math.PI*2);ctx.fill();}
  ctx.globalAlpha=1;if(active||strength>.002)frame=requestAnimationFrame(draw);}
 function request(){if(!frame)frame=requestAnimationFrame(draw)}
 function resize(){const r=panel.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);request()}
 panel.addEventListener('pointermove',e=>{if(e.pointerType==='touch')return;const r=panel.getBoundingClientRect();x=e.clientX-r.left;y=e.clientY-r.top;active=true;request()},{passive:true});
 panel.addEventListener('pointerleave',()=>{active=false;request()},{passive:true});
 new ResizeObserver(resize).observe(panel);resize();
});
</script>
'''

def apply(t):
    a = '<section class="board" aria-label="Serviços"><div class="stage" id="stage"></div></section>'
    assert t.count(a) == 1
    t = t.replace(a, a + '\n' + section(), 1)
    # o fundo (bola de fluido + SOLUÇÕES + WORK) some quando a tabela de preços chega, como já fazia no rodapé
    f = "function fade(){const ft=document.querySelector('wd-footer');"
    assert t.count(f) == 1
    t = t.replace(f, "function fade(){const ft=document.getElementById('planos')||document.querySelector('wd-footer');", 1)
    t = t.replace('</style>', CSS + '</style>', 1)
    t = t.replace('</body>', JS + '</body>', 1) if '</body>' in t else t + JS
    return t
