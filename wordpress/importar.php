<?php
/**
 * Importa o conteúdo do site com WP-CLI (quando há acesso SSH). Sem SSH, use enviar.py (mesmo resultado).
 * Uso:  WD_BASE=/caminho/do/repositorio WD_AUTOR=login wp eval-file wordpress/importar.php
 * Precisa do tema Work Digital ativo. Pode rodar de novo: nada é duplicado.
 */
if (!defined('ABSPATH') || !function_exists('wd_imp_upsert')) { fwrite(STDERR, "Ative o tema Work Digital e rode com: wp eval-file importar.php\n"); exit(1); }
$base = rtrim(getenv('WD_BASE') ?: dirname(__DIR__), '/');
$data = json_decode(file_get_contents($base . '/wordpress/importacao/conteudo.json'), true) or WP_CLI::error('conteudo.json não encontrado');
$login = getenv('WD_AUTOR');
$author = $login ? get_user_by('login', $login) : (get_users(['role' => 'administrator', 'number' => 1, 'orderby' => 'ID'])[0] ?? null);
if (!$author) WP_CLI::error('Usuário não encontrado.');
wp_set_current_user($author->ID);

$media = function ($f, $parent = 0) use ($base) {
    $path = $base . '/' . $f['file'];
    if (!file_exists($path)) { WP_CLI::warning('Arquivo não encontrado: ' . $f['file']); return 0; }
    $tmp = wp_tempnam(basename($path)); copy($path, $tmp);
    $name = str_contains($f['file'], '/cases/') ? basename(dirname($path)) . '-' . basename($path) : basename($path);
    $id = wd_imp_media_file($tmp, $name, $f['file'], md5_file($path), $f['alt'] ?? '', $parent);
    if (is_wp_error($id)) { WP_CLI::warning($f['file'] . ': ' . $id->get_error_message()); return 0; }
    return $id;
};
$cats = wd_imp_categories($data['categories']);
wd_imp_pages($data['pages'], $author->ID);
$kw = [];
foreach (glob($base . '/site/blog-artigos/*.json') as $f) { $j = json_decode(file_get_contents($f), true); $kw[basename($f, '.json')] = $j['keywords'][0] ?? ''; }
foreach ($data['posts'] as $p) wd_imp_article($p, $author->ID, $cats, $media($p['image']), $kw[$p['slug']] ?? '');
WP_CLI::log('Artigos: ' . count($data['posts']));
foreach ($data['cases'] as $c) { $ids = []; foreach ($c['files'] as $k => $f) $ids[$k] = $media($f); wd_imp_case($c, $author->ID, $ids); WP_CLI::log('Case: ' . $c['title']); }
WP_CLI::log(json_encode(wd_imp_finish($data['settings'])));
if (defined('WPSEO_VERSION')) WP_CLI::runcommand('yoast index --reindex --skip-confirmation', ['return' => true, 'exit_error' => false]);
WP_CLI::success('Importação concluída.');
