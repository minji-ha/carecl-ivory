# -*- coding: utf-8 -*-
"""careCL 회사소개 하위 페이지 6종 생성기.  python build_sub.py"""
import io
import parts

PAGES = [
    ("about",          "About careCL",     "회사소개"),
    ("greeting",       "CEO Message",      "인사말"),
    ("history",        "History",          "연혁"),
    ("certification",  "Certification",    "인증"),
    ("mission-vision", "Mission & Vision", "미션과 비전"),
    ("location",       "Location",         "오시는 길"),
]

def header():
    return parts.header(active="careCL")



def subvisual(slug, en, kr):
    tabs = "".join('<li><a href="%s.html"%s>%s</a></li>'
                   % (s, ' class="is-active"' if s == slug else "", k)
                   for s, e, k in PAGES)
    return ('<section class="subvisual">'
            '<img class="subvisual__img" src="assets/img/sub-visual.jpg" alt="">'
            '<div class="subvisual__fade"></div>'
            '<div class="subvisual__glow"></div>'
            '<div class="subvisual__inner">'
            '<p class="crumb">HOME &nbsp;/&nbsp; careCL &nbsp;/&nbsp; ' + kr + '</p>'
            '<h1>' + en + '</h1>'
            '<p class="kr">' + kr + '</p>'
            '</div></section>'
            '<nav class="submenu"><ul>' + tabs + '</ul></nav>')


FOOTER = parts.FOOTER


def label(en, kr):
    return '<div class="seclabel"><i></i><span>%s &nbsp;·&nbsp; %s</span></div>' % (en, kr)


BODY = {}

BODY["about"] = """<section class="sec">
  <div class="wrap">
    """ + label("ABOUT", "회사소개") + """
    <div class="about__grid">
      <div class="about__copy">
        <h2>클리닉의 기술을 집 안으로,<br>피부 노화의 기준을 다시 씁니다</h2>
        <p>케어클(careCL)은 보톡스 · 써마지 등 미용 시술 17년 경력의 전문가가 설립한 안티에이징 뷰티 브랜드입니다. 클리닉에서만 가능했던 고주파 스탬핑 기술을 홈케어 디바이스로 정제해, 누구나 매일의 루틴에서 사용할 수 있게 만들었습니다.</p>
        <p>나아가 얼굴을 22개 좌표로 나누어 개인의 노화 타입을 진단하는 Aging Map 22 체계를 구축하고, 진단 결과에 맞춘 케어 솔루션을 제안합니다.</p>
      </div>
      <div class="about__visual"><img src="assets/img/about-visual.jpg" alt="careCL"></div>
    </div>
    <dl class="facts">
      <div><dt>CEO</dt><dd>최형규 Hyungkyu Choi</dd></div>
      <div><dt>HEADQUARTERS</dt><dd>경기도 고양시 일산동구 동국로 32</dd></div>
      <div><dt>BUSINESS</dt><dd>뷰티 디바이스 · 코스메틱</dd></div>
      <div><dt>CLINICAL</dt><dd>콜라겐 생성 2.23배 임상 완료</dd></div>
    </dl>
  </div>
</section>"""

BODY["greeting"] = """<section class="sec sec--grey">
  <div class="wrap">
    <div class="ceo">
      <div class="ceo__visual" id="brandParticles"><canvas aria-label="careCL"></canvas><div class="ceo__visual-grid" aria-hidden="true"></div><div class="ceo__visual-top"><span>AGELESS BEAUTY</span></div></div>
      <div>
        """ + label("CEO MESSAGE", "인사말") + """
        <blockquote>피부의 시간을<br>다시 설계합니다</blockquote>
        <div class="ceo__body"><p>아름다움은 한순간의 인상이 아니라, 시간 위에 축적되는 결과입니다. 그리고 그 시간은 모두에게 같은 속도로 흐르지 않습니다. 노화가 시작되는 부위와 진행되는 방식은 사람마다 다르며, 그 차이를 정확히 이해하는 데서 진정한 안티에이징이 시작됩니다.</p><p>케어클은 이 차이를 과학의 언어로 읽어냅니다. 얼굴을 22개의 좌표로 정밀하게 분석하는 Aging Map 22는 막연한 관리를 측정 가능한 기준으로 전환하는 새로운 체계입니다. 개인의 피부가 지닌 고유한 흐름을 정의하고, 그에 맞는 가장 정확한 해답을 제시합니다.</p><p>기술은 신뢰 위에서만 가치를 가집니다. 케어클의 모든 제품은 임상으로 검증된 원리와 엄격한 품질 기준을 바탕으로 설계되며, 클리닉의 전문성을 일상의 루틴 안에서 온전히 구현하는 것을 목표로 합니다.</p><p>케어클은 피부 과학의 경계를 넓히며, 세계 어디에서나 신뢰받는 안티에이징의 새로운 기준이 되겠습니다. 시간 앞에서 더욱 당당한 아름다움, 그 여정에 케어클이 함께하겠습니다.</p></div>
        <div class="ceo__sign"><span>careCL 대표이사</span><b>최형규 &nbsp;Hyungkyu Choi</b></div>
      </div>
    </div>
  </div>
</section>"""

HISTORY_DATA = [
    ("2026", [("05", "GRID MASK TECH FIT 콜라겐 마스크팩 출시"),
              ("05", "Aging Map 22 진단 체계 구축 (얼굴 22개 좌표)"),
              ("02", "TECH FIT 스탬핑 고주파 디바이스 글로벌 출시"),
              ("02", "콜라겐 생성 2.23배 증가 임상 완료")]),
    ("2025", [("04", "careCL CLB 고주파 마사지기 출시"),
              ("—", "통신판매업 신고 · 온라인 스토어 오픈 (제2025-고양일산동-0585호)")]),
    ("2024", [("11", "케어클 라이트 토닝 세럼 출시"),
              ("09", "피렌체백 — CLB 전용 보관 가죽 케이스 출시")]),
    ("2023", [("12", "careCL Collagen Gel 출시 — 피부 자극 지수 0.00")]),
]
_groups = ""
for _year, _items in HISTORY_DATA:
    _lis = "".join('<div class="tl-item"><em>%s</em><p>%s</p></div>' % (m, t) for m, t in _items)
    _groups += ('<div class="tl-group"><div class="tl-year">%s</div>'
                '<div class="tl-dot"><i></i></div><div class="tl-items">%s</div></div>' % (_year, _lis))

BODY["history"] = """<section class="sec">
  <div class="wrap">
    """ + label("HISTORY", "연혁") + """
    <p class="history__title">정밀한 안티에이징을 만들기 위해<br>케어클이 걸어온 길</p>
    <p class="note">* 제품 출시 시점 기준 · 실제 사내 연혁으로 교체 필요</p>
    <div class="timeline">""" + _groups + """</div>
    <div class="history__img"><em>IMAGE 1500 × 420</em><span>연구·생산 현장 또는 제품 라인업 와이드 컷</span></div>
  </div>
</section>"""

CERTS = [("특허증", "고주파 스탬핑 전극 구조"), ("특허증", "피부 접촉 온도 제어 모듈"),
         ("디자인등록증", "TECH FIT 뷰티 디바이스"), ("상표등록증", "careCL / 케어클"),
         ("임상시험 결과보고서", "콜라겐 생성 2.23배 증가"), ("피부자극 시험성적서", "자극 지수 0.00 무자극"),
         ("KC 안전확인 신고증명서", "가정용 고주파 미용기기"), ("CE 적합성 인증서", "유럽 수출용 적합성 평가")]
_cards = "".join(
    '<div class="cert">'
    '<div class="cert__img"><div class="cert__paper">'
    '<i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><i class="seal"></i>'
    '</div></div>'
    '<h3>%s</h3><p>%s</p></div>' % (n, d) for n, d in CERTS)

BODY["certification"] = """<section class="sec sec--grey">
  <div class="wrap">
    """ + label("CERTIFICATION", "인증") + """
    <h2>보유 특허 및 인증</h2>
    <p class="note" style="margin-top:20px">* 시안용 예시 — 실제 보유 인증서 이미지로 교체 필요</p>
    <div class="certs">""" + _cards + """</div>
  </div>
</section>"""

PILLARS = [
    ("MISSION", "피부 노화를 측정 가능한 언어로",
     "감에 의존하던 안티에이징을 22개 좌표와 6가지 타입이라는 측정 가능한 기준으로 바꿉니다.",
     "얼굴 좌표 그리드 / 진단 화면 이미지"),
    ("VISION", "모두에게 다른 솔루션을",
     "같은 제품을 모두에게 권하지 않습니다. 진단 결과와 구매 이력에 따라 개인에게 맞는 루틴을 제안합니다.",
     "개인별 리포트 또는 맞춤 루틴 연출 컷"),
    ("VALUE", "임상으로 증명한 것만",
     "마케팅 언어가 아니라 임상 데이터와 시험 성적으로 증명된 기술만 제품에 담습니다.",
     "연구실 / 임상 테스트 현장 컷"),
]
import os


def _pillar_img(key, desc):
    """assets/img/mission.jpg · vision.jpg · value.jpg 가 있으면 이미지, 없으면 플레이스홀더"""
    for ext in ("jpg", "jpeg", "png", "webp"):
        f = "assets/img/%s.%s" % (key.lower(), ext)
        if os.path.exists(f):
            return '<div class="pillar__img has-img"><img src="%s" alt="%s"></div>' % (f, key)
    return '<div class="pillar__img"><em>IMAGE 476 × 320</em><span>%s</span></div>' % desc


_pillars = "".join(
    '<div class="pillar">' + _pillar_img(k, img) +
    '<h3>%s</h3><h4>%s</h4><p>%s</p></div>' % (k, t, d)
    for k, t, d, img in PILLARS)

BODY["mission-vision"] = """<section class="sec sec--grey">
  <div class="wrap">
    """ + label("MISSION & VISION", "미션과 비전") + """
    <h2>정확히 읽어내고,<br>정확히 케어한다</h2>
    <p class="mv__en">Read precisely, care exactly.</p>
    <p class="mv__sub">감에 의존하던 안티에이징을 측정 가능한 기준으로 바꾸고, 모두에게 같은 제품을 권하지 않는 것.<br>케어클이 일하는 방식은 이 두 문장에서 출발합니다.</p>
    <div class="pillars">""" + _pillars + """</div>
  </div>
</section>"""

BODY["location"] = """<section class="sec">
  <div class="wrap">
    """ + label("LOCATION", "오시는 길") + """
    <h2>케어클에서 만나요</h2>
    <div class="map"><span class="map__pin"></span><span class="map__label">GOOGLE MAPS EMBED</span></div>
    <dl class="locinfo">
      <div><dt>ADDRESS</dt><dd><p class="m">경기도 고양시 일산동구 동국로 32<br>산학협력관 2층 234호</p><p class="s">Rm 234, 2F, Sanhak Cooperation Hall,<br>32 Dongguk-ro, Ilsandong-gu, Goyang-si, Korea</p></dd></div>
      <div><dt>CONTACT</dt><dd><p class="m">+82 31-943-1028</p><p class="s">support@carecl.co.kr</p></dd></div>
      <div><dt>HOURS</dt><dd><p class="m">Mon – Fri &nbsp;10:00 – 18:00</p><p class="s">Lunch 12:00 – 13:00 / 주말 · 공휴일 휴무</p></dd></div>
    </dl>
  </div>
</section>"""

TPL = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(kr)s | careCL 케어클</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="libs/fontawesome/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=2609130353">
<link rel="stylesheet" href="css/nav.css?v=2609130353">
<link rel="stylesheet" href="css/sub.css?v=2609130353">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Noto+Serif+KR:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/theme-ivory.css">
</head>
<body class="sub">

%(header)s

<main>
%(subvisual)s
%(body)s
</main>

%(footer)s

<script src="libs/lenis.min.js"></script>
<script src="libs/gsap.min.js"></script>
<script src="libs/ScrollTrigger.min.js"></script>
<script src="js/sub.js?v=2609130353"></script>
<script src="js/particletext.js"></script>
<script src="js/nav.js?v=2609130353"></script>
</body>
</html>
"""

for slug, en, kr in PAGES:
    html = TPL % {"kr": kr, "header": header(),
                  "subvisual": subvisual(slug, en, kr),
                  "body": BODY[slug], "footer": FOOTER}
    io.open(slug + ".html", "w", encoding="utf-8").write(html)
    print("built", slug + ".html")
