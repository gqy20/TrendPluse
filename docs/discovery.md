# 项目发现历史

自动发现的 GitHub 热门项目报告，每周更新。

## 最新报告

### [2026-03-05](discovery-reports/discovery-2026-03-05.md)

**发现概览**:<br/>
- 总发现数: 200<br/>
- 通过质量评估: 200<br/>
- 高优先级: 135<br/>
- 去重移除: 33<br/>
- 已在监控: 21<br/>

## 发现流程

1. Trending 抓取
2. 关键词搜索
3. 去重与质量评估
4. 分类排序
5. 产出 discovery 报告与 actionable candidates

## 运行方式

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

## 输出位置

```text
reports/discovery/
docs/discovery-reports/
```

## 自动运行

项目发现由 GitHub Actions 工作流 [discover-projects.yml](https://github.com/gqy20/TrendPluse/actions/workflows/discover-projects.yml) 定时执行。

## 历史报告

| 日期 | 总发现 | 高优先级 | 报告 |
|------|--------|----------|------|
| 2026-03-05 | 200 | 135 | [查看](discovery-reports/discovery-2026-03-05.md) |
| 2026-03-04 | 200 | 135 | [查看](discovery-reports/discovery-2026-03-04.md) |
| 2026-03-02 | 200 | 140 | [查看](discovery-reports/discovery-2026-03-02.md) |
| 2026-03-01 | 200 | 138 | [查看](discovery-reports/discovery-2026-03-01.md) |
| 2026-02-28 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-28.md) |
| 2026-02-27 | 200 | 132 | [查看](discovery-reports/discovery-2026-02-27.md) |
| 2026-02-26 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-26.md) |
| 2026-02-25 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-25.md) |
| 2026-02-24 | 200 | 135 | [查看](discovery-reports/discovery-2026-02-24.md) |
| 2026-02-23 | 200 | 136 | [查看](discovery-reports/discovery-2026-02-23.md) |
