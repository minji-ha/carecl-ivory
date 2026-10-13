"""6 Aging Types 리포트 일러스트 생성기
   공통 얼굴 라인 위에 타입별 '먼저 변하는 부위'를 오렌지로 얹는다.
   python make_type_art.py → assets/img/report/type-{key}.svg
"""
import os
import re

INK = '#2B2724'
OR = '#C46A3A'
OR_SOFT = '#E9B48F'
BG = '#F4EFE8'
SKIN = '#FDFCFA'
HAIR = '#E3D9CC'

OUT = os.path.join(os.path.dirname(__file__), 'assets', 'img', 'report')


def mirror(d):
    """x 좌표를 240 기준으로 뒤집은 path (숫자 쌍 단위)"""
    out, toks = [], re.findall(r'[A-Za-z]|-?\d*\.?\d+', d)
    is_x = True
    for t in toks:
        try:
            v = float(t)
        except ValueError:
            out.append(t); is_x = True; continue
        out.append(f'{480 - v:g}' if is_x else f'{v:g}')
        is_x = not is_x
    return ' '.join(out)


def both(d, attrs):
    return f'<path d="{d}" {attrs}/><path d="{mirror(d)}" {attrs}/>'


def node(x, y, r=22, dot=True):
    """Aging Map 좌표 표식 — 점선 링 + 중심점"""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{OR}" stroke-width="1" '
            f'stroke-dasharray="2 4" opacity=".7"/>'
            + (f'<circle cx="{x}" cy="{y}" r="3.2" fill="{OR}"/>' if dot else ''))


def glow(x, y, rx, ry, op=.55):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="url(#glow)" opacity="{op}"/>'


LINE = f'fill="none" stroke="{INK}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"'
ACC = f'fill="none" stroke="{OR}" stroke-width="1.5" stroke-linecap="round"'
ACC_THIN = f'fill="none" stroke="{OR}" stroke-width="1.1" stroke-linecap="round"'

FACE = 'M240 96 C304 96 340 146 340 222 C340 292 330 336 310 372 C290 408 266 430 240 432 C214 430 190 408 170 372 C150 336 140 292 140 222 C140 146 176 96 240 96 Z'
HAIR_D = ('M240 66 C332 66 370 130 366 214 C363 238 356 252 346 262 C344 222 340 196 330 174 '
          'C312 146 278 134 240 136 C202 134 168 146 150 174 C140 196 136 222 134 262 '
          'C124 252 117 238 114 214 C110 130 148 66 240 66 Z')


def base(accent_under='', accent_over=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 560" role="img">
<defs>
  <radialGradient id="bg" cx="50%" cy="38%" r="70%"><stop offset="0" stop-color="#FBF8F4"/><stop offset="1" stop-color="{BG}"/></radialGradient>
  <radialGradient id="glow"><stop offset="0" stop-color="{OR_SOFT}" stop-opacity=".9"/><stop offset="1" stop-color="{OR_SOFT}" stop-opacity="0"/></radialGradient>
  <linearGradient id="hair" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{HAIR}"/><stop offset="1" stop-color="#D9CDBE"/></linearGradient>
</defs>
<rect width="480" height="560" fill="url(#bg)"/>
<g fill="none" stroke="{INK}" opacity=".09">
  <circle cx="240" cy="262" r="214"/><circle cx="240" cy="262" r="168" stroke-dasharray="1 7"/>
  <path d="M240 30 V60 M240 464 V494 M8 262 H38 M442 262 H472"/>
</g>
<path d="M204 410 C206 458 200 498 186 528 C150 540 100 548 60 560 H420 C380 548 330 540 294 528 C280 498 274 458 276 410" fill="{SKIN}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round" opacity=".9"/>
<path d="{FACE}" fill="{SKIN}"/>
{accent_under}
<path d="{FACE}" {LINE} opacity=".85"/>
{both('M143 246 C128 240 123 262 129 280 C133 292 140 296 146 294', LINE + ' opacity=".7"')}
<path d="{HAIR_D}" fill="url(#hair)"/>
<path d="M240 136 C238 112 236 90 240 68 M200 140 C192 116 190 96 196 76 M280 140 C288 116 290 96 284 76" fill="none" stroke="{INK}" stroke-width="1" opacity=".18"/>
{both('M180 205 C195 197 213 197 226 202', LINE)}
{both('M182 233 C194 241 212 241 224 233', LINE)}
<path d="M238 226 C236 258 230 284 232 297 M228 303 C236 309 244 309 252 303" {LINE} opacity=".8"/>
<path d="M214 346 C226 339 234 341 240 344 C246 341 254 339 266 346 M214 346 C228 353 252 353 266 346 M221 351 C231 365 249 365 259 351" {LINE} opacity=".85"/>
{accent_over}
</svg>
'''


# ── 타입별 강조 ──────────────────────────────────────────
def sparkle(x, y, s, op):
    return (f'<path d="M{x} {y-s} Q{x} {y} {x+s} {y} Q{x} {y} {x} {y+s} Q{x} {y} {x-s} {y} Q{x} {y} {x} {y-s}Z" '
            f'fill="{OR}" opacity="{op}"/>')


def early():
    under = glow(190, 285, 52, 40, .5) + glow(290, 285, 52, 40, .5) + glow(240, 165, 70, 28, .3)
    dots = [(176, 276, 2.2, .55), (196, 296, 1.6, .4), (208, 272, 1.4, .35), (284, 270, 2, .5),
            (300, 292, 1.5, .45), (270, 298, 1.3, .3), (226, 160, 1.4, .3), (258, 172, 1.8, .35)]
    over = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{OR}" opacity="{o}"/>' for x, y, r, o in dots)
    over += sparkle(318, 168, 9, .75) + sparkle(160, 236, 6, .55) + sparkle(332, 300, 5, .45)
    over += node(190, 285) + node(290, 285)
    return base(under, over)


def tired():
    under = glow(203, 258, 36, 16, .75) + glow(277, 258, 36, 16, .75)
    over = both('M184 248 C196 262 214 263 226 250', ACC + ' opacity=".8"')
    over += both('M188 258 C200 270 214 270 222 260', ACC_THIN + ' stroke-dasharray="2 4" opacity=".7"')
    over += both('M213 349 C211 353 209 355 206 357', ACC_THIN + ' opacity=".8"')
    over += node(203, 256, 26) + node(277, 256, 26)
    return base(under, over)


def fine():
    over = both('M308 226 L324 220 M309 233 L327 233 M308 240 L324 247', ACC_THIN)
    over += both('M198 248 C206 251 214 251 220 248', ACC_THIN + ' opacity=".7"')
    over += f'<path d="M228 335 L227 330 M235 334 L234.5 329 M245 334 L245.5 329 M252 335 L253 330" {ACC_THIN} opacity=".6"/>'
    over += f'<path d="M206 470 C226 476 254 476 274 470 M210 492 C230 498 250 498 270 492" {ACC_THIN} opacity=".75"/>'
    over += node(318, 233, 20) + node(162, 233, 20) + node(240, 347, 36, False) + node(240, 481, 20)
    return base('', over)


def sag():
    # 원래 윤곽(점선) 아래로 내려앉은 현재 윤곽(오렌지)
    jaw_now = 'M150 330 C154 366 170 396 190 418 C208 436 224 446 240 448 C256 446 272 436 290 418 C310 396 326 366 330 330'
    over = f'<path d="{jaw_now}" {ACC} opacity=".85"/>'
    over += both('M222 312 C212 325 209 337 212 349', ACC_THIN + ' opacity=".8"')
    over += both('M208 362 C206 376 200 388 192 398', ACC_THIN + ' opacity=".7"')
    arrow = lambda x, y: (f'<path d="M{x} {y} V{y+22} M{x-5} {y+16} L{x} {y+22} L{x+5} {y+16}" '
                          f'{ACC_THIN} opacity=".75"/>')
    over += arrow(176, 300) + arrow(304, 300) + arrow(240, 412)
    over += node(186, 412, 22) + node(294, 412, 22)
    return base(glow(178, 360, 34, 46, .35) + glow(302, 360, 34, 46, .35), over)


def muscle():
    over = (f'<path d="M196 150 C214 145 228 152 240 147 C252 152 266 145 284 150 '
            f'M190 166 C210 161 226 168 240 163 C254 168 270 161 290 166 '
            f'M198 182 C214 178 228 183 240 180 C252 183 266 178 282 182" {ACC} opacity=".85"/>')
    over += f'<path d="M233 196 L231 214 M247 196 L249 214" fill="none" stroke="{OR}" stroke-width="1.8" stroke-linecap="round"/>'
    over += both('M310 226 L328 219 M311 236 L330 237', ACC)
    over += node(240, 166, 34) + node(240, 205, 16)
    return base(glow(240, 168, 70, 30, .4), over)


def mixed():
    under = glow(196, 288, 40, 30, .4) + glow(288, 400, 34, 40, .35)
    over = (f'<path d="M204 160 C220 155 232 161 240 157 C248 161 260 155 276 160 '
            f'M206 175 C222 171 232 176 240 173 C248 176 258 171 274 175" {ACC} opacity=".75"/>')
    over += f'<path d="M308 226 L324 220 M309 234 L327 234 M308 242 L324 248" {ACC_THIN}/>'
    over += f'<path d="M290 418 C310 396 326 366 330 330" {ACC} opacity=".85"/>'
    over += ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{OR}" opacity="{o}"/>'
                    for x, y, r, o in [(184, 280, 2, .5), (200, 296, 1.5, .4), (210, 276, 1.3, .35)])
    over += node(240, 167, 28) + node(318, 234, 18) + node(196, 288, 24) + node(304, 392, 24)
    # 서로 다른 패턴을 잇는 맵 연결선
    over += (f'<path d="M240 195 L318 216 M318 252 L304 368 M262 167 L196 264" fill="none" '
             f'stroke="{OR}" stroke-width=".8" stroke-dasharray="1 5" opacity=".6"/>')
    return base(under, over)


TYPES = {'early': early, 'tired': tired, 'fine': fine, 'sag': sag, 'muscle': muscle, 'mixed': mixed}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for k, fn in TYPES.items():
        with open(os.path.join(OUT, f'type-{k}.svg'), 'w', encoding='utf-8') as f:
            f.write(fn())
    print('ok', OUT)
