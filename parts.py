# -*- coding: utf-8 -*-
"""careCL 공통 파츠 (헤더 / 전체메뉴 / 푸터).  build_sub.py · apply_nav.py 에서 사용"""

# (1뎁스 라벨, 링크, [(2뎁스 라벨, 링크, 페이지 한글명), ...])
# 노션 "케어클 홈페이지 구성" 기준 — GNB·서브 탭 모두 2뎁스까지만 쓴다.
# 3뎁스였던 항목들은 각 페이지 본문의 소제목으로 들어간다.
MENU = [
    ("COMPANY", "about.html", [
        ("About careCL", "about.html", "회사 소개"),
        ("Our Story", "greeting.html", "브랜드 스토리"),
        ("R&D / Patent", "rnd.html", "연구개발 · 특허"),
        ("Awards & Certification", "certification.html", "수상 · 인증"),
    ]),
    ("AGING LAB", "aging-types.html", [
        ("6 Aging Types", "aging-types.html", "6가지 노화 타입"),
        ("Aging Map 22", "aging-map.html", "22개 관리 부위"),
    ]),
    ("TECHNOLOGY", "technology.html", [
        ("Beauty Device Technology", "technology.html", "홈뷰티 디바이스 기술"),
        ("careCL Technology", "carecl-technology.html", "케어클 기술"),
    ]),
    ("PRODUCTS", "products.html", [
        ("Beauty Device", "products.html", "뷰티 디바이스"),
        ("Cosmetics", "cosmetics.html", "코스메틱"),
    ]),
    ("CONTACT", "contact.html", [
        ("Global Business", "contact.html", "해외 사업 문의"),
        ("Distributor / Partnership", "partnership.html", "유통 · 제휴 문의"),
        ("Media / PR", "press.html", "미디어 문의"),
        ("General Inquiry", "inquiry.html", "일반 문의"),
    ]),
]

FLOATING = (
    '<a class="aifab" href="survey.html" aria-label="AI 피부 진단 시작하기">'
    '<span class="aifab__ico">'
    '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
    '<path d="M12 2.2 14 8.4 20.2 10.4 14 12.4 12 18.6 10 12.4 3.8 10.4 10 8.4Z" fill="currentColor"/>'
    '<circle cx="19.4" cy="4.2" r="1.7" fill="currentColor" opacity=".9"/>'
    '<circle cx="4.8" cy="18.4" r="1.2" fill="currentColor" opacity=".7"/>'
    '</svg></span>'
    '<span class="aifab__txt">AI 피부 진단</span>'
    '</a>'
)

CURSOR_WORD = '<div class="cursorword" id="cursorWord" aria-hidden="true"></div>'

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
        badge = ""
        drop = ''
        if subs:
            links = "".join('<a class="dropdown__d2" href="%s">%s</a>' % (h, t)
                            for t, h, _kr in subs)
            drop = '<div class="dropdown"><div class="dropdown__inner">%s</div></div>' % links
        return ('<div class="navitem%s"><a href="%s"%s>%s</a>%s%s</div>'
                % (' has-badge' if badge else '', href, cls, label, badge, drop))

    nav = "".join(item(*m) for m in MENU)
    rows = [
        '<div class="announce">',
        '  <a class="announce__link" href="' + start_href + '">',
        '    <span class="announce__dot"></span>',
        '    <span>AGING MAP 22 진단 오픈 — 2분 설문으로 나의 노화 타입 확인하기</span>',
        '    <i class="announce__go">진단하러 가기 <b>→</b></i>',
        '  </a>',
        '</div>',
        '',
        '<header class="header" id="header">',
        '  <a href="' + logo_href + '" class="header__logo">CARECL</a>',
        '  <nav class="header__nav">' + nav + '</nav>',
        '  <div class="header__util">',
        '    <div class="lang"><span class="is-active">KR</span><i>·</i><span>EN</span></div>',
        '    <button type="button" class="allmenu" id="allMenuBtn" aria-label="전체 메뉴">'
        '<span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>'
        '</button>',
        '  </div>',
        '</header>',
        '',
    ]
    return chr(10).join(rows) + mega() + chr(10) + FLOATING + chr(10) + CURSOR_WORD


def mega():
    cols = ""
    for label, href, subs in MENU:
        links = "".join('<a class="mega__d2" href="%s">%s</a>' % (h, t) for t, h, _kr in subs)
        cols += '<div class="mega__col"><h3><a href="%s">%s</a></h3>%s</div>' % (href, label, links)
    rows = [
        '<div class="mega" id="megaMenu" aria-hidden="true">',
        '  <button type="button" class="mega__close" id="megaClose" aria-label="닫기"></button>',
        '  <div class="mega__inner">',
        '    <div class="mega__head"><span>ALL MENU</span><b>careCL</b></div>',
        '    <div class="mega__cols">' + cols + '</div>',
        '    <div class="mega__foot">',
        '      <a href="survey.html" class="mega__cta">AI 피부 진단 시작하기 <span>→</span></a>',
        '      <p>TEL +82 31-943-1028 &nbsp;·&nbsp; support@carecl.co.kr</p>',
        '    </div>',
        '  </div>',
        '</div>',
    ]
    return chr(10).join(rows)


FOOTER = """<footer class="footer">
  <div class="footer__top">
    <div class="footer__brand">
      <p class="logo">CARECL</p>
      <p class="tag">얼굴을 22개 좌표로 읽는<br>정밀 안티에이징 스킨케어</p>
    </div>
    <div class="footer__cols">
      <div><h4>COMPANY</h4><a href="about.html">About careCL</a><a href="greeting.html">Our Story</a><a href="rnd.html">R&amp;D / Patent</a><a href="certification.html">Awards &amp; Certification</a></div>
      <div><h4>AGING LAB</h4><a href="aging-types.html">6 Aging Types</a><a href="aging-map.html">Aging Map 22</a><a href="survey.html">나의 타입 알아보기</a></div>
      <div><h4>TECHNOLOGY</h4><a href="technology.html">Beauty Device Technology</a><a href="carecl-technology.html">careCL Technology</a></div>
      <div><h4>PRODUCTS</h4><a href="products.html">Beauty Device</a><a href="cosmetics.html">Cosmetics</a></div>
      <div><h4>CONTACT</h4><a href="contact.html">Global Business</a><a href="partnership.html">Distributor / Partnership</a><a href="inquiry.html">General Inquiry</a></div>
    </div>
  </div>
  <div class="footer__legal">
    <p>CARECL CO.,Ltd. &nbsp;·&nbsp; CEO Hyungkyu Choi &nbsp;·&nbsp; 사업자등록번호 591-88-03097 &nbsp;·&nbsp; 통신판매업 제2025-고양일산동-0585호<br>
    Rm 234, 2F, Sanhak Cooperation Hall, 32 Dongguk-ro, Ilsandong-gu, Goyang-si, Gyeonggi-do, Republic of Korea<br>
    TEL +82 31-943-1028 (Mon–Fri 10:00–18:00 / Lunch 12:00–13:00) &nbsp;·&nbsp; support@carecl.co.kr &nbsp;·&nbsp; © 2026 CARECL. All rights reserved.</p>
    <div class="footer__sns"><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a></div>
  </div>
</footer>"""
