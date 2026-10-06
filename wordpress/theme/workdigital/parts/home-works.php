<?php
/* Home, seção Works: os 4 cases marcados como destaque (posição 1 a 4) */
if (!defined('ABSPATH')) exit;
foreach (wd_home_cases() as $c) :
    [$w, $h] = wd_att_dims(wd_meta($c->ID, 'home_webp'));
    if (!$w) { $w = 840; $h = 1600; } ?>
<a class="wd-works-card" style="--wd-ar:<?php echo (int) $w; ?> / <?php echo (int) $h; ?>" href="<?php echo esc_url(get_permalink($c)); ?>">
    <h3><?php echo esc_html(get_the_title($c)); ?></h3>
    <div class="wd-works-media" data-thumb="<?php echo esc_attr($c->post_name); ?>-home" data-w="<?php echo (int) $w; ?>" data-h="<?php echo (int) $h; ?>"><div class="vm"></div></div>
    <p class="wd-works-description"><?php echo esc_html(wd_meta($c->ID, 'home_desc') ?: wd_meta($c->ID, 'frase')); ?></p>
   </a>
<?php endforeach;
