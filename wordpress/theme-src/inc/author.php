<?php
/* Autoria: campos extras no perfil (cargo, foto, assinatura, redes) e página de bio em /bio/ */
if (!defined('ABSPATH')) exit;

const WD_USER_FIELDS = [
    'wd_cargo' => 'Cargo (ex.: Fundador(a) da Work Digital)',
    'wd_foto' => 'Foto (ID da imagem na Biblioteca de mídia)',
    'wd_assinatura' => 'Assinatura manuscrita (ID da imagem, opcional)',
    'wd_linkedin' => 'LinkedIn (URL)',
    'wd_instagram' => 'Instagram (URL)',
];

function wd_user_fields_ui($user) {
    echo '<h2>Bio no site</h2><p>A biografia usa o campo "Informações biográficas" acima. A página /bio/ mostra a pessoa escolhida em Configurações › Leitura › "Autor(a) da bio".</p><table class="form-table">';
    foreach (WD_USER_FIELDS as $k => $label) {
        $v = get_user_meta($user->ID, $k, true);
        echo '<tr><th><label for="' . $k . '">' . esc_html($label) . '</label></th><td><input class="regular-text" id="' . $k . '" name="' . $k . '" value="' . esc_attr($v) . '"></td></tr>';
    }
    echo '</table>';
}
add_action('show_user_profile', 'wd_user_fields_ui');
add_action('edit_user_profile', 'wd_user_fields_ui');
function wd_user_fields_save($id) {
    if (!current_user_can('edit_user', $id)) return;
    foreach (array_keys(WD_USER_FIELDS) as $k) {
        if (!isset($_POST[$k])) continue;
        $v = wp_unslash($_POST[$k]);
        update_user_meta($id, $k, in_array($k, ['wd_foto', 'wd_assinatura'], true) ? (string) absint($v) : (str_starts_with($k, 'wd_l') || str_starts_with($k, 'wd_i') ? esc_url_raw($v) : sanitize_text_field($v)));
    }
}
add_action('personal_options_update', 'wd_user_fields_save');
add_action('edit_user_profile_update', 'wd_user_fields_save');

// quem aparece na página /bio/ (padrão: quem mais publicou artigos)
add_action('admin_init', function () {
    register_setting('reading', 'wd_bio_user', ['type' => 'integer', 'sanitize_callback' => 'absint']);
    add_settings_field('wd_bio_user', 'Autor(a) da bio', function () {
        wp_dropdown_users(['name' => 'wd_bio_user', 'selected' => (int) get_option('wd_bio_user'), 'show_option_none' => 'Automático']);
    }, 'reading');
});
function wd_bio_user() {
    $id = (int) get_option('wd_bio_user');
    if ($id && get_userdata($id)) return get_userdata($id);
    global $wpdb;
    $top = (int) $wpdb->get_var("SELECT post_author FROM {$wpdb->posts} WHERE post_type='post' AND post_status='publish' GROUP BY post_author ORDER BY COUNT(*) DESC LIMIT 1");
    return get_userdata($top ?: 1);
}
function wd_bio_url() { return wd_url('bio/'); }
function wd_user_img($user, $key, $size = 'medium') {
    $id = (int) get_user_meta($user->ID, $key, true);
    if ($id) return wp_get_attachment_image_url($id, $size);
    // sem foto própria: usa a foto do Gravatar (pelo e-mail do usuário)
    if ($key === 'wd_foto') return get_avatar_url($user, ['size' => $size === 'thumbnail' ? 96 : 480, 'default' => 'mp']);
    return '';
}

// perfil público do Gravatar (nome, "sobre", cargo e redes), guardado por 12 horas
function wd_gravatar_profile($user) {
    if (!$user || !$user->user_email) return [];
    $hash = hash('sha256', strtolower(trim($user->user_email)));
    $k = 'wd_grav_' . substr($hash, 0, 20);
    $p = get_transient($k);
    if ($p === false) {
        $r = wp_remote_get('https://api.gravatar.com/v3/profiles/' . $hash, ['timeout' => 5]);
        $p = (!is_wp_error($r) && wp_remote_retrieve_response_code($r) === 200) ? (json_decode(wp_remote_retrieve_body($r), true) ?: []) : [];
        set_transient($k, $p, $p ? 12 * HOUR_IN_SECONDS : HOUR_IN_SECONDS);
    }
    return $p;
}
// dados da bio: o que estiver preenchido no WordPress vale; o que faltar vem do Gravatar
function wd_bio_data($user) {
    $g = wd_gravatar_profile($user);
    $links = array_values(array_filter([get_user_meta($user->ID, 'wd_linkedin', true), get_user_meta($user->ID, 'wd_instagram', true)]));
    $named = [];
    if (get_user_meta($user->ID, 'wd_linkedin', true)) $named['LinkedIn'] = get_user_meta($user->ID, 'wd_linkedin', true);
    if (get_user_meta($user->ID, 'wd_instagram', true)) $named['Instagram'] = get_user_meta($user->ID, 'wd_instagram', true);
    foreach ($g['verified_accounts'] ?? [] as $a) if (!empty($a['url']) && !in_array($a['url'], $links, true)) $named[$a['service_label'] ?? $a['service_type'] ?? 'Perfil'] = $a['url'];
    foreach ($g['links'] ?? [] as $l) if (!empty($l['url'])) $named[$l['label'] ?? 'Site'] = $l['url'];
    return [
        'name' => $user->display_name,
        'cargo' => get_user_meta($user->ID, 'wd_cargo', true) ?: trim(($g['job_title'] ?? '') . (!empty($g['company']) ? ' · ' . $g['company'] : '')),
        'bio' => get_the_author_meta('description', $user->ID) ?: ($g['description'] ?? ''),
        'links' => $named,
    ];
}

// arquivo de autor (/author/...) leva para a bio: o site tem uma única autoria
add_action('template_redirect', function () {
    if (is_author()) { wp_safe_redirect(wd_bio_url(), 301); exit; }
});
add_filter('author_link', fn() => wd_bio_url());

// título da página /bio/: o nome de quem assina
function wd_bio_title($t) {
    if (!is_page('bio')) return $t;
    $u = wd_bio_user();
    return $u ? $u->display_name . ' - Work Digital' : $t;
}
add_filter('wpseo_title', 'wd_bio_title');
add_filter('pre_get_document_title', fn($t) => is_page('bio') && !wd_has_yoast() ? wd_bio_title($t) : $t, 20);

// Artigos: quadro "Linha fina" (texto abaixo do título)
add_action('add_meta_boxes_post', function () {
    add_meta_box('wd-dek', 'Linha fina (texto abaixo do título)', function ($post) {
        wp_nonce_field('wd_dek_save', 'wd_dek_nonce');
        echo '<textarea name="wd_dek" style="width:100%;min-height:70px">' . esc_textarea(get_post_meta($post->ID, 'wd_dek', true)) . '</textarea><p class="description">Se ficar vazio, usa o Resumo.</p>';
    }, 'post', 'normal', 'high');
});
add_action('save_post_post', function ($id) {
    if (!isset($_POST['wd_dek_nonce']) || !wp_verify_nonce($_POST['wd_dek_nonce'], 'wd_dek_save') || !current_user_can('edit_post', $id)) return;
    update_post_meta($id, 'wd_dek', sanitize_textarea_field(wp_unslash($_POST['wd_dek'] ?? '')));
});
