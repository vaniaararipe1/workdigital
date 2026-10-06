<?php
/**
 * Importa o conteúdo do site para o WordPress (cases, artigos, páginas e configurações).
 * Uso:  WD_BASE=/caminho/do/repositorio WD_AUTOR=login wp eval-file wordpress/importar.php
 * Pode rodar mais de uma vez: o que já existe é atualizado (nada é duplicado).
 */
if (!defined('ABSPATH')) { fwrite(STDERR, "Rode com: wp eval-file importar.php\n"); exit(1); }
require_once ABSPATH . 'wp-admin/includes/media.php';
require_once ABSPATH . 'wp-admin/includes/file.php';
require_once ABSPATH . 'wp-admin/includes/image.php';

$base = rtrim(getenv('WD_BASE') ?: dirname(__DIR__), '/');
define('WD_IMP_BASE', $base);
$data = json_decode(file_get_contents($base . '/wordpress/importacao/conteudo.json'), true);
if (!$data) { WP_CLI::error('conteudo.json não encontrado em ' . $base); }

$login = getenv('WD_AUTOR');
$author = $login ? get_user_by('login', $login) : null;
if (!$author) { $admins = get_users(['role' => 'administrator', 'number' => 1, 'orderby' => 'ID']); $author = $admins[0] ?? null; }
if (!$author) WP_CLI::error('Nenhum usuário administrador encontrado.');
WP_CLI::log('Autor(a) dos artigos: ' . $author->user_login);

// envia um arquivo para a Biblioteca de mídia (uma vez só: o caminho de origem fica guardado no anexo)
function wd_imp_media($rel, $parent = 0, $alt = '') {
    $path = WD_IMP_BASE . '/' . $rel;
    if (!file_exists($path)) { WP_CLI::warning('Arquivo não encontrado: ' . $rel); return 0; }
    $hash = md5_file($path);
    $found = get_posts(['post_type' => 'attachment', 'post_status' => 'inherit', 'numberposts' => 1, 'meta_query' => [['key' => '_wd_src', 'value' => $rel]]]);
    if ($found) {
        $id = $found[0]->ID;
        if (get_post_meta($id, '_wd_hash', true) === $hash) { if ($alt !== '') update_post_meta($id, '_wp_attachment_image_alt', $alt); return $id; }
        wp_delete_attachment($id, true); // o arquivo mudou: troca pelo novo
    }
    $tmp = wp_tempnam(basename($path)); copy($path, $tmp);
    $name = basename($path);
    if (preg_match('#^site/(cases|thumbs)/#', $rel) && str_contains($rel, '/cases/')) $name = basename(dirname($path)) . '-' . $name;
    $id = media_handle_sideload(['name' => $name, 'tmp_name' => $tmp], $parent);
    if (is_wp_error($id)) { @unlink($tmp); WP_CLI::warning($rel . ': ' . $id->get_error_message()); return 0; }
    update_post_meta($id, '_wd_src', $rel);
    update_post_meta($id, '_wd_hash', $hash);
    if ($alt !== '') update_post_meta($id, '_wp_attachment_image_alt', $alt);
    return $id;
}
function wd_imp_post($type, $slug, $args) {
    // procura primeiro o que este importador já criou; depois, um item com o mesmo endereço
    $ex = get_posts(['post_type' => $type, 'post_status' => 'any', 'numberposts' => 1, 'meta_query' => [['key' => '_wd_imp', 'value' => $slug]]])
        ?: get_posts(['post_type' => $type, 'name' => $slug, 'post_status' => 'any', 'numberposts' => 1]);
    if (!$ex && $type === 'page' && $slug === 'politica-de-privacidade' && (int) get_option('wp_page_for_privacy_policy')) {
        $ex = [get_post((int) get_option('wp_page_for_privacy_policy'))]; // a página de privacidade padrão do WordPress vira a nossa
    }
    $args += ['post_type' => $type, 'post_name' => $slug];
    $id = $ex && $ex[0] ? wp_update_post($args + ['ID' => $ex[0]->ID], true) : wp_insert_post($args, true);
    if (!is_wp_error($id)) update_post_meta($id, '_wd_imp', $slug);
    return $id;
}
function wd_imp_seo($id, $title, $desc, $kw = '') {
    if ($title !== '') update_post_meta($id, '_yoast_wpseo_title', $title);
    if ($desc !== '') update_post_meta($id, '_yoast_wpseo_metadesc', $desc);
    if ($kw !== '') update_post_meta($id, '_yoast_wpseo_focuskw', $kw);
}

// ---------- categorias ----------
$cat_ids = [];
foreach ($data['categories'] as $name) {
    $t = term_exists($name, 'category') ?: wp_insert_term($name, 'category', ['slug' => sanitize_title($name)]);
    $cat_ids[$name] = (int) (is_array($t) ? $t['term_id'] : $t);
}
$unc = get_term_by('slug', 'sem-categoria', 'category') ?: get_term_by('slug', 'uncategorized', 'category');
if ($unc && !$unc->count) wp_update_term($unc->term_id, 'category', ['name' => 'Negócios antigos']);

// ---------- páginas ----------
$page_ids = [];
foreach ($data['pages'] as $p) {
    $id = wd_imp_post('page', $p['slug'], ['post_title' => $p['title'], 'post_content' => $p['content'], 'post_status' => $p['status'] ?? 'publish', 'post_author' => $author->ID]);
    if (is_wp_error($id)) { WP_CLI::warning($p['slug'] . ': ' . $id->get_error_message()); continue; }
    $page_ids[$p['slug']] = $id;
    wd_imp_seo($id, $p['seo_title'], $p['seo_desc']);
}
update_option('show_on_front', 'page');
update_option('page_on_front', $page_ids['home']);
update_option('page_for_posts', $page_ids['blog']);
update_option('wp_page_for_privacy_policy', $page_ids['politica-de-privacidade']);
update_option('wd_bio_user', $author->ID);
WP_CLI::log('Páginas: ' . count($page_ids));

// ---------- artigos ----------
$keys = [];
foreach (glob($base . '/site/blog-artigos/*.json') as $f) { $j = json_decode(file_get_contents($f), true); $keys[basename($f, '.json')] = $j['keywords'][0] ?? ''; }
foreach ($data['posts'] as $p) {
    $id = wd_imp_post('post', $p['slug'], ['post_title' => $p['title'], 'post_content' => $p['content'], 'post_excerpt' => $p['excerpt'],
        'post_status' => 'publish', 'post_date' => $p['date'], 'post_date_gmt' => get_gmt_from_date($p['date']), 'post_author' => $author->ID,
        'post_category' => [$cat_ids[$p['cat']]], 'comment_status' => 'closed', 'ping_status' => 'closed']);
    if (is_wp_error($id)) { WP_CLI::warning($p['slug'] . ': ' . $id->get_error_message()); continue; }
    update_post_meta($id, 'wd_dek', $p['dek']);
    $img = wd_imp_media($p['image']['file'], $id, $p['image']['alt']);
    if ($img) set_post_thumbnail($id, $img);
    wd_imp_seo($id, '', $p['seo_desc'], $keys[$p['slug']] ?? '');
}
WP_CLI::log('Artigos: ' . count($data['posts']));

// ---------- cases ----------
foreach ($data['cases'] as $c) {
    $id = wd_imp_post('case', $c['slug'], ['post_title' => $c['title'], 'post_status' => 'publish', 'menu_order' => $c['order'], 'post_author' => $author->ID]);
    if (is_wp_error($id)) { WP_CLI::warning($c['slug'] . ': ' . $id->get_error_message()); continue; }
    foreach ($c['meta'] as $k => $v) update_post_meta($id, 'wd_' . $k, $v);
    foreach ($c['files'] as $k => $f) update_post_meta($id, 'wd_' . $k, (string) wd_imp_media($f['file'], $id, $f['alt'] ?? ''));
    if (!empty($c['files']['m01'])) set_post_thumbnail($id, (int) get_post_meta($id, 'wd_m01', true));
    wd_imp_seo($id, $c['seo_title'], $c['seo_desc']);
    WP_CLI::log('Case: ' . $c['title']);
}

// ---------- Yoast ----------
if (defined('WPSEO_VERSION')) {
    $s = $data['settings'];
    $t = get_option('wpseo_titles', []);
    $t = array_merge($t, [
        'separator' => 'sc-dash', 'website_name' => 'Work Digital', 'company_or_person' => 'company', 'company_name' => $s['company_name'],
        'company_logo' => get_template_directory_uri() . '/assets/ativos-externos/logo-work-digital-branco-criacao-de-site-sp.svg',
        'title-post' => '%%title%% %%sep%% %%sitename%%', 'title-page' => '%%title%% %%sep%% %%sitename%%',
        'title-case' => '%%title%% %%sep%% %%sitename%%', 'title-ptarchive-case' => $s['cases_archive_title'], 'metadesc-ptarchive-case' => $s['cases_archive_desc'],
        'title-tax-category' => '%%term_title%% %%sep%% Blog da Work', 'noindex-author-wpseo' => true, 'disable-author' => true,
        'disable-attachment' => true, 'noindex-tax-post_tag' => true,
        'title-404-wpseo' => 'Página não encontrada %%sep%% %%sitename%%', 'title-search-wpseo' => 'Busca: %%searchphrase%% %%sep%% %%sitename%%',
    ]);
    update_option('wpseo_titles', $t);
    $so = get_option('wpseo_social', []);
    $so['facebook_site'] = $s['social'][1];
    $so['other_social_urls'] = [$s['social'][0], $s['social'][2]];
    update_option('wpseo_social', $so);
    WP_CLI::log('Yoast configurado.');
}
flush_rewrite_rules();
WP_CLI::success('Importação concluída.');
