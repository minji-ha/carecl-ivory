/* =========================================================
   careCL — 메인 진입 인트로
   0 → 100 카운트 + 전체 화면 물결치는 그리드
   ========================================================= */
(function () {
  var root = document.getElementById('intro');
  if (!root) return;

  function skip() {
    if (root.parentNode) root.parentNode.removeChild(root);
    document.body.classList.remove('is-intro');
  }

  /* 이번 방문에서 이미 봤다면 다시 띄우지 않는다.
     - 탭/창을 닫으면 초기화
     - 마지막 재생 후 2시간이 지나면 다시 재생
     - 주소 뒤에 ?intro=1 을 붙이면 언제든 다시 재생 (확인용) */
  var KEY = 'carecl_intro_at';
  var GAP = 2 * 60 * 60 * 1000;
  var force = /[?&]intro=1/.test(location.search);
  if (!force) {
    var last = 0;
    try { last = parseInt(sessionStorage.getItem(KEY) || '0', 10) || 0; } catch (e) { last = 0; }
    if (last && (Date.now() - last) < GAP) { skip(); return; }
  }
  try { sessionStorage.setItem(KEY, String(Date.now())); } catch (e) {}

  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { skip(); return; }

  var canvas = root.querySelector('.intro__grid');
  var ctx = canvas.getContext('2d');
  var numEl = root.querySelector('.intro__num');
  var barEl = root.querySelector('.intro__bar i');

  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0;

  function resize() {
    W = window.innerWidth;
    H = window.innerHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  window.addEventListener('resize', resize);

  /* ── 물결치는 그리드 ── */
  var COLS = 13;          // 가로 선 개수 — 넓은 그리드
  var ROWS = 8;           // 세로 선 개수 — 넓은 그리드
  var t = 0;
  var progress = 0;       // 0 → 1 (카운트와 연동)

  function wave(x, y, time) {
    // 두 개의 사인파를 겹쳐 자연스러운 물결을 만든다
    var d = Math.sqrt((x - 0.5) * (x - 0.5) + (y - 0.5) * (y - 0.5));
    return (Math.sin(x * 6.0 + time * 1.1) * 12 +
            Math.sin(y * 5.0 - time * 0.9) * 10 +
            Math.sin(d * 11.0 - time * 1.6) * 16) * (0.35 + progress * 0.65);
  }

  function point(ix, iy, time) {
    var u = ix / COLS;
    var v = iy / ROWS;
    var pad = 0.06;
    var x = (pad + u * (1 - pad * 2)) * W;
    var y = (pad + v * (1 - pad * 2)) * H;
    return [x + wave(u, v, time) * 0.6, y + wave(v, u, time + 1.7)];
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    ctx.lineWidth = 1;

    // 진행률만큼 그리드를 그려 나간다
    var shown = 0.12 + progress * 0.88;

    for (var iy = 0; iy <= ROWS; iy++) {
      var rowAlpha = Math.max(0, Math.min(1, (shown - iy / ROWS) * 3.2));
      if (rowAlpha <= 0) continue;
      ctx.strokeStyle = 'rgba(196,106,58,' + (0.14 + rowAlpha * 0.26) + ')';
      ctx.beginPath();
      for (var ix = 0; ix <= COLS; ix++) {
        var p = point(ix, iy, t);
        if (ix === 0) ctx.moveTo(p[0], p[1]); else ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();
    }

    for (var ix2 = 0; ix2 <= COLS; ix2++) {
      var colAlpha = Math.max(0, Math.min(1, (shown - ix2 / COLS) * 3.2));
      if (colAlpha <= 0) continue;
      ctx.strokeStyle = 'rgba(43,39,36,' + (0.07 + colAlpha * 0.15) + ')';
      ctx.beginPath();
      for (var iy2 = 0; iy2 <= ROWS; iy2++) {
        var q = point(ix2, iy2, t);
        if (iy2 === 0) ctx.moveTo(q[0], q[1]); else ctx.lineTo(q[0], q[1]);
      }
      ctx.stroke();
    }

    // 교차점 — 진행률이 높을수록 또렷해진다
    var dotA = 0.10 + progress * 0.45;
    ctx.fillStyle = 'rgba(196,106,58,' + dotA + ')';
    for (var jy = 0; jy <= ROWS; jy += 2) {
      for (var jx = 0; jx <= COLS; jx += 2) {
        if (jx / COLS > shown || jy / ROWS > shown) continue;
        var r = point(jx, jy, t);
        ctx.fillRect(r[0] - 1, r[1] - 1, 2, 2);
      }
    }
  }

  /* ── 0 → 100 카운트 ── */
  var start = null;
  var DUR = 2200;          // 전체 인트로 길이
  var done = false;

  function frame(ts) {
    if (start === null) start = ts;
    var e = Math.min(1, (ts - start) / DUR);
    // 끝에서 부드럽게 멈추는 이징
    progress = 1 - Math.pow(1 - e, 2.2);
    t = (ts - start) / 1000;

    var n = Math.round(progress * 100);
    numEl.textContent = n < 10 ? '00' + n : (n < 100 ? '0' + n : '100');
    barEl.style.transform = 'scaleX(' + progress + ')';

    draw();

    if (e < 1) {
      requestAnimationFrame(frame);
    } else if (!done) {
      done = true;
      finish();
    }
  }

  function finish() {
    root.classList.add('is-out');
    document.body.classList.remove('is-intro');
    setTimeout(function () {
      if (root.parentNode) root.parentNode.removeChild(root);
      window.dispatchEvent(new Event('resize'));
    }, 1100);
  }

  document.body.classList.add('is-intro');
  requestAnimationFrame(frame);

  // 탭이 백그라운드였다가 돌아오는 등 rAF가 멈춘 경우에도 인트로가 걸려 있지 않도록
  setTimeout(function () {
    if (!done) {
      done = true;
      progress = 1;
      numEl.textContent = '100';
      barEl.style.transform = 'scaleX(1)';
      finish();
    }
  }, DUR + 2500);
})();
