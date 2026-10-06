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
    return $id ? wp_get_attachment_image_url($id, $size) : '';
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
