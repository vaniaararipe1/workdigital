/*
 * Holy Crepe — Wireframes lo-fi
 * Comportamento mínimo apenas para demonstrar a colapsagem do menu
 * em hambúrguer no mobile (accordion de submenus) e as abas da
 * página de Cursos. Não representa a implementação final.
 */
document.addEventListener('DOMContentLoaded', function () {
  var hamburgerBtn = document.getElementById('hamburgerBtn');
  var navMenu = document.getElementById('navMenu');

  if (hamburgerBtn && navMenu) {
    hamburgerBtn.addEventListener('click', function () {
      navMenu.classList.toggle('is-open');
    });
  }

  document.querySelectorAll('.has-submenu > a').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        link.parentElement.classList.toggle('is-open');
      }
    });
  });

  document.querySelectorAll('.wf-tabs').forEach(function (tabs) {
    tabs.querySelectorAll('.wf-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.querySelectorAll('.wf-tab').forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        var targetId = tab.getAttribute('data-target');
        var panelGroup = tabs.parentElement.querySelectorAll('.wf-tab-panel');
        panelGroup.forEach(function (p) { p.style.display = 'none'; });
        var target = document.getElementById(targetId);
        if (target) target.style.display = 'block';
      });
    });
  });
});
