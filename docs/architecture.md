# 架构说明

## 总体原则

当前代码结构遵循“入口、编排、采集、分析、模型、通知”分层，避免把命令行逻辑和核心业务流程混在一起。

## 目录职责

### `cli/`

- 只负责参数解析、环境加载、调用应用层
- 对外暴露 `pyproject.toml` 中的 CLI entrypoints

### `app/`

- 承担 daily / weekly / discovery / repo 管理等应用编排
- 放置运行时辅助、报告收尾、飞书通知辅助等主流程逻辑

### `collectors/`

- 拉取 GitHub 数据
- 构建 `AnalysisMaterial`
- 提供 issue snapshot / PR reader / release reader 等输入边界

### `analyzers/`

- LLM 结构化抽取
- 信号去重、聚合、release 总结、breaking change 检测
- issue agent runner、weekly aggregator 等分析侧能力

### `models/`

- `Signal`
- `DailyReport`
- `WeeklyReport`
- `IssueAgentBatchResult`
- `ProjectHighlight`

全部放在统一的结构化模型层，避免模型反向依赖业务实现。

### `reports/`

- 报告构建、Markdown 渲染、发布与持久化
- 区分“生成报告对象”和“输出报告产物”

### `notifiers/`

- 飞书通知发送器与消息格式化

### `discovery/`

- 项目发现子系统的采集、评估、去重、分类与报告能力

## 当前主链路

```text
CLI -> app -> collectors / analyzers / reports / notifiers
```

## 当前已完成的结构收敛

- `automation/` 已收敛到 `app/`
- `workflows/` 已删除
- `pipeline.py` 已迁移到 `app/pipeline.py`
- `readers/` 已并入 `collectors/`
- `IssueAgentRunner` 已收敛到 `analyzers/issue_agent_runner.py`
- 飞书 CLI 公共逻辑已抽到 `cli/feishu_common.py` 与 `cli/report_json_common.py`

## 后续适合继续演进的方向

1. 继续减少 CLI 样板重复
2. 为 Markdown / Feishu 输出建立共享展示适配层
3. 继续清理少量历史兼容逻辑
