# -*- coding: utf-8 -*-
"""index.html / survey.html 의 헤더·전체메뉴·푸터를 parts.py 기준으로 동기화한다."""
import io
import re
import parts

TARGETS = [("index.html", None), ("survey.html", "AGING MAP 22")]

for path, active in TARGETS:
    html = io.open(path, encoding="utf-8").read()

    # 1) 전체메뉴 · 플로팅 버튼 · 커서 글자 제거 (여러 번 실행해도 중복되지 않도록)
    html = re.sub(r'<div class="mega" id="megaMenu".*?\n</div>\n', '', html, flags=re.S)
    html = re.sub(r'<a class="aifab".*?</a>\n?', '', html, flags=re.S)
    html = re.sub(r'<div class="cursorword" id="cursorWord"[^>]*></div>\n?', '', html)

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
        html = html.replace("</body>", '<script src="js/cursorword.js"></script>' + chr(10) + '<script src="js/nav.js"></script>' + chr(10) + '</body>')

    io.open(path, "w", encoding="utf-8").write(html)
    print("updated", path)
