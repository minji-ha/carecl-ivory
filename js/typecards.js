/* =========================================================
   careCL — 6 AGING TYPES : 순차 등장 + 타입 바로가기 칩
   ========================================================= */
(function () {
  var wrapEl = document.querySelector('.typecards');
  if (!wrapEl) return;

  var cards = [].slice.call(wrapEl.querySelectorAll('.typecard'));
  if (!cards.length) return;

  /* 1) 순차 등장 */
  cards.forEach(function (c, i) { c.style.setProperty('--td', (i * 90) + 'ms'); });

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) {
    wrapEl.classList.add('js-anim');
    var shown = false;
    var show = function () {
      if (shown) return;
      shown = true;
      wrapEl.classList.add('is-in');
      window.removeEventListener('scroll', check);
    };
    var check = function () {
      var r = wrapEl.getBoundingClientRect();
      if (r.top < window.innerHeight * 0.92 && r.bottom > 0) show();
    };
    window.addEventListener('scroll', check, { passive: true });
    check();
    setTimeout(check, 400);
    setTimeout(show, 2500);          // 어떤 이유로든 감지가 안 되면 그냥 보여준다
  }

  /* 2) 타입 바로가기 칩 */
  var nav = document.createElement('nav');
  nav.className = 'typenav';
  cards.forEach(function (c, i) {
    var h = c.querySelector('h4');
    if (!h) return;
    var name = h.textContent.replace(/^\s*\d+\.\s*/, '').split(/\s+·\s+/)[0].trim();
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = (i + 1 < 10 ? '0' : '') + (i + 1) + '  ' + name;
    b.addEventListener('click', function () {
      var top = c.getBoundingClientRect().top + window.scrollY - 160;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
    nav.appendChild(b);
  });
  wrapEl.parentNode.insertBefore(nav, wrapEl);

  /* 3) 화면 중앙에 있는 카드를 칩에 표시 */
  var btns = [].slice.call(nav.querySelectorAll('button'));
  var tick = false;
  function sync() {
    var mid = window.innerHeight * 0.45;
    var best = -1, bestD = Infinity;
    cards.forEach(function (c, i) {
      var r = c.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      var d = Math.abs(r.top + r.height / 2 - mid);
      if (d < bestD) { bestD = d; best = i; }
    });
    btns.forEach(function (b, i) { b.classList.toggle('is-on', i === best); });
  }
  window.addEventListener('scroll', function () {
    if (tick) return;
    tick = true;
    requestAnimationFrame(function () { sync(); tick = false; });
  }, { passive: true });
  sync();
})();
