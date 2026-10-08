/* careCL — 공용 부드러운 스크롤 (Lenis) */
(function () {
  if (window.__lenis) return;
  if (!window.Lenis) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var lenis = new Lenis({
    duration: 1.25,
    easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
    smoothWheel: true,
    wheelMultiplier: 0.9,
    touchMultiplier: 1.6
  });
  (function raf(time) { lenis.raf(time); requestAnimationFrame(raf); })(0);
  window.__lenis = lenis;
})();
