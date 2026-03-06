# 架构说明

## 总体原则

当前代码结构遵循“入口、编排、采集、分析、模型、通知”分层，避免把命令行逻辑和核心业务流程混在一起。

## 目录职责

### `cli/`

- 只负责参数解析、环境加载、调用应用层
- 对外暴露 `pyproject.toml` 中的 CLI entrypoints

### `automation/`

- 只保留可复用批处理实现
- 不再承担最终命令入口职责

### `collectors/`

- 拉取 GitHub 数据
- 构建 `AnalysisMaterial`
- 提供 issue snapshot / PR reader / release reader 等输入边界

### `analyzers/`

- LLM 结构化抽取
- 信号去重、聚合、release 总结、breaking change 检测

### `workflows/`

- `daily_report_finalizer.py`
- `weekly_report_workflow.py`
- `issue_workflow.py`
- `issue_agent_runner.py`
- `report_output.py`

这一层负责串起多个 collector / analyzer，不直接承担读写参数解析。

### `models/`

- `Signal`
- `DailyReport`
- `WeeklyReport`
- `IssueAgentBatchResult`
- `ProjectHighlight`

全部放在统一的结构化模型层，避免模型反向依赖业务实现。

### `pipeline.py`

`pipeline.py` 仍放在包根，是因为它不是某一个 workflow，而是**调用多个 workflow 的总编排入口**。它不应放到 `cli/`，也暂时不需要单独再造 `application/` 目录。

## 当前主链路

```text
CLI -> pipeline -> collectors -> analyzers -> workflows -> notifiers / report output
```

## 当前已完成的结构收敛

- `services/` 已重命名并收敛到 `workflows/`
- `readers/` 已并入 `collectors/`
- `reporters/` 已平铺到根模块
- `agents/` 已拆分为 `workflows/issue_agent_runner.py` + `models/issue_agent.py`
- 飞书 CLI 公共逻辑已抽到 `cli/feishu_common.py` 与 `cli/report_json_common.py`

## 后续适合继续演进的方向

1. 继续减少 CLI 样板重复
2. 为 Markdown / Feishu 输出建立共享展示适配层
3. 继续清理少量历史兼容逻辑
