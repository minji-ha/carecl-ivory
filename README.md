# careCL Global — Main (퍼블리싱)

Figma 시안 `01 · Main (Desktop 1920)` 기준 퍼블리싱 결과물입니다.

## 폴더 구조

```
publish/
├─ index.html              메인
├─ about.html              회사소개
├─ greeting.html           인사말
├─ history.html            연혁
├─ certification.html      인증
├─ mission-vision.html     미션과 비전
├─ location.html           오시는 길
├─ survey.html             노화 타입 진단 설문 (18문항)
├─ build_sub.py            회사소개 6페이지 생성기
├─ css/  style.css · sub.css · survey.css
├─ js/   main.js · sub.js · survey.js
├─ libs/                 # 외부 라이브러리 (모두 로컬 다운로드)
│  ├─ gsap.min.js            3.12.5
│  ├─ ScrollTrigger.min.js   3.12.5
│  └─ lenis.min.js           1.1.18  (관성 스크롤)
└─ assets/
   ├─ img/              # 얼굴 이미지, 제품 6종, 히어로 포스터
   ├─ video/            # ← 브랜드 필름을 여기에 넣어주세요
   └─ fonts/            # (비어 있음 — 폰트 로컬 번들 시 사용)
```

## 실행

정적 파일이라 서버 없이 `index.html`을 열어도 동작하지만, 로컬 서버 사용을 권장합니다.

```bash
python -m http.server 5173 --directory publish
```

## 영상 넣는 법

`assets/video/brand-film.mp4` 경로에 파일을 넣으면 자동으로 재생됩니다.
(자동재생 / 무음 / 루프 / `playsinline` 설정 완료)

- 영상이 없는 동안에는 `assets/img/hero-poster.jpg` 포스터와 그라데이션 배경이 표시됩니다
- webm을 함께 쓰려면 `index.html`의 `<video>` 안에 `<source src="assets/video/brand-film.webm" type="video/webm">`를 mp4 앞에 추가하세요
- 권장: 1920×1080, 8~15초 루프, H.264, 5MB 이하

## 구현된 인터랙션

| 영역 | 동작 |
|---|---|
| 전체 | Lenis 관성 스크롤 |
| 헤더 | 히어로를 벗어나면 상단 안내바가 접히고 헤더가 화이트로 전환 |
| 히어로 | 헤드라인 라인별 마스크 슬라이드업, 카피 순차 페이드, 지표 카운트업, 스크롤 라인 루프 |
| 마퀴 | 무한 루프(38s), hover 시 감속 |
| AI Agent | 격자·물결 페이드인 + 물결 좌우 유영, 얼굴 스케일 인, 콜아웃 8개 순차 등장(포인트 → 라인 드로잉 → 카드) |
| Science Band | 6 / 22 / 2 카운트업 |
| **Products** | **섹션 진입 시 화면 고정(pin). 배경·좌측 텍스트는 고정되고 우측 2열 스태거 제품만 위로 이동. 마지막 제품이 지나가면 pin 해제 후 다음 섹션으로 진행.** 진행률 `01/06` + 바 연동, 카드 hover 시 이미지 1.06 확대 |
| Brand | 카피 순차 등장, 디바이스 이미지 패럴랙스, 17 / 2.23 / 2 카운트업 |

`prefers-reduced-motion` 설정 시 관성 스크롤과 루프 애니메이션은 자동으로 비활성화됩니다.

## 반응형

1600 / 1280 / 1024 / 640 브레이크포인트.
1024 이하에서는 제품 섹션의 pin을 해제하고 일반 2열 그리드로 전환, 콜아웃은 숨김 처리합니다.

## 폰트

현재 Google Fonts CDN(Noto Sans KR, Inter)을 사용합니다.
완전 오프라인/로컬 번들이 필요하면 woff2를 `assets/fonts/`에 받아 `@font-face`로 교체하면 됩니다. (한글 서브셋 파일이 많아 기본은 CDN으로 두었습니다)

## 교체가 필요한 항목

- `assets/video/brand-film.mp4` — 브랜드 필름
- `assets/img/hero-poster.jpg` — 영상 첫 프레임 이미지로 교체 권장
- 각 링크 `href="#"` — 실제 라우트 연결 (설문, 제품 상세, 회사소개 등)


---

## 페이지 / 링크 구조

| 페이지 | 파일 | 비고 |
|---|---|---|
| 메인 | `index.html` | |
| 회사소개 | `about.html` | 서브비주얼 + 라인 구분 서브메뉴 (6탭 공통) |
| 인사말 | `greeting.html` | 대표 포트레이트 자리 |
| 연혁 | `history.html` | 타임라인 + 하단 이미지 자리 |
| 인증 | `certification.html` | 인증서 갤러리 4×2 |
| 미션과 비전 | `mission-vision.html` | 3축 + 이미지 자리 3개 |
| 오시는 길 | `location.html` | 지도 임베드 자리 |
| 설문 | `survey.html` | 인트로 → 18문항 → 완료 |

**연결된 링크**

- GNB: careCL → `about.html` / Aging Map 22 → `survey.html` / Product → `index.html#products` / Contact → `location.html`
- 헤더 우측 `진단 시작`, 메인 CTA `노화 타입 진단 설문 시작하기` → `survey.html`
- 메인 히어로 `careCL`, 브랜드 섹션 `회사소개 보기` → `about.html`
- 회사소개 서브메뉴 6개 → 각 페이지 상호 연결
- 푸터: BRAND / AGING MAP 22 / SUPPORT 그룹 링크 연결
- 로고 클릭 → `index.html`

## 설문 동작

`js/survey.js` 안에 18문항 데이터가 들어 있습니다 (출처: `노화 진단 Test - final.xlsx`).

- 화면당 1문항, 선택 시 좌측에 하늘색 체크 원이 걸쳐 나타남
- Q15는 최대 3개 다중선택, **Q16은 Q15에서 고른 부위만 보기로 자동 생성**
- 이전/다음, 진행률 `NN / 18` + 바 연동, 미응답 시 다음 버튼 비활성화
- 각 보기에 `type`(피로형·초기노화형·잔주름형·변형처짐형·근육형) 값이 붙어 있어 완료 화면에서 임시 집계합니다 — **실제 6타입 판정 로직은 확정 후 교체 필요**
- 완료 화면은 임시입니다. 리포트 페이지 제작 시 `renderDone()`을 교체하거나 결과 페이지로 이동시키면 됩니다

## 회사소개 페이지 수정 방법

6개 페이지는 `build_sub.py`로 생성됩니다. 공통 헤더·푸터·서브메뉴를 바꾸려면 이 파일을 수정 후

```bash
python build_sub.py
```

를 실행하면 6개 HTML이 다시 만들어집니다. (개별 HTML을 직접 수정해도 무방하지만, 재생성 시 덮어써집니다)
