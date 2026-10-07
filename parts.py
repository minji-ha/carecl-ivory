# -*- coding: utf-8 -*-
"""careCL 공통 파츠 (헤더 / 전체메뉴 / 푸터).  build_sub.py · apply_nav.py 에서 사용"""

# (라벨, 링크, [(하위라벨, 하위링크), ...])
# 노션 "케어클 홈페이지 구성" 기준 3뎁스 구조
# (1뎁스 라벨, 링크, [(2뎁스 라벨, 링크, [(3뎁스 라벨, 링크), ...]), ...])
MENU = [
    ("COMPANY", "about.html", [
        ("About careCL", "about.html", []),
        ("Our Story", "greeting.html", [
            ("보톡스 써마지 업계 경험 born from botox &amp; Thermage", "greeting.html#born"),
            ("노화에 대한 이해와 관리 설계의 중요성", "greeting.html#understand"),
            ("홈 에이징 케어로 이어진 배경", "greeting.html#home"),
        ]),
        ("R&D / Patent", "rnd.html", []),
        ("Awards & Certification", "certification.html", []),
    ]),
    ("AGING LAB", "aging-types.html", [
        ("6 AGING TYPES", "aging-types.html", [
            ("Why We Age Differently", "aging-why.html"),
            ("6 Aging Types", "aging-types.html#list"),
            ("유형별 특징", "aging-types.html#list"),
            ("유형별 주요 고민", "aging-types.html#list"),
            ("나의 Aging Type 알아보기", "survey.html"),
        ]),
        ("AGING MAP 22", "aging-map.html", [
            ("Why Aging Map 22", "aging-map.html#why"),
            ("6 Aging Types × 22 Areas", "aging-map.html#matrix"),
            ("Face / Neck &amp; Body", "aging-map.html#areas"),
            ("22개 관리 부위", "aging-map.html#areas"),
            ("부위별 노화 특징", "aging-map.html#areas"),
            ("우선 관리 부위", "aging-map.html#care"),
            ("Personalized Care", "aging-map.html#care"),
        ]),
    ]),
    ("TECHNOLOGY", "technology.html", [
        ("Beauty Device Technology", "technology.html#basic", [
            ("RF", "technology.html#rf"),
            ("Ultrasound", "technology.html#us"),
            ("EMS", "technology.html#ems"),
            ("Microcurrent", "technology.html#micro"),
            ("Electroporation", "technology.html#ep"),
        ]),
        ("careCL Technology", "technology.html#stamping", [
            ("5 SEC. STAMPING", "technology.html#stamping"),
            ("왜 문지르는 방식이 아니라 스탬핑인가", "technology.html#stamping"),
            ("정해진 위치 / 정해진 시간", "technology.html#why5"),
            ("특허 기술", "technology.html#patent"),
            ("관련 시험 및 임상", "technology.html#evidence"),
            ("TECHFIT에 적용된 RF · EP · Microcurrent · EMS", "technology.html#maptostamp"),
        ]),
    ]),
    ("PRODUCTS", "products.html", [
        ("BEAUTY DEVICE", "products.html#device", [
            ("TECHFIT", "products.html#device"),
            ("CLB", "products.html#device"),
            ("향후 Device", "products.html#device"),
        ]),
        ("COSMETICS", "products.html#cosmetics", [
            ("Collagen Booster Gel", "products.html#cosmetics"),
            ("Grid Mask", "products.html#cosmetics"),
            ("Toning Serum", "products.html#cosmetics"),
            ("향후 Cosmetics", "products.html#cosmetics"),
        ]),
    ]),
    ("CONTACT", "contact.html", [
        ("Global Business", "contact.html#global", []),
        ("Distributor / Partnership", "contact.html#partner", []),
        ("Media / PR", "contact.html#pr", []),
        ("General Inquiry", "contact.html#inquiry", []),
    ]),
]

AI_BADGE = (
    '<span class="aibadge" aria-hidden="true">'
    '<span class="aibadge__circle">'
    '<svg viewBox="0 0 24 24" fill="none">'
    '<path d="M12 2.2 14 8.4 20.2 10.4 14 12.4 12 18.6 10 12.4 3.8 10.4 10 8.4Z" fill="currentColor"/>'
    '<circle cx="19.4" cy="4.2" r="1.7" fill="currentColor" opacity=".9"/>'
    '<circle cx="4.8" cy="18.4" r="1.2" fill="currentColor" opacity=".7"/>'
    '</svg>'
    '</span>'
    '<span class="aibadge__txt">AI 피부 진단</span>'
    '</span>'
)


DROPDOWN_ONLY = [m[0] for m in MENU]   # 전 메뉴 드롭다운 노출


def header(active=None, logo_href="index.html", start_href="survey.html"):
    def item(label, href, subs):
        if label not in DROPDOWN_ONLY:
            subs = []
        cls = ' class="is-active"' if active == label else ''
        badge = AI_BADGE if label == "AGING LAB" else ""
        drop = ''
        if subs:
            # GNB 드롭다운은 2뎁스까지만 (3뎁스는 각 페이지 상단 앵커 바에서 노출)
            links = "".join('<a class="dropdown__d2" href="%s">%s</a>' % (shref, stitle)
                            for stitle, shref, thirds in subs)
            drop = '<div class="dropdown"><div class="dropdown__inner">%s</div></div>' % links
        return ('<div class="navitem%s"><a href="%s"%s>%s</a>%s%s</div>'
                % (' has-badge' if badge else '', href, cls, label, badge, drop))

    nav = "".join(item(*m) for m in MENU)
    rows = [
        '<div class="announce">',
        '  <span class="announce__dot"></span>',
        '  <span>AGING MAP 22 진단 오픈 — 2분 설문으로 나의 노화 타입 확인하기</span>',
        '</div>',
        '',
        '<header class="header" id="header">',
        '  <a href="' + logo_href + '" class="header__logo">CARECL</a>',
        '  <nav class="header__nav">' + nav + '</nav>',
        '  <div class="header__util">',
        '    <div class="lang"><span class="is-active">KR</span><i>·</i><span>EN</span></div>',
        '    <a href="#" class="shop">SHOP</a>',
        '    <button type="button" class="allmenu" id="allMenuBtn" aria-label="전체 메뉴">'
        '<span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>'
        '</button>',
        '  </div>',
        '</header>',
        '',
    ]
    return "\n".join(rows) + mega()


def mega():
    cols = ""
    for label, href, subs in MENU:
        if label not in DROPDOWN_ONLY:
            subs = []
        links = ""
        for stitle, shref, thirds in subs:
            links += '<a class="mega__d2" href="%s">%s</a>' % (shref, stitle)
            for t3, h3 in thirds:
                links += '<a class="mega__d3" href="%s">%s</a>' % (h3, t3)
        cols += '<div class="mega__col"><h3><a href="%s">%s</a></h3>%s</div>' % (href, label, links)
    return (
        '<div class="mega" id="megaMenu" aria-hidden="true">\n'
        '  <button type="button" class="mega__close" id="megaClose" aria-label="닫기"></button>\n'
        '  <div class="mega__inner">\n'
        '    <div class="mega__head"><span>ALL MENU</span><b>careCL</b></div>\n'
        '    <div class="mega__cols">' + cols + '</div>\n'
        '    <div class="mega__foot">\n'
        '      <a href="survey.html" class="mega__cta">AI 피부 진단 시작하기 <span>→</span></a>\n'
        '      <p>TEL +82 31-943-1028 &nbsp;·&nbsp; support@carecl.co.kr</p>\n'
        '    </div>\n'
        '  </div>\n'
        '</div>'
    )


FOOTER = """<footer class="footer">
  <div class="footer__top">
    <div class="footer__brand">
      <p class="logo">CARECL</p>
      <p class="tag">얼굴을 22개 좌표로 읽는<br>정밀 안티에이징 스킨케어</p>
    </div>
    <div class="footer__cols">
      <div><h4>COMPANY</h4><a href="about.html">About careCL</a><a href="greeting.html">Our Story</a><a href="rnd.html">R&amp;D / Patent</a><a href="certification.html">Awards &amp; Certification</a></div>
      <div><h4>AGING LAB</h4><a href="aging-types.html">6 AGING TYPES</a><a href="aging-map.html">AGING MAP 22</a><a href="survey.html">나의 Aging Type 알아보기</a></div>
      <div><h4>TECHNOLOGY</h4><a href="technology.html#basic">Beauty Device Technology</a><a href="technology.html#stamping">5 SEC. STAMPING</a></div>
      <div><h4>PRODUCTS</h4><a href="products.html#device">BEAUTY DEVICE</a><a href="products.html#cosmetics">COSMETICS</a></div>
      <div><h4>CONTACT</h4><a href="contact.html#global">Global Business</a><a href="contact.html#partner">Distributor / Partnership</a><a href="contact.html#pr">Media / PR</a><a href="contact.html#inquiry">General Inquiry</a></div>
    </div>
  </div>
  <div class="footer__legal">
    <p>CARECL CO.,Ltd. &nbsp;·&nbsp; CEO Hyungkyu Choi &nbsp;·&nbsp; 사업자등록번호 591-88-03097 &nbsp;·&nbsp; 통신판매업 제2025-고양일산동-0585호<br>
    Rm 234, 2F, Sanhak Cooperation Hall, 32 Dongguk-ro, Ilsandong-gu, Goyang-si, Gyeonggi-do, Republic of Korea<br>
    TEL +82 31-943-1028 (Mon–Fri 10:00–18:00 / Lunch 12:00–13:00) &nbsp;·&nbsp; support@carecl.co.kr &nbsp;·&nbsp; © 2026 CARECL. All rights reserved.</p>
    <div class="footer__sns"><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a></div>
  </div>
</footer>"""


def depth3_groups(slug):
    """해당 페이지(slug.html)에 속한 2뎁스들의 3뎁스 목록 → [(2뎁스명, [(라벨, 링크), ...]), ...]"""
    page = slug + ".html"
    out = []
    for _d1, _h1, subs in MENU:
        for d2, h2, thirds in subs:
            if thirds and h2.split("#")[0] == page:
                out.append((d2, thirds))
    return out


def anchornav(slug):
    """페이지 상단 3뎁스 앵커 바"""
    groups = depth3_groups(slug)
    if not groups:
        return ""
    blocks = []
    for d2, thirds in groups:
        links = "".join('<a href="%s">%s</a>' % (h, t) for t, h in thirds)
        blocks.append('<div class="anchornav__group"><span class="anchornav__label">%s</span>'
                      '<div class="anchornav__links">%s</div></div>' % (d2, links))
    return ('<nav class="anchornav" id="anchorNav"><div class="anchornav__inner">%s</div></nav>'
            % "".join(blocks))
