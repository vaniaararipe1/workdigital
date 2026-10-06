<?php
/* Home, seção Blog: sempre os 3 artigos mais recentes */
if (!defined('ABSPATH')) exit;
foreach (get_posts(['numberposts' => 3, 'post_status' => 'publish']) as $p) :
    $cat = wd_post_cat($p); ?>
      <article class="wd-blog-item">
        <a class="wd-blog-link" href="<?php echo esc_url(get_permalink($p)); ?>">
          <img class="wd-blog-image" loading="lazy" decoding="async" width="900" height="500" src="<?php echo esc_url(wd_post_img($p, 'wd-card')); ?>" alt="<?php echo esc_attr(wd_post_alt($p) ?: get_the_title($p)); ?>">
          <div class="wd-blog-content">
            <h3 class="wd-blog-article-title"><?php echo esc_html(get_the_title($p)); ?></h3>
            <p class="wd-blog-excerpt"><?php echo esc_html(get_the_excerpt($p)); ?></p>
            <div class="wd-blog-meta">
              <time datetime="<?php echo esc_attr(get_the_date('Y-m-d', $p)); ?>"><?php echo esc_html(wd_date($p, true)); ?></time>
              <?php if ($cat) : ?><span class="wd-blog-category"><?php echo esc_html($cat->name); ?></span><?php endif; ?>
            </div>
          </div>
          <span class="wd-blog-arrow" aria-hidden="true">
            <svg viewBox="0 0 14 14" fill="none"><path d="M12.065 1.142L.5 12.706M1.968 .706h9.573c.53 0 .959.429.959.961v9.571" stroke="currentColor" stroke-width="1.412"/></svg>
          </span>
        </a>
      </article>
<?php endforeach;
