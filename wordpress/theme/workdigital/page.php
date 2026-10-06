<?php if (!defined('ABSPATH')) exit; ?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="<?php echo WD_URI; ?>/img/inline/1b99465de9a2.svg">
<script>/* wd-lite */(function(){var lite=false;try{if(/[?&]lite=1/.test(location.search))lite=true;if(!/[?&]lite=0/.test(location.search)){var cv=document.createElement("canvas"),g=cv.getContext("webgl");var e=g&&g.getExtension("WEBGL_debug_renderer_info"),r=e?String(g.getParameter(e.UNMASKED_RENDERER_WEBGL)):"";if(!g||/SwiftShader|llvmpipe|softpipe|Basic Render|Intel\(R\) (HD Graphics( [2-5]\d{3})?|Q?G\d+)\b|GMA/i.test(r))lite=true;var lc=g&&g.getExtension("WEBGL_lose_context");lc&&lc.loseContext();if((navigator.hardwareConcurrency||8)<=2)lite=true;}}catch(x){}if(lite)document.documentElement.classList.add("wd-lite");window.WD_LITE=lite;})();(function(){try{if(!location.hash){history.scrollRestoration="manual";var top=function(){scrollTo(0,0)};top();addEventListener("DOMContentLoaded",top,{once:true});addEventListener("load",function(){requestAnimationFrame(top)},{once:true});}}catch(e){}document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(".site-nav a[href='#'],.site-nav a[href='#topo'],.site-nav a[href='#top'],.site-nav a[href='#hero']");if(!a)return;e.preventDefault();scrollTo({top:0,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});try{history.replaceState(null,"",location.pathname+location.search)}catch(x){}});})();</script>
<style id="wd-a11y">
/* Acessibilidade: pular para o conteúdo, foco visível, texto só para leitores de tela, pausa das animações */
.wd-sr{position:absolute!important;width:1px!important;height:1px!important;padding:0!important;margin:-1px!important;overflow:hidden!important;clip:rect(0,0,0,0)!important;white-space:nowrap!important;border:0!important}
.wd-skip{position:fixed;left:16px;top:-80px;z-index:100000;padding:12px 18px;border-radius:12px;background:#F7F6FB;color:#24123e;font:600 15px/1.2 "Space Grotesk",Arial,sans-serif;text-decoration:none;box-shadow:0 10px 30px -10px rgba(0,0,0,.5);transition:top .2s}
.wd-skip:focus{top:16px;outline:3px solid #6025E1;outline-offset:2px}
:where(a,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--wd-focus,#6025E1)!important;outline-offset:3px!important}
.wd-pause{position:fixed;left:16px;bottom:16px;z-index:9990;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 12px;border-radius:999px;border:1px solid rgba(189,164,255,.35);background:rgba(18,19,22,.78);color:#F7F6FB;font:500 12px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);opacity:.82;transition:opacity .2s,background .2s}
.wd-pause:hover,.wd-pause:focus-visible{opacity:1;background:rgba(96,37,225,.85)}
.wd-pause svg{width:14px;height:14px;flex:none}
.wd-pause .on{display:none}html.wd-paused .wd-pause .on{display:inline}html.wd-paused .wd-pause .off{display:none}
@media(max-width:700px){.wd-pause{width:40px;padding:0;justify-content:center}.wd-pause .t{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}}
html.wd-paused *,html.wd-paused *::before,html.wd-paused *::after{animation-play-state:paused!important}
html.wd-paused .particle-art canvas,html.wd-paused .native-particles canvas,html.wd-paused #fluid,html.wd-paused #cfluid{visibility:hidden!important}
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Nunito:wght@300;400;600;700&display=swap">
<style>
/* Layout: Intercom-blog structure — floating pill header, giant centered title, category row, featured post (text left / image right), editorial row list with right thumbnails, pagination, footer. Light cream look by client request. */
:root{
  --bg:#F4F3EC; --ink:#17131F; --muted:#6B6578; --line:rgba(23,19,31,.13);
  --accent:#6025E1; --lilac:#C4A8FF; --pink:#FF8FCB; --pill:#ffffff;
  --display:"Space Grotesk","Helvetica Neue",Arial,sans-serif;
  --body:"Nunito",system-ui,sans-serif;
  --pad:clamp(16px,4vw,64px);
  --ease:cubic-bezier(.22,1,.36,1);
  color-scheme:light;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);overflow-x:hidden}
a{color:inherit;text-decoration:none}
button,input{font:inherit;color:inherit}
button{border:0;background:none;cursor:pointer;padding:0}
img{display:block;max-width:100%}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:6px}
.wrap{max-width:1312px;margin:0 auto;padding:0 var(--pad)}
.grad{background:linear-gradient(90deg,#7C5CFF 0%,#B98CFF 50%,#FF8FCB 100%);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:transparent}

/* Header: two floating pills */
.hd{position:fixed;top:16px;left:0;right:0;z-index:40;display:flex;justify-content:space-between;align-items:flex-start;padding:0 var(--pad);pointer-events:none;transition:transform .5s var(--ease)}
.hd.hide{transform:translateY(-120%)}
.pill{pointer-events:auto;display:flex;align-items:center;gap:6px;background:var(--pill);border-radius:16px;padding:8px;box-shadow:0 1px 0 rgba(23,19,31,.04),0 10px 30px -18px rgba(23,19,31,.25)}
.logo{display:flex;align-items:center;gap:10px;padding:4px 14px 4px 6px;font:700 15px/1 var(--display);letter-spacing:.02em;text-transform:uppercase}
.logo i{width:28px;height:28px;border-radius:9px;background:linear-gradient(135deg,#7C5CFF,#C4A8FF 55%,#FF8FCB);display:grid;place-items:center;font:700 14px/1 var(--display);color:#fff;font-style:normal}
.nv{display:flex;align-items:center;gap:2px}
.nv a,.nv button{display:flex;align-items:center;gap:6px;height:40px;padding:0 14px;border-radius:10px;font:500 15px/1 var(--display);transition:background .25s}
.nv a:hover,.nv button:hover{background:#F1EEF7}
.nv a.cur{text-decoration:underline;text-decoration-thickness:1.5px;text-underline-offset:5px}
.nv svg{width:10px;height:10px;transition:transform .3s var(--ease)}
.dd{position:relative}
.dd .menu{position:absolute;top:calc(100% + 10px);left:0;min-width:220px;background:#fff;border-radius:14px;padding:8px;box-shadow:0 20px 50px -20px rgba(23,19,31,.35);opacity:0;visibility:hidden;transform:translateY(-6px);transition:all .3s var(--ease)}
.dd .menu a{height:auto;padding:12px 14px;font:500 14px/1.2 var(--display);border-radius:10px}
.dd.open .menu{opacity:1;visibility:visible;transform:none}
.dd.open > button svg{transform:rotate(180deg)}
.srch{display:flex;align-items:center;height:40px;border-radius:10px;overflow:hidden;transition:background .25s}
.srch button{width:40px;height:40px;display:grid;place-items:center;border-radius:10px}
.srch button:hover{background:#F1EEF7}
.srch svg{width:18px;height:18px}
.srch input{width:0;border:0;outline:0;background:transparent;font:500 15px var(--display);padding:0;transition:width .45s var(--ease),padding .45s var(--ease)}
.srch.on{background:#F1EEF7}
.srch.on input{width:200px;padding-right:12px}
.cta{position:relative;overflow:hidden;display:flex;align-items:center;gap:10px;height:40px;padding:0 18px;border-radius:10px;background:var(--ink);color:#fff;font:600 13px/1 var(--display);letter-spacing:.06em;text-transform:uppercase;isolation:isolate}
.cta::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,#7C5CFF,#FF8FCB);transform:translateY(101%);transition:transform .45s var(--ease)}
.cta:hover::before{transform:none}
.cta.out::before{transform:translateY(-101%)}
.burger{display:none;width:40px;height:40px;border-radius:10px;place-items:center}
.burger span,.burger span::before{display:block;width:18px;height:1.5px;background:var(--ink);position:relative}
.burger span::before{content:"";position:absolute;top:6px}
.burger span{top:-3px}

/* Hero */
.hero{padding-top:clamp(120px,15vw,190px);text-align:center}
.hero .up{font:600 13px/1 var(--display);letter-spacing:.16em;text-transform:uppercase;margin:0 auto 22px}
.hero h1{margin:0;font:600 clamp(44px,8vw,120px)/.94 var(--display);letter-spacing:-.05em}
.hero p{max-width:560px;margin:28px auto 0;font-size:18px;line-height:1.55;color:var(--muted)}
.cats{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 6px;margin:48px 0 0;padding:0;list-style:none}
.cats button{white-space:nowrap;height:40px;padding:0 16px;border-radius:999px;font:500 16px/1 var(--display);color:var(--ink);transition:background .25s,color .25s}
.cats button:hover{background:rgba(124,92,255,.08)}
.cats button[aria-pressed="true"]{background:var(--ink);color:#fff}
.rule{height:1px;background:var(--line);margin-top:40px}

/* Featured */
.feat{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:clamp(28px,4vw,64px);align-items:center;padding:clamp(40px,5vw,72px) 0}
.meta{display:flex;align-items:center;flex-wrap:wrap;gap:8px 14px;font:500 14px/1 var(--display);color:var(--muted)}
.meta .tag{color:var(--accent);font-weight:600}
.meta .dot{width:3px;height:3px;border-radius:50%;background:currentColor;opacity:.6}
.meta svg{width:14px;height:14px;margin-right:5px;vertical-align:-2px}
.feat .badge{display:inline-flex;align-items:center;gap:8px;margin-bottom:22px;font:600 12px/1 var(--display);letter-spacing:.14em;text-transform:uppercase}
.feat .badge::before{content:"";width:8px;height:8px;border-radius:50%;background:linear-gradient(135deg,#7C5CFF,#FF8FCB)}
.feat h2{margin:18px 0 0;font:600 clamp(32px,3.6vw,52px)/1.04 var(--display);letter-spacing:-.035em}
.feat h2 a{background:linear-gradient(currentColor,currentColor) 0 100%/0 2px no-repeat;transition:background-size .5s var(--ease)}
.feat h2 a{background-image:none!important;text-decoration:none!important;transition:color .3s}
.feat:hover h2 a,.feat h2 a:focus-visible{color:var(--accent)}
.feat p{margin:22px 0 0;font-size:18px;line-height:1.6;color:var(--muted);max-width:480px}
.more{display:inline-flex;align-items:center;gap:10px;margin-top:30px;font:600 15px/1 var(--display)}
.more svg{width:16px;height:16px;transition:transform .4s var(--ease)}
.more:hover svg,.feat:hover .more svg{transform:translateX(5px)}
.feat .img{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:16/10;background:#E6E1F3}
.feat .img img{width:100%;height:100%;object-fit:cover;transition:transform 1s var(--ease)}
.feat:hover .img img{transform:scale(1.03)}

/* Rows */
.list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.row{border-bottom:1px solid var(--line)}
.row a{display:grid;grid-template-columns:minmax(0,1fr) 220px;gap:40px;align-items:center;padding:36px 0;position:relative}
.row h3{margin:16px 0 0;max-width:860px;font:600 clamp(24px,2.5vw,36px)/1.12 var(--display);letter-spacing:-.03em;transition:color .35s}
.row a:hover h3{color:var(--accent)}
.row .th{width:220px;aspect-ratio:16/10;border-radius:12px;overflow:hidden;background:#E6E1F3}
.row .th img{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.row a:hover .th img{transform:scale(1.06)}
.row[hidden],.feat[hidden]{display:none}
.empty{padding:64px 0;text-align:center;font:500 20px var(--display);color:var(--muted)}

/* Pagination */
.pag{display:flex;justify-content:center;align-items:center;gap:6px;padding:56px 0 24px}
.pag a,.pag span{min-width:44px;height:44px;padding:0 6px;display:grid;place-items:center;border-radius:12px;font:500 16px/1 var(--display);transition:background .25s}
.pag a:hover{background:#fff}
.pag a[aria-current]{background:var(--ink);color:#fff}
.pag svg{width:16px;height:16px}
.pag .off{opacity:.3;pointer-events:none}

/* Footer */
.ft{margin-top:clamp(64px,8vw,120px);padding:clamp(56px,7vw,96px) 0 32px;border-top:1px solid var(--line)}
.ft-top{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:48px;align-items:end}
.ft h2{margin:0;font:600 clamp(40px,6vw,88px)/.95 var(--display);letter-spacing:-.045em}
.ft .side{display:flex;flex-direction:column;align-items:flex-start;gap:24px}
.ft .side p{margin:0;font-size:17px;line-height:1.6;color:var(--muted);max-width:380px}
.cta.lg{height:52px;padding:0 24px;border-radius:14px;font-size:14px}
.cta .arr{width:14px;height:14px}
.ft-mid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin-top:clamp(56px,7vw,96px);padding-top:40px;border-top:1px solid var(--line)}
.ft-mid h4{margin:0 0 16px;font:600 12px/1 var(--display);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
.ft-mid ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.ft-mid a{font:500 16px/1.3 var(--display);transition:color .25s}
.ft-mid a:hover{color:var(--accent)}
.soc{display:flex;gap:10px}
.soc a{width:44px;height:44px;border-radius:12px;background:#fff;display:grid;place-items:center;transition:background .25s,color .25s}
.soc a:hover{background:var(--ink);color:#fff}
.soc svg{width:18px;height:18px;fill:currentColor}
.ft-big{margin:clamp(48px,6vw,80px) 0 0;font:700 clamp(54px,14.6vw,212px)/.8 var(--display);letter-spacing:-.06em;text-align:center;white-space:nowrap;user-select:none}
.ft-bot{display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-top:32px;font-size:14px;color:var(--muted)}

/* WhatsApp float */
.wa{position:fixed;right:20px;bottom:calc(20px + env(safe-area-inset-bottom,0px));z-index:30;width:56px;height:56px;border-radius:50%;background:#25D366;display:grid;place-items:center;box-shadow:0 10px 30px -8px rgba(37,211,102,.6);transition:transform .3s var(--ease)}
.wa:hover{transform:scale(1.06)}
.wa svg{width:28px;height:28px;fill:#fff}

/* Reveal */
.rv{opacity:0;transform:translateY(24px);transition:opacity .9s var(--ease),transform .9s var(--ease)}
.rv.in{opacity:1;transform:none}

/* Cursor */
.wd-cursor{position:fixed;left:0;top:0;z-index:2147483000;pointer-events:none;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#F2EEF8;box-shadow:0 0 0 1px rgba(18,19,22,.35);
  transition:width .4s cubic-bezier(.22,1,.36,1),height .4s cubic-bezier(.22,1,.36,1),margin .4s cubic-bezier(.22,1,.36,1),background .3s;display:grid;place-items:center}
.wd-cursor b{font:500 11px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#fff;opacity:0;transition:opacity .2s;white-space:nowrap}
.wd-cursor.link{width:40px;height:40px;margin:-20px 0 0 -20px}
.wd-cursor.big{width:96px;height:96px;margin:-48px 0 0 -48px;background:#7C5CFF;mix-blend-mode:normal}
.wd-cursor.big b{opacity:1}
@media not all and (pointer: coarse){.has-wd-cursor,.has-wd-cursor a,.has-wd-cursor button,.has-wd-cursor input{cursor:none}}

/* Mobile drawer */
.drawer{position:fixed;inset:0;z-index:50;background:var(--bg);padding:96px var(--pad) 32px;display:flex;flex-direction:column;gap:8px;opacity:0;visibility:hidden;transition:opacity .35s var(--ease),visibility .35s}
.drawer.open{opacity:1;visibility:visible}
.drawer a{font:600 36px/1.2 var(--display);letter-spacing:-.03em;padding:6px 0;border-bottom:1px solid var(--line)}
.drawer .x{position:absolute;top:24px;right:var(--pad);width:44px;height:44px;border-radius:12px;background:#fff;font-size:22px}
.drawer input{margin-top:16px;height:52px;border-radius:14px;border:1px solid var(--line);background:#fff;padding:0 16px;font:500 16px var(--display)}

@media (max-width:1060px){
  .nv .hide-md{display:none}
}
@media (max-width:860px){
  .hd{top:12px}
  .nv,.srch{display:none}
  .burger{display:grid}
  .cta.sm{height:40px;padding:0 14px;font-size:12px}
  .feat{grid-template-columns:1fr}
  .feat .img{order:-1}
  .row a{grid-template-columns:minmax(0,1fr) 112px;gap:18px;padding:26px 0}
  .row .th{width:112px;aspect-ratio:1}
  .row h3{margin-top:10px;font-size:20px}
  .row .meta>:nth-last-child(-n+2){display:none}
  .ft-top{grid-template-columns:1fr}
  .ft-mid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .cats{flex-wrap:nowrap;justify-content:flex-start;overflow-x:auto;margin-left:calc(var(--pad)*-1);margin-right:calc(var(--pad)*-1);padding:0 var(--pad);scrollbar-width:none}
  .cats::-webkit-scrollbar{display:none}
  .cats button{flex:none;font-size:15px}
}
@media (max-width:420px){
  .logo span{display:none}
  .meta{font-size:13px}
  .pag .hide-sm{display:none}
@media(max-width:420px){.pag{gap:2px;flex-wrap:wrap}.pag a,.pag span{min-width:38px;height:40px;padding:0 4px}}
}
@media (prefers-reduced-motion:reduce){
  *{transition:none!important}
  .rv{opacity:1;transform:none}
}
.pag button{min-width:44px;height:44px;padding:0 6px;display:grid;place-items:center;border:0;border-radius:12px;background:transparent;color:inherit;font:500 16px/1 var(--display);cursor:pointer;transition:background .25s}.pag button:hover{background:#fff}.pag button[aria-current]{background:var(--ink);color:#fff}.pag button.off{opacity:.3;cursor:default}body{margin:0}
:root{--purple:#6025E1;--green:#04CD8F;--wine:#C00252}
/* MENU (copiado da home) */
/* HEADER */
.site-header{position:fixed;top:18px;left:0;right:0;z-index:90;padding:0 clamp(18px,3.2vw,48px);pointer-events:none}
.site-nav{pointer-events:auto;max-width:1240px;margin:0 auto;height:72px;display:flex;align-items:center;gap:34px;padding:0 14px 0 20px;border:1px solid rgba(255,255,255,.10);border-radius:20px;background:rgba(18,19,22,.58);backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%);box-shadow:0 18px 55px rgba(0,0,0,.18)}
.brand{display:flex;align-items:center;flex:0 0 auto;margin-right:auto}
.brand img{display:block;width:142px;height:auto}
.nav-links{display:flex;align-items:center;gap:32px}
.nav-item,.nav-link{position:relative;display:flex;align-items:center;height:72px;color:#f7f6fb;text-decoration:none;font-size:12px;font-weight:650;letter-spacing:.075em;text-transform:uppercase;white-space:nowrap}
.nav-link:after,.nav-trigger:after{content:"";position:absolute;left:0;right:100%;bottom:19px;height:1px;background:var(--green);transition:right .32s cubic-bezier(.22,1,.36,1)}
.nav-link:hover:after,.nav-item:hover .nav-trigger:after{right:0}
.nav-trigger{appearance:none;border:0;background:none;color:#f7f6fb;font-size:12px;text-transform:uppercase;height:72px;padding:0;cursor:pointer;display:flex;align-items:center;gap:8px;position:relative}
.nav-trigger svg{width:11px;height:11px;transition:transform .3s ease}
.nav-item:hover .nav-trigger svg,.nav-item:focus-within .nav-trigger svg{transform:rotate(180deg)}
.dropdown{position:absolute;top:62px;left:50%;width:min(390px,88vw);padding:12px;border:1px solid rgba(255,255,255,.13);border-radius:18px;background:rgba(26,24,32,.48);backdrop-filter:blur(28px) saturate(170%);-webkit-backdrop-filter:blur(28px) saturate(170%);box-shadow:0 24px 70px rgba(0,0,0,.34);opacity:0;visibility:hidden;transform:translate(-50%,12px) scale(.985);transform-origin:50% 0;transition:opacity .24s ease,transform .34s cubic-bezier(.22,1,.36,1),visibility .24s}
.nav-item:hover .dropdown,.nav-item:focus-within .dropdown{opacity:1;visibility:visible;transform:translate(-50%,0) scale(1)}
.dropdown a{display:grid;grid-template-columns:38px 1fr auto;align-items:center;gap:12px;min-height:66px;padding:12px 14px;border-radius:12px;color:#f7f6fb;text-decoration:none;transition:background .22s ease,transform .22s ease}
.dropdown a:hover{background:rgba(255,255,255,.075);transform:translateX(2px)}
.drop-index{font-size:11px;color:var(--green);letter-spacing:.08em}
.drop-copy strong{display:block;font-size:14px;font-weight:600;letter-spacing:-.01em;text-transform:none}
.drop-copy small{display:block;margin-top:3px;color:#a9b0b0;font-size:12px;font-weight:400;letter-spacing:0;text-transform:none}
.drop-arrow{font-size:18px;color:#8c9594;transition:transform .22s ease,color .22s ease}
.dropdown a:hover .drop-arrow{transform:translateX(3px);color:var(--green)}
.lang{display:flex;align-items:center;gap:6px;color:#9da5a4;font-size:11px;letter-spacing:.08em;text-transform:uppercase;white-space:nowrap}
.lang strong{color:#fff;font-weight:650}
.nav-cta{height:46px;display:inline-flex;align-items:center;justify-content:center;gap:10px;padding:0 20px;border-radius:6px;background:linear-gradient(90deg,#CBFFFC 0%,#EDFFFE 26.25%,#FFFDFA 47.57%,#FAD1FF 88.96%);background-size:180% 100%;background-position:0% 50%;color:#222;text-decoration:none;font-size:14px;line-height:1;text-transform:uppercase;white-space:nowrap;border:0;transition:background-position .55s cubic-bezier(.22,1,.36,1),color .3s ease}
.nav-cta span{transition:transform .35s ease}
.nav-cta:hover{background-position:100% 50%;color:#111}
.nav-cta:hover span{transform:translate(3px,-3px)}
.mobile-toggle{display:none;width:44px;height:44px;border-radius:12px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.05);color:#fff;align-items:center;justify-content:center}
.mobile-toggle i,.mobile-toggle i:before,.mobile-toggle i:after{display:block;width:18px;height:1px;background:#fff;position:relative;content:""}
.mobile-toggle i:before{position:absolute;top:-6px}.mobile-toggle i:after{position:absolute;top:6px}


@media(max-width:980px){
  .nav-links,.lang,.nav-cta{display:none}
  .site-nav{height:64px;border-radius:17px;padding-right:10px}
  .brand img{width:132px}
  .mobile-toggle{display:flex}
}
.site-nav{position:relative;isolation:isolate;background:transparent;backdrop-filter:none;-webkit-backdrop-filter:none}
.site-nav::before{content:"";position:absolute;inset:0;border-radius:inherit;background:rgba(18,19,22,.58);backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%);z-index:-1;pointer-events:none}
.dropdown{background:rgba(28,22,42,.28);backdrop-filter:blur(36px) saturate(145%);-webkit-backdrop-filter:blur(36px) saturate(145%);border:1px solid rgba(255,255,255,.14);box-shadow:0 22px 60px rgba(0,0,0,.20)}
.dropdown a{display:flex;gap:0;padding:16px 18px;min-height:68px}
/* Rodapé da home numa faixa escura, com a mesma luz da home (páginas claras) */
.wd-dark-band{position:relative;isolation:isolate;overflow:hidden;background:#121316;color:#f7f6fb}
.wd-dark-band > wd-footer{position:relative;z-index:1}
.wd-dark-band > .light-field-inner{z-index:0}
.light-field-inner{position:absolute;inset:0;height:100%;overflow:hidden;background:#121316}
.light-field-inner::before{content:"";position:absolute;left:-20%;top:-20%;width:35%;height:35%;transform-origin:0 0;transform:scale(4);background:
 radial-gradient(ellipse at 24% 42%,rgba(96,37,225,.92),transparent 44%),
 radial-gradient(ellipse at 78% 60%,rgba(237,72,151,.82),transparent 40%),
 radial-gradient(ellipse at 60% 84%,rgba(4,205,143,.32),transparent 34%),
 radial-gradient(ellipse at 42% 68%,rgba(150,72,253,.48),transparent 45%);
 animation:lightFieldDrift 22s ease-in-out infinite alternate;will-change:transform}
.light-field-inner::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 24%,rgba(18,19,22,.26),transparent 63%)}
@keyframes lightFieldDrift{from{transform:scale(4) translate3d(-4%,-3%,0) scale(1)}to{transform:scale(4) translate3d(5%,4%,0) scale(1.10)}}
@media(prefers-reduced-motion:reduce){.light-field-inner::before{animation:none}}
.bsearch{display:flex;align-items:center;gap:10px;width:min(360px,100%);height:46px;margin:18px auto 0;padding:0 18px;border:1px solid var(--line);border-radius:999px;background:rgba(255,255,255,.6);color:var(--muted);transition:border-color .25s,background .25s}
.bsearch:focus-within{border-color:#6025E1;background:#fff}
.bsearch svg{width:18px;height:18px;flex:none}
.bsearch input{flex:1;min-width:0;border:0;outline:0;background:transparent;color:var(--ink);font:500 15px var(--display)}
wd-footer{margin-top:clamp(64px,8vw,120px)}
.hero .up,.empty{font-family:var(--display)!important}

</style>

<link rel="stylesheet" href="<?php echo WD_URI; ?>/wd-revision.css">
<link rel="stylesheet" href="<?php echo WD_URI; ?>/contact.css">
<style>
/* Botões da página mantêm o próprio estilo; o padrão global de botão da home vale só para os CTAs .wd-cta */
button:where(:not(.wd-cta)){font-family:inherit;font-weight:inherit;letter-spacing:inherit}
</style>
<style>
/* Versão positiva (páginas claras): menu, painel de contato e rodapé em tons claros */
.site-nav{border-color:transparent!important;box-shadow:0 18px 55px rgba(23,19,31,.10)!important}
.site-nav::before{background:rgba(255,255,255,.74)!important}
.nav-item,.nav-link,.nav-trigger{color:#17131F!important}
.dropdown{background:rgba(255,255,255,.86)!important;border-color:rgba(23,19,31,.10)!important;box-shadow:0 22px 60px rgba(23,19,31,.14)!important}
.dropdown a{color:#17131F!important}
.dropdown a:hover,.dropdown a:focus-visible{background:rgba(96,37,225,.07)!important}
.mobile-toggle{border-color:rgba(23,19,31,.14)!important;background:rgba(23,19,31,.04)!important;color:#17131F!important}
.mobile-toggle i,.mobile-toggle i:before,.mobile-toggle i:after{background:#17131F!important}
.site-nav.wd-contact-open .mobile-toggle i{background:transparent!important}
@media(max-width:980px){.site-nav.wd-nav-open .nav-links{background:rgba(255,255,255,.95)!important;border-color:rgba(96,37,225,.16)!important}}
.nav-cta,.wd-contact .nav-cta.wd-cta{background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365)!important;background-size:280% 100%!important;background-position:100% 0!important;color:#fff!important;transition:background-position .6s ease,color .2s ease!important}
.nav-cta:hover,.nav-cta:focus-visible,.wd-contact .nav-cta.wd-cta:hover,.wd-contact .nav-cta.wd-cta:focus-visible{background-position:0 0!important;color:#2b1450!important}
.site-nav.wd-contact-open .wd-contact-close-trigger{background:none!important;color:#17131F!important}
.wd-contact-glass{background:rgba(255,255,255,.80)!important}
.wd-contact-stroke{stroke:rgba(23,19,31,.10)!important}
.wd-contact-shadow{fill:rgba(23,19,31,.12)!important}
.wd-contact-backdrop{background:rgba(244,243,236,.45)!important}
.wd-contact,.wd-contact-title,.wd-contact-result-title{color:#17131F!important}
.wd-contact .wd-contact-uptitle.wd-uptitle{background:linear-gradient(90deg,#6025E1,#A23FC9 55%,#D9467F)!important;-webkit-background-clip:text!important;background-clip:text!important}
.wd-contact .wd-contact-input{color:#17131F!important;border-bottom-color:rgba(23,19,31,.18)!important}
.wd-contact .wd-contact-input:hover{border-color:rgba(23,19,31,.42)!important}
.wd-contact .wd-contact-input::placeholder{color:#6B6578!important}
.wd-contact .wd-contact-input:focus,.wd-contact .wd-contact-input:focus-visible{caret-color:#17131F!important}
.wd-contact-field::after{background:linear-gradient(90deg,#6025E1,#A23FC9,#D9467F)!important}
.wd-contact .wd-contact-input[aria-invalid="true"]{border-color:#C9184A!important}
.wd-contact .wd-contact-input[aria-invalid="true"]::placeholder,.wd-contact-field-error{color:#C9184A!important}
.wd-contact-privacy,.wd-contact-result-text,.wd-contact-result-note{color:#6B6578!important}
.wd-contact-privacy a{color:#17131F!important}
wd-cursor-fix{}
.wd-cursor:not(.big){background:#17131F!important;box-shadow:0 0 0 1px rgba(255,255,255,.6)!important}
wd-footer{--wd-footer-icon-cutout:#F4F3EC!important;border-top:1px solid rgba(23,19,31,.10)!important}
</style>
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="wd-skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <nav class="site-nav" aria-label="Navegação principal">
    <a class="brand" href="<?php echo esc_url(wd_url('')); ?>" aria-label="Work Digital — Home">
      <img src="<?php echo WD_URI; ?>/img/logo-work-digital-positivo.svg" alt="Work Digital">
    </a>
    <div class="nav-links">
      <a class="nav-link" href="<?php echo esc_url(wd_url('')); ?>">Home</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('solucoes/')); ?>">Soluções</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('cases/')); ?>">Works</a>
      <a class="nav-link" href="#" aria-current="page">Blog</a>
    </div>
    <div class="wd-nav-actions">
      <button class="nav-cta wd-cta" data-wd-contact type="button">SOLICITAR PROPOSTA <span>↗</span></button>
      <button class="mobile-toggle" type="button" aria-label="Abrir menu"><i></i></button>
    </div>
  </nav>
</header>

<main id="conteudo" tabindex="-1">
<?php get_template_part('parts/page'); ?>
</main>
<wd-footer id="wd-footer" data-theme="light"></wd-footer>



<div class="wd-cursor" id="wdCursor" aria-hidden="true" hidden><b></b></div>

<script>
// Reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}}),{rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));

// Cursor (igual às outras páginas)
(function(){
  if(!matchMedia('not all and (pointer: coarse)').matches||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c=document.getElementById('wdCursor'), lb=c.querySelector('b'); c.hidden=false; document.body.classList.add('has-wd-cursor');
  const LABELS=[[".row a","Ler"],[".feat .img","Ler"]];
  let mx=innerWidth/2,my=innerHeight/2,x=mx,y=my;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;c.style.transform=`translate(${mx}px,${my}px)`;},{passive:true});
  document.addEventListener('mouseover',e=>{
    let label=null; for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }
    c.classList.toggle('big',!!label);document.documentElement.classList.toggle('wd-big',!!label); if(label) lb.textContent=label;
    c.classList.toggle('link',!label && !!e.target.closest('a,button,input'));
  });
  document.addEventListener('mouseleave',()=>{c.classList.remove('big','link');});
  
})();
</script>
<script src="<?php echo WD_URI; ?>/footer.js" defer></script>
<script src="<?php echo WD_URI; ?>/wd-revision.js" defer></script>
<!-- cursor_css_done --><style>/* Cursor desenhado pelo sistema (sem atraso). O círculo com texto continua só sobre os cards. */
@media not all and (pointer: coarse){html,html body,html body *{cursor:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2216%22%20height%3D%2216%22%3E%3Ccircle%20cx%3D%228%22%20cy%3D%228%22%20r%3D%225.5%22%20fill%3D%22%2317131F%22%20stroke%3D%22%23fff%22%20stroke-opacity%3D%22.7%22/%3E%3C/svg%3E") 8 8,auto!important}html body a,html body a *,html body button,html body button *,html body [role=button],html body label,html body .svc:not(.is-open),html body .svc:not(.is-open) *{cursor:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2240%22%20height%3D%2240%22%3E%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%236025E1%22/%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%23C00252%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Ccircle%20cx%3D%2220%22%20cy%3D%2220%22%20r%3D%2218.5%22%20fill%3D%22url%28%23g%29%22%20fill-opacity%3D%22.28%22%20stroke%3D%22url%28%23g%29%22%20stroke-width%3D%222%22/%3E%3Ccircle%20cx%3D%2220%22%20cy%3D%2220%22%20r%3D%223%22%20fill%3D%22url%28%23g%29%22/%3E%3C/svg%3E") 20 20,pointer!important}html body input,html body textarea{cursor:text!important}html.wd-big,html.wd-big body,html.wd-big body *{cursor:none!important}}.wd-cursor:not(.big),.cursor:not(.big){opacity:0!important}.wd-cursor.big,.cursor.big{background:linear-gradient(135deg,#6025E1,#C00252)!important;color:#fff!important;box-shadow:none!important;border:0!important;outline:0!important}</style>
<style>/* Modo leve (GPU fraca): sem desfoque por trás dos painéis — fundos mais opacos no lugar; luz de fundo parada */
html.wd-lite *,html.wd-lite *::before,html.wd-lite *::after{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}html.wd-lite .site-nav::before{background:rgba(255,255,255,.96)!important}html.wd-lite .dropdown{background:rgba(255,255,255,.98)!important}html.wd-lite .site-nav.wd-nav-open .nav-links{background:rgba(255,255,255,.98)!important}html.wd-lite .wd-contact-glass{background:rgba(255,255,255,.97)!important}html.wd-lite .wd-contact-backdrop{background:rgba(10,10,14,.55)!important}html.wd-lite .light-field-inner::before,html.wd-lite .light-field-inner::after,html.wd-lite .light-field-inner{animation:none!important}html.wd-lite .svc{--card:linear-gradient(125deg,rgba(96,37,225,.16),rgba(49,22,78,.26)),rgba(20,20,26,.94)}html.wd-lite .orb,html.wd-lite .orb2,html.wd-lite .orb::after{animation:none!important}</style>
<style>/* Responsivo (todas as páginas) */
html,body{overflow-x:clip}@media(min-width:981px) and (max-width:1180px){.site-header .site-nav{grid-template-columns:auto minmax(0,1fr) auto;gap:16px}.site-header .nav-links{gap:clamp(14px,2.1vw,28px)}.site-header .wd-nav-actions{gap:14px}}</style>
<?php wp_footer(); ?>
</body>
</html>
