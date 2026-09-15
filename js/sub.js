/* careCL — sub pages (회사소개) */
(function () {
  'use strict';
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  gsap.registerPlugin(ScrollTrigger);

  if (!reduceMotion && window.Lenis) {
    var lenis = new Lenis({ duration: 1.05, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  /* 스크롤 시 안내바 접기 */
  ScrollTrigger.create({
    start: 'top -60',
    onEnter: function () { document.body.classList.add('is-scrolled'); },
    onLeaveBack: function () { document.body.classList.remove('is-scrolled'); }
  });

  /* 서브 비주얼 인트로 */
  gsap.from('.subvisual__inner > *', { opacity: 0, y: 24, duration: .9, ease: 'power2.out', stagger: .1, delay: .15 });
  if (!reduceMotion) {
    gsap.to('.subvisual__img', {
      scrollTrigger: { trigger: '.subvisual', start: 'top top', end: 'bottom top', scrub: true },
      y: 60, ease: 'none'
    });
  }

  /* 공통 등장 */
  var targets = '.seclabel, .sec h2, .about__copy p, .about__visual, .facts > div, ' +
                '.ceo__photo, .ceo blockquote, .ceo__body, .ceo__sign, ' +
                '.history__title, .tl-group, .history__img, ' +
                '.cert, .mv__en, .mv__sub, .pillar, .map, .locinfo > div';
  gsap.utils.toArray(targets).forEach(function (el, i) {
    gsap.from(el, {
      scrollTrigger: { trigger: el, start: 'top 88%' },
      opacity: 0, y: 26, duration: .85, ease: 'power2.out'
    });
  });

  var burger = document.querySelector('.header__burger');
  if (burger) burger.addEventListener('click', function () { document.body.classList.toggle('nav-open'); });

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
