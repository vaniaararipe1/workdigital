<?php
/* Formulário "Solicitar proposta": envia por e-mail (wp_mail) pelo endpoint /wp-json/wd/v1/contato */
if (!defined('ABSPATH')) exit;

add_action('admin_init', function () {
    register_setting('general', 'wd_contact_to', ['type' => 'string', 'sanitize_callback' => 'sanitize_email']);
    add_settings_field('wd_contact_to', 'E-mail que recebe as propostas', function () {
        echo '<input class="regular-text" type="email" name="wd_contact_to" value="' . esc_attr(get_option('wd_contact_to')) . '" placeholder="' . esc_attr(get_option('admin_email')) . '">';
    }, 'general');
});

add_action('rest_api_init', function () {
    register_rest_route('wd/v1', '/contato', ['methods' => 'POST', 'permission_callback' => '__return_true', 'callback' => function (WP_REST_Request $r) {
        $d = $r->get_json_params() ?: [];
        if (!empty($d['empresa_site'])) return new WP_REST_Response(['ok' => true], 200); // campo-isca contra robôs
        $ip = preg_replace('/[^0-9a-f:.]/i', '', $_SERVER['REMOTE_ADDR'] ?? '');
        $k = 'wd_ct_' . md5($ip);
        $n = (int) get_transient($k);
        if ($n >= 5) return new WP_REST_Response(['ok' => false, 'erro' => 'Muitas tentativas. Tente de novo em alguns minutos.'], 429);
        set_transient($k, $n + 1, 10 * MINUTE_IN_SECONDS);
        $nome = sanitize_text_field($d['nome'] ?? '');
        $email = sanitize_email($d['email'] ?? '');
        if ($nome === '' || !is_email($email)) return new WP_REST_Response(['ok' => false, 'erro' => 'Nome e e-mail são obrigatórios.'], 400);
        $linhas = [];
        foreach ($d as $campo => $valor) {
            if (in_array($campo, ['empresa_site'], true) || is_array($valor)) continue;
            $linhas[] = ucfirst(sanitize_key($campo)) . ': ' . sanitize_textarea_field((string) $valor);
        }
        $to = get_option('wd_contact_to') ?: get_option('admin_email');
        $ok = wp_mail($to, 'Nova solicitação de proposta — ' . $nome, implode("\n", $linhas) . "\n\nEnviado pelo site " . home_url('/'), ['Reply-To: ' . $nome . ' <' . $email . '>']);
        return new WP_REST_Response(['ok' => (bool) $ok], $ok ? 200 : 500);
    }]);
});

// o script do formulário lê este endereço e o link da política de privacidade
add_action('wp_head', function () {
    $privacy = get_privacy_policy_url();
    echo '<script>window.WD_CONTACT_CONFIG=' . wp_json_encode(['endpoint' => rest_url('wd/v1/contato'), 'privacyUrl' => $privacy ?: '']) . ';</script>' . "\n";
}, 1);
