/* =========================================================
   careCL Global — Main  /  interactions
   deps: lenis, gsap, ScrollTrigger  (all local in /libs)
   ========================================================= */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  gsap.registerPlugin(ScrollTrigger);

  /* ---------- 1. smooth scroll (Lenis) ---------- */
  var lenis = null;
  if (!reduceMotion && window.Lenis) {
    lenis = new Lenis({ duration: 1.1, smoothWheel: true });
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add(function (t) { lenis.raf(t * 1000); });
    gsap.ticker.lagSmoothing(0);
  }

  /* ---------- 2. header state ---------- */
  var header = document.getElementById('header');
  var hero = document.getElementById('hero');
  ScrollTrigger.create({
    trigger: hero,
    start: 'bottom top+=' + (header.offsetHeight + 44),
    onEnter: function () { header.classList.add('is-light'); document.body.classList.add('is-scrolled'); },
    onLeaveBack: function () { header.classList.remove('is-light'); document.body.classList.remove('is-scrolled'); }
  });

  /* ---------- 3. hero intro ---------- */
  var heroTl = gsap.timeline({ delay: .25 });
  heroTl
    .to('.hero__title .line > span', { y: '0%', duration: 1.1, ease: 'power3.out', stagger: .1 })
    .to('.hero__eyebrow', { opacity: 1, y: 0, duration: .8, ease: 'power2.out' }, '-=.9')
    .to('.hero__sub', { opacity: 1, y: 0, duration: .8, ease: 'power2.out' }, '-=.65')
    .to('.hero__link', { opacity: 1, y: 0, duration: .8, ease: 'power2.out' }, '-=.6')
    .from('.hero__meta li', { opacity: 0, y: 16, duration: .7, ease: 'power2.out', stagger: .07 }, '-=.5');

  /* ---------- 4. counters ---------- */
  function runCount(el, delay) {
    var target = parseFloat(el.dataset.count);
    var dec = parseInt(el.dataset.dec || '0', 10);
    var obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 1.4, delay: delay || 0, ease: 'power2.out',
      onUpdate: function () { el.textContent = obj.v.toFixed(dec); }
    });
  }
  function initCounter(el) {
    if (el.closest('.hero')) { runCount(el, 1.1); return; }
    ScrollTrigger.create({
      trigger: el, start: 'top 92%', once: true,
      onEnter: function () { runCount(el, 0); }
    });
  }
  document.querySelectorAll('[data-count]').forEach(initCounter);

  /* ---------- 5. marquee loop ---------- */
  var track = document.getElementById('marqueeTrack');
  if (track) {
    var group = track.querySelector('.marquee__group');
    var loop = gsap.to(track, {
      x: function () { return -group.offsetWidth; },
      duration: 38, ease: 'none', repeat: -1
    });
    track.parentElement.addEventListener('mouseenter', function () { loop.timeScale(.25); });
    track.parentElement.addEventListener('mouseleave', function () { loop.timeScale(1); });
  }

  /* ---------- 6. agent section ---------- */
  gsap.from('.agent__head > *', {
    scrollTrigger: { trigger: '.agent__head', start: 'top 78%' },
    opacity: 0, y: 26, duration: .9, ease: 'power2.out', stagger: .12
  });
  gsap.from('.agent__faceclip', {
    scrollTrigger: { trigger: '.agent__stage', start: 'top 78%' },
    opacity: 0, y: 18, duration: 1.1, ease: 'power2.out'
  });
  (function () {
    var pts = gsap.utils.toArray('.callouts .pt');
    var cards = gsap.utils.toArray('.callouts .card');
    var lines = gsap.utils.toArray('.colines line');
    var st = { trigger: '.agent__stage', start: 'top 72%' };
    gsap.from(pts,   { scrollTrigger: st, opacity: 0, scale: .3, duration: .45, ease: 'back.out(2)', stagger: .12, delay: .3 });
    gsap.from(lines, { scrollTrigger: st, opacity: 0, duration: .5, ease: 'power2.out', stagger: .12, delay: .45 });
    gsap.from(cards, { scrollTrigger: st, opacity: 0, y: 12, duration: .5, ease: 'power2.out', stagger: .12, delay: .55 });
  })();

  /* ---------- 7. products : pinned section, right column scrolls ---------- */
  var cards = gsap.utils.toArray('.pcard');
  var idxEl = document.getElementById('prodIndex');
  var fillEl = document.getElementById('prodFill');

  ScrollTrigger.matchMedia({
    '(min-width: 1025px)': function () {
      var section = document.querySelector('.products');
      var list = document.querySelector('.products__list');
      var viewport = document.querySelector('.products__viewport');

      var getDistance = function () {
        return Math.max(0, list.scrollHeight - viewport.offsetHeight);
      };

      var tl = gsap.timeline({
        scrollTrigger: {
          trigger: section,
          start: 'top top',
          end: function () { return '+=' + getDistance(); },
          pin: true,
          pinSpacing: true,
          scrub: 0.6,
          invalidateOnRefresh: true,
          onUpdate: function (self) {
            var p = self.progress;
            var n = Math.min(cards.length, Math.max(1, Math.ceil(p * cards.length) || 1));
            if (idxEl) idxEl.textContent = ('0' + n).slice(-2);
            if (fillEl) fillEl.style.width = Math.max(8, p * 100) + '%';
          }
        }
      });
      tl.to(list, { y: function () { return -getDistance(); }, ease: 'none' });
    },
    '(max-width: 1024px)': function () {
      cards.forEach(function (card) {
        gsap.from(card, {
          scrollTrigger: { trigger: card, start: 'top 92%' },
          opacity: 0, y: 50, duration: .9, ease: 'power3.out'
        });
      });
    }
  });

  /* ---------- 8. brand story ---------- */
  gsap.from('.brand__copy > *', {
    scrollTrigger: { trigger: '.brand', start: 'top 72%' },
    opacity: 0, y: 28, duration: .9, ease: 'power2.out', stagger: .1
  });
  if (!reduceMotion) {
    gsap.to('.brand__visual', {
      scrollTrigger: { trigger: '.brand', start: 'top bottom', end: 'bottom top', scrub: true },
      y: -40, ease: 'none'
    });
  }
  gsap.from('.brand__stats li', {
    scrollTrigger: { trigger: '.brand__stats', start: 'top 85%' },
    opacity: 0, y: 24, duration: .8, ease: 'power2.out', stagger: .1
  });

  /* ---------- 9. generic reveal ---------- */
  gsap.utils.toArray('.science__def, .science__stats li, .footer__cols > div').forEach(function (el, i) {
    gsap.from(el, {
      scrollTrigger: { trigger: el, start: 'top 90%' },
      opacity: 0, y: 20, duration: .8, ease: 'power2.out', delay: (i % 4) * .06
    });
  });

  /* ---------- 10. mobile menu (placeholder) ---------- */
  var burger = document.querySelector('.header__burger');
  if (burger) {
    burger.addEventListener('click', function () {
      document.body.classList.toggle('nav-open');
    });
  }

  window.addEventListener('load', function () { ScrollTrigger.refresh(); });
})();
