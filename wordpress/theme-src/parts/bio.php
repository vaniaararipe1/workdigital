<?php
/* Página /bio/: quem assina os artigos */
if (!defined('ABSPATH')) exit;
$u = wd_bio_user();
$photo = $u ? wd_user_img($u, 'wd_foto', 'large') : '';
$sign = $u ? wd_user_img($u, 'wd_assinatura', 'medium') : '';
$posts = $u ? get_posts(['author' => $u->ID, 'numberposts' => 6]) : [];
$bio = $u ? wd_bio_data($u) : ['name' => 'Work Digital', 'cargo' => '', 'bio' => '', 'links' => []];
?>
  <section class="wd-bio wrap">
    <div class="wd-bio-head">
      <?php if ($photo) : ?><img class="wd-bio-photo" src="<?php echo esc_url($photo); ?>" alt="<?php echo esc_attr($u->display_name); ?>" width="320" height="320"><?php endif; ?>
      <div>
        <p class="up grad">Quem escreve</p>
        <h1><?php echo esc_html($bio['name']); ?></h1>
        <?php if ($bio['cargo']) : ?><p class="wd-bio-role"><?php echo esc_html($bio['cargo']); ?></p><?php endif; ?>
        <ul class="wd-bio-social">
          <?php foreach ($bio['links'] as $l => $v) echo '<li><a href="' . esc_url($v) . '" target="_blank" rel="noopener me">' . esc_html($l) . '</a></li>'; ?>
        </ul>
      </div>
    </div>
    <div class="wd-bio-text"><?php echo wpautop(wp_kses_post($bio['bio'])); ?>
      <?php if ($sign) : ?><img class="wd-bio-sign" src="<?php echo esc_url($sign); ?>" alt="Assinatura de <?php echo esc_attr($u->display_name); ?>"><?php endif; ?>
    </div>
    <?php if ($posts) : ?>
    <h2 class="wd-bio-h2">Artigos</h2>
    <ul class="wd-bio-posts"><?php foreach ($posts as $p) : ?><li><a href="<?php echo esc_url(get_permalink($p)); ?>"><span><?php echo esc_html(wd_date($p)); ?></span><?php echo esc_html(get_the_title($p)); ?></a></li><?php endforeach; ?></ul>
    <?php endif; ?>
  </section>
<?php
if ($u) {
    $same = array_values($bio['links']);
    wd_ld(['@context' => 'https://schema.org', '@type' => 'ProfilePage', 'mainEntity' => array_filter(['@type' => 'Person', 'name' => $bio['name'],
        'jobTitle' => $bio['cargo'] ?: null, 'image' => $photo ?: null, 'sameAs' => $same ?: null,
        'worksFor' => ['@type' => 'Organization', 'name' => 'Work Digital', 'url' => home_url('/')]])]);
}
