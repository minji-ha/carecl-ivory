/* careCL — 전체메뉴(메가 메뉴) 토글 */
(function () {
  'use strict';
  var btn = document.getElementById('allMenuBtn');
  var mega = document.getElementById('megaMenu');
  var close = document.getElementById('megaClose');
  if (!btn || !mega) return;

  function open() {
    document.body.classList.add('mega-open');
    mega.setAttribute('aria-hidden', 'false');
  }
  function shut() {
    document.body.classList.remove('mega-open');
    mega.setAttribute('aria-hidden', 'true');
  }

  btn.addEventListener('click', function () {
    document.body.classList.contains('mega-open') ? shut() : open();
  });
  if (close) close.addEventListener('click', shut);
  mega.addEventListener('click', function (e) { if (e.target === mega) shut(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') shut(); });
  Array.prototype.forEach.call(mega.querySelectorAll('a'), function (a) {
    a.addEventListener('click', shut);
  });
})();

/* ── 서브 2뎁스 탭 : 같은 페이지 앵커일 때 현재 섹션 표시 ── */
(function () {
  var bar = document.getElementById('subMenu');
  if (!bar) return;
  var links = [].slice.call(bar.querySelectorAll('a'));
  var page = location.pathname.split('/').pop() || 'index.html';
  var map = [];
  links.forEach(function (a) {
    var href = a.getAttribute('href') || '';
    var i = href.indexOf('#');
    if (i < 0) return;
    var base = href.slice(0, i);
    if (base && base !== page) return;
    var el = document.getElementById(href.slice(i + 1));
    if (el) map.push({ a: a, el: el });
  });
  if (map.length < 2) return;

  function sync() {
    var line = window.scrollY + 220;
    var cur = map[0];
    map.forEach(function (m) {
      if (m.el.getBoundingClientRect().top + window.scrollY <= line) cur = m;
    });
    links.forEach(function (a) { a.classList.remove('is-active'); });
    cur.a.classList.add('is-active');
  }
  var tick = false;
  window.addEventListener('scroll', function () {
    if (tick) return;
    tick = true;
    requestAnimationFrame(function () { sync(); tick = false; });
  }, { passive: true });
  sync();
})();
