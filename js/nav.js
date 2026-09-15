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
