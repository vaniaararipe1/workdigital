<?php
/* Google Tag Manager com Modo de Consentimento (LGPD): nada de análise/anúncios antes do "Aceitar" */
if (!defined('ABSPATH')) exit;

add_action('wp_head', function () {
    if (is_admin()) return; ?>
<script>
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
(function(){var c=null;try{c=localStorage.getItem('wdConsent');}catch(e){}
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',functionality_storage:'granted',security_storage:'granted',wait_for_update:500});
if(c==='all')gtag('consent','update',{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'});})();
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','<?php echo esc_js(WD_GTM); ?>');</script>
<!-- End Google Tag Manager -->
<?php }, 2);

add_action('wp_body_open', function () { ?>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=<?php echo esc_attr(WD_GTM); ?>" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
<?php }, 1);

// aviso de cookies
add_action('wp_footer', function () {
    $privacy = get_privacy_policy_url(); ?>
<div class="wd-consent" id="wdConsent" role="region" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies para entender como o site é usado e melhorar a sua experiência. Você pode aceitar ou recusar os cookies de análise e anúncios.<?php if ($privacy) : ?> <a href="<?php echo esc_url($privacy); ?>">Política de privacidade</a><?php endif; ?></p>
  <div class="b"><button type="button" data-c="essential">Recusar</button><button type="button" data-c="all" class="ok">Aceitar</button></div>
</div>
<style>
.wd-consent{position:fixed;z-index:99990;left:50%;bottom:16px;transform:translateX(-50%);width:min(720px,calc(100% - 32px));display:flex;gap:16px 24px;align-items:center;justify-content:space-between;flex-wrap:wrap;padding:18px 22px;border-radius:20px;background:rgba(18,19,22,.92);color:#F7F6FB;border:1px solid rgba(189,164,255,.3);box-shadow:0 20px 60px -20px rgba(0,0,0,.6);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);font:400 14px/1.55 "Space Grotesk",Arial,sans-serif}
.wd-consent p{margin:0;flex:1 1 320px}.wd-consent a{color:#CBB6FF;text-decoration:underline;text-underline-offset:3px}
.wd-consent .b{display:flex;gap:10px}.wd-consent button{min-height:44px;padding:0 20px;border-radius:999px;border:1px solid rgba(189,164,255,.45);background:transparent;color:#F7F6FB;font:500 13px/1 "Space Grotesk",Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;cursor:pointer}
.wd-consent button.ok{background:#F7F6FB;color:#24123e;border-color:#F7F6FB}.wd-consent button:focus-visible{outline:2px solid #CBB6FF;outline-offset:3px}
</style>
<script>
(function(){var b=document.getElementById('wdConsent');if(!b)return;var c=null;try{c=localStorage.getItem('wdConsent');}catch(e){}
if(!c)b.hidden=false;
b.addEventListener('click',function(e){var t=e.target.closest('button[data-c]');if(!t)return;var v=t.dataset.c;try{localStorage.setItem('wdConsent',v);}catch(x){}
if(v==='all'&&window.gtag)gtag('consent','update',{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'});
window.dataLayer&&dataLayer.push({event:'wd_consent',wd_consent:v});b.hidden=true;});})();
</script>
<?php }, 50);
