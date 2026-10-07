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

/* ── 페이지 상단 3뎁스 앵커 바 : 현재 섹션 표시 ── */
(function () {
  var bar = document.getElementById('anchorNav');
  if (!bar) return;
  var links = [].slice.call(bar.querySelectorAll('a'));
  var map = [];
  links.forEach(function (a) {
    var href = a.getAttribute('href') || '';
    var i = href.indexOf('#');
    if (i < 0) return;
    var base = href.slice(0, i);
    if (base && base !== location.pathname.split('/').pop()) return;
    var el = document.getElementById(href.slice(i + 1));
    if (el) map.push({ a: a, el: el });
  });
  if (!map.length) return;

  function sync() {
    var line = window.scrollY + bar.getBoundingClientRect().bottom + 80;
    var cur = null;
    map.forEach(function (m) {
      if (m.el.getBoundingClientRect().top + window.scrollY <= line) cur = m;
    });
    links.forEach(function (a) { a.classList.remove('is-active'); });
    if (cur) {
      // 같은 앵커를 가리키는 링크가 여러 개면 첫 번째만 표시
      var first = map.filter(function (m) { return m.el === cur.el; })[0];
      first.a.classList.add('is-active');
    }
  }
  var tick = false;
  window.addEventListener('scroll', function () {
    if (tick) return;
    tick = true;
    requestAnimationFrame(function () { sync(); tick = false; });
  }, { passive: true });
  sync();
})();
