/**
 * TrendPulse 动画和交互增强
 *
 * 提供：
 * - 信号卡片展开/折叠动画
 * - 平滑滚动效果
 * - 增强的卡片悬停效果
 * - 进入动画（staggered fade-in）
 * - 响应式菜单切换
 */

(function () {
  "use strict";

  // 配置
  const CONFIG = {
    staggerDelay: 100, // 卡片进入动画延迟（毫秒）
    scrollDuration: 300, // 平滑滚动持续时间（毫秒）
    hoverScale: 1.02, // 悬停时缩放比例
    hoverShadow: "0 8px 25px rgba(0,0,0,0.15)", // 悬停时阴影
  };

  // 等待 DOM 加载完成
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  /**
   * 初始化动画和交互
   */
  function init() {
    // 只在报告页面启用
    if (!document.querySelector(".bento-grid")) {
      return;
    }

    initCardAnimations();
    initSmoothScroll();
    initHoverEffects();
    initScrollAnimations();
    initMobileMenu();
  }

  /**
   * 初始化卡片动画
   */
  function initCardAnimations() {
    // 为所有信号卡片添加展开/折叠动画监听
    document.querySelectorAll(".signal-card details").forEach((details, index) => {
      // 添加初始动画延迟
      details.style.animationDelay = `${index * CONFIG.staggerDelay}ms`;

      // 监听展开事件
      details.addEventListener("toggle", function (e) {
        const card = this.closest(".signal-card");
        if (!card) return;

        if (this.open) {
          // 展开：添加动画类
          card.classList.add("is-expanding");
          setTimeout(() => {
            card.classList.remove("is-expanding");
            card.classList.add("is-expanded");
          }, 300);
        } else {
          // 折叠：移除展开状态
          card.classList.remove("is-expanded");
          card.classList.add("is-collapsing");
          setTimeout(() => {
            card.classList.remove("is-collapsing");
          }, 300);
        }
      });
    });

    // 为卡片内容添加展开动画
    document.querySelectorAll(".signal-details").forEach((details) => {
      details.addEventListener("toggle", function (e) {
        const content = this.querySelector(".signal-body");
        const footer = this.querySelector(".signal-footer");

        if (!content || !footer) return;

        if (this.open) {
          // 内容滑入动画
          content.style.opacity = "0";
          content.style.transform = "translateY(-10px)";

          footer.style.opacity = "0";
          footer.style.transform = "translateY(-10px)";

          // 强制重绘
          void content.offsetWidth;

          // 触发动画
          requestAnimationFrame(() => {
            content.style.transition = "all 0.3s ease";
            footer.style.transition = "all 0.3s ease 0.1s";

            content.style.opacity = "1";
            content.style.transform = "translateY(0)";

            footer.style.opacity = "1";
            footer.style.transform = "translateY(0)";
          });
        }
      });
    });
  }

  /**
   * 初始化平滑滚动
   */
  function initSmoothScroll() {
    // 为所有内部链接添加平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
      anchor.addEventListener("click", function (e) {
        const targetId = this.getAttribute("href");
        if (targetId === "#") return;

        const target = document.querySelector(targetId);
        if (!target) {
          e.preventDefault();
          return;
        }

        e.preventDefault();
        scrollToElement(target);
      });
    });

    // 为筛选按钮添加滚动到网格功能
    document.querySelectorAll(".filter-btn").forEach((btn) => {
      btn.addEventListener("click", function () {
        const filterBar = this.closest(".filter-bar");
        if (!filterBar) return;

        const grid = filterBar.nextElementSibling;
        if (!grid || !grid.matches(".bento-grid")) return;

        // 平滑滚动到网格顶部
        scrollIntoView(grid, { block: "start", behavior: "smooth" });
      });
    });
  }

  /**
   * 滚动到元素
   */
  function scrollIntoView(element, options = {}) {
    const defaultOptions = {
      behavior: "smooth",
      block: "start",
      inline: "nearest",
    };

    const mergedOptions = { ...defaultOptions, ...options };

    if (element.scrollIntoView) {
      element.scrollIntoView(mergedOptions);
    } else {
      // 回退方案
      const targetPosition =
        element.getBoundingClientRect().top + window.pageYOffset - 80;
      window.scrollTo({
        top: targetPosition,
        behavior: "smooth",
      });
    }
  }

  /**
   * 滚动到指定元素（兼容方法）
   */
  function scrollToElement(target) {
    const targetPosition =
      target.getBoundingClientRect().top + window.pageYOffset - 80;

    window.scrollTo({
      top: targetPosition,
      behavior: "smooth",
    });
  }

  /**
   * 初始化悬停效果
   */
  function initHoverEffects() {
    // 为所有信号卡片添加悬停效果
    document.querySelectorAll(".signal-card").forEach((card) => {
      // 鼠标进入
      card.addEventListener("mouseenter", function () {
        if (this.classList.contains("signal-empty")) return;

        this.style.transform = `scale(${CONFIG.hoverScale})`;
        this.style.boxShadow = CONFIG.hoverShadow;
        this.style.zIndex = "10";
      });

      // 鼠标离开
      card.addEventListener("mouseleave", function () {
        if (this.classList.contains("signal-empty")) return;

        this.style.transform = "";
        this.style.boxShadow = "";
        this.style.zIndex = "";
      });

      // 聚焦效果（键盘导航）
      const details = card.querySelector("details");
      if (details) {
        details.addEventListener("focus", function () {
          card.classList.add("is-focused");
        });

        details.addEventListener("blur", function () {
          card.classList.remove("is-focused");
        });
      }
    });

    // 为按钮添加波纹效果
    document.querySelectorAll(".filter-btn, .action-btn").forEach((btn) => {
      btn.addEventListener("click", createRippleEffect);
    });
  }

  /**
   * 创建波纹效果
   */
  function createRippleEffect(e) {
    const button = e.currentTarget;
    const ripple = document.createElement("span");
    const rect = button.getBoundingClientRect();
    const size = Math.max(rect.width, rect.height);
    const x = e.clientX - rect.left - size / 2;
    const y = e.clientY - rect.top - size / 2;

    ripple.style.width = ripple.style.height = `${size}px`;
    ripple.style.left = `${x}px`;
    ripple.style.top = `${y}px`;
    ripple.classList.add("ripple");

    // 移除旧的波纹
    const oldRipple = button.querySelector(".ripple");
    if (oldRipple) {
      oldRipple.remove();
    }

    button.appendChild(ripple);

    // 动画结束后移除
    setTimeout(() => {
      ripple.remove();
    }, 600);
  }

  /**
   * 初始化滚动动画
   */
  function initScrollAnimations() {
    // 为所有 Bento Grid 添加滚动进入动画
    const observerOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.1,
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          // 动画完成后停止观察
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // 观察所有 Bento Grid
    document.querySelectorAll(".bento-grid").forEach((grid) => {
      grid.classList.add("fade-in-section");
      observer.observe(grid);
    });

    // 为每个卡片添加延迟动画
    document.querySelectorAll(".signal-card").forEach((card, index) => {
      card.style.animationDelay = `${index * 50}ms`;
      card.classList.add("fade-in-card");
    });
  }

  /**
   * 初始化移动端菜单
   */
  function initMobileMenu() {
    // 检查是否有移动端菜单
    const menuToggle = document.querySelector(
      '[data-md-toggle="drawer"]'
    );
    if (!menuToggle) return;

    // 监听菜单状态变化
    menuToggle.addEventListener("change", function () {
      const body = document.body;
      if (this.checked) {
        body.classList.add("menu-open");
      } else {
        body.classList.remove("menu-open");
      }
    });

    // 点击菜单外部时关闭
    document.addEventListener("click", function (e) {
      const drawer = document.querySelector('[data-md-component="drawer"]');
      if (!drawer) return;

      if (
        menuToggle.checked &&
        !drawer.contains(e.target) &&
        !e.target.closest('[data-md-toggle="drawer"]')
      ) {
        menuToggle.checked = false;
        document.body.classList.remove("menu-open");
      }
    });
  }

  /**
   * 平滑更新筛选结果（动画过渡）
   */
  function animateFilterUpdate(grid, hiddenCards, visibleCards) {
    // 淡出隐藏的卡片
    hiddenCards.forEach((card) => {
      card.style.transition = "opacity 0.3s ease, transform 0.3s ease";
      card.style.opacity = "0";
      card.style.transform = "scale(0.95)";

      setTimeout(() => {
        card.style.display = "none";
      }, 300);
    });

    // 显示可见的卡片
    visibleCards.forEach((card, index) => {
      const wasHidden = card.style.display === "none";
      card.style.display = "";

      if (wasHidden) {
        card.style.opacity = "0";
        card.style.transform = "scale(0.95)";

        // 强制重绘
        void card.offsetWidth;

        // 延迟触发动画
        setTimeout(() => {
          card.style.transition = "opacity 0.3s ease, transform 0.3s ease";
          card.style.opacity = "1";
          card.style.transform = "scale(1)";
        }, index * 50);
      }
    });
  }

  // 导出到全局作用域（供其他脚本使用）
  window.TrendPulseAnimations = {
    animateFilterUpdate,
    scrollIntoView,
    CONFIG,
  };
})();
