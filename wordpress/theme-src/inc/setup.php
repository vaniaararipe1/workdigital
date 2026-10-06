<?php
/* Suportes do tema, tipo de conteúdo Cases, imagens e limpeza do <head> */
if (!defined('ABSPATH')) exit;

add_action('after_setup_theme', function () {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'gallery', 'caption', 'style', 'script']);
    add_theme_support('responsive-embeds');
});

// Cases: cada case tem a própria página em /cases/{titulo-do-case}/ (o endereço nasce do título)
add_action('init', function () {
    register_post_type('case', [
        'labels' => [
            'name' => 'Cases', 'singular_name' => 'Case', 'add_new' => 'Adicionar case', 'add_new_item' => 'Adicionar novo case',
            'edit_item' => 'Editar case', 'new_item' => 'Novo case', 'view_item' => 'Ver case', 'search_items' => 'Buscar cases',
            'not_found' => 'Nenhum case encontrado', 'all_items' => 'Todos os cases', 'menu_name' => 'Cases',
        ],
        'public' => true,
        'has_archive' => 'cases',
        'rewrite' => ['slug' => 'cases', 'with_front' => false],
        'menu_icon' => 'dashicons-portfolio',
        'menu_position' => 5,
        'supports' => ['title', 'thumbnail', 'page-attributes', 'revisions'],
        'show_in_rest' => true,
    ]);
});
// ordem dos cases: campo "Ordem" (menu_order), do menor para o maior
add_action('pre_get_posts', function ($q) {
    if (!is_admin() && $q->is_main_query() && $q->is_post_type_archive('case')) {
        $q->set('orderby', ['menu_order' => 'ASC', 'date' => 'ASC']);
        $q->set('posts_per_page', -1);
    }
});

// Imagens: qualidade alta (90), sem reduzir as originais grandes, e versões menores em WebP para telas menores
add_filter('wp_editor_set_quality', fn() => 90);
add_filter('jpeg_quality', fn() => 90);
add_filter('big_image_size_threshold', '__return_false');
add_filter('image_editor_output_format', function ($formats) {
    $formats['image/jpeg'] = 'image/webp';
    $formats['image/png'] = 'image/webp';
    return $formats;
});
add_action('after_setup_theme', function () {
    add_image_size('wd-card', 960, 0);
    add_image_size('wd-wide', 1600, 0);
});
add_filter('upload_mimes', function ($m) { $m['webp'] = 'image/webp'; $m['webm'] = 'video/webm'; $m['svg'] = 'image/svg+xml'; return $m; });

// <head> enxuto: o tema não usa blocos, emojis nem oEmbed
add_action('init', function () {
    remove_action('wp_head', 'print_emoji_detection_script', 7);
    remove_action('wp_print_styles', 'print_emoji_styles');
    remove_action('wp_head', 'wp_generator');
    remove_action('wp_head', 'wlwmanifest_link');
    remove_action('wp_head', 'rsd_link');
    remove_action('wp_head', 'wp_oembed_add_discovery_links');
    remove_action('wp_head', 'wp_shortlink_wp_head');
    remove_action('wp_head', 'rest_output_link_wp_head');
});
add_action('wp_enqueue_scripts', function () {
    foreach (['wp-block-library', 'wp-block-library-theme', 'global-styles', 'classic-theme-styles'] as $h) wp_dequeue_style($h);
}, 100);
add_filter('should_load_separate_core_block_assets', '__return_true');

// Sem comentários no site
add_action('init', function () {
    remove_post_type_support('post', 'comments');
    remove_post_type_support('post', 'trackbacks');
});
add_filter('comments_open', '__return_false', 20);
add_filter('pings_open', '__return_false', 20);

// URL de uma página do site (sempre com barra no fim)
function wd_url($path = '') {
    return home_url('/' . ltrim($path, '/'));
}
