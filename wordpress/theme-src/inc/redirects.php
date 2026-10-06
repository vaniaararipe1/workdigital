<?php
/* Redirecionamentos das URLs do site antigo (redirecionamentos.csv: origem,destino,codigo) */
if (!defined('ABSPATH')) exit;

add_action('template_redirect', function () {
    if (!is_404()) return;
    $path = '/' . trim(strtok($_SERVER['REQUEST_URI'] ?? '', '?'), '/') . '/';
    if ($path === '//') return;
    $file = WD_DIR . '/redirecionamentos.csv';
    if (!is_readable($file)) return;
    $h = fopen($file, 'r'); fgetcsv($h);
    while (($row = fgetcsv($h)) !== false) {
        if (count($row) < 2) continue;
        if (rtrim($row[0], '/') . '/' === $path) { fclose($h); wp_redirect(wd_url(ltrim($row[1], '/')), (int) ($row[2] ?? 301) ?: 301); exit; }
    }
    fclose($h);
}, 1);
