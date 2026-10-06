<?php
/* Dados usados pelos modelos: cases, thumbs, artigos e datas */
if (!defined('ABSPATH')) exit;

const WD_BLOCKS = [ // arquivo, classes do bloco, largura, altura, tem legenda, carrega já
    '01' => ['01-home', 'h74 w169', 2400, 1350, true, true],
    '02' => ['02-key-visual', 'full w34', 1500, 2000, false, true],
    '03' => ['03-detalhe', 'h74 w11', 1600, 1600, true, false],
    '04' => ['04-pagina', 'h74 w169', 2400, 1350, true, false],
    '05' => ['05-mobile', 'full w45', 1600, 2000, false, false],
    '06' => ['06-conceito', 'full w34', 1500, 2000, false, false],
    '07' => ['07-paleta', 'h74 w34', 1500, 2000, false, false],
];

function wd_meta($id, $key) { return get_post_meta($id, 'wd_' . $key, true); }
function wd_lines($text) { return array_values(array_filter(array_map('trim', preg_split('/\r?\n/', (string) $text)))); }
function wd_att_url($id) { return $id ? wp_get_attachment_url((int) $id) : ''; }
function wd_att_dims($id) {
    $m = $id ? wp_get_attachment_metadata((int) $id) : null;
    return [(int) ($m['width'] ?? 0), (int) ($m['height'] ?? 0)];
}

function wd_cases() {
    static $all = null;
    if ($all === null) $all = get_posts(['post_type' => 'case', 'numberposts' => -1, 'orderby' => ['menu_order' => 'ASC', 'date' => 'ASC'], 'post_status' => 'publish']);
    return $all;
}

// próximo case na ordem (o último volta para o primeiro)
function wd_next_case($post) {
    $all = wd_cases();
    if (!$all) return null;
    foreach ($all as $i => $c) if ($c->ID === $post->ID) return $all[($i + 1) % count($all)];
    return $all[0];
}

// cards da página de Cases (mesmo formato de dados do layout original)
function wd_projects() {
    $size = ['grande' => 'large', 'medio' => 'medium', 'pequeno' => 'small'];
    $out = []; $medium = 0;
    foreach (wd_cases() as $c) {
        $s = $size[wd_meta($c->ID, 'formato')] ?? 'small';
        [$w, $h] = wd_att_dims(wd_meta($c->ID, 'thumb_webp'));
        if (!$w) { $w = 1200; $h = 1500; }
        $out[] = [
            'slug' => $c->post_name, 'client' => get_the_title($c), 'title' => (string) wd_meta($c->ID, 'frase'),
            'services' => wd_lines(wd_meta($c->ID, 'servicos')), 'size' => $s,
            'offset' => $s === 'medium' ? (bool) ($medium++ % 2) : false, // os cards médios alternam a posição
            'w' => $w, 'h' => $h, 'url' => get_permalink($c), 'link' => (string) wd_meta($c->ID, 'link'),
        ];
    }
    return $out;
}

// thumbs animadas: endereço de cada arquivo (imagem, vídeos e versão animada de reserva)
function wd_thumbs_map() {
    $map = [];
    foreach (wd_cases() as $c) {
        foreach (['' => 'thumb', '-home' => 'home'] as $suf => $pre) {
            $files = [];
            foreach (['webp' => 'webp', 'mp4' => 'mp4', 'webm' => 'webm', 'anim.webp' => 'anim'] as $ext => $k) {
                $u = wd_att_url(wd_meta($c->ID, $pre . '_' . $k));
                if ($u) $files[$ext] = $u;
            }
            if ($files) $map[$c->post_name . $suf] = $files;
        }
    }
    return $map;
}

// cases da seção Works da home (posições 1 a 4)
function wd_home_cases() {
    $list = [];
    foreach (wd_cases() as $c) {
        $slot = (int) wd_meta($c->ID, 'home_slot');
        if ($slot >= 1 && $slot <= 4 && !isset($list[$slot])) $list[$slot] = $c;
    }
    ksort($list);
    return array_values($list);
}

// datas em português
function wd_month($n, $long = false) {
    $s = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'];
    $l = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
    return ($long ? $l : $s)[$n - 1];
}
function wd_date($post, $long = false) {
    $t = get_post_timestamp($post);
    return (int) wp_date('j', $t) . ($long ? ' de ' : ' ') . wd_month((int) wp_date('n', $t), $long) . ($long ? ' de ' : ' ') . wp_date('Y', $t);
}
function wd_reading_time($post) {
    $words = count(preg_split('/\s+/u', trim(wp_strip_all_tags(get_post_field('post_content', $post))), -1, PREG_SPLIT_NO_EMPTY));
    return max(1, (int) round($words / 200));
}
function wd_post_cat($post) {
    $c = get_the_category($post->ID);
    return $c ? $c[0] : null;
}
function wd_post_img($post, $size = 'wd-wide') {
    $id = get_post_thumbnail_id($post);
    return $id ? (wp_get_attachment_image_url($id, $size) ?: wp_get_attachment_url($id)) : WD_URI . '/img/servico-blog.jpg';
}
function wd_post_alt($post) {
    $id = get_post_thumbnail_id($post);
    return $id ? (string) get_post_meta($id, '_wp_attachment_image_alt', true) : '';
}
function wd_dek($post) {
    $d = get_post_meta($post->ID, 'wd_dek', true);
    return $d ?: get_the_excerpt($post);
}

// dados da listagem do blog (o filtro, a busca e a paginação são feitos na página)
function wd_blog_data() {
    $posts = get_posts(['numberposts' => -1, 'post_status' => 'publish']);
    $img = []; $list = [];
    foreach ($posts as $p) {
        $k = 'p' . $p->ID;
        $img[$k] = wd_post_img($p, 'wd-card');
        $cat = wd_post_cat($p);
        $list[] = ['cat' => $cat ? $cat->name : '', 'date' => wd_date($p), 'min' => wd_reading_time($p), 'img' => $k,
                   'title' => get_the_title($p), 'excerpt' => get_the_excerpt($p), 'url' => get_permalink($p)];
    }
    $featured = $list ? array_shift($list) : null;
    $order = ['Criação de sites', 'Lojas virtuais', 'SEO', 'Performance', 'Tráfego', 'Negócios'];
    $have = array_unique(array_merge(array_map(fn($p) => $p['cat'], $list), $featured ? [$featured['cat']] : []));
    $cats = array_merge(['Todos'], array_values(array_intersect($order, $have)), array_values(array_diff($have, $order, [''])));
    return ['img' => $img, 'posts' => $list, 'featured' => $featured, 'cats' => $cats];
}

// artigos relacionados: mesma categoria primeiro, depois os mais recentes
function wd_related($post, $n = 3) {
    $cat = wd_post_cat($post);
    $same = $cat ? get_posts(['numberposts' => $n, 'category' => $cat->term_id, 'exclude' => [$post->ID]]) : [];
    if (count($same) < $n) {
        $more = get_posts(['numberposts' => $n - count($same), 'exclude' => array_merge([$post->ID], wp_list_pluck($same, 'ID'))]);
        $same = array_merge($same, $more);
    }
    return $same;
}
