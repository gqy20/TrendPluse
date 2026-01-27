/**
 * TrendPulse 信号筛选和交互功能
 *
 * 提供：
 * - 按影响级别和类型筛选信号
 * - 搜索框功能
 * - 展开/折叠所有信号
 * - 排序功能（按评分/日期）
 */

(function () {
  "use strict";

  // 等待 DOM 加载完成
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  /**
   * 初始化筛选和交互功能
   */
  function init() {
    // 只在报告页面启用
    if (!document.querySelector(".bento-grid")) {
      return;
    }

    createFilterBar();
    attachEventListeners();
    restoreFilterState();
  }

  /**
   * 创建筛选栏
   */
  function createFilterBar() {
    const firstGrid = document.querySelector(".bento-grid");
    if (!firstGrid) return;

    const header = firstGrid.previousElementSibling;
    if (!header || !header.matches("h2")) return;

    const category = header.textContent.trim();

    const filterBar = document.createElement("div");
    filterBar.className = "filter-bar";
    filterBar.dataset.category = category;

    filterBar.innerHTML = `
      <div class="filter-section">
        <label class="filter-label">影响级别</label>
        <div class="filter-group" data-filter-type="impact">
          <button class="filter-btn active" data-value="all">全部</button>
          <button class="filter-btn" data-value="high">高 ⭐⭐⭐⭐</button>
          <button class="filter-btn" data-value="medium">中 ⭐⭐⭐</button>
          <button class="filter-btn" data-value="low">低 ⭐⭐</button>
        </div>
      </div>
      <div class="filter-section">
        <label class="filter-label">信号类型</label>
        <div class="filter-group" data-filter-type="type">
          <button class="filter-btn active" data-value="all">全部</button>
          <button class="filter-btn" data-value="capability">🚀 能力</button>
          <button class="filter-btn" data-value="abstraction">🎨 抽象</button>
          <button class="filter-btn" data-value="workflow">⚙️ 工作流</button>
          <button class="filter-btn" data-value="eval">📊 评估</button>
          <button class="filter-btn" data-value="safety">🛡️ 安全</button>
          <button class="filter-btn" data-value="performance">⚡ 性能</button>
          <button class="filter-btn" data-value="commit">💾 提交</button>
          <button class="filter-btn" data-value="release">🎯 发布</button>
        </div>
      </div>
      <div class="filter-section filter-search">
        <label class="filter-label">搜索</label>
        <input type="text" class="search-input" placeholder="搜索标题、仓库或来源..." />
      </div>
      <div class="filter-section filter-actions">
        <button class="action-btn" id="expand-all">展开全部</button>
        <button class="action-btn" id="collapse-all">折叠全部</button>
        <button class="action-btn" id="sort-score">按评分排序</button>
      </div>
    `;

    header.parentNode.insertBefore(filterBar, firstGrid);
  }

  /**
   * 附加事件监听器
   */
  function attachEventListeners() {
    // 影响级别筛选按钮
    document.querySelectorAll('[data-filter-type="impact"] .filter-btn').forEach(
      (btn) => {
        btn.addEventListener("click", (e) => {
          const group = e.target.closest('[data-filter-type="impact"]');
          group.querySelectorAll(".filter-btn").forEach((b) =>
            b.classList.remove("active")
          );
          e.target.classList.add("active");
          applyFilters();
          saveFilterState();
        });
      }
    );

    // 类型筛选按钮
    document.querySelectorAll('[data-filter-type="type"] .filter-btn').forEach(
      (btn) => {
        btn.addEventListener("click", (e) => {
          const group = e.target.closest('[data-filter-type="type"]');
          group.querySelectorAll(".filter-btn").forEach((b) =>
            b.classList.remove("active")
          );
          e.target.classList.add("active");
          applyFilters();
          saveFilterState();
        });
      }
    );

    // 搜索输入
    document.querySelectorAll(".search-input").forEach((input) => {
      input.addEventListener("input", debounce(() => {
        applyFilters();
        saveFilterState();
      }, 300));
    });

    // 展开全部
    document.querySelectorAll("#expand-all").forEach((btn) => {
      btn.addEventListener("click", expandAll);
    });

    // 折叠全部
    document.querySelectorAll("#collapse-all").forEach((btn) => {
      btn.addEventListener("click", collapseAll);
    });

    // 按评分排序
    document.querySelectorAll("#sort-score").forEach((btn) => {
      btn.addEventListener("click", sortByScore);
    });
  }

  /**
   * 应用筛选条件
   */
  function applyFilters() {
    document.querySelectorAll(".filter-bar").forEach((filterBar) => {
      const category = filterBar.dataset.category;
      const grid = filterBar.nextElementSibling;

      if (!grid || !grid.matches(".bento-grid")) return;

      // 获取筛选条件
      const impactBtn =
        filterBar.querySelector('[data-filter-type="impact"] .filter-btn.active');
      const typeBtn =
        filterBar.querySelector('[data-filter-type="type"] .filter-btn.active');
      const searchInput = filterBar.querySelector(".search-input");

      const impactFilter = impactBtn ? impactBtn.dataset.value : "all";
      const typeFilter = typeBtn ? typeBtn.dataset.value : "all";
      const searchText = searchInput ? searchInput.value.toLowerCase() : "";

      let visibleCount = 0;

      // 筛选卡片
      grid.querySelectorAll(".signal-card").forEach((card) => {
        if (card.classList.contains("signal-empty")) {
          card.style.display = "none";
          return;
        }

        const matchesImpact = matchImpact(card, impactFilter);
        const matchesType = matchType(card, typeFilter);
        const matchesSearch = matchSearch(card, searchText);

        if (matchesImpact && matchesType && matchesSearch) {
          card.style.display = "";
          visibleCount++;
        } else {
          card.style.display = "none";
        }
      });

      // 显示结果计数
      showResultCount(filterBar, visibleCount);
    });
  }

  /**
   * 匹配影响级别
   */
  function matchImpact(card, filter) {
    if (filter === "all") return true;

    if (card.classList.contains("signal-high-impact") && filter === "high")
      return true;
    if (
      card.classList.contains("signal-medium-impact") &&
      filter === "medium"
    )
      return true;
    if (card.classList.contains("signal-low-impact") && filter === "low")
      return true;

    return false;
  }

  /**
   * 匹配信号类型
   */
  function matchType(card, filter) {
    if (filter === "all") return true;

    const typeBadge = card.querySelector(".signal-type-badge");
    if (!typeBadge) return false;

    return typeBadge.classList.contains(filter);
  }

  /**
   * 匹配搜索文本
   */
  function matchSearch(card, searchText) {
    if (!searchText) return true;

    const title = card.querySelector(".signal-title");
    const repos = card.querySelectorAll(".repo-tag");
    const sources = card.querySelectorAll(".signal-sources a");

    const titleText = title ? title.textContent.toLowerCase() : "";
    const repoText = Array.from(repos)
      .map((r) => r.textContent.toLowerCase())
      .join(" ");
    const sourceText = Array.from(sources)
      .map((s) => s.textContent.toLowerCase())
      .join(" ");

    return (
      titleText.includes(searchText) ||
      repoText.includes(searchText) ||
      sourceText.includes(searchText)
    );
  }

  /**
   * 显示结果计数
   */
  function showResultCount(filterBar, count) {
    let countBadge = filterBar.querySelector(".result-count");
    if (!countBadge) {
      countBadge = document.createElement("span");
      countBadge.className = "result-count";
      filterBar
        .querySelector(".filter-actions")
        .insertBefore(
          countBadge,
          filterBar.querySelector(".filter-actions").firstChild
        );
    }
    countBadge.textContent = `显示 ${count} 个`;
  }

  /**
   * 展开全部信号
   */
  function expandAll() {
    document.querySelectorAll(".signal-card details").forEach((details) => {
      details.open = true;
    });
  }

  /**
   * 折叠全部信号
   */
  function collapseAll() {
    document.querySelectorAll(".signal-card details").forEach((details) => {
      details.open = false;
    });
  }

  /**
   * 按评分排序
   */
  function sortByScore() {
    document.querySelectorAll(".bento-grid").forEach((grid) => {
      const cards = Array.from(grid.querySelectorAll(".signal-card")).filter(
        (card) => !card.classList.contains("signal-empty")
      );

      if (cards.length === 0) return;

      // 检查当前排序状态
      const isAscending = grid.dataset.sortOrder === "asc";

      cards.sort((a, b) => {
        const scoreA = extractScore(a);
        const scoreB = extractScore(b);

        // 按评分降序/升序排列
        return isAscending ? scoreA - scoreB : scoreB - scoreA;
      });

      // 重新插入卡片
      cards.forEach((card) => grid.appendChild(card));

      // 切换排序状态
      grid.dataset.sortOrder = isAscending ? "desc" : "asc";

      // 更新按钮文本
      const sortBtn = grid.previousElementSibling?.querySelector("#sort-score");
      if (sortBtn) {
        sortBtn.textContent = isAscending
          ? "按评分排序 ↓"
          : "按评分排序 ↑";
      }
    });
  }

  /**
   * 从卡片中提取评分
   */
  function extractScore(card) {
    const scoreEl = card.querySelector(".signal-score");
    if (!scoreEl) return 0;

    const match = scoreEl.textContent.match(/\((\d+)\//);
    return match ? parseInt(match[1], 10) : 0;
  }

  /**
   * 保存筛选状态到 localStorage
   */
  function saveFilterState() {
    const state = {};

    document.querySelectorAll(".filter-bar").forEach((filterBar) => {
      const category = filterBar.dataset.category;

      const impactBtn =
        filterBar.querySelector('[data-filter-type="impact"] .filter-btn.active');
      const typeBtn =
        filterBar.querySelector('[data-filter-type="type"] .filter-btn.active');
      const searchInput = filterBar.querySelector(".search-input");

      state[category] = {
        impact: impactBtn ? impactBtn.dataset.value : "all",
        type: typeBtn ? typeBtn.dataset.value : "all",
        search: searchInput ? searchInput.value : "",
      };
    });

    try {
      localStorage.setItem("trendpulse-filters", JSON.stringify(state));
    } catch (e) {
      // localStorage 可能被禁用
    }
  }

  /**
   * 恢复筛选状态
   */
  function restoreFilterState() {
    try {
      const saved = localStorage.getItem("trendpulse-filters");
      if (!saved) return;

      const state = JSON.parse(saved);

      Object.entries(state).forEach(([category, filters]) => {
        const filterBar = document.querySelector(
          `.filter-bar[data-category="${category}"]`
        );
        if (!filterBar) return;

        // 恢复影响级别筛选
        if (filters.impact) {
          const impactBtn = filterBar.querySelector(
            `[data-filter-type="impact"] .filter-btn[data-value="${filters.impact}"]`
          );
          if (impactBtn) {
            filterBar
              .querySelectorAll('[data-filter-type="impact"] .filter-btn')
              .forEach((b) => b.classList.remove("active"));
            impactBtn.classList.add("active");
          }
        }

        // 恢复类型筛选
        if (filters.type) {
          const typeBtn = filterBar.querySelector(
            `[data-filter-type="type"] .filter-btn[data-value="${filters.type}"]`
          );
          if (typeBtn) {
            filterBar
              .querySelectorAll('[data-filter-type="type"] .filter-btn')
              .forEach((b) => b.classList.remove("active"));
            typeBtn.classList.add("active");
          }
        }

        // 恢复搜索文本
        if (filters.search) {
          const searchInput = filterBar.querySelector(".search-input");
          if (searchInput) {
            searchInput.value = filters.search;
          }
        }
      });

      // 应用恢复的筛选条件
      applyFilters();
    } catch (e) {
      // 忽略错误
    }
  }

  /**
   * 防抖函数
   */
  function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
})();
