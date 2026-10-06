<?php
/* Página do case: apresentação, as 7 artes (bloco 5 em vídeo) e o "Próximo case" */
if (!defined('ABSPATH')) exit;
the_post();
$id = get_the_ID();
$serv = wd_lines(wd_meta($id, 'servicos'));
$next = wd_next_case(get_post());
$arrow = '<svg viewBox="0 0 14 14" fill="none" aria-hidden="true"><path d="M12.0641 1.14239L.499 12.7061M1.9673.7061h9.5726c.53 0 .9591.4291.9591.9605v9.5712" stroke="currentColor" stroke-width="1.41181"/></svg>';
?>
        <div class="intro">
          <h1><?php the_title(); ?></h1>
          <div>
            <p><?php echo esc_html(wd_meta($id, 'p1')); ?></p>
            <p><?php echo esc_html(wd_meta($id, 'p2')); ?></p>
            <?php if (wd_meta($id, 'link_mostrar') === '1' && wd_meta($id, 'link')) : ?>
            <a class="wd-work-cta wd-cta cta" href="<?php echo esc_url(wd_meta($id, 'link')); ?>" target="_blank" rel="noopener"><span>VER PROJETO NO AR</span><?php echo $arrow; ?></a>
            <?php endif; ?>
          </div>
          <div>
            <h2>Serviços</h2>
            <ul><?php foreach ($serv as $s) echo '<li>' . esc_html($s) . '</li>'; ?></ul>
          </div>
        </div>
<?php
foreach (WD_BLOCKS as $n => [$file, $cls, $w, $h, $cap, $eager]) {
    $img = (int) wd_meta($id, 'm' . $n);
    $alt = $img ? (string) get_post_meta($img, '_wp_attachment_image_alt', true) : '';
    if ($n === '05') {
        $srcs = '';
        foreach (['webm' => 'v05_webm', 'mp4' => 'v05_mp4'] as $x => $k) { $u = wd_att_url(wd_meta($id, $k)); if ($u) $srcs .= '<source data-src="' . esc_url($u) . '" type="video/' . $x . '">'; }
        if (!$srcs) continue;
        $poster = $img ? ' poster="' . esc_url(wp_get_attachment_url($img)) . '"' : '';
        $inner = '<video class="case-video" muted loop playsinline preload="none"' . $poster . ' width="' . $w . '" height="' . $h . '" aria-label="' . esc_attr($alt) . '">' . $srcs . '</video>';
    } else {
        if (!$img) continue;
        // imagem original como maior versão; as menores servem às telas menores
        $inner = wp_get_attachment_image($img, 'full', false, ['alt' => $alt, 'decoding' => 'async', 'loading' => $eager ? 'eager' : 'lazy',
            'sizes' => str_contains($cls, 'full') ? '(max-width: 900px) 100vw, 60vh' : '(max-width: 900px) 100vw, 130vh']);
    }
    $legenda = $cap ? wd_meta($id, 'legenda_' . $n) : '';
    if ($legenda) $inner .= '<span class="cap">' . esc_html($legenda) . '</span>';
    echo '<div class="m ' . esc_attr($cls) . '">' . $inner . "</div>\n        ";
}
if ($next) : ?>
        <a class="next" href="<?php echo esc_url(get_permalink($next)); ?>" id="next" data-slug="<?php echo esc_attr($next->post_name); ?>" aria-label="Próximo case: <?php echo esc_attr(get_the_title($next)); ?>">
          <div class="big">Próximo case</div>
          <div class="bottom"><span><?php echo esc_html(get_the_title($next)); ?></span><i></i><b>→</b></div>
        </a>
<?php endif;
