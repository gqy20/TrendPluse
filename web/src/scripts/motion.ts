/**
 * 全局动效入口（GSAP）。
 *
 * 设计要点：
 * - 仅在「用户未偏好减少动效」时播放；reduce 用户由 CSS 保证内容天然可见，
 *   此处 matchMedia 天然不进入回调，零配置无障碍。
 * - 全部使用 transform / autoAlpha，避免触发 layout；滚动入场用 ScrollTrigger.batch 节流。
 * - JS 若初始化失败，catch 移除 <html>.js 类，CSS 预隐藏规则随之失效，内容全部恢复可见（渐进增强兜底）。
 *
 * 通用钩子（组件只需加 class / data-*，不改结构）：
 *   [data-reveal]   滚动进入视口淡入上移（批量 stagger）
 *   [data-count-up] 数字从 0 计数到 data-count-up 指定值
 *   .impact-bar     柱状图从底部生长（scaleY 0→1）
 *   [data-hover]    悬停时轻微上浮
 *   .hero-eyebrow / .hero-title / .hero-cta  首屏 Hero 分层入场
 */
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

try {
  gsap.matchMedia().add('(prefers-reduced-motion: no-preference)', () => {
    // ── 初态（与 global.css 的 .js 预隐藏对齐，防 FOUC） ──
    gsap.set('[data-reveal]', { autoAlpha: 0, y: 16 });
    gsap.set('.impact-bar', { scaleY: 0, transformOrigin: 'bottom' });

    // ── 1. Hero 分层入场 ──
    if (gsap.utils.toArray('.hero-eyebrow, .hero-title, .hero-sub, .hero-cta').length > 0) {
      // 用 fromTo 而非 from：CSS 已把这些元素预隐藏为 opacity:0，
      // from() 会把"当前值 0"当作终点导致永远停在透明；fromTo 明确终点 autoAlpha:1 才能覆盖
      gsap
        .timeline({ defaults: { ease: 'back.out(1.4)', duration: 0.6 } })
        .fromTo('.hero-eyebrow', { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0 })
        .fromTo('.hero-title', { autoAlpha: 0, y: 14 }, { autoAlpha: 1, y: 0 }, '-=0.35')
        .fromTo('.hero-sub', { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0 }, '-=0.35')
        .fromTo('.hero-cta', { autoAlpha: 0, y: 10 }, { autoAlpha: 1, y: 0 }, '-=0.35');
    }

    // ── 2. 滚动批量入场（同时进入视口的元素自动错开） ──
    ScrollTrigger.batch('[data-reveal]', {
      start: 'top 88%',
      once: true,
      onEnter: (batch) =>
        gsap.to(batch, {
          autoAlpha: 1,
          y: 0,
          duration: 0.5,
          stagger: 0.08,
          ease: 'power2.out',
          overwrite: true,
        }),
    });

    // ── 3. 数字计数 ──
    gsap.utils.toArray<HTMLElement>('[data-count-up]').forEach((el) => {
      const end = Number(el.dataset.countUp);
      if (!Number.isFinite(end)) return;
      el.textContent = '0'; // 初态：从 0 起，进入视口再滚到终值
      const obj = { v: 0 };
      ScrollTrigger.create({
        trigger: el,
        start: 'top 92%',
        once: true,
        onEnter: () =>
          gsap.to(obj, {
            v: end,
            duration: 1.1,
            ease: 'power2.out',
            snap: { v: 1 },
            onUpdate: () => {
              el.textContent = Math.round(obj.v).toLocaleString();
            },
          }),
      });
    });

    // ── 4. 柱状图从底部生长 ──
    ScrollTrigger.batch('.impact-bar', {
      start: 'top 90%',
      once: true,
      onEnter: (batch) =>
        gsap.to(batch, {
          scaleY: 1,
          duration: 0.7,
          stagger: 0.08,
          ease: 'power3.out',
        }),
    });

    // ── 5. 悬停微交互 ──
    gsap.utils.toArray<HTMLElement>('[data-hover]').forEach((el) => {
      el.addEventListener('mouseenter', () =>
        gsap.to(el, { y: -3, duration: 0.2, ease: 'power2.out' }),
      );
      el.addEventListener('mouseleave', () =>
        gsap.to(el, { y: 0, duration: 0.2, ease: 'power2.out' }),
      );
    });
  });
} catch (err) {
  // 兜底：动画初始化失败时移除 .js 类，CSS 预隐藏规则失效，内容全部恢复可见
  console.error('[motion] 初始化失败，降级为无动画：', err);
  document.documentElement.classList.remove('js');
}
