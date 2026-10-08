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


  /* ── 진행 표시줄 ── */
  var bar = document.createElement('div');
  bar.className = 'typeprog';
  bar.innerHTML = '<i></i>';
  track.parentNode.insertBefore(bar, track.nextSibling);
  var fill = bar.querySelector('i');

  if (!canPin) {
    bar.style.display = 'none';
    return;
  }

  /* ── 가로로 흐르는 핀 스크롤 ── */
  track.classList.add('is-rail');
  if (stage) stage.classList.add('is-pinned');
  gsap.registerPlugin(ScrollTrigger);

  function distance() {
    return Math.max(0, track.scrollWidth - window.innerWidth + 140);
  }

  gsap.to(track, {
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
      }
    }
  });

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
