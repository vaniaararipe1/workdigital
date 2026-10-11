<?php
/* Formulário "Solicitar proposta": envia por e-mail (wp_mail) pelo endpoint /wp-json/wd/v1/contato */
if (!defined('ABSPATH')) exit;

add_action('admin_init', function () {
    register_setting('general', 'wd_contact_to', ['type' => 'string', 'sanitize_callback' => 'sanitize_email']);
    add_settings_field('wd_contact_to', 'E-mail que recebe as propostas', function () {
        echo '<input class="regular-text" type="email" name="wd_contact_to" value="' . esc_attr(get_option('wd_contact_to')) . '" placeholder="' . esc_attr(get_option('admin_email')) . '">';
    }, 'general');
});

// RD Station Marketing: cada proposta vira uma conversão "solicitar-proposta-site"
add_action('admin_init', function () {
    foreach ([
        'wd_rd_public_token' => ['Token público do RD Station', 'RD Station Marketing › Conta › Integrações › Token público. Com ele, cada proposta do formulário entra no RD como conversão "solicitar-proposta-site".'],
        'wd_rd_cf_ideia' => ['Campo do RD para "Qual é a sua ideia?"', 'Opcional. Identificador do campo personalizado no RD (ex.: cf_ideia).'],
        'wd_rd_cf_origem' => ['Campo do RD para "Como você conheceu a Work?"', 'Opcional. Identificador do campo personalizado no RD (ex.: cf_como_conheceu).'],
    ] as $k => [$label, $help]) {
        register_setting('general', $k, ['type' => 'string', 'sanitize_callback' => 'sanitize_text_field']);
        add_settings_field($k, $label, function () use ($k, $help) {
            echo '<input class="regular-text" name="' . $k . '" value="' . esc_attr(get_option($k)) . '"><p class="description">' . esc_html($help) . '</p>';
            if ($k === 'wd_rd_public_token' && ($last = get_option('wd_rd_last'))) echo '<p class="description">Último envio ao RD: ' . esc_html($last) . '</p>';
        }, 'general');
    }
});

function wd_rd_token() { return trim((string) (get_option('wd_rd_public_token') ?: get_option('rdsm_public_token'))); }

// envia ao RD; devolve true (enviado), false (falhou) ou null (sem token configurado)
function wd_rd_conversion($d, $nome, $email) {
    $token = wd_rd_token();
    if ($token === '') return null;
    $payload = ['conversion_identifier' => 'solicitar-proposta-site', 'email' => $email, 'name' => $nome,
        'legal_bases' => [['category' => 'communications', 'type' => 'legitimate_interest', 'status' => 'granted']]];
    if (!empty($d['empresa'])) $payload['company_name'] = sanitize_text_field($d['empresa']);
    $src = $_COOKIE['__trf_src'] ?? ($_COOKIE['__trf.src'] ?? ''); // origem do tráfego gravada pelo script do RD
    if ($src) $payload['traffic_source'] = sanitize_text_field(wp_unslash($src));
    $extra = [];
    foreach (['ideia' => 'wd_rd_cf_ideia', 'origem' => 'wd_rd_cf_origem'] as $campo => $opt) {
        $cf = sanitize_key(get_option($opt));
        if ($cf && !empty($d[$campo])) $extra[$cf] = sanitize_textarea_field((string) $d[$campo]);
    }
    $send = function ($p) use ($token) {
        return wp_remote_post('https://api.rd.services/platform/conversions?api_key=' . rawurlencode($token), [
            'timeout' => 10, 'headers' => ['Content-Type' => 'application/json'],
            'body' => wp_json_encode(['event_type' => 'CONVERSION', 'event_family' => 'CDP', 'payload' => $p])]);
    };
    $r = $send($payload + $extra);
    $code = is_wp_error($r) ? 0 : (int) wp_remote_retrieve_response_code($r);
    if ($extra && $code === 400) { $r = $send($payload); $code = is_wp_error($r) ? 0 : (int) wp_remote_retrieve_response_code($r); } // campo personalizado inexistente no RD: envia o básico
    $ok = $code >= 200 && $code < 300;
    $msg = $ok ? 'ok' : ('erro ' . ($code ?: (is_wp_error($r) ? $r->get_error_message() : '?')) . ' ' . substr((string) wp_remote_retrieve_body($r), 0, 200));
    update_option('wd_rd_last', wp_date('d/m/Y H:i') . ' — ' . $msg, false);
    if (!$ok) error_log('Work Digital / RD Station: ' . $msg);
    return $ok;
}

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
        $mail = wp_mail($to, 'Nova solicitação de proposta — ' . $nome, implode("\n", $linhas) . "\n\nEnviado pelo site " . home_url('/'), ['Reply-To: ' . $nome . ' <' . $email . '>']);
        $rd = wd_rd_conversion($d, $nome, $email);
        $ok = $mail || $rd === true; // o lead vale se chegou por e-mail OU no RD Station
        return new WP_REST_Response(['ok' => $ok, 'email' => (bool) $mail, 'rd' => $rd === null ? 'desligado' : (bool) $rd], $ok ? 200 : 500);
    }]);
});

// o script do formulário lê este endereço e o link da política de privacidade
add_action('wp_head', function () {
    $privacy = get_privacy_policy_url();
    echo '<script>window.WD_CONTACT_CONFIG=' . wp_json_encode(['endpoint' => rest_url('wd/v1/contato'), 'privacyUrl' => $privacy ?: '', 'thanksUrl' => wd_url('obrigado/')]) . ';</script>' . "\n";
}, 1);

// /obrigado/ fica fora do Google e do sitemap (é página de conversão, não de conteúdo)
add_filter('wpseo_robots', fn($r) => is_page('obrigado') ? 'noindex, nofollow' : $r);
add_filter('wp_robots', function ($r) { if (is_page('obrigado')) { $r['noindex'] = true; $r['nofollow'] = true; } return $r; });
add_filter('wpseo_exclude_from_sitemap_by_post_ids', function ($ids) {
    $p = get_page_by_path('obrigado');
    return $p ? array_merge((array) $ids, [$p->ID]) : $ids;
});

// cria a página /obrigado/ sozinho (uma vez), se ainda não existir
add_action('init', function () {
    if (get_option('wd_obrigado_ok') || get_page_by_path('obrigado')) { update_option('wd_obrigado_ok', 1); return; }
    $id = wp_insert_post(['post_type' => 'page', 'post_status' => 'publish', 'post_title' => 'Obrigado', 'post_name' => 'obrigado', 'post_content' => '', 'comment_status' => 'closed']);
    if ($id && !is_wp_error($id)) {
        update_post_meta($id, '_yoast_wpseo_title', 'Obrigado pelo contato - Work Digital');
        update_post_meta($id, '_wd_imp', 'obrigado');
        update_option('wd_obrigado_ok', 1);
    }
}, 20);
