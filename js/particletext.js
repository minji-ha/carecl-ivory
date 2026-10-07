/* =========================================================
   careCL — 파티클 타이포그래피
   · 흩어진 빛 입자가 모여 'careCL' 을 만든다
   · 커서/터치를 가져가면 입자가 밀려났다가 스프링처럼 복귀
   · 주기적으로 스캔 광선이 지나가며 입자를 밝힘
   · 클릭하면 폭발 → 재조립
   ========================================================= */
(function () {
  'use strict';
  var host = document.getElementById('brandParticles');
  if (!host) return;

  var cv = host.querySelector('canvas');
  var ctx = cv.getContext('2d');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var W, H, dpr, parts = [], dust = [], mouse = { x: -9999, y: -9999, on: false };
  var scanX = -200, t = 0, running = false;

  function rand(a, b) { return a + Math.random() * (b - a); }

  function sampleText() {
    var off = document.createElement('canvas');
    off.width = W; off.height = H;
    var o = off.getContext('2d');
    var size = Math.min(W * 0.29, 180);
    o.fillStyle = '#000';
    o.textAlign = 'center';
    o.textBaseline = 'middle';
    o.font = "600 " + (size * 0.92) + "px Inter, 'Noto Sans KR', sans-serif";
    o.fillText('careCL', W / 2, H * 0.46);

    var data = o.getImageData(0, 0, W, H).data;
    var step = W < 420 ? 2 : 3;
    var pts = [];
    for (var y = 0; y < H; y += step) {
      for (var x = 0; x < W; x += step) {
        if (data[(y * W + x) * 4 + 3] > 140) pts.push([x, y]);
      }
    }
    return pts;
  }

  function build() {
    var pts = sampleText();
    var old = parts;
    parts = pts.map(function (p, i) {
      var q = old[i];
      return {
        tx: p[0], ty: p[1],
        x: q ? q.x : rand(0, W), y: q ? q.y : rand(0, H),
        vx: 0, vy: 0,
        r: rand(0.9, 1.6),
        seed: Math.random() * Math.PI * 2,
        glow: 0, hot: 0
      };
    });
    dust = [];
    for (var i = 0; i < 70; i++) {
      dust.push({ x: rand(0, W), y: rand(0, H), r: rand(0.5, 1.4), s: rand(0.15, 0.5), a: rand(0.15, 0.5) });
    }
  }

  function resize() {
    var r = host.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = Math.round(r.width); H = Math.round(r.height);
    cv.width = W * dpr; cv.height = H * dpr;
    cv.style.width = W + 'px'; cv.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    build();
  }

  function explode() {
    parts.forEach(function (p) {
      var a = Math.random() * Math.PI * 2, f = rand(8, 26);
      p.vx += Math.cos(a) * f; p.vy += Math.sin(a) * f;
    });
  }

  function frame() {
    requestAnimationFrame(frame);
    if (!running) return;
    t += 1;

    ctx.clearRect(0, 0, W, H);

    /* 배경 먼지 입자 */
    for (var d = 0; d < dust.length; d++) {
      var u = dust[d];
      u.y -= u.s; if (u.y < -4) { u.y = H + 4; u.x = rand(0, W); }
      ctx.beginPath(); ctx.arc(u.x, u.y, u.r, 0, 6.283);
      ctx.fillStyle = 'rgba(217,203,182,' + u.a + ')';
      ctx.fill();
    }

    /* 스캔 광선 */
    scanX += reduce ? 0 : 5;
    if (scanX > W + 260) scanX = -260 - Math.random() * 400;
    var sg = ctx.createLinearGradient(scanX - 90, 0, scanX + 90, 0);
    sg.addColorStop(0, 'rgba(217,203,182,0)');
    sg.addColorStop(0.5, 'rgba(217,203,182,.10)');
    sg.addColorStop(1, 'rgba(217,203,182,0)');
    ctx.fillStyle = sg;
    ctx.fillRect(scanX - 90, 0, 180, H);

    /* 커서 빛무리 */
    if (mouse.on) {
      var hg = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 120);
      hg.addColorStop(0, 'rgba(214,138,86,.16)');
      hg.addColorStop(0.55, 'rgba(214,138,86,.05)');
      hg.addColorStop(1, 'rgba(214,138,86,0)');
      ctx.fillStyle = hg;
      ctx.fillRect(mouse.x - 120, mouse.y - 120, 240, 240);
    }

    /* 글자 입자 */
    var R = 90, R2 = R * R;
    for (var i = 0; i < parts.length; i++) {
      var p = parts[i];
      var wob = reduce ? 0 : Math.sin(t * 0.03 + p.seed) * 0.6;
      var ax = (p.tx + wob - p.x) * 0.055;
      var ay = (p.ty + Math.cos(t * 0.025 + p.seed) * 0.6 - p.y) * 0.055;

      /* 마우스 : 흩어지는 대신 커서 둘레를 천천히 도는 소용돌이 */
      var hot = 0;
      if (mouse.on) {
        var dx = p.x - mouse.x, dy = p.y - mouse.y, dd = dx * dx + dy * dy;
        if (dd < R2) {
          var len = Math.sqrt(dd) || 1;
          hot = 1 - len / R;
          var f = hot * hot;
          ax += (-dy / len) * f * 2.6 + (dx / len) * f * 0.9;   // 접선 회전 + 아주 약한 밀어내기
          ay += (dx / len) * f * 2.6 + (dy / len) * f * 0.9;
        }
      }
      p.hot += (hot - p.hot) * 0.12;
      p.vx = (p.vx + ax) * 0.84;
      p.vy = (p.vy + ay) * 0.84;
      p.x += p.vx; p.y += p.vy;

      var near = Math.abs(p.x - scanX) < 70 ? 1 - Math.abs(p.x - scanX) / 70 : 0;
      p.glow += (near - p.glow) * 0.2;
      var speed = Math.min(1, (Math.abs(p.vx) + Math.abs(p.vy)) / 6);

      /* 좌→우 스카이 그라데이션 */
      var k = p.tx / W;
      var h = p.hot || 0;
      var cr = Math.round((236 - 36 * k + 19 * p.glow) * (1 - h) + 214 * h);
      var cg = Math.round((226 - 42 * k + 29 * p.glow) * (1 - h) + 138 * h);
      var cb = Math.round((210 - 56 * k + 45 * p.glow) * (1 - h) + 86 * h);
      ctx.fillStyle = 'rgba(' + Math.min(255, cr) + ',' + Math.min(255, cg) + ',' + Math.min(255, cb) + ',' + (0.86 + p.glow * 0.14) + ')';
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r + p.glow * 1.1 + speed * 0.8 + (p.hot || 0) * 1.3, 0, 6.283);
      ctx.fill();
    }
  }

  function toLocal(e) {
    var r = cv.getBoundingClientRect();
    var pt = e.touches ? e.touches[0] : e;
    mouse.x = pt.clientX - r.left; mouse.y = pt.clientY - r.top; mouse.on = true;
  }
  host.addEventListener('mousemove', toLocal);
  host.addEventListener('touchmove', function (e) { toLocal(e); }, { passive: true });
  host.addEventListener('mouseleave', function () { mouse.on = false; });
  host.addEventListener('touchend', function () { mouse.on = false; });
  host.addEventListener('click', explode);

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { running = en[0].isIntersecting; }, { rootMargin: '80px' }).observe(host);
  } else { running = true; }

  var ready = (document.fonts && document.fonts.load) ? document.fonts.load('600 160px Inter') : Promise.resolve();
  ready.then(function () {
    resize(); frame();
    if ('ResizeObserver' in window) new ResizeObserver(function () { resize(); }).observe(host);
    else window.addEventListener('resize', resize);
  });
})();
