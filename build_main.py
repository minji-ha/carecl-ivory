# -*- coding: utf-8 -*-
"""메인페이지 v2 생성 — 케어클 노션 '메인페이지 뼈대' 구성. python build_main.py"""
import io
import time
import parts

V = time.strftime('%y%m%d%H%M%S')

# 롤링 배너 섹션 — 상단 영상 배너가 그 역할을 하므로 주석 처리 (필요 시 BODY 안에 다시 넣으면 된다)
MROLL_DISABLED = """
  <!-- 02 롤링 배너 -->
  <section class="mroll" data-roll>
    <div class="inner">
      <div class="mroll__stage">
        <div class="mroll__track">

          <div class="mroll__slide">
            <img src="assets/img/p-leaning.jpg" alt="careCL TECHFIT">
            <div class="mroll__cap">
              <em>NEW DEVICE</em>
              <b>문지르지 않습니다<br>정해진 자리에 5초, 눌러서 전달합니다</b>
              <p>TECHFIT 스탬핑 고주파 디바이스</p>
              <a href="products.html">제품 보기 →</a>
            </div>
          </div>

          <div class="mroll__slide">
            <img src="assets/img/p-eye.jpg" alt="Aging Map 22">
            <div class="mroll__cap">
              <em>AGING MAP 22</em>
              <b>어디를 먼저 관리해야 할까요</b>
              <p>얼굴과 목·바디를 22개 부위로 나누어 우선순위를 제안합니다</p>
              <a href="aging-map.html">진단 체계 보기 →</a>
            </div>
          </div>

          <div class="mroll__slide mroll__slide--cos">
            <img src="assets/img/p-devices-w.jpg" alt="careCL 제품 라인업">
            <div class="mroll__cap">
              <em>COSMETICS</em>
              <b>디바이스와 함께 쓰는<br>전용 코스메틱</b>
              <p>콜라겐 부스터 젤 · 그리드 마스크 · 토닝 세럼</p>
              <a href="cosmetics.html">코스메틱 보기 →</a>
            </div>
          </div>

        </div>
      </div>

      <div class="mroll__ui">
        <div class="mroll__dots">
          <button type="button" aria-label="1번 배너"></button>
          <button type="button" aria-label="2번 배너"></button>
          <button type="button" aria-label="3번 배너"></button>
        </div>
        <div class="mroll__arrows">
          <button type="button" data-roll-prev aria-label="이전 배너"><i class="fa-solid fa-angle-left"></i></button>
          <button type="button" data-roll-next aria-label="다음 배너"><i class="fa-solid fa-angle-right"></i></button>
        </div>
      </div>
    </div>
  </section>

"""

BODY = """
<main class="m2">

  <!-- 01 상단 배너 -->
  <section class="mhero">
    <div class="mhero__media">
      <video class="mhero__video" autoplay muted loop playsinline poster="assets/img/hero-poster.jpg">
        <source src="assets/video/brand-film.mp4" type="video/mp4">
      </video>
    </div>
    <div class="mhero__scrim"></div>
    <div class="mhero__inner">
      <p class="mhero__eyebrow">ANTI-AGING SKINCARE</p>
      <h1>노화는 저마다 다릅니다<br>그래서 관리도 달라야 합니다</h1>
      <p>케어클은 얼굴을 22개 부위로 나누어 읽고, 먼저 관리해야 할 곳부터 제안합니다.</p>
      <div class="mhero__cta">
        <a href="aging-types.html" class="mbtn mbtn--solid">6가지 노화 타입 보기</a>
        <a href="survey.html" class="mbtn mbtn--line">나의 타입 알아보기</a>
      </div>
    </div>
    <div class="mhero__scroll"><span>SCROLL</span><i></i></div>
  </section>

  <!-- 02 배너 설명 -->
  <section class="mbinfo">
    <div class="inner">
      <div class="mbinfo__head">
        <span class="label" data-fx="up">careCL Solution</span>
        <h2 data-fx="lines">케어클이 제안하는<br>세 가지 홈 에이징 케어</h2>
      </div>

      <a class="mbrow" href="products.html" data-fx="up">
        <span class="mbrow__tag">Device</span>
        <div class="mbrow__txt">
          <b>Device Solution</b>
          <strong>정해진 자리에 머무르는 스탬핑 디바이스</strong>
          <p>문지르지 않고 관리할 부위에 머물러 에너지를 전달합니다.</p>
        </div>
        <div class="mbrow__img"><img src="assets/img/p-cheek.jpg" alt="뷰티 디바이스" data-fx-para="10"></div>
      </a>

      <a class="mbrow" href="cosmetics.html" data-fx="up">
        <span class="mbrow__tag">Cosmetics</span>
        <div class="mbrow__txt">
          <b>Beauty Solution</b>
          <strong>디바이스와 함께 쓰는 전용 코스메틱</strong>
          <p>그리드 마스크와 전용 제형으로 관리 위치를 정확히 안내합니다.</p>
        </div>
        <div class="mbrow__img"><img src="assets/img/p-packs.jpg" alt="전용 코스메틱" data-fx-para="10"></div>
      </a>

      <a class="mbrow" href="aging-map.html" data-fx="up">
        <span class="mbrow__tag">Aging Map 22</span>
        <div class="mbrow__txt">
          <b>Care Solution</b>
          <strong>얼굴과 목 · 바디를 22개 부위로</strong>
          <p>나의 노화 방식을 이해하고 먼저 관리할 곳부터 순서대로 제안합니다.</p>
        </div>
        <div class="mbrow__img"><img src="assets/img/p-mask-face.jpg" alt="부위별 케어" data-fx-para="10"></div>
      </a>
    </div>
  </section>

  <!-- 03 철학 -->
  <section class="mphil">
    <div class="inner" data-reveal>
      <span class="label">Our Philosophy</span>
      <h2 data-fx="lines">같은 나이라도<br>노화가 시작되는 자리는 저마다 다릅니다</h2>
      <p class="lead">유전, 뼈의 구조, 얼굴 근육의 발달, 피하 지방의 양에 따라 처짐이 먼저 오기도 하고 주름이 먼저 생기기도 합니다.
      케어클은 그 차이를 먼저 읽는 것에서 안티에이징을 시작합니다. 모두에게 같은 제품을 권하지 않습니다.</p>
      <p class="mphil__en">Read precisely, care exactly.</p>
    </div>
  </section>

  <!-- 04 핵심 3가지 (오브젝트 + 주변 항목) -->
  <section class="mcore">
    <div class="inner">
      <div class="mcore__head" data-reveal>
        <span class="label">How careCL Works</span>
        <h2>읽고 · 찾고 · 전달합니다</h2>
      </div>

      <div class="mcore__stage" data-core>
        <div class="mcore__ring"></div>
        <div class="mcore__object"><img src="assets/img/face.png" alt=""></div>

        <div class="mcore__item mcore__item--sky">
          <em>01 READ</em><b>6가지 노화 타입</b>
          <p>나는 어떤 방식으로 나이 들고 있는가</p>
          <a href="aging-types.html">타입 보기</a>
        </div>
        <div class="mcore__item mcore__item--sky">
          <em>02 MAP</em><b>22개 관리 부위</b>
          <p>어디를 먼저 관리해야 하는가</p>
          <a href="aging-map.html">부위 보기</a>
        </div>
        <div class="mcore__item">
          <em>03 TECH</em><b>5초 스탬핑</b>
          <p>어떻게 전달할 것인가</p>
          <a href="carecl-technology.html">기술 보기</a>
        </div>
        <div class="mcore__item">
          <em>04 PRODUCT</em><b>디바이스 · 코스메틱</b>
          <p>무엇으로 관리할 것인가</p>
          <a href="products.html">제품 보기</a>
        </div>
        <div class="mcore__item mcore__item--sky">
          <em>05 AI AGENT</em><b>AI 피부 진단</b>
          <p>2분 진단으로 나의 타입과 우선 부위 확인</p>
          <a href="survey.html">진단 시작</a>
        </div>
      </div>

      <div class="mcore__cta">
        <a href="survey.html" class="mbtn mbtn--ink">나의 Aging Type 알아보기 &nbsp;→</a>
      </div>
    </div>
  </section>

  <!-- 05 환기용 이미지 -->
  <section class="mbreak">
    <img src="assets/img/p-leaning.jpg" alt="" data-fx-zoom>
    <p class="mbreak__txt">클리닉의 기술을, 집 안의 리추얼로</p>
  </section>

  <!-- 06 콜렉션 (카로셀) -->
  <section class="mcoll" data-coll>
    <div class="inner">
      <div class="mcoll__head" data-reveal>
        <div>
          <span class="label">Collection</span>
          <h2 data-fx="lines">진단 결과에 맞춰<br>조합하는 제품</h2>
        </div>
        <div class="mroll__arrows">
          <button type="button" data-coll-prev aria-label="이전 제품"><i class="fa-solid fa-angle-left"></i></button>
          <button type="button" data-coll-next aria-label="다음 제품"><i class="fa-solid fa-angle-right"></i></button>
        </div>
      </div>

      <div class="mcoll__viewport">
        <div class="mcoll__track">
          <a class="mcard" href="products.html"><div class="mcard__img"><img src="assets/img/product-techfit.jpg" alt="TECHFIT"></div><em>DEVICE</em><b>TECHFIT</b><span>5초 스탬핑 고주파 디바이스</span></a>
          <a class="mcard" href="products.html"><div class="mcard__img"><img src="assets/img/product-clb.png" alt="CLB"></div><em>DEVICE</em><b>CLB</b><span>고주파 마사지기</span></a>
          <a class="mcard" href="cosmetics.html"><div class="mcard__img"><img src="assets/img/product-gel.png" alt="Collagen Booster Gel"></div><em>COSMETIC</em><b>Collagen Booster Gel</b><span>콜라겐 부스터 젤</span></a>
          <a class="mcard" href="cosmetics.html"><div class="mcard__img"><img src="assets/img/product-mask.jpg" alt="Grid Mask"></div><em>COSMETIC</em><b>Grid Mask</b><span>그리드 마스크</span></a>
          <a class="mcard" href="cosmetics.html"><div class="mcard__img"><img src="assets/img/product-serum.jpg" alt="Toning Serum"></div><em>COSMETIC</em><b>Toning Serum</b><span>라이트 토닝 세럼</span></a>
          <a class="mcard" href="products.html"><div class="mcard__img"><img src="assets/img/product-bag.jpg" alt="Case"></div><em>ACCESSORY</em><b>전용 케이스</b><span>디바이스 보관 가죽 케이스</span></a>
        </div>
      </div>
    </div>
  </section>

  <!-- 07 5 STEP -->
  <section class="mstep" data-step>
    <div class="inner">
      <div class="mstep__head">
        <span class="label">Daily Routine</span>
        <h2 data-fx="lines">다섯 단계로 이어지는<br>홈 에이징 케어</h2>
        <p class="mstep__lead" data-fx="up">하루 10분. 같은 자리를 반복하는 동안 피부는 기록을 남깁니다.</p>
      </div>
      <div class="mstep__rail"><i data-step-bar></i></div>
      <div class="mstep__grid">
        <div class="mstep__card" data-step-card>
          <i class="mstep__fill"></i>
          <span class="mstep__ghost" aria-hidden="true">01</span>
          <span class="mstep__no">01</span>
          <em>CLEANSE</em><b>씻어냅니다</b><p>잔여물을 정리해 다음 단계가 제대로 전달되도록 준비합니다.</p>
        </div>
        <div class="mstep__card" data-step-card>
          <i class="mstep__fill"></i>
          <span class="mstep__ghost" aria-hidden="true">02</span>
          <span class="mstep__no">02</span>
          <em>READ</em><b>읽습니다</b><p>오늘 먼저 관리할 부위를 Aging Map 22 기준으로 확인합니다.</p>
        </div>
        <div class="mstep__card" data-step-card>
          <i class="mstep__fill"></i>
          <span class="mstep__ghost" aria-hidden="true">03</span>
          <span class="mstep__no">03</span>
          <em>ACTIVATE</em><b>깨웁니다</b><p>한 부위에 머무르며 수직으로 전달합니다.</p>
        </div>
        <div class="mstep__card" data-step-card>
          <i class="mstep__fill"></i>
          <span class="mstep__ghost" aria-hidden="true">04</span>
          <span class="mstep__no">04</span>
          <em>RECOVERY</em><b>채웁니다</b><p>전용 코스메틱으로 전달 직후의 피부를 안정시킵니다.</p>
        </div>
        <div class="mstep__card" data-step-card>
          <i class="mstep__fill"></i>
          <span class="mstep__ghost" aria-hidden="true">05</span>
          <span class="mstep__no">05</span>
          <em>MAINTAIN</em><b>이어갑니다</b><p>주 2~3회 같은 자리를 반복해 변화를 기록합니다.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- 08 샵 링크 -->
  <section class="mshop">
    <div class="mshop__bg"><img src="assets/img/p-mask-close.jpg" alt=""></div>
    <div class="inner mshop__inner">
      <div>
        <h2>제품 구매는 공식몰에서</h2>
        <p>진단 결과에 맞는 구성으로 담아 보세요.</p>
      </div>
      <a href="#" class="mbtn mbtn--solid">SHOP 바로가기 &nbsp;→</a>
    </div>
  </section>

  <!-- 10 컨택트 -->
  <!-- CARECL 롤링 -->
  <section class="mmarq" aria-hidden="true">
    <div class="mmarq__track">
      <span>CARECL</span><span>CARECL</span><span>CARECL</span><span>CARECL</span>
      <span>CARECL</span><span>CARECL</span><span>CARECL</span><span>CARECL</span>
    </div>
  </section>

  <section class="mcontact">
    <div class="inner">
      <div data-reveal>
        <span class="label">Contact</span>
        <h2>케어클과 함께하실 분들께</h2>
      </div>
      <div class="mcontact__grid">
        <div class="mcontact__card"><em>GLOBAL BUSINESS</em><b>해외 사업</b><p>수출 · 해외 유통 문의<br>support@carecl.co.kr</p></div>
        <div class="mcontact__card"><em>PARTNERSHIP</em><b>유통 · 제휴</b><p>총판 및 제휴 제안<br>support@carecl.co.kr</p></div>
        <div class="mcontact__card"><em>MEDIA / PR</em><b>미디어</b><p>취재 · 광고 · 협찬<br>support@carecl.co.kr</p></div>
        <div class="mcontact__card"><em>GENERAL</em><b>일반 문의</b><p>제품 사용 · A/S<br>TEL +82 31-943-1028</p></div>
      </div>
    </div>
  </section>

</main>
"""

TPL = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>careCL 케어클 — 정밀하게 읽고, 부위별로 되돌리다</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<link rel="stylesheet" href="libs/fontawesome/css/all.min.css">
<link rel="stylesheet" href="css/style.css?v=%(v)s">
<link rel="stylesheet" href="css/nav.css?v=%(v)s">
<link rel="stylesheet" href="css/theme-ivory.css?v=%(v)s">
<link rel="stylesheet" href="css/mainv2.css?v=%(v)s">
<link rel="stylesheet" href="css/intro.css?v=%(v)s">
</head>
<body class="main2 is-intro">

<div class="intro" id="intro">
  <canvas class="intro__grid"></canvas>
  <div class="intro__center">
    <span class="intro__logo">CARECL</span>
    <span class="intro__num">000</span>
    <span class="intro__bar"><i></i></span>
    <span class="intro__tag">AGING MAP 22</span>
  </div>
</div>

%(header)s

%(body)s

%(footer)s

<script src="libs/lenis.min.js"></script>
<script src="js/intro.js?v=%(v)s"></script>
<script src="js/mainv2.js?v=%(v)s"></script>
<script src="js/scrollfx.js?v=%(v)s"></script>
<script src="js/cursorword.js"></script>
<script src="js/nav.js?v=%(v)s"></script>
</body>
</html>
"""

html = TPL % {"v": V, "header": parts.header(active=None), "body": BODY, "footer": parts.FOOTER}
io.open("index.html", "w", encoding="utf-8").write(html)
print("built index.html", V)
