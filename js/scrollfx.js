/* =========================================================
   careCL — 메인 스크롤 연출 모음
   · lines  : 제목을 줄 단위로 마스크 리빌
   · up     : 아래에서 떠오르며 흐림이 걷힘 (순차)
   · zoom   : 스크롤에 따라 배경이 서서히 제 크기로
   · para   : 스크롤에 따라 느리게 따라오는 패럴랙스
   ========================================================= */
(function () {
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── 1. 제목 줄 단위 마스크 ── */
  function splitLines(el) {
    if (el.dataset.fxReady) return;
    var html = el.innerHTML.split(/<br\s*\/?>/i);
    el.innerHTML = html.map(function (line, i) {
      return '<span class="fx-line"><span class="fx-line__in" style="--d:' +
             (i * 110) + 'ms">' + line + '</span></span>';
    }).join('');
    el.dataset.fxReady = '1';
  }

  /* ── 2. 관찰 대상 수집 ── */
  var lineTargets = [].slice.call(document.querySelectorAll('[data-fx="lines"]'));
  var upGroups = [].slice.call(document.querySelectorAll('[data-fx-group]'));
  var upTargets = [].slice.call(document.querySelectorAll('[data-fx="up"]'));

  lineTargets.forEach(splitLines);

  upGroups.forEach(function (g) {
    [].slice.call(g.children).forEach(function (c, i) {
      c.classList.add('fx-up');
      c.style.setProperty('--d', (i * 90) + 'ms');
    });
  });
  upTargets.forEach(function (el) { el.classList.add('fx-up'); });

  if (reduce) {
    document.querySelectorAll('.fx-up').forEach(function (e) { e.classList.add('is-in'); });
    lineTargets.forEach(function (e) { e.classList.add('is-in'); });
    return;
  }

  /* ── 3. 등장 감지 (스크롤 기준, 부드러운 스크롤과 무관하게 동작) ── */
  var watch = lineTargets.concat([].slice.call(document.querySelectorAll('.fx-up')));
  function check() {
    if (!watch.length) return;
    var vh = window.innerHeight;
    for (var i = watch.length - 1; i >= 0; i--) {
      var el = watch[i];
      var r = el.getBoundingClientRect();
      if (r.top < vh * 0.92 && r.bottom > 0) {
        el.classList.add('is-in');
        watch.splice(i, 1);
      }
    }
  }
  window.addEventListener('scroll', check, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', check);
  window.addEventListener('resize', check);
  check();

  /* ── 4. 패럴랙스 · 줌 ── */
  var paras = [].slice.call(document.querySelectorAll('[data-fx-para]'));
  var zooms = [].slice.call(document.querySelectorAll('[data-fx-zoom]'));

  function frame() {
    var vh = window.innerHeight;
    paras.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var p = (r.top + r.height / 2 - vh / 2) / vh;          // -1 ~ 1
      var amt = parseFloat(el.dataset.fxPara) || 14;
      el.style.transform = 'translate3d(0,' + (-p * amt).toFixed(2) + '%,0)';
    });
    zooms.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.bottom < -200 || r.top > vh + 200) return;
      var p = 1 - Math.max(0, Math.min(1, (r.top + r.height * 0.2) / vh));
      var s = 1.16 - p * 0.16;
      el.style.transform = 'scale(' + s.toFixed(3) + ')';
    });
  }
  window.addEventListener('scroll', frame, { passive: true });
  window.addEventListener('resize', frame);
  (function loop() { frame(); check(); requestAnimationFrame(loop); })();
  frame();
})();
