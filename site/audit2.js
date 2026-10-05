const { chromium } = require('playwright');const fs=require('fs'),path=require('path');
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.svg':'image/svg+xml','.webp':'image/webp','.jpg':'image/jpeg','.png':'image/png','.webm':'video/webm','.mp4':'video/mp4'};
const AXE=fs.readFileSync('node_modules/axe-core/axe.min.js','utf8');
const pages=[['home','home.html'],['solucoes','solucoes.html'],['cases','cases.html'],['case','case-interna.html#genera'],['blog','blog.html'],['post','post.html#lgpd-no-site']];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const out={};
for(const [name,url] of pages){const ctx=await b.newContext({viewport:{width:1366,height:900}});
await ctx.route(/^https:/,async r=>{const u=new URL(r.request().url());if(u.host==='site.test'){const f=path.join('site-build',decodeURIComponent(u.pathname));return fs.existsSync(f)?r.fulfill({status:200,body:fs.readFileSync(f),contentType:types[path.extname(f)]}):r.fulfill({status:404,body:''});}r.abort();});
const p=await ctx.newPage();await p.goto('https://site.test/'+url.replace('#','?lite=1#').replace(/^([^?#]+)$/,'$1?lite=1'));await p.waitForTimeout(2500);
const seo=await p.evaluate(()=>{const q=s=>document.querySelector(s);const imgs=[...document.images];
 return {lang:document.documentElement.lang,title:document.title,desc:q('meta[name=description]')?.content||null,canonical:q('link[rel=canonical]')?.href||null,robots:q('meta[name=robots]')?.content||null,og:[...document.querySelectorAll('meta[property^="og:"]')].map(m=>m.getAttribute('property')),twitter:!!q('meta[name^="twitter:"]'),jsonld:[...document.querySelectorAll('script[type="application/ld+json"]')].length,
 h1:[...document.querySelectorAll('h1')].map(h=>h.textContent.trim().slice(0,60)),headings:[...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h=>h.tagName).join(''),
 imgs:imgs.length,noAlt:imgs.filter(i=>!i.hasAttribute('alt')).length,emptyAlt:imgs.filter(i=>i.getAttribute('alt')==='').length,noDims:imgs.filter(i=>!i.getAttribute('width')).length,
 bigImgs:imgs.filter(i=>i.naturalWidth>2*i.getBoundingClientRect().width&&i.getBoundingClientRect().width>0).length,
 links:document.links.length,hashLinks:[...document.links].filter(a=>a.getAttribute('href')==='#').length,
 videos:[...document.querySelectorAll('video')].length,videosNoLabel:[...document.querySelectorAll('video')].filter(v=>!v.getAttribute('aria-label')&&!v.getAttribute('aria-hidden')&&!v.closest('[aria-hidden=true]')).length,
 skip:!!q('a[href^="#"][class*=skip],a.skip-link,.skip'),main:!!q('main'),words:document.body.innerText.split(/\s+/).length}});
await p.addScriptTag({content:AXE});
const ax=await p.evaluate(async()=>{const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']}});return r.violations.map(v=>({id:v.id,impact:v.impact,n:v.nodes.length,help:v.help,ex:v.nodes.slice(0,2).map(n=>n.target.join(' ')+' :: '+(n.failureSummary||'').split('\n').slice(1,2).join(' ').slice(0,110))}))});
const size=fs.statSync(path.join('site-build',url.split('#')[0])).size;
out[name]={size,seo,ax};await ctx.close();}
fs.writeFileSync('audit2.json',JSON.stringify(out,null,1));await b.close();})();
