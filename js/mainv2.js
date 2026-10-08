/* careCL — 메인페이지 v2 : 롤링 배너 / 콜렉션 캐러셀 / 등장 효과 */
(function () {
  'use strict';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- 부드러운 스크롤 ---------- */
  if (!reduce && window.Lenis) {
    var lenis = new Lenis({
      duration: 1.25,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true,
      wheelMultiplier: 0.9,
      touchMultiplier: 1.6
    });
    (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
    window.__lenis = lenis;
  }

  /* ---------- 02 롤링 배너 ---------- */
  var roll = document.querySelector('[data-roll]');
  if (roll) {
    var track = roll.querySelector('.mroll__track');
    var slides = [].slice.call(roll.querySelectorAll('.mroll__slide'));
    var dots = [].slice.call(roll.querySelectorAll('.mroll__dots button'));
    var idx = 0, timer = null;

    function go(n) {
      idx = (n + slides.length) % slides.length;
      track.style.transform = 'translateX(' + (-idx * 100) + '%)';
      dots.forEach(function (d, i) { d.classList.toggle('is-on', i === idx); });
    }
    function play() { if (reduce) return; stop(); timer = setInterval(function () { go(idx + 1); }, 6000); }
    function stop() { if (timer) clearInterval(timer); }

    dots.forEach(function (d, i) { d.addEventListener('click', function () { go(i); play(); }); });
    var prev = roll.querySelector('[data-roll-prev]');
    var next = roll.querySelector('[data-roll-next]');
    if (prev) prev.addEventListener('click', function () { go(idx - 1); play(); });
    if (next) next.addEventListener('click', function () { go(idx + 1); play(); });
    roll.addEventListener('mouseenter', stop);
    roll.addEventListener('mouseleave', play);

    /* 터치 스와이프 */
    var sx = 0;
    roll.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; stop(); }, { passive: true });
    roll.addEventListener('touchend', function (e) {
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 40) go(idx + (dx < 0 ? 1 : -1));
      play();
    });

    go(0); play();
  }

  /* ---------- 06 콜렉션 캐러셀 ---------- */
  var coll = document.querySelector('[data-coll]');
  if (coll) {
    var ctrack = coll.querySelector('.mcoll__track');
    var cards = [].slice.call(coll.querySelectorAll('.mcard'));
    var pos = 0;

    function step() {
      if (cards.length < 2) return 0;
      return cards[1].getBoundingClientRect().left - cards[0].getBoundingClientRect().left;
    }
    function maxPos() {
      var vw = coll.querySelector('.mcoll__viewport').clientWidth;
      return Math.max(0, ctrack.scrollWidth - vw);
    }
    function move(dir) {
      pos = Math.min(maxPos(), Math.max(0, pos + dir * step()));
      ctrack.style.transform = 'translateX(' + (-pos) + 'px)';
    }
    var cp = coll.querySelector('[data-coll-prev]');
    var cn = coll.querySelector('[data-coll-next]');
    if (cp) cp.addEventListener('click', function () { move(-1); });
    if (cn) cn.addEventListener('click', function () { move(1); });
    window.addEventListener('resize', function () { pos = Math.min(pos, maxPos()); ctrack.style.transform = 'translateX(' + (-pos) + 'px)'; });

    var tx = 0, tp = 0;
    coll.addEventListener('touchstart', function (e) { tx = e.touches[0].clientX; tp = pos; }, { passive: true });
    coll.addEventListener('touchmove', function (e) {
      pos = Math.min(maxPos(), Math.max(0, tp - (e.touches[0].clientX - tx)));
      ctrack.style.transition = 'none';
      ctrack.style.transform = 'translateX(' + (-pos) + 'px)';
    }, { passive: true });
    coll.addEventListener('touchend', function () { ctrack.style.transition = ''; });
  }

  /* ---------- 04 핵심 항목 원형 배치 ---------- */
  function placeCore() {
    var stage = document.querySelector('[data-core]');
    if (!stage) return;
    var items = [].slice.call(stage.querySelectorAll('.mcore__item'));
    if (window.innerWidth <= 860) {
      items.forEach(function (el) { el.style.left = ''; el.style.top = ''; });
      return;
    }
    var n = items.length;
    items.forEach(function (el, i) {
      var a = (-90 + (360 / n) * i) * Math.PI / 180;   /* 12시 방향부터 시계 방향 */
      var rx = 42, ry = 44;                            /* 무대 대비 % 반지름 */
      el.style.left = (50 + Math.cos(a) * rx) + '%';
      el.style.top = (50 + Math.sin(a) * ry) + '%';
      el.dataset.dx = (Math.cos(a) * 90).toFixed(1);   /* 모이기 전 바깥 위치 */
      el.dataset.dy = (Math.sin(a) * 90).toFixed(1);
    });
  }
  placeCore();
  window.addEventListener('resize', placeCore);

  /* ---------- 헤더 : 히어로 구간만 투명, 이후 라이트 ---------- */
  (function headerLight() {
    var header = document.getElementById('header');
    var hero = document.querySelector('.mhero');
    if (!header || !hero) return;
    function sync() {
      var y = window.scrollY || 0;
      var limit = hero.offsetHeight - header.offsetHeight - 30;
      header.classList.toggle('is-light', y > limit);
      document.body.classList.toggle('is-scrolled', y > 60);
    }
    sync();
    window.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
  })();

  /* ---------- 스크롤 등장 ---------- */
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px' });
    [].forEach.call(document.querySelectorAll('[data-reveal]'), function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(22px)';
      el.style.transition = 'opacity .9s ease, transform 1s cubic-bezier(.2,.7,.2,1)';
      io.observe(el);
    });
    document.addEventListener('transitionend', function () {});
    var style = document.createElement('style');
    style.textContent = '[data-reveal].is-in{opacity:1 !important;transform:none !important;}';
    document.head.appendChild(style);
  }
})();

/* ── 메인 히어로 헤드라인 : 글자가 솟아오르며 흐림이 걷히는 등장 ── */
(function () {
  var h1 = document.querySelector('.mhero h1');
  if (!h1) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    h1.classList.add('is-in');
    return;
  }

  /* 줄 단위로 나누고, 줄 안의 글자를 각각 감싼다 */
  var lines = h1.innerHTML.split(/<br\s*\/?>/i);
  var html = '';
  var idx = 0;
  lines.forEach(function (line, li) {
    html += '<span class="hl"><span class="hl__in">';
    line.replace(/<[^>]+>/g, '').split('').forEach(function (ch) {
      if (ch === ' ') { html += '<span class="hc hc--sp"> </span>'; idx++; return; }
      html += '<span class="hc" style="--d:' + (idx * 28) + 'ms">' + ch + '</span>';
      idx++;
    });
    html += '</span></span>';
    if (li < lines.length - 1) html += '<br>';
    idx += 2;
  });
  h1.innerHTML = html;

  /* 인트로가 끝난 뒤 시작 */
  function play() { requestAnimationFrame(function () { h1.classList.add('is-in'); }); }
  if (document.getElementById('intro')) {
    var t = setInterval(function () {
      if (!document.getElementById('intro')) { clearInterval(t); play(); }
    }, 120);
    setTimeout(function () { clearInterval(t); play(); }, 6000);
  } else {
    setTimeout(play, 260);
  }
})();

/* ── 샵 링크 : 스크롤에 따라 높이가 300px에서 화면 전체로 자란다 ── */
(function () {
  var shop = document.querySelector('.mshop');
  if (!shop) return;
  var bg = shop.querySelector('.mshop__bg');
  var img = bg && bg.querySelector('img');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var BASE = 300;                       /* 처음 보이는 띠 높이 */
  function apply(p) {
    var vh = window.innerHeight;
    var base = Math.min(BASE, vh * 0.5);
    shop.style.marginLeft = '0px';
    shop.style.marginRight = '0px';
    shop.style.borderRadius = '0px';
    shop.style.height = (base + (vh - base) * p) + 'px';
    shop.style.minHeight = '0px';
    shop.style.paddingTop = '0px';
    shop.style.paddingBottom = '0px';
    if (bg) bg.style.opacity = (0.24 + p * 0.16).toFixed(3);
    if (img) img.style.transform = 'scale(' + (1.16 - p * 0.16).toFixed(3) + ')';
  }
  if (reduce) { apply(1); return; }

  var last = -1;
  function update() {
    var r = shop.getBoundingClientRect();
    var vh = window.innerHeight;
    /* 섹션 윗변이 화면 아래 85% 지점에서 상단 10% 지점까지 오는 동안 0 → 1 */
    var p = (vh * 0.85 - r.top) / (vh * 0.75);
    p = Math.max(0, Math.min(1, p));
    p = p * p * (3 - 2 * p);          /* 시작과 끝을 부드럽게 */
    if (Math.abs(p - last) > 0.002) { last = p; apply(p); }
  }
  /* 스크롤 이벤트로 즉시 반영하고, 프레임 루프로 부드럽게 보정한다 */
  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) { window.__lenis.on('scroll', update); }
  (function loop() { update(); requestAnimationFrame(loop); })();
  window.addEventListener('resize', function () { last = -1; update(); });
})();


/* ── 핵심 항목이 스크롤에 따라 가운데로 모인다 ── */
(function () {
  var stage = document.querySelector('[data-core]');
  if (!stage) return;
  var items = [].slice.call(stage.querySelectorAll('.mcore__item'));
  var obj = stage.querySelector('.mcore__object');
  if (!items.length) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function clear() {
    items.forEach(function (el) { el.style.transform = ''; el.style.opacity = ''; });
    if (obj) obj.style.transform = '';
  }
  function apply(p) {
    if (window.innerWidth <= 860) { clear(); return; }
    var q = 1 - p;                       /* 1 = 흩어짐, 0 = 제자리 */
    items.forEach(function (el) {
      var dx = parseFloat(el.dataset.dx || 0) * q;
      var dy = parseFloat(el.dataset.dy || 0) * q;
      el.style.transform = 'translate(-50%,-50%) translate(' + dx.toFixed(1) + 'px,' + dy.toFixed(1) + 'px) scale(' + (0.9 + p * 0.1).toFixed(3) + ')';
      el.style.opacity = (0.2 + p * 0.8).toFixed(2);
    });
    if (obj) obj.style.transform = 'translate(-50%,-50%) scale(' + (0.92 + p * 0.08).toFixed(3) + ')';
  }
  if (reduce) { apply(1); return; }

  var last = -1;
  function update() {
    if (window.innerWidth <= 860) { if (last !== 9) { last = 9; clear(); } return; }
    var r = stage.getBoundingClientRect();
    var vh = window.innerHeight;
    var p = (vh - r.top) / (vh * 0.95);
    p = Math.max(0, Math.min(1, p));
    p = p * p * (3 - 2 * p);
    if (Math.abs(p - last) > 0.002) { last = p; apply(p); }
  }
  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', update);
  window.addEventListener('resize', function () { last = -1; update(); });
  (function loop() { update(); requestAnimationFrame(loop); })();
  update();
})();

/* ── 환기용 이미지 문구 : 글자가 번지듯 나타나고 천천히 떠오른다 ── */
(function () {
  var txt = document.querySelector('.mbreak__txt');
  if (!txt) return;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) { txt.classList.add('is-in'); return; }

  var words = txt.textContent.trim().split(/\s+/);
  txt.innerHTML = words.map(function (w, i) {
    return '<span class="bw"><span class="bw__in" style="--d:' + (i * 120) + 'ms">' + w + '</span></span>';
  }).join(' ');

  var sec = txt.closest('.mbreak');
  var last = -1;
  function update() {
    var r = sec.getBoundingClientRect();
    var vh = window.innerHeight;
    var p = (vh - r.top) / (vh + r.height);
    p = Math.max(0, Math.min(1, p));
    if (p > 0.22) txt.classList.add('is-in');
    if (Math.abs(p - last) > 0.003) {
      last = p;
      txt.style.transform = 'translateY(' + ((0.5 - p) * 60).toFixed(1) + 'px)';
      txt.style.letterSpacing = (-0.03 + p * 0.03).toFixed(3) + 'em';
    }
  }
  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', update);
  window.addEventListener('resize', update);
  (function loop() { update(); requestAnimationFrame(loop); })();
  update();
})();

/* ── 07 5 STEP : 스크롤에 따라 다섯 단계가 차례로 올라온다 ── */
(function () {
  var sec = document.querySelector('[data-step]');
  if (!sec) return;
  var cards = [].slice.call(sec.querySelectorAll('[data-step-card]'));
  var bar = sec.querySelector('[data-step-bar]');
  if (!cards.length) return;

  function cl(v) { return Math.max(0, Math.min(1, v)); }
  function ease(p) { return p * p * (3 - 2 * p); }

  var cleared = false;
  function clear() {
    if (cleared) return;
    cards.forEach(function (c) {
      c.style.transform = ''; c.style.opacity = '';
      var f = c.querySelector('.mstep__fill'); if (f) f.style.transform = '';
    });
    if (bar) bar.style.transform = '';
    cleared = true;
  }

  function update() {
    if (window.innerWidth <= 860) { clear(); return; }
    cleared = false;
    var r = sec.getBoundingClientRect(), vh = window.innerHeight;
    var p = cl((vh * 0.92 - r.top) / (vh * 0.9));
    if (bar) bar.style.transform = 'scaleX(' + ease(p).toFixed(3) + ')';
    cards.forEach(function (c, i) {
      var q = ease(cl((p - i * 0.1) / 0.5));
      c.style.transform = 'translate3d(0,' + ((1 - q) * 96).toFixed(1) + 'px,0) scale(' + (0.95 + q * 0.05).toFixed(3) + ')';
      c.style.opacity = (0.06 + q * 0.94).toFixed(3);
      var f = c.querySelector('.mstep__fill');
      if (f) f.style.transform = 'scaleY(' + q.toFixed(3) + ')';
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', update);
  window.addEventListener('resize', update);
  (function loop() { update(); requestAnimationFrame(loop); })();
  update();
})();

/* ── 06 콜렉션 : 카드가 순차로 떠오르고 이미지가 제 크기를 찾는다 ── */
(function () {
  var sec = document.querySelector('[data-coll]');
  if (!sec) return;
  var cards = [].slice.call(sec.querySelectorAll('.mcard'));
  if (!cards.length) return;

  function cl(v) { return Math.max(0, Math.min(1, v)); }
  function ease(p) { return p * p * (3 - 2 * p); }

  var cleared = false;
  function clear() {
    if (cleared) return;
    cards.forEach(function (c) {
      c.style.transform = ''; c.style.opacity = '';
      var w = c.querySelector('.mcard__img'); if (w) w.style.transform = '';
    });
    cleared = true;
  }

  function update() {
    if (window.innerWidth <= 860) { clear(); return; }
    cleared = false;
    var r = sec.getBoundingClientRect(), vh = window.innerHeight;
    var p = cl((vh * 0.9 - r.top) / (vh * 0.8));
    cards.forEach(function (c, i) {
      var q = ease(cl((p - i * 0.07) / 0.55));
      c.style.transform = 'translate3d(0,' + ((1 - q) * 80).toFixed(1) + 'px,0)';
      c.style.opacity = (0.08 + q * 0.92).toFixed(3);
      var w = c.querySelector('.mcard__img');
      if (w) w.style.transform = 'scale(' + (0.9 + q * 0.1).toFixed(3) + ')';
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', update);
  window.addEventListener('resize', update);
  (function loop() { update(); requestAnimationFrame(loop); })();
  update();
})();

/* ── 02 배너 설명 : 행마다 선이 그어지고 글과 이미지가 차례로 열린다 ── */
(function () {
  var rows = [].slice.call(document.querySelectorAll('.mbinfo [data-row]'));
  if (!rows.length) return;

  function cl(v) { return Math.max(0, Math.min(1, v)); }
  function ease(p) { return p * p * (3 - 2 * p); }

  var data = rows.map(function (r) {
    return {
      row: r,
      line: r.querySelector('.mbrow__line'),
      imgin: r.querySelector('.mbrow__imgin'),
      texts: [].slice.call(r.querySelectorAll('.mbrow__tag, .mbrow__txt b, .mbrow__txt strong, .mbrow__txt p'))
    };
  });

  var cleared = false;
  function clear() {
    if (cleared) return;
    data.forEach(function (d) {
      if (d.line) d.line.style.transform = '';
      if (d.imgin) { d.imgin.style.transform = ''; d.imgin.style.opacity = ''; }
      d.texts.forEach(function (t) { t.style.transform = ''; t.style.opacity = ''; });
    });
    cleared = true;
  }

  function update() {
    if (window.innerWidth <= 900) { clear(); return; }
    cleared = false;
    var vh = window.innerHeight;
    data.forEach(function (d) {
      var r = d.row.getBoundingClientRect();
      if (r.bottom < -300 || r.top > vh + 300) return;
      var p = cl((vh * 0.88 - r.top) / (vh * 0.62));

      if (d.line) d.line.style.transform = 'scaleX(' + ease(p).toFixed(3) + ')';

      d.texts.forEach(function (t, i) {
        var q = ease(cl((p - i * 0.07) / 0.5));
        t.style.transform = 'translate3d(0,' + ((1 - q) * 34).toFixed(1) + 'px,0)';
        t.style.opacity = q.toFixed(3);
      });

      if (d.imgin) {
        var q = ease(cl((p - 0.08) / 0.55));
        var drift = (0.5 - cl((r.top + r.height / 2) / vh)) * 5;    // 느린 패럴랙스(%)
        // 아래에서 떠오르며 제자리를 찾는다 (가림막은 바깥 틀이 맡는다)
        d.imgin.style.transform =
          'translate3d(0,' + (drift + (1 - q) * 9).toFixed(1) + '%,0) scale(' + (1.22 - q * 0.22).toFixed(3) + ')';
        d.imgin.style.opacity = (0.25 + q * 0.75).toFixed(3);
      }
    });
  }

  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) window.__lenis.on('scroll', update);
  window.addEventListener('resize', update);
  (function loop() { update(); requestAnimationFrame(loop); })();
  update();
})();

/* ── 06 콜렉션 : 3D 커버플로 (가운데 제품이 정면, 양옆은 비스듬히) ── */
(function () {
  var sec = document.querySelector('[data-cov]');
  if (!sec) return;
  var stage = sec.querySelector('[data-cov-stage]');
  var items = [].slice.call(sec.querySelectorAll('[data-cov-item]'));
  var arc = sec.querySelector('[data-cov-arc]');
  var capTag = sec.querySelector('[data-cov-tag]');
  var capName = sec.querySelector('[data-cov-name]');
  var capDesc = sec.querySelector('[data-cov-desc]');
  var capLink = sec.querySelector('[data-cov-link]');
  var prevBtn = sec.querySelector('[data-cov-prev]');
  var nextBtn = sec.querySelector('[data-cov-next]');
  var N = items.length;
  if (!stage || N < 2) return;

  var ROT = 52, DEPTH = 320, VISIBLE = 2.6;
  var active = 0, dots = [];

  function step() {
    return items[0].getBoundingClientRect().width * 0.66;
  }

  function place() {
    var sx = step();
    items.forEach(function (el, i) {
      var d = i - active;
      if (d > N / 2) d -= N;
      if (d < -N / 2) d += N;
      var ad = Math.abs(d);
      var capped = Math.min(ad, 3);
      var sign = d < 0 ? -1 : 1;
      /* 첫 칸은 넓게, 그 뒤로는 좁혀서 겹쳐 쌓는다 */
      var x = sign * (Math.min(capped, 1) * sx + Math.max(0, capped - 1) * sx * 0.52);
      var z = -capped * DEPTH;
      var r = -sign * Math.min(capped * ROT, 70);
      el.style.transform = 'translate(-50%,-50%) translate3d(' + x.toFixed(1) + 'px,0,' + z.toFixed(0) + 'px) rotateY(' + r.toFixed(1) + 'deg)';
      el.style.opacity = ad > VISIBLE ? '0' : (ad === 0 ? '1' : '0.86');
      el.style.zIndex = String(100 - Math.round(ad * 10));
      el.classList.toggle('is-active', ad === 0);
      var a = el.querySelector('a');
      if (a) a.setAttribute('tabindex', ad === 0 ? '0' : '-1');
    });
    dots.forEach(function (b, i) { b.classList.toggle('is-on', i === active); });
    var cur = items[active];
    if (capTag) capTag.textContent = cur.dataset.tag || '';
    if (capName) capName.textContent = cur.dataset.name || '';
    if (capDesc) capDesc.textContent = cur.dataset.desc || '';
    if (capLink && cur.dataset.href) capLink.setAttribute('href', cur.dataset.href);
  }

  function go(i) {
    active = ((i % N) + N) % N;
    place();
  }

  /* 아래 곡선 위에 점을 올린다 */
  function buildDots() {
    if (!arc) return;
    items.forEach(function (el, i) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'mcov__dot';
      b.setAttribute('aria-label', (el.dataset.name || (i + 1)) + ' 보기');
      b.addEventListener('click', function () { go(i); hold(); });
      arc.appendChild(b);
      dots.push(b);
    });
  }
  function layoutDots() {
    if (!arc || !dots.length) return;
    var w = arc.clientWidth, h = arc.clientHeight;
    var rx = w / 2 - 10, ry = h - 8, cx = w / 2;
    dots.forEach(function (b, i) {
      var t = N === 1 ? 0.5 : i / (N - 1);
      var th = Math.PI * t;                       /* 0 → π */
      b.style.left = (cx - rx * Math.cos(th)).toFixed(1) + 'px';
      b.style.top = (ry * (1 - Math.sin(th))).toFixed(1) + 'px';
    });
  }

  buildDots();
  go(0);
  layoutDots();

  items.forEach(function (el, i) {
    el.addEventListener('click', function (e) {
      if (i !== active) { e.preventDefault(); go(i); hold(); }
    });
  });
  if (prevBtn) prevBtn.addEventListener('click', function () { go(active - 1); hold(); });
  if (nextBtn) nextBtn.addEventListener('click', function () { go(active + 1); hold(); });

  /* 드래그 · 스와이프 */
  var sx0 = null;
  stage.addEventListener('pointerdown', function (e) { sx0 = e.clientX; });
  window.addEventListener('pointerup', function (e) {
    if (sx0 === null) return;
    var dx = e.clientX - sx0; sx0 = null;
    if (Math.abs(dx) > 40) { go(active + (dx < 0 ? 1 : -1)); hold(); }
  });

  /* 자동 넘김 — 화면에 보일 때만, 마우스가 올라가면 멈춘다 */
  var timer = null, paused = false, held = 0;
  function tick() {
    if (paused || Date.now() < held) return;
    var r = sec.getBoundingClientRect();
    if (r.bottom < 0 || r.top > window.innerHeight) return;
    go(active + 1);
  }
  function hold() { held = Date.now() + 6000; }
  sec.addEventListener('mouseenter', function () { paused = true; });
  sec.addEventListener('mouseleave', function () { paused = false; });
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce) timer = setInterval(tick, 4500);

  window.addEventListener('resize', function () { place(); layoutDots(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { place(); layoutDots(); });
})();
