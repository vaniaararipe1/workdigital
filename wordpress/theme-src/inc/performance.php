<?php
/* Desempenho: conexões antecipadas, sem jQuery no site e vídeos pausados fora da tela */
if (!defined('ABSPATH')) exit;

add_action('wp_enqueue_scripts', function () {
    if (!is_admin()) { wp_dequeue_script('jquery'); wp_deregister_script('jquery-migrate'); }
}, 100);
add_filter('wp_resource_hints', function ($urls, $rel) {
    if ($rel === 'preconnect') { $urls[] = ['href' => 'https://fonts.gstatic.com', 'crossorigin']; $urls[] = 'https://www.googletagmanager.com'; }
    return $urls;
}, 10, 2);
// vídeos automáticos (não os dos cases, que já se controlam) pausam quando saem da tela e voltam quando entram
add_action('wp_footer', function () { ?>
<script>
(function(){if(!('IntersectionObserver'in window))return;var io=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(v.closest('.case-lb')||v.classList.contains('case-video')||v.classList.contains('vm-video'))return;if(!e.isIntersecting){if(!v.paused){v.dataset.wdAuto=1;v.pause();}}else if(v.dataset.wdAuto&&!(window.wdIsPaused&&wdIsPaused())){delete v.dataset.wdAuto;var p=v.play();p&&p.catch(function(){});}});},{rootMargin:'100px'});
document.querySelectorAll('video[autoplay]').forEach(function(v){io.observe(v);});})();
</script>
<?php }, 60);
