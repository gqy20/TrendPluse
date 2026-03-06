# 项目发现历史

自动发现 GitHub 热门项目，并按质量、相关性与可跟踪性进行筛选与归档。

## 页面说明

- 先看“本期概览”，判断本轮发现规模与推荐密度。
- 再看“高优先级推荐 Top 5”，快速锁定值得纳入监控的项目。
- 最后用“历史报告”表格回看不同日期的发现结果。

## 本期概览

### [2026-03-06](discovery-reports/discovery-2026-03-06.md)

| 指标 | 数值 | 指标 | 数值 |
|------|------|------|------|
| 总发现数 | 200 | 通过质量评估 | 200 |
| 高优先级 | 140 | 去重移除 | 40 |
| 已在监控 | 20 | 完整报告 | [查看](discovery-reports/discovery-2026-03-06.md) |

### 分类分布 Top 5

| 分类 | 数量 |
|------|------|
| 🤖 AI Agents | 30 |
| 🔍 RAG/检索 | 18 |
| 💬 LLM 界面 | 22 |
| 🧠 机器学习框架 | 11 |
| 🛠️ 开发工具 | 18 |

## 高优先级推荐 Top 5

| 项目 | Stars |
|------|-------|
| 暂无 | - |


## 历史报告

| 日期 | 总发现 | 高优先级 | 报告 |
|------|--------|----------|------|
| 2026-03-06 | 200 | 140 | [查看](discovery-reports/discovery-2026-03-06.md) |
| 2026-03-05 | 200 | 135 | [查看](discovery-reports/discovery-2026-03-05.md) |
| 2026-03-04 | 200 | 135 | [查看](discovery-reports/discovery-2026-03-04.md) |
| 2026-03-02 | 200 | 140 | [查看](discovery-reports/discovery-2026-03-02.md) |
| 2026-03-01 | 200 | 138 | [查看](discovery-reports/discovery-2026-03-01.md) |
| 2026-02-28 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-28.md) |
| 2026-02-27 | 200 | 132 | [查看](discovery-reports/discovery-2026-02-27.md) |
| 2026-02-26 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-26.md) |
| 2026-02-25 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-25.md) |
| 2026-02-24 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-24.md) |

## 关于发现功能

### 发现来源

项目通过以下方式自动发现：

1. **GitHub Trending** - 爬取各语言的 Trending 页面
2. **关键词搜索** - 基于 AI 相关关键词搜索

### 质量评估

每个发现的项目会经过多维度质量评估：

- **Stars 指标** (20分): 项目受欢迎程度
- **活跃度指标** (30分): 最近提交时间
- **社区指标** (20分): Forks 和 Watchers 数量
- **代码质量** (20分): License 和 Open Issues 比例
- **相关性** (15分): 与 AI/LLM 主题的相关度

**总质量分**: 0-100 分，≥60 分为推荐

### 推荐优先级

- **高优先级** (high): 质量分数 ≥ 85
- **中优先级** (medium): 70 ≤ 质量分数 < 85
- **低优先级** (low): 60 ≤ 质量分数 < 70

### 运行方式

```bash
# 本地运行发现
uv run trendpluse-discover-projects

# 自定义参数
uv run trendpluse-discover-projects \
  --days 7 \
  --min-quality 60.0 \
  --languages python typescript go \
  --keywords "AI agent" "LLM" "Claude" "RAG"
```

### 自动运行

项目发现通过 GitHub Actions 每周一 UTC 00:10
(北京时间 08:10) 自动运行。

查看工作流: [discover-projects.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-projects.yml)
