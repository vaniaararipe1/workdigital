<?php
/* Página comum (ex.: Política de privacidade, Contato) */
if (!defined('ABSPATH')) exit;
while (have_posts()) : the_post(); ?>
  <section class="wd-page wrap">
    <h1><?php the_title(); ?></h1>
    <div class="wd-page-body"><?php the_content(); ?></div>
  </section>
<?php endwhile;
