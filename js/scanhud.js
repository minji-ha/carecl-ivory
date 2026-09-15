/* careCL — AI 스캔 HUD : 진행률 / 포인트 카운트 / 코드 스트림 / 좌표 태그 */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function hex(n) { var s = ''; while (n--) s += '0123456789ABCDEF'[Math.floor(Math.random() * 16)]; return s; }
  function rnd(a, b) { return (a + Math.random() * (b - a)).toFixed(3); }

  function run(hud) {
    var box = hud.parentElement;
    var pctEl = hud.querySelector('[data-scan-pct]');
    var ptsEl = hud.querySelector('[data-scan-pts]');
    var barEl = hud.querySelector('.scanhud__bar b');
    var codeEl = hud.querySelector('.scanhud__code');
    var line = hud.querySelector('.scanhud__line');

    /* 스캔 라인 이동 거리를 박스 높이에 맞춤 */
    function fit() { if (line) line.style.setProperty('--hud-h', (box.clientHeight + 90) + 'px'); hud.style.setProperty('--hud-h', (box.clientHeight + 90) + 'px'); }
    fit();
    window.addEventListener('resize', fit);

    /* 좌표 태그 : 포인트(.pt) 옆에 순환 표시 */
    var pts = [].slice.call(box.querySelectorAll('.pt'));
    var tags = pts.map(function (p) {
      var t = document.createElement('span');
      t.className = 'scanhud__tag';
      t.style.left = p.style.getPropertyValue('--x');
      t.style.top = p.style.getPropertyValue('--y');
      hud.appendChild(t);
      return t;
    });

    var pct = 0, lines = [];
    function tick() {
      pct += reduce ? 100 : (0.6 + Math.random() * 1.4);
      if (pct > 100) pct = 0;
      var p = Math.floor(pct);
      if (pctEl) pctEl.textContent = p < 10 ? '0' + p : p;
      if (barEl) barEl.style.width = p + '%';
      if (ptsEl) { var n = Math.min(22, Math.round(p / 100 * 22)); ptsEl.textContent = n < 10 ? '0' + n : n; }

      if (codeEl && Math.random() > 0.35) {
        lines.push('> ' + hex(4) + '  x ' + rnd(0.2, 0.8) + '  y ' + rnd(0.2, 0.9));
        if (lines.length > 4) lines.shift();
        codeEl.textContent = 'AGING MAP 22 / MORPHO-NET\n' + lines.join('\n');
      }

      if (tags.length && Math.random() > 0.55) {
        var i = Math.floor(Math.random() * tags.length);
        var tg = tags[i];
        tg.textContent = 'P' + (i + 1 < 10 ? '0' : '') + (i + 1) + ' · ' + rnd(0.1, 0.99);
        tg.classList.add('is-on');
        setTimeout(function () { tg.classList.remove('is-on'); }, 1100);
      }
    }
    tick();
    if (!reduce) setInterval(tick, 120);
  }

  [].forEach.call(document.querySelectorAll('.scanhud'), run);
})();
