<?php
/* Página /bio/: quem assina os artigos */
if (!defined('ABSPATH')) exit;
$u = wd_bio_user();
$photo = $u ? wd_user_img($u, 'wd_foto', 'large') : '';
$sign = $u ? wd_user_img($u, 'wd_assinatura', 'medium') : '';
$posts = $u ? get_posts(['author' => $u->ID, 'numberposts' => 6]) : [];
?>
  <section class="wd-bio wrap">
    <div class="wd-bio-head">
      <?php if ($photo) : ?><img class="wd-bio-photo" src="<?php echo esc_url($photo); ?>" alt="<?php echo esc_attr($u->display_name); ?>" width="320" height="320"><?php endif; ?>
      <div>
        <p class="up grad">Quem escreve</p>
        <h1><?php echo esc_html($u ? $u->display_name : 'Work Digital'); ?></h1>
        <?php $cargo = $u ? get_user_meta($u->ID, 'wd_cargo', true) : ''; if ($cargo) : ?><p class="wd-bio-role"><?php echo esc_html($cargo); ?></p><?php endif; ?>
        <ul class="wd-bio-social">
          <?php foreach (['wd_linkedin' => 'LinkedIn', 'wd_instagram' => 'Instagram'] as $k => $l) { $v = $u ? get_user_meta($u->ID, $k, true) : ''; if ($v) echo '<li><a href="' . esc_url($v) . '" target="_blank" rel="noopener me">' . $l . '</a></li>'; } ?>
        </ul>
      </div>
    </div>
    <div class="wd-bio-text"><?php echo $u ? wpautop(wp_kses_post(get_the_author_meta('description', $u->ID))) : ''; ?>
      <?php if ($sign) : ?><img class="wd-bio-sign" src="<?php echo esc_url($sign); ?>" alt="Assinatura de <?php echo esc_attr($u->display_name); ?>"><?php endif; ?>
    </div>
    <?php if ($posts) : ?>
    <h2 class="wd-bio-h2">Artigos</h2>
    <ul class="wd-bio-posts"><?php foreach ($posts as $p) : ?><li><a href="<?php echo esc_url(get_permalink($p)); ?>"><span><?php echo esc_html(wd_date($p)); ?></span><?php echo esc_html(get_the_title($p)); ?></a></li><?php endforeach; ?></ul>
    <?php endif; ?>
  </section>
<?php
if ($u) {
    $same = array_values(array_filter([get_user_meta($u->ID, 'wd_linkedin', true), get_user_meta($u->ID, 'wd_instagram', true)]));
    wd_ld(['@context' => 'https://schema.org', '@type' => 'ProfilePage', 'mainEntity' => array_filter(['@type' => 'Person', 'name' => $u->display_name,
        'jobTitle' => get_user_meta($u->ID, 'wd_cargo', true) ?: null, 'image' => $photo ?: null, 'sameAs' => $same ?: null,
        'worksFor' => ['@type' => 'Organization', 'name' => 'Work Digital', 'url' => home_url('/')]])]);
}
