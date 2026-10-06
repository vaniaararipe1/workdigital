<?php
/* Site: folha de estilo das peças novas e endereços das thumbs animadas (home e Cases) */
if (!defined('ABSPATH')) exit;

add_action('wp_enqueue_scripts', function () {
    wp_enqueue_style('wd-theme', WD_URI . '/wd-theme.css', [], WD_VER);
});
add_action('wp_head', function () {
    if (!is_front_page() && !is_post_type_archive('case')) return;
    echo '<script>window.WD_THUMBS=' . wp_json_encode(wd_thumbs_map(), JSON_UNESCAPED_SLASHES) . ';window.wdT=function(s,x){var m=(window.WD_THUMBS||{})[s];return m&&m[x]?m[x]:"";};</script>' . "\n";
}, 3);
