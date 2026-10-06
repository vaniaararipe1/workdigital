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
:where(a,button,input,select,textarea,summary,[tabindex]):focus-visible{outline:2px solid var(--wd-focus,#CBB6FF)!important;outline-offset:3px!important}
.wd-pause{position:fixed;left:16px;bottom:16px;z-index:9990;display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 14px 0 12px;border-radius:999px;border:1px solid rgba(189,164,255,.35);background:rgba(18,19,22,.78);color:#F7F6FB;font:500 12px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;cursor:pointer;backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);opacity:.82;transition:opacity .2s,background .2s}
.wd-pause:hover,.wd-pause:focus-visible{opacity:1;background:rgba(96,37,225,.85)}
.wd-pause svg{width:14px;height:14px;flex:none}
.wd-pause .on{display:none}html.wd-paused .wd-pause .on{display:inline}html.wd-paused .wd-pause .off{display:none}
@media(max-width:700px){.wd-pause{width:40px;padding:0;justify-content:center}.wd-pause .t{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0)}}
html.wd-paused *,html.wd-paused *::before,html.wd-paused *::after{animation-play-state:paused!important}
html.wd-paused .particle-art canvas,html.wd-paused .native-particles canvas,html.wd-paused #fluid,html.wd-paused #cfluid{visibility:hidden!important}
html{background-color:#0B0B0C}
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Nunito:wght@300;400;600&family=Silkscreen&display=swap">
<style>
/* Layout: Lusion-style horizontal case page — fixed pill header, intro panel at left, media strip scrolled sideways by vertical scroll, light "next project" panel at the end. Single dark look by choice. */
:root{
  --bg:#150e24; --fg:#F4F0FA; --muted:#B6ADC9; --accent:#C4A8FF; --pink:#FF9BD0;
  --pill:#ffffff; --pill-dark:#2a2140; --line:rgba(244,240,250,.14);
  --display:"Space Grotesk","Helvetica Neue",Arial,sans-serif;
  --body:"Nunito",system-ui,sans-serif;
  --pad:clamp(16px,3.4vw,48px);
  --ease:cubic-bezier(.22,1,.36,1);
  color-scheme:dark;
}
*{box-sizing:border-box}
html{background:#121316}body{background:transparent;color:var(--fg);font-family:var(--body);overflow-x:hidden}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;border:0;background:none;cursor:pointer}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}

/* Header (fixed pills) */
.hd{position:fixed;top:env(safe-area-inset-top,0px);left:0;right:0;z-index:20;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;padding:24px var(--pad);pointer-events:none}
.hd > *{pointer-events:auto}
.logo{font:600 22px/1 var(--display);letter-spacing:.02em;text-transform:uppercase;color:var(--accent);justify-self:start}
.pill{display:inline-flex;align-items:center;gap:10px;height:42px;padding:0 20px;border-radius:999px;font:500 13px/1 var(--display);letter-spacing:.04em;text-transform:uppercase;transition:transform .4s var(--ease),background .3s}
.pill:hover{transform:scale(1.04)}
.pill.light{background:var(--pill);color:#140c22}
.pill.dark{background:var(--pill-dark);color:#fff}
.pill .dot{width:5px;height:5px;border-radius:50%;background:currentColor}
.circle{width:42px;height:42px;border-radius:50%;background:var(--pill);display:grid;place-items:center}
.circle i{width:14px;height:2px;background:#140c22;border-radius:2px}
.hd .right{justify-self:end;display:flex;gap:10px;align-items:center}

/* Horizontal scroller */
.hs{position:relative}
.stick{position:sticky;top:0;height:100vh;height:100svh;overflow:hidden}
.track{display:flex;align-items:center;gap:40px;height:100%;padding-left:var(--pad);will-change:transform}
.intro{flex:0 0 auto;width:min(760px,62vw);height:100%;display:grid;grid-template-columns:1.25fr .75fr;gap:32px;align-content:center;padding-top:40px}
.intro h1{grid-column:1 / -1;font:400 clamp(44px,5vw,72px)/1 var(--display);letter-spacing:-.03em;margin:0 0 12px}
.intro p{font-size:14.5px;line-height:1.55;margin:0 0 14px;color:var(--fg);max-width:46ch}
.intro p a{color:var(--accent);transition:color .2s}
.intro p a:hover{color:var(--pink)}
.intro h2{font:500 11px/1 var(--display);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 10px}
.intro ul{list-style:none;margin:0 0 28px;padding:0;font-size:13.5px;line-height:1.6}
.intro ul a{border-bottom:1px solid transparent;transition:border-color .2s}
.intro ul a:hover{border-color:currentColor}
.intro .cta{margin-top:18px}
.note{font:400 11px/1.4 var(--display);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-top:22px}

/* Media items */
.m{flex:0 0 auto;position:relative;border-radius:12px;overflow:hidden;background:#21183a}
.m.h74{height:74%}
.m.full{height:100%;border-radius:0}
.w169{aspect-ratio:16/9}.w34{aspect-ratio:3/4}.w11{aspect-ratio:1}.w45{aspect-ratio:4/5}
.m .cap{position:absolute;left:14px;bottom:12px;font:500 10px var(--display);letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.8);background:rgba(20,12,34,.5);padding:6px 10px;border-radius:999px;backdrop-filter:blur(6px)}

/* Mock site visuals (stand-ins for case images) */
.site{position:absolute;inset:0;background:#F7F4EC;color:#141414;display:grid;grid-template-rows:auto 1fr}
.site nav{display:flex;justify-content:space-between;align-items:center;padding:2.4% 4%;font:700 clamp(9px,1vw,13px) var(--display);text-transform:uppercase}
.site nav span{font-weight:500;opacity:.6;letter-spacing:.06em}
.site .hero{display:grid;grid-template-columns:1.1fr 1fr;align-items:center;gap:5%;padding:0 6% 5%}
.site h3{font:700 clamp(22px,3.6vw,58px)/.92 var(--display);text-transform:uppercase;margin:0 0 4%}
.site p{font-size:clamp(9px,.95vw,14px);margin:0 0 6%;color:#555}
.site .btn{display:inline-block;background:#0091FE;color:#fff;font:600 clamp(8px,.85vw,12px) var(--display);padding:3% 5%;letter-spacing:.04em;text-transform:uppercase}
.mark{aspect-ratio:1;background:conic-gradient(from 45deg,#0091FE 0 25%,#141414 0 50%,#0091FE 0 75%,#F7F4EC 0);border:3px solid #141414}
.poster{position:absolute;inset:0;background:radial-gradient(60% 50% at 50% 55%,#0091FE 0%,#0a3f78 45%,#0b0b14 85%);display:flex;flex-direction:column;justify-content:space-between;padding:110px 7% 7%}
.poster b{font:700 clamp(40px,6vw,96px)/.85 var(--display);text-transform:uppercase;color:#F7F4EC;letter-spacing:-.02em}
.poster small{font:500 11px var(--display);letter-spacing:.12em;text-transform:uppercase;color:#cfe8ff;display:flex;justify-content:space-between}
.poster .sh{align-self:center;width:46%;aspect-ratio:1;border-radius:50%;background:radial-gradient(circle at 40% 35%,#1d1d2b,#000);box-shadow:0 0 80px 20px rgba(0,145,254,.55)}
.fabric{position:absolute;inset:0;background:
  repeating-linear-gradient(45deg,rgba(255,255,255,.06) 0 2px,transparent 2px 7px),
  repeating-linear-gradient(-45deg,rgba(0,0,0,.18) 0 2px,transparent 2px 7px),
  radial-gradient(70% 70% at 40% 40%,#2c6fd6,#0d2c66)}
.fabric .tag{position:absolute;left:12%;top:16%;width:34%;aspect-ratio:1;background:conic-gradient(from 45deg,#F7F4EC 0 25%,#141414 0 50%,#F7F4EC 0 75%,transparent 0);opacity:.9;transform:rotate(-8deg);mix-blend-mode:screen}
.phone{position:absolute;left:50%;top:50%;width:46%;aspect-ratio:9/19;transform:translate(-50%,-50%);border-radius:30px;border:7px solid #0e0a18;background:#F7F4EC;padding:16% 9% 10%;display:flex;flex-direction:column;gap:7%;box-shadow:0 40px 80px -30px rgba(0,0,0,.8)}
.phone .t{height:9%;width:85%;background:#141414}.phone .s{height:4%;width:60%;background:#cfc8ba}.phone .i{flex:1;background:conic-gradient(from 45deg,#0091FE 0 25%,#141414 0 50%,#0091FE 0 75%,#e7e1d4 0)}.phone .c{height:7%;width:55%;background:#0091FE}
.phone-bg{position:absolute;inset:0;background:radial-gradient(70% 60% at 50% 60%,#6b4fd0,#241444)}
.sketch{position:absolute;inset:0;background:#e9dfc8;background-image:
  radial-gradient(circle at 30% 26%,transparent 17%,rgba(80,60,40,.5) 17.3%,transparent 17.8%),
  radial-gradient(circle at 70% 24%,transparent 9%,rgba(80,60,40,.45) 9.3%,transparent 9.8%),
  radial-gradient(circle at 46% 66%,transparent 21%,rgba(80,60,40,.45) 21.3%,transparent 21.8%),
  linear-gradient(rgba(80,60,40,.18) 1px,transparent 1px),linear-gradient(90deg,rgba(80,60,40,.18) 1px,transparent 1px);
  background-size:auto,auto,auto,48px 48px,48px 48px}
.sketch em{position:absolute;right:10%;top:44%;font:italic 400 clamp(18px,2.2vw,30px)/1.1 Georgia,serif;color:rgba(60,45,30,.8);transform:rotate(-6deg)}
.palette{position:absolute;inset:0;display:grid;grid-template-rows:repeat(4,1fr)}
.palette span{display:flex;align-items:center;padding:0 10%;font:500 13px var(--display);letter-spacing:.08em}

/* Next project (light panel) */
.next{flex:0 0 auto;width:min(980px,78vw);height:100%;background:#f1eef7;color:#16102a;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;padding:0 6%}
.next::before{content:"";position:absolute;inset:-10%;background:radial-gradient(40% 18% at 30% 40%,rgba(124,92,255,.16),transparent 70%),radial-gradient(30% 14% at 60% 52%,rgba(255,155,208,.18),transparent 70%);transform:rotate(-12deg)}
.next .big{position:relative;font:300 clamp(56px,8vw,128px)/1 var(--display);letter-spacing:-.04em;color:#b9b2c9;white-space:nowrap;transition:color .5s var(--ease),transform .7s var(--ease)}
.next:hover .big{color:#16102a;transform:translateX(-14px)}
.next .bottom{position:absolute;left:6%;right:6%;bottom:9%;display:flex;align-items:center;gap:20px;font:500 12px var(--display);letter-spacing:.06em;text-transform:uppercase}
.next .bottom i{flex:0 0 120px;height:1px;background:#16102a;opacity:.5;transition:flex-basis .6s var(--ease)}
.next:hover .bottom i{flex-basis:200px}
.next .bottom b{font-size:18px}

/* Loader shown when "next project" is clicked */
.loader{position:fixed;inset:0;z-index:50;background:#07050d;display:grid;place-items:center;opacity:0;visibility:hidden;transition:opacity .4s,visibility .4s}
.loader.on{opacity:1;visibility:visible}
.loader p{font:400 clamp(14px,1.6vw,20px) "Silkscreen",monospace;letter-spacing:.4em;color:#fff;margin:0}
.loader .bar{position:absolute;left:50%;top:58%;transform:translateX(-50%);width:120px;height:8px;background:#2a2140}
.loader .bar span{display:block;height:100%;width:0;background:#fff}
.loader .num{position:absolute;bottom:6%;left:50%;transform:translateX(-50%);font:300 clamp(48px,7vw,96px)/1 var(--display);letter-spacing:-.04em;font-variant-numeric:tabular-nums}

/* WhatsApp float */
.wa{position:fixed;right:20px;bottom:calc(20px + env(safe-area-inset-bottom,0px));z-index:30;width:56px;height:56px;border-radius:50%;background:#25D366;display:grid;place-items:center;box-shadow:0 10px 30px -8px rgba(37,211,102,.6)}
.wa svg{width:28px;height:28px;fill:#fff}

/* Mobile: vertical stack */
@media (max-width:900px){
  .hd{grid-template-columns:1fr auto;padding:16px var(--pad)}
  .hd .back{display:none}
  .hd .circle,.hd .pill.dark{display:none}
  .hs{height:auto!important}
  .stick{position:static;height:auto;overflow:visible}
  .track{flex-direction:column;align-items:stretch;transform:none!important;padding:96px var(--pad) 40px;gap:16px}
  .intro{width:auto;grid-template-columns:1fr;padding-top:0;gap:8px;margin-bottom:24px}
  .m.h74,.m.full{height:auto;width:100%;border-radius:12px}
  .m.full.w34,.m.full.w45{aspect-ratio:4/5}
  .next{width:auto;min-height:60vh;border-radius:12px;margin-top:8px}
  .next .big{white-space:normal;font-size:clamp(44px,13vw,72px)}
  .note{margin-bottom:24px}
  .site + .cap{display:none}
  .next{min-height:52vh}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}

/* Custom cursor (same as the Works page): small dot that follows the mouse; grows on links, shows a label on key items */
.wd-cursor{position:fixed;left:0;top:0;z-index:2147483000;pointer-events:none;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#F2EEF8;box-shadow:0 0 0 1px rgba(18,19,22,.35);
  transition:width .4s cubic-bezier(.22,1,.36,1),height .4s cubic-bezier(.22,1,.36,1),margin .4s cubic-bezier(.22,1,.36,1),background .3s;display:grid;place-items:center}
.wd-cursor b{font:500 11px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#fff;opacity:0;transition:opacity .2s;white-space:nowrap}
.wd-cursor.link{width:40px;height:40px;margin:-20px 0 0 -20px}
.wd-cursor.big{width:96px;height:96px;margin:-48px 0 0 -48px;background:#7C5CFF;mix-blend-mode:normal}
.wd-cursor.big b{opacity:1}
@media not all and (pointer: coarse){.has-wd-cursor,.has-wd-cursor a,.has-wd-cursor button{cursor:none}}
body{margin:0}
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
/* Fundo da home: camada de luz fixa (copiada da home) */
body{isolation:isolate}
.light-field{position:fixed;inset:0;z-index:-1;pointer-events:none}
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
wd-footer{position:relative;z-index:1}
/* Menu da home só como base do painel de contato (o menu antigo continua visível) */
.site-header{opacity:0;visibility:hidden;transition:opacity .3s,visibility .3s}
.site-header.wd-contact-header-open{opacity:1;visibility:visible}
.hd{transition:opacity .3s}
body:has(.site-header.wd-contact-header-open) .hd{opacity:0;pointer-events:none}
.hd .nav-cta{display:inline-flex!important}
.wd-work-cta{display:inline-flex;align-items:center;justify-content:center;gap:16px;width:max-content;max-width:100%;min-height:54px;padding:14px 20px;border:0;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;text-transform:uppercase;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0%;transition:background-position .6s ease,color .2s ease}
.wd-work-cta:hover,.wd-work-cta:focus-visible{background-position:0% 0%;color:#24123e}
.wd-work-cta svg{width:14px;height:14px;flex:0 0 14px}
/* logo: troca para a versão positiva quando passa por cima de uma imagem clara */
.hd .logo{position:relative;display:block}
.hd .logo img{display:block;width:142px;height:auto;transition:opacity .25s ease}
.hd .logo .logo-pos{position:absolute;left:0;top:0;opacity:0}
.hd .logo.on-light .logo-neg{opacity:0}
.hd .logo.on-light .logo-pos{opacity:1}
.hd.over-footer{opacity:0!important;visibility:hidden;transition:opacity .3s ease,visibility 0s .3s}
@media(max-width:900px){.intro .cta{margin-bottom:36px}.track{height:auto}}
@media(max-width:600px){.hd .logo img{width:120px}}
/* Voltar: vidro escuro com borda (estilo do menu), para não competir com o "Solicitar proposta" */
.hd .pill.light.back{background:rgba(18,19,22,.58);color:#F7F6FB;border:1px solid rgba(189,164,255,.28);backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%)}
.hd .pill.light.back:hover{background:rgba(96,37,225,.42);border-color:rgba(189,164,255,.5)}
html.wd-lite .hd .pill.light.back{background:rgba(18,19,22,.93)}
@media(max-width:600px){.hd .nav-cta{height:42px;padding:0 14px;font-size:11px;letter-spacing:.06em}}
/* galeria: as imagens ficam entre o cabeçalho e o fim da tela (antes encostavam nos botões em telas baixas) */
@media (min-width:901px){.track{padding-top:96px;padding-bottom:28px}.intro{padding-top:0}.m.full{align-self:flex-start;height:100vh;height:100svh;margin-top:-96px}}


/* Mídias reais dos cases: preenchem o bloco (o arredondamento e a legenda são do site) */
.m>img,.m>video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.m>video{background:#120B20}
.m .cap{z-index:2}
</style>

<link rel="stylesheet" href="<?php echo WD_URI; ?>/wd-revision.css">
<link rel="stylesheet" href="<?php echo WD_URI; ?>/contact.css">
<style>
/* Botões da página mantêm o próprio estilo; o padrão global de botão da home vale só para os CTAs .wd-cta */
button:where(:not(.wd-cta)){font-family:inherit;font-weight:inherit;letter-spacing:inherit}
</style>
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="wd-skip" href="#top">Pular para o conteúdo</a>
<button class="wd-pause" type="button" aria-pressed="false" data-wd-pause><svg class="off" viewBox="0 0 16 16" aria-hidden="true"><rect x="3" y="2" width="3.5" height="12" rx="1" fill="currentColor"/><rect x="9.5" y="2" width="3.5" height="12" rx="1" fill="currentColor"/></svg><svg class="on" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 2.5v11l9-5.5z" fill="currentColor"/></svg><span class="t"><span class="off">Pausar animações</span><span class="on">Retomar animações</span></span></button>
<header class="hd">
  <a class="logo" href="<?php echo esc_url(wd_url('')); ?>" aria-label="Work Digital, início"><img class="logo-neg" src="<?php echo WD_URI; ?>/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital"><img class="logo-pos" src="<?php echo WD_URI; ?>/img/logo-work-digital-positivo.svg" alt="" aria-hidden="true"></a>
  <a class="pill light back" href="<?php echo esc_url(wd_url('cases/')); ?>">← Voltar</a>
</header>

<div class="light-field" aria-hidden="true"><div class="light-field-inner"></div></div>
<header class="site-header">
  <nav class="site-nav" aria-label="Navegação principal">
    <a class="brand" href="<?php echo esc_url(wd_url('')); ?>" aria-label="Work Digital — Home">
      <img src="<?php echo WD_URI; ?>/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital">
    </a>
    <div class="nav-links">
      <a class="nav-link" href="<?php echo esc_url(wd_url('')); ?>">Home</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('solucoes/')); ?>">Soluções</a>
      <a class="nav-link" href="#" aria-current="page">Works</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('blog/')); ?>">Blog</a>
    </div>
    <div class="wd-nav-actions">
      <div class="nav-item wd-language">
        <button class="nav-trigger wd-language-trigger wd-cta" type="button" aria-label="Idioma do site: Português" aria-haspopup="true" aria-expanded="false" aria-controls="wd-language-dropdown"><svg class="wd-language-globe" viewBox="0 0 24 24" fill="none" aria-hidden="true"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.5"/><ellipse cx="12" cy="12" rx="4" ry="9" stroke="currentColor" stroke-width="1.5"/><path d="M3 12h18" stroke="currentColor" stroke-width="1.5"/></svg>PT<svg viewBox="0 0 12 12" fill="none" aria-hidden="true"><path d="M2.5 4.25 6 7.75l3.5-3.5" stroke="currentColor" stroke-width="1.2"/></svg></button>
        <div class="dropdown" id="wd-language-dropdown">
          <a href="https://workdigital.art.br/" lang="pt-BR" aria-current="true"><span class="drop-copy"><strong>Português</strong></span></a>
          <a href="https://workdigital.art.br/en/" lang="en"><span class="drop-copy"><strong>English</strong></span></a>
        </div>
      </div>
      <button class="nav-cta wd-cta" data-wd-contact type="button">SOLICITAR PROPOSTA <span>↗</span></button>
      <button class="mobile-toggle" type="button" aria-label="Abrir menu"><i></i></button>
    </div>
  </nav>
</header>
<main id="top" tabindex="-1">
  <section class="hs" id="hs">
    <div class="stick">
      <div class="track" id="track">
<?php get_template_part('parts/case-track'); ?>
      </div>
    </div>
  </section>
</main>
<script>
/* Case: vídeo do bloco 5 carrega perto da tela e toca com 50% visível; o item focado pelo teclado entra na tela */
(function(){
  const track=document.getElementById('track'); if(!track) return;
  const still=matchMedia('(prefers-reduced-motion: reduce)').matches||document.documentElement.classList.contains('wd-lite');
  const vs=[...track.querySelectorAll('video.case-video')];
  if(!still&&vs.length){
    const load=v=>{if(v.dataset.ld)return;v.dataset.ld=1;v.querySelectorAll('source[data-src]').forEach(s=>s.src=s.dataset.src);v.load();};
    const ioLoad=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){load(en.target);ioLoad.unobserve(en.target);}}),{rootMargin:'300px'});
    const ioPlay=new IntersectionObserver(es=>es.forEach(en=>{const v=en.target;if(en.intersectionRatio>=.5){load(v);const p=v.play();p&&p.catch(()=>{});}else v.pause();}),{threshold:[0,.5,1]});
    vs.forEach(v=>{ioLoad.observe(v);ioPlay.observe(v);});
  }
  track.addEventListener('focusin',e=>{
    if(matchMedia('(max-width:900px)').matches)return;
    const hs=document.getElementById('hs'), st=hs&&hs.querySelector('.stick'); if(!hs)return;
    if(st)st.scrollLeft=0;
    const r=e.target.getBoundingClientRect(), x=r.left-track.getBoundingClientRect().left;
    const dist=Math.max(0,track.scrollWidth-innerWidth), want=Math.min(dist,Math.max(0,x+r.width/2-innerWidth/2));
    scrollTo({top:hs.getBoundingClientRect().top+scrollY+want,behavior:'auto'});
  });
})();
</script>


<div class="loader" id="loader" aria-hidden="true"><p>Carregando</p><div class="bar"><span id="bar"></span></div><div class="num" id="num">000</div></div>


<div class="wd-cursor" id="wdCursor" aria-hidden="true" hidden><b></b></div>
<script>
(function(){
  const hs=document.getElementById('hs'), track=document.getElementById('track');
  const mobile=matchMedia('(max-width:900px)'), reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let dist=0, cur=0, target=0;
  function size(){
    if(mobile.matches){ hs.style.height=''; track.style.transform=''; return; }
    dist=Math.max(0, track.scrollWidth - innerWidth);
    hs.style.height=(innerHeight + dist)+'px';
    update(); cur=target; apply();
  }
  function update(){
    const top=hs.getBoundingClientRect().top;
    const p=Math.min(1,Math.max(0,-top/Math.max(1,dist)));
    target=p*dist;
  }
  function apply(){ track.style.transform='translate3d('+(-cur)+'px,0,0)'; }
  function loop(){
    if(!mobile.matches){
      cur += reduce ? (target-cur) : (target-cur)*0.12;
      if(Math.abs(target-cur)<0.1) cur=target;
      apply();
    }
    requestAnimationFrame(loop);
  }
  addEventListener('scroll',update,{passive:true});
  addEventListener('resize',size);
  mobile.addEventListener('change',size);
  document.fonts && document.fonts.ready.then(size);
  size(); loop();

  // "Next project" loader, as in the reference
  const loader=document.getElementById('loader'), bar=document.getElementById('bar'), num=document.getElementById('num');
  document.addEventListener('click',e=>{ if(!e.target.closest('#next')) return;
    e.preventDefault(); loader.classList.add('on');
    let n=0; const t=setInterval(()=>{ n=Math.min(100,n+Math.ceil(Math.random()*9));
      num.textContent=String(n).padStart(3,'0'); bar.style.width=n+'%';
      if(n>=100){ clearInterval(t); setTimeout(()=>{ const nx=document.getElementById('next'); if(nx){location.href=nx.href;return;} loader.classList.remove('on'); bar.style.width='0'; num.textContent='000'; scrollTo({top:0}); },500); }
    },70);
  });
})();

// Custom cursor (shared across pages)
(function(){
  if(!matchMedia('not all and (pointer: coarse)').matches||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c=document.getElementById('wdCursor'), lb=c.querySelector('b'); c.hidden=false; document.body.classList.add('has-wd-cursor');
  const LABELS=[["#next","Próximo"],[".m","Ver"]];
  let mx=innerWidth/2,my=innerHeight/2,x=mx,y=my;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;c.style.transform=`translate(${mx}px,${my}px)`;},{passive:true});
  document.addEventListener('mouseover',e=>{
    let label=null; if(!e.target.closest('.case-lb'))for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }
    c.classList.toggle('big',!!label);document.documentElement.classList.toggle('wd-big',!!label); if(label) lb.textContent=label;
    c.classList.toggle('link',!label && !!e.target.closest('a,button'));
  });
  document.addEventListener('mouseleave',()=>{c.classList.remove('big','link');});
  
})();
</script>
<script>
(function(){
  const logo=document.querySelector('.hd .logo'); if(!logo)return;
  const hd=document.querySelector('.hd');
  function lum(c){const m=c.match(/[\d.]+/g);if(!m)return null;const a=m.length>3?+m[3]:1;if(a<.5)return null;return (0.2126*m[0]+0.7152*m[1]+0.0722*m[2])/255;}
  function bgAt(x,y){
    for(const el of document.elementsFromPoint(x,y)){
      if(hd.contains(el)||el.closest('.site-header,wd-footer,.wd-whatsapp'))continue;
      for(let n=el;n&&n!==document.documentElement;n=n.parentElement){const l=lum(getComputedStyle(n).backgroundColor);if(l!==null)return l;}
      return 0;
    }
    return 0;
  }
  function check(){
    const r=logo.getBoundingClientRect();if(!r.width)return;
    const pts=[[.15,.5],[.5,.5],[.85,.5]];let light=0;
    pts.forEach(([fx,fy])=>{if(bgAt(r.left+r.width*fx,r.top+r.height*fy)>.62)light++;});
    logo.classList.toggle('on-light',light>=2);
    // no rodapé (que já tem o logo grande e o CTA) o cabeçalho do case some para não duplicar
    const ft=document.querySelector('wd-footer');
    hd.classList.toggle('over-footer',!!ft&&ft.getBoundingClientRect().top<hd.getBoundingClientRect().bottom+24);
  }
  let busy=false;
  function req(){if(!busy){busy=true;requestAnimationFrame(()=>{busy=false;check();});}}
  addEventListener('scroll',()=>{req();clearTimeout(window.__wdLogoT);window.__wdLogoT=setTimeout(check,350);},{passive:true});
  addEventListener('resize',req,{passive:true});
  setInterval(()=>{if(!document.hidden)check();},400);
  check();
})();
</script>
<script src="<?php echo WD_URI; ?>/footer.js" defer></script>
<script src="<?php echo WD_URI; ?>/wd-revision.js" defer></script>
<style>
/* Tela cheia das imagens do case */
.case-lb{position:fixed;inset:0;z-index:1000;visibility:hidden;pointer-events:none}
.case-lb.open{visibility:visible;pointer-events:auto}
.case-lb-bg{position:absolute;inset:0;background:rgba(12,8,22,.94);opacity:0;transition:opacity .45s cubic-bezier(.22,1,.36,1)}
.case-lb.open .case-lb-bg{opacity:1}
.case-lb-stage{position:absolute;inset:0;overflow:hidden}
.case-lb-item{position:absolute;margin:0!important;align-self:auto;transform-origin:0 0;border-radius:16px!important;box-shadow:0 40px 120px -30px rgba(0,0,0,.7);transition:transform .55s cubic-bezier(.22,1,.36,1),opacity .35s ease}
.case-lb-ui{position:absolute;inset:0;pointer-events:none;opacity:0;transition:opacity .3s ease}
.case-lb.open.ready .case-lb-ui{opacity:1}
.case-lb-ui>*{pointer-events:auto}
.case-lb-btn{position:absolute;display:grid;place-items:center;width:52px;height:52px;border-radius:50%;border:1px solid rgba(189,164,255,.35);background:rgba(18,19,22,.6);color:#F7F6FB;font:400 22px/1 "Space Grotesk",Arial,sans-serif;transition:background .25s,border-color .25s,transform .25s}
.case-lb-btn:hover,.case-lb-btn:focus-visible{background:linear-gradient(135deg,#6025E1,#C00252);border-color:transparent}
.case-lb-btn:focus-visible{outline:2px solid #CBB6FF;outline-offset:3px}
.case-lb-close{top:24px;right:clamp(16px,3.4vw,48px)}
.case-lb-prev,.case-lb-next{top:50%;margin-top:-26px}
.case-lb-prev{left:clamp(16px,3.4vw,48px)}
.case-lb-next{right:clamp(16px,3.4vw,48px)}
.case-lb-prev:hover{transform:translateX(-3px)}.case-lb-next:hover{transform:translateX(3px)}
.case-lb-count{position:absolute;top:38px;left:clamp(16px,3.4vw,48px);color:#EFE7FF;font:500 13px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.12em}
@media(max-width:700px){.case-lb-prev,.case-lb-next{top:auto;bottom:24px;margin:0}.case-lb-btn{width:46px;height:46px}}
.m{cursor:zoom-in}
html.case-lb-on .hd,html.case-lb-on .wd-whatsapp-root,html.case-lb-on wd-whatsapp{visibility:hidden}
@media(prefers-reduced-motion:reduce){.case-lb-item,.case-lb-bg,.case-lb-ui{transition:none}}
</style>
<div class="case-lb" id="caseLb" role="dialog" aria-modal="true" aria-label="Imagem do projeto em tela cheia" aria-hidden="true">
  <div class="case-lb-bg"></div>
  <div class="case-lb-stage"></div>
  <div class="case-lb-ui">
    <span class="case-lb-count" aria-live="polite"></span>
    <button class="case-lb-btn case-lb-close" type="button" aria-label="Fechar">✕</button>
    <button class="case-lb-btn case-lb-prev" type="button" aria-label="Imagem anterior">←</button>
    <button class="case-lb-btn case-lb-next" type="button" aria-label="Próxima imagem">→</button>
  </div>
</div>
<script>
(function(){
  const lb=document.getElementById('caseLb'), stage=lb.querySelector('.case-lb-stage'), count=lb.querySelector('.case-lb-count');
  let items=[];const refresh=()=>{items=[...document.querySelectorAll('.track .m')];};refresh();
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let idx=-1, node=null, last=null;
  function fit(src){
    const r=src.getBoundingClientRect(), ratio=r.width/Math.max(1,r.height);
    const padX=innerWidth<=700?16:Math.max(96,innerWidth*.07), padY=innerWidth<=700?96:72;
    let w=innerWidth-padX*2, h=w/ratio;
    if(h>innerHeight-padY*2){h=innerHeight-padY*2;w=h*ratio;}
    return {r,w,h,x:(innerWidth-w)/2,y:(innerHeight-h)/2};
  }
  function build(i){
    const src=items[i], f=fit(src), el=src.cloneNode(true);
    el.removeAttribute('id');el.querySelectorAll('[id]').forEach(n=>n.removeAttribute('id'));
    el.classList.add('case-lb-item');const cv=el.querySelector('video');if(cv){const ov=src.querySelector('video');cv.querySelectorAll('source').forEach(s=>{if(s.dataset.src)s.src=s.dataset.src;});cv.muted=true;cv.loop=true;cv.playsInline=true;if(!(matchMedia('(prefers-reduced-motion: reduce)').matches||document.documentElement.classList.contains('wd-lite'))){cv.preload='auto';cv.load();try{cv.currentTime=ov?ov.currentTime:0;}catch(x){}const p=cv.play();p&&p.catch(()=>{});}}el.setAttribute('aria-hidden','true');
    Object.assign(el.style,{left:f.x+'px',top:f.y+'px',width:f.w+'px',height:f.h+'px',aspectRatio:'auto'});
    return {el,f};
  }
  function fromRect(f){return `translate(${f.r.left-f.x}px,${f.r.top-f.y}px) scale(${f.r.width/f.w},${f.r.height/f.h})`;}
  function show(i,dir){
    i=(i+items.length)%items.length;
    const {el,f}=build(i), old=node;
    if(dir){el.style.transition='none';el.style.opacity='0';el.style.transform=`translateX(${dir*60}px)`;}
    stage.append(el);node=el;idx=i;
    count.textContent=String(i+1).padStart(2,'0')+' / '+String(items.length).padStart(2,'0');
    if(old){old.style.transform=`translateX(${-(dir||1)*60}px)`;old.style.opacity='0';setTimeout(()=>old.remove(),reduce?0:350);}
    requestAnimationFrame(()=>requestAnimationFrame(()=>{el.style.transition='';el.style.opacity='1';el.style.transform='none';}));
  }
  function open(i){
    last=document.activeElement;
    document.documentElement.classList.add('case-lb-on');
    lb.classList.add('open');lb.setAttribute('aria-hidden','false');
    const {el,f}=build(i);idx=i;node=el;
    el.style.transition='none';el.style.transform=reduce?'none':fromRect(f);
    stage.append(el);
    count.textContent=String(i+1).padStart(2,'0')+' / '+String(items.length).padStart(2,'0');
    requestAnimationFrame(()=>requestAnimationFrame(()=>{el.style.transition='';el.style.transform='none';}));
    setTimeout(()=>{lb.classList.add('ready');lb.querySelector('.case-lb-close').focus({preventScroll:true});},reduce?0:380);
  }
  function close(){
    if(!lb.classList.contains('open'))return;
    lb.classList.remove('ready');
    const el=node, f=fit(items[idx]);
    if(el&&!reduce){el.style.transform=fromRect(f);}
    lb.classList.remove('open');
    setTimeout(()=>{stage.replaceChildren();node=null;lb.setAttribute('aria-hidden','true');document.documentElement.classList.remove('case-lb-on');last&&last.focus&&last.focus({preventScroll:true});},reduce?0:550);
  }
  const prep=()=>{refresh();items.forEach((m,i)=>{m.setAttribute('role','button');m.tabIndex=0;m.setAttribute('aria-label','Ver imagem '+(i+1)+' em tela cheia');});};
  prep();window.wdLbRefresh=prep;
  document.addEventListener('click',e=>{const m=e.target.closest&&e.target.closest('.track .m');if(!m)return;refresh();open(items.indexOf(m));});
  document.addEventListener('keydown',e=>{const m=e.target.closest&&e.target.closest('.track .m');if(!m||lb.classList.contains('open'))return;if(e.key==='Enter'||e.key===' '){e.preventDefault();refresh();open(items.indexOf(m));}});
  lb.querySelector('.case-lb-close').addEventListener('click',close);
  lb.querySelector('.case-lb-bg').addEventListener('click',close);
  stage.addEventListener('click',e=>{if(e.target===stage)close();});
  lb.querySelector('.case-lb-prev').addEventListener('click',()=>show(idx-1,-1));
  lb.querySelector('.case-lb-next').addEventListener('click',()=>show(idx+1,1));
  addEventListener('keydown',e=>{
    if(!lb.classList.contains('open'))return;
    if(e.key==='Escape'){e.preventDefault();close();}
    else if(e.key==='ArrowRight'){e.preventDefault();show(idx+1,1);}
    else if(e.key==='ArrowLeft'){e.preventDefault();show(idx-1,-1);}
    else if([' ','PageDown','PageUp','ArrowDown','ArrowUp','Home','End'].includes(e.key))e.preventDefault();
    else if(e.key==='Tab'){const f=[...lb.querySelectorAll('button')];const a=f.indexOf(document.activeElement);e.preventDefault();f[(a+(e.shiftKey?-1:1)+f.length)%f.length].focus();}
  });
  // com a tela cheia aberta a página de trás não rola
  lb.addEventListener('wheel',e=>e.preventDefault(),{passive:false});
  lb.addEventListener('touchmove',e=>e.preventDefault(),{passive:false});
  // deslizar para os lados troca de imagem no celular
  let sx=null;
  lb.addEventListener('touchstart',e=>{sx=e.touches[0].clientX;},{passive:true});
  lb.addEventListener('touchend',e=>{if(sx===null)return;const dx=e.changedTouches[0].clientX-sx;sx=null;if(Math.abs(dx)>50)show(idx+(dx<0?1:-1),dx<0?1:-1);});
  addEventListener('resize',()=>{if(node&&lb.classList.contains('open')){const f=fit(items[idx]);Object.assign(node.style,{left:f.x+'px',top:f.y+'px',width:f.w+'px',height:f.h+'px'});}});
})();
</script>
<!-- cursor_css_done --><style>/* Cursor desenhado pelo sistema (sem atraso). O círculo com texto continua só sobre os cards. */
@media not all and (pointer: coarse){html,html body,html body *{cursor:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2216%22%20height%3D%2216%22%3E%3Ccircle%20cx%3D%228%22%20cy%3D%228%22%20r%3D%225.5%22%20fill%3D%22%23F2EEF8%22%20stroke%3D%22%23121316%22%20stroke-opacity%3D%22.45%22/%3E%3C/svg%3E") 8 8,auto!important}html body a,html body a *,html body button,html body button *,html body [role=button],html body label,html body .svc:not(.is-open),html body .svc:not(.is-open) *{cursor:url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A//www.w3.org/2000/svg%22%20width%3D%2240%22%20height%3D%2240%22%3E%3Cdefs%3E%3ClinearGradient%20id%3D%22g%22%20x1%3D%220%22%20y1%3D%220%22%20x2%3D%221%22%20y2%3D%221%22%3E%3Cstop%20offset%3D%220%22%20stop-color%3D%22%236025E1%22/%3E%3Cstop%20offset%3D%221%22%20stop-color%3D%22%23C00252%22/%3E%3C/linearGradient%3E%3C/defs%3E%3Ccircle%20cx%3D%2220%22%20cy%3D%2220%22%20r%3D%2219.3%22%20fill%3D%22none%22%20stroke%3D%22%23fff%22%20stroke-opacity%3D%22.55%22%20stroke-width%3D%221%22/%3E%3Ccircle%20cx%3D%2220%22%20cy%3D%2220%22%20r%3D%2217.8%22%20fill%3D%22url%28%23g%29%22%20fill-opacity%3D%22.45%22%20stroke%3D%22url%28%23g%29%22%20stroke-width%3D%222%22/%3E%3Ccircle%20cx%3D%2220%22%20cy%3D%2220%22%20r%3D%223%22%20fill%3D%22%23F7F6FB%22/%3E%3C/svg%3E") 20 20,pointer!important}html body input,html body textarea{cursor:text!important}html.wd-big,html.wd-big body,html.wd-big body *{cursor:none!important}}.wd-cursor:not(.big),.cursor:not(.big){opacity:0!important}.wd-cursor.big,.cursor.big{background:linear-gradient(135deg,#6025E1,#C00252)!important;color:#fff!important;box-shadow:none!important;border:0!important;outline:0!important}</style>
<style>/* Modo leve (GPU fraca): sem desfoque por trás dos painéis — fundos mais opacos no lugar; luz de fundo parada */
html.wd-lite *,html.wd-lite *::before,html.wd-lite *::after{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}html.wd-lite .site-nav::before{background:rgba(18,19,22,.93)!important}html.wd-lite .dropdown{background:rgba(28,22,42,.97)!important}html.wd-lite .site-nav.wd-nav-open .nav-links{background:rgba(36,18,62,.97)!important}html.wd-lite .wd-contact-glass{background:rgba(18,19,22,.95)!important}html.wd-lite .wd-contact-backdrop{background:rgba(10,10,14,.55)!important}html.wd-lite .light-field-inner::before,html.wd-lite .light-field-inner::after,html.wd-lite .light-field-inner{animation:none!important}html.wd-lite .svc{--card:linear-gradient(125deg,rgba(96,37,225,.16),rgba(49,22,78,.26)),rgba(20,20,26,.94)}html.wd-lite .orb,html.wd-lite .orb2,html.wd-lite .orb::after{animation:none!important}</style>
<style>/* Responsivo (todas as páginas) */
html,body{overflow-x:clip}@media(min-width:981px) and (max-width:1180px){.site-header .site-nav{grid-template-columns:auto minmax(0,1fr) auto;gap:16px}.site-header .nav-links{gap:clamp(14px,2.1vw,28px)}.site-header .wd-nav-actions{gap:14px}}</style>
<script>
/* Pausar animações (WCAG 2.2.2): para animações em CSS, esconde as animações em canvas e pausa os vídeos automáticos */
(function(){
  const root=document.documentElement, btn=document.querySelector('[data-wd-pause]');
  let on=false; try{on=localStorage.getItem('wdPaused')==='1';}catch(e){}
  const auto=v=>!v.classList.contains('vm-video')&&!v.closest('.case-lb');
  function apply(){root.classList.toggle('wd-paused',on);btn&&btn.setAttribute('aria-pressed',String(on));
    if(on)document.querySelectorAll('video').forEach(v=>{if(auto(v))v.pause();});}
  document.addEventListener('play',e=>{if(on&&e.target.tagName==='VIDEO'&&auto(e.target))e.target.pause();},true);
  btn&&btn.addEventListener('click',()=>{on=!on;try{localStorage.setItem('wdPaused',on?'1':'0');}catch(e){}apply();});
  window.wdIsPaused=()=>on;
  apply();
})();
</script>
<?php wp_footer(); ?>
</body>
</html>
