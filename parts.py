# -*- coding: utf-8 -*-
"""careCL 공통 파츠 (헤더 / 전체메뉴 / 푸터).  build_sub.py · apply_nav.py 에서 사용"""

# (라벨, 링크, [(하위라벨, 하위링크), ...])
MENU = [
    ("COMPANY", "about.html", [
        ("About careCL", "about.html"),
        ("Our Story", "greeting.html"),
        ("History", "history.html"),
        ("R&D / Patent", "rnd.html"),
        ("Awards & Certification", "certification.html"),
        ("Mission & Vision", "mission-vision.html"),
    ]),
    ("AGING LAB", "aging-types.html", [
        ("Why We Age Differently", "aging-types.html#why"),
        ("6 Aging Types", "aging-types.html#types"),
        ("나의 Aging Type 알아보기", "survey.html"),
    ]),
    ("AGING MAP 22", "aging-map.html", [
        ("Why Aging Map 22", "aging-map.html#why"),
        ("6 Types × 22 Areas", "aging-map.html#matrix"),
        ("Face / Neck & Body", "aging-map.html#areas"),
        ("Personalized Care", "aging-map.html#care"),
    ]),
    ("TECHNOLOGY", "technology.html", [
        ("Beauty Device Technology", "technology.html#basic"),
        ("5 SEC. STAMPING", "technology.html#stamping"),
        ("TECHFIT 적용 기술", "technology.html#techfit"),
    ]),
    ("PRODUCTS", "products.html", [
        ("Beauty Device", "products.html#device"),
        ("Cosmetics", "products.html#cosmetics"),
    ]),
    ("CONTACT", "contact.html", [
        ("Global Business", "contact.html#global"),
        ("Distributor / Partnership", "contact.html#partner"),
        ("Media / PR", "contact.html#pr"),
        ("General Inquiry", "contact.html#inquiry"),
        ("오시는 길", "location.html"),
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
        badge = AI_BADGE if label == "AGING MAP 22" else ""
        drop = ''
        if subs:
            sub = "".join('<a href="%s">%s</a>' % (h, t) for t, h in subs)
            drop = '<div class="dropdown"><div class="dropdown__inner">%s</div></div>' % sub
        return ('<div class="navitem%s"><a href="%s"%s>%s</a>%s%s</div>'
                % (' has-badge' if badge else '', href, cls, label, badge, drop))

    half = (len(MENU) + 1) // 2
    left = "".join(item(*m) for m in MENU[:half])
    right = "".join(item(*m) for m in MENU[half:])
    rows = [
        '<div class="announce">',
        '  <span class="announce__dot"></span>',
        '  <span>AGING MAP 22 진단 오픈 — 2분 설문으로 나의 노화 타입 확인하기</span>',
        '</div>',
        '',
        '<header class="header" id="header">',
        '  <nav class="header__nav header__nav--left">' + left + '</nav>',
        '  <a href="' + logo_href + '" class="header__logo">CARECL</a>',
        '  <nav class="header__nav header__nav--right">' + right + '</nav>',
        '  <div class="header__util">',
        '    <div class="lang"><span class="is-active">KR</span><i>·</i><span>EN</span></div>',
        '    <a href="#" class="shop">SHOP</a>',
        '    <a href="#" class="login">로그인</a>',
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
        links = "".join('<a href="%s">%s</a>' % (h, t) for t, h in subs)
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
      <div><h4>COMPANY</h4><a href="about.html">About careCL</a><a href="greeting.html">Our Story</a><a href="history.html">History</a><a href="rnd.html">R&amp;D / Patent</a><a href="certification.html">Awards &amp; Certification</a><a href="mission-vision.html">Mission &amp; Vision</a></div>
      <div><h4>AGING LAB</h4><a href="aging-types.html">6 Aging Types</a><a href="survey.html">나의 타입 알아보기</a></div>
      <div><h4>AGING MAP 22</h4><a href="aging-map.html">Why Aging Map 22</a><a href="aging-map.html#areas">22개 관리 부위</a></div>
      <div><h4>TECHNOLOGY</h4><a href="technology.html">Beauty Device Technology</a><a href="technology.html#stamping">5 SEC. STAMPING</a></div>
      <div><h4>PRODUCTS</h4><a href="products.html#device">Beauty Device</a><a href="products.html#cosmetics">Cosmetics</a></div>
      <div><h4>CONTACT</h4><a href="contact.html">문의하기</a><a href="location.html">오시는 길</a></div>
    </div>
  </div>
  <div class="footer__legal">
    <p>CARECL CO.,Ltd. &nbsp;·&nbsp; CEO Hyungkyu Choi &nbsp;·&nbsp; 사업자등록번호 591-88-03097 &nbsp;·&nbsp; 통신판매업 제2025-고양일산동-0585호<br>
    Rm 234, 2F, Sanhak Cooperation Hall, 32 Dongguk-ro, Ilsandong-gu, Goyang-si, Gyeonggi-do, Republic of Korea<br>
    TEL +82 31-943-1028 (Mon–Fri 10:00–18:00 / Lunch 12:00–13:00) &nbsp;·&nbsp; support@carecl.co.kr &nbsp;·&nbsp; © 2026 CARECL. All rights reserved.</p>
    <div class="footer__sns"><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a></div>
  </div>
</footer>"""
