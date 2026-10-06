<?php
/* Campos do case no painel: textos, serviços, as 7 artes, o vídeo do bloco 5, thumbs e destaque na home */
if (!defined('ABSPATH')) exit;

function wd_case_fields() {
    $media = [];
    foreach (WD_BLOCKS as $n => $b) $media['m' . $n] = ['Bloco ' . (int) $n . ' — ' . $b[0] . ($n === '05' ? ' (imagem de capa do vídeo)' : ''), 'image'];
    return [
        'Página do case' => [
            'projeto' => ['Tipo de projeto (ex.: Site institucional)', 'text'],
            'p1' => ['Parágrafo 1', 'textarea'],
            'p2' => ['Parágrafo 2', 'textarea'],
            'servicos' => ['Serviços (um por linha)', 'textarea'],
            'link' => ['Link do projeto no ar', 'url'],
            'link_mostrar' => ['Mostrar o botão "Ver projeto no ar"', 'checkbox'],
            'legenda_01' => ['Legenda do bloco 1', 'text'],
            'legenda_03' => ['Legenda do bloco 3', 'text'],
            'legenda_04' => ['Legenda do bloco 4', 'text'],
        ],
        'Artes (o texto alternativo de cada imagem é editado na Biblioteca de mídia)' => $media + [
            'v05_mp4' => ['Bloco 5 — vídeo MP4', 'video'],
            'v05_webm' => ['Bloco 5 — vídeo WebM', 'video'],
        ],
        'Card na página de Cases' => [
            'frase' => ['Frase do card', 'text'],
            'formato' => ['Formato do card', 'select', ['grande' => 'Grande', 'medio' => 'Médio', 'pequeno' => 'Pequeno']],
            'thumb_webp' => ['Thumb — imagem (WebP)', 'image'],
            'thumb_mp4' => ['Thumb — vídeo MP4', 'video'],
            'thumb_webm' => ['Thumb — vídeo WebM', 'video'],
            'thumb_anim' => ['Thumb — imagem animada de reserva (WebP)', 'image'],
        ],
        'Destaque na home (seção Works)' => [
            'home_slot' => ['Posição na home', 'select', ['0' => 'Não aparece', '1' => '1 — alto, à esquerda', '2' => '2 — largo', '3' => '3 — quadrado', '4' => '4 — quadrado']],
            'home_desc' => ['Descrição no card da home', 'text'],
            'home_webp' => ['Home — imagem (WebP)', 'image'],
            'home_mp4' => ['Home — vídeo MP4', 'video'],
            'home_webm' => ['Home — vídeo WebM', 'video'],
            'home_anim' => ['Home — imagem animada de reserva (WebP)', 'image'],
        ],
    ];
}

add_action('add_meta_boxes_case', function () {
    add_meta_box('wd-case', 'Conteúdo do case', 'wd_case_box', 'case', 'normal', 'high');
});

function wd_case_box($post) {
    wp_nonce_field('wd_case_save', 'wd_case_nonce');
    echo '<style>.wd-f{display:grid;grid-template-columns:260px 1fr;gap:6px 16px;align-items:start;margin:0 0 10px}.wd-f label{font-weight:600;padding-top:6px}.wd-f input[type=text],.wd-f input[type=url],.wd-f textarea,.wd-f select{width:100%}.wd-f textarea{min-height:70px}.wd-sec{margin:22px 0 10px;padding-top:12px;border-top:1px solid #ddd;font-size:14px}.wd-pick{display:flex;gap:10px;align-items:center}.wd-pick img{max-height:60px;max-width:110px;border-radius:4px}.wd-pick .n{color:#666;font-size:12px}</style>';
    foreach (wd_case_fields() as $sec => $fields) {
        echo '<h3 class="wd-sec">' . esc_html($sec) . '</h3>';
        foreach ($fields as $k => $f) {
            $v = get_post_meta($post->ID, 'wd_' . $k, true);
            $id = 'wd_' . $k;
            echo '<div class="wd-f"><label for="' . $id . '">' . esc_html($f[0]) . '</label><div>';
            switch ($f[1]) {
                case 'textarea': echo '<textarea id="' . $id . '" name="' . $id . '">' . esc_textarea($v) . '</textarea>'; break;
                case 'checkbox': echo '<input type="checkbox" id="' . $id . '" name="' . $id . '" value="1"' . checked($v, '1', false) . '>'; break;
                case 'select':
                    echo '<select id="' . $id . '" name="' . $id . '">';
                    foreach ($f[2] as $ov => $ol) echo '<option value="' . esc_attr($ov) . '"' . selected((string) $v, (string) $ov, false) . '>' . esc_html($ol) . '</option>';
                    echo '</select>'; break;
                case 'image': case 'video':
                    $url = $v ? wp_get_attachment_url((int) $v) : '';
                    $prev = $f[1] === 'image' && $url ? '<img src="' . esc_url(wp_get_attachment_image_url((int) $v, 'thumbnail') ?: $url) . '" alt="">' : '';
                    echo '<div class="wd-pick" data-type="' . $f[1] . '"><input type="hidden" id="' . $id . '" name="' . $id . '" value="' . esc_attr($v) . '">'
                        . '<span class="p">' . $prev . '</span><span class="n">' . esc_html($url ? basename($url) : 'Nenhum arquivo') . '</span>'
                        . '<button type="button" class="button wd-choose">Escolher</button><button type="button" class="button-link wd-clear">Remover</button></div>';
                    break;
                default: echo '<input type="' . ($f[1] === 'url' ? 'url' : 'text') . '" id="' . $id . '" name="' . $id . '" value="' . esc_attr($v) . '">';
            }
            echo '</div></div>';
        }
    }
}

add_action('admin_enqueue_scripts', function ($hook) {
    if (!in_array($hook, ['post.php', 'post-new.php'], true) || get_post_type() !== 'case') return;
    wp_enqueue_media();
    wp_add_inline_script('jquery-core', "jQuery(function($){
      $(document).on('click','.wd-choose',function(){const box=$(this).closest('.wd-pick'),type=box.data('type');
        const fr=wp.media({title:'Escolher arquivo',multiple:false,library:{type:type}});
        fr.on('select',function(){const a=fr.state().get('selection').first().toJSON();box.find('input').val(a.id);box.find('.n').text(a.filename);
          box.find('.p').html(type==='image'?'<img src=\"'+((a.sizes&&a.sizes.thumbnail)?a.sizes.thumbnail.url:a.url)+'\" alt=\"\">':'');});fr.open();});
      $(document).on('click','.wd-clear',function(){const box=$(this).closest('.wd-pick');box.find('input').val('');box.find('.n').text('Nenhum arquivo');box.find('.p').empty();});
    });");
});

add_action('save_post_case', function ($post_id) {
    if (!isset($_POST['wd_case_nonce']) || !wp_verify_nonce($_POST['wd_case_nonce'], 'wd_case_save')) return;
    if (defined('DOING_AUTOSAVE') && DOING_AUTOSAVE) return;
    if (!current_user_can('edit_post', $post_id)) return;
    foreach (wd_case_fields() as $fields) foreach ($fields as $k => $f) {
        $name = 'wd_' . $k; $raw = wp_unslash($_POST[$name] ?? '');
        $val = match ($f[1]) {
            'textarea' => sanitize_textarea_field($raw),
            'url' => esc_url_raw($raw),
            'checkbox' => $raw === '1' ? '1' : '',
            'image', 'video' => $raw === '' ? '' : (string) absint($raw),
            default => sanitize_text_field($raw),
        };
        update_post_meta($post_id, $name, $val);
    }
});

// lista de cases no painel: ordem e destaque na home
add_filter('manage_case_posts_columns', fn($c) => array_slice($c, 0, 2) + ['wd_ordem' => 'Ordem', 'wd_home' => 'Home'] + $c);
add_action('manage_case_posts_custom_column', function ($col, $id) {
    if ($col === 'wd_ordem') echo (int) get_post_field('menu_order', $id);
    if ($col === 'wd_home') { $s = (int) get_post_meta($id, 'wd_home_slot', true); echo $s ? 'Posição ' . $s : '—'; }
}, 10, 2);
