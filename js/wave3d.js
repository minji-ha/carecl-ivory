/* =========================================================
   careCL — 3D 와이어프레임 물결 배경 (+ 떠오르는 빛 입자)
   원본: 산림공간디지털플랫폼 index_v2.html (three.js r160)
   사용: <div data-wave="light"></div>  /  <div data-wave="dark"></div>
   ========================================================= */
import * as THREE from '../libs/three/three.module.min.js';

const THEMES = {
  /* 흰 배경 섹션 (메인 AI Agent) */
  light: { fog: 0xffffff, grid: 0xc46a3a, gridOpacity: 0.22, dot: [91, 191, 236], dotOpacity: 0.42, camY: 3.2, camZ: 30 },
  /* 어두운 패널 (설문 좌측) */
  dark:  { fog: 0x0e1820, grid: 0xe0a77f, gridOpacity: 0.16, dot: [135, 211, 242], dotOpacity: 0.55, camY: 4.2, camZ: 26 }
};

document.querySelectorAll('[data-wave]').forEach(host => init(host, THEMES[host.dataset.wave] || THEMES.light));

function init(host, theme) {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const watchEl = host.closest('.agent, .sv__panel') || host;

  let W = Math.max(1, host.clientWidth);
  let H = Math.max(1, host.clientHeight);

  const scene = new THREE.Scene();
  scene.fog = new THREE.FogExp2(theme.fog, 0.016);

  const camera = new THREE.PerspectiveCamera(70, W / H, 0.1, 1000);
  camera.position.set(0, theme.camY, theme.camZ);
  camera.lookAt(0, -3, 0);

  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(W, H);
  renderer.setClearColor(0x000000, 0);
  host.appendChild(renderer.domElement);

  /* 와이어프레임 평면 — 잔잔한 물결 */
  const gridGeo = new THREE.PlaneGeometry(220, 220, 70, 70);
  const basePos = gridGeo.attributes.position.array.slice();
  const terrain = new THREE.Mesh(gridGeo, new THREE.MeshBasicMaterial({
    color: theme.grid, wireframe: true, transparent: true, opacity: theme.gridOpacity
  }));
  terrain.rotation.x = -Math.PI / 2;
  terrain.position.y = -7;
  scene.add(terrain);

  /* 빛 입자 */
  const pCount = 200;
  const pPos = new Float32Array(pCount * 3);
  for (let i = 0; i < pCount * 3; i++) pPos[i] = (Math.random() - 0.5) * 160;
  const pGeo = new THREE.BufferGeometry();
  pGeo.setAttribute('position', new THREE.BufferAttribute(pPos, 3));

  const c = document.createElement('canvas');
  c.width = c.height = 64;
  const g = c.getContext('2d');
  const [r, gg, b] = theme.dot;
  const grad = g.createRadialGradient(32, 32, 0, 32, 32, 32);
  grad.addColorStop(0, `rgba(${r},${gg},${b},1)`);
  grad.addColorStop(0.45, `rgba(${r},${gg},${b},.45)`);
  grad.addColorStop(1, `rgba(${r},${gg},${b},0)`);
  g.fillStyle = grad;
  g.beginPath(); g.arc(32, 32, 32, 0, Math.PI * 2); g.fill();

  const particles = new THREE.Points(pGeo, new THREE.PointsMaterial({
    size: 0.7, sizeAttenuation: true, map: new THREE.CanvasTexture(c),
    transparent: true, opacity: theme.dotOpacity, depthWrite: false
  }));
  scene.add(particles);

  const clock = new THREE.Clock();
  const pos = gridGeo.attributes.position;
  let visible = true;

  function frame() {
    requestAnimationFrame(frame);
    if (!visible) return;
    const t = reduceMotion ? 0 : clock.getElapsedTime();
    for (let i = 0; i < pos.count; i++) {
      const x = basePos[i * 3];
      const y = basePos[i * 3 + 1];
      pos.setZ(i,
        Math.sin(x * 0.12 + t * 1.2) * 2.6 +
        Math.cos(y * 0.10 - t * 1.0) * 2.6 +
        Math.sin((x + y) * 0.06 + t * 0.5) * 1.4);
    }
    pos.needsUpdate = true;
    particles.rotation.y = t * 0.04;
    renderer.render(scene, camera);
  }
  frame();

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(e => { visible = e[0].isIntersecting; }, { rootMargin: '120px' }).observe(watchEl);
  }

  function fit() {
    W = Math.max(1, host.clientWidth);
    H = Math.max(1, host.clientHeight);
    camera.aspect = W / H;
    camera.updateProjectionMatrix();
    renderer.setSize(W, H);
  }
  if ('ResizeObserver' in window) new ResizeObserver(fit).observe(host);
  else window.addEventListener('resize', fit);
}
