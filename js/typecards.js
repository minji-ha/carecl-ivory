/* =========================================================
   careCL — 6 AGING TYPES
   화면을 고정한 채 카드가 가로로 흘러가는 스크롤 연출 (데스크톱)
   모바일·모션최소화 환경에서는 세로 카드 그대로
   ========================================================= */
(function () {
  var track = document.querySelector('.typecards');
  if (!track) return;

  var cards = [].slice.call(track.querySelectorAll('.typecard'));
  if (!cards.length) return;

  var stage = track.closest('.sec');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canPin = !reduce && window.gsap && window.ScrollTrigger &&
               window.matchMedia('(min-width: 901px)').matches;

  /* ── 타입 바로가기 칩 ── */
  var nav = document.createElement('nav');
  nav.className = 'typenav';
  cards.forEach(function (c, i) {
    var h = c.querySelector('h4');
    if (!h) return;
    var name = h.textContent.replace(/^\s*\d+\.\s*/, '').split(/\s+·\s+/)[0].trim();
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = (i + 1 < 10 ? '0' : '') + (i + 1) + '  ' + name;
    nav.appendChild(b);
  });
  track.parentNode.insertBefore(nav, track);
  var btns = [].slice.call(nav.querySelectorAll('button'));

  /* ── 진행 표시줄 ── */
  var bar = document.createElement('div');
  bar.className = 'typeprog';
  bar.innerHTML = '<i></i>';
  track.parentNode.insertBefore(bar, track.nextSibling);
  var fill = bar.querySelector('i');

  if (!canPin) {
    bar.style.display = 'none';
    btns.forEach(function (b, i) {
      b.addEventListener('click', function () {
        var top = cards[i].getBoundingClientRect().top + window.scrollY - 140;
        window.scrollTo({ top: top, behavior: 'smooth' });
      });
    });
    return;
  }

  /* ── 가로로 흐르는 핀 스크롤 ── */
  track.classList.add('is-rail');
  if (stage) stage.classList.add('is-pinned');
  gsap.registerPlugin(ScrollTrigger);

  function distance() {
    return Math.max(0, track.scrollWidth - window.innerWidth + 140);
  }

  var tween = gsap.to(track, {
    x: function () { return -distance(); },
    ease: 'none',
    scrollTrigger: {
      trigger: stage,
      start: 'top top',
      end: function () { return '+=' + (distance() + window.innerHeight * 0.35); },
      pin: true,
      scrub: 0.6,
      anticipatePin: 1,
      invalidateOnRefresh: true,
      onUpdate: function (self) {
        fill.style.transform = 'scaleX(' + self.progress + ')';
        var mid = window.innerWidth / 2;
        var best = 0, bestD = Infinity;
        for (var i = 0; i < cards.length; i++) {
          var r = cards[i].getBoundingClientRect();
          var d = Math.abs(r.left + r.width / 2 - mid);
          if (d < bestD) { bestD = d; best = i; }
        }
        for (var j = 0; j < btns.length; j++) btns[j].classList.toggle('is-on', j === best);
      }
    }
  });

  btns.forEach(function (b, i) {
    b.addEventListener('click', function () {
      var st = tween.scrollTrigger;
      var total = cards.length - 1;
      var p = total ? i / total : 0;
      window.scrollTo({ top: st.start + (st.end - st.start) * p, behavior: 'smooth' });
    });
  });

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
