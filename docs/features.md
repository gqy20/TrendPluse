# 功能概述

TrendPulse 是一个围绕 GitHub 活动、LLM 分析和文档发布构建的自动化趋势分析系统。

## 核心能力

### 每日趋势分析

- 采集 GitHub PR、Release、Commit、Issue
- 将原始数据统一转换为 `AnalysisMaterial`
- 用 LLM 提取趋势信号、Release 总结和 Issue 洞察
- 生成 Markdown / JSON 日报
- 可选发送飞书通知

### 周报聚合

- 从近 7 天日报聚合高影响趋势
- 生成 weekly Markdown / JSON
- 支持独立 CLI 和定时工作流

### 项目发现

- 从 Trending 与关键词搜索发现候选项目
- 进行去重、评估、分类、推荐
- 输出 discovery 报告和候选结果

### Issue Agent 洞察

- 对 issue JSONL 执行三轮分析
- 提取 `top_pain_points`、`quality_score`、`quality_status`
- 融入 daily 报告与后续排查流程

## 当前架构分层

```text
cli/           命令入口与参数解析
automation/    可复用批处理实现
collectors/    外部数据采集与 AnalysisMaterial 构建
analyzers/     LLM 分析、聚合、去重
workflows/     日报/周报/issue/report 输出编排
models/        结构化数据模型
notifiers/     飞书通知与格式化
discovery/     独立的项目发现子系统
pipeline.py    主应用编排入口
```

## 关键工作流

### Daily

1. `collectors` 拉取活动、PR、release、issue
2. `analyzers` 提取趋势信号与摘要
3. `workflows.daily_report_finalizer` 生成日报对象
4. `workflows.report_output` 持久化产物
5. `notifiers` 可选发送飞书

### Weekly

1. `workflows.weekly_report_workflow` 读取 daily JSON
2. `WeeklyAggregator` 聚合高价值信号和活跃度
3. `workflows.report_output` 统一输出 weekly 产物

### Discovery

1. Trending / 搜索发现
2. 质量评估与去重
3. 高亮分析与报告输出
4. 可桥接到监控仓库列表

## 产物

```text
reports/daily/
reports/weekly/
reports/discovery/
docs/reports/
docs/discovery-reports/
```

## 自动化工作流

- `ci.yml`: Ruff、mypy、pytest、打包验证
- `run-daily.yml`: 每日分析
- `run-weekly.yml`: 周报聚合
- `discover-projects.yml`: 项目发现
- `issue-analyzer.yml`: Issue / Comment 触发分析
- `send-feishu.yml`: 飞书补发
- `deploy-pages.yml`: MkDocs 部署
