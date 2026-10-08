# careCL 케어클 — 홈페이지 퍼블리싱

정적 사이트입니다. 빌드 도구·패키지 매니저 없이 **HTML + CSS + 바닐라 JS**로만 되어 있고,
반복되는 HTML(헤더·푸터·서브페이지)만 Python 스크립트로 찍어냅니다.

- 배포 주소 : <https://minji-ha.github.io/carecl-ivory/> (GitHub Pages, `main` 브랜치 루트)
- 폰트 : Pretendard (CDN) · 아이콘 : Font Awesome (로컬 `libs/`)
- 외부 라이브러리 : GSAP + ScrollTrigger, Lenis, three.js — **전부 `libs/`에 로컬 번들**

---

## 1. 바로 실행

```bash
python -m http.server 5173
```

그 뒤 <http://localhost:5173/index.html> 을 엽니다.
(`file://`로 직접 열면 일부 JS가 동작하지 않습니다.)

---

## 2. ⚠️ 가장 먼저 알아야 할 것 — 자동 생성 파일

**HTML 대부분은 생성 결과물입니다. 직접 고치면 다음 빌드 때 덮어써집니다.**

| 파일 | 수정해야 할 곳 | 다시 만드는 명령 |
|---|---|---|
| `index.html` | `build_main.py` | `python build_main.py` |
| 서브 14개 페이지 | `build_sub.py`, 본문은 `content_bodies.py` | `python build_sub.py` |
| 모든 페이지의 헤더·전체메뉴·푸터·플로팅 버튼 | `parts.py` | 위 두 개를 다시 실행 |
| `index.html` · `survey.html`의 헤더/푸터만 동기화 | `parts.py` | `python apply_nav.py` |
| **`survey.html`** (진단 설문) | **HTML을 직접 수정** | — |
| **`report.html`** (진단 결과 리포트) | **HTML을 직접 수정** | — |

> `report.html`은 어떤 스크립트도 건드리지 않습니다.
> `parts.py`의 헤더·푸터를 바꿨다면 `report.html`은 **손으로 맞춰야** 합니다.

### 빌드 순서

```bash
python build_main.py     # index.html
python build_sub.py      # 서브 14개 페이지
python apply_nav.py      # index.html / survey.html 헤더·푸터 동기화
python bust.py           # ★ 반드시 마지막에
```

`bust.py`는 모든 HTML의 `css/…`, `js/…` 링크에 `?v=<현재시각>`을 다시 붙입니다.
**이걸 빼먹으면 방문자 브라우저가 예전 CSS/JS를 계속 씁니다.**

---

## 3. 페이지 구조

GNB는 **2뎁스까지만** 노출하고, 3뎁스였던 항목은 페이지 안 소제목으로 들어갑니다.
메뉴 1개 = 페이지 1개로 1:1 대응하며, 메뉴 정의는 `parts.py`의 `MENU` 하나뿐입니다.
**여기를 고치면 GNB·전체메뉴·서브탭·`build_sub.py`가 생성하는 페이지 목록이 함께 바뀝니다.**

| 1뎁스 | 2뎁스 | 파일 |
|---|---|---|
| COMPANY | About careCL | `about.html` |
| | Our Story | `greeting.html` |
| | R&D / Patent | `rnd.html` |
| | Awards & Certification | `certification.html` |
| AGING LAB | 6 Aging Types | `aging-types.html` |
| | Aging Map 22 | `aging-map.html` |
| TECHNOLOGY | Beauty Device Technology | `technology.html` |
| | careCL Technology | `carecl-technology.html` |
| PRODUCTS | Beauty Device | `products.html` |
| | Cosmetics | `cosmetics.html` |
| CONTACT | Global Business | `contact.html` |
| | Distributor / Partnership | `partnership.html` |
| | Media / PR | `press.html` |
| | General Inquiry | `inquiry.html` |

메뉴에 없는 독립 페이지 : `index.html` · `survey.html` · `report.html`

---

## 4. CSS 로드 순서 (중요)

나중에 오는 파일이 앞의 선언을 덮습니다. **순서를 바꾸면 디자인이 깨집니다.**

```
서브 페이지 : style.css → nav.css → sub.css → theme-ivory.css → subv2.css
메인        : style.css → nav.css → theme-ivory.css → mainv2.css → intro.css
설문/리포트  : style.css → scanhud.css → nav.css → survey.css → report.css → theme-ivory.css
```

| 파일 | 역할 |
|---|---|
| `style.css` | 기본 리셋·타이포·버튼 |
| `nav.css` | 헤더 · 드롭다운 · 전체메뉴 |
| `sub.css` / `subv2.css` | 서브 페이지 레이아웃 / **최종 보정(가장 셈)** |
| `theme-ivory.css` | 아이보리 테마 색·폰트 변수 |
| `mainv2.css` · `intro.css` | 메인 섹션 / 인트로 카운트 화면 |
| `survey.css` · `report.css` | 설문 / 진단 결과 리포트 |
| `scanhud.css` | 얼굴 스캔 HUD 연출 |

---

## 5. JS

| 파일 | 역할 |
|---|---|
| `smoothscroll.js` | Lenis 관성 스크롤. **`window.__lenis`로 노출** |
| `mainv2.js` | 메인 전체 — 히어로 슬라이드, 핵심 3가지 모이기, 제품 커버플로, 5 STEP, 공식몰 확장 |
| `scrollfx.js` | 공용 스크롤 등장 효과 (`data-fx="lines" / "up"`, `data-fx-group`, `data-fx-para`, `data-fx-zoom`) |
| `intro.js` | 첫 방문 시 0→100 카운트 인트로 (2시간 내 재방문은 생략, `?intro=1`로 강제 재생) |
| `cursorword.js` | 마우스를 따라다니는 careCL 글자 |
| `nav.js` | 헤더 스크롤 상태 · 전체메뉴 토글 |
| `sub.js` · `typecards.js` | 서브 페이지 등장 효과 / 6 Aging Types 가로 스크롤(핀) |
| `survey.js` | 설문 18문항 진행 · 유형 집계 |
| `report.js` | **진단 결과 리포트 데이터 + 마크업 생성 (설문·리포트 페이지 공용)** |
| `reportpage.js` | `report.html`에서 주소의 `type` 값을 읽어 리포트를 그림 |
| `scanhud.js` · `wave3d.js` · `particletext.js` | 스캔 HUD · 3D 물결 · 파티클 타이틀 |

> **스크롤 효과는 `IntersectionObserver` 대신 `scroll` 이벤트 + `window.__lenis.on('scroll')`로 감지합니다.**
> 관성 스크롤 환경에서 IO가 발화하지 않는 문제가 있어 의도적으로 바꾼 것이니 되돌리지 마세요.

---

## 6. 진단 결과 리포트 연동 규약

진단 앱에서 결과가 나오면 **타입 키를 주소에 붙여** 리포트를 열면 됩니다.

```
report.html?type=muscle
```

| 키 | 타입 |
|---|---|
| `early` | 초기 노화형 |
| `tired` | 피로형 |
| `fine` | 잔주름형 |
| `sag` | 변형 · 처짐형 |
| `muscle` | 근육형 |
| `mixed` | 혼합형 |

값이 없거나 목록에 없으면 `muscle`로 보여줍니다.

- 타입별 문구(코드·이름·한 줄 요약·설명·특징·대표 고민)는 **`js/report.js`의 `REPORT` 한 곳**에만 있습니다.
- 리포트 마크업은 진단 앱이 쓰던 `.cku-*` 클래스 이름을 그대로 씁니다.
  **앱 쪽 DOM을 바꾸지 않고 `css/report.css`만 연결해도 디자인이 적용됩니다.**
- `window.ckuReport.html(key, opts)`로 HTML 문자열을 받아 쓸 수 있습니다.
  - `opts.counts` : `{타입키: 점수}` — 주면 응답 분포 막대를 그립니다
  - `opts.parts` : 집중 관리 부위 문자열
  - `opts.restart` : `true`면 버튼이 "다시 하기"(설문 재시작), `false`면 `survey.html`로 이동
  - 그린 뒤 `window.ckuReport.fillBars(root)`를 호출하면 분포 막대가 채워집니다

---

## 7. 배포

`main` 브랜치에 push하면 GitHub Pages가 자동으로 다시 빌드합니다.

```bash
python build_main.py && python build_sub.py && python apply_nav.py && python bust.py
git add -A && git commit -m "..." && git push
```

반영 확인 :

```bash
gh api repos/minji-ha/carecl-ivory/pages/builds/latest --jq '.status + " " + .commit'
```

`built <방금 푸시한 커밋 SHA>`가 나오면 완료입니다. 보통 30초~2분 걸립니다.

---

## 8. 인계 시 주의

- **공개 레포입니다.** 비공개 자료(시험성적서 등)는 올리지 마세요. 과거에 올라갔던 시험성적서 PDF는 git 기록까지 삭제했습니다.
- 특허·인증서 이미지는 **개인정보(법인등록번호·발명자 인적사항·서명)를 가린 상태**로 커밋되어 있습니다. 원본으로 교체하지 마세요.
- `content_apply.py`는 레포 밖 경로(`C:\work\carecl\자료\content_rich.txt`)의 원고 파일을 읽습니다.
  **그 파일이 없으면 실행되지 않습니다.** 본문을 고칠 때는 결과물인 `content_bodies.py`를 직접 수정하세요.
- 영상은 `assets/video/brand-film.mp4` 한 개입니다. 교체 시 같은 경로·파일명을 유지하면 됩니다.
- 상단 배너 슬라이드는 `build_main.py`의 `HERO_SLIDES` 목록에 항목을 추가하면 늘어납니다
  (`kind`: `video` 또는 `image`). 인디케이터 개수와 카운터는 목록 길이를 따라갑니다.
