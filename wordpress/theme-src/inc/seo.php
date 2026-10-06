<?php
/* SEO: o Yoast cuida de título, descrição, canonical, Open Graph e sitemap. O tema acrescenta os dados
   estruturados próprios (planos e FAQ em Soluções, case como CreativeWork) e um modo básico sem o Yoast. */
if (!defined('ABSPATH')) exit;

function wd_has_yoast() { return defined('WPSEO_VERSION'); }
function wd_ld($obj) { echo '<script type="application/ld+json">' . wp_json_encode($obj, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "</script>\n"; }

// textos de SEO guardados nos campos do Yoast (também usados quando o Yoast não está ativo)
function wd_seo_title($id) { return (string) get_post_meta($id, '_yoast_wpseo_title', true); }
function wd_seo_desc($id) { return (string) get_post_meta($id, '_yoast_wpseo_metadesc', true); }

add_filter('pre_get_document_title', function ($t) {
    if (wd_has_yoast()) return $t;
    $id = is_singular() ? get_queried_object_id() : (is_home() ? (int) get_option('page_for_posts') : 0);
    if (is_front_page()) $id = (int) get_option('page_on_front');
    if (is_post_type_archive('case')) return 'Work Digital - Cases da Work';
    $s = $id ? wd_seo_title($id) : '';
    if ($s) return wp_strip_all_tags(str_replace(['%%sitename%%', '%%sep%%', '%%title%%'], ['Work Digital', '-', get_the_title($id)], $s));
    if (is_singular('post')) return get_the_title() . ' - Work Digital';
    return $t;
});
add_filter('document_title_separator', fn() => '-');

add_action('wp_head', function () {
    if (!wd_has_yoast()) {
        $id = is_singular() ? get_queried_object_id() : 0;
        if (is_front_page()) $id = (int) get_option('page_on_front');
        if (is_home()) $id = (int) get_option('page_for_posts');
        $desc = $id ? (wd_seo_desc($id) ?: (is_singular('post') ? get_the_excerpt($id) : '')) : '';
        if (is_post_type_archive('case')) $desc = 'Cases da Work Digital: sites, portais, lojas virtuais e blogs criados para marcas como Bacio di Latte, Linea Alimentos e CBPq.';
        $url = is_singular() ? get_permalink($id) : (is_post_type_archive('case') ? get_post_type_archive_link('case') : (is_home() ? get_permalink($id) : home_url('/')));
        if ($desc) echo '<meta name="description" content="' . esc_attr($desc) . '">' . "\n";
        echo '<link rel="canonical" href="' . esc_url($url) . '">' . "\n";
        echo '<meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Work Digital"><meta property="og:url" content="' . esc_url($url) . '"><meta property="og:title" content="' . esc_attr(wp_get_document_title()) . '">' . "\n";
        if ($desc) echo '<meta property="og:description" content="' . esc_attr($desc) . '">' . "\n";
        $img = is_singular('post') ? wd_post_img(get_post($id), 'full') : (is_singular('case') ? wd_att_url(wd_meta($id, 'm01')) : WD_URI . '/media/servico-sites.jpg');
        echo '<meta property="og:image" content="' . esc_url($img) . '"><meta name="twitter:card" content="summary_large_image">' . "\n";
    }
    // dados estruturados próprios
    if (is_page('solucoes')) {
        wd_ld(['@context' => 'https://schema.org', '@type' => 'Service', 'name' => 'Criação de sites', 'areaServed' => 'BR',
            'provider' => ['@type' => 'Organization', 'name' => 'Work Digital', 'url' => home_url('/')],
            'hasOfferCatalog' => ['@type' => 'OfferCatalog', 'name' => 'Contrate um site profissional', 'itemListElement' => [
                ['@type' => 'Offer', 'name' => 'Blog de conteúdo', 'price' => '995.00', 'priceCurrency' => 'BRL', 'description' => 'Pagamento único'],
                ['@type' => 'Offer', 'name' => 'Site profissional por assinatura', 'priceCurrency' => 'BRL', 'description' => 'Suporte + hospedagem mensal',
                 'priceSpecification' => ['@type' => 'UnitPriceSpecification', 'price' => '590.00', 'priceCurrency' => 'BRL', 'unitText' => 'MONTH']],
                ['@type' => 'Offer', 'name' => 'Site profissional personalizado', 'description' => 'Sob consulta']]]]);
        if (function_exists('wd_faq')) wd_ld(['@context' => 'https://schema.org', '@type' => 'FAQPage', 'mainEntity' => array_map(fn($q) => ['@type' => 'Question', 'name' => $q[0], 'acceptedAnswer' => ['@type' => 'Answer', 'text' => $q[1]]], wd_faq())]);
    }
    if (is_singular('case')) {
        $id = get_queried_object_id();
        wd_ld(['@context' => 'https://schema.org', '@type' => 'CreativeWork', 'name' => get_the_title($id), 'headline' => wd_seo_title($id) ?: get_the_title($id),
            'description' => wd_seo_desc($id), 'url' => get_permalink($id), 'image' => wd_att_url(wd_meta($id, 'm01')), 'inLanguage' => 'pt-BR',
            'creator' => ['@type' => 'Organization', 'name' => 'Work Digital', 'url' => home_url('/')]]);
    }
}, 20);

// Yoast: o case usa a primeira arte como imagem de compartilhamento quando não há outra
add_filter('wpseo_opengraph_image', function ($img) {
    if (!$img && is_singular('case')) return wd_att_url(wd_meta(get_queried_object_id(), 'm01'));
    return $img;
});
