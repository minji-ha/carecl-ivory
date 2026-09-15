# -*- coding: utf-8 -*-
"""index.html / survey.html 의 헤더·전체메뉴·푸터를 parts.py 기준으로 동기화한다."""
import io
import re
import parts

TARGETS = [("index.html", "careCL"), ("survey.html", "Aging Map 22")]

for path, active in TARGETS:
    html = io.open(path, encoding="utf-8").read()

    # 1) 기존 전체메뉴 블록 모두 제거 (중복 방지)
    html = re.sub(r'<div class="mega" id="megaMenu".*?\n</div>\n', '', html, flags=re.S)

    # 2) 안내바 + 헤더 교체 (+ 전체메뉴 새로 삽입)
    start = html.index('<div class="announce">')
    end = html.index("</header>") + len("</header>")
    html = html[:start] + parts.header(active=active) + html[end:]

    # 3) 푸터 교체
    fs = html.index('<footer class="footer">')
    fe = html.index("</footer>") + len("</footer>")
    html = html[:fs] + parts.FOOTER + html[fe:]

    # 4) nav.js 삽입
    if "js/nav.js" not in html:
        html = html.replace("</body>", '<script src="js/nav.js"></script>\n</body>')

    io.open(path, "w", encoding="utf-8").write(html)
    print("updated", path)
