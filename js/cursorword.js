/* =========================================================
   careCL — 커서를 따라다니는 "careCL" 글자 (울렁이며 따라옴)
   ========================================================= */
(function () {
  var host = document.getElementById('cursorWord');
  if (!host) return;

  var fine = window.matchMedia && window.matchMedia('(pointer: fine)').matches;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!fine || reduce) { host.parentNode && host.parentNode.removeChild(host); return; }

  var WORD = 'careCL';
  var letters = [];
  for (var i = 0; i < WORD.length; i++) {
    var el = document.createElement('span');
    el.className = 'cursorword__c';
    el.textContent = WORD[i];
    host.appendChild(el);
    letters.push({ el: el, x: -200, y: -200 });
  }

  var mx = -200, my = -200, has = false, t = 0;

  window.addEventListener('mousemove', function (e) {
    mx = e.clientX; my = e.clientY;
    if (!has) { has = true; host.classList.add('is-on'); }
  }, { passive: true });

  document.addEventListener('mouseleave', function () {
    has = false; host.classList.remove('is-on');
  });

  /* 링크·버튼 위에서는 방해되지 않게 살짝 숨긴다 */
  document.addEventListener('mouseover', function (e) {
    var over = e.target.closest && e.target.closest('a,button,input,textarea,select,.doccard,.docgrid');
    host.classList.toggle('is-dim', !!over);
  }, { passive: true });

  function frame() {
    t += 0.06;
    var px = mx + 22, py = my + 20;          // 커서 오른쪽 아래에서 따라온다
    for (var i = 0; i < letters.length; i++) {
      var L = letters[i];
      var ease = 0.26 - i * 0.025;           // 뒤 글자일수록 더 느리게 → 꼬리처럼 끌림
      if (ease < 0.07) ease = 0.07;
      L.x += (px - L.x) * ease;
      L.y += (py - L.y) * ease;
      var wob = Math.sin(t + i * 0.7) * (2.2 + i * 0.5);   // 울렁임
      L.el.style.transform = 'translate3d(' + (L.x + i * 10.5) + 'px,' + (L.y + wob) + 'px,0)';
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
