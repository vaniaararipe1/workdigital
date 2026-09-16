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
      if (window.innerWidth <= 720) {
        e.preventDefault();
        link.parentElement.classList.toggle('is-open');
      }
    });
  });

  document.querySelectorAll('.tabs-row').forEach(function (tabs) {
    tabs.querySelectorAll('.tab-btn').forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.querySelectorAll('.tab-btn').forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        var target = tab.getAttribute('data-target');
        var group = tabs.parentElement.querySelectorAll('.tab-panel');
        group.forEach(function (p) { p.style.display = 'none'; });
        var el = document.getElementById(target);
        if (el) el.style.display = 'block';
      });
    });
  });
});
