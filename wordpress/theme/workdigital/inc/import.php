<?php
/* Importação do conteúdo do site (cases, artigos, páginas e configurações).
   Usada pelo envio remoto (rotas /wp-json/wd/v1/import/*, só para administradores) e pelo importar.php (WP-CLI).
   Tudo pode ser repetido: o que já existe é atualizado, nada é duplicado. */
if (!defined('ABSPATH')) exit;

function wd_imp_includes() {
    require_once ABSPATH . 'wp-admin/includes/media.php';
    require_once ABSPATH . 'wp-admin/includes/file.php';
    require_once ABSPATH . 'wp-admin/includes/image.php';
    require_once ABSPATH . 'wp-admin/includes/misc.php';
}

// anexo já importado com o mesmo arquivo de origem e o mesmo conteúdo
function wd_imp_find_media($src, $hash = '') {
    $found = get_posts(['post_type' => 'attachment', 'post_status' => 'inherit', 'numberposts' => 1, 'fields' => 'ids', 'meta_query' => [['key' => '_wd_src', 'value' => $src]]]);
    if (!$found) return 0;
    if ($hash !== '' && get_post_meta($found[0], '_wd_hash', true) !== $hash) return -$found[0]; // existe, mas o arquivo mudou
    return $found[0];
}

// envia um arquivo para a Biblioteca de mídia; $tmp é apagado depois
function wd_imp_media_file($tmp, $name, $src, $hash, $alt = '', $parent = 0) {
    wd_imp_includes();
    $ex = wd_imp_find_media($src, $hash);
    if ($ex > 0) { @unlink($tmp); if ($alt !== '') update_post_meta($ex, '_wp_attachment_image_alt', $alt); return $ex; }
    if ($ex < 0) wp_delete_attachment(-$ex, true);
    $id = media_handle_sideload(['name' => $name, 'tmp_name' => $tmp], $parent);
    if (is_wp_error($id)) { @unlink($tmp); return $id; }
    update_post_meta($id, '_wd_src', $src);
    update_post_meta($id, '_wd_hash', $hash);
    if ($alt !== '') update_post_meta($id, '_wp_attachment_image_alt', $alt);
    return $id;
}

function wd_imp_upsert($type, $slug, $args) {
    $ex = get_posts(['post_type' => $type, 'post_status' => 'any', 'numberposts' => 1, 'meta_query' => [['key' => '_wd_imp', 'value' => $slug]]])
        ?: get_posts(['post_type' => $type, 'name' => $slug, 'post_status' => 'any', 'numberposts' => 1]);
    if (!$ex && $type === 'page' && $slug === 'politica-de-privacidade' && ($pp = get_post((int) get_option('wp_page_for_privacy_policy')))) $ex = [$pp];
    $args += ['post_type' => $type, 'post_name' => $slug];
    $id = $ex ? wp_update_post($args + ['ID' => $ex[0]->ID], true) : wp_insert_post($args, true);
    if (!is_wp_error($id)) update_post_meta($id, '_wd_imp', $slug);
    return $id;
}

function wd_imp_seo($id, $title = '', $desc = '', $kw = '') {
    if ($title !== '') update_post_meta($id, '_yoast_wpseo_title', $title);
    if ($desc !== '') update_post_meta($id, '_yoast_wpseo_metadesc', $desc);
    if ($kw !== '') update_post_meta($id, '_yoast_wpseo_focuskw', $kw);
}

function wd_imp_categories($names) {
    $ids = [];
    foreach ($names as $name) {
        $t = term_exists($name, 'category') ?: wp_insert_term($name, 'category', ['slug' => sanitize_title($name)]);
        $ids[$name] = (int) (is_array($t) ? $t['term_id'] : $t);
    }
    $unc = get_term_by('slug', 'sem-categoria', 'category') ?: get_term_by('slug', 'uncategorized', 'category');
    if ($unc && !$unc->count && (int) get_option('default_category') === (int) $unc->term_id && isset($ids['Negócios'])) update_option('default_category', $ids['Negócios']);
    return $ids;
}

// páginas, página inicial, página de artigos, privacidade e bio
function wd_imp_pages($pages, $author_id) {
    $ids = [];
    foreach ($pages as $p) {
        $id = wd_imp_upsert('page', $p['slug'], ['post_title' => $p['title'], 'post_content' => $p['content'], 'post_status' => $p['status'] ?? 'publish', 'post_author' => $author_id]);
        if (is_wp_error($id)) continue;
        $ids[$p['slug']] = $id;
        wd_imp_seo($id, $p['seo_title'] ?? '', $p['seo_desc'] ?? '');
    }
    if (isset($ids['home'])) { update_option('show_on_front', 'page'); update_option('page_on_front', $ids['home']); }
    if (isset($ids['blog'])) update_option('page_for_posts', $ids['blog']);
    if (isset($ids['politica-de-privacidade'])) update_option('wp_page_for_privacy_policy', $ids['politica-de-privacidade']);
    update_option('wd_bio_user', $author_id);
    // conteúdo de exemplo de uma instalação nova
    foreach ([['post', 'ola-mundo'], ['post', 'hello-world'], ['page', 'pagina-exemplo'], ['page', 'sample-page']] as [$t, $s]) {
        foreach (get_posts(['post_type' => $t, 'name' => $s, 'post_status' => 'any', 'numberposts' => 1]) as $x) if (!get_post_meta($x->ID, '_wd_imp', true)) wp_delete_post($x->ID, true);
    }
    return $ids;
}

function wd_imp_article($p, $author_id, $cat_ids, $img_id = 0, $kw = '') {
    $id = wd_imp_upsert('post', $p['slug'], ['post_title' => $p['title'], 'post_content' => $p['content'], 'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish', 'post_date' => $p['date'], 'post_date_gmt' => get_gmt_from_date($p['date']), 'post_author' => $author_id,
        'post_category' => [$cat_ids[$p['cat']] ?? 0], 'comment_status' => 'closed', 'ping_status' => 'closed']);
    if (is_wp_error($id)) return $id;
    update_post_meta($id, 'wd_dek', $p['dek']);
    if ($img_id) { set_post_thumbnail($id, $img_id); wp_update_post(['ID' => $img_id, 'post_parent' => $id]); }
    wd_imp_seo($id, '', $p['seo_desc'] ?? '', $kw);
    return $id;
}

function wd_imp_case($c, $author_id, $files) {
    $id = wd_imp_upsert('case', $c['slug'], ['post_title' => $c['title'], 'post_status' => 'publish', 'menu_order' => $c['order'], 'post_author' => $author_id]);
    if (is_wp_error($id)) return $id;
    foreach ($c['meta'] as $k => $v) update_post_meta($id, 'wd_' . $k, $v);
    foreach ($files as $k => $att) { update_post_meta($id, 'wd_' . $k, (string) (int) $att); if ($att) wp_update_post(['ID' => (int) $att, 'post_parent' => $id]); }
    if (!empty($files['m01'])) set_post_thumbnail($id, (int) $files['m01']);
    wd_imp_seo($id, $c['seo_title'] ?? '', $c['seo_desc'] ?? '');
    return $id;
}

// endereços, Yoast e regras de reescrita
function wd_imp_finish($s) {
    wd_imp_includes();
    update_option('permalink_structure', '/blog/%postname%/');
    update_option('category_base', 'blog/categoria');
    update_option('tag_base', 'blog/tag');
    update_option('timezone_string', 'America/Sao_Paulo');
    update_option('default_comment_status', 'closed');
    update_option('blogdescription', 'Criação de sites profissionais');
    if (defined('WPSEO_VERSION')) {
        $t = array_merge(get_option('wpseo_titles', []) ?: [], [
            'separator' => 'sc-dash', 'website_name' => 'Work Digital', 'company_or_person' => 'company', 'company_name' => $s['company_name'] ?? 'Work Digital',
            'company_logo' => get_template_directory_uri() . '/assets/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg',
            'title-post' => '%%title%% %%sep%% %%sitename%%', 'title-page' => '%%title%% %%sep%% %%sitename%%', 'title-case' => '%%title%% %%sep%% %%sitename%%',
            'title-ptarchive-case' => $s['cases_archive_title'] ?? '', 'metadesc-ptarchive-case' => $s['cases_archive_desc'] ?? '',
            'title-tax-category' => '%%term_title%% %%sep%% Blog da Work', 'noindex-author-wpseo' => true, 'disable-author' => true,
            'disable-attachment' => true, 'noindex-tax-post_tag' => true,
            'title-404-wpseo' => 'Página não encontrada %%sep%% %%sitename%%', 'title-search-wpseo' => 'Busca: %%searchphrase%% %%sep%% %%sitename%%',
        ]);
        update_option('wpseo_titles', $t);
        $so = get_option('wpseo_social', []) ?: [];
        if (!empty($s['social'])) { $so['facebook_site'] = $s['social'][1]; $so['other_social_urls'] = [$s['social'][0], $s['social'][2]]; }
        $so['og_default_image'] = get_template_directory_uri() . '/assets/media/servico-sites.jpg';
        update_option('wpseo_social', $so);
    }
    flush_rewrite_rules(true);
    return ['permalinks' => get_option('permalink_structure'), 'yoast' => defined('WPSEO_VERSION'), 'htaccess' => got_mod_rewrite() ? 'apache' : 'outro'];
}

// ---------- rotas do envio remoto ----------
add_action('rest_api_init', function () {
    $admin = fn() => current_user_can('manage_options');
    $ns = 'wd/v1';
    register_rest_route($ns, '/import/ping', ['methods' => 'GET', 'permission_callback' => $admin, 'callback' => fn() => [
        'tema' => WD_VER, 'usuario' => wp_get_current_user()->user_login, 'yoast' => defined('WPSEO_VERSION'),
        'upload_max' => wp_max_upload_size(), 'php' => PHP_VERSION, 'wp' => get_bloginfo('version')]]);
    register_rest_route($ns, '/import/media', [
        ['methods' => 'GET', 'permission_callback' => $admin, 'callback' => function (WP_REST_Request $r) {
            $id = wd_imp_find_media((string) $r['src'], (string) $r['hash']);
            return ['id' => $id > 0 ? $id : 0];
        }],
        ['methods' => 'POST', 'permission_callback' => $admin, 'callback' => function (WP_REST_Request $r) {
            $f = $r->get_file_params()['file'] ?? null;
            if (!$f || !empty($f['error'])) return new WP_Error('wd_upload', 'Arquivo não recebido (código ' . ($f['error'] ?? '?') . ')', ['status' => 400]);
            wd_imp_includes();
            $tmp = wp_tempnam($f['name']); move_uploaded_file($f['tmp_name'], $tmp) || copy($f['tmp_name'], $tmp);
            $id = wd_imp_media_file($tmp, sanitize_file_name($r['name'] ?: $f['name']), (string) $r['src'], (string) $r['hash'], (string) $r['alt']);
            return is_wp_error($id) ? $id : ['id' => $id];
        }],
    ]);
    register_rest_route($ns, '/import/setup', ['methods' => 'POST', 'permission_callback' => $admin, 'callback' => function (WP_REST_Request $r) {
        $d = $r->get_json_params();
        $cats = wd_imp_categories($d['categories'] ?? []);
        $pages = wd_imp_pages($d['pages'] ?? [], get_current_user_id());
        return ['categorias' => $cats, 'paginas' => $pages];
    }]);
    register_rest_route($ns, '/import/post', ['methods' => 'POST', 'permission_callback' => $admin, 'callback' => function (WP_REST_Request $r) {
        $d = $r->get_json_params();
        $cats = wd_imp_categories([$d['post']['cat']]);
        $id = wd_imp_article($d['post'], get_current_user_id(), $cats, (int) ($d['image_id'] ?? 0), (string) ($d['keyword'] ?? ''));
        return is_wp_error($id) ? $id : ['id' => $id, 'url' => get_permalink($id)];
    }]);
    register_rest_route($ns, '/import/case', ['methods' => 'POST', 'permission_callback' => $admin, 'callback' => function (WP_REST_Request $r) {
        $d = $r->get_json_params();
        $id = wd_imp_case($d['case'], get_current_user_id(), $d['files'] ?? []);
        return is_wp_error($id) ? $id : ['id' => $id];
    }]);
    register_rest_route($ns, '/import/finish', ['methods' => 'POST', 'permission_callback' => $admin, 'callback' => fn(WP_REST_Request $r) => wd_imp_finish($r->get_json_params() ?: [])]);
});
