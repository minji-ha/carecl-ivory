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


def figure(img, cap_en, cap_kr, tone=""):
    """본문 중간에 들어가는 풀블리드 이미지 — stembeauty 식 여백 큰 비주얼 브레이크"""
    return ('<section class="figbreak%s">'
            '<div class="figbreak__img"><img src="assets/img/%s" alt=""></div>'
            '<div class="figbreak__cap"><em>%s</em><span>%s</span></div>'
            '</section>') % (tone, img, cap_en, cap_kr)


def label(en, kr):
    if not en and not kr:
        return ""
    return '<div class="seclabel"><i></i><span>%s &nbsp;·&nbsp; %s</span></div>' % (en, kr)


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
      <div class="about__visual"><img src="assets/img/about-visual.jpg" alt="careCL"></div>
    </div>
    <dl class="facts">
      <div><dt>CEO</dt><dd>최형규 Hyungkyu Choi</dd></div>
      <div><dt>HEADQUARTERS</dt><dd>경기도 고양시 일산동구 동국로 32</dd></div>
      <div><dt>BUSINESS</dt><dd>뷰티 디바이스 · 코스메틱</dd></div>
      <div><dt>TECHNOLOGY</dt><dd>5 SEC. STAMPING RF</dd></div>
    </dl>
  </div>
</section>""" % (label("ABOUT CARECL", "회사 소개"), t(1), ps(2, 3, 4), plines(5, 6))


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
    label("OUR STORY", "브랜드 스토리"), t(12),
    ps(13, 14), pjoin(15, 16), ps(17, 18),
    plines(19, 20, 21, 22), ps(23, 24, 25),
    label("UNDERSTAND FIRST", "사람을 먼저 이해합니다"), t(26),
    ps(27, 28, 29, 30, 31),
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
        worry = '<p class="type__worry"><em>%s</em>%s</p>' % (t(ci - 1), t(ci))
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
    label("", ""), t(46),
    ps(47, 48), plines(49, 50, 51, 52), p(53), p(54), ps(55, 56, 57), plines(58, 59),
    label("6 AGING TYPES", "유형별 특징"), t(70),
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
    label("6 AGING TYPES", "6가지 노화 타입"), t(62),
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
    label("5 SEC. STAMPING", "정해진 위치에, 정해진 시간"), t(169),
    p(170), ps(171, 172, 173, 174), plines(175, 176) + p(177),
    label("WHY 5 SECONDS?", "왜 5초인가"),
    p(179), ul(180, 181, 182), p(183), ps(184, 185),
    label("FROM MAP TO STAMP", "지도에서 스탬핑으로"),
    plines(187, 188), ps(189, 190),
    p(191), plines(192, 193, 194), p(195),
    label("PATENTED TECHNOLOGY", "특허 기술"), t(197),
    p(198), t(201),
    label("EVIDENCE", "시험 결과"), t(205), t(206),
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


certification = """<section class="sec">
  <div class="wrap">
    %s
    <h2>국제 인증과 품질 경영 체계</h2>
    <p class="mv__sub">케어클이 보유한 인증서를 원문 그대로 확인하실 수 있습니다.</p>
    %s
    <p class="note" style="margin-top:28px">* 인증서 원본(병합본)을 PDF로 제공합니다. 개별 인증서가 필요하시면 문의해 주세요.</p>
  </div>
</section>""" % (
    label("AWARDS & CERTIFICATION", "수상 · 인증"),
    doclist([("CE · FCC · ISO 9001 · ISO 14001 인증서", "주식회사 케어클 인증 병합본",
              "assets/docs/carecl-certifications.pdf", "1.1MB")]),
)


rnd = """<section class="sec">
  <div class="wrap">
    %s
    <h2>특허 기술</h2>
    <div class="story__body">%s</div>
    %s
  </div>
</section>

<section class="sec sec--grey">
  <div class="wrap">
    %s
    <h2>시험 성적서</h2>
    <p class="mv__sub">TECH FIT · GRID MASK TECH FIT은 외부 시험기관에서 콜라겐 발현, 효능 평가, 피부층 밀도 시험을 진행했습니다.</p>
    <p class="note" style="margin-top:24px">* 시험 성적서 원문은 비공개 자료입니다. 필요하신 경우 support@carecl.co.kr 로 문의해 주세요.</p>
  </div>
</section>""" % (
    label("PATENT", "특허"), p(198),
    doclist([("주식회사 케어클 특허 병합본", "대한민국 등록특허 제10-2938674호",
              "assets/docs/carecl-patents.pdf", "974KB")]),
    label("TEST REPORT", "시험 성적서"),
)


# ───────────────────────────────── content_bodies.py 로 저장
out = ["# -*- coding: utf-8 -*-",
       '"""케어클 제공 원고 기반 본문 — content_apply.py 가 생성합니다. 직접 수정하지 마세요."""',
       "BODY = {}", ""]
# 본문 사이사이에 기존 carecl.com 비주얼을 넣는다
FIG_MODEL = figure("cc-model-c.jpg", "DESIGNED BY BOTOX &amp; THERMAGE EXPERTS", "임상 현장의 감각을 그대로 홈케어로")
FIG_LINEUP = figure("cc-lineup-c.jpg", "CLINIC-LEVEL EXPERTISE", "디바이스와 전용 코스메틱의 한 세트")
FIG_STAMPING = figure("cc-stamping-c.jpg", "STAMPING, INSPIRED BY REAL PROCEDURES", "정해진 자리에 5초, 눌러서 전달합니다", " figbreak--dark")


def insert_before(html, marker, block):
    i = html.find(marker)
    return html if i < 0 else html[:i] + block + chr(10) + html[i:]


about = insert_before(about, '<dl class="facts">', "")
story = story.replace('<section class="sec sec--grey" id="understand">',
                      FIG_MODEL + chr(10) + '<section class="sec sec--grey" id="understand">')
technology = insert_before(technology, '<section class="sec" id="stamping">', FIG_STAMPING)
aging_types_full = aging_why + chr(10) + aging_types
certification = certification + chr(10) + FIG_LINEUP

for key, html in [("about", about + chr(10) + FIG_MODEL), ("greeting", story),
                  ("aging-types", aging_types_full), ("technology", technology),
                  ("certification", certification), ("rnd", rnd)]:
    out.append('BODY["%s"] = """%s"""' % (key, html))
    out.append("")
io.open("content_bodies.py", "w", encoding="utf-8").write(chr(10).join(out))
print("content_bodies updated")
