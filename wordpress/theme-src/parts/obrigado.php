<?php
/* Página /obrigado/: destino do formulário "Solicitar proposta" (conversão do Google Ads) */
if (!defined('ABSPATH')) exit; ?>
  <section class="wd-page wd-thanks wrap">
    <p class="up grad">Mensagem recebida</p>
    <h1>Obrigado pelo contato!</h1>
    <p class="wd-thanks-lead">Recebemos sua mensagem e nossa equipe já está analisando. Em breve entraremos em contato pelo e-mail ou telefone que você informou.</p>
    <p>Enquanto isso, conheça um pouco mais do nosso trabalho:</p>
    <ul class="wd-404-links">
      <li><a href="<?php echo esc_url(wd_url('cases/')); ?>">Veja os cases</a></li>
      <li><a href="<?php echo esc_url(wd_url('solucoes/')); ?>">Soluções e planos</a></li>
      <li><a href="<?php echo esc_url(wd_url('blog/')); ?>">Leia o blog</a></li>
    </ul>
    <p class="wd-thanks-wa">Tem pressa? Fale com a gente no <a href="https://wa.me/5511993916363" target="_blank" rel="noopener">WhatsApp: (11) 99391-6363</a>.</p>
  </section>
  <script>
  /* conversão: só conta quando a pessoa chegou aqui pelo formulário (recarregar a página não conta de novo) */
  (function(){var ok=false;try{ok=sessionStorage.getItem('wdLead')==='1';sessionStorage.removeItem('wdLead');}catch(e){}
  if(ok){window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'wd_lead',wd_form:'solicitar_proposta'});}})();
  </script>
