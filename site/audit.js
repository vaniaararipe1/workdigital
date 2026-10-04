const { chromium } = require('playwright');const fs=require('fs'),path=require('path');
const types={'.html':'text/html; charset=utf-8','.js':'text/javascript','.css':'text/css','.png':'image/png','.svg':'image/svg+xml','.jpg':'image/jpeg','.webp':'image/webp','.webm':'video/webm'};
const PAGES=(process.env.PAGES||'home.html,solucoes.html,cases.html,case-interna.html,blog.html,post.html').split(',');
const W=(process.env.WIDTHS||'320,360,375,390,414,480,600,700,768,820,900,980,1024,1100,1199,1242,1280,1366,1440,1600,1920,2560').split(',').map(Number);
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',proxy:{server:process.env.HTTPS_PROXY}});
const out={};
for(const pg of PAGES){for(const w of W){const h=w<700?800:w<1100?900:w<=1280?700:900;
const ctx=await b.newContext({viewport:{width:w,height:h},isMobile:w<768,hasTouch:w<768});
await ctx.route(/^https:/,async r=>{const u=new URL(r.request().url());if(u.host==='site.test'){const f=path.join('site-build',decodeURIComponent(u.pathname.split('?')[0]));if(!fs.existsSync(f))return r.fulfill({status:404,body:'nf'});return r.fulfill({status:200,body:fs.readFileSync(f),contentType:types[path.extname(f)]||'application/octet-stream'});}if(/fonts\.(googleapis|gstatic)/.test(u.host)){try{const resp=await r.fetch({timeout:30000});return r.fulfill({response:resp});}catch(e){}}r.abort();});
const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message.slice(0,100)));
await p.goto('https://site.test/'+pg+'?lite=1',{waitUntil:'load',timeout:60000});await p.waitForTimeout(1200);
// rola a página toda para disparar animações de entrada
await p.evaluate(async()=>{for(let y=0;y<document.documentElement.scrollHeight;y+=innerHeight*.8){scrollTo(0,y);await new Promise(r=>setTimeout(r,120));}scrollTo(0,0);await new Promise(r=>setTimeout(r,400));});
const res=await p.evaluate(()=>{const vw=document.documentElement.clientWidth;const issues=[];
 const hscroll=document.documentElement.scrollWidth>vw+1||document.body.scrollWidth>vw+1;
 const clipped=e=>{for(let a=e.parentElement;a&&a!==document.body;a=a.parentElement){const s=getComputedStyle(a);if(/(hidden|clip|auto|scroll)/.test(s.overflowX+s.overflow)){const r=a.getBoundingClientRect();if(r.right<=vw+2&&r.left>=-2)return true;}if(s.position==='fixed')return true;}return false;};
 const name=e=>e.tagName.toLowerCase()+(e.id?'#'+e.id:'')+(typeof e.className==='string'&&e.className?'.'+e.className.trim().split(/\s+/).slice(0,2).join('.'):'');
 for(const e of document.body.querySelectorAll('*')){const s=getComputedStyle(e);if(s.display==='none'||s.visibility==='hidden'||+s.opacity===0)continue;const r=e.getBoundingClientRect();if(!r.width||!r.height)continue;
  if((r.right>vw+2||r.left<-2)&&!clipped(e)&&s.position!=='fixed'){issues.push('OVERFLOW '+name(e)+' ['+Math.round(r.left)+'..'+Math.round(r.right)+']');}
  // texto cortado dentro de caixa com overflow escondido
  if(/(hidden|clip)/.test(s.overflowX)&&e.clientWidth>2&&e.children.length===0&&e.textContent.trim().length>2&&e.scrollWidth>e.clientWidth+2)issues.push('TEXT-CUT '+name(e)+' "'+e.textContent.trim().slice(0,30)+'"');
 }
 // menu: itens visíveis que se sobrepõem
 const nav=[...document.querySelectorAll('.site-nav > *, .nav-links > *, .wd-nav-actions > *')].filter(e=>{const s=getComputedStyle(e);const r=e.getBoundingClientRect();return s.display!=='none'&&s.visibility!=='hidden'&&r.width>0});
 for(let i=0;i<nav.length;i++)for(let j=i+1;j<nav.length;j++){if(nav[i].contains(nav[j])||nav[j].contains(nav[i]))continue;const a=nav[i].getBoundingClientRect(),c=nav[j].getBoundingClientRect();if(a.left<c.right-2&&c.left<a.right-2&&a.top<c.bottom-2&&c.top<a.bottom-2)issues.push('NAV-OVERLAP '+name(nav[i])+' x '+name(nav[j]));}
 return {hscroll,sw:document.documentElement.scrollWidth,vw,issues:[...new Set(issues)].slice(0,12)};});
const key=pg+' '+w;if(res.hscroll||res.issues.length||errs.length){console.log(key,res.hscroll?'HSCROLL sw='+res.sw+' vw='+res.vw:'',res.issues.join(' | '),errs.join(';'));}
if([320,390,768,1024,1242,1440,1920].includes(w)&&process.env.SHOTS)await p.screenshot({path:`aud/${pg.split('.')[0]}-${w}.png`,fullPage:true});
await ctx.close();}console.log('done',pg);}
await b.close();})();
