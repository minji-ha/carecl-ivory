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

/* ── 샵 링크 : 스크롤에 따라 화면을 좌우·상하로 꽉 채운다 ── */
(function () {
  var shop = document.querySelector('.mshop');
  if (!shop) return;
  var bg = shop.querySelector('.mshop__bg');
  var img = bg && bg.querySelector('img');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function gutter() {
    return Math.max(16, Math.min(110, window.innerWidth * 0.07));
  }
  function apply(p) {
    var g = gutter() * (1 - p);
    shop.style.marginLeft = g + 'px';
    shop.style.marginRight = g + 'px';
    shop.style.borderRadius = (10 * (1 - p)) + 'px';
    shop.style.minHeight = ((0.52 + p * 0.48) * window.innerHeight) + 'px';
    if (bg) bg.style.opacity = (0.22 + p * 0.18).toFixed(3);
    if (img) img.style.transform = 'scale(' + (1.14 - p * 0.14).toFixed(3) + ')';
  }
  if (reduce) { apply(1); return; }

  var last = -1;
  function update() {
    var r = shop.getBoundingClientRect();
    var vh = window.innerHeight;
    var p = 1 - (r.top - vh * 0.15) / (vh * 0.70);
    p = Math.max(0, Math.min(1, p));
    if (Math.abs(p - last) > 0.002) { last = p; apply(p); }
  }
  /* 스크롤 이벤트로 즉시 반영하고, 프레임 루프로 부드럽게 보정한다 */
  window.addEventListener('scroll', update, { passive: true });
  if (window.__lenis && window.__lenis.on) { window.__lenis.on('scroll', update); }
  (function loop() { update(); requestAnimationFrame(loop); })();
  window.addEventListener('resize', function () { last = -1; update(); });
})();
