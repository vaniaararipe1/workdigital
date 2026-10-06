<?php
/* Tema Work Digital */
if (!defined('ABSPATH')) exit;
define('WD_VER', '1.0.0');
define('WD_URI', get_template_directory_uri() . '/assets');
define('WD_DIR', get_template_directory());
define('WD_GTM', 'GTM-592RCDK9');
foreach (['setup', 'data', 'case-fields', 'author', 'seo', 'contact', 'redirects', 'consent', 'performance', 'front', 'import'] as $f) {
    require WD_DIR . "/inc/$f.php";
}
