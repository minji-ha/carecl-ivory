# -*- coding: utf-8 -*-
"""케어클 제공 원고(자료/홈페이지 컨텐츠_261007.docx)를 서브 페이지에 그대로 반영.
   - 본문은 자료/content_rich.txt 에서 가져온다 (원문 + 원문의 굵게 강조 그대로)
   - 강조는 원문에서 굵게 처리된 부분만 사용한다
   python content_apply.py"""
import io

SRC = r"C:\work\carecl\자료\content_rich.txt"
L = io.open(SRC, encoding="utf-8").read().split("\n")


def t(i):
    """원문 한 줄 (이미 이스케이프 + <strong> 처리됨)"""
    return L[i].strip()


def p(i):
    return "<p>%s</p>" % t(i)


def ps(*idx):
    return "".join(p(i) for i in idx)


def pjoin(*idx):
    """여러 줄을 한 문단으로 — 줄바꿈이 자연스럽게 흐르도록"""
    return "<p>%s</p>" % " ".join(t(i) for i in idx)


def plines(*idx):
    """원문의 줄바꿈을 그대로 살리는 문단"""
    return "<p>%s</p>" % "<br>".join(t(i) for i in idx)


def ul(*idx):
    return '<ul class="ulist">%s</ul>' % "".join("<li>%s</li>" % t(i) for i in idx)


def figure(img, cap_en, cap_kr, tone="", width=0):
    """본문 중간 비주얼 — width를 주면 원본 해상도를 넘기지 않도록 폭을 제한한다"""
    st = ' style="--fw:%dpx"' % width if width else ''
    return ('<section class="figbreak%s"%s>'
            '<div class="figbreak__img"><img src="assets/img/%s" alt=""></div>'
            '<div class="figbreak__cap"><em>%s</em><span>%s</span></div>'
            '</section>') % (tone, st, img, cap_en, cap_kr)


def split(img, h3, body, rev=False):
    """이미지 + 카피 2단 블록"""
    return ('<section class="sec"><div class="wrap"><div class="splitfig%s">'
            '<div class="splitfig__img"><img src="assets/img/%s" alt=""></div>'
            '<div class="splitfig__copy"><h3>%s</h3><p>%s</p></div>'
            '</div></div></section>') % (" splitfig--rev" if rev else "", img, h3, body)


def label(en, kr):
    if not en and not kr:
        return ""
    txt = '%s &nbsp;·&nbsp; %s' % (en, kr) if kr else en
    return '<div class="seclabel"><i></i><span>%s</span></div>' % txt


# ───────────────────────────────── About careCL
about = """<section class="sec">
  <div class="wrap">
    %s
    <div class="about__grid">
      <div class="about__copy">
        <h2>%s</h2>
        <div class="story__body">
          %s
          %s
        </div>
      </div>
      <div class="about__visual"><img src="assets/img/cc-model-c.jpg" alt="careCL"></div>
    </div>
    <dl class="facts">
      <div><dt>CEO</dt><dd>최형규 Hyungkyu Choi</dd></div>
      <div><dt>HEADQUARTERS</dt><dd>경기도 고양시 일산동구 동국로 32</dd></div>
      <div><dt>BUSINESS</dt><dd>뷰티 디바이스 · 코스메틱</dd></div>
      <div><dt>TECHNOLOGY</dt><dd>5 SEC. STAMPING RF</dd></div>
    </dl>
  </div>
</section>""" % (label("ABOUT CARECL", ""), t(1), ps(2, 3, 4), plines(5, 6))


# ───────────────────────────────── Our Story
story = """<section class="sec" id="born">
  <div class="wrap">
    %s
    <div class="ceo">
      <div class="ceo__visual" id="brandParticles"><canvas aria-label="careCL"></canvas><div class="ceo__visual-grid"></div><div class="ceo__visual-top"><span>AGELESS BEAUTY</span></div></div>
      <div class="ceo__text">
        <h2>%s</h2>
        <div class="story__body">
          %s
          %s
          %s
          %s
          %s
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--grey" id="understand">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
    </div>
  </div>
</section>

<section class="sec" id="home">
  <div class="wrap">
    <div class="story__body">
      %s
      %s
    </div>
    <div class="story__cta"><a href="aging-types.html" class="btn btn--primary">6가지 노화 타입 보기 <span>→</span></a></div>
  </div>
</section>""" % (
    label("OUR STORY", ""), t(12),
    ps(13, 14), pjoin(15, 16), ps(17, 18),
    plines(19, 20, 21, 22), ps(23, 24, 25),
    label("UNDERSTAND FIRST", ""), "사람을 먼저 이해합니다",
    p(26) + ps(27, 28, 29, 30, 31),
    plines(32, 33, 34),
    ps(35, 36),
    plines(37, 38, 39), p(40),
)


# ───────────────────────────────── AGING LAB
types = [(71, 72, 73, 75), (77, 78, 79, 81), (83, 84, 85, 87),
         (89, 90, 91, 93), (95, 96, 97, 99), (101, 102, 103, None)]
cards = []
for no, (ti, qi, di, ci) in enumerate(types, start=1):
    if ci is None:
        body = "<p>%s</p><p>%s</p><p>%s</p>" % (t(103), t(104), t(105))
        worry = ""
    else:
        body = "<p>%s</p>" % t(di)
        worry = '<p class="type__worry"><em>%s</em><span>%s</span></p>' % (t(ci - 1), t(ci))
    cards.append(
        '<div class="typecard"><span class="typecard__no">%02d</span>'
        '<h4>%s</h4><p class="typecard__quote">%s</p>%s%s</div>'
        % (no, t(ti), t(qi), body, worry)
    )

aging_types = """<section class="sec" id="types">
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
    </div>
  </div>
</section>

<section class="sec sec--grey" id="list">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="typecards">%s</div>
  </div>
</section>

<section class="sec" id="next">
  <div class="wrap">
    <h2>%s</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
    </div>
    <div class="story__cta">
      <a href="aging-map.html" class="btn btn--primary">AGING MAP 22 보기 <span>→</span></a>
      <a href="survey.html" class="btn btn--ghost">나의 타입 알아보기 <span>→</span></a>
    </div>
  </div>
</section>""" % (
    label("6 AGING TYPES", ""), t(47),
    p(48), plines(49, 50, 51, 52), p(53), p(54), ps(55, 56, 57), plines(58, 59),
    label("TYPE 01 — 06", ""), t(70),
    "".join(cards),
    t(107),
    ps(108, 109, 110), p(111), p(112), plines(113, 114),
)


aging_why = """<section class="sec" id="why">
  <div class="wrap">
    %s
    <h2>%s</h2>
    <div class="story__body">
      %s
    </div>
  </div>
</section>""" % (
    label(t(61), ""), t(62),
    ps(63, 64, 65, 66, 67, 68, 69),
)


# ───────────────────────────────── TECHNOLOGY
tech_cards = [
    ("rf", 119, 120, [121, 122, 123, 124], (125, [126, 127, 128], 129), 130),
    ("us", 132, 133, [134, 135, 136, 137, 138], (139, [140, 141, 142], None), None),
    ("ems", 147, 148, [149, 150, 151], None, None),
    ("micro", 153, 154, [155, 156, 157], (158, [159, 160], None), None),
    ("ep", 162, 163, [164, 165, 166], None, None),
]
blocks = []
for bid, ti, si, paras, bullets, tail in tech_cards:
    b = '<div class="techblock" id="%s"><h3>%s</h3><p class="techblock__sub">%s</p>' % (bid, t(ti), t(si))
    b += ps(*paras)
    if bullets:
        lead, items, close = bullets
        b += p(lead) + ul(*items)
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
    </div>
  </div>
</section>

<section class="sec sec--grey" id="why5">
  <div class="wrap">
    %s
    <h2>왜 5초인가</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
    </div>
  </div>
</section>

<section class="sec" id="maptostamp">
  <div class="wrap">
    %s
    <h2>지도에서 스탬핑으로</h2>
    <div class="story__body">
      %s
      %s
      %s
      %s
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
      <p class="patent__ttl">%s</p><p class="patent__no">%s</p>
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
    label("BEAUTY DEVICE TECHNOLOGY", ""),
    "".join(blocks),
    label("RF vs ULTRASOUND", ""), t(144), thead, tbody,
    label("5 SEC. STAMPING", ""), t(170),
    p(169), ps(171, 172, 173, 174), plines(175, 176) + p(177),
    label("WHY 5 SECONDS?", ""),
    p(179), ul(180, 181, 182), p(183), ps(184, 185),
    label("FROM MAP TO STAMP", ""),
    plines(187, 188), ps(189, 190),
    p(191), plines(192, 193, 194), p(195),
    label("PATENTED TECHNOLOGY", ""), "특허 기술",
    p(198), t(200), t(201),
    label("EVIDENCE", ""), t(205), t(206),
)


# ───────────────────────────────── 인증 · 특허 (PDF 목록)
def doclist(items):
    rows = []
    for title, desc, href, size in items:
        rows.append(
            '<a class="doc" href="%s" target="_blank" rel="noopener">'
            '<span class="doc__ico"><i class="fa-regular fa-file-pdf"></i></span>'
            '<span class="doc__txt"><b>%s</b><em>%s</em></span>'
            '<span class="doc__meta">PDF · %s</span></a>' % (href, title, desc, size)
        )
    return '<div class="docs">%s</div>' % "".join(rows)


CERT_CARDS = """<div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-ce.jpg" alt="CE" loading="lazy"></span><span class="docrow__txt"><b>CE</b><span class="docrow__desc">Declaration of Conformity · EMC 2014/30/EU</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-fcc.jpg" alt="FCC" loading="lazy"></span><span class="docrow__txt"><b>FCC</b><span class="docrow__desc">Supplier's Declaration of Conformity · CFR47 Part 15 Subpart B</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-iso9001-en.jpg" alt="ISO 9001:2015" loading="lazy"></span><span class="docrow__txt"><b>ISO 9001:2015</b><span class="docrow__desc">Quality Management System · TQCSI</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-iso9001-kr.jpg" alt="ISO 9001:2015" loading="lazy"></span><span class="docrow__txt"><b>ISO 9001:2015</b><span class="docrow__desc">품질경영시스템 인증서 · TQCSI</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-iso14001-en.jpg" alt="ISO 14001:2015" loading="lazy"></span><span class="docrow__txt"><b>ISO 14001:2015</b><span class="docrow__desc">Environmental Management System · TQCSI</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/cert-iso14001-kr.jpg" alt="ISO 14001:2015" loading="lazy"></span><span class="docrow__txt"><b>ISO 14001:2015</b><span class="docrow__desc">환경경영시스템 인증서 · TQCSI</span></span></div>"""

PATENT_CARDS = """<div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/patent-2938674.jpg" alt="제 10-2938674 호" loading="lazy"></span><span class="docrow__txt"><b>제 10-2938674 호</b><span class="docrow__desc">피부 접촉에 따른 전압 증폭 및 반복 출력 제어를 이용한 고주파 스탬핑 피부 미용 방법</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/patent-2799588.jpg" alt="제 10-2799588 호" loading="lazy"></span><span class="docrow__txt"><b>제 10-2799588 호</b><span class="docrow__desc">고강도 집속 초음파 원형 조사와 범위 조절 가능한 고주파 스탬핑 기능을 통합한 휴대용 피부 마사지기</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/patent-2799593.jpg" alt="제 10-2799593 호" loading="lazy"></span><span class="docrow__txt"><b>제 10-2799593 호</b><span class="docrow__desc">고강도 집속 초음파의 반경 조절이 가능한 휴대용 피부 마사지기</span></span></div><div class="docrow"><span class="docrow__thumb"><img src="assets/img/doc/patent-1647183.jpg" alt="제 10-1647183 호" loading="lazy"></span><span class="docrow__txt"><b>제 10-1647183 호</b><span class="docrow__desc">치료약물 및 세포전달용 마이크로입자 및 이의 제조방법</span></span></div>"""


certification = """<section class="sec">
  <div class="wrap">
    %s
    <h2>국제 인증과 품질 경영 체계</h2>
    <p class="mv__sub">특허청 · 인증기관에서 발급한 인증서 원본입니다. 이미지를 클릭하면 크게 볼 수 있습니다.</p>
    <div class="docgrid">%s</div>
  </div>
</section>""" % (
    label("AWARDS & CERTIFICATION", ""),
    CERT_CARDS,
)


rnd = """<section class="sec">
  <div class="wrap">
    %s
    <h2>등록 특허</h2>
    <div class="story__body">%s</div>
    <div class="docgrid">%s</div>
    <p class="note" style="margin-top:28px">* 개인정보(법인등록번호 · 발명자 인적사항)는 가린 상태로 공개합니다. 원본이 필요하시면 support@carecl.co.kr 로 문의해 주세요.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    %s
    <h2>시험 성적서</h2>
    <p class="mv__sub">TECH FIT · GRID MASK TECH FIT은 외부 시험기관에서 콜라겐 발현, 효능 평가, 피부층 밀도 시험을 진행했습니다.</p>
    <p class="note" style="margin-top:24px">* 시험 성적서 원문은 비공개 자료입니다. 필요하신 경우 support@carecl.co.kr 로 문의해 주세요.</p>
  </div>
</section>""" % (
    label("PATENT", ""), p(198),
    PATENT_CARDS,
    label("TEST REPORT", ""),
)


# ───────────────────────────────── content_bodies.py 로 저장
out = ["# -*- coding: utf-8 -*-",
       '"""케어클 제공 원고 기반 본문 — content_apply.py 가 생성합니다. 직접 수정하지 마세요."""',
       "BODY = {}", ""]
# 본문 사이사이에 기존 carecl.com 비주얼을 넣는다
FIG_MODEL = figure("p-touch.jpg", "DESIGNED BY BOTOX &amp; THERMAGE EXPERTS", "임상 현장의 감각을 그대로 홈케어로")
FIG_LINEUP = ""
FIG_STAMPING = figure("p-mask-close.jpg", "STAMPING, INSPIRED BY REAL PROCEDURES", "정해진 자리에 5초, 눌러서 전달합니다", width=760)


def insert_before(html, marker, block):
    i = html.find(marker)
    return html if i < 0 else html[:i] + block + chr(10) + html[i:]



story = story.replace('<section class="sec sec--grey" id="understand">',
                      FIG_MODEL + chr(10) + '<section class="sec sec--grey" id="understand">')
# TECHNOLOGY는 2뎁스 2개 → 페이지 2개로 나눈다
_i = technology.index('<section class="sec" id="stamping">')
tech_basic = technology[:_i].rstrip() + chr(10) + split("p-eye.jpg", "에너지를 어디에, 얼마나 일정하게", "같은 기술이라도 전달하는 위치와 시간, 접촉 방식에 따라 결과는 달라집니다. 케어클은 그 조건을 고정했습니다.")
_j = technology.index('<section class="sec sec--grey" id="why5">')
tech_carecl = technology[_i:_j].rstrip() + chr(10) + FIG_STAMPING + chr(10) + technology[_j:]
aging_types_full = aging_why + chr(10) + aging_types

story = story.replace('<section class="sec" id="home">',
    split("p-leaning.jpg",
          "집에서, 매일, 같은 방식으로",
          "클리닉에서 쌓인 기준을 매일의 루틴으로 옮겼습니다. 같은 자리에 같은 시간, 반복할 수 있는 관리가 변화를 만듭니다.",
          rev=True) + chr(10) + '<section class="sec" id="home">')

aging_types_full = aging_types_full.replace('<section class="sec" id="next">',
    split("p-skin.jpg",
          "노화는 한 가지 모양이 아닙니다",
          "피부결, 탄력, 톤, 윤곽 — 먼저 나타나는 변화가 사람마다 다릅니다. 그래서 관리의 출발점도 달라야 합니다.")
    + chr(10) + '<section class="sec" id="next">')

tech_carecl = tech_carecl + chr(10) + split("p-mask-device.jpg",
    "그리드 위에, 정확한 위치로",
    "그리드 마스크가 관리 부위를 안내하고, 디바이스는 그 자리에 5초 동안 에너지를 전달합니다.", rev=True)

for key, html in [("about", about), ("greeting", story),
                  ("aging-types", aging_types_full), ("technology", tech_basic),
                  ("carecl-technology", tech_carecl),
                  ("certification", certification), ("rnd", rnd)]:
    out.append('BODY["%s"] = """%s"""' % (key, html))
    out.append("")
io.open("content_bodies.py", "w", encoding="utf-8").write(chr(10).join(out))
print("content_bodies updated")
