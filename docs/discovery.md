# 项目发现历史

自动发现的 GitHub 热门项目报告，每周一更新。

## 最新报告

### [2026-02-24](discovery-reports/discovery-2026-02-24.md)

**发现概览**:<br/>
- 总发现数: 200<br/>
- 通过质量评估: 200<br/>
- 高优先级: 135<br/>
- 去重移除: 30<br/>
- 已在监控: 20<br/>

**高优先级推荐 Top 5**:<br/>


## 历史报告

| 日期 | 总发现 | 高优先级 | 报告 |
|------|--------|----------|------|
| 2026-02-24 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-24.md) |
| 2026-02-23 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-23.md) |
| 2026-02-22 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-22.md) |
| 2026-02-21 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-21.md) |
| 2026-02-20 | 200 | 140 | [查看](discovery-reports/discovery-2026-02-20.md) |
| 2026-02-19 | 200 | 140 | [查看](discovery-reports/discovery-2026-02-19.md) |
| 2026-02-18 | 200 | 138 | [查看](discovery-reports/discovery-2026-02-18.md) |
| 2026-02-17 | 200 | 140 | [查看](discovery-reports/discovery-2026-02-17.md) |
| 2026-02-16 | 200 | 138 | [查看](discovery-reports/discovery-2026-02-16.md) |
| 2026-02-15 | 200 | 140 | [查看](discovery-reports/discovery-2026-02-15.md) |

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
uv run python scripts/discover_projects.py

# 自定义参数
uv run python scripts/discover_projects.py \
  --days 7 \
  --min-quality 60.0 \
  --languages python typescript go \
  --keywords "AI agent" "LLM" "Claude" "RAG"
```

### 自动运行

项目发现通过 GitHub Actions 每周一 UTC 00:10
(北京时间 08:10) 自动运行。

查看工作流: [discover-repos.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-repos.yml)
