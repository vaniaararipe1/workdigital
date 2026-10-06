<?php if (!defined('ABSPATH')) exit; ?><!doctype html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" type="image/svg+xml" href="<?php echo WD_URI; ?>/img/inline/1b99465de9a2.svg">
<script>/* wd-lite */(function(){var lite=false;try{if(/[?&]lite=1/.test(location.search))lite=true;if(!/[?&]lite=0/.test(location.search)){var cv=document.createElement("canvas"),g=cv.getContext("webgl");var e=g&&g.getExtension("WEBGL_debug_renderer_info"),r=e?String(g.getParameter(e.UNMASKED_RENDERER_WEBGL)):"";if(!g||/SwiftShader|llvmpipe|softpipe|Basic Render|Intel\(R\) (HD Graphics( [2-5]\d{3})?|Q?G\d+)\b|GMA/i.test(r))lite=true;var lc=g&&g.getExtension("WEBGL_lose_context");lc&&lc.loseContext();if((navigator.hardwareConcurrency||8)<=2)lite=true;}}catch(x){}if(lite)document.documentElement.classList.add("wd-lite");window.WD_LITE=lite;})();(function(){try{if(!location.hash){history.scrollRestoration="manual";var top=function(){scrollTo(0,0)};top();addEventListener("DOMContentLoaded",top,{once:true});addEventListener("load",function(){requestAnimationFrame(top)},{once:true});}}catch(e){}document.addEventListener("click",function(e){var a=e.target.closest&&e.target.closest(".site-nav a[href='#'],.site-nav a[href='#topo'],.site-nav a[href='#top'],.site-nav a[href='#hero']");if(!a)return;e.preventDefault();scrollTo({top:0,behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth"});try{history.replaceState(null,"",location.pathname+location.search)}catch(x){}});})();</script>

<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Nunito:wght@400;600&display=swap">
<style>
:root{
  --bg:#121316;
  --bg-deep:#16171B;
  --ink:#f6f6f8;
  --muted:#a7abae;
  --purple:#6025E1;
  --green:#04CD8F;
  --wine:#C00252;
}
*{box-sizing:border-box}
html{background:var(--bg);color:var(--ink);scroll-behavior:smooth}
body{margin:0;font-family:"Space Grotesk",system-ui,sans-serif;background:var(--bg);overflow-x:hidden}
a{color:inherit}
button{font:inherit}

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

/* HERO */
.hero-scroll{height:340vh;position:relative;background:var(--bg)}
.hero-sticky{position:sticky;top:0;height:100vh;overflow:hidden;isolation:isolate;background:
  radial-gradient(72vw 62vw at 12% 10%,rgba(96,37,225,.34),transparent 60%),
  radial-gradient(56vw 52vw at 88% 18%,rgba(192,2,82,.20),transparent 62%),
  radial-gradient(60vw 54vw at 18% 92%,rgba(4,205,143,.14),transparent 64%),
  linear-gradient(135deg,#16171B 0%,#121316 46%,#0E0F12 100%)}
.hero-sticky::before{content:"";position:absolute;inset:0;z-index:1;background:radial-gradient(120% 140% at 52% 46%, transparent 0%, rgba(0,0,0,.04) 50%, rgba(0,0,0,.18) 100%)}
.noise{position:absolute;inset:0;z-index:1;pointer-events:none;opacity:.028;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E")}
.canvas-wrap{position:absolute;inset:0;z-index:6;pointer-events:none}
#particleCanvas{width:100%;height:100%;display:block}

.stage{position:absolute;inset:0;z-index:5;padding:clamp(98px,13vh,150px) clamp(24px,6vw,88px);will-change:transform,opacity,filter}
.shell{max-width:1180px;height:100%;margin:0 auto;position:relative}

.intro{opacity:1}
.intro .shell{display:flex;align-items:center;justify-content:center;text-align:center}
.intro-block{max-width:680px;position:relative;z-index:7}
.intro-title{margin:0;line-height:1;letter-spacing:-.04em;font-weight:500;text-transform:none}
.intro-title span{display:block}
.intro-desc{margin:28px auto 0;max-width:600px;font-size:16px;line-height:1.4;color:#bbc7c6}
.hero-cta{display:inline-flex;align-items:center;justify-content:center;gap:10px;margin-top:28px;height:52px;padding:0 22px;border-radius:6px;background:linear-gradient(90deg,#CBFFFC 0%,#EDFFFE 26.25%,#FFFDFA 47.57%,#FAD1FF 88.96%);background-size:180% 100%;background-position:0% 50%;color:#222;font-size:14px;line-height:1;text-transform:uppercase;border:0;transition:background-position .55s cubic-bezier(.22,1,.36,1),color .3s ease}
.hero-cta span{transition:transform .35s ease}
.hero-cta:hover{background-position:100% 50%;color:#111}
.hero-cta:hover span{transform:translate(3px,-3px)}

.statement{opacity:0;z-index:4}
.statement .shell{display:flex;align-items:center;justify-content:center;text-align:center;max-width:none}
.statement-main{margin:0;width:100%;font-size:clamp(78px,14.2vw,210px);line-height:1;letter-spacing:-.046em;font-weight:500;text-transform:none}
.statement-line{display:flex;justify-content:center;overflow:visible;padding:.12em .06em}
.statement-line .char{display:inline-block;opacity:0;transform:translate3d(0,1.08em,0) rotateX(18deg);transform-origin:50% 100%;will-change:transform,opacity}
.payoff{opacity:0}
.payoff .shell{display:flex;align-items:center;justify-content:center;text-align:center}
.payoff-block{max-width:760px;padding:0}
.payoff-copy{margin:0;font-size:clamp(30px,3.25vw,48px);line-height:1;letter-spacing:-.04em;font-weight:500;color:#fff}
.payoff-copy span{display:block}

.after{min-height:70vh;background:#f1eef9}

@media(max-width:980px){
  .nav-links,.lang,.nav-cta{display:none}
  .site-nav{height:64px;border-radius:17px;padding-right:10px}
  .brand img{width:132px}
  .mobile-toggle{display:flex}
  .site-header{top:12px;padding-inline:12px}
}
@media(max-width:760px){
  .hero-scroll{height:300vh}
  .hero-sticky{height:100svh}
  .stage{padding:96px 22px 52px}
  .intro .shell{align-items:end}
  .intro-block{max-width:100%;padding-bottom:92px}
  .intro-title{font-size:clamp(48px,13vw,68px)}
  .intro-desc{max-width:95%;font-size:16px}
  .statement-main{font-size:clamp(66px,19vw,108px);line-height:1}
  .payoff .shell{align-items:end}
  .payoff-block{max-width:88%;padding-bottom:46px}
  .payoff-copy{font-size:clamp(28px,8vw,36px);line-height:1}
}
@media(prefers-reduced-motion:reduce){
  .hero-scroll{height:auto}
  .hero-sticky{position:relative;min-height:100vh}
  .stage{position:relative;min-height:100vh;opacity:1!important;transform:none!important;filter:none!important}
  .statement-line>span{transform:none!important}
}

/* Motion revision: normal document flow and opposing scroll-linked lines. */
.hero-scroll{height:auto;overflow:clip}
.hero-sticky{position:relative;height:auto;overflow:visible}
.noise{position:absolute}
.canvas-wrap{position:absolute;top:30vh;height:125svh;inset-inline:0;z-index:2}
.stage{position:relative;inset:auto;opacity:1;transform:none;filter:none;will-change:auto}
.intro{min-height:160svh;padding:clamp(180px,24vh,250px) 24px 80px;z-index:5}
.intro .shell{height:auto;display:block}
.intro-block{max-width:820px;margin:auto}
.intro-title{line-height:1;letter-spacing:-.045em}
.intro-desc{margin:48px auto 0;max-width:720px;font-size:clamp(17px,1.5vw,22px);line-height:1.4}
.hero-cta{margin-top:48px}
.statement{padding:0;z-index:5}
.statement .shell{display:block;height:auto;max-width:none}
.statement-main{font-size:clamp(86px,18.2vw,320px);line-height:1;letter-spacing:-.045em;text-align:left}
.statement-line{display:block;padding:.04em 0;overflow:visible;white-space:nowrap}
.statement-line>span{display:inline-block;will-change:transform}
.payoff{padding:clamp(140px,19vh,260px) 4.5vw;min-height:76vh;display:flex;align-items:center;z-index:5}
.payoff .shell{height:auto;width:100%;display:block}
.payoff-block{max-width:1440px;margin:auto}
.payoff-copy{font-size:clamp(42px,5.2vw,96px);line-height:1;letter-spacing:-.045em}
.payoff-copy span{--from:#6025E1;--to:#04CD8F;background:linear-gradient(90deg,var(--from),var(--to));background-clip:text;-webkit-background-clip:text;color:transparent;padding-bottom:.06em}
@media(max-width:760px){
 .intro{min-height:145svh;padding:180px 24px 70px}
 .intro-block{padding:0}
 .intro-title{font-size:clamp(40px,10.6vw,68px)}
 .intro-desc{max-width:100%;margin-top:32px}
 .hero-cta{margin-top:32px;font-size:12px;padding-inline:16px}
 .canvas-wrap{top:40svh;height:100svh}
 .statement-main{font-size:25vw}
 .payoff{min-height:76svh;padding:120px 24px}
 .payoff-block{max-width:100%;padding:0}
 .payoff-copy{font-size:clamp(36px,8.8vw,62px)}
}
@media(prefers-reduced-motion:reduce){
 .intro{min-height:100svh}
 .statement{min-height:0}
 .statement-main{font-size:clamp(48px,13vw,180px);text-align:center}
 .statement-line>span{transform:none!important}
 .payoff{min-height:70svh}
 .payoff-copy span{color:var(--ink);background:none}
 .canvas-wrap{display:none}
}

/* Work light field: a viewport-sized layer follows the whole hero sequence. */
.hero-sticky{background:#121316}
.hero-sticky::before,.hero-sticky::after{display:none}
.light-field{position:absolute;inset:0;z-index:0;pointer-events:none}
.light-field-inner{position:sticky;top:0;height:100svh;overflow:hidden;background:#121316}
.light-field-inner::before{content:"";position:absolute;left:-20%;top:-20%;width:35%;height:35%;transform-origin:0 0;transform:scale(4);background:
 radial-gradient(ellipse at 24% 42%,rgba(96,37,225,.92),transparent 44%),
 radial-gradient(ellipse at 78% 60%,rgba(237,72,151,.82),transparent 40%),
 radial-gradient(ellipse at 60% 84%,rgba(4,205,143,.32),transparent 34%),
 radial-gradient(ellipse at 42% 68%,rgba(150,72,253,.48),transparent 45%);
 animation:lightFieldDrift 22s ease-in-out infinite alternate;will-change:transform}
.light-field-inner::after{content:"";position:absolute;inset:0;background:radial-gradient(ellipse at 50% 24%,rgba(18,19,22,.26),transparent 63%)}
@keyframes lightFieldDrift{from{transform:scale(4) translate3d(-4%,-3%,0) scale(1)}to{transform:scale(4) translate3d(5%,4%,0) scale(1.10)}}
.noise{opacity:.018}
.statement-line:last-child{color:inherit}
.statement-line>span{background:linear-gradient(108deg,rgba(220,244,235,.76) 0%,rgba(232,220,255,.78) 30%,rgba(178,137,245,.76) 65%,rgba(216,145,177,.70) 100%);background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent;opacity:1;text-shadow:none;filter:none}
.canvas-wrap{top:43svh;height:115svh}
#particleFallback{position:absolute;inset:0;width:100%;height:100%;display:block}
.canvas-wrap.has-webgl #particleFallback{display:none}
@media(max-width:760px){.canvas-wrap{top:50svh;height:95svh}}
@media(prefers-reduced-motion:reduce){.light-field-inner::before{animation:none}.canvas-wrap{display:block;opacity:.75}}

/* Review corrections: quiet dropdown, complete kinetic phrases and real particle art. */
.site-nav{position:relative;isolation:isolate;background:transparent;backdrop-filter:none;-webkit-backdrop-filter:none}
.site-nav::before{content:"";position:absolute;inset:0;border-radius:inherit;background:rgba(18,19,22,.58);backdrop-filter:blur(22px) saturate(155%);-webkit-backdrop-filter:blur(22px) saturate(155%);z-index:-1;pointer-events:none}
.dropdown{background:rgba(28,22,42,.28);backdrop-filter:blur(36px) saturate(145%);-webkit-backdrop-filter:blur(36px) saturate(145%);border:1px solid rgba(255,255,255,.14);box-shadow:0 22px 60px rgba(0,0,0,.20)}
.dropdown a{display:flex;gap:0;padding:16px 18px;min-height:68px}
.hero-cta,.hero-cta:hover,.hero-cta:focus-visible{text-decoration:none}
.statement-main{font-size:clamp(64px,15.5vw,270px);line-height:1.08}
.statement-line{padding:.08em 0}
.statement-line>span{padding-right:.03em}
.payoff-copy{font-size:clamp(36px,4.65vw,80px);line-height:1.08}
.payoff-copy span{white-space:nowrap}
.canvas-wrap{top:34svh;height:120svh;z-index:2;mix-blend-mode:screen}
.particle-art{position:absolute;inset:0;--pointer-x:0px;--pointer-y:0px;transform:translate3d(var(--pointer-x),var(--pointer-y),0)}
.particle-art img{display:block;position:absolute;width:min(100%,1500px);height:auto;left:50%;top:50%;transform:translate(-50%,-50%);filter:hue-rotate(90deg) saturate(.90) brightness(.96)}
.particle-art canvas{position:absolute;inset:0;width:100%;height:100%;filter:hue-rotate(90deg) saturate(.9) brightness(.96)}
.particle-art.has-live-particles img{visibility:hidden}
.intro{pointer-events:none}.intro-block{pointer-events:auto}
.canvas-wrap{pointer-events:auto}
@media(max-width:760px){
 .statement-main{font-size:19.5vw}
 .payoff-copy{font-size:clamp(24px,5.5vw,42px)}
 .payoff{padding-inline:20px}
 .canvas-wrap{top:42svh;height:100svh}
 .particle-art img{width:175%;max-width:none}
}
@media(prefers-reduced-motion:reduce){.particle-art img{animation:none}.particle-art{transform:none}}
.intro-desc{max-width:1000px;font-size:clamp(16px,1.4vw,22px)}
.intro-desc>span{display:block;white-space:nowrap}
.native-particles{position:absolute;left:0;right:0;top:calc((100% - 117vw)/2);height:117vw}
.particle-art .native-particles canvas{filter:none}
.particle-art.has-native-particles>canvas,.particle-art.has-native-particles>img{visibility:hidden}
@media(max-width:760px){.intro-desc{max-width:95%;font-size:17px}.intro-desc>span{display:contents;white-space:normal}}
.canvas-wrap{overflow:visible}
.native-particles{position:absolute;left:0;right:0;top:-29vw;height:117vw}
/* Compact transition from Be digital to the business statement. */
.payoff{min-height:0;padding:clamp(32px,4vw,64px) 4.5vw 96px;align-items:flex-start}
@media(max-width:760px){.payoff{min-height:0;padding:32px 20px 64px}}
/* Área compacta: metade do espaço anteriormente reservado à nuvem. */
.canvas-wrap{height:170vh;overflow:hidden;background:transparent}
.particle-art{transform:none}
.native-particles{position:absolute;inset:0;height:100%}
.particle-art canvas{display:block;width:100%;height:100%}
@media(max-width:760px){.canvas-wrap{height:170vh}}

/* Two lines retain the existing font size and use more of the section width. */
.payoff{padding-inline:clamp(12px,1.5vw,24px)}
.payoff .shell,.payoff-block{width:100%;max-width:none}
</style>
<link rel="stylesheet" href="<?php echo WD_URI; ?>/wd-revision.css?v=20261003-shared-hover">
<!-- Contact layers must be styled before contact.js inserts them above the nav. -->
<link rel="stylesheet" href="<?php echo WD_URI; ?>/contact.css?v=20261003-contact-minimal">
<style>html.wd-lite .particle-art{display:none!important}</style>
<style>a.wd-works-card{color:inherit;text-decoration:none}</style>
<style>
/* Thumbs: pôster + versão animada no hover (aparece com fade quando começa a tocar) */
.vm{position:absolute;inset:0;overflow:hidden;transition:transform 1.1s cubic-bezier(.22,1,.36,1)}
.vm img,.vm video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.vm video,.vm .vm-anim{opacity:0;transition:opacity .25s ease}
.vm.vm-on video,.vm.vm-on .vm-anim{opacity:1}
/* enquanto a animação carrega: brilho que percorre a base do card */
.vm .vm-load{position:absolute;left:0;right:0;bottom:0;height:2px;z-index:3;opacity:0;pointer-events:none;background:linear-gradient(90deg,transparent,#cbb6ff,#f5c3d8,transparent);background-size:40% 100%;background-repeat:no-repeat}
.vm.vm-wait:not(.vm-on) .vm-load{opacity:1;animation:vmLoad 1s linear infinite}
@keyframes vmLoad{from{background-position:-40% 0}to{background-position:140% 0}}
/* inclinação 3D + reflexo de luz que segue o mouse */
.wd-tilt-host{transform-style:preserve-3d;will-change:transform;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.wd-tilt-host.wd-tilting{transition:transform .12s linear}
.wd-glare{position:absolute;inset:0;z-index:4;pointer-events:none;border-radius:inherit;opacity:0;transition:opacity .4s ease;mix-blend-mode:soft-light;background:radial-gradient(circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.55),rgba(203,182,255,.18) 28%,transparent 60%)}
.wd-tilting .wd-glare{opacity:1}

.wd-works-section .wd-works-grid{grid-template-rows:auto auto}
.wd-works-section .wd-works-card:nth-child(n){min-height:0;background:#1d0f36;color:#fff}
.wd-works-section .wd-works-card:nth-child(n):not(:first-child){aspect-ratio:var(--wd-ar)}
.wd-works-section .wd-works-card:nth-child(n) .wd-works-media{position:absolute;inset:0;align-self:stretch;justify-self:stretch;height:auto;z-index:0;max-width:none;width:auto;aspect-ratio:auto;border:0;border-radius:inherit;background:#1d0f36}
.wd-works-section .wd-works-card::after{content:"";position:absolute;inset:0;z-index:1;pointer-events:none;border-radius:inherit;background:linear-gradient(180deg,rgba(20,8,40,.62) 0%,rgba(20,8,40,0) 22%,rgba(20,8,40,0) 62%,rgba(20,8,40,.86) 100%)}
.wd-works-section .wd-works-dots{display:none}
.wd-works-section .wd-works-card h3{color:#fff;text-shadow:0 2px 18px rgba(10,4,24,.45)}
.wd-works-section .wd-works-card:nth-child(n) .wd-works-description{color:#ece8f5;max-width:34ch;text-shadow:0 1px 12px rgba(10,4,24,.5)}
.wd-works-card:hover .wd-works-media .vm,.wd-works-card:focus-visible .wd-works-media .vm{transform:scale(1.045)}
.wd-works-section .wd-works-card.wd-tilt-host.wd-works-visible,.wd-works-section .wd-works-card.wd-tilt-host:not(.wd-works-entering){transition:transform .6s cubic-bezier(.22,1,.36,1),opacity .8s}
.wd-works-section .wd-works-card.wd-tilt-host.wd-tilting{transition:transform .12s linear}
.wd-works-section .wd-works-card .wd-glare{z-index:3}
@media (max-width:1180px){.wd-works-section .wd-works-card:nth-child(n){padding:26px}.wd-works-section .wd-works-card h3{font-size:30px}.wd-works-section .wd-works-card:nth-child(n) .wd-works-description{font-size:15px}}
/* 2 colunas: mesma ideia — Bacio alto à esquerda, STW e CBPq empilhados à direita, Linea larga embaixo */
@media (max-width:991px){
 .wd-works-section .wd-works-grid{grid-template-rows:auto auto auto}
 .wd-works-section .wd-works-card:nth-child(1){grid-column:1;grid-row:1 / span 2}
 .wd-works-section .wd-works-card:nth-child(3){grid-column:2;grid-row:1}
 .wd-works-section .wd-works-card:nth-child(4){grid-column:2;grid-row:2}
 .wd-works-section .wd-works-card:nth-child(2){grid-column:1 / span 2;grid-row:3}
}
/* 1 coluna: cada card na proporção da própria arte */
@media (max-width:599px){
 .wd-works-section .wd-works-grid{grid-template-columns:minmax(0,1fr);grid-template-rows:none}
 .wd-works-section .wd-works-card:nth-child(n){grid-column:1;grid-row:auto;aspect-ratio:var(--wd-ar);padding:22px 20px}
 .wd-works-section .wd-works-card:nth-child(1){max-height:none}
 .wd-works-section .wd-works-card:nth-child(n):nth-child(2){aspect-ratio:auto;padding:0;gap:0;justify-content:flex-start}
 .wd-works-section .wd-works-card:nth-child(n):nth-child(2) .wd-works-media{flex-shrink:0;position:relative;inset:auto;order:-1;aspect-ratio:var(--wd-ar);border-radius:0}
 .wd-works-section .wd-works-card:nth-child(2) h3{position:absolute;top:18px;left:20px}
 .wd-works-section .wd-works-card:nth-child(2)::after{background:linear-gradient(180deg,rgba(20,8,40,.62) 0%,rgba(20,8,40,0) 30%)}
 .wd-works-section .wd-works-card:nth-child(2) .wd-works-description{padding:18px 20px 22px}
}
</style>
<style>
/* Blog da home: 3 artigos mais recentes */
@media (max-width:991px) and (min-width:700px){.wd-blog-section .wd-blog-list{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}.wd-blog-section .wd-blog-link{padding:18px 18px 32px;gap:24px 12px}}
</style>
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<a class="wd-skip" href="#conteudo">Pular para o conteúdo</a>
<div class="light-field" aria-hidden="true"><div class="light-field-inner"></div></div>
<header class="site-header">
  <nav class="site-nav" aria-label="Navegação principal">
    <a class="brand" href="#hero" aria-label="Work Digital — Home">
      <img src="<?php echo WD_URI; ?>/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg" alt="Work Digital">
    </a>
    <div class="nav-links">
      <a class="nav-link" href="#hero">Home</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('solucoes/')); ?>">Soluções</a>
      <a class="nav-link" href="<?php echo esc_url(wd_url('cases/')); ?>">Works</a>
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

<main id="conteudo" tabindex="-1">
  <section class="hero-scroll" id="hero">
    <div class="hero-sticky">
      
      <div class="noise"></div>
      <div class="canvas-wrap" aria-hidden="true"><div class="particle-art webgpu-container"><img src="<?php echo WD_URI; ?>/img/inline/3a818cc49dab.webp" alt="" aria-hidden="true" width="1600" height="1280"></div></div>

      <section class="stage intro" id="intro">
        <div class="shell">
          <div class="intro-block">
            <h1 class="intro-title wd-uptitle"><span>Criação de sites</span> <br><span>profissionais</span></h1>
            <p class="intro-desc wd-section-desc"><span>Somos uma empresa especializada em criação de sites em WordPress,</span> <span>landing pages e lojas virtuais, focados em geração de leads e alta performance.</span></p>
            <a class="hero-cta wd-cta" href="<?php echo esc_url(wd_url('cases/')); ?>">CONHEÇA NOSSO PORTFOLIO <span>↗</span></a>
          </div>
        </div>
      </section>

      <section class="stage statement" id="statement">
        <div class="shell">
          <h2 class="statement-main">
            <span class="statement-line"><span>Be beyond.</span></span>
            <span class="statement-line"><span>Be digital.</span></span>
          </h2>
        </div>
      </section>

      <section class="stage payoff" id="payoff">
        <div class="shell">
          <div class="payoff-block">
            <p class="payoff-copy"><span>O site da sua empresa precisa ser</span><span>um gerador de novos negócios</span></p>
          </div>
        </div>
      </section>
    </div>
  </section>
  
<style>
/* A única camada de luz é compartilhada por header, hero e Explore. */
body{isolation:isolate}
.hero-scroll,.hero-sticky{background:transparent}
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
@media(max-width:760px){}
@media(prefers-reduced-motion:reduce){.light-field-inner::before{animation:none}}

.wd-explore-section{
 --wd-explore-bg:#121316;--wd-explore-ink:#f7f6fb;
 --wd-explore-copy:#c8c4d3;--wd-explore-accent:#6025e1;
 --wd-explore-surface:rgba(96,37,225,.5);
 --wd-explore-panel:rgba(29,14,54,.5);
 --wd-explore-font:"Space Grotesk",Arial,sans-serif;
 --wd-explore-gap:56px;--wd-explore-panel-padding:48px;--wd-explore-card-padding:32px 22px;
 --wd-explore-ease:cubic-bezier(.22,1,.36,1);
 padding:96px 3vw;background:transparent;
 color:var(--wd-explore-ink);font-family:var(--wd-explore-font);
}
.wd-explore-section *{box-sizing:border-box}
.wd-explore-layout{position:relative;max-width:1440px;margin:auto;
 display:grid;grid-template-columns:1fr 1fr;gap:var(--wd-explore-gap);padding:var(--wd-explore-panel-padding);
 border-radius:8px;isolation:isolate;overflow:hidden;
 background:transparent;
}
.wd-explore-heading{margin:0 0 31px;padding:0 22px;
 font-size:20px;line-height:1.4;letter-spacing:.2em;font-weight:500;
 text-transform:uppercase;max-width:500px;}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .wd-explore-heading{;}
}
.wd-explore-subtitle{margin:0 0 64px;padding:0 22px}
.wd-explore-list{grid-column:1;min-width:0;padding:40px 20px;border-radius:12px;background:var(--wd-explore-panel)}
.wd-explore-card{display:block;padding:var(--wd-explore-card-padding);border-radius:8px;
 color:inherit;text-decoration:none;transition:background .6s var(--wd-explore-ease)}

.wd-explore-card:focus-visible,.wd-explore-cta:focus-visible{
 outline:2px solid #bda4ff;outline-offset:5px}
.wd-explore-card-title{display:flex;align-items:flex-start;justify-content:space-between;gap:24px}
.wd-explore-card h3{margin:0;font-size:clamp(30px,2.6vw,38px);
 line-height:1;letter-spacing:-.035em;font-weight:500}
.wd-explore-arrow{display:grid;place-items:center;flex:0 0 40px;
 width:40px;height:40px;border-radius:8px;background:rgba(255,255,255,.05);
 font:28px/1 Arial,sans-serif;transition:background .6s var(--wd-explore-ease)}
.wd-explore-card.is-active .wd-explore-arrow,.wd-explore-card:hover .wd-explore-arrow,.wd-explore-card:focus-visible .wd-explore-arrow{background:rgba(96,37,225,.35)}
.wd-explore-card p{margin:28px 0 0;font-family:"Nunito",system-ui,sans-serif;font-size:clamp(16px,1.27vw,18px);
 line-height:1.6;font-weight:400;color:var(--wd-explore-copy)}
.wd-explore-image{position:absolute;left:calc(50% + 28px);right:48px;top:200px;
 aspect-ratio:16/10;display:block;overflow:hidden;border-radius:8px;
 background:#211832;opacity:0;pointer-events:none;z-index:2;
 clip-path:inset(100% 0 0 0);transition:opacity .6s var(--wd-explore-ease),clip-path .6s var(--wd-explore-ease)}
.wd-explore-image img{display:block;width:100%;height:100%;object-fit:cover;
 transform:scale(1.05);transition:transform .6s var(--wd-explore-ease)}
.wd-explore-card:hover .wd-explore-image,.wd-explore-card:focus-visible .wd-explore-image{
 opacity:1;clip-path:inset(0)}
.wd-explore-card:hover .wd-explore-image img,.wd-explore-card:focus-visible .wd-explore-image img{transform:scale(1)}
.wd-explore-visual{grid-column:2;grid-row:1;position:relative;min-height:100%;
 background:radial-gradient(ellipse at 50% 45%,rgba(96,37,225,.24),transparent 70%)}
.wd-explore-default{position:absolute;left:0;right:0;top:152px;aspect-ratio:16/10;
 border:1px solid rgba(189,164,255,.18);border-radius:8px;
 background:linear-gradient(145deg,rgba(96,37,225,.12),rgba(192,2,82,.09));
 display:grid;place-items:center;color:#b8abc9;font-size:14px;letter-spacing:.02em}
.wd-explore-cta{display:flex;align-items:center;justify-content:center;gap:16px;
 width:max-content;max-width:100%;margin-left:auto;min-height:52px;padding:14px 20px;
 border-radius:6px;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;
 border:0;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);
 background-size:280% 100%;background-position:100% 0%;
 transition:background-position 600ms ease,color 200ms ease}
.wd-explore-cta:hover,.wd-explore-cta:focus-visible{background-position:0% 0%;color:#24123e}
.wd-explore-cta-icon{width:14px;height:14px;flex:0 0 14px;color:inherit}
@media(max-width:991px){
 .wd-explore-section{padding:64px 24px}
 .wd-explore-layout{display:flex;flex-direction:column;padding:32px 24px;gap:32px}
 .wd-explore-list{padding:28px 20px}
 .wd-explore-heading{padding:0;font-size:16px;margin-bottom:24px}
 .wd-explore-subtitle{padding:0;margin-bottom:40px}
 .wd-explore-card{padding:16px 12px 32px;margin-bottom:32px;border-radius:8px;
 border-bottom:1px solid rgba(189,164,255,.2)}
 .wd-explore-card:last-child{margin-bottom:0;padding-bottom:0;border-bottom:0}
 
 .wd-explore-image{position:relative;left:auto;right:auto;top:auto;width:100%;
 opacity:1;clip-path:none;margin-bottom:28px;pointer-events:auto}
 .wd-explore-image img{transform:none}
 .wd-explore-card h3,.wd-explore-card:first-child h3{font-size:32px;line-height:1.05}
 .wd-explore-card p{font-size:16px;margin-top:20px;line-height:1.6}
 .wd-explore-visual{min-height:0;background:none}
 .wd-explore-default{display:none}
 .wd-explore-cta{margin:0;white-space:normal}
}
@media(max-width:479px){
 .wd-explore-section{padding:48px 16px}
 .wd-explore-layout{padding:28px 20px}
 .wd-explore-list{padding:24px 12px}
 .wd-explore-subtitle{}
 .wd-explore-card p{font-size:15px}
 .wd-explore-card h3,.wd-explore-card:first-child h3{font-size:30px}
 .wd-explore-arrow{flex-basis:36px;width:36px;height:36px}
}
@media(prefers-reduced-motion:reduce){
 .wd-explore-section *{transition:none!important}
 .wd-explore-image img{transform:none}
}
</style>
<style>
/* Estrutura dos dois retângulos; mantém tipografia, CTA e estados existentes. */
#wd-explore{background:transparent}
#wd-explore .wd-explore-layout{display:block;padding:28px;border-radius:16px;border:1px solid rgba(189,164,255,.13);background:linear-gradient(125deg,rgba(96,37,225,.12),rgba(49,22,78,.2));isolation:isolate;overflow:hidden}
#wd-explore .wd-explore-dots{position:absolute;inset:0;z-index:0;pointer-events:none;border-radius:inherit;background-size:24px 24px,37px 37px;}
#wd-explore .wd-explore-header{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:start;margin-bottom:32px}
#wd-explore .wd-explore-intro{min-width:0;padding:40px 20px 0}
#wd-explore .wd-explore-subtitle{margin-bottom:0}
#wd-explore .wd-explore-header>.wd-explore-cta{align-self:start;margin-top:40px}
#wd-explore .wd-explore-body{position:relative;z-index:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px;align-items:stretch}
#wd-explore .wd-explore-list{grid-column:auto;min-width:0;border-radius:12px;background:linear-gradient(90deg,rgba(29,14,54,0) 0%,rgba(42,17,78,.40) 40%,rgba(70,26,143,.72) 100%)}
#wd-explore .wd-explore-photo{position:relative;min-width:0;min-height:0;margin:0;border-radius:12px;overflow:hidden;background:rgba(96,37,225,.12)}
#wd-explore .wd-explore-photo>img{position:absolute;inset:0;display:block;width:100%;height:100%;object-fit:cover}
/* Mesma revelação dos cards, agora alinhada ao painel fotográfico inteiro. */
@media(min-width:992px){#wd-explore .wd-explore-image{left:calc(50% + 14px);right:0;top:0;bottom:0;aspect-ratio:auto;border-radius:12px;z-index:2}}
@media(max-width:991px){
 #wd-explore .wd-explore-header{grid-template-columns:minmax(0,1fr);gap:24px;margin-bottom:28px}
 #wd-explore .wd-explore-intro{padding:0}
 #wd-explore .wd-explore-header>.wd-explore-cta{margin-top:0}
 #wd-explore .wd-explore-body{grid-template-columns:minmax(0,1fr);gap:28px}
 #wd-explore .wd-explore-photo{width:100%;aspect-ratio:4/3}
}
@media(max-width:479px){#wd-explore .wd-explore-layout{padding:20px}#wd-explore .wd-explore-body{gap:20px}}
</style>
<section class="wd-explore-section" id="wd-explore" aria-labelledby="wd-explore-heading">
 <div class="wd-explore-layout">
  <canvas class="wd-explore-dots" aria-hidden="true"></canvas>
  <div class="wd-explore-header">
   <div class="wd-explore-intro">
   <h2 class="wd-explore-heading wd-uptitle" id="wd-explore-heading">Aceite o desafio do novo</h2>
   <h2 class="wd-explore-subtitle wd-section-title">Soluções Work</h2>
   </div>
   <a class="wd-explore-cta wd-cta" data-wd-contact href="#contato">SOLICITE UMA PROPOSTA <svg class="wd-explore-cta-icon" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12 1 1 12M2 1h10v10" stroke="currentColor" stroke-width="1.4"/></svg></a>
  </div>
  <div class="wd-explore-body">
   <div class="wd-explore-list">
   <a class="wd-explore-card is-active" href="#criacao-de-sites" data-wd-explore-url="https://workdigital.art.br/criacao-de-site/">
    <div class="wd-explore-card-title"><h3>Criação de Sites</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Sites profissionais, personalizados, otimizados, de fácil gerenciamento, tornando o seu negócio visível para milhares de clientes e valorizando sua marca.</p>
   </a>
   <a class="wd-explore-card" href="#criacao-de-blogs" data-wd-explore-url="https://workdigital.art.br/criacao-de-blog/">
    <div class="wd-explore-card-title"><h3>Criação de Blogs</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Criação de blogs profissionais para sua marca acessar todo o poder do marketing de conteúdo. Construa sua audiência na web e seja autoridade em sua área de atuação.</p>
   </a>
   <a class="wd-explore-card" href="#criacao-de-landing-pages" data-wd-explore-url="https://workdigital.art.br/criacao-de-landing-pages/">
    <div class="wd-explore-card-title"><h3>Criação de Landing pages</h3><span class="wd-explore-arrow" aria-hidden="true">↗</span></div>
    <p>Atrair não é o suficiente. É preciso conquistar seu visitante no momento em que ele chega a sua página de vendas. Criamos Landing Pages que convertem e alavancam seus resultados.</p>
   </a>
   </div>
   <figure class="wd-explore-photo" aria-label="Imagens das soluções Work Digital">
    <div class="wd-explore-media is-visible" data-wd-service="0"><video class="wd-explore-video" muted loop playsinline preload="none" poster="<?php echo WD_URI; ?>/media/servico-sites.jpg?v=20261003-media2" aria-label="Animação de Criação de Sites"><source src="<?php echo WD_URI; ?>/media/criacao-de-sites-servico-sites.webm?v=20261003-media2" type="video/webm"></video></div>
    <div class="wd-explore-media" data-wd-service="1"><video class="wd-explore-video" muted loop playsinline preload="none" poster="<?php echo WD_URI; ?>/media/servico-blog.jpg?v=20261003-media2" aria-label="Animação de Criação de Blogs"><source src="<?php echo WD_URI; ?>/media/criacao-de-sites-servico-blog.webm?v=20261003-media2" type="video/webm"></video></div>
    <div class="wd-explore-media" data-wd-service="2"><video class="wd-explore-video" muted loop playsinline preload="none" poster="<?php echo WD_URI; ?>/media/servico-landing-page.jpg?v=20261003-media2" aria-label="Animação de Criação de Landing pages"><source src="<?php echo WD_URI; ?>/media/criacao-de-sites-servico-landing-page.webm?v=20261003-media2" type="video/webm"></video></div>
   </figure>
  </div>
 </div>
</section>
<style>
.wd-works-section{--wd-works-ink:#f7f6fb;--wd-works-copy:#c8c4d3;--wd-works-panel:#29134d;--wd-works-ease:cubic-bezier(.22,1,.36,1);padding:96px 6vw;scroll-margin-top:96px;background:transparent;color:var(--wd-works-ink);font-family:"Space Grotesk",system-ui,sans-serif}
.wd-works-section *{box-sizing:border-box}
.wd-works-container{max-width:1280px;margin:auto}
.wd-works-header{text-align:center;max-width:660px;margin:0 auto 80px}
.wd-works-eyebrow{margin:0 0 31px;font-size:20px;line-height:1.4;letter-spacing:.2em;font-weight:500;text-transform:uppercase;color:#d8c4ff}
.wd-works-title{margin:0;color:#d8c4ff}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .wd-works-eyebrow,.wd-works-title{background:linear-gradient(90deg,#cbb6ff 0%,#efe7ff 26.25%,#fffdfa 47.57%,#f5c3d8 88.96%);-webkit-background-clip:text;background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
}
.wd-works-intro{margin:48px 0 0;font-family:"Nunito",system-ui,sans-serif;font-size:clamp(16px,1.27vw,18px);line-height:1.6;color:var(--wd-works-copy)}
.wd-works-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(2,minmax(380px,auto));gap:20px}
.wd-works-card{position:relative;isolation:isolate;overflow:hidden;min-width:0;padding:36px;border-radius:16px;background:var(--wd-works-panel);display:flex;flex-direction:column;justify-content:space-between;gap:24px}
.wd-works-card:nth-child(1){grid-column:1;grid-row:1 / span 2;background:radial-gradient(41288.31% 255.77% at -42.4% -22.13%,#f5c3d8 0%,#fffdfa 44.72%,#efe7ff 85.38%,#cbb6ff 100%);color:#24123e}
.wd-works-card:nth-child(2){grid-column:2 / span 2;grid-row:1}
.wd-works-card:nth-child(3){grid-column:2;grid-row:2}
.wd-works-card:nth-child(4){grid-column:3;grid-row:2}
.wd-works-card h3{position:relative;z-index:2;margin:0;font-size:clamp(30px,2.6vw,38px);line-height:1;letter-spacing:-.035em;font-weight:500;overflow-wrap:anywhere}
.wd-works-media{position:relative;z-index:2;display:block;align-self:center;width:100%;max-width:320px;aspect-ratio:16 / 10;overflow:hidden;border-radius:8px;border:1px solid rgba(189,164,255,.25);background:rgba(255,255,255,.035)}
.wd-works-media img{display:block;width:100%;height:100%;aspect-ratio:16 / 10;object-fit:cover}
.wd-works-card:first-child .wd-works-media{border-color:rgba(36,18,62,.18);background:rgba(36,18,62,.025)}
.wd-works-description{position:relative;z-index:2;margin:0;font-family:"Nunito",system-ui,sans-serif;font-size:clamp(16px,1.27vw,18px);line-height:1.6;color:var(--wd-works-copy)}
.wd-works-card:first-child .wd-works-description{color:#514261}
.wd-works-dots{position:absolute;inset:0;width:100%;height:100%;z-index:1;pointer-events:none}
.wd-works-card.wd-works-entering{opacity:0;transform:translateY(24px)}
.wd-works-card.wd-works-entering.wd-works-visible{opacity:1;transform:none;transition:opacity .8s var(--wd-works-ease),transform .8s var(--wd-works-ease);transition-delay:var(--wd-works-delay,0ms)}
@media(max-width:991px){
 .wd-works-section{padding:64px 24px}
 .wd-works-header{margin-bottom:48px}
 .wd-works-eyebrow{font-size:16px;margin-bottom:24px}
 .wd-works-title{}
 .wd-works-intro,.wd-works-description{font-size:16px}
 .wd-works-grid{grid-template-columns:repeat(2,minmax(0,1fr));grid-template-rows:none}
 .wd-works-card:nth-child(n){grid-column:auto;grid-row:auto;min-height:380px;padding:28px}
 .wd-works-card h3{font-size:32px;line-height:1.05}
}
@media(max-width:479px){
 .wd-works-section{padding:48px 16px}
 .wd-works-title{}
 .wd-works-intro,.wd-works-description{font-size:15px}
 .wd-works-grid{grid-template-columns:minmax(0,1fr)}
 .wd-works-card:nth-child(n){padding:28px 20px;min-height:360px}
 .wd-works-card h3{font-size:30px}
}
@media(prefers-reduced-motion:reduce){
 .wd-works-section *{animation:none!important;transition:none!important}
 .wd-works-card.wd-works-entering{opacity:1;transform:none}
}
</style>
<section class="wd-works-section" id="wd-works" aria-labelledby="wd-works-title">
 <div class="wd-works-container">
  <header class="wd-works-header">
   <h2 class="wd-works-title wd-section-title" id="wd-works-title">WORKS</h2>
   <p class="wd-works-intro wd-section-desc">Alguns dos projetos que tiramos do papel. Sites, blogs e landing pages feitos sob medida para marcas de diferentes segmentos, cada um pensado para o negócio do cliente.</p>
  </header>
  <div class="wd-works-grid">
   <?php get_template_part('parts/home-works'); ?>
  </div>
 </div>
</section>
<script>
(()=>{
 const section=document.getElementById('wd-works');
 if(!section||section.dataset.wdWorksReady)return;
 section.dataset.wdWorksReady='true';
 const cards=[...section.querySelectorAll('.wd-works-card')];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let entrance;
 if('IntersectionObserver' in window&&!reduced.matches){
  entrance=new IntersectionObserver(entries=>entries.forEach(entry=>{
   if(entry.isIntersecting){entry.target.classList.add('wd-works-visible');entrance.unobserve(entry.target)}
  }),{threshold:.08});
  cards.forEach((card,index)=>{card.style.setProperty('--wd-works-delay',`${index*100}ms`);card.classList.add('wd-works-entering');entrance.observe(card)});
 }
 cards.forEach((card,index)=>{
  const canvas=document.createElement('canvas');canvas.className='wd-works-dots';canvas.setAttribute('aria-hidden','true');card.append(canvas);
  const ctx=canvas.getContext('2d');if(!ctx)return;
  let width=0,height=0,frame=0,active=false,inView=true,x=-200,y=-200,strength=0;
  function draw(){
   frame=0;strength+=(Number(active)-strength)*.12;
   ctx.clearRect(0,0,width,height);ctx.fillStyle=index===0?'#514261':'#bda4ff';
   for(let py=12;py<height;py+=22)for(let px=12;px<width;px+=22){
    const dx=px-x,dy=py-y,distance=Math.hypot(dx,dy);
    const influence=Math.exp(-distance*distance/(90*90))*strength;
    const shift=influence*10/(distance||1);
    ctx.globalAlpha=.09+influence*.35;
    ctx.beginPath();ctx.arc(px+dx*shift,py+dy*shift,.8+influence*.7,0,Math.PI*2);ctx.fill();
   }
   ctx.globalAlpha=1;
   if(!reduced.matches&&inView&&(active||strength>.002))frame=requestAnimationFrame(draw);
  }
  function request(){if(!frame)frame=requestAnimationFrame(draw)}
  function resize(){const r=card.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);request()}
  card.addEventListener('pointermove',event=>{if(reduced.matches||event.pointerType==='touch')return;const r=card.getBoundingClientRect();x=event.clientX-r.left;y=event.clientY-r.top;active=true;request()},{passive:true});
  card.addEventListener('pointerleave',()=>{active=false;request()},{passive:true});
  if('ResizeObserver' in window)new ResizeObserver(resize).observe(card);
  addEventListener('resize',resize,{passive:true});
  if('IntersectionObserver' in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;if(inView)request();else{cancelAnimationFrame(frame);frame=0}}).observe(card);
  reduced.addEventListener('change',()=>{active=false;strength=0;request()});resize();
 });
 reduced.addEventListener('change',()=>{if(reduced.matches){entrance?.disconnect();cards.forEach(card=>card.classList.add('wd-works-visible'))}});
})();
</script>

<script>
// A seleção inicial termina na primeira interação e não é restaurada.
const wdExplore=document.getElementById('wd-explore');
const wdExploreCards=[...wdExplore.querySelectorAll('.wd-explore-card')];
let wdExploreInteracted=false;
function wdExploreClearInitial(){
 if(wdExploreInteracted)return;
 wdExploreInteracted=true;
 wdExploreCards.forEach(card=>card.classList.remove('is-active'));
 wdExploreCards.forEach(card=>{
  card.removeEventListener('mouseenter',wdExploreClearInitial);
  card.removeEventListener('focusin',wdExploreClearInitial);
 });
}
wdExploreCards.forEach(card=>{
 card.addEventListener('mouseenter',wdExploreClearInitial,{once:true});
 card.addEventListener('focusin',wdExploreClearInitial,{once:true});
});
document.querySelectorAll('[data-wd-explore-url]').forEach(link=>{
 const target=document.getElementById(link.getAttribute('href').slice(1));
 if(!target)link.href=link.dataset.wdExploreUrl;
});
</script>

<style>
/* Both sections share the existing page light field. */
.wd-statement-section,.wd-transformacao-section{box-sizing:border-box;background:transparent;color:#f7f6fb;font-family:"Space Grotesk",Arial,sans-serif}
.wd-statement-section *, .wd-transformacao-section *{box-sizing:border-box}
.wd-statement-section{min-height:75vh;display:flex;align-items:center;justify-content:center;padding:96px 40px}
.wd-statement-inner{width:100%;max-width:1200px;margin-inline:auto}
.wd-transformacao-closing-text{margin:0;font-size:clamp(44px,6.835vw,120px);font-weight:500;line-height:1;letter-spacing:-.04167em;text-align:center;text-wrap:balance;color:#efe7ff}
.wd-statement-title{max-width:1100px;margin-inline:auto}
.wd-statement-line,.wd-transformacao-line{display:block;padding-bottom:.055em;--wd-line-from:#6025e1;--wd-line-to:#cbb6ff}
.wd-statement-emphasis{font:inherit;color:#04cd8f}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .wd-statement-line,.wd-transformacao-line{background:linear-gradient(90deg,var(--wd-line-from),var(--wd-line-to));background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
 .wd-statement-emphasis{background:linear-gradient(90deg,#efe7ff,#04cd8f);background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
}
.wd-transformacao-section{overflow:clip}
.wd-transformacao-content{position:relative;z-index:2;width:50%;max-width:572px;padding-left:40px}
.wd-transformacao-heading{display:flex;flex-direction:column;align-items:flex-start;gap:32px}
.wd-transformacao-eyebrow{margin:0;font-size:20px;font-weight:500;line-height:1.4;letter-spacing:.2em;text-transform:uppercase;}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .wd-transformacao-eyebrow{;}
}
.wd-transformacao-title{margin:0;text-wrap:balance}
.wd-transformacao-description{margin:48px 0 0;font-family:"Nunito",system-ui,sans-serif;font-size:clamp(16px,1.27vw,18px);line-height:1.6;font-weight:400;color:#c8c4d3}
.wd-transformacao-cta{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;gap:16px;width:max-content;max-width:calc(100% - 40px);min-height:52px;margin:48px 0 0 40px;padding:14px 20px;border:0;border-radius:6px;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0%;transition:background-position 600ms ease,color 200ms ease}
.wd-transformacao-cta:hover,.wd-transformacao-cta:focus-visible{background-position:0% 0%;color:#24123e}
.wd-transformacao-cta:focus-visible{outline:2px solid #bda4ff;outline-offset:5px}
.wd-transformacao-cta-icon{width:14px;height:14px;flex:0 0 14px;color:inherit}
.wd-transformacao-closing{min-height:75vh;padding:96px 40px;display:flex;align-items:center;justify-content:center}
.wd-transformacao-closing-text{width:100%;max-width:1200px}
@media(max-width:991px){
 .wd-statement-section,.wd-transformacao-closing{min-height:65vh;padding:72px 24px}
 .wd-transformacao-closing-text{font-size:clamp(44px,7.2vw,76px)}
 .wd-transformacao-content{width:100%;max-width:620px;padding:0}
 .wd-transformacao-heading{gap:24px}
 .wd-transformacao-eyebrow{font-size:16px}
 .wd-transformacao-title{}
 .wd-transformacao-description{font-size:16px;margin-top:32px}
 .wd-transformacao-cta{margin:32px 0 0;max-width:100%}
}
@media(max-width:600px){
 .wd-statement-section,.wd-transformacao-closing{min-height:65svh;padding:64px 20px}
 .wd-transformacao-closing-text{font-size:clamp(36px,9.4vw,56px)}
 .wd-transformacao-title{}
 .wd-transformacao-description{font-size:15px}
}
@media(prefers-reduced-motion:reduce){
 .wd-transformacao-cta{transition:none}
 .wd-statement-line,.wd-transformacao-line{--wd-line-from:#efe7ff!important;--wd-line-to:#f5c3d8!important}
}

/* Give the two-line statement the available width. */
#wd-statement{padding-inline:clamp(12px,1.5vw,24px)}
.wd-statement-inner{max-width:1440px}
.wd-statement-title{max-width:none}
.wd-statement-line{white-space:nowrap}
/* Transformação digital: card contained within the continuous page background. */
.wd-transformacao-section{background:transparent;padding:80px 0 0;overflow:visible;color:#fff;font-family:"Space Grotesk",Arial,sans-serif}
.wd-transformacao-section *{box-sizing:border-box}
.wd-transformacao-content{position:relative;z-index:2;width:calc(55% + 16px);max-width:660px;padding:0}
.wd-transformacao-heading{display:flex;flex-direction:column;align-items:flex-start;gap:32px}
.wd-transformacao-eyebrow{margin:0;font-size:20px;font-weight:500;line-height:1.4;letter-spacing:.2em;text-transform:uppercase}
.wd-transformacao-title{margin:0;color:#fff;text-wrap:nowrap;white-space:nowrap}
.wd-transformacao-description{margin:40px 0 0;max-width:540px;color:#fff;font-family:"Nunito",system-ui,sans-serif;font-size:18px;line-height:1.5;font-weight:400}
.wd-transformacao-cta{position:relative;z-index:2;display:flex;align-items:center;justify-content:center;gap:16px;width:max-content;max-width:100%;min-height:54px;margin:40px 0 0;padding:14px 20px;border:0;border-radius:4px;text-decoration:none;color:#fff;font-size:14px;line-height:1;white-space:nowrap;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0%;transition:background-position 600ms ease,color 200ms ease}
.wd-transformacao-cta:hover,.wd-transformacao-cta:focus-visible{background-position:0% 0%;color:#24123e}
.wd-transformacao-cta:focus-visible{outline:2px solid #bda4ff;outline-offset:5px}
.wd-transformacao-cta-icon{width:14px;height:14px;flex:0 0 14px;color:inherit}
.wd-transformacao-closing{min-height:75vh;padding:96px 40px;display:flex;align-items:center;justify-content:center;background:transparent}
.wd-transformacao-closing-text{margin:0;width:100%;max-width:1200px;font-size:clamp(44px,6.835vw,120px);font-weight:500;line-height:1;letter-spacing:-.04167em;text-align:center;text-wrap:balance;color:#efe7ff}
.wd-transformacao-line{display:block;padding-bottom:.055em;--wd-line-from:#6025e1;--wd-line-to:#cbb6ff}
@supports ((background-clip:text) or (-webkit-background-clip:text)){
 .wd-transformacao-line{background:linear-gradient(90deg,var(--wd-line-from),var(--wd-line-to));background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
}
@media(max-width:1199px) and (min-width:992px){
 .wd-transformacao-content{width:60%}
 .wd-transformacao-description{max-width:470px;font-size:17px}
}
@media(max-width:991px){
 .wd-transformacao-section{padding-top:64px}
 .wd-transformacao-content{width:100%;max-width:none;padding:0}
 .wd-transformacao-heading{gap:24px}
 .wd-transformacao-eyebrow{font-size:16px}
 .wd-transformacao-title{white-space:normal}
 .wd-transformacao-description{margin-top:32px;font-size:16px;max-width:620px}
 .wd-transformacao-cta{margin-top:32px}
 .wd-transformacao-closing{min-height:65vh;padding:72px 24px}
 .wd-transformacao-closing-text{font-size:clamp(44px,7.2vw,76px)}
}
@media(max-width:600px){
 .wd-transformacao-title{}
 .wd-transformacao-description{font-size:15px}
 .wd-transformacao-cta{font-size:13px}
 .wd-transformacao-closing{min-height:65svh;padding:64px 20px}
 .wd-transformacao-closing-text{font-size:clamp(36px,9.4vw,56px)}
}
@media(prefers-reduced-motion:reduce){
 .wd-transformacao-cta{transition:none}
 .wd-transformacao-line{--wd-line-from:#efe7ff!important;--wd-line-to:#f5c3d8!important}
}
@media(max-width:991px){}
/* Prevent focus from scrolling the card's oversized decorative globe. */
@supports(overflow:clip){}
@media(max-width:991px){
}
@media(max-width:600px){
}
@media(max-width:991px){
}
@media(max-width:600px){
}
</style>
<section id="wd-statement" class="wd-statement-section" aria-labelledby="wd-statement-title">
 <div class="wd-statement-inner">
  <h2 id="wd-statement-title" class="wd-statement-title" aria-label="Onde você está quando seu cliente NÃO procura por você?">Onde você está quando seu cliente <strong class="wd-statement-emphasis">NÃO</strong> procura por você?</h2>
 </div>
</section>
<section id="wd-transformacao" class="wd-transformacao-section" aria-labelledby="wd-transformacao-title">
 <div class="wd-tr-card">
  <div class="wd-tr-glow" aria-hidden="true"></div>
  <div class="wd-tr-globe" aria-hidden="true"><div class="wd-tr-dots"><svg class="wd-transformacao-globe-points" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1040 1040" fill="none" aria-hidden="true" focusable="false"><g fill="#7A6E9E" opacity=".70"><circle cx="368" cy="184" r="2.05"/><circle cx="384" cy="184" r="2.05"/><circle cx="392" cy="184" r="2.05"/><circle cx="400" cy="184" r="2.05"/><circle cx="408" cy="184" r="2.05"/><circle cx="416" cy="184" r="2.05"/><circle cx="424" cy="184" r="2.05"/><circle cx="432" cy="184" r="2.05"/><circle cx="440" cy="184" r="2.05"/><circle cx="448" cy="184" r="2.05"/><circle cx="456" cy="184" r="2.05"/><circle cx="464" cy="184" r="2.05"/><circle cx="480" cy="184" r="2.05"/><circle cx="528" cy="184" r="2.05"/><circle cx="304" cy="192" r="2.05"/><circle cx="312" cy="192" r="2.05"/><circle cx="320" cy="192" r="2.05"/><circle cx="328" cy="192" r="2.05"/><circle cx="344" cy="192" r="2.05"/><circle cx="352" cy="192" r="2.05"/><circle cx="360" cy="192" r="2.05"/><circle cx="368" cy="192" r="2.05"/><circle cx="392" cy="192" r="2.05"/><circle cx="400" cy="192" r="2.05"/><circle cx="408" cy="192" r="2.05"/><circle cx="416" cy="192" r="2.05"/><circle cx="424" cy="192" r="2.05"/><circle cx="432" cy="192" r="2.05"/><circle cx="440" cy="192" r="2.05"/><circle cx="448" cy="192" r="2.05"/><circle cx="456" cy="192" r="2.05"/><circle cx="464" cy="192" r="2.05"/><circle cx="472" cy="192" r="2.05"/><circle cx="480" cy="192" r="2.05"/><circle cx="488" cy="192" r="2.05"/><circle cx="264" cy="200" r="2.05"/><circle cx="272" cy="200" r="2.05"/><circle cx="280" cy="200" r="2.05"/><circle cx="304" cy="200" r="2.05"/><circle cx="320" cy="200" r="2.05"/><circle cx="336" cy="200" r="2.05"/><circle cx="416" cy="200" r="2.05"/><circle cx="424" cy="200" r="2.05"/><circle cx="432" cy="200" r="2.05"/><circle cx="440" cy="200" r="2.05"/><circle cx="448" cy="200" r="2.05"/><circle cx="456" cy="200" r="2.05"/><circle cx="464" cy="200" r="2.05"/><circle cx="472" cy="200" r="2.05"/><circle cx="480" cy="200" r="2.05"/><circle cx="488" cy="200" r="2.05"/><circle cx="496" cy="200" r="2.05"/><circle cx="504" cy="200" r="2.05"/><circle cx="232" cy="208" r="2.05"/><circle cx="240" cy="208" r="2.05"/><circle cx="248" cy="208" r="2.05"/><circle cx="256" cy="208" r="2.05"/><circle cx="264" cy="208" r="2.05"/><circle cx="272" cy="208" r="2.05"/><circle cx="280" cy="208" r="2.05"/><circle cx="296" cy="208" r="2.05"/><circle cx="312" cy="208" r="2.05"/><circle cx="320" cy="208" r="2.05"/><circle cx="328" cy="208" r="2.05"/><circle cx="336" cy="208" r="2.05"/><circle cx="344" cy="208" r="2.05"/><circle cx="352" cy="208" r="2.05"/><circle cx="408" cy="208" r="2.05"/><circle cx="416" cy="208" r="2.05"/><circle cx="424" cy="208" r="2.05"/><circle cx="432" cy="208" r="2.05"/><circle cx="440" cy="208" r="2.05"/><circle cx="448" cy="208" r="2.05"/><circle cx="456" cy="208" r="2.05"/><circle cx="464" cy="208" r="2.05"/><circle cx="472" cy="208" r="2.05"/><circle cx="480" cy="208" r="2.05"/><circle cx="488" cy="208" r="2.05"/><circle cx="496" cy="208" r="2.05"/><circle cx="504" cy="208" r="2.05"/><circle cx="616" cy="208" r="2.05"/><circle cx="624" cy="208" r="2.05"/><circle cx="632" cy="208" r="2.05"/><circle cx="640" cy="208" r="2.05"/><circle cx="648" cy="208" r="2.05"/><circle cx="208" cy="216" r="2.05"/><circle cx="216" cy="216" r="2.05"/><circle cx="224" cy="216" r="2.05"/><circle cx="232" cy="216" r="2.05"/><circle cx="240" cy="216" r="2.05"/><circle cx="248" cy="216" r="2.05"/><circle cx="256" cy="216" r="2.05"/><circle cx="264" cy="216" r="2.05"/><circle cx="272" cy="216" r="2.05"/><circle cx="280" cy="216" r="2.05"/><circle cx="288" cy="216" r="2.05"/><circle cx="296" cy="216" r="2.05"/><circle cx="312" cy="216" r="2.05"/><circle cx="336" cy="216" r="2.05"/><circle cx="344" cy="216" r="2.05"/><circle cx="352" cy="216" r="2.05"/><circle cx="360" cy="216" r="2.05"/><circle cx="424" cy="216" r="2.05"/><circle cx="432" cy="216" r="2.05"/><circle cx="440" cy="216" r="2.05"/><circle cx="448" cy="216" r="2.05"/><circle cx="456" cy="216" r="2.05"/><circle cx="464" cy="216" r="2.05"/><circle cx="472" cy="216" r="2.05"/><circle cx="480" cy="216" r="2.05"/><circle cx="488" cy="216" r="2.05"/><circle cx="496" cy="216" r="2.05"/><circle cx="504" cy="216" r="2.05"/><circle cx="632" cy="216" r="2.05"/><circle cx="640" cy="216" r="2.05"/><circle cx="648" cy="216" r="2.05"/><circle cx="656" cy="216" r="2.05"/><circle cx="664" cy="216" r="2.05"/><circle cx="192" cy="224" r="2.05"/><circle cx="200" cy="224" r="2.05"/><circle cx="208" cy="224" r="2.05"/><circle cx="216" cy="224" r="2.05"/><circle cx="224" cy="224" r="2.05"/><circle cx="232" cy="224" r="2.05"/><circle cx="240" cy="224" r="2.05"/><circle cx="248" cy="224" r="2.05"/><circle cx="256" cy="224" r="2.05"/><circle cx="264" cy="224" r="2.05"/><circle cx="272" cy="224" r="2.05"/><circle cx="280" cy="224" r="2.05"/><circle cx="288" cy="224" r="2.05"/><circle cx="336" cy="224" r="2.05"/><circle cx="344" cy="224" r="2.05"/><circle cx="352" cy="224" r="2.05"/><circle cx="360" cy="224" r="2.05"/><circle cx="368" cy="224" r="2.05"/><circle cx="408" cy="224" r="2.05"/><circle cx="416" cy="224" r="2.05"/><circle cx="424" cy="224" r="2.05"/><circle cx="432" cy="224" r="2.05"/><circle cx="440" cy="224" r="2.05"/><circle cx="448" cy="224" r="2.05"/><circle cx="456" cy="224" r="2.05"/><circle cx="464" cy="224" r="2.05"/><circle cx="472" cy="224" r="2.05"/><circle cx="480" cy="224" r="2.05"/><circle cx="640" cy="224" r="2.05"/><circle cx="648" cy="224" r="2.05"/><circle cx="656" cy="224" r="2.05"/><circle cx="672" cy="224" r="2.05"/><circle cx="680" cy="224" r="2.05"/><circle cx="688" cy="224" r="2.05"/><circle cx="168" cy="232" r="2.05"/><circle cx="176" cy="232" r="2.05"/><circle cx="184" cy="232" r="2.05"/><circle cx="192" cy="232" r="2.05"/><circle cx="200" cy="232" r="2.05"/><circle cx="208" cy="232" r="2.05"/><circle cx="216" cy="232" r="2.05"/><circle cx="224" cy="232" r="2.05"/><circle cx="232" cy="232" r="2.05"/><circle cx="240" cy="232" r="2.05"/><circle cx="248" cy="232" r="2.05"/><circle cx="256" cy="232" r="2.05"/><circle cx="280" cy="232" r="2.05"/><circle cx="288" cy="232" r="2.05"/><circle cx="312" cy="232" r="2.05"/><circle cx="328" cy="232" r="2.05"/><circle cx="336" cy="232" r="2.05"/><circle cx="344" cy="232" r="2.05"/><circle cx="352" cy="232" r="2.05"/><circle cx="416" cy="232" r="2.05"/><circle cx="424" cy="232" r="2.05"/><circle cx="432" cy="232" r="2.05"/><circle cx="440" cy="232" r="2.05"/><circle cx="448" cy="232" r="2.05"/><circle cx="456" cy="232" r="2.05"/><circle cx="536" cy="232" r="2.05"/><circle cx="544" cy="232" r="2.05"/><circle cx="552" cy="232" r="2.05"/><circle cx="560" cy="232" r="2.05"/><circle cx="648" cy="232" r="2.05"/><circle cx="656" cy="232" r="2.05"/><circle cx="664" cy="232" r="2.05"/><circle cx="680" cy="232" r="2.05"/><circle cx="688" cy="232" r="2.05"/><circle cx="696" cy="232" r="2.05"/><circle cx="704" cy="232" r="2.05"/><circle cx="712" cy="232" r="2.05"/><circle cx="152" cy="240" r="2.05"/><circle cx="160" cy="240" r="2.05"/><circle cx="168" cy="240" r="2.05"/><circle cx="176" cy="240" r="2.05"/><circle cx="184" cy="240" r="2.05"/><circle cx="192" cy="240" r="2.05"/><circle cx="200" cy="240" r="2.05"/><circle cx="208" cy="240" r="2.05"/><circle cx="216" cy="240" r="2.05"/><circle cx="224" cy="240" r="2.05"/><circle cx="232" cy="240" r="2.05"/><circle cx="304" cy="240" r="2.05"/><circle cx="336" cy="240" r="2.05"/><circle cx="352" cy="240" r="2.05"/><circle cx="416" cy="240" r="2.05"/><circle cx="424" cy="240" r="2.05"/><circle cx="432" cy="240" r="2.05"/><circle cx="440" cy="240" r="2.05"/><circle cx="448" cy="240" r="2.05"/><circle cx="648" cy="240" r="2.05"/><circle cx="656" cy="240" r="2.05"/><circle cx="664" cy="240" r="2.05"/><circle cx="672" cy="240" r="2.05"/><circle cx="680" cy="240" r="2.05"/><circle cx="712" cy="240" r="2.05"/><circle cx="720" cy="240" r="2.05"/><circle cx="728" cy="240" r="2.05"/><circle cx="136" cy="248" r="2.05"/><circle cx="144" cy="248" r="2.05"/><circle cx="152" cy="248" r="2.05"/><circle cx="160" cy="248" r="2.05"/><circle cx="168" cy="248" r="2.05"/><circle cx="176" cy="248" r="2.05"/><circle cx="184" cy="248" r="2.05"/><circle cx="192" cy="248" r="2.05"/><circle cx="200" cy="248" r="2.05"/><circle cx="208" cy="248" r="2.05"/><circle cx="216" cy="248" r="2.05"/><circle cx="296" cy="248" r="2.05"/><circle cx="304" cy="248" r="2.05"/><circle cx="312" cy="248" r="2.05"/><circle cx="320" cy="248" r="2.05"/><circle cx="424" cy="248" r="2.05"/><circle cx="432" cy="248" r="2.05"/><circle cx="440" cy="248" r="2.05"/><circle cx="448" cy="248" r="2.05"/><circle cx="664" cy="248" r="2.05"/><circle cx="672" cy="248" r="2.05"/><circle cx="680" cy="248" r="2.05"/><circle cx="688" cy="248" r="2.05"/><circle cx="696" cy="248" r="2.05"/><circle cx="720" cy="248" r="2.05"/><circle cx="728" cy="248" r="2.05"/><circle cx="736" cy="248" r="2.05"/><circle cx="744" cy="248" r="2.05"/><circle cx="120" cy="256" r="2.05"/><circle cx="128" cy="256" r="2.05"/><circle cx="136" cy="256" r="2.05"/><circle cx="144" cy="256" r="2.05"/><circle cx="152" cy="256" r="2.05"/><circle cx="160" cy="256" r="2.05"/><circle cx="168" cy="256" r="2.05"/><circle cx="176" cy="256" r="2.05"/><circle cx="184" cy="256" r="2.05"/><circle cx="192" cy="256" r="2.05"/><circle cx="200" cy="256" r="2.05"/><circle cx="208" cy="256" r="2.05"/><circle cx="216" cy="256" r="2.05"/><circle cx="288" cy="256" r="2.05"/><circle cx="296" cy="256" r="2.05"/><circle cx="304" cy="256" r="2.05"/><circle cx="312" cy="256" r="2.05"/><circle cx="320" cy="256" r="2.05"/><circle cx="344" cy="256" r="2.05"/><circle cx="632" cy="256" r="2.05"/><circle cx="688" cy="256" r="2.05"/><circle cx="696" cy="256" r="2.05"/><circle cx="704" cy="256" r="2.05"/><circle cx="728" cy="256" r="2.05"/><circle cx="736" cy="256" r="2.05"/><circle cx="744" cy="256" r="2.05"/><circle cx="752" cy="256" r="2.05"/><circle cx="760" cy="256" r="2.05"/><circle cx="112" cy="264" r="2.05"/><circle cx="120" cy="264" r="2.05"/><circle cx="128" cy="264" r="2.05"/><circle cx="136" cy="264" r="2.05"/><circle cx="144" cy="264" r="2.05"/><circle cx="152" cy="264" r="2.05"/><circle cx="160" cy="264" r="2.05"/><circle cx="168" cy="264" r="2.05"/><circle cx="176" cy="264" r="2.05"/><circle cx="184" cy="264" r="2.05"/><circle cx="192" cy="264" r="2.05"/><circle cx="200" cy="264" r="2.05"/><circle cx="208" cy="264" r="2.05"/><circle cx="216" cy="264" r="2.05"/><circle cx="224" cy="264" r="2.05"/><circle cx="288" cy="264" r="2.05"/><circle cx="296" cy="264" r="2.05"/><circle cx="304" cy="264" r="2.05"/><circle cx="312" cy="264" r="2.05"/><circle cx="320" cy="264" r="2.05"/><circle cx="328" cy="264" r="2.05"/><circle cx="336" cy="264" r="2.05"/><circle cx="344" cy="264" r="2.05"/><circle cx="352" cy="264" r="2.05"/><circle cx="640" cy="264" r="2.05"/><circle cx="648" cy="264" r="2.05"/><circle cx="696" cy="264" r="2.05"/><circle cx="704" cy="264" r="2.05"/><circle cx="712" cy="264" r="2.05"/><circle cx="736" cy="264" r="2.05"/><circle cx="744" cy="264" r="2.05"/><circle cx="752" cy="264" r="2.05"/><circle cx="760" cy="264" r="2.05"/><circle cx="768" cy="264" r="2.05"/><circle cx="104" cy="272" r="2.05"/><circle cx="112" cy="272" r="2.05"/><circle cx="120" cy="272" r="2.05"/><circle cx="128" cy="272" r="2.05"/><circle cx="136" cy="272" r="2.05"/><circle cx="144" cy="272" r="2.05"/><circle cx="152" cy="272" r="2.05"/><circle cx="160" cy="272" r="2.05"/><circle cx="168" cy="272" r="2.05"/><circle cx="176" cy="272" r="2.05"/><circle cx="184" cy="272" r="2.05"/><circle cx="192" cy="272" r="2.05"/><circle cx="200" cy="272" r="2.05"/><circle cx="208" cy="272" r="2.05"/><circle cx="216" cy="272" r="2.05"/><circle cx="224" cy="272" r="2.05"/><circle cx="232" cy="272" r="2.05"/><circle cx="240" cy="272" r="2.05"/><circle cx="272" cy="272" r="2.05"/><circle cx="280" cy="272" r="2.05"/><circle cx="288" cy="272" r="2.05"/><circle cx="296" cy="272" r="2.05"/><circle cx="304" cy="272" r="2.05"/><circle cx="312" cy="272" r="2.05"/><circle cx="320" cy="272" r="2.05"/><circle cx="328" cy="272" r="2.05"/><circle cx="336" cy="272" r="2.05"/><circle cx="344" cy="272" r="2.05"/><circle cx="352" cy="272" r="2.05"/><circle cx="640" cy="272" r="2.05"/><circle cx="648" cy="272" r="2.05"/><circle cx="656" cy="272" r="2.05"/><circle cx="664" cy="272" r="2.05"/><circle cx="712" cy="272" r="2.05"/><circle cx="720" cy="272" r="2.05"/><circle cx="728" cy="272" r="2.05"/><circle cx="736" cy="272" r="2.05"/><circle cx="744" cy="272" r="2.05"/><circle cx="752" cy="272" r="2.05"/><circle cx="760" cy="272" r="2.05"/><circle cx="768" cy="272" r="2.05"/><circle cx="776" cy="272" r="2.05"/><circle cx="784" cy="272" r="2.05"/><circle cx="88" cy="280" r="2.05"/><circle cx="96" cy="280" r="2.05"/><circle cx="104" cy="280" r="2.05"/><circle cx="112" cy="280" r="2.05"/><circle cx="120" cy="280" r="2.05"/><circle cx="128" cy="280" r="2.05"/><circle cx="136" cy="280" r="2.05"/><circle cx="144" cy="280" r="2.05"/><circle cx="152" cy="280" r="2.05"/><circle cx="160" cy="280" r="2.05"/><circle cx="168" cy="280" r="2.05"/><circle cx="176" cy="280" r="2.05"/><circle cx="184" cy="280" r="2.05"/><circle cx="192" cy="280" r="2.05"/><circle cx="200" cy="280" r="2.05"/><circle cx="208" cy="280" r="2.05"/><circle cx="216" cy="280" r="2.05"/><circle cx="224" cy="280" r="2.05"/><circle cx="232" cy="280" r="2.05"/><circle cx="256" cy="280" r="2.05"/><circle cx="264" cy="280" r="2.05"/><circle cx="272" cy="280" r="2.05"/><circle cx="280" cy="280" r="2.05"/><circle cx="288" cy="280" r="2.05"/><circle cx="296" cy="280" r="2.05"/><circle cx="304" cy="280" r="2.05"/><circle cx="312" cy="280" r="2.05"/><circle cx="320" cy="280" r="2.05"/><circle cx="328" cy="280" r="2.05"/><circle cx="336" cy="280" r="2.05"/><circle cx="344" cy="280" r="2.05"/><circle cx="352" cy="280" r="2.05"/><circle cx="360" cy="280" r="2.05"/><circle cx="368" cy="280" r="2.05"/><circle cx="640" cy="280" r="2.05"/><circle cx="648" cy="280" r="2.05"/><circle cx="664" cy="280" r="2.05"/><circle cx="672" cy="280" r="2.05"/><circle cx="704" cy="280" r="2.05"/><circle cx="712" cy="280" r="2.05"/><circle cx="720" cy="280" r="2.05"/><circle cx="728" cy="280" r="2.05"/><circle cx="736" cy="280" r="2.05"/><circle cx="744" cy="280" r="2.05"/><circle cx="752" cy="280" r="2.05"/><circle cx="760" cy="280" r="2.05"/><circle cx="768" cy="280" r="2.05"/><circle cx="776" cy="280" r="2.05"/><circle cx="784" cy="280" r="2.05"/><circle cx="792" cy="280" r="2.05"/><circle cx="800" cy="280" r="2.05"/><circle cx="88" cy="288" r="2.05"/><circle cx="96" cy="288" r="2.05"/><circle cx="104" cy="288" r="2.05"/><circle cx="112" cy="288" r="2.05"/><circle cx="120" cy="288" r="2.05"/><circle cx="128" cy="288" r="2.05"/><circle cx="136" cy="288" r="2.05"/><circle cx="144" cy="288" r="2.05"/><circle cx="152" cy="288" r="2.05"/><circle cx="160" cy="288" r="2.05"/><circle cx="168" cy="288" r="2.05"/><circle cx="176" cy="288" r="2.05"/><circle cx="184" cy="288" r="2.05"/><circle cx="192" cy="288" r="2.05"/><circle cx="200" cy="288" r="2.05"/><circle cx="208" cy="288" r="2.05"/><circle cx="216" cy="288" r="2.05"/><circle cx="224" cy="288" r="2.05"/><circle cx="232" cy="288" r="2.05"/><circle cx="256" cy="288" r="2.05"/><circle cx="264" cy="288" r="2.05"/><circle cx="272" cy="288" r="2.05"/><circle cx="280" cy="288" r="2.05"/><circle cx="288" cy="288" r="2.05"/><circle cx="296" cy="288" r="2.05"/><circle cx="304" cy="288" r="2.05"/><circle cx="312" cy="288" r="2.05"/><circle cx="320" cy="288" r="2.05"/><circle cx="328" cy="288" r="2.05"/><circle cx="336" cy="288" r="2.05"/><circle cx="344" cy="288" r="2.05"/><circle cx="352" cy="288" r="2.05"/><circle cx="360" cy="288" r="2.05"/><circle cx="368" cy="288" r="2.05"/><circle cx="376" cy="288" r="2.05"/><circle cx="640" cy="288" r="2.05"/><circle cx="648" cy="288" r="2.05"/><circle cx="664" cy="288" r="2.05"/><circle cx="672" cy="288" r="2.05"/><circle cx="680" cy="288" r="2.05"/><circle cx="688" cy="288" r="2.05"/><circle cx="704" cy="288" r="2.05"/><circle cx="712" cy="288" r="2.05"/><circle cx="720" cy="288" r="2.05"/><circle cx="728" cy="288" r="2.05"/><circle cx="736" cy="288" r="2.05"/><circle cx="744" cy="288" r="2.05"/><circle cx="752" cy="288" r="2.05"/><circle cx="760" cy="288" r="2.05"/><circle cx="768" cy="288" r="2.05"/><circle cx="776" cy="288" r="2.05"/><circle cx="784" cy="288" r="2.05"/><circle cx="792" cy="288" r="2.05"/><circle cx="800" cy="288" r="2.05"/><circle cx="808" cy="288" r="2.05"/><circle cx="72" cy="296" r="2.05"/><circle cx="80" cy="296" r="2.05"/><circle cx="88" cy="296" r="2.05"/><circle cx="96" cy="296" r="2.05"/><circle cx="104" cy="296" r="2.05"/><circle cx="112" cy="296" r="2.05"/><circle cx="120" cy="296" r="2.05"/><circle cx="128" cy="296" r="2.05"/><circle cx="136" cy="296" r="2.05"/><circle cx="144" cy="296" r="2.05"/><circle cx="152" cy="296" r="2.05"/><circle cx="160" cy="296" r="2.05"/><circle cx="168" cy="296" r="2.05"/><circle cx="176" cy="296" r="2.05"/><circle cx="184" cy="296" r="2.05"/><circle cx="192" cy="296" r="2.05"/><circle cx="200" cy="296" r="2.05"/><circle cx="208" cy="296" r="2.05"/><circle cx="216" cy="296" r="2.05"/><circle cx="224" cy="296" r="2.05"/><circle cx="232" cy="296" r="2.05"/><circle cx="240" cy="296" r="2.05"/><circle cx="248" cy="296" r="2.05"/><circle cx="256" cy="296" r="2.05"/><circle cx="264" cy="296" r="2.05"/><circle cx="272" cy="296" r="2.05"/><circle cx="280" cy="296" r="2.05"/><circle cx="288" cy="296" r="2.05"/><circle cx="296" cy="296" r="2.05"/><circle cx="304" cy="296" r="2.05"/><circle cx="312" cy="296" r="2.05"/><circle cx="320" cy="296" r="2.05"/><circle cx="328" cy="296" r="2.05"/><circle cx="336" cy="296" r="2.05"/><circle cx="344" cy="296" r="2.05"/><circle cx="352" cy="296" r="2.05"/><circle cx="360" cy="296" r="2.05"/><circle cx="704" cy="296" r="2.05"/><circle cx="712" cy="296" r="2.05"/><circle cx="720" cy="296" r="2.05"/><circle cx="728" cy="296" r="2.05"/><circle cx="736" cy="296" r="2.05"/><circle cx="744" cy="296" r="2.05"/><circle cx="752" cy="296" r="2.05"/><circle cx="760" cy="296" r="2.05"/><circle cx="768" cy="296" r="2.05"/><circle cx="776" cy="296" r="2.05"/><circle cx="784" cy="296" r="2.05"/><circle cx="792" cy="296" r="2.05"/><circle cx="800" cy="296" r="2.05"/><circle cx="808" cy="296" r="2.05"/><circle cx="816" cy="296" r="2.05"/><circle cx="64" cy="304" r="2.05"/><circle cx="72" cy="304" r="2.05"/><circle cx="80" cy="304" r="2.05"/><circle cx="88" cy="304" r="2.05"/><circle cx="96" cy="304" r="2.05"/><circle cx="104" cy="304" r="2.05"/><circle cx="112" cy="304" r="2.05"/><circle cx="120" cy="304" r="2.05"/><circle cx="128" cy="304" r="2.05"/><circle cx="136" cy="304" r="2.05"/><circle cx="144" cy="304" r="2.05"/><circle cx="152" cy="304" r="2.05"/><circle cx="160" cy="304" r="2.05"/><circle cx="168" cy="304" r="2.05"/><circle cx="176" cy="304" r="2.05"/><circle cx="184" cy="304" r="2.05"/><circle cx="192" cy="304" r="2.05"/><circle cx="200" cy="304" r="2.05"/><circle cx="208" cy="304" r="2.05"/><circle cx="216" cy="304" r="2.05"/><circle cx="224" cy="304" r="2.05"/><circle cx="232" cy="304" r="2.05"/><circle cx="240" cy="304" r="2.05"/><circle cx="248" cy="304" r="2.05"/><circle cx="256" cy="304" r="2.05"/><circle cx="264" cy="304" r="2.05"/><circle cx="272" cy="304" r="2.05"/><circle cx="280" cy="304" r="2.05"/><circle cx="288" cy="304" r="2.05"/><circle cx="296" cy="304" r="2.05"/><circle cx="328" cy="304" r="2.05"/><circle cx="360" cy="304" r="2.05"/><circle cx="368" cy="304" r="2.05"/><circle cx="688" cy="304" r="2.05"/><circle cx="696" cy="304" r="2.05"/><circle cx="704" cy="304" r="2.05"/><circle cx="712" cy="304" r="2.05"/><circle cx="720" cy="304" r="2.05"/><circle cx="728" cy="304" r="2.05"/><circle cx="736" cy="304" r="2.05"/><circle cx="744" cy="304" r="2.05"/><circle cx="752" cy="304" r="2.05"/><circle cx="760" cy="304" r="2.05"/><circle cx="768" cy="304" r="2.05"/><circle cx="776" cy="304" r="2.05"/><circle cx="784" cy="304" r="2.05"/><circle cx="792" cy="304" r="2.05"/><circle cx="800" cy="304" r="2.05"/><circle cx="808" cy="304" r="2.05"/><circle cx="832" cy="304" r="2.05"/><circle cx="56" cy="312" r="2.05"/><circle cx="64" cy="312" r="2.05"/><circle cx="72" cy="312" r="2.05"/><circle cx="80" cy="312" r="2.05"/><circle cx="88" cy="312" r="2.05"/><circle cx="96" cy="312" r="2.05"/><circle cx="104" cy="312" r="2.05"/><circle cx="112" cy="312" r="2.05"/><circle cx="120" cy="312" r="2.05"/><circle cx="128" cy="312" r="2.05"/><circle cx="136" cy="312" r="2.05"/><circle cx="144" cy="312" r="2.05"/><circle cx="152" cy="312" r="2.05"/><circle cx="160" cy="312" r="2.05"/><circle cx="168" cy="312" r="2.05"/><circle cx="176" cy="312" r="2.05"/><circle cx="184" cy="312" r="2.05"/><circle cx="192" cy="312" r="2.05"/><circle cx="200" cy="312" r="2.05"/><circle cx="208" cy="312" r="2.05"/><circle cx="216" cy="312" r="2.05"/><circle cx="224" cy="312" r="2.05"/><circle cx="232" cy="312" r="2.05"/><circle cx="240" cy="312" r="2.05"/><circle cx="248" cy="312" r="2.05"/><circle cx="256" cy="312" r="2.05"/><circle cx="264" cy="312" r="2.05"/><circle cx="272" cy="312" r="2.05"/><circle cx="280" cy="312" r="2.05"/><circle cx="288" cy="312" r="2.05"/><circle cx="296" cy="312" r="2.05"/><circle cx="304" cy="312" r="2.05"/><circle cx="312" cy="312" r="2.05"/><circle cx="352" cy="312" r="2.05"/><circle cx="360" cy="312" r="2.05"/><circle cx="368" cy="312" r="2.05"/><circle cx="376" cy="312" r="2.05"/><circle cx="384" cy="312" r="2.05"/><circle cx="704" cy="312" r="2.05"/><circle cx="712" cy="312" r="2.05"/><circle cx="720" cy="312" r="2.05"/><circle cx="728" cy="312" r="2.05"/><circle cx="736" cy="312" r="2.05"/><circle cx="744" cy="312" r="2.05"/><circle cx="752" cy="312" r="2.05"/><circle cx="760" cy="312" r="2.05"/><circle cx="768" cy="312" r="2.05"/><circle cx="776" cy="312" r="2.05"/><circle cx="784" cy="312" r="2.05"/><circle cx="792" cy="312" r="2.05"/><circle cx="800" cy="312" r="2.05"/><circle cx="808" cy="312" r="2.05"/><circle cx="816" cy="312" r="2.05"/><circle cx="832" cy="312" r="2.05"/><circle cx="840" cy="312" r="2.05"/><circle cx="48" cy="320" r="2.05"/><circle cx="56" cy="320" r="2.05"/><circle cx="64" cy="320" r="2.05"/><circle cx="72" cy="320" r="2.05"/><circle cx="80" cy="320" r="2.05"/><circle cx="88" cy="320" r="2.05"/><circle cx="96" cy="320" r="2.05"/><circle cx="104" cy="320" r="2.05"/><circle cx="112" cy="320" r="2.05"/><circle cx="120" cy="320" r="2.05"/><circle cx="128" cy="320" r="2.05"/><circle cx="136" cy="320" r="2.05"/><circle cx="144" cy="320" r="2.05"/><circle cx="152" cy="320" r="2.05"/><circle cx="160" cy="320" r="2.05"/><circle cx="168" cy="320" r="2.05"/><circle cx="176" cy="320" r="2.05"/><circle cx="184" cy="320" r="2.05"/><circle cx="192" cy="320" r="2.05"/><circle cx="200" cy="320" r="2.05"/><circle cx="208" cy="320" r="2.05"/><circle cx="216" cy="320" r="2.05"/><circle cx="224" cy="320" r="2.05"/><circle cx="232" cy="320" r="2.05"/><circle cx="240" cy="320" r="2.05"/><circle cx="248" cy="320" r="2.05"/><circle cx="256" cy="320" r="2.05"/><circle cx="264" cy="320" r="2.05"/><circle cx="272" cy="320" r="2.05"/><circle cx="280" cy="320" r="2.05"/><circle cx="288" cy="320" r="2.05"/><circle cx="296" cy="320" r="2.05"/><circle cx="304" cy="320" r="2.05"/><circle cx="368" cy="320" r="2.05"/><circle cx="384" cy="320" r="2.05"/><circle cx="712" cy="320" r="2.05"/><circle cx="720" cy="320" r="2.05"/><circle cx="728" cy="320" r="2.05"/><circle cx="736" cy="320" r="2.05"/><circle cx="744" cy="320" r="2.05"/><circle cx="752" cy="320" r="2.05"/><circle cx="760" cy="320" r="2.05"/><circle cx="768" cy="320" r="2.05"/><circle cx="792" cy="320" r="2.05"/><circle cx="800" cy="320" r="2.05"/><circle cx="808" cy="320" r="2.05"/><circle cx="816" cy="320" r="2.05"/><circle cx="824" cy="320" r="2.05"/><circle cx="48" cy="328" r="2.05"/><circle cx="56" cy="328" r="2.05"/><circle cx="64" cy="328" r="2.05"/><circle cx="72" cy="328" r="2.05"/><circle cx="80" cy="328" r="2.05"/><circle cx="88" cy="328" r="2.05"/><circle cx="96" cy="328" r="2.05"/><circle cx="104" cy="328" r="2.05"/><circle cx="112" cy="328" r="2.05"/><circle cx="120" cy="328" r="2.05"/><circle cx="128" cy="328" r="2.05"/><circle cx="136" cy="328" r="2.05"/><circle cx="144" cy="328" r="2.05"/><circle cx="152" cy="328" r="2.05"/><circle cx="160" cy="328" r="2.05"/><circle cx="168" cy="328" r="2.05"/><circle cx="176" cy="328" r="2.05"/><circle cx="184" cy="328" r="2.05"/><circle cx="192" cy="328" r="2.05"/><circle cx="200" cy="328" r="2.05"/><circle cx="208" cy="328" r="2.05"/><circle cx="216" cy="328" r="2.05"/><circle cx="224" cy="328" r="2.05"/><circle cx="232" cy="328" r="2.05"/><circle cx="240" cy="328" r="2.05"/><circle cx="248" cy="328" r="2.05"/><circle cx="256" cy="328" r="2.05"/><circle cx="264" cy="328" r="2.05"/><circle cx="272" cy="328" r="2.05"/><circle cx="280" cy="328" r="2.05"/><circle cx="288" cy="328" r="2.05"/><circle cx="296" cy="328" r="2.05"/><circle cx="304" cy="328" r="2.05"/><circle cx="312" cy="328" r="2.05"/><circle cx="320" cy="328" r="2.05"/><circle cx="328" cy="328" r="2.05"/><circle cx="720" cy="328" r="2.05"/><circle cx="728" cy="328" r="2.05"/><circle cx="736" cy="328" r="2.05"/><circle cx="744" cy="328" r="2.05"/><circle cx="752" cy="328" r="2.05"/><circle cx="760" cy="328" r="2.05"/><circle cx="776" cy="328" r="2.05"/><circle cx="784" cy="328" r="2.05"/><circle cx="808" cy="328" r="2.05"/><circle cx="816" cy="328" r="2.05"/><circle cx="824" cy="328" r="2.05"/><circle cx="832" cy="328" r="2.05"/><circle cx="848" cy="328" r="2.05"/><circle cx="40" cy="336" r="2.05"/><circle cx="48" cy="336" r="2.05"/><circle cx="56" cy="336" r="2.05"/><circle cx="64" cy="336" r="2.05"/><circle cx="72" cy="336" r="2.05"/><circle cx="80" cy="336" r="2.05"/><circle cx="88" cy="336" r="2.05"/><circle cx="96" cy="336" r="2.05"/><circle cx="104" cy="336" r="2.05"/><circle cx="112" cy="336" r="2.05"/><circle cx="120" cy="336" r="2.05"/><circle cx="128" cy="336" r="2.05"/><circle cx="136" cy="336" r="2.05"/><circle cx="144" cy="336" r="2.05"/><circle cx="152" cy="336" r="2.05"/><circle cx="160" cy="336" r="2.05"/><circle cx="168" cy="336" r="2.05"/><circle cx="176" cy="336" r="2.05"/><circle cx="184" cy="336" r="2.05"/><circle cx="192" cy="336" r="2.05"/><circle cx="200" cy="336" r="2.05"/><circle cx="208" cy="336" r="2.05"/><circle cx="216" cy="336" r="2.05"/><circle cx="224" cy="336" r="2.05"/><circle cx="232" cy="336" r="2.05"/><circle cx="240" cy="336" r="2.05"/><circle cx="248" cy="336" r="2.05"/><circle cx="256" cy="336" r="2.05"/><circle cx="264" cy="336" r="2.05"/><circle cx="272" cy="336" r="2.05"/><circle cx="296" cy="336" r="2.05"/><circle cx="304" cy="336" r="2.05"/><circle cx="688" cy="336" r="2.05"/><circle cx="696" cy="336" r="2.05"/><circle cx="704" cy="336" r="2.05"/><circle cx="712" cy="336" r="2.05"/><circle cx="720" cy="336" r="2.05"/><circle cx="728" cy="336" r="2.05"/><circle cx="736" cy="336" r="2.05"/><circle cx="744" cy="336" r="2.05"/><circle cx="776" cy="336" r="2.05"/><circle cx="792" cy="336" r="2.05"/><circle cx="800" cy="336" r="2.05"/><circle cx="824" cy="336" r="2.05"/><circle cx="832" cy="336" r="2.05"/><circle cx="840" cy="336" r="2.05"/><circle cx="848" cy="336" r="2.05"/><circle cx="856" cy="336" r="2.05"/><circle cx="864" cy="336" r="2.05"/><circle cx="40" cy="344" r="2.05"/><circle cx="48" cy="344" r="2.05"/><circle cx="56" cy="344" r="2.05"/><circle cx="64" cy="344" r="2.05"/><circle cx="72" cy="344" r="2.05"/><circle cx="80" cy="344" r="2.05"/><circle cx="88" cy="344" r="2.05"/><circle cx="96" cy="344" r="2.05"/><circle cx="104" cy="344" r="2.05"/><circle cx="112" cy="344" r="2.05"/><circle cx="120" cy="344" r="2.05"/><circle cx="128" cy="344" r="2.05"/><circle cx="136" cy="344" r="2.05"/><circle cx="144" cy="344" r="2.05"/><circle cx="152" cy="344" r="2.05"/><circle cx="160" cy="344" r="2.05"/><circle cx="168" cy="344" r="2.05"/><circle cx="176" cy="344" r="2.05"/><circle cx="184" cy="344" r="2.05"/><circle cx="192" cy="344" r="2.05"/><circle cx="200" cy="344" r="2.05"/><circle cx="208" cy="344" r="2.05"/><circle cx="216" cy="344" r="2.05"/><circle cx="224" cy="344" r="2.05"/><circle cx="232" cy="344" r="2.05"/><circle cx="240" cy="344" r="2.05"/><circle cx="248" cy="344" r="2.05"/><circle cx="256" cy="344" r="2.05"/><circle cx="688" cy="344" r="2.05"/><circle cx="696" cy="344" r="2.05"/><circle cx="704" cy="344" r="2.05"/><circle cx="712" cy="344" r="2.05"/><circle cx="720" cy="344" r="2.05"/><circle cx="728" cy="344" r="2.05"/><circle cx="736" cy="344" r="2.05"/><circle cx="744" cy="344" r="2.05"/><circle cx="808" cy="344" r="2.05"/><circle cx="816" cy="344" r="2.05"/><circle cx="832" cy="344" r="2.05"/><circle cx="840" cy="344" r="2.05"/><circle cx="856" cy="344" r="2.05"/><circle cx="864" cy="344" r="2.05"/><circle cx="872" cy="344" r="2.05"/><circle cx="40" cy="352" r="2.05"/><circle cx="48" cy="352" r="2.05"/><circle cx="56" cy="352" r="2.05"/><circle cx="64" cy="352" r="2.05"/><circle cx="72" cy="352" r="2.05"/><circle cx="80" cy="352" r="2.05"/><circle cx="88" cy="352" r="2.05"/><circle cx="96" cy="352" r="2.05"/><circle cx="104" cy="352" r="2.05"/><circle cx="112" cy="352" r="2.05"/><circle cx="120" cy="352" r="2.05"/><circle cx="128" cy="352" r="2.05"/><circle cx="136" cy="352" r="2.05"/><circle cx="144" cy="352" r="2.05"/><circle cx="152" cy="352" r="2.05"/><circle cx="160" cy="352" r="2.05"/><circle cx="168" cy="352" r="2.05"/><circle cx="176" cy="352" r="2.05"/><circle cx="184" cy="352" r="2.05"/><circle cx="192" cy="352" r="2.05"/><circle cx="200" cy="352" r="2.05"/><circle cx="208" cy="352" r="2.05"/><circle cx="216" cy="352" r="2.05"/><circle cx="224" cy="352" r="2.05"/><circle cx="232" cy="352" r="2.05"/><circle cx="240" cy="352" r="2.05"/><circle cx="696" cy="352" r="2.05"/><circle cx="704" cy="352" r="2.05"/><circle cx="712" cy="352" r="2.05"/><circle cx="720" cy="352" r="2.05"/><circle cx="728" cy="352" r="2.05"/><circle cx="736" cy="352" r="2.05"/><circle cx="840" cy="352" r="2.05"/><circle cx="856" cy="352" r="2.05"/><circle cx="864" cy="352" r="2.05"/><circle cx="872" cy="352" r="2.05"/><circle cx="880" cy="352" r="2.05"/><circle cx="32" cy="360" r="2.05"/><circle cx="40" cy="360" r="2.05"/><circle cx="48" cy="360" r="2.05"/><circle cx="56" cy="360" r="2.05"/><circle cx="64" cy="360" r="2.05"/><circle cx="72" cy="360" r="2.05"/><circle cx="80" cy="360" r="2.05"/><circle cx="88" cy="360" r="2.05"/><circle cx="96" cy="360" r="2.05"/><circle cx="104" cy="360" r="2.05"/><circle cx="112" cy="360" r="2.05"/><circle cx="120" cy="360" r="2.05"/><circle cx="128" cy="360" r="2.05"/><circle cx="136" cy="360" r="2.05"/><circle cx="144" cy="360" r="2.05"/><circle cx="152" cy="360" r="2.05"/><circle cx="160" cy="360" r="2.05"/><circle cx="168" cy="360" r="2.05"/><circle cx="176" cy="360" r="2.05"/><circle cx="184" cy="360" r="2.05"/><circle cx="192" cy="360" r="2.05"/><circle cx="200" cy="360" r="2.05"/><circle cx="208" cy="360" r="2.05"/><circle cx="216" cy="360" r="2.05"/><circle cx="224" cy="360" r="2.05"/><circle cx="696" cy="360" r="2.05"/><circle cx="704" cy="360" r="2.05"/><circle cx="712" cy="360" r="2.05"/><circle cx="720" cy="360" r="2.05"/><circle cx="728" cy="360" r="2.05"/><circle cx="736" cy="360" r="2.05"/><circle cx="744" cy="360" r="2.05"/><circle cx="848" cy="360" r="2.05"/><circle cx="872" cy="360" r="2.05"/><circle cx="880" cy="360" r="2.05"/><circle cx="888" cy="360" r="2.05"/><circle cx="32" cy="368" r="2.05"/><circle cx="40" cy="368" r="2.05"/><circle cx="48" cy="368" r="2.05"/><circle cx="56" cy="368" r="2.05"/><circle cx="64" cy="368" r="2.05"/><circle cx="72" cy="368" r="2.05"/><circle cx="80" cy="368" r="2.05"/><circle cx="88" cy="368" r="2.05"/><circle cx="96" cy="368" r="2.05"/><circle cx="104" cy="368" r="2.05"/><circle cx="112" cy="368" r="2.05"/><circle cx="120" cy="368" r="2.05"/><circle cx="128" cy="368" r="2.05"/><circle cx="136" cy="368" r="2.05"/><circle cx="144" cy="368" r="2.05"/><circle cx="152" cy="368" r="2.05"/><circle cx="160" cy="368" r="2.05"/><circle cx="168" cy="368" r="2.05"/><circle cx="176" cy="368" r="2.05"/><circle cx="184" cy="368" r="2.05"/><circle cx="192" cy="368" r="2.05"/><circle cx="200" cy="368" r="2.05"/><circle cx="208" cy="368" r="2.05"/><circle cx="216" cy="368" r="2.05"/><circle cx="704" cy="368" r="2.05"/><circle cx="712" cy="368" r="2.05"/><circle cx="720" cy="368" r="2.05"/><circle cx="728" cy="368" r="2.05"/><circle cx="736" cy="368" r="2.05"/><circle cx="744" cy="368" r="2.05"/><circle cx="888" cy="368" r="2.05"/><circle cx="896" cy="368" r="2.05"/><circle cx="32" cy="376" r="2.05"/><circle cx="40" cy="376" r="2.05"/><circle cx="48" cy="376" r="2.05"/><circle cx="56" cy="376" r="2.05"/><circle cx="64" cy="376" r="2.05"/><circle cx="72" cy="376" r="2.05"/><circle cx="80" cy="376" r="2.05"/><circle cx="88" cy="376" r="2.05"/><circle cx="96" cy="376" r="2.05"/><circle cx="104" cy="376" r="2.05"/><circle cx="112" cy="376" r="2.05"/><circle cx="120" cy="376" r="2.05"/><circle cx="128" cy="376" r="2.05"/><circle cx="136" cy="376" r="2.05"/><circle cx="144" cy="376" r="2.05"/><circle cx="152" cy="376" r="2.05"/><circle cx="160" cy="376" r="2.05"/><circle cx="168" cy="376" r="2.05"/><circle cx="176" cy="376" r="2.05"/><circle cx="184" cy="376" r="2.05"/><circle cx="192" cy="376" r="2.05"/><circle cx="200" cy="376" r="2.05"/><circle cx="208" cy="376" r="2.05"/><circle cx="704" cy="376" r="2.05"/><circle cx="720" cy="376" r="2.05"/><circle cx="728" cy="376" r="2.05"/><circle cx="736" cy="376" r="2.05"/><circle cx="744" cy="376" r="2.05"/><circle cx="768" cy="376" r="2.05"/><circle cx="776" cy="376" r="2.05"/><circle cx="784" cy="376" r="2.05"/><circle cx="792" cy="376" r="2.05"/><circle cx="800" cy="376" r="2.05"/><circle cx="808" cy="376" r="2.05"/><circle cx="904" cy="376" r="2.05"/><circle cx="24" cy="384" r="2.05"/><circle cx="32" cy="384" r="2.05"/><circle cx="40" cy="384" r="2.05"/><circle cx="48" cy="384" r="2.05"/><circle cx="56" cy="384" r="2.05"/><circle cx="64" cy="384" r="2.05"/><circle cx="72" cy="384" r="2.05"/><circle cx="80" cy="384" r="2.05"/><circle cx="88" cy="384" r="2.05"/><circle cx="96" cy="384" r="2.05"/><circle cx="104" cy="384" r="2.05"/><circle cx="112" cy="384" r="2.05"/><circle cx="120" cy="384" r="2.05"/><circle cx="128" cy="384" r="2.05"/><circle cx="136" cy="384" r="2.05"/><circle cx="144" cy="384" r="2.05"/><circle cx="152" cy="384" r="2.05"/><circle cx="160" cy="384" r="2.05"/><circle cx="168" cy="384" r="2.05"/><circle cx="176" cy="384" r="2.05"/><circle cx="184" cy="384" r="2.05"/><circle cx="192" cy="384" r="2.05"/><circle cx="200" cy="384" r="2.05"/><circle cx="208" cy="384" r="2.05"/><circle cx="728" cy="384" r="2.05"/><circle cx="760" cy="384" r="2.05"/><circle cx="768" cy="384" r="2.05"/><circle cx="776" cy="384" r="2.05"/><circle cx="784" cy="384" r="2.05"/><circle cx="792" cy="384" r="2.05"/><circle cx="800" cy="384" r="2.05"/><circle cx="808" cy="384" r="2.05"/><circle cx="816" cy="384" r="2.05"/><circle cx="904" cy="384" r="2.05"/><circle cx="912" cy="384" r="2.05"/><circle cx="24" cy="392" r="2.05"/><circle cx="32" cy="392" r="2.05"/><circle cx="40" cy="392" r="2.05"/><circle cx="48" cy="392" r="2.05"/><circle cx="56" cy="392" r="2.05"/><circle cx="64" cy="392" r="2.05"/><circle cx="72" cy="392" r="2.05"/><circle cx="80" cy="392" r="2.05"/><circle cx="88" cy="392" r="2.05"/><circle cx="96" cy="392" r="2.05"/><circle cx="104" cy="392" r="2.05"/><circle cx="112" cy="392" r="2.05"/><circle cx="120" cy="392" r="2.05"/><circle cx="128" cy="392" r="2.05"/><circle cx="136" cy="392" r="2.05"/><circle cx="144" cy="392" r="2.05"/><circle cx="152" cy="392" r="2.05"/><circle cx="160" cy="392" r="2.05"/><circle cx="168" cy="392" r="2.05"/><circle cx="176" cy="392" r="2.05"/><circle cx="184" cy="392" r="2.05"/><circle cx="192" cy="392" r="2.05"/><circle cx="200" cy="392" r="2.05"/><circle cx="728" cy="392" r="2.05"/><circle cx="736" cy="392" r="2.05"/><circle cx="744" cy="392" r="2.05"/><circle cx="752" cy="392" r="2.05"/><circle cx="760" cy="392" r="2.05"/><circle cx="768" cy="392" r="2.05"/><circle cx="776" cy="392" r="2.05"/><circle cx="784" cy="392" r="2.05"/><circle cx="792" cy="392" r="2.05"/><circle cx="800" cy="392" r="2.05"/><circle cx="808" cy="392" r="2.05"/><circle cx="816" cy="392" r="2.05"/><circle cx="824" cy="392" r="2.05"/><circle cx="872" cy="392" r="2.05"/><circle cx="912" cy="392" r="2.05"/><circle cx="24" cy="400" r="2.05"/><circle cx="32" cy="400" r="2.05"/><circle cx="40" cy="400" r="2.05"/><circle cx="48" cy="400" r="2.05"/><circle cx="56" cy="400" r="2.05"/><circle cx="64" cy="400" r="2.05"/><circle cx="72" cy="400" r="2.05"/><circle cx="80" cy="400" r="2.05"/><circle cx="88" cy="400" r="2.05"/><circle cx="96" cy="400" r="2.05"/><circle cx="104" cy="400" r="2.05"/><circle cx="112" cy="400" r="2.05"/><circle cx="120" cy="400" r="2.05"/><circle cx="128" cy="400" r="2.05"/><circle cx="136" cy="400" r="2.05"/><circle cx="144" cy="400" r="2.05"/><circle cx="152" cy="400" r="2.05"/><circle cx="160" cy="400" r="2.05"/><circle cx="168" cy="400" r="2.05"/><circle cx="176" cy="400" r="2.05"/><circle cx="728" cy="400" r="2.05"/><circle cx="736" cy="400" r="2.05"/><circle cx="744" cy="400" r="2.05"/><circle cx="752" cy="400" r="2.05"/><circle cx="760" cy="400" r="2.05"/><circle cx="768" cy="400" r="2.05"/><circle cx="776" cy="400" r="2.05"/><circle cx="784" cy="400" r="2.05"/><circle cx="792" cy="400" r="2.05"/><circle cx="800" cy="400" r="2.05"/><circle cx="808" cy="400" r="2.05"/><circle cx="816" cy="400" r="2.05"/><circle cx="824" cy="400" r="2.05"/><circle cx="832" cy="400" r="2.05"/><circle cx="840" cy="400" r="2.05"/><circle cx="848" cy="400" r="2.05"/><circle cx="872" cy="400" r="2.05"/><circle cx="880" cy="400" r="2.05"/><circle cx="888" cy="400" r="2.05"/><circle cx="896" cy="400" r="2.05"/><circle cx="904" cy="400" r="2.05"/><circle cx="912" cy="400" r="2.05"/><circle cx="920" cy="400" r="2.05"/><circle cx="16" cy="408" r="2.05"/><circle cx="24" cy="408" r="2.05"/><circle cx="32" cy="408" r="2.05"/><circle cx="40" cy="408" r="2.05"/><circle cx="48" cy="408" r="2.05"/><circle cx="56" cy="408" r="2.05"/><circle cx="64" cy="408" r="2.05"/><circle cx="72" cy="408" r="2.05"/><circle cx="80" cy="408" r="2.05"/><circle cx="88" cy="408" r="2.05"/><circle cx="96" cy="408" r="2.05"/><circle cx="104" cy="408" r="2.05"/><circle cx="112" cy="408" r="2.05"/><circle cx="120" cy="408" r="2.05"/><circle cx="128" cy="408" r="2.05"/><circle cx="136" cy="408" r="2.05"/><circle cx="144" cy="408" r="2.05"/><circle cx="152" cy="408" r="2.05"/><circle cx="160" cy="408" r="2.05"/><circle cx="720" cy="408" r="2.05"/><circle cx="728" cy="408" r="2.05"/><circle cx="736" cy="408" r="2.05"/><circle cx="744" cy="408" r="2.05"/><circle cx="752" cy="408" r="2.05"/><circle cx="760" cy="408" r="2.05"/><circle cx="768" cy="408" r="2.05"/><circle cx="776" cy="408" r="2.05"/><circle cx="784" cy="408" r="2.05"/><circle cx="792" cy="408" r="2.05"/><circle cx="800" cy="408" r="2.05"/><circle cx="808" cy="408" r="2.05"/><circle cx="816" cy="408" r="2.05"/><circle cx="824" cy="408" r="2.05"/><circle cx="832" cy="408" r="2.05"/><circle cx="840" cy="408" r="2.05"/><circle cx="848" cy="408" r="2.05"/><circle cx="856" cy="408" r="2.05"/><circle cx="864" cy="408" r="2.05"/><circle cx="880" cy="408" r="2.05"/><circle cx="888" cy="408" r="2.05"/><circle cx="896" cy="408" r="2.05"/><circle cx="904" cy="408" r="2.05"/><circle cx="912" cy="408" r="2.05"/><circle cx="920" cy="408" r="2.05"/><circle cx="928" cy="408" r="2.05"/><circle cx="16" cy="416" r="2.05"/><circle cx="24" cy="416" r="2.05"/><circle cx="32" cy="416" r="2.05"/><circle cx="40" cy="416" r="2.05"/><circle cx="48" cy="416" r="2.05"/><circle cx="56" cy="416" r="2.05"/><circle cx="64" cy="416" r="2.05"/><circle cx="72" cy="416" r="2.05"/><circle cx="80" cy="416" r="2.05"/><circle cx="88" cy="416" r="2.05"/><circle cx="96" cy="416" r="2.05"/><circle cx="104" cy="416" r="2.05"/><circle cx="112" cy="416" r="2.05"/><circle cx="120" cy="416" r="2.05"/><circle cx="128" cy="416" r="2.05"/><circle cx="136" cy="416" r="2.05"/><circle cx="144" cy="416" r="2.05"/><circle cx="152" cy="416" r="2.05"/><circle cx="720" cy="416" r="2.05"/><circle cx="728" cy="416" r="2.05"/><circle cx="736" cy="416" r="2.05"/><circle cx="744" cy="416" r="2.05"/><circle cx="752" cy="416" r="2.05"/><circle cx="760" cy="416" r="2.05"/><circle cx="768" cy="416" r="2.05"/><circle cx="776" cy="416" r="2.05"/><circle cx="784" cy="416" r="2.05"/><circle cx="792" cy="416" r="2.05"/><circle cx="800" cy="416" r="2.05"/><circle cx="808" cy="416" r="2.05"/><circle cx="816" cy="416" r="2.05"/><circle cx="824" cy="416" r="2.05"/><circle cx="832" cy="416" r="2.05"/><circle cx="840" cy="416" r="2.05"/><circle cx="848" cy="416" r="2.05"/><circle cx="856" cy="416" r="2.05"/><circle cx="864" cy="416" r="2.05"/><circle cx="872" cy="416" r="2.05"/><circle cx="880" cy="416" r="2.05"/><circle cx="888" cy="416" r="2.05"/><circle cx="896" cy="416" r="2.05"/><circle cx="904" cy="416" r="2.05"/><circle cx="912" cy="416" r="2.05"/><circle cx="920" cy="416" r="2.05"/><circle cx="928" cy="416" r="2.05"/><circle cx="16" cy="424" r="2.05"/><circle cx="24" cy="424" r="2.05"/><circle cx="32" cy="424" r="2.05"/><circle cx="40" cy="424" r="2.05"/><circle cx="48" cy="424" r="2.05"/><circle cx="56" cy="424" r="2.05"/><circle cx="64" cy="424" r="2.05"/><circle cx="88" cy="424" r="2.05"/><circle cx="96" cy="424" r="2.05"/><circle cx="128" cy="424" r="2.05"/><circle cx="144" cy="424" r="2.05"/><circle cx="152" cy="424" r="2.05"/><circle cx="728" cy="424" r="2.05"/><circle cx="736" cy="424" r="2.05"/><circle cx="744" cy="424" r="2.05"/><circle cx="752" cy="424" r="2.05"/><circle cx="760" cy="424" r="2.05"/><circle cx="768" cy="424" r="2.05"/><circle cx="776" cy="424" r="2.05"/><circle cx="784" cy="424" r="2.05"/><circle cx="792" cy="424" r="2.05"/><circle cx="800" cy="424" r="2.05"/><circle cx="808" cy="424" r="2.05"/><circle cx="816" cy="424" r="2.05"/><circle cx="824" cy="424" r="2.05"/><circle cx="832" cy="424" r="2.05"/><circle cx="840" cy="424" r="2.05"/><circle cx="848" cy="424" r="2.05"/><circle cx="856" cy="424" r="2.05"/><circle cx="864" cy="424" r="2.05"/><circle cx="872" cy="424" r="2.05"/><circle cx="880" cy="424" r="2.05"/><circle cx="888" cy="424" r="2.05"/><circle cx="896" cy="424" r="2.05"/><circle cx="904" cy="424" r="2.05"/><circle cx="912" cy="424" r="2.05"/><circle cx="920" cy="424" r="2.05"/><circle cx="928" cy="424" r="2.05"/><circle cx="936" cy="424" r="2.05"/><circle cx="16" cy="432" r="2.05"/><circle cx="24" cy="432" r="2.05"/><circle cx="32" cy="432" r="2.05"/><circle cx="40" cy="432" r="2.05"/><circle cx="48" cy="432" r="2.05"/><circle cx="144" cy="432" r="2.05"/><circle cx="152" cy="432" r="2.05"/><circle cx="720" cy="432" r="2.05"/><circle cx="728" cy="432" r="2.05"/><circle cx="736" cy="432" r="2.05"/><circle cx="744" cy="432" r="2.05"/><circle cx="752" cy="432" r="2.05"/><circle cx="760" cy="432" r="2.05"/><circle cx="768" cy="432" r="2.05"/><circle cx="776" cy="432" r="2.05"/><circle cx="784" cy="432" r="2.05"/><circle cx="792" cy="432" r="2.05"/><circle cx="800" cy="432" r="2.05"/><circle cx="808" cy="432" r="2.05"/><circle cx="816" cy="432" r="2.05"/><circle cx="824" cy="432" r="2.05"/><circle cx="832" cy="432" r="2.05"/><circle cx="840" cy="432" r="2.05"/><circle cx="848" cy="432" r="2.05"/><circle cx="856" cy="432" r="2.05"/><circle cx="864" cy="432" r="2.05"/><circle cx="872" cy="432" r="2.05"/><circle cx="880" cy="432" r="2.05"/><circle cx="888" cy="432" r="2.05"/><circle cx="896" cy="432" r="2.05"/><circle cx="904" cy="432" r="2.05"/><circle cx="912" cy="432" r="2.05"/><circle cx="920" cy="432" r="2.05"/><circle cx="928" cy="432" r="2.05"/><circle cx="944" cy="432" r="2.05"/><circle cx="16" cy="440" r="2.05"/><circle cx="24" cy="440" r="2.05"/><circle cx="32" cy="440" r="2.05"/><circle cx="40" cy="440" r="2.05"/><circle cx="144" cy="440" r="2.05"/><circle cx="152" cy="440" r="2.05"/><circle cx="712" cy="440" r="2.05"/><circle cx="720" cy="440" r="2.05"/><circle cx="728" cy="440" r="2.05"/><circle cx="736" cy="440" r="2.05"/><circle cx="744" cy="440" r="2.05"/><circle cx="752" cy="440" r="2.05"/><circle cx="760" cy="440" r="2.05"/><circle cx="768" cy="440" r="2.05"/><circle cx="776" cy="440" r="2.05"/><circle cx="784" cy="440" r="2.05"/><circle cx="792" cy="440" r="2.05"/><circle cx="800" cy="440" r="2.05"/><circle cx="808" cy="440" r="2.05"/><circle cx="816" cy="440" r="2.05"/><circle cx="824" cy="440" r="2.05"/><circle cx="832" cy="440" r="2.05"/><circle cx="840" cy="440" r="2.05"/><circle cx="848" cy="440" r="2.05"/><circle cx="856" cy="440" r="2.05"/><circle cx="864" cy="440" r="2.05"/><circle cx="872" cy="440" r="2.05"/><circle cx="880" cy="440" r="2.05"/><circle cx="888" cy="440" r="2.05"/><circle cx="896" cy="440" r="2.05"/><circle cx="904" cy="440" r="2.05"/><circle cx="912" cy="440" r="2.05"/><circle cx="920" cy="440" r="2.05"/><circle cx="928" cy="440" r="2.05"/><circle cx="936" cy="440" r="2.05"/><circle cx="8" cy="448" r="2.05"/><circle cx="16" cy="448" r="2.05"/><circle cx="24" cy="448" r="2.05"/><circle cx="32" cy="448" r="2.05"/><circle cx="40" cy="448" r="2.05"/><circle cx="144" cy="448" r="2.05"/><circle cx="152" cy="448" r="2.05"/><circle cx="168" cy="448" r="2.05"/><circle cx="704" cy="448" r="2.05"/><circle cx="712" cy="448" r="2.05"/><circle cx="720" cy="448" r="2.05"/><circle cx="728" cy="448" r="2.05"/><circle cx="736" cy="448" r="2.05"/><circle cx="744" cy="448" r="2.05"/><circle cx="752" cy="448" r="2.05"/><circle cx="760" cy="448" r="2.05"/><circle cx="768" cy="448" r="2.05"/><circle cx="776" cy="448" r="2.05"/><circle cx="784" cy="448" r="2.05"/><circle cx="792" cy="448" r="2.05"/><circle cx="800" cy="448" r="2.05"/><circle cx="808" cy="448" r="2.05"/><circle cx="816" cy="448" r="2.05"/><circle cx="824" cy="448" r="2.05"/><circle cx="832" cy="448" r="2.05"/><circle cx="840" cy="448" r="2.05"/><circle cx="848" cy="448" r="2.05"/><circle cx="856" cy="448" r="2.05"/><circle cx="864" cy="448" r="2.05"/><circle cx="872" cy="448" r="2.05"/><circle cx="880" cy="448" r="2.05"/><circle cx="888" cy="448" r="2.05"/><circle cx="896" cy="448" r="2.05"/><circle cx="904" cy="448" r="2.05"/><circle cx="912" cy="448" r="2.05"/><circle cx="920" cy="448" r="2.05"/><circle cx="928" cy="448" r="2.05"/><circle cx="936" cy="448" r="2.05"/><circle cx="944" cy="448" r="2.05"/><circle cx="952" cy="448" r="2.05"/><circle cx="8" cy="456" r="2.05"/><circle cx="16" cy="456" r="2.05"/><circle cx="24" cy="456" r="2.05"/><circle cx="32" cy="456" r="2.05"/><circle cx="144" cy="456" r="2.05"/><circle cx="696" cy="456" r="2.05"/><circle cx="704" cy="456" r="2.05"/><circle cx="712" cy="456" r="2.05"/><circle cx="720" cy="456" r="2.05"/><circle cx="728" cy="456" r="2.05"/><circle cx="736" cy="456" r="2.05"/><circle cx="744" cy="456" r="2.05"/><circle cx="752" cy="456" r="2.05"/><circle cx="760" cy="456" r="2.05"/><circle cx="768" cy="456" r="2.05"/><circle cx="776" cy="456" r="2.05"/><circle cx="784" cy="456" r="2.05"/><circle cx="792" cy="456" r="2.05"/><circle cx="800" cy="456" r="2.05"/><circle cx="808" cy="456" r="2.05"/><circle cx="816" cy="456" r="2.05"/><circle cx="824" cy="456" r="2.05"/><circle cx="832" cy="456" r="2.05"/><circle cx="840" cy="456" r="2.05"/><circle cx="848" cy="456" r="2.05"/><circle cx="856" cy="456" r="2.05"/><circle cx="864" cy="456" r="2.05"/><circle cx="872" cy="456" r="2.05"/><circle cx="880" cy="456" r="2.05"/><circle cx="888" cy="456" r="2.05"/><circle cx="896" cy="456" r="2.05"/><circle cx="904" cy="456" r="2.05"/><circle cx="912" cy="456" r="2.05"/><circle cx="920" cy="456" r="2.05"/><circle cx="928" cy="456" r="2.05"/><circle cx="936" cy="456" r="2.05"/><circle cx="944" cy="456" r="2.05"/><circle cx="952" cy="456" r="2.05"/><circle cx="8" cy="464" r="2.05"/><circle cx="16" cy="464" r="2.05"/><circle cx="24" cy="464" r="2.05"/><circle cx="160" cy="464" r="2.05"/><circle cx="696" cy="464" r="2.05"/><circle cx="704" cy="464" r="2.05"/><circle cx="712" cy="464" r="2.05"/><circle cx="720" cy="464" r="2.05"/><circle cx="728" cy="464" r="2.05"/><circle cx="736" cy="464" r="2.05"/><circle cx="744" cy="464" r="2.05"/><circle cx="752" cy="464" r="2.05"/><circle cx="760" cy="464" r="2.05"/><circle cx="768" cy="464" r="2.05"/><circle cx="776" cy="464" r="2.05"/><circle cx="784" cy="464" r="2.05"/><circle cx="792" cy="464" r="2.05"/><circle cx="800" cy="464" r="2.05"/><circle cx="808" cy="464" r="2.05"/><circle cx="816" cy="464" r="2.05"/><circle cx="824" cy="464" r="2.05"/><circle cx="832" cy="464" r="2.05"/><circle cx="840" cy="464" r="2.05"/><circle cx="848" cy="464" r="2.05"/><circle cx="856" cy="464" r="2.05"/><circle cx="864" cy="464" r="2.05"/><circle cx="872" cy="464" r="2.05"/><circle cx="880" cy="464" r="2.05"/><circle cx="888" cy="464" r="2.05"/><circle cx="896" cy="464" r="2.05"/><circle cx="904" cy="464" r="2.05"/><circle cx="912" cy="464" r="2.05"/><circle cx="920" cy="464" r="2.05"/><circle cx="928" cy="464" r="2.05"/><circle cx="936" cy="464" r="2.05"/><circle cx="944" cy="464" r="2.05"/><circle cx="952" cy="464" r="2.05"/><circle cx="8" cy="472" r="2.05"/><circle cx="16" cy="472" r="2.05"/><circle cx="24" cy="472" r="2.05"/><circle cx="696" cy="472" r="2.05"/><circle cx="704" cy="472" r="2.05"/><circle cx="712" cy="472" r="2.05"/><circle cx="720" cy="472" r="2.05"/><circle cx="728" cy="472" r="2.05"/><circle cx="736" cy="472" r="2.05"/><circle cx="744" cy="472" r="2.05"/><circle cx="752" cy="472" r="2.05"/><circle cx="760" cy="472" r="2.05"/><circle cx="768" cy="472" r="2.05"/><circle cx="776" cy="472" r="2.05"/><circle cx="784" cy="472" r="2.05"/><circle cx="792" cy="472" r="2.05"/><circle cx="800" cy="472" r="2.05"/><circle cx="808" cy="472" r="2.05"/><circle cx="816" cy="472" r="2.05"/><circle cx="824" cy="472" r="2.05"/><circle cx="832" cy="472" r="2.05"/><circle cx="840" cy="472" r="2.05"/><circle cx="848" cy="472" r="2.05"/><circle cx="856" cy="472" r="2.05"/><circle cx="864" cy="472" r="2.05"/><circle cx="872" cy="472" r="2.05"/><circle cx="880" cy="472" r="2.05"/><circle cx="888" cy="472" r="2.05"/><circle cx="896" cy="472" r="2.05"/><circle cx="904" cy="472" r="2.05"/><circle cx="912" cy="472" r="2.05"/><circle cx="920" cy="472" r="2.05"/><circle cx="928" cy="472" r="2.05"/><circle cx="936" cy="472" r="2.05"/><circle cx="944" cy="472" r="2.05"/><circle cx="952" cy="472" r="2.05"/><circle cx="8" cy="480" r="2.05"/><circle cx="16" cy="480" r="2.05"/><circle cx="24" cy="480" r="2.05"/><circle cx="112" cy="480" r="2.05"/><circle cx="136" cy="480" r="2.05"/><circle cx="144" cy="480" r="2.05"/><circle cx="152" cy="480" r="2.05"/><circle cx="696" cy="480" r="2.05"/><circle cx="704" cy="480" r="2.05"/><circle cx="712" cy="480" r="2.05"/><circle cx="720" cy="480" r="2.05"/><circle cx="728" cy="480" r="2.05"/><circle cx="736" cy="480" r="2.05"/><circle cx="744" cy="480" r="2.05"/><circle cx="752" cy="480" r="2.05"/><circle cx="760" cy="480" r="2.05"/><circle cx="768" cy="480" r="2.05"/><circle cx="776" cy="480" r="2.05"/><circle cx="784" cy="480" r="2.05"/><circle cx="792" cy="480" r="2.05"/><circle cx="800" cy="480" r="2.05"/><circle cx="808" cy="480" r="2.05"/><circle cx="816" cy="480" r="2.05"/><circle cx="824" cy="480" r="2.05"/><circle cx="832" cy="480" r="2.05"/><circle cx="840" cy="480" r="2.05"/><circle cx="848" cy="480" r="2.05"/><circle cx="856" cy="480" r="2.05"/><circle cx="864" cy="480" r="2.05"/><circle cx="872" cy="480" r="2.05"/><circle cx="880" cy="480" r="2.05"/><circle cx="888" cy="480" r="2.05"/><circle cx="896" cy="480" r="2.05"/><circle cx="904" cy="480" r="2.05"/><circle cx="912" cy="480" r="2.05"/><circle cx="920" cy="480" r="2.05"/><circle cx="928" cy="480" r="2.05"/><circle cx="936" cy="480" r="2.05"/><circle cx="944" cy="480" r="2.05"/><circle cx="952" cy="480" r="2.05"/><circle cx="8" cy="488" r="2.05"/><circle cx="16" cy="488" r="2.05"/><circle cx="24" cy="488" r="2.05"/><circle cx="72" cy="488" r="2.05"/><circle cx="80" cy="488" r="2.05"/><circle cx="88" cy="488" r="2.05"/><circle cx="152" cy="488" r="2.05"/><circle cx="160" cy="488" r="2.05"/><circle cx="688" cy="488" r="2.05"/><circle cx="696" cy="488" r="2.05"/><circle cx="704" cy="488" r="2.05"/><circle cx="712" cy="488" r="2.05"/><circle cx="720" cy="488" r="2.05"/><circle cx="728" cy="488" r="2.05"/><circle cx="736" cy="488" r="2.05"/><circle cx="744" cy="488" r="2.05"/><circle cx="752" cy="488" r="2.05"/><circle cx="760" cy="488" r="2.05"/><circle cx="768" cy="488" r="2.05"/><circle cx="776" cy="488" r="2.05"/><circle cx="784" cy="488" r="2.05"/><circle cx="792" cy="488" r="2.05"/><circle cx="800" cy="488" r="2.05"/><circle cx="808" cy="488" r="2.05"/><circle cx="816" cy="488" r="2.05"/><circle cx="824" cy="488" r="2.05"/><circle cx="832" cy="488" r="2.05"/><circle cx="840" cy="488" r="2.05"/><circle cx="848" cy="488" r="2.05"/><circle cx="856" cy="488" r="2.05"/><circle cx="864" cy="488" r="2.05"/><circle cx="872" cy="488" r="2.05"/><circle cx="880" cy="488" r="2.05"/><circle cx="888" cy="488" r="2.05"/><circle cx="896" cy="488" r="2.05"/><circle cx="904" cy="488" r="2.05"/><circle cx="912" cy="488" r="2.05"/><circle cx="920" cy="488" r="2.05"/><circle cx="928" cy="488" r="2.05"/><circle cx="936" cy="488" r="2.05"/><circle cx="944" cy="488" r="2.05"/><circle cx="952" cy="488" r="2.05"/><circle cx="8" cy="496" r="2.05"/><circle cx="16" cy="496" r="2.05"/><circle cx="24" cy="496" r="2.05"/><circle cx="64" cy="496" r="2.05"/><circle cx="72" cy="496" r="2.05"/><circle cx="80" cy="496" r="2.05"/><circle cx="168" cy="496" r="2.05"/><circle cx="176" cy="496" r="2.05"/><circle cx="696" cy="496" r="2.05"/><circle cx="704" cy="496" r="2.05"/><circle cx="712" cy="496" r="2.05"/><circle cx="720" cy="496" r="2.05"/><circle cx="728" cy="496" r="2.05"/><circle cx="736" cy="496" r="2.05"/><circle cx="744" cy="496" r="2.05"/><circle cx="752" cy="496" r="2.05"/><circle cx="760" cy="496" r="2.05"/><circle cx="768" cy="496" r="2.05"/><circle cx="776" cy="496" r="2.05"/><circle cx="784" cy="496" r="2.05"/><circle cx="792" cy="496" r="2.05"/><circle cx="800" cy="496" r="2.05"/><circle cx="808" cy="496" r="2.05"/><circle cx="816" cy="496" r="2.05"/><circle cx="824" cy="496" r="2.05"/><circle cx="832" cy="496" r="2.05"/><circle cx="840" cy="496" r="2.05"/><circle cx="848" cy="496" r="2.05"/><circle cx="856" cy="496" r="2.05"/><circle cx="864" cy="496" r="2.05"/><circle cx="872" cy="496" r="2.05"/><circle cx="880" cy="496" r="2.05"/><circle cx="888" cy="496" r="2.05"/><circle cx="896" cy="496" r="2.05"/><circle cx="904" cy="496" r="2.05"/><circle cx="912" cy="496" r="2.05"/><circle cx="920" cy="496" r="2.05"/><circle cx="928" cy="496" r="2.05"/><circle cx="936" cy="496" r="2.05"/><circle cx="944" cy="496" r="2.05"/><circle cx="952" cy="496" r="2.05"/><circle cx="8" cy="504" r="2.05"/><circle cx="16" cy="504" r="2.05"/><circle cx="24" cy="504" r="2.05"/><circle cx="32" cy="504" r="2.05"/><circle cx="40" cy="504" r="2.05"/><circle cx="48" cy="504" r="2.05"/><circle cx="56" cy="504" r="2.05"/><circle cx="64" cy="504" r="2.05"/><circle cx="72" cy="504" r="2.05"/><circle cx="80" cy="504" r="2.05"/><circle cx="200" cy="504" r="2.05"/><circle cx="208" cy="504" r="2.05"/><circle cx="216" cy="504" r="2.05"/><circle cx="696" cy="504" r="2.05"/><circle cx="704" cy="504" r="2.05"/><circle cx="712" cy="504" r="2.05"/><circle cx="720" cy="504" r="2.05"/><circle cx="728" cy="504" r="2.05"/><circle cx="736" cy="504" r="2.05"/><circle cx="744" cy="504" r="2.05"/><circle cx="752" cy="504" r="2.05"/><circle cx="760" cy="504" r="2.05"/><circle cx="768" cy="504" r="2.05"/><circle cx="776" cy="504" r="2.05"/><circle cx="784" cy="504" r="2.05"/><circle cx="792" cy="504" r="2.05"/><circle cx="800" cy="504" r="2.05"/><circle cx="808" cy="504" r="2.05"/><circle cx="816" cy="504" r="2.05"/><circle cx="824" cy="504" r="2.05"/><circle cx="832" cy="504" r="2.05"/><circle cx="840" cy="504" r="2.05"/><circle cx="848" cy="504" r="2.05"/><circle cx="856" cy="504" r="2.05"/><circle cx="864" cy="504" r="2.05"/><circle cx="872" cy="504" r="2.05"/><circle cx="880" cy="504" r="2.05"/><circle cx="888" cy="504" r="2.05"/><circle cx="896" cy="504" r="2.05"/><circle cx="904" cy="504" r="2.05"/><circle cx="912" cy="504" r="2.05"/><circle cx="920" cy="504" r="2.05"/><circle cx="928" cy="504" r="2.05"/><circle cx="936" cy="504" r="2.05"/><circle cx="944" cy="504" r="2.05"/><circle cx="952" cy="504" r="2.05"/><circle cx="8" cy="512" r="2.05"/><circle cx="16" cy="512" r="2.05"/><circle cx="24" cy="512" r="2.05"/><circle cx="32" cy="512" r="2.05"/><circle cx="40" cy="512" r="2.05"/><circle cx="48" cy="512" r="2.05"/><circle cx="56" cy="512" r="2.05"/><circle cx="64" cy="512" r="2.05"/><circle cx="72" cy="512" r="2.05"/><circle cx="152" cy="512" r="2.05"/><circle cx="160" cy="512" r="2.05"/><circle cx="184" cy="512" r="2.05"/><circle cx="192" cy="512" r="2.05"/><circle cx="200" cy="512" r="2.05"/><circle cx="208" cy="512" r="2.05"/><circle cx="216" cy="512" r="2.05"/><circle cx="224" cy="512" r="2.05"/><circle cx="704" cy="512" r="2.05"/><circle cx="712" cy="512" r="2.05"/><circle cx="720" cy="512" r="2.05"/><circle cx="728" cy="512" r="2.05"/><circle cx="736" cy="512" r="2.05"/><circle cx="744" cy="512" r="2.05"/><circle cx="752" cy="512" r="2.05"/><circle cx="760" cy="512" r="2.05"/><circle cx="768" cy="512" r="2.05"/><circle cx="776" cy="512" r="2.05"/><circle cx="784" cy="512" r="2.05"/><circle cx="792" cy="512" r="2.05"/><circle cx="800" cy="512" r="2.05"/><circle cx="808" cy="512" r="2.05"/><circle cx="816" cy="512" r="2.05"/><circle cx="824" cy="512" r="2.05"/><circle cx="832" cy="512" r="2.05"/><circle cx="840" cy="512" r="2.05"/><circle cx="848" cy="512" r="2.05"/><circle cx="856" cy="512" r="2.05"/><circle cx="864" cy="512" r="2.05"/><circle cx="872" cy="512" r="2.05"/><circle cx="880" cy="512" r="2.05"/><circle cx="888" cy="512" r="2.05"/><circle cx="896" cy="512" r="2.05"/><circle cx="904" cy="512" r="2.05"/><circle cx="912" cy="512" r="2.05"/><circle cx="920" cy="512" r="2.05"/><circle cx="928" cy="512" r="2.05"/><circle cx="936" cy="512" r="2.05"/><circle cx="944" cy="512" r="2.05"/><circle cx="952" cy="512" r="2.05"/><circle cx="16" cy="520" r="2.05"/><circle cx="24" cy="520" r="2.05"/><circle cx="32" cy="520" r="2.05"/><circle cx="40" cy="520" r="2.05"/><circle cx="48" cy="520" r="2.05"/><circle cx="56" cy="520" r="2.05"/><circle cx="64" cy="520" r="2.05"/><circle cx="704" cy="520" r="2.05"/><circle cx="712" cy="520" r="2.05"/><circle cx="720" cy="520" r="2.05"/><circle cx="728" cy="520" r="2.05"/><circle cx="736" cy="520" r="2.05"/><circle cx="744" cy="520" r="2.05"/><circle cx="752" cy="520" r="2.05"/><circle cx="760" cy="520" r="2.05"/><circle cx="768" cy="520" r="2.05"/><circle cx="776" cy="520" r="2.05"/><circle cx="784" cy="520" r="2.05"/><circle cx="792" cy="520" r="2.05"/><circle cx="800" cy="520" r="2.05"/><circle cx="808" cy="520" r="2.05"/><circle cx="816" cy="520" r="2.05"/><circle cx="824" cy="520" r="2.05"/><circle cx="832" cy="520" r="2.05"/><circle cx="840" cy="520" r="2.05"/><circle cx="848" cy="520" r="2.05"/><circle cx="856" cy="520" r="2.05"/><circle cx="864" cy="520" r="2.05"/><circle cx="872" cy="520" r="2.05"/><circle cx="880" cy="520" r="2.05"/><circle cx="888" cy="520" r="2.05"/><circle cx="896" cy="520" r="2.05"/><circle cx="904" cy="520" r="2.05"/><circle cx="912" cy="520" r="2.05"/><circle cx="920" cy="520" r="2.05"/><circle cx="928" cy="520" r="2.05"/><circle cx="936" cy="520" r="2.05"/><circle cx="944" cy="520" r="2.05"/><circle cx="952" cy="520" r="2.05"/><circle cx="40" cy="528" r="2.05"/><circle cx="48" cy="528" r="2.05"/><circle cx="56" cy="528" r="2.05"/><circle cx="64" cy="528" r="2.05"/><circle cx="72" cy="528" r="2.05"/><circle cx="80" cy="528" r="2.05"/><circle cx="88" cy="528" r="2.05"/><circle cx="96" cy="528" r="2.05"/><circle cx="704" cy="528" r="2.05"/><circle cx="712" cy="528" r="2.05"/><circle cx="720" cy="528" r="2.05"/><circle cx="728" cy="528" r="2.05"/><circle cx="736" cy="528" r="2.05"/><circle cx="744" cy="528" r="2.05"/><circle cx="752" cy="528" r="2.05"/><circle cx="760" cy="528" r="2.05"/><circle cx="768" cy="528" r="2.05"/><circle cx="776" cy="528" r="2.05"/><circle cx="784" cy="528" r="2.05"/><circle cx="792" cy="528" r="2.05"/><circle cx="800" cy="528" r="2.05"/><circle cx="808" cy="528" r="2.05"/><circle cx="816" cy="528" r="2.05"/><circle cx="824" cy="528" r="2.05"/><circle cx="832" cy="528" r="2.05"/><circle cx="840" cy="528" r="2.05"/><circle cx="848" cy="528" r="2.05"/><circle cx="856" cy="528" r="2.05"/><circle cx="864" cy="528" r="2.05"/><circle cx="872" cy="528" r="2.05"/><circle cx="880" cy="528" r="2.05"/><circle cx="888" cy="528" r="2.05"/><circle cx="896" cy="528" r="2.05"/><circle cx="904" cy="528" r="2.05"/><circle cx="912" cy="528" r="2.05"/><circle cx="920" cy="528" r="2.05"/><circle cx="928" cy="528" r="2.05"/><circle cx="936" cy="528" r="2.05"/><circle cx="944" cy="528" r="2.05"/><circle cx="952" cy="528" r="2.05"/><circle cx="48" cy="536" r="2.05"/><circle cx="56" cy="536" r="2.05"/><circle cx="64" cy="536" r="2.05"/><circle cx="72" cy="536" r="2.05"/><circle cx="80" cy="536" r="2.05"/><circle cx="88" cy="536" r="2.05"/><circle cx="96" cy="536" r="2.05"/><circle cx="104" cy="536" r="2.05"/><circle cx="696" cy="536" r="2.05"/><circle cx="704" cy="536" r="2.05"/><circle cx="712" cy="536" r="2.05"/><circle cx="720" cy="536" r="2.05"/><circle cx="728" cy="536" r="2.05"/><circle cx="736" cy="536" r="2.05"/><circle cx="744" cy="536" r="2.05"/><circle cx="752" cy="536" r="2.05"/><circle cx="760" cy="536" r="2.05"/><circle cx="768" cy="536" r="2.05"/><circle cx="776" cy="536" r="2.05"/><circle cx="784" cy="536" r="2.05"/><circle cx="792" cy="536" r="2.05"/><circle cx="800" cy="536" r="2.05"/><circle cx="808" cy="536" r="2.05"/><circle cx="816" cy="536" r="2.05"/><circle cx="824" cy="536" r="2.05"/><circle cx="832" cy="536" r="2.05"/><circle cx="840" cy="536" r="2.05"/><circle cx="848" cy="536" r="2.05"/><circle cx="856" cy="536" r="2.05"/><circle cx="864" cy="536" r="2.05"/><circle cx="872" cy="536" r="2.05"/><circle cx="880" cy="536" r="2.05"/><circle cx="888" cy="536" r="2.05"/><circle cx="896" cy="536" r="2.05"/><circle cx="904" cy="536" r="2.05"/><circle cx="912" cy="536" r="2.05"/><circle cx="920" cy="536" r="2.05"/><circle cx="928" cy="536" r="2.05"/><circle cx="936" cy="536" r="2.05"/><circle cx="944" cy="536" r="2.05"/><circle cx="952" cy="536" r="2.05"/><circle cx="64" cy="544" r="2.05"/><circle cx="72" cy="544" r="2.05"/><circle cx="80" cy="544" r="2.05"/><circle cx="88" cy="544" r="2.05"/><circle cx="96" cy="544" r="2.05"/><circle cx="696" cy="544" r="2.05"/><circle cx="704" cy="544" r="2.05"/><circle cx="712" cy="544" r="2.05"/><circle cx="720" cy="544" r="2.05"/><circle cx="728" cy="544" r="2.05"/><circle cx="736" cy="544" r="2.05"/><circle cx="744" cy="544" r="2.05"/><circle cx="752" cy="544" r="2.05"/><circle cx="760" cy="544" r="2.05"/><circle cx="768" cy="544" r="2.05"/><circle cx="776" cy="544" r="2.05"/><circle cx="784" cy="544" r="2.05"/><circle cx="792" cy="544" r="2.05"/><circle cx="800" cy="544" r="2.05"/><circle cx="808" cy="544" r="2.05"/><circle cx="816" cy="544" r="2.05"/><circle cx="824" cy="544" r="2.05"/><circle cx="832" cy="544" r="2.05"/><circle cx="840" cy="544" r="2.05"/><circle cx="848" cy="544" r="2.05"/><circle cx="856" cy="544" r="2.05"/><circle cx="864" cy="544" r="2.05"/><circle cx="872" cy="544" r="2.05"/><circle cx="880" cy="544" r="2.05"/><circle cx="888" cy="544" r="2.05"/><circle cx="896" cy="544" r="2.05"/><circle cx="904" cy="544" r="2.05"/><circle cx="912" cy="544" r="2.05"/><circle cx="920" cy="544" r="2.05"/><circle cx="928" cy="544" r="2.05"/><circle cx="936" cy="544" r="2.05"/><circle cx="944" cy="544" r="2.05"/><circle cx="952" cy="544" r="2.05"/><circle cx="80" cy="552" r="2.05"/><circle cx="88" cy="552" r="2.05"/><circle cx="96" cy="552" r="2.05"/><circle cx="704" cy="552" r="2.05"/><circle cx="712" cy="552" r="2.05"/><circle cx="720" cy="552" r="2.05"/><circle cx="728" cy="552" r="2.05"/><circle cx="736" cy="552" r="2.05"/><circle cx="744" cy="552" r="2.05"/><circle cx="752" cy="552" r="2.05"/><circle cx="760" cy="552" r="2.05"/><circle cx="768" cy="552" r="2.05"/><circle cx="776" cy="552" r="2.05"/><circle cx="784" cy="552" r="2.05"/><circle cx="792" cy="552" r="2.05"/><circle cx="800" cy="552" r="2.05"/><circle cx="808" cy="552" r="2.05"/><circle cx="816" cy="552" r="2.05"/><circle cx="824" cy="552" r="2.05"/><circle cx="832" cy="552" r="2.05"/><circle cx="840" cy="552" r="2.05"/><circle cx="848" cy="552" r="2.05"/><circle cx="856" cy="552" r="2.05"/><circle cx="864" cy="552" r="2.05"/><circle cx="872" cy="552" r="2.05"/><circle cx="880" cy="552" r="2.05"/><circle cx="888" cy="552" r="2.05"/><circle cx="896" cy="552" r="2.05"/><circle cx="904" cy="552" r="2.05"/><circle cx="912" cy="552" r="2.05"/><circle cx="920" cy="552" r="2.05"/><circle cx="928" cy="552" r="2.05"/><circle cx="936" cy="552" r="2.05"/><circle cx="944" cy="552" r="2.05"/><circle cx="952" cy="552" r="2.05"/><circle cx="80" cy="560" r="2.05"/><circle cx="88" cy="560" r="2.05"/><circle cx="96" cy="560" r="2.05"/><circle cx="192" cy="560" r="2.05"/><circle cx="704" cy="560" r="2.05"/><circle cx="712" cy="560" r="2.05"/><circle cx="720" cy="560" r="2.05"/><circle cx="728" cy="560" r="2.05"/><circle cx="736" cy="560" r="2.05"/><circle cx="744" cy="560" r="2.05"/><circle cx="752" cy="560" r="2.05"/><circle cx="760" cy="560" r="2.05"/><circle cx="768" cy="560" r="2.05"/><circle cx="776" cy="560" r="2.05"/><circle cx="784" cy="560" r="2.05"/><circle cx="792" cy="560" r="2.05"/><circle cx="800" cy="560" r="2.05"/><circle cx="808" cy="560" r="2.05"/><circle cx="816" cy="560" r="2.05"/><circle cx="824" cy="560" r="2.05"/><circle cx="832" cy="560" r="2.05"/><circle cx="840" cy="560" r="2.05"/><circle cx="848" cy="560" r="2.05"/><circle cx="856" cy="560" r="2.05"/><circle cx="864" cy="560" r="2.05"/><circle cx="872" cy="560" r="2.05"/><circle cx="880" cy="560" r="2.05"/><circle cx="888" cy="560" r="2.05"/><circle cx="896" cy="560" r="2.05"/><circle cx="904" cy="560" r="2.05"/><circle cx="912" cy="560" r="2.05"/><circle cx="920" cy="560" r="2.05"/><circle cx="928" cy="560" r="2.05"/><circle cx="936" cy="560" r="2.05"/><circle cx="944" cy="560" r="2.05"/><circle cx="952" cy="560" r="2.05"/><circle cx="88" cy="568" r="2.05"/><circle cx="96" cy="568" r="2.05"/><circle cx="168" cy="568" r="2.05"/><circle cx="176" cy="568" r="2.05"/><circle cx="184" cy="568" r="2.05"/><circle cx="192" cy="568" r="2.05"/><circle cx="208" cy="568" r="2.05"/><circle cx="216" cy="568" r="2.05"/><circle cx="720" cy="568" r="2.05"/><circle cx="728" cy="568" r="2.05"/><circle cx="736" cy="568" r="2.05"/><circle cx="744" cy="568" r="2.05"/><circle cx="752" cy="568" r="2.05"/><circle cx="760" cy="568" r="2.05"/><circle cx="768" cy="568" r="2.05"/><circle cx="776" cy="568" r="2.05"/><circle cx="784" cy="568" r="2.05"/><circle cx="792" cy="568" r="2.05"/><circle cx="800" cy="568" r="2.05"/><circle cx="808" cy="568" r="2.05"/><circle cx="816" cy="568" r="2.05"/><circle cx="824" cy="568" r="2.05"/><circle cx="832" cy="568" r="2.05"/><circle cx="840" cy="568" r="2.05"/><circle cx="848" cy="568" r="2.05"/><circle cx="856" cy="568" r="2.05"/><circle cx="864" cy="568" r="2.05"/><circle cx="872" cy="568" r="2.05"/><circle cx="880" cy="568" r="2.05"/><circle cx="888" cy="568" r="2.05"/><circle cx="896" cy="568" r="2.05"/><circle cx="904" cy="568" r="2.05"/><circle cx="912" cy="568" r="2.05"/><circle cx="920" cy="568" r="2.05"/><circle cx="928" cy="568" r="2.05"/><circle cx="936" cy="568" r="2.05"/><circle cx="944" cy="568" r="2.05"/><circle cx="952" cy="568" r="2.05"/><circle cx="96" cy="576" r="2.05"/><circle cx="160" cy="576" r="2.05"/><circle cx="168" cy="576" r="2.05"/><circle cx="176" cy="576" r="2.05"/><circle cx="184" cy="576" r="2.05"/><circle cx="200" cy="576" r="2.05"/><circle cx="208" cy="576" r="2.05"/><circle cx="216" cy="576" r="2.05"/><circle cx="224" cy="576" r="2.05"/><circle cx="232" cy="576" r="2.05"/><circle cx="240" cy="576" r="2.05"/><circle cx="264" cy="576" r="2.05"/><circle cx="272" cy="576" r="2.05"/><circle cx="288" cy="576" r="2.05"/><circle cx="728" cy="576" r="2.05"/><circle cx="736" cy="576" r="2.05"/><circle cx="744" cy="576" r="2.05"/><circle cx="752" cy="576" r="2.05"/><circle cx="760" cy="576" r="2.05"/><circle cx="768" cy="576" r="2.05"/><circle cx="776" cy="576" r="2.05"/><circle cx="784" cy="576" r="2.05"/><circle cx="792" cy="576" r="2.05"/><circle cx="800" cy="576" r="2.05"/><circle cx="808" cy="576" r="2.05"/><circle cx="816" cy="576" r="2.05"/><circle cx="824" cy="576" r="2.05"/><circle cx="832" cy="576" r="2.05"/><circle cx="840" cy="576" r="2.05"/><circle cx="848" cy="576" r="2.05"/><circle cx="856" cy="576" r="2.05"/><circle cx="864" cy="576" r="2.05"/><circle cx="872" cy="576" r="2.05"/><circle cx="880" cy="576" r="2.05"/><circle cx="888" cy="576" r="2.05"/><circle cx="896" cy="576" r="2.05"/><circle cx="904" cy="576" r="2.05"/><circle cx="912" cy="576" r="2.05"/><circle cx="920" cy="576" r="2.05"/><circle cx="928" cy="576" r="2.05"/><circle cx="936" cy="576" r="2.05"/><circle cx="944" cy="576" r="2.05"/><circle cx="952" cy="576" r="2.05"/><circle cx="96" cy="584" r="2.05"/><circle cx="104" cy="584" r="2.05"/><circle cx="112" cy="584" r="2.05"/><circle cx="120" cy="584" r="2.05"/><circle cx="136" cy="584" r="2.05"/><circle cx="152" cy="584" r="2.05"/><circle cx="160" cy="584" r="2.05"/><circle cx="168" cy="584" r="2.05"/><circle cx="176" cy="584" r="2.05"/><circle cx="184" cy="584" r="2.05"/><circle cx="200" cy="584" r="2.05"/><circle cx="208" cy="584" r="2.05"/><circle cx="216" cy="584" r="2.05"/><circle cx="224" cy="584" r="2.05"/><circle cx="232" cy="584" r="2.05"/><circle cx="240" cy="584" r="2.05"/><circle cx="248" cy="584" r="2.05"/><circle cx="256" cy="584" r="2.05"/><circle cx="264" cy="584" r="2.05"/><circle cx="272" cy="584" r="2.05"/><circle cx="280" cy="584" r="2.05"/><circle cx="288" cy="584" r="2.05"/><circle cx="736" cy="584" r="2.05"/><circle cx="744" cy="584" r="2.05"/><circle cx="752" cy="584" r="2.05"/><circle cx="760" cy="584" r="2.05"/><circle cx="768" cy="584" r="2.05"/><circle cx="776" cy="584" r="2.05"/><circle cx="784" cy="584" r="2.05"/><circle cx="792" cy="584" r="2.05"/><circle cx="800" cy="584" r="2.05"/><circle cx="808" cy="584" r="2.05"/><circle cx="816" cy="584" r="2.05"/><circle cx="824" cy="584" r="2.05"/><circle cx="832" cy="584" r="2.05"/><circle cx="840" cy="584" r="2.05"/><circle cx="848" cy="584" r="2.05"/><circle cx="856" cy="584" r="2.05"/><circle cx="864" cy="584" r="2.05"/><circle cx="872" cy="584" r="2.05"/><circle cx="880" cy="584" r="2.05"/><circle cx="888" cy="584" r="2.05"/><circle cx="896" cy="584" r="2.05"/><circle cx="904" cy="584" r="2.05"/><circle cx="912" cy="584" r="2.05"/><circle cx="920" cy="584" r="2.05"/><circle cx="928" cy="584" r="2.05"/><circle cx="936" cy="584" r="2.05"/><circle cx="944" cy="584" r="2.05"/><circle cx="952" cy="584" r="2.05"/><circle cx="120" cy="592" r="2.05"/><circle cx="136" cy="592" r="2.05"/><circle cx="144" cy="592" r="2.05"/><circle cx="152" cy="592" r="2.05"/><circle cx="160" cy="592" r="2.05"/><circle cx="168" cy="592" r="2.05"/><circle cx="176" cy="592" r="2.05"/><circle cx="184" cy="592" r="2.05"/><circle cx="192" cy="592" r="2.05"/><circle cx="200" cy="592" r="2.05"/><circle cx="208" cy="592" r="2.05"/><circle cx="216" cy="592" r="2.05"/><circle cx="224" cy="592" r="2.05"/><circle cx="232" cy="592" r="2.05"/><circle cx="240" cy="592" r="2.05"/><circle cx="248" cy="592" r="2.05"/><circle cx="256" cy="592" r="2.05"/><circle cx="264" cy="592" r="2.05"/><circle cx="272" cy="592" r="2.05"/><circle cx="280" cy="592" r="2.05"/><circle cx="288" cy="592" r="2.05"/><circle cx="296" cy="592" r="2.05"/><circle cx="736" cy="592" r="2.05"/><circle cx="744" cy="592" r="2.05"/><circle cx="752" cy="592" r="2.05"/><circle cx="760" cy="592" r="2.05"/><circle cx="768" cy="592" r="2.05"/><circle cx="776" cy="592" r="2.05"/><circle cx="784" cy="592" r="2.05"/><circle cx="792" cy="592" r="2.05"/><circle cx="800" cy="592" r="2.05"/><circle cx="808" cy="592" r="2.05"/><circle cx="816" cy="592" r="2.05"/><circle cx="824" cy="592" r="2.05"/><circle cx="832" cy="592" r="2.05"/><circle cx="840" cy="592" r="2.05"/><circle cx="848" cy="592" r="2.05"/><circle cx="856" cy="592" r="2.05"/><circle cx="864" cy="592" r="2.05"/><circle cx="872" cy="592" r="2.05"/><circle cx="880" cy="592" r="2.05"/><circle cx="888" cy="592" r="2.05"/><circle cx="896" cy="592" r="2.05"/><circle cx="904" cy="592" r="2.05"/><circle cx="912" cy="592" r="2.05"/><circle cx="920" cy="592" r="2.05"/><circle cx="928" cy="592" r="2.05"/><circle cx="936" cy="592" r="2.05"/><circle cx="944" cy="592" r="2.05"/><circle cx="952" cy="592" r="2.05"/><circle cx="144" cy="600" r="2.05"/><circle cx="152" cy="600" r="2.05"/><circle cx="160" cy="600" r="2.05"/><circle cx="168" cy="600" r="2.05"/><circle cx="176" cy="600" r="2.05"/><circle cx="184" cy="600" r="2.05"/><circle cx="192" cy="600" r="2.05"/><circle cx="200" cy="600" r="2.05"/><circle cx="208" cy="600" r="2.05"/><circle cx="216" cy="600" r="2.05"/><circle cx="224" cy="600" r="2.05"/><circle cx="232" cy="600" r="2.05"/><circle cx="240" cy="600" r="2.05"/><circle cx="248" cy="600" r="2.05"/><circle cx="256" cy="600" r="2.05"/><circle cx="264" cy="600" r="2.05"/><circle cx="272" cy="600" r="2.05"/><circle cx="280" cy="600" r="2.05"/><circle cx="288" cy="600" r="2.05"/><circle cx="296" cy="600" r="2.05"/><circle cx="304" cy="600" r="2.05"/><circle cx="752" cy="600" r="2.05"/><circle cx="760" cy="600" r="2.05"/><circle cx="768" cy="600" r="2.05"/><circle cx="776" cy="600" r="2.05"/><circle cx="784" cy="600" r="2.05"/><circle cx="792" cy="600" r="2.05"/><circle cx="800" cy="600" r="2.05"/><circle cx="808" cy="600" r="2.05"/><circle cx="816" cy="600" r="2.05"/><circle cx="824" cy="600" r="2.05"/><circle cx="832" cy="600" r="2.05"/><circle cx="840" cy="600" r="2.05"/><circle cx="872" cy="600" r="2.05"/><circle cx="880" cy="600" r="2.05"/><circle cx="888" cy="600" r="2.05"/><circle cx="896" cy="600" r="2.05"/><circle cx="904" cy="600" r="2.05"/><circle cx="912" cy="600" r="2.05"/><circle cx="920" cy="600" r="2.05"/><circle cx="928" cy="600" r="2.05"/><circle cx="936" cy="600" r="2.05"/><circle cx="944" cy="600" r="2.05"/><circle cx="144" cy="608" r="2.05"/><circle cx="152" cy="608" r="2.05"/><circle cx="160" cy="608" r="2.05"/><circle cx="168" cy="608" r="2.05"/><circle cx="176" cy="608" r="2.05"/><circle cx="184" cy="608" r="2.05"/><circle cx="192" cy="608" r="2.05"/><circle cx="200" cy="608" r="2.05"/><circle cx="208" cy="608" r="2.05"/><circle cx="216" cy="608" r="2.05"/><circle cx="224" cy="608" r="2.05"/><circle cx="232" cy="608" r="2.05"/><circle cx="240" cy="608" r="2.05"/><circle cx="248" cy="608" r="2.05"/><circle cx="256" cy="608" r="2.05"/><circle cx="264" cy="608" r="2.05"/><circle cx="272" cy="608" r="2.05"/><circle cx="280" cy="608" r="2.05"/><circle cx="288" cy="608" r="2.05"/><circle cx="296" cy="608" r="2.05"/><circle cx="304" cy="608" r="2.05"/><circle cx="312" cy="608" r="2.05"/><circle cx="760" cy="608" r="2.05"/><circle cx="768" cy="608" r="2.05"/><circle cx="776" cy="608" r="2.05"/><circle cx="784" cy="608" r="2.05"/><circle cx="792" cy="608" r="2.05"/><circle cx="800" cy="608" r="2.05"/><circle cx="808" cy="608" r="2.05"/><circle cx="816" cy="608" r="2.05"/><circle cx="824" cy="608" r="2.05"/><circle cx="872" cy="608" r="2.05"/><circle cx="880" cy="608" r="2.05"/><circle cx="896" cy="608" r="2.05"/><circle cx="904" cy="608" r="2.05"/><circle cx="912" cy="608" r="2.05"/><circle cx="920" cy="608" r="2.05"/><circle cx="928" cy="608" r="2.05"/><circle cx="936" cy="608" r="2.05"/><circle cx="944" cy="608" r="2.05"/><circle cx="144" cy="616" r="2.05"/><circle cx="152" cy="616" r="2.05"/><circle cx="160" cy="616" r="2.05"/><circle cx="168" cy="616" r="2.05"/><circle cx="176" cy="616" r="2.05"/><circle cx="184" cy="616" r="2.05"/><circle cx="192" cy="616" r="2.05"/><circle cx="200" cy="616" r="2.05"/><circle cx="208" cy="616" r="2.05"/><circle cx="216" cy="616" r="2.05"/><circle cx="224" cy="616" r="2.05"/><circle cx="232" cy="616" r="2.05"/><circle cx="240" cy="616" r="2.05"/><circle cx="248" cy="616" r="2.05"/><circle cx="256" cy="616" r="2.05"/><circle cx="264" cy="616" r="2.05"/><circle cx="272" cy="616" r="2.05"/><circle cx="280" cy="616" r="2.05"/><circle cx="288" cy="616" r="2.05"/><circle cx="296" cy="616" r="2.05"/><circle cx="304" cy="616" r="2.05"/><circle cx="312" cy="616" r="2.05"/><circle cx="320" cy="616" r="2.05"/><circle cx="328" cy="616" r="2.05"/><circle cx="336" cy="616" r="2.05"/><circle cx="344" cy="616" r="2.05"/><circle cx="352" cy="616" r="2.05"/><circle cx="360" cy="616" r="2.05"/><circle cx="776" cy="616" r="2.05"/><circle cx="896" cy="616" r="2.05"/><circle cx="904" cy="616" r="2.05"/><circle cx="912" cy="616" r="2.05"/><circle cx="920" cy="616" r="2.05"/><circle cx="928" cy="616" r="2.05"/><circle cx="936" cy="616" r="2.05"/><circle cx="944" cy="616" r="2.05"/><circle cx="144" cy="624" r="2.05"/><circle cx="152" cy="624" r="2.05"/><circle cx="160" cy="624" r="2.05"/><circle cx="168" cy="624" r="2.05"/><circle cx="176" cy="624" r="2.05"/><circle cx="184" cy="624" r="2.05"/><circle cx="192" cy="624" r="2.05"/><circle cx="200" cy="624" r="2.05"/><circle cx="208" cy="624" r="2.05"/><circle cx="216" cy="624" r="2.05"/><circle cx="224" cy="624" r="2.05"/><circle cx="232" cy="624" r="2.05"/><circle cx="240" cy="624" r="2.05"/><circle cx="248" cy="624" r="2.05"/><circle cx="256" cy="624" r="2.05"/><circle cx="264" cy="624" r="2.05"/><circle cx="272" cy="624" r="2.05"/><circle cx="280" cy="624" r="2.05"/><circle cx="288" cy="624" r="2.05"/><circle cx="296" cy="624" r="2.05"/><circle cx="304" cy="624" r="2.05"/><circle cx="312" cy="624" r="2.05"/><circle cx="320" cy="624" r="2.05"/><circle cx="328" cy="624" r="2.05"/><circle cx="336" cy="624" r="2.05"/><circle cx="344" cy="624" r="2.05"/><circle cx="352" cy="624" r="2.05"/><circle cx="360" cy="624" r="2.05"/><circle cx="368" cy="624" r="2.05"/><circle cx="904" cy="624" r="2.05"/><circle cx="912" cy="624" r="2.05"/><circle cx="920" cy="624" r="2.05"/><circle cx="928" cy="624" r="2.05"/><circle cx="936" cy="624" r="2.05"/><circle cx="944" cy="624" r="2.05"/><circle cx="136" cy="632" r="2.05"/><circle cx="144" cy="632" r="2.05"/><circle cx="152" cy="632" r="2.05"/><circle cx="160" cy="632" r="2.05"/><circle cx="168" cy="632" r="2.05"/><circle cx="176" cy="632" r="2.05"/><circle cx="184" cy="632" r="2.05"/><circle cx="192" cy="632" r="2.05"/><circle cx="200" cy="632" r="2.05"/><circle cx="208" cy="632" r="2.05"/><circle cx="216" cy="632" r="2.05"/><circle cx="224" cy="632" r="2.05"/><circle cx="232" cy="632" r="2.05"/><circle cx="240" cy="632" r="2.05"/><circle cx="248" cy="632" r="2.05"/><circle cx="256" cy="632" r="2.05"/><circle cx="264" cy="632" r="2.05"/><circle cx="272" cy="632" r="2.05"/><circle cx="280" cy="632" r="2.05"/><circle cx="288" cy="632" r="2.05"/><circle cx="296" cy="632" r="2.05"/><circle cx="304" cy="632" r="2.05"/><circle cx="312" cy="632" r="2.05"/><circle cx="320" cy="632" r="2.05"/><circle cx="328" cy="632" r="2.05"/><circle cx="336" cy="632" r="2.05"/><circle cx="344" cy="632" r="2.05"/><circle cx="352" cy="632" r="2.05"/><circle cx="360" cy="632" r="2.05"/><circle cx="368" cy="632" r="2.05"/><circle cx="376" cy="632" r="2.05"/><circle cx="896" cy="632" r="2.05"/><circle cx="904" cy="632" r="2.05"/><circle cx="912" cy="632" r="2.05"/><circle cx="920" cy="632" r="2.05"/><circle cx="928" cy="632" r="2.05"/><circle cx="936" cy="632" r="2.05"/><circle cx="944" cy="632" r="2.05"/><circle cx="128" cy="640" r="2.05"/><circle cx="136" cy="640" r="2.05"/><circle cx="144" cy="640" r="2.05"/><circle cx="152" cy="640" r="2.05"/><circle cx="160" cy="640" r="2.05"/><circle cx="168" cy="640" r="2.05"/><circle cx="176" cy="640" r="2.05"/><circle cx="184" cy="640" r="2.05"/><circle cx="192" cy="640" r="2.05"/><circle cx="200" cy="640" r="2.05"/><circle cx="208" cy="640" r="2.05"/><circle cx="216" cy="640" r="2.05"/><circle cx="224" cy="640" r="2.05"/><circle cx="232" cy="640" r="2.05"/><circle cx="240" cy="640" r="2.05"/><circle cx="248" cy="640" r="2.05"/><circle cx="256" cy="640" r="2.05"/><circle cx="264" cy="640" r="2.05"/><circle cx="272" cy="640" r="2.05"/><circle cx="280" cy="640" r="2.05"/><circle cx="288" cy="640" r="2.05"/><circle cx="296" cy="640" r="2.05"/><circle cx="304" cy="640" r="2.05"/><circle cx="312" cy="640" r="2.05"/><circle cx="320" cy="640" r="2.05"/><circle cx="328" cy="640" r="2.05"/><circle cx="336" cy="640" r="2.05"/><circle cx="344" cy="640" r="2.05"/><circle cx="352" cy="640" r="2.05"/><circle cx="360" cy="640" r="2.05"/><circle cx="368" cy="640" r="2.05"/><circle cx="376" cy="640" r="2.05"/><circle cx="384" cy="640" r="2.05"/><circle cx="896" cy="640" r="2.05"/><circle cx="904" cy="640" r="2.05"/><circle cx="912" cy="640" r="2.05"/><circle cx="920" cy="640" r="2.05"/><circle cx="928" cy="640" r="2.05"/><circle cx="936" cy="640" r="2.05"/><circle cx="120" cy="648" r="2.05"/><circle cx="128" cy="648" r="2.05"/><circle cx="136" cy="648" r="2.05"/><circle cx="144" cy="648" r="2.05"/><circle cx="152" cy="648" r="2.05"/><circle cx="160" cy="648" r="2.05"/><circle cx="168" cy="648" r="2.05"/><circle cx="176" cy="648" r="2.05"/><circle cx="184" cy="648" r="2.05"/><circle cx="192" cy="648" r="2.05"/><circle cx="200" cy="648" r="2.05"/><circle cx="208" cy="648" r="2.05"/><circle cx="216" cy="648" r="2.05"/><circle cx="224" cy="648" r="2.05"/><circle cx="232" cy="648" r="2.05"/><circle cx="240" cy="648" r="2.05"/><circle cx="248" cy="648" r="2.05"/><circle cx="256" cy="648" r="2.05"/><circle cx="264" cy="648" r="2.05"/><circle cx="272" cy="648" r="2.05"/><circle cx="280" cy="648" r="2.05"/><circle cx="288" cy="648" r="2.05"/><circle cx="296" cy="648" r="2.05"/><circle cx="304" cy="648" r="2.05"/><circle cx="312" cy="648" r="2.05"/><circle cx="320" cy="648" r="2.05"/><circle cx="328" cy="648" r="2.05"/><circle cx="336" cy="648" r="2.05"/><circle cx="344" cy="648" r="2.05"/><circle cx="352" cy="648" r="2.05"/><circle cx="360" cy="648" r="2.05"/><circle cx="368" cy="648" r="2.05"/><circle cx="376" cy="648" r="2.05"/><circle cx="384" cy="648" r="2.05"/><circle cx="896" cy="648" r="2.05"/><circle cx="904" cy="648" r="2.05"/><circle cx="912" cy="648" r="2.05"/><circle cx="920" cy="648" r="2.05"/><circle cx="928" cy="648" r="2.05"/><circle cx="936" cy="648" r="2.05"/><circle cx="120" cy="656" r="2.05"/><circle cx="128" cy="656" r="2.05"/><circle cx="136" cy="656" r="2.05"/><circle cx="144" cy="656" r="2.05"/><circle cx="152" cy="656" r="2.05"/><circle cx="160" cy="656" r="2.05"/><circle cx="168" cy="656" r="2.05"/><circle cx="176" cy="656" r="2.05"/><circle cx="184" cy="656" r="2.05"/><circle cx="192" cy="656" r="2.05"/><circle cx="200" cy="656" r="2.05"/><circle cx="208" cy="656" r="2.05"/><circle cx="216" cy="656" r="2.05"/><circle cx="224" cy="656" r="2.05"/><circle cx="232" cy="656" r="2.05"/><circle cx="240" cy="656" r="2.05"/><circle cx="248" cy="656" r="2.05"/><circle cx="256" cy="656" r="2.05"/><circle cx="264" cy="656" r="2.05"/><circle cx="272" cy="656" r="2.05"/><circle cx="280" cy="656" r="2.05"/><circle cx="288" cy="656" r="2.05"/><circle cx="296" cy="656" r="2.05"/><circle cx="304" cy="656" r="2.05"/><circle cx="312" cy="656" r="2.05"/><circle cx="320" cy="656" r="2.05"/><circle cx="328" cy="656" r="2.05"/><circle cx="336" cy="656" r="2.05"/><circle cx="344" cy="656" r="2.05"/><circle cx="352" cy="656" r="2.05"/><circle cx="360" cy="656" r="2.05"/><circle cx="368" cy="656" r="2.05"/><circle cx="376" cy="656" r="2.05"/><circle cx="384" cy="656" r="2.05"/><circle cx="896" cy="656" r="2.05"/><circle cx="904" cy="656" r="2.05"/><circle cx="912" cy="656" r="2.05"/><circle cx="920" cy="656" r="2.05"/><circle cx="928" cy="656" r="2.05"/><circle cx="936" cy="656" r="2.05"/><circle cx="120" cy="664" r="2.05"/><circle cx="128" cy="664" r="2.05"/><circle cx="136" cy="664" r="2.05"/><circle cx="144" cy="664" r="2.05"/><circle cx="152" cy="664" r="2.05"/><circle cx="160" cy="664" r="2.05"/><circle cx="168" cy="664" r="2.05"/><circle cx="176" cy="664" r="2.05"/><circle cx="184" cy="664" r="2.05"/><circle cx="192" cy="664" r="2.05"/><circle cx="200" cy="664" r="2.05"/><circle cx="208" cy="664" r="2.05"/><circle cx="216" cy="664" r="2.05"/><circle cx="224" cy="664" r="2.05"/><circle cx="232" cy="664" r="2.05"/><circle cx="240" cy="664" r="2.05"/><circle cx="248" cy="664" r="2.05"/><circle cx="256" cy="664" r="2.05"/><circle cx="264" cy="664" r="2.05"/><circle cx="272" cy="664" r="2.05"/><circle cx="280" cy="664" r="2.05"/><circle cx="288" cy="664" r="2.05"/><circle cx="296" cy="664" r="2.05"/><circle cx="304" cy="664" r="2.05"/><circle cx="312" cy="664" r="2.05"/><circle cx="320" cy="664" r="2.05"/><circle cx="328" cy="664" r="2.05"/><circle cx="336" cy="664" r="2.05"/><circle cx="344" cy="664" r="2.05"/><circle cx="352" cy="664" r="2.05"/><circle cx="360" cy="664" r="2.05"/><circle cx="368" cy="664" r="2.05"/><circle cx="376" cy="664" r="2.05"/><circle cx="384" cy="664" r="2.05"/><circle cx="392" cy="664" r="2.05"/><circle cx="400" cy="664" r="2.05"/><circle cx="904" cy="664" r="2.05"/><circle cx="912" cy="664" r="2.05"/><circle cx="920" cy="664" r="2.05"/><circle cx="928" cy="664" r="2.05"/><circle cx="128" cy="672" r="2.05"/><circle cx="136" cy="672" r="2.05"/><circle cx="144" cy="672" r="2.05"/><circle cx="152" cy="672" r="2.05"/><circle cx="160" cy="672" r="2.05"/><circle cx="168" cy="672" r="2.05"/><circle cx="176" cy="672" r="2.05"/><circle cx="184" cy="672" r="2.05"/><circle cx="192" cy="672" r="2.05"/><circle cx="200" cy="672" r="2.05"/><circle cx="208" cy="672" r="2.05"/><circle cx="216" cy="672" r="2.05"/><circle cx="224" cy="672" r="2.05"/><circle cx="232" cy="672" r="2.05"/><circle cx="240" cy="672" r="2.05"/><circle cx="248" cy="672" r="2.05"/><circle cx="256" cy="672" r="2.05"/><circle cx="264" cy="672" r="2.05"/><circle cx="272" cy="672" r="2.05"/><circle cx="280" cy="672" r="2.05"/><circle cx="288" cy="672" r="2.05"/><circle cx="296" cy="672" r="2.05"/><circle cx="304" cy="672" r="2.05"/><circle cx="312" cy="672" r="2.05"/><circle cx="320" cy="672" r="2.05"/><circle cx="328" cy="672" r="2.05"/><circle cx="336" cy="672" r="2.05"/><circle cx="344" cy="672" r="2.05"/><circle cx="352" cy="672" r="2.05"/><circle cx="360" cy="672" r="2.05"/><circle cx="368" cy="672" r="2.05"/><circle cx="376" cy="672" r="2.05"/><circle cx="384" cy="672" r="2.05"/><circle cx="392" cy="672" r="2.05"/><circle cx="400" cy="672" r="2.05"/><circle cx="408" cy="672" r="2.05"/><circle cx="416" cy="672" r="2.05"/><circle cx="424" cy="672" r="2.05"/><circle cx="432" cy="672" r="2.05"/><circle cx="440" cy="672" r="2.05"/><circle cx="904" cy="672" r="2.05"/><circle cx="912" cy="672" r="2.05"/><circle cx="920" cy="672" r="2.05"/><circle cx="928" cy="672" r="2.05"/><circle cx="120" cy="680" r="2.05"/><circle cx="128" cy="680" r="2.05"/><circle cx="136" cy="680" r="2.05"/><circle cx="144" cy="680" r="2.05"/><circle cx="152" cy="680" r="2.05"/><circle cx="160" cy="680" r="2.05"/><circle cx="168" cy="680" r="2.05"/><circle cx="176" cy="680" r="2.05"/><circle cx="184" cy="680" r="2.05"/><circle cx="192" cy="680" r="2.05"/><circle cx="200" cy="680" r="2.05"/><circle cx="208" cy="680" r="2.05"/><circle cx="216" cy="680" r="2.05"/><circle cx="224" cy="680" r="2.05"/><circle cx="232" cy="680" r="2.05"/><circle cx="240" cy="680" r="2.05"/><circle cx="248" cy="680" r="2.05"/><circle cx="256" cy="680" r="2.05"/><circle cx="264" cy="680" r="2.05"/><circle cx="272" cy="680" r="2.05"/><circle cx="280" cy="680" r="2.05"/><circle cx="288" cy="680" r="2.05"/><circle cx="296" cy="680" r="2.05"/><circle cx="304" cy="680" r="2.05"/><circle cx="312" cy="680" r="2.05"/><circle cx="320" cy="680" r="2.05"/><circle cx="328" cy="680" r="2.05"/><circle cx="336" cy="680" r="2.05"/><circle cx="344" cy="680" r="2.05"/><circle cx="352" cy="680" r="2.05"/><circle cx="360" cy="680" r="2.05"/><circle cx="368" cy="680" r="2.05"/><circle cx="376" cy="680" r="2.05"/><circle cx="384" cy="680" r="2.05"/><circle cx="392" cy="680" r="2.05"/><circle cx="400" cy="680" r="2.05"/><circle cx="408" cy="680" r="2.05"/><circle cx="416" cy="680" r="2.05"/><circle cx="424" cy="680" r="2.05"/><circle cx="432" cy="680" r="2.05"/><circle cx="440" cy="680" r="2.05"/><circle cx="448" cy="680" r="2.05"/><circle cx="456" cy="680" r="2.05"/><circle cx="464" cy="680" r="2.05"/><circle cx="912" cy="680" r="2.05"/><circle cx="920" cy="680" r="2.05"/><circle cx="928" cy="680" r="2.05"/><circle cx="112" cy="688" r="2.05"/><circle cx="120" cy="688" r="2.05"/><circle cx="128" cy="688" r="2.05"/><circle cx="136" cy="688" r="2.05"/><circle cx="144" cy="688" r="2.05"/><circle cx="152" cy="688" r="2.05"/><circle cx="160" cy="688" r="2.05"/><circle cx="168" cy="688" r="2.05"/><circle cx="176" cy="688" r="2.05"/><circle cx="184" cy="688" r="2.05"/><circle cx="192" cy="688" r="2.05"/><circle cx="200" cy="688" r="2.05"/><circle cx="208" cy="688" r="2.05"/><circle cx="216" cy="688" r="2.05"/><circle cx="224" cy="688" r="2.05"/><circle cx="232" cy="688" r="2.05"/><circle cx="240" cy="688" r="2.05"/><circle cx="248" cy="688" r="2.05"/><circle cx="256" cy="688" r="2.05"/><circle cx="264" cy="688" r="2.05"/><circle cx="272" cy="688" r="2.05"/><circle cx="280" cy="688" r="2.05"/><circle cx="288" cy="688" r="2.05"/><circle cx="296" cy="688" r="2.05"/><circle cx="304" cy="688" r="2.05"/><circle cx="312" cy="688" r="2.05"/><circle cx="320" cy="688" r="2.05"/><circle cx="328" cy="688" r="2.05"/><circle cx="336" cy="688" r="2.05"/><circle cx="344" cy="688" r="2.05"/><circle cx="352" cy="688" r="2.05"/><circle cx="360" cy="688" r="2.05"/><circle cx="368" cy="688" r="2.05"/><circle cx="376" cy="688" r="2.05"/><circle cx="384" cy="688" r="2.05"/><circle cx="392" cy="688" r="2.05"/><circle cx="400" cy="688" r="2.05"/><circle cx="408" cy="688" r="2.05"/><circle cx="416" cy="688" r="2.05"/><circle cx="424" cy="688" r="2.05"/><circle cx="432" cy="688" r="2.05"/><circle cx="440" cy="688" r="2.05"/><circle cx="448" cy="688" r="2.05"/><circle cx="456" cy="688" r="2.05"/><circle cx="464" cy="688" r="2.05"/><circle cx="472" cy="688" r="2.05"/><circle cx="480" cy="688" r="2.05"/><circle cx="488" cy="688" r="2.05"/><circle cx="496" cy="688" r="2.05"/><circle cx="912" cy="688" r="2.05"/><circle cx="920" cy="688" r="2.05"/><circle cx="120" cy="696" r="2.05"/><circle cx="128" cy="696" r="2.05"/><circle cx="136" cy="696" r="2.05"/><circle cx="144" cy="696" r="2.05"/><circle cx="152" cy="696" r="2.05"/><circle cx="160" cy="696" r="2.05"/><circle cx="168" cy="696" r="2.05"/><circle cx="176" cy="696" r="2.05"/><circle cx="184" cy="696" r="2.05"/><circle cx="192" cy="696" r="2.05"/><circle cx="200" cy="696" r="2.05"/><circle cx="208" cy="696" r="2.05"/><circle cx="216" cy="696" r="2.05"/><circle cx="224" cy="696" r="2.05"/><circle cx="232" cy="696" r="2.05"/><circle cx="240" cy="696" r="2.05"/><circle cx="248" cy="696" r="2.05"/><circle cx="256" cy="696" r="2.05"/><circle cx="264" cy="696" r="2.05"/><circle cx="272" cy="696" r="2.05"/><circle cx="280" cy="696" r="2.05"/><circle cx="288" cy="696" r="2.05"/><circle cx="296" cy="696" r="2.05"/><circle cx="304" cy="696" r="2.05"/><circle cx="312" cy="696" r="2.05"/><circle cx="320" cy="696" r="2.05"/><circle cx="328" cy="696" r="2.05"/><circle cx="336" cy="696" r="2.05"/><circle cx="344" cy="696" r="2.05"/><circle cx="352" cy="696" r="2.05"/><circle cx="360" cy="696" r="2.05"/><circle cx="368" cy="696" r="2.05"/><circle cx="376" cy="696" r="2.05"/><circle cx="384" cy="696" r="2.05"/><circle cx="392" cy="696" r="2.05"/><circle cx="400" cy="696" r="2.05"/><circle cx="408" cy="696" r="2.05"/><circle cx="416" cy="696" r="2.05"/><circle cx="424" cy="696" r="2.05"/><circle cx="432" cy="696" r="2.05"/><circle cx="440" cy="696" r="2.05"/><circle cx="448" cy="696" r="2.05"/><circle cx="456" cy="696" r="2.05"/><circle cx="464" cy="696" r="2.05"/><circle cx="472" cy="696" r="2.05"/><circle cx="480" cy="696" r="2.05"/><circle cx="488" cy="696" r="2.05"/><circle cx="496" cy="696" r="2.05"/><circle cx="504" cy="696" r="2.05"/><circle cx="512" cy="696" r="2.05"/><circle cx="912" cy="696" r="2.05"/><circle cx="920" cy="696" r="2.05"/><circle cx="120" cy="704" r="2.05"/><circle cx="128" cy="704" r="2.05"/><circle cx="136" cy="704" r="2.05"/><circle cx="144" cy="704" r="2.05"/><circle cx="152" cy="704" r="2.05"/><circle cx="160" cy="704" r="2.05"/><circle cx="168" cy="704" r="2.05"/><circle cx="176" cy="704" r="2.05"/><circle cx="184" cy="704" r="2.05"/><circle cx="192" cy="704" r="2.05"/><circle cx="200" cy="704" r="2.05"/><circle cx="208" cy="704" r="2.05"/><circle cx="216" cy="704" r="2.05"/><circle cx="224" cy="704" r="2.05"/><circle cx="232" cy="704" r="2.05"/><circle cx="240" cy="704" r="2.05"/><circle cx="248" cy="704" r="2.05"/><circle cx="256" cy="704" r="2.05"/><circle cx="264" cy="704" r="2.05"/><circle cx="272" cy="704" r="2.05"/><circle cx="280" cy="704" r="2.05"/><circle cx="288" cy="704" r="2.05"/><circle cx="296" cy="704" r="2.05"/><circle cx="304" cy="704" r="2.05"/><circle cx="312" cy="704" r="2.05"/><circle cx="320" cy="704" r="2.05"/><circle cx="328" cy="704" r="2.05"/><circle cx="336" cy="704" r="2.05"/><circle cx="344" cy="704" r="2.05"/><circle cx="352" cy="704" r="2.05"/><circle cx="360" cy="704" r="2.05"/><circle cx="368" cy="704" r="2.05"/><circle cx="376" cy="704" r="2.05"/><circle cx="384" cy="704" r="2.05"/><circle cx="392" cy="704" r="2.05"/><circle cx="400" cy="704" r="2.05"/><circle cx="408" cy="704" r="2.05"/><circle cx="416" cy="704" r="2.05"/><circle cx="424" cy="704" r="2.05"/><circle cx="432" cy="704" r="2.05"/><circle cx="440" cy="704" r="2.05"/><circle cx="448" cy="704" r="2.05"/><circle cx="456" cy="704" r="2.05"/><circle cx="464" cy="704" r="2.05"/><circle cx="472" cy="704" r="2.05"/><circle cx="480" cy="704" r="2.05"/><circle cx="488" cy="704" r="2.05"/><circle cx="496" cy="704" r="2.05"/><circle cx="504" cy="704" r="2.05"/><circle cx="512" cy="704" r="2.05"/><circle cx="520" cy="704" r="2.05"/><circle cx="528" cy="704" r="2.05"/><circle cx="912" cy="704" r="2.05"/><circle cx="920" cy="704" r="2.05"/><circle cx="128" cy="712" r="2.05"/><circle cx="136" cy="712" r="2.05"/><circle cx="144" cy="712" r="2.05"/><circle cx="152" cy="712" r="2.05"/><circle cx="160" cy="712" r="2.05"/><circle cx="168" cy="712" r="2.05"/><circle cx="176" cy="712" r="2.05"/><circle cx="184" cy="712" r="2.05"/><circle cx="192" cy="712" r="2.05"/><circle cx="200" cy="712" r="2.05"/><circle cx="208" cy="712" r="2.05"/><circle cx="216" cy="712" r="2.05"/><circle cx="224" cy="712" r="2.05"/><circle cx="232" cy="712" r="2.05"/><circle cx="240" cy="712" r="2.05"/><circle cx="248" cy="712" r="2.05"/><circle cx="256" cy="712" r="2.05"/><circle cx="264" cy="712" r="2.05"/><circle cx="272" cy="712" r="2.05"/><circle cx="280" cy="712" r="2.05"/><circle cx="288" cy="712" r="2.05"/><circle cx="296" cy="712" r="2.05"/><circle cx="304" cy="712" r="2.05"/><circle cx="312" cy="712" r="2.05"/><circle cx="320" cy="712" r="2.05"/><circle cx="328" cy="712" r="2.05"/><circle cx="336" cy="712" r="2.05"/><circle cx="344" cy="712" r="2.05"/><circle cx="352" cy="712" r="2.05"/><circle cx="360" cy="712" r="2.05"/><circle cx="368" cy="712" r="2.05"/><circle cx="376" cy="712" r="2.05"/><circle cx="384" cy="712" r="2.05"/><circle cx="392" cy="712" r="2.05"/><circle cx="400" cy="712" r="2.05"/><circle cx="408" cy="712" r="2.05"/><circle cx="416" cy="712" r="2.05"/><circle cx="424" cy="712" r="2.05"/><circle cx="432" cy="712" r="2.05"/><circle cx="440" cy="712" r="2.05"/><circle cx="448" cy="712" r="2.05"/><circle cx="456" cy="712" r="2.05"/><circle cx="464" cy="712" r="2.05"/><circle cx="472" cy="712" r="2.05"/><circle cx="480" cy="712" r="2.05"/><circle cx="488" cy="712" r="2.05"/><circle cx="496" cy="712" r="2.05"/><circle cx="504" cy="712" r="2.05"/><circle cx="512" cy="712" r="2.05"/><circle cx="520" cy="712" r="2.05"/><circle cx="528" cy="712" r="2.05"/><circle cx="536" cy="712" r="2.05"/><circle cx="912" cy="712" r="2.05"/><circle cx="136" cy="720" r="2.05"/><circle cx="144" cy="720" r="2.05"/><circle cx="152" cy="720" r="2.05"/><circle cx="160" cy="720" r="2.05"/><circle cx="168" cy="720" r="2.05"/><circle cx="176" cy="720" r="2.05"/><circle cx="184" cy="720" r="2.05"/><circle cx="192" cy="720" r="2.05"/><circle cx="200" cy="720" r="2.05"/><circle cx="208" cy="720" r="2.05"/><circle cx="216" cy="720" r="2.05"/><circle cx="224" cy="720" r="2.05"/><circle cx="232" cy="720" r="2.05"/><circle cx="240" cy="720" r="2.05"/><circle cx="248" cy="720" r="2.05"/><circle cx="256" cy="720" r="2.05"/><circle cx="264" cy="720" r="2.05"/><circle cx="272" cy="720" r="2.05"/><circle cx="280" cy="720" r="2.05"/><circle cx="288" cy="720" r="2.05"/><circle cx="296" cy="720" r="2.05"/><circle cx="304" cy="720" r="2.05"/><circle cx="312" cy="720" r="2.05"/><circle cx="320" cy="720" r="2.05"/><circle cx="328" cy="720" r="2.05"/><circle cx="336" cy="720" r="2.05"/><circle cx="344" cy="720" r="2.05"/><circle cx="352" cy="720" r="2.05"/><circle cx="360" cy="720" r="2.05"/><circle cx="368" cy="720" r="2.05"/><circle cx="376" cy="720" r="2.05"/><circle cx="384" cy="720" r="2.05"/><circle cx="392" cy="720" r="2.05"/><circle cx="400" cy="720" r="2.05"/><circle cx="408" cy="720" r="2.05"/><circle cx="416" cy="720" r="2.05"/><circle cx="424" cy="720" r="2.05"/><circle cx="432" cy="720" r="2.05"/><circle cx="440" cy="720" r="2.05"/><circle cx="448" cy="720" r="2.05"/><circle cx="456" cy="720" r="2.05"/><circle cx="464" cy="720" r="2.05"/><circle cx="472" cy="720" r="2.05"/><circle cx="480" cy="720" r="2.05"/><circle cx="488" cy="720" r="2.05"/><circle cx="496" cy="720" r="2.05"/><circle cx="504" cy="720" r="2.05"/><circle cx="512" cy="720" r="2.05"/><circle cx="520" cy="720" r="2.05"/><circle cx="528" cy="720" r="2.05"/><circle cx="536" cy="720" r="2.05"/><circle cx="912" cy="720" r="2.05"/><circle cx="144" cy="728" r="2.05"/><circle cx="152" cy="728" r="2.05"/><circle cx="160" cy="728" r="2.05"/><circle cx="168" cy="728" r="2.05"/><circle cx="176" cy="728" r="2.05"/><circle cx="184" cy="728" r="2.05"/><circle cx="192" cy="728" r="2.05"/><circle cx="200" cy="728" r="2.05"/><circle cx="208" cy="728" r="2.05"/><circle cx="216" cy="728" r="2.05"/><circle cx="224" cy="728" r="2.05"/><circle cx="232" cy="728" r="2.05"/><circle cx="240" cy="728" r="2.05"/><circle cx="248" cy="728" r="2.05"/><circle cx="256" cy="728" r="2.05"/><circle cx="264" cy="728" r="2.05"/><circle cx="272" cy="728" r="2.05"/><circle cx="280" cy="728" r="2.05"/><circle cx="288" cy="728" r="2.05"/><circle cx="296" cy="728" r="2.05"/><circle cx="304" cy="728" r="2.05"/><circle cx="312" cy="728" r="2.05"/><circle cx="320" cy="728" r="2.05"/><circle cx="328" cy="728" r="2.05"/><circle cx="336" cy="728" r="2.05"/><circle cx="344" cy="728" r="2.05"/><circle cx="352" cy="728" r="2.05"/><circle cx="360" cy="728" r="2.05"/><circle cx="368" cy="728" r="2.05"/><circle cx="376" cy="728" r="2.05"/><circle cx="384" cy="728" r="2.05"/><circle cx="392" cy="728" r="2.05"/><circle cx="400" cy="728" r="2.05"/><circle cx="408" cy="728" r="2.05"/><circle cx="416" cy="728" r="2.05"/><circle cx="424" cy="728" r="2.05"/><circle cx="432" cy="728" r="2.05"/><circle cx="440" cy="728" r="2.05"/><circle cx="448" cy="728" r="2.05"/><circle cx="456" cy="728" r="2.05"/><circle cx="464" cy="728" r="2.05"/><circle cx="472" cy="728" r="2.05"/><circle cx="480" cy="728" r="2.05"/><circle cx="488" cy="728" r="2.05"/><circle cx="496" cy="728" r="2.05"/><circle cx="504" cy="728" r="2.05"/><circle cx="512" cy="728" r="2.05"/><circle cx="520" cy="728" r="2.05"/><circle cx="528" cy="728" r="2.05"/><circle cx="144" cy="736" r="2.05"/><circle cx="152" cy="736" r="2.05"/><circle cx="160" cy="736" r="2.05"/><circle cx="168" cy="736" r="2.05"/><circle cx="176" cy="736" r="2.05"/><circle cx="184" cy="736" r="2.05"/><circle cx="192" cy="736" r="2.05"/><circle cx="200" cy="736" r="2.05"/><circle cx="208" cy="736" r="2.05"/><circle cx="216" cy="736" r="2.05"/><circle cx="224" cy="736" r="2.05"/><circle cx="232" cy="736" r="2.05"/><circle cx="240" cy="736" r="2.05"/><circle cx="248" cy="736" r="2.05"/><circle cx="256" cy="736" r="2.05"/><circle cx="264" cy="736" r="2.05"/><circle cx="272" cy="736" r="2.05"/><circle cx="280" cy="736" r="2.05"/><circle cx="288" cy="736" r="2.05"/><circle cx="296" cy="736" r="2.05"/><circle cx="304" cy="736" r="2.05"/><circle cx="312" cy="736" r="2.05"/><circle cx="320" cy="736" r="2.05"/><circle cx="328" cy="736" r="2.05"/><circle cx="336" cy="736" r="2.05"/><circle cx="344" cy="736" r="2.05"/><circle cx="352" cy="736" r="2.05"/><circle cx="360" cy="736" r="2.05"/><circle cx="368" cy="736" r="2.05"/><circle cx="376" cy="736" r="2.05"/><circle cx="384" cy="736" r="2.05"/><circle cx="392" cy="736" r="2.05"/><circle cx="400" cy="736" r="2.05"/><circle cx="408" cy="736" r="2.05"/><circle cx="416" cy="736" r="2.05"/><circle cx="424" cy="736" r="2.05"/><circle cx="432" cy="736" r="2.05"/><circle cx="440" cy="736" r="2.05"/><circle cx="448" cy="736" r="2.05"/><circle cx="456" cy="736" r="2.05"/><circle cx="464" cy="736" r="2.05"/><circle cx="472" cy="736" r="2.05"/><circle cx="480" cy="736" r="2.05"/><circle cx="488" cy="736" r="2.05"/><circle cx="496" cy="736" r="2.05"/><circle cx="504" cy="736" r="2.05"/><circle cx="512" cy="736" r="2.05"/><circle cx="520" cy="736" r="2.05"/><circle cx="152" cy="744" r="2.05"/><circle cx="160" cy="744" r="2.05"/><circle cx="168" cy="744" r="2.05"/><circle cx="176" cy="744" r="2.05"/><circle cx="184" cy="744" r="2.05"/><circle cx="192" cy="744" r="2.05"/><circle cx="200" cy="744" r="2.05"/><circle cx="208" cy="744" r="2.05"/><circle cx="216" cy="744" r="2.05"/><circle cx="224" cy="744" r="2.05"/><circle cx="232" cy="744" r="2.05"/><circle cx="240" cy="744" r="2.05"/><circle cx="248" cy="744" r="2.05"/><circle cx="256" cy="744" r="2.05"/><circle cx="264" cy="744" r="2.05"/><circle cx="272" cy="744" r="2.05"/><circle cx="280" cy="744" r="2.05"/><circle cx="288" cy="744" r="2.05"/><circle cx="296" cy="744" r="2.05"/><circle cx="304" cy="744" r="2.05"/><circle cx="312" cy="744" r="2.05"/><circle cx="320" cy="744" r="2.05"/><circle cx="328" cy="744" r="2.05"/><circle cx="336" cy="744" r="2.05"/><circle cx="344" cy="744" r="2.05"/><circle cx="352" cy="744" r="2.05"/><circle cx="360" cy="744" r="2.05"/><circle cx="368" cy="744" r="2.05"/><circle cx="376" cy="744" r="2.05"/><circle cx="384" cy="744" r="2.05"/><circle cx="392" cy="744" r="2.05"/><circle cx="400" cy="744" r="2.05"/><circle cx="408" cy="744" r="2.05"/><circle cx="416" cy="744" r="2.05"/><circle cx="424" cy="744" r="2.05"/><circle cx="432" cy="744" r="2.05"/><circle cx="440" cy="744" r="2.05"/><circle cx="448" cy="744" r="2.05"/><circle cx="456" cy="744" r="2.05"/><circle cx="464" cy="744" r="2.05"/><circle cx="472" cy="744" r="2.05"/><circle cx="480" cy="744" r="2.05"/><circle cx="488" cy="744" r="2.05"/><circle cx="496" cy="744" r="2.05"/><circle cx="504" cy="744" r="2.05"/><circle cx="512" cy="744" r="2.05"/><circle cx="160" cy="752" r="2.05"/><circle cx="168" cy="752" r="2.05"/><circle cx="176" cy="752" r="2.05"/><circle cx="184" cy="752" r="2.05"/><circle cx="192" cy="752" r="2.05"/><circle cx="200" cy="752" r="2.05"/><circle cx="208" cy="752" r="2.05"/><circle cx="216" cy="752" r="2.05"/><circle cx="224" cy="752" r="2.05"/><circle cx="232" cy="752" r="2.05"/><circle cx="240" cy="752" r="2.05"/><circle cx="248" cy="752" r="2.05"/><circle cx="256" cy="752" r="2.05"/><circle cx="264" cy="752" r="2.05"/><circle cx="272" cy="752" r="2.05"/><circle cx="280" cy="752" r="2.05"/><circle cx="288" cy="752" r="2.05"/><circle cx="296" cy="752" r="2.05"/><circle cx="304" cy="752" r="2.05"/><circle cx="312" cy="752" r="2.05"/><circle cx="320" cy="752" r="2.05"/><circle cx="328" cy="752" r="2.05"/><circle cx="336" cy="752" r="2.05"/><circle cx="344" cy="752" r="2.05"/><circle cx="352" cy="752" r="2.05"/><circle cx="360" cy="752" r="2.05"/><circle cx="368" cy="752" r="2.05"/><circle cx="376" cy="752" r="2.05"/><circle cx="384" cy="752" r="2.05"/><circle cx="392" cy="752" r="2.05"/><circle cx="400" cy="752" r="2.05"/><circle cx="408" cy="752" r="2.05"/><circle cx="416" cy="752" r="2.05"/><circle cx="424" cy="752" r="2.05"/><circle cx="432" cy="752" r="2.05"/><circle cx="440" cy="752" r="2.05"/><circle cx="448" cy="752" r="2.05"/><circle cx="456" cy="752" r="2.05"/><circle cx="464" cy="752" r="2.05"/><circle cx="472" cy="752" r="2.05"/><circle cx="480" cy="752" r="2.05"/><circle cx="488" cy="752" r="2.05"/><circle cx="496" cy="752" r="2.05"/><circle cx="504" cy="752" r="2.05"/><circle cx="896" cy="752" r="2.05"/><circle cx="160" cy="760" r="2.05"/><circle cx="168" cy="760" r="2.05"/><circle cx="176" cy="760" r="2.05"/><circle cx="184" cy="760" r="2.05"/><circle cx="192" cy="760" r="2.05"/><circle cx="200" cy="760" r="2.05"/><circle cx="208" cy="760" r="2.05"/><circle cx="216" cy="760" r="2.05"/><circle cx="224" cy="760" r="2.05"/><circle cx="232" cy="760" r="2.05"/><circle cx="240" cy="760" r="2.05"/><circle cx="248" cy="760" r="2.05"/><circle cx="256" cy="760" r="2.05"/><circle cx="264" cy="760" r="2.05"/><circle cx="272" cy="760" r="2.05"/><circle cx="280" cy="760" r="2.05"/><circle cx="288" cy="760" r="2.05"/><circle cx="296" cy="760" r="2.05"/><circle cx="304" cy="760" r="2.05"/><circle cx="312" cy="760" r="2.05"/><circle cx="320" cy="760" r="2.05"/><circle cx="328" cy="760" r="2.05"/><circle cx="336" cy="760" r="2.05"/><circle cx="344" cy="760" r="2.05"/><circle cx="352" cy="760" r="2.05"/><circle cx="360" cy="760" r="2.05"/><circle cx="368" cy="760" r="2.05"/><circle cx="376" cy="760" r="2.05"/><circle cx="384" cy="760" r="2.05"/><circle cx="392" cy="760" r="2.05"/><circle cx="400" cy="760" r="2.05"/><circle cx="408" cy="760" r="2.05"/><circle cx="416" cy="760" r="2.05"/><circle cx="424" cy="760" r="2.05"/><circle cx="432" cy="760" r="2.05"/><circle cx="440" cy="760" r="2.05"/><circle cx="448" cy="760" r="2.05"/><circle cx="456" cy="760" r="2.05"/><circle cx="464" cy="760" r="2.05"/><circle cx="472" cy="760" r="2.05"/><circle cx="480" cy="760" r="2.05"/><circle cx="488" cy="760" r="2.05"/><circle cx="496" cy="760" r="2.05"/><circle cx="168" cy="768" r="2.05"/><circle cx="176" cy="768" r="2.05"/><circle cx="184" cy="768" r="2.05"/><circle cx="192" cy="768" r="2.05"/><circle cx="200" cy="768" r="2.05"/><circle cx="208" cy="768" r="2.05"/><circle cx="216" cy="768" r="2.05"/><circle cx="224" cy="768" r="2.05"/><circle cx="232" cy="768" r="2.05"/><circle cx="240" cy="768" r="2.05"/><circle cx="248" cy="768" r="2.05"/><circle cx="256" cy="768" r="2.05"/><circle cx="264" cy="768" r="2.05"/><circle cx="272" cy="768" r="2.05"/><circle cx="280" cy="768" r="2.05"/><circle cx="288" cy="768" r="2.05"/><circle cx="296" cy="768" r="2.05"/><circle cx="304" cy="768" r="2.05"/><circle cx="312" cy="768" r="2.05"/><circle cx="320" cy="768" r="2.05"/><circle cx="328" cy="768" r="2.05"/><circle cx="336" cy="768" r="2.05"/><circle cx="344" cy="768" r="2.05"/><circle cx="352" cy="768" r="2.05"/><circle cx="360" cy="768" r="2.05"/><circle cx="368" cy="768" r="2.05"/><circle cx="376" cy="768" r="2.05"/><circle cx="384" cy="768" r="2.05"/><circle cx="392" cy="768" r="2.05"/><circle cx="400" cy="768" r="2.05"/><circle cx="408" cy="768" r="2.05"/><circle cx="416" cy="768" r="2.05"/><circle cx="424" cy="768" r="2.05"/><circle cx="432" cy="768" r="2.05"/><circle cx="440" cy="768" r="2.05"/><circle cx="448" cy="768" r="2.05"/><circle cx="456" cy="768" r="2.05"/><circle cx="464" cy="768" r="2.05"/><circle cx="472" cy="768" r="2.05"/><circle cx="480" cy="768" r="2.05"/><circle cx="488" cy="768" r="2.05"/><circle cx="496" cy="768" r="2.05"/><circle cx="184" cy="776" r="2.05"/><circle cx="192" cy="776" r="2.05"/><circle cx="200" cy="776" r="2.05"/><circle cx="208" cy="776" r="2.05"/><circle cx="216" cy="776" r="2.05"/><circle cx="224" cy="776" r="2.05"/><circle cx="232" cy="776" r="2.05"/><circle cx="240" cy="776" r="2.05"/><circle cx="248" cy="776" r="2.05"/><circle cx="256" cy="776" r="2.05"/><circle cx="264" cy="776" r="2.05"/><circle cx="272" cy="776" r="2.05"/><circle cx="280" cy="776" r="2.05"/><circle cx="288" cy="776" r="2.05"/><circle cx="296" cy="776" r="2.05"/><circle cx="304" cy="776" r="2.05"/><circle cx="312" cy="776" r="2.05"/><circle cx="320" cy="776" r="2.05"/><circle cx="328" cy="776" r="2.05"/><circle cx="336" cy="776" r="2.05"/><circle cx="344" cy="776" r="2.05"/><circle cx="352" cy="776" r="2.05"/><circle cx="360" cy="776" r="2.05"/><circle cx="368" cy="776" r="2.05"/><circle cx="376" cy="776" r="2.05"/><circle cx="384" cy="776" r="2.05"/><circle cx="392" cy="776" r="2.05"/><circle cx="400" cy="776" r="2.05"/><circle cx="408" cy="776" r="2.05"/><circle cx="416" cy="776" r="2.05"/><circle cx="424" cy="776" r="2.05"/><circle cx="432" cy="776" r="2.05"/><circle cx="440" cy="776" r="2.05"/><circle cx="448" cy="776" r="2.05"/><circle cx="456" cy="776" r="2.05"/><circle cx="464" cy="776" r="2.05"/><circle cx="472" cy="776" r="2.05"/><circle cx="480" cy="776" r="2.05"/><circle cx="488" cy="776" r="2.05"/><circle cx="496" cy="776" r="2.05"/><circle cx="200" cy="784" r="2.05"/><circle cx="208" cy="784" r="2.05"/><circle cx="216" cy="784" r="2.05"/><circle cx="224" cy="784" r="2.05"/><circle cx="232" cy="784" r="2.05"/><circle cx="240" cy="784" r="2.05"/><circle cx="248" cy="784" r="2.05"/><circle cx="256" cy="784" r="2.05"/><circle cx="264" cy="784" r="2.05"/><circle cx="272" cy="784" r="2.05"/><circle cx="280" cy="784" r="2.05"/><circle cx="288" cy="784" r="2.05"/><circle cx="296" cy="784" r="2.05"/><circle cx="304" cy="784" r="2.05"/><circle cx="312" cy="784" r="2.05"/><circle cx="320" cy="784" r="2.05"/><circle cx="328" cy="784" r="2.05"/><circle cx="336" cy="784" r="2.05"/><circle cx="344" cy="784" r="2.05"/><circle cx="352" cy="784" r="2.05"/><circle cx="360" cy="784" r="2.05"/><circle cx="368" cy="784" r="2.05"/><circle cx="376" cy="784" r="2.05"/><circle cx="384" cy="784" r="2.05"/><circle cx="392" cy="784" r="2.05"/><circle cx="400" cy="784" r="2.05"/><circle cx="408" cy="784" r="2.05"/><circle cx="416" cy="784" r="2.05"/><circle cx="424" cy="784" r="2.05"/><circle cx="432" cy="784" r="2.05"/><circle cx="440" cy="784" r="2.05"/><circle cx="448" cy="784" r="2.05"/><circle cx="456" cy="784" r="2.05"/><circle cx="464" cy="784" r="2.05"/><circle cx="472" cy="784" r="2.05"/><circle cx="480" cy="784" r="2.05"/><circle cx="488" cy="784" r="2.05"/><circle cx="216" cy="792" r="2.05"/><circle cx="224" cy="792" r="2.05"/><circle cx="232" cy="792" r="2.05"/><circle cx="240" cy="792" r="2.05"/><circle cx="248" cy="792" r="2.05"/><circle cx="256" cy="792" r="2.05"/><circle cx="264" cy="792" r="2.05"/><circle cx="272" cy="792" r="2.05"/><circle cx="280" cy="792" r="2.05"/><circle cx="288" cy="792" r="2.05"/><circle cx="296" cy="792" r="2.05"/><circle cx="304" cy="792" r="2.05"/><circle cx="312" cy="792" r="2.05"/><circle cx="320" cy="792" r="2.05"/><circle cx="328" cy="792" r="2.05"/><circle cx="336" cy="792" r="2.05"/><circle cx="344" cy="792" r="2.05"/><circle cx="352" cy="792" r="2.05"/><circle cx="360" cy="792" r="2.05"/><circle cx="368" cy="792" r="2.05"/><circle cx="376" cy="792" r="2.05"/><circle cx="384" cy="792" r="2.05"/><circle cx="392" cy="792" r="2.05"/><circle cx="400" cy="792" r="2.05"/><circle cx="408" cy="792" r="2.05"/><circle cx="416" cy="792" r="2.05"/><circle cx="424" cy="792" r="2.05"/><circle cx="432" cy="792" r="2.05"/><circle cx="440" cy="792" r="2.05"/><circle cx="448" cy="792" r="2.05"/><circle cx="456" cy="792" r="2.05"/><circle cx="464" cy="792" r="2.05"/><circle cx="472" cy="792" r="2.05"/><circle cx="480" cy="792" r="2.05"/><circle cx="488" cy="792" r="2.05"/><circle cx="216" cy="800" r="2.05"/><circle cx="224" cy="800" r="2.05"/><circle cx="232" cy="800" r="2.05"/><circle cx="240" cy="800" r="2.05"/><circle cx="248" cy="800" r="2.05"/><circle cx="256" cy="800" r="2.05"/><circle cx="264" cy="800" r="2.05"/><circle cx="272" cy="800" r="2.05"/><circle cx="280" cy="800" r="2.05"/><circle cx="288" cy="800" r="2.05"/><circle cx="296" cy="800" r="2.05"/><circle cx="304" cy="800" r="2.05"/><circle cx="312" cy="800" r="2.05"/><circle cx="320" cy="800" r="2.05"/><circle cx="328" cy="800" r="2.05"/><circle cx="336" cy="800" r="2.05"/><circle cx="344" cy="800" r="2.05"/><circle cx="352" cy="800" r="2.05"/><circle cx="360" cy="800" r="2.05"/><circle cx="368" cy="800" r="2.05"/><circle cx="376" cy="800" r="2.05"/><circle cx="384" cy="800" r="2.05"/><circle cx="392" cy="800" r="2.05"/><circle cx="400" cy="800" r="2.05"/><circle cx="408" cy="800" r="2.05"/><circle cx="416" cy="800" r="2.05"/><circle cx="424" cy="800" r="2.05"/><circle cx="432" cy="800" r="2.05"/><circle cx="440" cy="800" r="2.05"/><circle cx="448" cy="800" r="2.05"/><circle cx="456" cy="800" r="2.05"/><circle cx="464" cy="800" r="2.05"/><circle cx="472" cy="800" r="2.05"/><circle cx="480" cy="800" r="2.05"/><circle cx="488" cy="800" r="2.05"/><circle cx="224" cy="808" r="2.05"/><circle cx="232" cy="808" r="2.05"/><circle cx="240" cy="808" r="2.05"/><circle cx="248" cy="808" r="2.05"/><circle cx="256" cy="808" r="2.05"/><circle cx="264" cy="808" r="2.05"/><circle cx="272" cy="808" r="2.05"/><circle cx="280" cy="808" r="2.05"/><circle cx="288" cy="808" r="2.05"/><circle cx="296" cy="808" r="2.05"/><circle cx="304" cy="808" r="2.05"/><circle cx="312" cy="808" r="2.05"/><circle cx="320" cy="808" r="2.05"/><circle cx="328" cy="808" r="2.05"/><circle cx="336" cy="808" r="2.05"/><circle cx="344" cy="808" r="2.05"/><circle cx="352" cy="808" r="2.05"/><circle cx="360" cy="808" r="2.05"/><circle cx="368" cy="808" r="2.05"/><circle cx="376" cy="808" r="2.05"/><circle cx="384" cy="808" r="2.05"/><circle cx="392" cy="808" r="2.05"/><circle cx="400" cy="808" r="2.05"/><circle cx="408" cy="808" r="2.05"/><circle cx="416" cy="808" r="2.05"/><circle cx="424" cy="808" r="2.05"/><circle cx="432" cy="808" r="2.05"/><circle cx="440" cy="808" r="2.05"/><circle cx="448" cy="808" r="2.05"/><circle cx="456" cy="808" r="2.05"/><circle cx="464" cy="808" r="2.05"/><circle cx="472" cy="808" r="2.05"/><circle cx="480" cy="808" r="2.05"/><circle cx="224" cy="816" r="2.05"/><circle cx="232" cy="816" r="2.05"/><circle cx="240" cy="816" r="2.05"/><circle cx="248" cy="816" r="2.05"/><circle cx="256" cy="816" r="2.05"/><circle cx="264" cy="816" r="2.05"/><circle cx="272" cy="816" r="2.05"/><circle cx="280" cy="816" r="2.05"/><circle cx="288" cy="816" r="2.05"/><circle cx="296" cy="816" r="2.05"/><circle cx="304" cy="816" r="2.05"/><circle cx="312" cy="816" r="2.05"/><circle cx="320" cy="816" r="2.05"/><circle cx="328" cy="816" r="2.05"/><circle cx="336" cy="816" r="2.05"/><circle cx="344" cy="816" r="2.05"/><circle cx="352" cy="816" r="2.05"/><circle cx="360" cy="816" r="2.05"/><circle cx="368" cy="816" r="2.05"/><circle cx="376" cy="816" r="2.05"/><circle cx="384" cy="816" r="2.05"/><circle cx="392" cy="816" r="2.05"/><circle cx="400" cy="816" r="2.05"/><circle cx="408" cy="816" r="2.05"/><circle cx="416" cy="816" r="2.05"/><circle cx="424" cy="816" r="2.05"/><circle cx="432" cy="816" r="2.05"/><circle cx="440" cy="816" r="2.05"/><circle cx="448" cy="816" r="2.05"/><circle cx="456" cy="816" r="2.05"/><circle cx="464" cy="816" r="2.05"/><circle cx="472" cy="816" r="2.05"/><circle cx="224" cy="824" r="2.05"/><circle cx="232" cy="824" r="2.05"/><circle cx="240" cy="824" r="2.05"/><circle cx="248" cy="824" r="2.05"/><circle cx="256" cy="824" r="2.05"/><circle cx="264" cy="824" r="2.05"/><circle cx="272" cy="824" r="2.05"/><circle cx="280" cy="824" r="2.05"/><circle cx="288" cy="824" r="2.05"/><circle cx="296" cy="824" r="2.05"/><circle cx="304" cy="824" r="2.05"/><circle cx="312" cy="824" r="2.05"/><circle cx="320" cy="824" r="2.05"/><circle cx="328" cy="824" r="2.05"/><circle cx="336" cy="824" r="2.05"/><circle cx="344" cy="824" r="2.05"/><circle cx="352" cy="824" r="2.05"/><circle cx="360" cy="824" r="2.05"/><circle cx="368" cy="824" r="2.05"/><circle cx="376" cy="824" r="2.05"/><circle cx="384" cy="824" r="2.05"/><circle cx="392" cy="824" r="2.05"/><circle cx="400" cy="824" r="2.05"/><circle cx="408" cy="824" r="2.05"/><circle cx="416" cy="824" r="2.05"/><circle cx="424" cy="824" r="2.05"/><circle cx="432" cy="824" r="2.05"/><circle cx="440" cy="824" r="2.05"/><circle cx="448" cy="824" r="2.05"/><circle cx="456" cy="824" r="2.05"/><circle cx="464" cy="824" r="2.05"/><circle cx="472" cy="824" r="2.05"/><circle cx="224" cy="832" r="2.05"/><circle cx="232" cy="832" r="2.05"/><circle cx="240" cy="832" r="2.05"/><circle cx="248" cy="832" r="2.05"/><circle cx="256" cy="832" r="2.05"/><circle cx="264" cy="832" r="2.05"/><circle cx="272" cy="832" r="2.05"/><circle cx="280" cy="832" r="2.05"/><circle cx="288" cy="832" r="2.05"/><circle cx="296" cy="832" r="2.05"/><circle cx="304" cy="832" r="2.05"/><circle cx="312" cy="832" r="2.05"/><circle cx="320" cy="832" r="2.05"/><circle cx="328" cy="832" r="2.05"/><circle cx="336" cy="832" r="2.05"/><circle cx="344" cy="832" r="2.05"/><circle cx="352" cy="832" r="2.05"/><circle cx="360" cy="832" r="2.05"/><circle cx="368" cy="832" r="2.05"/><circle cx="376" cy="832" r="2.05"/><circle cx="384" cy="832" r="2.05"/><circle cx="392" cy="832" r="2.05"/><circle cx="400" cy="832" r="2.05"/><circle cx="408" cy="832" r="2.05"/><circle cx="416" cy="832" r="2.05"/><circle cx="424" cy="832" r="2.05"/><circle cx="432" cy="832" r="2.05"/><circle cx="440" cy="832" r="2.05"/><circle cx="224" cy="840" r="2.05"/><circle cx="232" cy="840" r="2.05"/><circle cx="240" cy="840" r="2.05"/><circle cx="248" cy="840" r="2.05"/><circle cx="256" cy="840" r="2.05"/><circle cx="264" cy="840" r="2.05"/><circle cx="272" cy="840" r="2.05"/><circle cx="280" cy="840" r="2.05"/><circle cx="288" cy="840" r="2.05"/><circle cx="296" cy="840" r="2.05"/><circle cx="304" cy="840" r="2.05"/><circle cx="312" cy="840" r="2.05"/><circle cx="320" cy="840" r="2.05"/><circle cx="328" cy="840" r="2.05"/><circle cx="336" cy="840" r="2.05"/><circle cx="344" cy="840" r="2.05"/><circle cx="352" cy="840" r="2.05"/><circle cx="360" cy="840" r="2.05"/><circle cx="368" cy="840" r="2.05"/><circle cx="376" cy="840" r="2.05"/><circle cx="384" cy="840" r="2.05"/><circle cx="392" cy="840" r="2.05"/><circle cx="400" cy="840" r="2.05"/><circle cx="408" cy="840" r="2.05"/><circle cx="416" cy="840" r="2.05"/><circle cx="224" cy="848" r="2.05"/><circle cx="232" cy="848" r="2.05"/><circle cx="240" cy="848" r="2.05"/><circle cx="248" cy="848" r="2.05"/><circle cx="256" cy="848" r="2.05"/><circle cx="264" cy="848" r="2.05"/><circle cx="272" cy="848" r="2.05"/><circle cx="280" cy="848" r="2.05"/><circle cx="288" cy="848" r="2.05"/><circle cx="296" cy="848" r="2.05"/><circle cx="304" cy="848" r="2.05"/><circle cx="312" cy="848" r="2.05"/><circle cx="320" cy="848" r="2.05"/><circle cx="328" cy="848" r="2.05"/><circle cx="336" cy="848" r="2.05"/><circle cx="344" cy="848" r="2.05"/><circle cx="352" cy="848" r="2.05"/><circle cx="360" cy="848" r="2.05"/><circle cx="368" cy="848" r="2.05"/><circle cx="376" cy="848" r="2.05"/><circle cx="384" cy="848" r="2.05"/><circle cx="392" cy="848" r="2.05"/><circle cx="400" cy="848" r="2.05"/><circle cx="408" cy="848" r="2.05"/><circle cx="224" cy="856" r="2.05"/><circle cx="232" cy="856" r="2.05"/><circle cx="240" cy="856" r="2.05"/><circle cx="248" cy="856" r="2.05"/><circle cx="256" cy="856" r="2.05"/><circle cx="264" cy="856" r="2.05"/><circle cx="272" cy="856" r="2.05"/><circle cx="280" cy="856" r="2.05"/><circle cx="288" cy="856" r="2.05"/><circle cx="296" cy="856" r="2.05"/><circle cx="304" cy="856" r="2.05"/><circle cx="312" cy="856" r="2.05"/><circle cx="320" cy="856" r="2.05"/><circle cx="328" cy="856" r="2.05"/><circle cx="336" cy="856" r="2.05"/><circle cx="344" cy="856" r="2.05"/><circle cx="352" cy="856" r="2.05"/><circle cx="360" cy="856" r="2.05"/><circle cx="368" cy="856" r="2.05"/><circle cx="376" cy="856" r="2.05"/><circle cx="384" cy="856" r="2.05"/><circle cx="392" cy="856" r="2.05"/><circle cx="400" cy="856" r="2.05"/><circle cx="408" cy="856" r="2.05"/><circle cx="224" cy="864" r="2.05"/><circle cx="232" cy="864" r="2.05"/><circle cx="240" cy="864" r="2.05"/><circle cx="248" cy="864" r="2.05"/><circle cx="256" cy="864" r="2.05"/><circle cx="264" cy="864" r="2.05"/><circle cx="272" cy="864" r="2.05"/><circle cx="280" cy="864" r="2.05"/><circle cx="288" cy="864" r="2.05"/><circle cx="296" cy="864" r="2.05"/><circle cx="304" cy="864" r="2.05"/><circle cx="312" cy="864" r="2.05"/><circle cx="320" cy="864" r="2.05"/><circle cx="328" cy="864" r="2.05"/><circle cx="336" cy="864" r="2.05"/><circle cx="344" cy="864" r="2.05"/><circle cx="352" cy="864" r="2.05"/><circle cx="360" cy="864" r="2.05"/><circle cx="368" cy="864" r="2.05"/><circle cx="376" cy="864" r="2.05"/><circle cx="384" cy="864" r="2.05"/><circle cx="392" cy="864" r="2.05"/><circle cx="400" cy="864" r="2.05"/><circle cx="408" cy="864" r="2.05"/><circle cx="224" cy="872" r="2.05"/><circle cx="232" cy="872" r="2.05"/><circle cx="240" cy="872" r="2.05"/><circle cx="248" cy="872" r="2.05"/><circle cx="256" cy="872" r="2.05"/><circle cx="264" cy="872" r="2.05"/><circle cx="272" cy="872" r="2.05"/><circle cx="280" cy="872" r="2.05"/><circle cx="288" cy="872" r="2.05"/><circle cx="296" cy="872" r="2.05"/><circle cx="304" cy="872" r="2.05"/><circle cx="312" cy="872" r="2.05"/><circle cx="320" cy="872" r="2.05"/><circle cx="328" cy="872" r="2.05"/><circle cx="336" cy="872" r="2.05"/><circle cx="344" cy="872" r="2.05"/><circle cx="352" cy="872" r="2.05"/><circle cx="360" cy="872" r="2.05"/><circle cx="368" cy="872" r="2.05"/><circle cx="376" cy="872" r="2.05"/><circle cx="384" cy="872" r="2.05"/><circle cx="392" cy="872" r="2.05"/><circle cx="400" cy="872" r="2.05"/><circle cx="232" cy="880" r="2.05"/><circle cx="240" cy="880" r="2.05"/><circle cx="248" cy="880" r="2.05"/><circle cx="256" cy="880" r="2.05"/><circle cx="264" cy="880" r="2.05"/><circle cx="272" cy="880" r="2.05"/><circle cx="280" cy="880" r="2.05"/><circle cx="288" cy="880" r="2.05"/><circle cx="296" cy="880" r="2.05"/><circle cx="304" cy="880" r="2.05"/><circle cx="312" cy="880" r="2.05"/><circle cx="320" cy="880" r="2.05"/><circle cx="328" cy="880" r="2.05"/><circle cx="336" cy="880" r="2.05"/><circle cx="344" cy="880" r="2.05"/><circle cx="352" cy="880" r="2.05"/><circle cx="360" cy="880" r="2.05"/><circle cx="368" cy="880" r="2.05"/><circle cx="376" cy="880" r="2.05"/><circle cx="384" cy="880" r="2.05"/><circle cx="392" cy="880" r="2.05"/><circle cx="232" cy="888" r="2.05"/><circle cx="240" cy="888" r="2.05"/><circle cx="248" cy="888" r="2.05"/><circle cx="256" cy="888" r="2.05"/><circle cx="264" cy="888" r="2.05"/><circle cx="272" cy="888" r="2.05"/><circle cx="280" cy="888" r="2.05"/><circle cx="288" cy="888" r="2.05"/><circle cx="296" cy="888" r="2.05"/><circle cx="304" cy="888" r="2.05"/><circle cx="312" cy="888" r="2.05"/><circle cx="320" cy="888" r="2.05"/><circle cx="328" cy="888" r="2.05"/><circle cx="336" cy="888" r="2.05"/><circle cx="344" cy="888" r="2.05"/><circle cx="352" cy="888" r="2.05"/><circle cx="360" cy="888" r="2.05"/><circle cx="368" cy="888" r="2.05"/><circle cx="376" cy="888" r="2.05"/><circle cx="384" cy="888" r="2.05"/><circle cx="232" cy="896" r="2.05"/><circle cx="240" cy="896" r="2.05"/><circle cx="248" cy="896" r="2.05"/><circle cx="256" cy="896" r="2.05"/><circle cx="264" cy="896" r="2.05"/><circle cx="272" cy="896" r="2.05"/><circle cx="280" cy="896" r="2.05"/><circle cx="288" cy="896" r="2.05"/><circle cx="296" cy="896" r="2.05"/><circle cx="304" cy="896" r="2.05"/><circle cx="312" cy="896" r="2.05"/><circle cx="320" cy="896" r="2.05"/><circle cx="328" cy="896" r="2.05"/><circle cx="336" cy="896" r="2.05"/><circle cx="344" cy="896" r="2.05"/><circle cx="352" cy="896" r="2.05"/><circle cx="360" cy="896" r="2.05"/><circle cx="368" cy="896" r="2.05"/><circle cx="376" cy="896" r="2.05"/><circle cx="232" cy="904" r="2.05"/><circle cx="240" cy="904" r="2.05"/><circle cx="248" cy="904" r="2.05"/><circle cx="256" cy="904" r="2.05"/><circle cx="264" cy="904" r="2.05"/><circle cx="272" cy="904" r="2.05"/><circle cx="280" cy="904" r="2.05"/><circle cx="288" cy="904" r="2.05"/><circle cx="296" cy="904" r="2.05"/><circle cx="304" cy="904" r="2.05"/><circle cx="312" cy="904" r="2.05"/><circle cx="320" cy="904" r="2.05"/><circle cx="328" cy="904" r="2.05"/><circle cx="344" cy="904" r="2.05"/><circle cx="352" cy="904" r="2.05"/><circle cx="360" cy="904" r="2.05"/><circle cx="368" cy="904" r="2.05"/><circle cx="232" cy="912" r="2.05"/><circle cx="240" cy="912" r="2.05"/><circle cx="248" cy="912" r="2.05"/><circle cx="256" cy="912" r="2.05"/><circle cx="264" cy="912" r="2.05"/><circle cx="272" cy="912" r="2.05"/><circle cx="280" cy="912" r="2.05"/><circle cx="288" cy="912" r="2.05"/><circle cx="296" cy="912" r="2.05"/><circle cx="304" cy="912" r="2.05"/><circle cx="312" cy="912" r="2.05"/><circle cx="320" cy="912" r="2.05"/><circle cx="328" cy="912" r="2.05"/><circle cx="336" cy="912" r="2.05"/><circle cx="232" cy="920" r="2.05"/><circle cx="240" cy="920" r="2.05"/><circle cx="248" cy="920" r="2.05"/><circle cx="256" cy="920" r="2.05"/><circle cx="264" cy="920" r="2.05"/><circle cx="272" cy="920" r="2.05"/><circle cx="280" cy="920" r="2.05"/><circle cx="288" cy="920" r="2.05"/><circle cx="296" cy="920" r="2.05"/><circle cx="304" cy="920" r="2.05"/><circle cx="312" cy="920" r="2.05"/><circle cx="320" cy="920" r="2.05"/><circle cx="328" cy="920" r="2.05"/><circle cx="336" cy="920" r="2.05"/><circle cx="344" cy="920" r="2.05"/><circle cx="240" cy="928" r="2.05"/><circle cx="248" cy="928" r="2.05"/><circle cx="256" cy="928" r="2.05"/><circle cx="264" cy="928" r="2.05"/><circle cx="272" cy="928" r="2.05"/><circle cx="280" cy="928" r="2.05"/><circle cx="288" cy="928" r="2.05"/><circle cx="296" cy="928" r="2.05"/><circle cx="304" cy="928" r="2.05"/><circle cx="312" cy="928" r="2.05"/><circle cx="320" cy="928" r="2.05"/><circle cx="328" cy="928" r="2.05"/><circle cx="248" cy="936" r="2.05"/><circle cx="256" cy="936" r="2.05"/><circle cx="264" cy="936" r="2.05"/><circle cx="272" cy="936" r="2.05"/><circle cx="280" cy="936" r="2.05"/><circle cx="288" cy="936" r="2.05"/><circle cx="296" cy="936" r="2.05"/><circle cx="304" cy="936" r="2.05"/><circle cx="312" cy="936" r="2.05"/><circle cx="264" cy="944" r="2.05"/><circle cx="272" cy="944" r="2.05"/><circle cx="280" cy="944" r="2.05"/><circle cx="288" cy="944" r="2.05"/><circle cx="296" cy="944" r="2.05"/><circle cx="280" cy="952" r="2.05"/><circle cx="288" cy="952" r="2.05"/><circle cx="296" cy="952" r="2.05"/><circle cx="296" cy="960" r="2.05"/></g></svg></div></div>
  <div class="wd-tr-content">
   <div class="wd-transformacao-content">

   <div class="wd-transformacao-heading">
    <p class="wd-transformacao-eyebrow wd-uptitle">EXPLORE</p>
    <h2 id="wd-transformacao-title" class="wd-transformacao-title wd-section-title">Transformação digital</h2>
   </div>
   <p class="wd-transformacao-description wd-section-desc">Transformação digital é colocar a sua empresa onde o cliente já está. Organizamos sua presença online, do site às redes sociais, com processos simples de acompanhar, para você atender melhor, vender mais e decidir com base em números reais.</p>
   </div>
  <a class="wd-transformacao-cta wd-cta" data-wd-contact href="#contato"><span>SOLICITE PROPOSTA</span><svg class="wd-transformacao-cta-icon" viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.0641 1.14239L.499 12.7061M1.9673.7061h9.5726c.53 0 .9591.4291.9591.9605v9.5712" stroke="currentColor" stroke-width="1.41181"/></svg></a>
  </div>
 </div>
 <div class="wd-certifications" aria-label="Certificados oficiais da Work Digital">
 <img src="<?php echo WD_URI; ?>/media/cert-wordpress.svg" alt="WordPress" loading="lazy" decoding="async">
 <img src="<?php echo WD_URI; ?>/media/cert-rd-station.svg" alt="RD Station" loading="lazy" decoding="async">
 <img src="<?php echo WD_URI; ?>/media/cert-mailchimp.svg" alt="Mailchimp" loading="lazy" decoding="async">
 <img src="<?php echo WD_URI; ?>/media/cert-shopify.svg" alt="Shopify" loading="lazy" decoding="async">
 <img src="<?php echo WD_URI; ?>/media/cert-loja-integrada.svg" alt="Loja Integrada" loading="lazy" decoding="async">
 <img src="<?php echo WD_URI; ?>/media/cert-nuvem-shop.svg" alt="Nuvemshop" loading="lazy" decoding="async">
</div>
</section>

<style>
/* Confiança: Auros Trust composition adapted to Work Digital assets. */
#wd-trust{background:transparent;padding:24px 0 80px;color:#fff;font-family:"Space Grotesk",Arial,sans-serif;scroll-margin-top:110px}
#wd-trust *{box-sizing:border-box}
.wd-trust-panel{width:min(1360px,calc(100% - 64px));margin:0 auto;padding:80px 0 40px;border-radius:16px;overflow:hidden;background:rgba(37,17,67,.62);box-shadow:0 0 100px rgba(96,37,225,.12)}
.wd-trust-header{text-align:center;padding:0 40px 46px}
.wd-trust-eyebrow{margin:0 0 32px;font-size:20px;line-height:1.4;font-weight:500;letter-spacing:.2em;text-transform:uppercase;}
.wd-trust-title{margin:0;text-wrap:balance}
.wd-trust-controls{display:none;justify-content:flex-end;gap:12px;padding:0 32px 20px}
.wd-trust-control{width:44px;height:44px;border:1px solid rgba(203,182,255,.45);border-radius:4px;background:transparent;color:#fff;cursor:pointer;font:24px/1 system-ui;transition:background-color .2s}
.wd-trust-control:hover{background:rgba(96,37,225,.5)}
.wd-trust-control:disabled{opacity:.35;cursor:default}
.wd-trust-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));padding:0 40px;gap:0;list-style:none;margin:0}
.wd-trust-card{position:relative;isolation:isolate;display:flex;flex-direction:column;justify-content:space-between;gap:32px;min-width:0;min-height:0;margin:0;padding:48px 36px;border-radius:16px;outline-offset:-3px}
.wd-trust-card::before{content:"";position:absolute;inset:0;z-index:-1;border-radius:inherit;background:linear-gradient(0deg,#34165b,#54258d);opacity:0;transition:opacity .2s ease-in-out}
.wd-trust-card::after{content:"";position:absolute;right:0;top:48px;bottom:48px;width:1px;background:rgba(203,182,255,.16);transition:opacity .2s}
.wd-trust-card:hover::before,.wd-trust-card:focus-visible::before{opacity:1}
.wd-trust-card:hover::after,.wd-trust-card:focus-visible::after{opacity:0}
.wd-trust-quote{margin:0;color:#f2f2f2;font-family:"Nunito",system-ui,sans-serif;font-size:clamp(18px,1.5vw,20px);font-weight:400;line-height:1.3}
.wd-trust-quote::before{content:"“"}.wd-trust-quote::after{content:"”"}
.wd-trust-attribution{display:flex;flex-direction:column;align-items:flex-start;gap:32px;margin:0}
.wd-trust-person{margin:0;color:#d7cde5;font-size:clamp(16px,1.46vw,20px);line-height:1.4;letter-spacing:.025em;text-transform:uppercase;font-style:normal;font-weight:400}
.wd-trust-person span{display:block}
.wd-trust-marquee{overflow:hidden;width:100%;margin-top:48px;position:relative}
.wd-trust-track{display:flex;width:max-content;animation:wd-trust-marquee var(--wd-trust-duration,180s) linear infinite;animation-play-state:paused;will-change:transform}
.wd-trust-logo-group{display:flex;align-items:center;flex-shrink:0;list-style:none;padding:0;margin:0}
.wd-trust-logo-item{display:flex;justify-content:center;align-items:center;flex:0 0 220px;width:220px;height:56px;padding-right:70px}
.wd-trust-logo{display:block;max-width:150px;max-height:56px;width:auto;height:auto;object-fit:contain}
#wd-trust :focus-visible{outline:2px solid #cbb6ff;outline-offset:5px}
#wd-trust .wd-trust-card:focus-visible{outline-offset:-3px}
@keyframes wd-trust-marquee{to{transform:translateX(-50%)}}
@media(max-width:1179px){
 .wd-trust-panel{padding:64px 0 32px;width:calc(100% - 32px)}
 .wd-trust-header{padding:0 32px 40px}
 .wd-trust-controls{display:flex}
 .wd-trust-grid{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;overscroll-behavior-x:contain;scrollbar-width:thin;scrollbar-color:#7d51b8 transparent;padding:0 32px 16px;scroll-padding-inline:32px}
 .wd-trust-card{flex:0 0 calc(100% / 1.06);scroll-snap-align:start;padding:40px 32px}
 .wd-trust-quote{font-size:20px;line-height:1.5}
 .wd-trust-person{font-size:18px}
 .wd-trust-marquee{margin-top:40px}
}
@media(max-width:600px){
 #wd-trust{padding:16px 0 48px}
 .wd-trust-panel{padding:48px 0 24px}
 .wd-trust-header{padding:0 24px 32px}
 .wd-trust-eyebrow{font-size:16px;margin-bottom:24px}
 .wd-trust-title{}
 .wd-trust-controls{padding:0 24px 16px}
 .wd-trust-grid{padding:0 16px 16px;scroll-padding-inline:16px}
 .wd-trust-card{padding:32px 24px;gap:32px;min-height:0}
 .wd-trust-quote{font-size:18px;line-height:1.5}
 .wd-trust-person{font-size:16px}
 .wd-trust-attribution{gap:24px}
 .wd-trust-marquee{margin-top:32px}
 .wd-trust-logo-item{flex-basis:180px;width:180px;padding-right:40px;height:48px}
 .wd-trust-logo{max-width:140px;max-height:48px}
}
@media(prefers-reduced-motion:reduce){
 .wd-trust-track{animation:none;will-change:auto;width:100%}
 .wd-trust-logo-group{width:100%;flex-wrap:wrap;justify-content:center;gap:24px}
 .wd-trust-logo-group[aria-hidden="true"],.wd-trust-logo-repeat{display:none}
 .wd-trust-logo-item{flex:0 0 150px;width:150px;padding-right:0}
 .wd-trust-card::before,.wd-trust-card::after,.wd-trust-control{transition:none}
}
</style>
<!-- Inserir depois de #wd-transformacao. Fontes já carregadas na home. -->


<section id="wd-blog" class="wd-blog-section" aria-labelledby="wd-blog-title">
  <div class="wd-blog-inner">
    <header class="wd-blog-header">
      <p class="wd-blog-eyebrow wd-uptitle">BLOG</p>
      <h2 id="wd-blog-title" class="wd-blog-title wd-section-title">Insights e perspectivas</h2>
      <p class="wd-blog-intro wd-section-desc">Explore ideias, tendências do digital e o que aprendemos criando sites, blogs e landing pages.</p>
    </header>

    <!-- Dois artigos: mesma quantidade da lista desktop atual da Auros.
         Dados reais da home da Work; resumos e datas do WordPress oficial. -->
    <div class="wd-blog-list">
<?php get_template_part('parts/home-blog'); ?>
    </div>

    <div class="wd-blog-footer">
      <a class="wd-blog-cta wd-cta" href="<?php echo esc_url(wd_url('blog/')); ?>">
        <span>VER TODOS OS ARTIGOS</span>
        <svg aria-hidden="true" viewBox="0 0 14 14" fill="none"><path d="M12.065 1.142L.5 12.706M1.968 .706h9.573c.53 0 .959.429.959.961v9.571" stroke="currentColor" stroke-width="1.412"/></svg>
      </a>
    </div>
  </div>
</section>

<style>
#wd-statement-2,#wd-blog{box-sizing:border-box;background:transparent;color:#f7f6fb;font-family:"Space Grotesk",Arial,sans-serif}
#wd-statement-2 *,#wd-blog *{box-sizing:border-box}
.wd-statement-2-section{min-height:75vh;display:flex;align-items:center;justify-content:center;padding:96px 40px}
.wd-statement-2-inner{width:100%;max-width:1200px;margin-inline:auto}
.wd-statement-2-title{margin:0;font-size:clamp(44px,6.835vw,120px);font-weight:500;line-height:1;letter-spacing:-.04167em;text-align:center;text-wrap:balance;color:#efe7ff}
.wd-statement-2-line{display:block;padding-bottom:.055em;--wd-from:#6025e1;--wd-to:#cbb6ff;color:#efe7ff}
.wd-blog-section{padding:120px 40px;scroll-margin-top:110px}
.wd-blog-inner{max-width:1520px;margin-inline:auto;padding-inline:40px}
.wd-blog-header{display:flex;flex-direction:column;align-items:center;text-align:center;margin-bottom:80px}
.wd-blog-eyebrow{margin:0 0 31px;font-size:clamp(16px,1.46vw,22px);font-weight:500;line-height:1.4;letter-spacing:.24em;}
.wd-blog-title{margin:0;color:#f7f6fb;text-wrap:balance}
.wd-blog-intro,.wd-blog-excerpt{font-family:"Nunito",system-ui,sans-serif;font-size:16px;font-weight:400;line-height:1.6;color:#d9cfe7}
.wd-blog-intro{max-width:420px;margin:48px 0 0;text-wrap:pretty}
.wd-blog-list{display:grid;grid-template-columns:minmax(0,1fr);margin-bottom:80px}
.wd-blog-item{min-width:0;border-bottom:1px solid rgba(151,112,211,.25);transition:border-color .2s ease-in-out}
.wd-blog-link{position:relative;isolation:isolate;display:grid;grid-template-columns:250px minmax(0,1fr) 50px;align-items:start;column-gap:clamp(40px,7.196vw,97px);padding:40px;border-radius:16px;overflow:hidden;text-decoration:none;color:inherit}
.wd-blog-link::before{content:"";position:absolute;z-index:-1;inset:0;background:linear-gradient(0deg,#301258,#4b247e);opacity:0;transition:opacity .2s ease-in-out}
.wd-blog-image{display:block;width:100%;height:auto;aspect-ratio:25/16;object-fit:cover;border-radius:6px}
.wd-blog-content{display:flex;flex-direction:column;gap:24px;min-width:0;max-width:710px}
.wd-blog-article-title{margin:0;font-size:clamp(28px,2.623vw,42px);font-weight:500;line-height:1;letter-spacing:0;text-wrap:pretty;overflow-wrap:break-word;color:#f7f6fb}
.wd-blog-excerpt{margin:0}
.wd-blog-meta{display:flex;flex-wrap:wrap;gap:8px 18px;color:#cfc1e4;font-size:14px;font-weight:400;line-height:1.4;text-transform:uppercase;letter-spacing:.025em}
.wd-blog-arrow{display:flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:6px;background:rgba(255,255,255,.05);color:#f7f6fb}
.wd-blog-arrow svg{display:block;width:18px;height:18px}
.wd-blog-footer{display:flex;justify-content:center}
.wd-blog-cta{display:flex;align-items:center;justify-content:center;gap:20px;min-height:54px;max-width:100%;padding:18px 20px;border-radius:6px;background:linear-gradient(90deg,#e7dcff,#f5c3d8,#6025e1,#341365);background-size:280% 100%;background-position:100% 0;color:#fff;text-decoration:none;font-size:inherit;transition:background-position 600ms ease,color 200ms ease}
.wd-blog-cta svg{flex:none;width:14px;height:14px}
.wd-blog-cta:hover,.wd-blog-cta:focus-visible{background-position:0 0;color:#2b1450}
.wd-blog-link:focus-visible,.wd-blog-cta:focus-visible{outline:2px solid #e7dcff;outline-offset:5px}
.wd-blog-link:focus-visible::before{opacity:1}
.wd-blog-item:focus-within{border-bottom-color:transparent}
@supports (background-clip:text) or (-webkit-background-clip:text){
 .wd-statement-2-line{background:linear-gradient(90deg,var(--wd-from),var(--wd-to));background-clip:text;-webkit-background-clip:text;color:transparent;-webkit-text-fill-color:transparent}
 .wd-blog-eyebrow{;}
}
/* O título da Auros é sólido; somente o eyebrow e a frase têm gradiente. */
@media not all and (pointer: coarse){
 .wd-blog-link:hover::before{opacity:1}
 .wd-blog-item:hover,.wd-blog-item:has(+ .wd-blog-item:hover){border-bottom-color:transparent}
}
@media (max-width:1199px) and (min-width:992px){
 .wd-blog-link{grid-template-columns:210px minmax(0,1fr) 50px;gap:40px;padding:32px}
}
@media (max-width:991px){
 .wd-statement-2-section{min-height:65vh;padding:72px 24px}
 .wd-statement-2-title{font-size:clamp(44px,7.2vw,76px)}
 .wd-blog-section{padding:80px 20px}
 .wd-blog-inner{padding-inline:20px}
 .wd-blog-list{grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
 .wd-blog-item{border:0;border-radius:16px;background:linear-gradient(0deg,#301258,#4b247e)}
 .wd-blog-link{height:100%;grid-template-columns:minmax(0,1fr) 50px;gap:36px 16px;padding:24px 24px 42px}
 .wd-blog-image{grid-column:1/-1;aspect-ratio:16/9}
 .wd-blog-content{display:contents}
 .wd-blog-article-title{grid-column:1;grid-row:2;font-size:30px}
 .wd-blog-arrow{grid-column:2;grid-row:2}
 .wd-blog-excerpt,.wd-blog-meta{grid-column:1/-1}
 .wd-blog-link::before{display:none}
 .wd-blog-item:focus-within{outline:2px solid #e7dcff;outline-offset:4px}
 .wd-blog-link:focus-visible{outline:none}
}
@media (max-width:600px){
 .wd-statement-2-section{min-height:60vh;padding:64px 20px}
 .wd-statement-2-title{font-size:clamp(36px,9.4vw,56px)}
 .wd-blog-section{padding:64px 16px}
 .wd-blog-inner{padding:0}
 .wd-blog-header{margin-bottom:48px}
 .wd-blog-title{}
 .wd-blog-intro{margin-top:32px}
 .wd-blog-intro,.wd-blog-excerpt{font-size:15px;line-height:1.6}
 /* Carrossel nativo: arraste/toque e navegação por Tab, sem biblioteca. */
 .wd-blog-list{display:flex;gap:16px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding-inline:6px;overscroll-behavior-x:contain;padding:6px;margin:0 -6px 48px;scrollbar-width:thin;scrollbar-color:#cbb6ff transparent}
 .wd-blog-item{flex:0 0 92%;scroll-snap-align:start}
 .wd-blog-link{padding:24px 24px 42px;gap:32px 12px;grid-template-columns:minmax(0,1fr) 42px}
 .wd-blog-article-title{font-size:28px}
 .wd-blog-arrow{width:42px;height:42px}
 .wd-blog-meta{font-size:12px}
}
@media (prefers-reduced-motion:reduce){
 .wd-blog-item,.wd-blog-link::before,.wd-blog-cta{transition:none}
 .wd-blog-list{scroll-behavior:auto;scroll-snap-type:none}
 .wd-statement-2-line{--wd-from:#efe7ff!important;--wd-to:#f5c3d8!important}
}
</style>

<script>
(() => {
  const title = document.getElementById('wd-statement-2-title');
  if (!title || title.dataset.wdInitialized) return;
  title.dataset.wdInitialized = 'true';
  const text = title.getAttribute('aria-label');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const measure = document.createElement('canvas').getContext('2d');
  const clamp = value => Math.max(0, Math.min(1, value));
  const mix = (a, b, p) => `rgb(${a.map((v,i) => Math.round(v+(b[i]-v)*p)).join(',')})`;
  let frame = 0;

  function splitLines() {
    if (!measure || !title.clientWidth) return;
    const css = getComputedStyle(title);
    measure.font = `${css.fontWeight} ${css.fontSize} ${css.fontFamily}`;
    const spacing = parseFloat(css.letterSpacing) || 0;
    const widthOf = s => measure.measureText(s).width + spacing * Math.max(0,s.length-1);
    const words = text.split(/\s+/), lines = [];
    let line = '';
    words.forEach(word => {
      const next = line ? `${line} ${word}` : word;
      if (line && widthOf(next) > title.clientWidth) { lines.push(line); line = word; }
      else line = next;
    });
    if (line) lines.push(line);
    // Mesmo número de linhas, com comprimentos equilibrados.
    const target = widthOf(text)/lines.length, memo = new Map();
    function balance(start, count) {
      if (!count) return start === words.length ? {cost:0,lines:[]} : null;
      const key = `${start}:${count}`;
      if (memo.has(key)) return memo.get(key);
      let best = null;
      for (let end=start+1; end<=words.length-count+1; end++) {
        const part = words.slice(start,end).join(' '), width = widthOf(part);
        if (width > title.clientWidth) break;
        const next = balance(end,count-1);
        if (!next) continue;
        const cost = (width-target)**2 + next.cost;
        if (!best || cost < best.cost) best = {cost,lines:[part,...next.lines]};
      }
      memo.set(key,best);
      return best;
    }
    const balanced = balance(0,lines.length);
    const fragment = document.createDocumentFragment();
    (balanced?.lines || lines).forEach((part,i,array) => {
      const span = document.createElement('span');
      span.className = 'wd-statement-2-line';
      span.setAttribute('aria-hidden','true');
      span.textContent = part + (i < array.length-1 ? ' ' : '');
      fragment.append(span);
    });
    title.replaceChildren(fragment);
    update();
  }

  function update() {
    frame = 0;
    const rect = title.getBoundingClientRect(), lines = [...title.children];
    // Igual à frase anterior: scrub top 60% → bottom 60%, stagger 0.3.
    const progress = reduced.matches ? 1 : clamp((innerHeight*.6-rect.top)/Math.max(1,rect.height));
    const duration = 1 + .3 * Math.max(0,lines.length-1);
    lines.forEach((line,i) => {
      const p = clamp(progress*duration-i*.3);
      line.style.setProperty('--wd-from',mix([96,37,225],[239,231,255],p));
      line.style.setProperty('--wd-to',mix([203,182,255],[245,195,216],p));
    });
  }
  function request() { if (!frame) frame = requestAnimationFrame(update); }
  addEventListener('scroll',request,{passive:true});
  addEventListener('resize',splitLines,{passive:true});
  reduced.addEventListener('change',request);
  document.fonts.ready.then(splitLines);
  splitLines();
})();
</script>

<section id="wd-trust" aria-labelledby="wd-trust-title"><div class="wd-trust-panel"><header class="wd-trust-header"><p class="wd-trust-eyebrow wd-uptitle">Confiança</p><h2 class="wd-trust-title wd-section-title" id="wd-trust-title">O que nossos clientes dizem</h2></header><div class="wd-trust-controls"><button type="button" class="wd-trust-control" data-wd-trust-prev aria-label="Depoimento anterior" aria-controls="wd-trust-grid">←</button><button type="button" class="wd-trust-control" data-wd-trust-next aria-label="Próximo depoimento" aria-controls="wd-trust-grid">→</button></div><ul class="wd-trust-grid" id="wd-trust-grid" aria-label="Depoimentos de clientes"><li class="wd-trust-card" tabindex="0"><blockquote class="wd-trust-quote">O time da Work Digital sempre foram excelentes em prazo e soluções para nossos projetos. A Vania, mais do que uma parceira, sem dúvidas, é uma consultora em tecnologia e que tem foco no problema de negócio e não somente na solução ou na ferramenta.</blockquote><div class="wd-trust-attribution"><p class="wd-trust-person">Gustavo Franco<span>Bacio di Latte</span></p></div></li><li class="wd-trust-card" tabindex="0"><blockquote class="wd-trust-quote">A Work Digital nos foi indicada pelo nosso time de marketing, e desde as primeiras conversas, tivemos uma aula de como funcionaria nossa identidade na Web. Após o desenvolvimento do site, nosso setor comercial e a nossa imagem na web mudou, ficamos muito felizes com o resultado e hoje podemos falar com todas a letras o quanto ficamos satisfeito.</blockquote><div class="wd-trust-attribution"><p class="wd-trust-person">Leandro Morales<span>STWBrasil</span></p></div></li><li class="wd-trust-card" tabindex="0"><blockquote class="wd-trust-quote">A Work Digital foi muito comprometida. Fomos atendidos prontamente em todas as escolhas e mudanças durante o processo do trabalho. Sempre muito profissional, tudo foi entregue dentro do prazo. A empresa se envolveu no projeto, tornando o trabalho mais personalizado possível. Recomendo e trabalharei com eles novamente.</blockquote><div class="wd-trust-attribution"><p class="wd-trust-person">Sueli Haro<span>Fiamm Latin America</span></p></div></li></ul><div class="wd-trust-marquee" aria-label="Clientes da Work Digital"><div class="wd-trust-track"><ul class="wd-trust-logo-group"><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/dcef6897584c.png" alt="Bacio di Latte" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/a39c1162e883.png" alt="Dasa" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/679f93e77513.png" alt="Confederação Brasileira de Paraquedismo" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/5895b1a097a9.png" alt="Fiamm Latin America" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/ff67f0cc4bcd.png" alt="Linea Alimentos" decoding="async" loading="eager"></li><li class="wd-trust-logo-item wd-trust-logo-repeat" aria-hidden="true"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/dcef6897584c.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item wd-trust-logo-repeat" aria-hidden="true"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/a39c1162e883.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item wd-trust-logo-repeat" aria-hidden="true"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/679f93e77513.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item wd-trust-logo-repeat" aria-hidden="true"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/5895b1a097a9.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item wd-trust-logo-repeat" aria-hidden="true"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/ff67f0cc4bcd.png" alt="" decoding="async" loading="eager"></li></ul><ul class="wd-trust-logo-group" aria-hidden="true"><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/dcef6897584c.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/a39c1162e883.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/679f93e77513.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/5895b1a097a9.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/ff67f0cc4bcd.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/dcef6897584c.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/a39c1162e883.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/679f93e77513.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/5895b1a097a9.png" alt="" decoding="async" loading="eager"></li><li class="wd-trust-logo-item"><img class="wd-trust-logo" src="<?php echo WD_URI; ?>/img/inline/ff67f0cc4bcd.png" alt="" decoding="async" loading="eager"></li></ul></div></div></div></section>
<script>
(()=>{
 const root=document.getElementById('wd-trust');
 if(!root||root.dataset.initialized)return;
 root.dataset.initialized='true';
 const LOGO_SPEED=11.25; // pixels per second, measured on the Auros partner marquee.
 const track=root.querySelector('.wd-trust-track');
 const marquee=root.querySelector('.wd-trust-marquee');
 const group=root.querySelector('.wd-trust-logo-group');
 const grid=root.querySelector('.wd-trust-grid');
 const cards=[...root.querySelectorAll('.wd-trust-card')];
 const previous=root.querySelector('[data-wd-trust-prev]');
 const next=root.querySelector('[data-wd-trust-next]');
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let inView=false;
 function motion(){track.style.animationPlayState=!reduced.matches&&inView&&!document.hidden?'running':'paused';}
 function resize(){track.style.setProperty('--wd-trust-duration',`${group.getBoundingClientRect().width/LOGO_SPEED}s`);navigation();}
 function navigation(){const max=grid.scrollWidth-grid.clientWidth;previous.disabled=grid.scrollLeft<=2;next.disabled=grid.scrollLeft>=max-2;}
 function move(direction){
  const current=cards.reduce((best,card,i)=>Math.abs(card.offsetLeft-grid.offsetLeft-grid.scrollLeft)<Math.abs(cards[best].offsetLeft-grid.offsetLeft-grid.scrollLeft)?i:best,0);
  const target=cards[Math.max(0,Math.min(cards.length-1,current+direction))];
  grid.scrollTo({left:target.offsetLeft-cards[0].offsetLeft,behavior:reduced.matches?'instant':'smooth'});
 }
 previous.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));
 grid.addEventListener('scroll',navigation,{passive:true});
 grid.addEventListener('keydown',event=>{if(event.key==='ArrowRight'||event.key==='ArrowLeft'){event.preventDefault();move(event.key==='ArrowRight'?1:-1);}});
 if('IntersectionObserver'in window)new IntersectionObserver(entries=>{inView=entries[0].isIntersecting;motion();},{threshold:0}).observe(marquee);
 else {inView=true;motion();}
 if('ResizeObserver'in window)new ResizeObserver(resize).observe(group);
 window.addEventListener('resize',resize,{passive:true});
 reduced.addEventListener('change',()=>{resize();motion();});
 document.addEventListener('visibilitychange',motion);
 resize();motion();
})();
</script>

<script>
(()=>{
 const root=document.getElementById('wd-transformacao');
 if(!root||root.dataset.wdInitialized)return;
 root.dataset.wdInitialized='true';
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const titles=[document.getElementById('wd-statement-title'),root.querySelector('.wd-transformacao-closing-text')].filter(Boolean);
 const measurement=document.createElement('canvas').getContext('2d');
 const originals=titles.map(el=>el.getAttribute('aria-label'));
 const clamp=x=>Math.min(1,Math.max(0,x));
 const color=(a,b,p)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*p)).join(',')})`;
 let queued=false;
 function split(el,text){
  const twoLines=el.id==='wd-statement-title';
  if(twoLines)el.style.fontSize='';
  const css=getComputedStyle(el),width=el.clientWidth;
  if(!measurement||width<=0)return;
  measurement.font=`${css.fontWeight} ${css.fontSize} ${css.fontFamily}`;
  let spacing=parseFloat(css.letterSpacing)||0;
  const measure=text=>measurement.measureText(text).width+spacing*Math.max(0,text.length-1);
  const lines=[];let line='';
  for(const word of text.split(/\s+/)){
   const candidate=line?`${line} ${word}`:word;
   if(line&&measure(candidate)>width){lines.push(line);line=word;}else line=candidate;
  }
  if(line)lines.push(line);
  if(twoLines && innerWidth>991){
   lines.splice(0,lines.length,'Onde você está','quando seu cliente','NÃO procura por você?');
  }
  const fragment=document.createDocumentFragment();
  lines.forEach((text,i)=>{
   const span=document.createElement('span');span.className=el.id==='wd-statement-title'?'wd-statement-line':'wd-transformacao-line';span.setAttribute('aria-hidden','true');
   const words=text.split(/(NÃO)/);
   words.forEach(word=>{
    if(word==='NÃO'){const strong=document.createElement('strong');strong.className='wd-statement-emphasis';strong.textContent=word;span.append(strong);}else span.append(document.createTextNode(word));
   });
   if(i<lines.length-1)span.append(document.createTextNode(' '));
   fragment.append(span);
  });
  el.replaceChildren(fragment);
 }
 function update(){
  queued=false;
  titles.forEach(el=>{
   const rect=el.getBoundingClientRect(),lines=[...el.children];
   // Auros: top 60% -> bottom 60%, scrubbed color, 0.3 stagger.
   const progress=reduced.matches?1:clamp((innerHeight*.6-rect.top)/Math.max(1,rect.height));
   const duration=1+.3*Math.max(0,lines.length-1);
   lines.forEach((line,i)=>{
    const p=clamp(progress*duration-i*.3);
    line.style.setProperty('--wd-line-from',color([96,37,225],[239,231,255],p));
    line.style.setProperty('--wd-line-to',color([203,182,255],[245,195,216],p));
   });
  });
 }
 function request(){if(!queued){queued=true;requestAnimationFrame(update);}}
 function resize(){titles.forEach((el,i)=>split(el,originals[i]));request();}
 addEventListener('scroll',request,{passive:true});
 addEventListener('resize',resize,{passive:true});
 reduced.addEventListener('change',request);
 document.fonts.ready.then(resize);resize();

})();
</script>

</main>

<script>
// Anchor the particle viewport below the portfolio CTA, including after font loading.
(()=>{
 const hero=document.querySelector('.hero-sticky'),cta=document.querySelector('.hero-cta'),wrap=document.querySelector('.canvas-wrap');
 function place(){
  const mobile=innerWidth<=760,gap=mobile?8:12;
  const height=innerHeight*1.7;
  // Overlap only the transparent canvas margins with the adjacent sections.
  // Preserve the canvas dimensions, particle scale and simulation unchanged.
  const trimTop=height*(mobile?.33:.23);
  const trimBottom=height*(mobile?.35:.25);
  const top=cta.getBoundingClientRect().bottom-hero.getBoundingClientRect().top+gap-trimTop;
  wrap.style.top=`${top}px`;wrap.style.height=`${height}px`;
  document.querySelector('.intro').style.minHeight=`${top+height-trimBottom+(mobile?10:12)}px`;
 }

 new ResizeObserver(place).observe(document.querySelector('.intro-block'));
 addEventListener('resize',place,{passive:true});
 document.fonts.ready.then(place);place();
})();

// Matches the reference's geometry: start "top 90%", end "bottom top".
// Typography motion stays independent of WebGL / CDN availability.
(()=>{
 const section=document.getElementById('statement');
 const lines=[...section.querySelectorAll('.statement-line > span')];
 const copy=document.querySelector('.payoff-copy');
 const colorLines=[...copy.children];
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 const clamp=x=>Math.min(1,Math.max(0,x));
 const blend=(a,b,p)=>`rgb(${a.map((v,i)=>Math.round(v+(b[i]-v)*p)).join(',')})`;
 let queued=false;
 function update(){
  queued=false;
  if(reduced.matches){lines.forEach(el=>el.style.transform='none');return;}
  const vw=document.documentElement.clientWidth,vh=innerHeight;
  const rect=section.getBoundingClientRect();
  const progress=clamp((vh*.9-rect.top)/(vh*.9+rect.height));
  lines.forEach((el,i)=>{
   const w=el.offsetWidth;
   const edge=Math.max(16,vw-w-16);
   const from=i===0?edge:16;
   const to=i===0?16:edge;
   el.style.transform=`translate3d(${from+(to-from)*progress}px,0,0)`;
  });
  const cr=copy.getBoundingClientRect();
  const p=clamp((vh*.6-cr.top)/cr.height);
  colorLines.forEach((el,i)=>{
   const t=clamp(p*1.6-i*.3);
   el.style.setProperty('--from',blend([96,37,225],[246,246,248],t));
   el.style.setProperty('--to',blend([4,205,143],[150,72,253],t));
  });
 }
 function request(){if(!queued){queued=true;requestAnimationFrame(update);}}
 addEventListener('scroll',request,{passive:true});
 addEventListener('resize',request,{passive:true});
 reduced.addEventListener('change',request);
 document.fonts.ready.then(request);
 update();
})();
</script>

<script>
// Shared timing and size settings for both particle renderers.
const PARTICLE_SPEED = 1; // Reference rate. 0.8 = slower; 1.2 = faster.
const PARTICLE_COUNT = 40960;
const PARTICLE_SIZE = 0.01; // World units, as in the reference.
const PARTICLE_FIXED_STEP = 1 / 60;
const PARTICLE_POINTER_RESPONSE = -60 * Math.log(1 - 0.07);
// Compatible renderer retains the supplied artwork; GPU uses the fluid solver.
(()=>{
 const art=document.querySelector('.particle-art'),image=art.querySelector('img');
 if(window.WD_LITE){art.remove();return;}
 const canvas=document.createElement('canvas');canvas.setAttribute('aria-hidden','true');art.append(canvas);
 const ctx=canvas.getContext('2d',{alpha:true});if(!ctx)return;
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');
 let particles=[],width=1,height=1,raf=0,last=0,time=0,visible=true,ready=false;
 let mx=0,my=0,tx=0,ty=0,pointerActive=false;
 let randomSeed=921;const random=()=>{randomSeed=(Math.imul(randomSeed,1664525)+1013904223)>>>0;return randomSeed/4294967296;};
 function resize(){const r=art.getBoundingClientRect();width=r.width;height=r.height;const d=Math.min(devicePixelRatio||1,window.WD_LITE?1:1.5);canvas.width=Math.round(width*d);canvas.height=Math.round(height*d);ctx.setTransform(d,0,0,d,0,0);start();}
 function setup(){
  if(ready)return;
  const source=document.createElement('canvas');source.width=image.naturalWidth;source.height=image.naturalHeight;
  const g=source.getContext('2d',{willReadFrequently:true});g.drawImage(image,0,0);
  const pixels=g.getImageData(0,0,source.width,source.height).data;
  const candidates=[];
  for(let y=330;y<980;y+=2)for(let x=480;x<1100;x+=2){
   const i=(y*source.width+x)*4,brightness=Math.max(pixels[i],pixels[i+1],pixels[i+2]);
   if(brightness<48)continue;
   const px=(x-785)/302,py=(y-650)/335,rr=px*px+py*py;
   if(rr>1.18)continue;
   candidates.push({sx:x,sy:y,x:px,y:py,z:Math.sqrt(Math.max(.015,1-Math.min(.985,rr))),brightness});
  }
  const count=Math.round(PARTICLE_COUNT*(window.WD_LITE?.2:.4));
  // Samples retain the real glyph fragments and luminous variation of the supplied art.
  for(let i=0;i<count;i++){
   const p=candidates[Math.floor(random()*candidates.length)];
   particles.push({...p,z:p.z*(random()<.55?1:-1),phase:random()*6.283,size:(.75+random()*.5)*(window.WD_LITE?2.1:1.5)});
  }
  ready=true;art.classList.add('has-live-particles');resize();start();
 }
 function draw(stamp){
  raf=0;if(!ready||!visible||document.hidden||art.classList.contains("has-native-particles"))return;
  if(window.WD_LITE&&last&&stamp-last<30&&!reduced.matches){raf=requestAnimationFrame(draw);return;}
  const dt=last?Math.max(0,(stamp-last)/1000):0;last=stamp;
  if(!reduced.matches)time+=dt*PARTICLE_SPEED;
  const smoothing=1-Math.exp(-PARTICLE_POINTER_RESPONSE*dt);
  mx+=(tx-mx)*smoothing;my+=(ty-my)*smoothing;
  ctx.clearRect(0,0,width,height);
  const radius=Math.min(width*.36,height*.225),cx=width*.5,cy=height*.5;
  // One-second opening sweep, then ambient movement after ten seconds.
  const ambient=Math.max(0,time-10);
  const cycle=Math.floor(ambient/6.5);
  const progress=time<1?time:time<10?1:Math.min(1,(ambient%6.5)/6);
  const path=(time<10?7:[7,2,8,3,6,1,9,4][cycle%8])*Math.PI/5;
  const ease=progress<.5?2*progress*progress:1-Math.pow(-2*progress+2,2)/2;
  const travel=-.5+1.5*ease,ax=Math.cos(path)*travel,ay=Math.sin(path)*travel;
  const visibleCount=particles.length;
  for(let particleIndex=0;particleIndex<visibleCount;particleIndex++){
   const p=particles[particleIndex];
   let x=p.x,y=p.y,z=p.z;
   // A travelling pressure field advects independent points; the cloud does not rotate as a rigid object.
   const distance=(x-ax)*(x-ax)+(y-ay)*(y-ay);
   const pressure=Math.exp(-distance*3.8);
   const ripple=Math.sin(x*4+y*3+z*2-time*.7);
   x+=Math.cos(path)*pressure*.19+Math.sin(y*5+z*3-time*.48)*.035;
   y+=Math.sin(path)*pressure*.19+Math.cos(x*4-z*4+time*.42)*.035;
   z+=pressure*.13*ripple;
   const perspective=4.5/(4.5-z),front=(z+1)*.5;
   let dx=cx+x*radius*perspective,dy=cy+y*radius*1.08*perspective;
   if(pointerActive&&!reduced.matches){const vx=dx-mx,vy=dy-my,d=Math.sqrt(vx*vx+vy*vy);const force=Math.exp(-d*d/(radius*radius*.04))*12;dx+=vx/(d+1)*force;dy+=vy/(d+1)*force;}
   const size=(radius*PARTICLE_SIZE/.4)*p.size*perspective;
   dx=Math.max(size/2,Math.min(width-size/2,dx));
   dy=Math.max(size/2,Math.min(height-size/2,dy));
   ctx.globalAlpha=.26+.64*front;
   ctx.drawImage(image,p.sx-3,p.sy-3,6,6,dx-size/2,dy-size/2,size,size);
  }
  ctx.globalAlpha=1;
  if(!reduced.matches)raf=requestAnimationFrame(draw);
 }
 art.addEventListener("nativeparticlesready",()=>{cancelAnimationFrame(raf);raf=0;});
 art.addEventListener("nativeparticlesfailed",()=>start());
 function start(){if(!raf&&ready&&visible&&!document.hidden){last=0;raf=requestAnimationFrame(draw);}}
 new IntersectionObserver(es=>{visible=es[0].isIntersecting;if(visible)start();else{cancelAnimationFrame(raf);raf=0;}},{rootMargin:'100px'}).observe(art);
 new ResizeObserver(resize).observe(art);
 addEventListener('resize',resize,{passive:true});
 addEventListener('pointermove',e=>{const r=art.getBoundingClientRect();tx=e.clientX-r.left;ty=e.clientY-r.top;pointerActive=true;},{passive:true});
 document.addEventListener('pointerleave',()=>{pointerActive=false;});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(raf);raf=0;}else start();});
 reduced.addEventListener('change',()=>{cancelAnimationFrame(raf);raf=0;start();});
 if(image.complete&&image.naturalWidth)setup();else image.addEventListener('load',setup,{once:true});
})();

</script>
<script>(async()=>{try{if(!window.WD_LITE&&navigator.gpu&&!matchMedia("(prefers-reduced-motion: reduce)").matches&&await navigator.gpu.requestAdapter()){const s=document.createElement("script");s.type="module";s.src="<?php echo WD_URI; ?>/app.js";document.head.append(s);}}catch(e){}})();</script>
<script src="<?php echo WD_URI; ?>/footer.js?v=20261003-footer-one-line" defer></script>
<script src="<?php echo WD_URI; ?>/wd-revision.js?v=20261003-contact-minimal" defer></script>
<style>
/* Cursor personalizado (igual ao das páginas internas) */
.wd-cursor{position:fixed;left:0;top:0;z-index:2147483000;pointer-events:none;width:12px;height:12px;margin:-6px 0 0 -6px;border-radius:50%;background:#F2EEF8;box-shadow:0 0 0 1px rgba(18,19,22,.35);display:grid;place-items:center;
  transition:width .4s cubic-bezier(.22,1,.36,1),height .4s cubic-bezier(.22,1,.36,1),margin .4s cubic-bezier(.22,1,.36,1),background .3s}
.wd-cursor b{font:500 11px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#fff;opacity:0;transition:opacity .2s;white-space:nowrap}
.wd-cursor.link{width:40px;height:40px;margin:-20px 0 0 -20px}
.wd-cursor.big{width:96px;height:96px;margin:-48px 0 0 -48px;background:#6025E1;mix-blend-mode:normal}
.wd-cursor.big b{opacity:1}
@media not all and (pointer: coarse){.has-wd-cursor,.has-wd-cursor a,.has-wd-cursor button{cursor:none}}
</style>
<div class="wd-cursor" id="wdCursor" aria-hidden="true" hidden><b></b></div>
<script>
(function(){
  if(!matchMedia('not all and (pointer: coarse)').matches||matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const c=document.getElementById('wdCursor'), lb=c.querySelector('b'); c.hidden=false; document.body.classList.add('has-wd-cursor');
  const LABELS=[['.wd-works-card','Ver case'],['.wd-blog-link','Ler']];
  let mx=innerWidth/2,my=innerHeight/2,x=mx,y=my;
  addEventListener('pointermove',e=>{mx=e.clientX;my=e.clientY;c.style.transform=`translate(${mx}px,${my}px)`;},{passive:true});
  document.addEventListener('mouseover',e=>{
    let label=null; for(const [sel,txt] of LABELS){ if(e.target.closest(sel)){label=txt;break;} }
    c.classList.toggle('big',!!label);document.documentElement.classList.toggle('wd-big',!!label); if(label) lb.textContent=label;
    c.classList.toggle('link',!label && !!e.target.closest('a,button,input,textarea'));
  });
  document.addEventListener('mouseleave',()=>c.classList.remove('big','link'));
  
})();
</script>
<script>
(function(){
  try{if(!location.hash){history.scrollRestoration='manual';scrollTo(0,0);}}catch(e){}
  document.querySelectorAll('a[href="#hero"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();
    const top=()=>scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});top();
    try{history.replaceState(null,'',location.pathname+location.search);}catch(x){}}));
})();
</script>
<script>

// Vale para qualquer computador com mouse (inclusive notebooks com tela de toque).
// A animação só começa por ação do visitante (passar o mouse), por isso não depende do "movimento reduzido" do sistema.
const WD_CAN_PLAY = !matchMedia("(pointer: coarse)").matches;
const wdMouse = e => !e || e.pointerType !== "touch";
function wdThumb(box, slug, w, h) {
  let video = null, anim = null, loaded = false, failed = false, want = false;
  const poster = () => `<img class="vm-poster" src="${wdT(slug,"webp")}" width="${w}" height="${h}" alt="" loading="lazy" decoding="async"><i class="vm-load" aria-hidden="true"></i>`;
  box.innerHTML = poster();
  function useAnim() {
    if (failed) return; failed = true;
    if (video) { video.remove(); video = null; }
    anim = document.createElement("img"); anim.className = "vm-anim"; anim.alt = ""; anim.setAttribute("aria-hidden", "true"); anim.decoding = "async";
    anim.addEventListener("load", () => { if (want) box.classList.add("vm-on"); box.classList.remove("vm-wait"); });
    box.appendChild(anim);
    if (want) anim.src = `${wdT(slug,"anim.webp")}`;
  }
  function load(eager) {
    if (loaded || !WD_CAN_PLAY) return; loaded = true;
    video = document.createElement("video");
    video.className = "vm-video"; video.muted = true; video.loop = true; video.playsInline = true; video.preload = eager ? "auto" : "metadata";
    video.setAttribute("muted", ""); video.setAttribute("playsinline", ""); video.setAttribute("aria-hidden", "true");
    video.innerHTML = `<source src="${wdT(slug,"webm")}" type="video/webm"><source src="${wdT(slug,"mp")}4" type="video/mp4">`;
    const last = video.lastElementChild;
    last.addEventListener("error", useAnim); video.addEventListener("error", useAnim);
    video.addEventListener("playing", () => { if (want) box.classList.add("vm-on"); box.classList.remove("vm-wait"); });
    box.appendChild(video);
  }
  if (WD_CAN_PLAY && "IntersectionObserver" in window) {
    const io = new IntersectionObserver(es => { if (es[0].isIntersecting) { load(false); io.disconnect(); } }, { rootMargin: "300px" });
    io.observe(box);
  }
  const api = {
    play() {
      if (!WD_CAN_PLAY) return; want = true; load(true);
      if (failed) { box.classList.add("vm-wait"); if (anim.src) { anim.src = ""; } anim.src = `${wdT(slug,"anim.webp")}`; if (anim.complete && anim.naturalWidth) box.classList.add("vm-on"); return; }
      box.classList.add("vm-wait"); video.preload = "auto";
      const p = video.play(); if (p) p.catch(e => { if (e && e.name === "NotSupportedError") { useAnim(); api.play(); } });
    },
    stop() { want = false; box.classList.remove("vm-on", "vm-wait"); if (video) { video.pause(); try { video.currentTime = 0; } catch (e) {} } },
    set(nslug, nw, nh) { api.stop(); slug = nslug; w = nw; h = nh; loaded = false; failed = false; video = null; anim = null; box.innerHTML = poster(); }
  };
  return api;
}
function wdTilt(el, max) {
  if (!WD_CAN_PLAY) return;
  max = max || 5; let raf = 0, x = .5, y = .5;
  const glare = document.createElement("span"); glare.className = "wd-glare"; glare.setAttribute("aria-hidden", "true"); el.appendChild(glare);
  const apply = () => { raf = 0; el.style.setProperty("--mx", (x * 100).toFixed(1) + "%"); el.style.setProperty("--my", (y * 100).toFixed(1) + "%");
    el.style.transform = `perspective(1100px) rotateX(${((.5 - y) * max).toFixed(2)}deg) rotateY(${((x - .5) * max).toFixed(2)}deg) scale(1.012)`; };
  el.addEventListener("pointerenter", e => { if (wdMouse(e)) el.classList.add("wd-tilting"); });
  el.addEventListener("pointermove", e => { if (!wdMouse(e)) return; const r = el.getBoundingClientRect(); x = (e.clientX - r.left) / r.width; y = (e.clientY - r.top) / r.height; if (!raf) raf = requestAnimationFrame(apply); });
  el.addEventListener("pointerleave", () => { cancelAnimationFrame(raf); raf = 0; el.classList.remove("wd-tilting"); el.style.transform = ""; });
}
document.querySelectorAll(".wd-works-card").forEach(card => {
  const m = card.querySelector(".wd-works-media"); if (!m) return;
  const ctl = wdThumb(m.querySelector(".vm"), m.dataset.thumb, +m.dataset.w, +m.dataset.h);
  card.classList.add("wd-tilt-host"); wdTilt(card, 5);
  card.addEventListener("pointerenter", e => { if (wdMouse(e)) ctl.play(); }); card.addEventListener("pointerleave", ctl.stop);
  card.addEventListener("focus", ctl.play); card.addEventListener("blur", ctl.stop);
});
</script>
<?php wp_footer(); ?>
</body>
</html>
