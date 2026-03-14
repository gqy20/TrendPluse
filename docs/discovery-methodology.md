# 项目发现方法说明

这个页面只解释发现逻辑，不承担结果展示。

## 发现来源

项目通过两条主链路发现候选仓库：

1. **GitHub Trending**：抓取不同语言的 Trending 页面。
2. **关键词搜索**：围绕 AI/LLM/Agent 相关关键词搜索候选项目。

## 质量评估

每个候选项目会经过统一评分：

- **Stars 指标**：受欢迎程度，20 分。
- **活跃度指标**：最近提交时间，30 分。
- **社区指标**：Forks 和 Watchers，20 分。
- **代码质量**：License 与 Open Issues 比例，20 分。
- **相关性**：与 AI/LLM 主题匹配度，15 分。

总质量分为 0-100，当前以 **60 分** 作为推荐阈值。

## 推荐优先级

- **高优先级**：质量分数 ≥ 85
- **中优先级**：70 ≤ 质量分数 < 85
- **低优先级**：60 ≤ 质量分数 < 70

## 运行方式

```bash
uv run trendpluse-discover-projects

uv run trendpluse-discover-projects \
  --days 7 \
  --min-quality 60.0 \
  --languages python typescript go \
  --keywords "AI agent" "LLM" "Claude" "RAG"
```

## 自动运行

项目发现通过 GitHub Actions 每周一 UTC 00:10 自动运行，对应北京时间 08:10。

工作流入口：
[discover-projects.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-projects.yml)
