/* 진단 결과 리포트 미리보기 — 설문 없이 타입을 골라 본다 */
(function () {
  var tabs = document.querySelector('[data-rpt-tabs]');
  var out = document.querySelector('[data-rpt-out]');
  if (!tabs || !out || !window.ckuReport) return;

  var ORDER = ['early', 'tired', 'fine', 'sag', 'muscle', 'mixed'];
  var NAMES = window.ckuReport.names;

  function current() {
    var q = (location.search.match(/[?&]type=([a-z]+)/) || [])[1];
    return ORDER.indexOf(q) > -1 ? q : 'muscle';
  }

  function draw(key, push) {
    out.innerHTML = window.ckuReport.html(key, {});
    window.ckuReport.fillBars(out);
    Array.prototype.forEach.call(tabs.children, function (b) {
      b.classList.toggle('is-on', b.dataset.key === key);
    });
    if (push) history.replaceState(null, '', '?type=' + key);
  }

  ORDER.forEach(function (key) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'rptpick__tab';
    b.dataset.key = key;
    b.innerHTML = '<em>' + ('0' + (ORDER.indexOf(key) + 1)).slice(-2) + '</em><b>' + NAMES[key] + '</b>';
    b.addEventListener('click', function () { draw(key, true); });
    tabs.appendChild(b);
  });

  draw(current(), false);
})();
