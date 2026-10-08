# -*- coding: utf-8 -*-
"""모든 HTML의 css/js 링크에 ?v=<현재시각> 을 붙여 브라우저 캐시를 끊는다.

    python bust.py

빌드(build_main.py / build_sub.py) 후 반드시 한 번 실행한다.
실행하지 않으면 방문자 브라우저가 예전 css/js를 계속 쓴다.
"""
import glob
import io
import re
import time

VER = time.strftime("%y%m%d%H%M%S")
PAT = re.compile(r'((?:href|src)="(?:css|js)/[^"]+?)(\?v=\d+)?(")')

changed = 0
for path in sorted(glob.glob("*.html")):
    src = io.open(path, encoding="utf-8").read()
    out = PAT.sub(lambda m: m.group(1) + "?v=" + VER + m.group(3), src)
    if out != src:
        io.open(path, "w", encoding="utf-8").write(out)
        changed += 1

print("v=%s  (%d files)" % (VER, changed))
