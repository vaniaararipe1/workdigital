<?php
/* Página não encontrada */
if (!defined('ABSPATH')) exit; ?>
  <section class="wd-page wd-404 wrap">
    <p class="up grad">Erro 404</p>
    <h1>Página não encontrada</h1>
    <p>O endereço pode ter mudado. Veja por onde continuar:</p>
    <ul class="wd-404-links">
      <li><a href="<?php echo esc_url(home_url('/')); ?>">Home</a></li>
      <li><a href="<?php echo esc_url(wd_url('solucoes/')); ?>">Soluções e planos</a></li>
      <li><a href="<?php echo esc_url(wd_url('cases/')); ?>">Cases</a></li>
      <li><a href="<?php echo esc_url(wd_url('blog/')); ?>">Blog</a></li>
    </ul>
  </section>
