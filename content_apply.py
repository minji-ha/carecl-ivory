# -*- coding: utf-8 -*-
"""케어클 제공 원고(자료/홈페이지 컨텐츠_261007.docx)를 서브 페이지에 그대로 반영.
   원문은 자료/content.txt 에서 한 줄도 바꾸지 않고 가져온다.  python content_apply.py"""
import io
import re

SRC = r"C:\work\carecl\자료\content.txt"
L = io.open(SRC, encoding="utf-8").read().split("\n")


def t(i):
    """원문 한 줄(줄바꿈은 <br>로만 변환)"""
    return L[i].strip().replace("&", "&amp;").replace("<", "&lt;")


def p(i):
    return "<p>%s</p>" % t(i)


def label(en, kr):
    return '<div class="seclabel"><i></i><span>%s &nbsp;·&nbsp; %s</span></div>' % (en, kr)


# ───────────────────────────────── About careCL
about = """<section class="sec">
  <div class="wrap">
    %s
    <div class="about__grid">
      <div class="about__copy">
        <h2>%s</h2>
        %s
        %s
        %s
        <blockquote class="pullquote">%s<br>%s</blockquote>
      </div>
      <div class="about__visual"><img src="assets/img/about-visual.jpg" alt="careCL"></div>
    </div>
    <dl class="facts">
      <div><dt>CEO</dt><dd>최형규 Hyungkyu Choi</dd></div>
      <div><dt>HEADQUARTERS</dt><dd>경기도 고양시 일산동구 동국로 32</dd></div>
      <div><dt>BUSINESS</dt><dd>뷰티 디바이스 · 코스메틱</dd></div>
      <div><dt>TECHNOLOGY</dt><dd>5 SEC. STAMPING RF</dd></div>
    </dl>
  </div>
</section>""" % (label("ABOUT CARECL", "회사 소개"), t(1), p(2), p(3), p(4), t(5), t(6))


# ───────────────────────────────── Our Story
story = """<section class="sec">
  <div class="wrap">
    %s
    <div class="ceo">
      <div class="ceo__visual" id="brandParticles"><canvas aria-label="careCL"></canvas><div class="ceo__visual-grid"></div><div class="ceo__visual-top"><span>AGELESS BEAUTY</span></div></div>
      <div class="ceo__text">
        <h2>%s</h2>
        <div class="ceo__body">
          %s
          %s
          <blockquote class="pullquote">%s<br>%s</blockquote>
          %s
          %s
          <ul class="ulist"><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ul>
          %s
          %s
          %s
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--grey">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
      %s
      <blockquote class="pullquote">%s<br>%s<br>%s</blockquote>
      %s
      %s
      <blockquote class="pullquote">%s<br>%s<br>%s<br>%s</blockquote>
    </div>
    <div class="story__cta"><a href="aging-types.html" class="btn btn--primary">6가지 노화 타입 보기 <span>→</span></a></div>
  </div>
</section>""" % (
    label("OUR STORY", "브랜드 스토리"), t(12),
    p(13), p(14), t(15), t(16), p(17), p(18),
    t(19), t(20), t(21), t(22),
    p(23), p(24), p(25),
    label("UNDERSTAND FIRST", "사람을 먼저 이해합니다"), t(26),
    p(27), p(28), p(29), p(30), p(31),
    t(32), t(33), t(34),
    p(35), p(36),
    t(37), t(38), t(39), t(40),
)


# ───────────────────────────────── AGING LAB / 6 Aging Types
types = [
    (71, 72, 73, 75),
    (77, 78, 79, 81),
    (83, 84, 85, 87),
    (89, 90, 91, 93),
    (95, 96, 97, 99),
    (101, 102, 103, None),
]
cards = []
for no, (ti, qi, di, ci) in enumerate(types, start=1):
    extra = ""
    if ci is None:   # 06 혼합형 : 설명이 세 문단
        extra = "<p>%s</p><p>%s</p>" % (t(104), t(105))
        worry = ""
    else:
        worry = '<p class="type__worry"><em>%s</em>%s</p>' % (t(ci - 1), t(ci))
    cards.append(
        '<div class="typecard"><span class="typecard__no">%02d</span>'
        '<h4>%s</h4><p class="typecard__quote">%s</p><p>%s</p>%s%s</div>'
        % (no, t(ti).split(". ", 1)[1], t(qi), t(di), extra, worry)
    )

aging_types = """<section class="sec" id="types">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      <blockquote class="pullquote">%s<br>%s<br>%s<br>%s</blockquote>
      %s
      <blockquote class="pullquote">%s</blockquote>
      %s
      %s
      %s
      <p>%s<br>%s</p>
    </div>
  </div>
</section>

<section class="sec sec--grey" id="why">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
      %s
      %s
      %s
    </div>
  </div>
</section>

<section class="sec" id="list">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="typecards">%s</div>
  </div>
</section>

<section class="sec sec--grey" id="next">
  <div class="wrap">
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
      <blockquote class="pullquote">%s</blockquote>
      %s
      <p>%s<br>%s</p>
    </div>
    <div class="story__cta">
      <a href="aging-map.html" class="btn btn--primary">AGING MAP 22 보기 <span>→</span></a>
      <a href="survey.html" class="btn btn--ghost">나의 타입 알아보기 <span>→</span></a>
    </div>
  </div>
</section>""" % (
    label("AGING LAB", "6가지 노화 타입"), t(46),
    p(47), p(48),
    t(49), t(50), t(51), t(52),
    p(53), t(54), p(55), p(56), p(57), t(58), t(59),
    label("WHY WE AGE DIFFERENTLY", "왜 노화는 다르게 나타날까"), t(62),
    p(63), p(64), p(65), p(66), p(67), p(68), p(69),
    label("6 AGING TYPES", "유형별 특징"), t(70),
    "".join(cards),
    t(107),
    p(108), p(109), p(110), t(111), p(112), t(113), t(114),
)


# ───────────────────────────────── TECHNOLOGY
tech_cards = [
    (119, 120, [121, 122, 123, 124], (125, [126, 127, 128], 129), 130),
    (132, 133, [134, 135, 136, 137, 138], (139, [140, 141, 142], None), None),
    (147, 148, [149, 150, 151], None, None),
    (153, 154, [155, 156, 157], (158, [159, 160], None), None),
    (162, 163, [164, 165, 166], None, None),
]
blocks = []
for ti, si, paras, bullets, tail in tech_cards:
    b = '<div class="techblock"><h3>%s</h3><p class="techblock__sub">%s</p>' % (t(ti), t(si))
    b += "".join(p(i) for i in paras)
    if bullets:
        lead, items, close = bullets
        b += "<p>%s</p><ul class=\"ulist\">%s</ul>" % (t(lead), "".join("<li>%s</li>" % t(i) for i in items))
        if close:
            b += p(close)
    if tail:
        b += p(tail)
    b += "</div>"
    blocks.append(b)

table_rows = [
    ("", "고주파", "초음파"),
    ("사용하는 에너지", "고주파 전기 에너지", "고주파 음파 에너지"),
    ("기본 원리", "조직의 저항을 이용해 열에너지 형성", "음파의 기계적 진동을 전달"),
    ("주요 설계 요소", "주파수, 전극 구조, 출력, 접촉 시간", "주파수, 출력, 초점 및 전달 방식"),
    ("홈뷰티 활용", "주로 피부 탄력·피부결 관리", "목적에 따라 피부 관리부터 집속 에너지 관리까지 다양"),
    ("핵심", "어디에 얼마나 일정하게 전달하는가", "어디에 어떤 방식으로 음파를 전달하는가"),
]
thead = "<tr><th></th><th>%s</th><th>%s</th></tr>" % (table_rows[0][1], table_rows[0][2])
tbody = "".join("<tr><th>%s</th><td>%s</td><td>%s</td></tr>" % r for r in table_rows[1:])

technology = """<section class="sec" id="basic">
  <div class="wrap">
    %s
    <h2>홈뷰티 디바이스 기술 바로 알기</h2>
    <div class="techblocks">%s</div>
  </div>
</section>

<section class="sec sec--grey" id="compare">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="ctable"><table>%s%s</table></div>
  </div>
</section>

<section class="sec" id="stamping">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
      <blockquote class="pullquote">%s<br>%s</blockquote>
      %s
    </div>
  </div>
</section>

<section class="sec sec--grey" id="why5">
  <div class="wrap">
    %s
    <div class="story__body">
      %s
      <ul class="ulist"><li>%s</li><li>%s</li><li>%s</li></ul>
      %s
      %s
      %s
    </div>
  </div>
</section>

<section class="sec" id="maptostamp">
  <div class="wrap">
    %s
    <div class="story__body">
      <p>%s<br>%s</p>
      %s
      %s
      <blockquote class="pullquote">%s<br>%s<br>%s<br>%s</blockquote>
      %s
    </div>
  </div>
</section>

<section class="sec sec--grey" id="patent">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      <p class="patent__no">%s</p>
    </div>
  </div>
</section>

<section class="sec" id="evidence">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <p class="mv__sub">%s</p>
    <div class="evid">
      <div class="evid__item"><b>—</b><span>콜라겐 발현</span></div>
      <div class="evid__item"><b>—</b><span>피부층 밀도</span></div>
      <div class="evid__item"><b>—</b><span>효능 평가</span></div>
    </div>
    <p class="note">* 수치는 시험성적서(콜라겐 발현 · 피부층 밀도 · 효능 평가) 확인 후 기입 예정입니다.</p>
  </div>
</section>""" % (
    label("BEAUTY DEVICE TECHNOLOGY", "기술 소개"),
    "".join(blocks),
    label("RF vs ULTRASOUND", "기술 비교"), t(144), thead, tbody,
    label("5 SEC. STAMPING", t(170)), t(169),
    p(171), p(172), p(173), p(174), t(175), t(176), p(177),
    label("WHY 5 SECONDS?", "왜 5초인가"),
    p(179),
    t(180), t(181), t(182),
    p(183), p(184), p(185),
    label("FROM MAP TO STAMP", "지도에서 스탬핑으로"),
    t(187), t(188), p(189), p(190),
    t(191), t(192), t(193), t(194),
    p(195),
    label("PATENTED TECHNOLOGY", t(200)), t(197),
    p(198), t(201),
    label("EVIDENCE", "시험 결과"), t(205), t(206),
)


# ───────────────────────────────── content_bodies.py 로 저장 (build_sub.py가 불러씀)
out = ['# -*- coding: utf-8 -*-', '"""케어클 제공 원고 기반 본문 — content_apply.py 가 생성합니다. 직접 수정하지 마세요."""', 'BODY = {}', '']
for key, html in [("about", about), ("greeting", story), ("aging-types", aging_types), ("technology", technology)]:
    out.append('BODY["%s"] = """%s"""' % (key, html))
    out.append('')
io.open("content_bodies.py", "w", encoding="utf-8").write(chr(10).join(out))
print("content_bodies updated")
