# -*- coding: utf-8 -*-
"""careCL 공통 파츠 (헤더 / 전체메뉴 / 푸터).  build_sub.py · apply_nav.py 에서 사용"""

# (라벨, 링크, [(하위라벨, 하위링크), ...])
MENU = [
    ("careCL", "about.html", [
        ("회사소개", "about.html"),
        ("인사말", "greeting.html"),
        ("연혁", "history.html"),
        ("인증", "certification.html"),
        ("미션과 비전", "mission-vision.html"),
        ("오시는 길", "location.html"),
    ]),
    ("Aging Map 22", "survey.html", [
        ("진단 설문 시작", "survey.html"),
        ("6가지 노화 타입", "#"),
        ("리포트 예시", "#"),
        ("Aging Map 22란?", "#"),
    ]),
    ("Technology", "#", [
        ("TECH FIT 스탬핑", "#"),
        ("고주파 원리", "#"),
        ("임상 데이터", "#"),
        ("특허 · 인증", "certification.html"),
    ]),
    ("Product", "index.html#products", [
        ("Device", "#"),
        ("Cosmetic", "#"),
        ("Accessory", "#"),
        ("전체 제품 보기", "#"),
    ]),
    ("Contact", "location.html", [
        ("오시는 길", "location.html"),
        ("1:1 문의", "#"),
        ("자주 묻는 질문", "#"),
        ("이용안내", "#"),
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


DROPDOWN_ONLY = ["careCL"]   # 드롭다운을 노출할 메뉴


def header(active=None, logo_href="index.html", start_href="survey.html"):
    items = []
    for label, href, subs in MENU:
        if label not in DROPDOWN_ONLY:
            subs = []
        cls = ' class="is-active"' if active == label else ''
        badge = AI_BADGE if label == "Aging Map 22" else ""
        if subs:
            sub = "".join('<a href="%s">%s</a>' % (h, t) for t, h in subs)
            drop = '<div class="dropdown"><div class="dropdown__inner">%s</div></div>' % sub
        else:
            drop = ''
        items.append(
            '<div class="navitem%s"><a href="%s"%s>%s</a>%s%s</div>'
            % (' has-badge' if badge else '', href, cls, label, badge, drop)
        )
    nav = "".join(items)
    return (
        '<div class="announce">\n'
        '  <span class="announce__dot"></span>\n'
        '  <span>AGING MAP 22 진단 오픈 — 2분 설문으로 나의 노화 타입 확인하기</span>\n'
        '</div>\n\n'
        '<header class="header" id="header">\n'
        '  <nav class="header__nav">' + nav + '</nav>\n'
        '  <a href="' + logo_href + '" class="header__logo">CARECL</a>\n'
        '  <div class="header__util">\n'
        '    <div class="lang"><span class="is-active">KR</span><i>·</i><span>EN</span></div>\n'
        '    <a href="#" class="login">로그인</a>\n'
        '    <button type="button" class="allmenu" id="allMenuBtn" aria-label="전체 메뉴">'
        '<span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span>'
        '</button>\n'
        '  </div>\n'
        '</header>\n\n' + mega()
    )


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
      <div><h4>careCL</h4><a href="about.html">회사소개</a><a href="greeting.html">인사말</a><a href="history.html">연혁</a><a href="certification.html">인증</a><a href="mission-vision.html">미션과 비전</a><a href="location.html">오시는 길</a></div>
      <div><h4>AGING MAP 22</h4><a href="survey.html">진단 설문 시작</a></div>
      <div><h4>TECHNOLOGY</h4><a href="#">기술 소개</a></div>
      <div><h4>PRODUCT</h4><a href="index.html#products">제품 보기</a></div>
      <div><h4>CONTACT</h4><a href="location.html">오시는 길</a></div>
    </div>
  </div>
  <div class="footer__legal">
    <p>CARECL CO.,Ltd. &nbsp;·&nbsp; CEO Hyungkyu Choi &nbsp;·&nbsp; 사업자등록번호 591-88-03097 &nbsp;·&nbsp; 통신판매업 제2025-고양일산동-0585호<br>
    Rm 234, 2F, Sanhak Cooperation Hall, 32 Dongguk-ro, Ilsandong-gu, Goyang-si, Gyeonggi-do, Republic of Korea<br>
    TEL +82 31-943-1028 (Mon–Fri 10:00–18:00 / Lunch 12:00–13:00) &nbsp;·&nbsp; support@carecl.co.kr &nbsp;·&nbsp; © 2026 CARECL. All rights reserved.</p>
    <div class="footer__sns"><a href="#" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a><a href="#" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a></div>
  </div>
</footer>"""
