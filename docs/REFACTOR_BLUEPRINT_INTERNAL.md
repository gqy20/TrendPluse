# TrendPulse 重构蓝图（内部文档）

> 用途：指导代码重构，不接入前端展示，不作为产品文档对外发布。
>
> 文档日期：2026-03-06
>
> 范围：仅讨论代码组织、模型语义、测试迁移和实施顺序，不讨论功能新增。

---

## 1. 文档目标

这份文档用于回答四个问题：

1. 当前项目为什么会显得“架构重、主路径绕、概念多”。
2. 目标结构应该长什么样。
3. 现有文件应该如何迁移、合并、删除。
4. 应该按什么顺序实施，才能降低风险。

本文档不是一次性“大重写”方案，而是一套分阶段收敛方案。原则是：

- 先压平主路径，再删除包装层。
- 先修正模型语义，再整理命名。
- 先保护行为一致，再做测试瘦身。
- 不为了“更面向对象”而引入新抽象。

---

## 2. 当前问题总结

### 2.1 主流程过重

当前 [`src/trendpluse/pipeline.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/pipeline.py) 同时承担了：

- 依赖装配
- daily 编排
- weekly 编排入口
- 同步/异步双轨实现
- issue/release/report/output 的中间协调

这导致 `pipeline.py` 成为事实上的 God object。

### 2.2 包装层多，但硬边界少

当前存在多层组织：

- `cli/`
- `automation/`
- `workflows/`
- `pipeline.py`

问题不在于目录多，而在于很多层只是转发，没有形成稳定边界。例如：

- `cli -> automation`
- `pipeline -> workflow/service`
- `finalizer -> output_service`

这些层让人要先理解名词，才能理解流程。

### 2.3 数据模型语义不完全诚实

当前 [`src/trendpluse/models/signal.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/models/signal.py) 中的 `DailyReport` 同时包含：

- `engineering_signals`
- `research_signals`
- `commit_signals`
- `release_signals`

但在 [`src/trendpluse/workflows/daily_report_finalizer.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/workflows/daily_report_finalizer.py) 里，`commit_signals` 会被清空，同时统计又继续把 commit 数记入 `stats`。这说明模型字段和最终语义并不一致。

### 2.4 同步/异步两条主链路重复

当前 daily 流程存在两套实现：

- 同步版本
- 异步版本

输入收集、PR 信号分析、报告构建都有两份接近重复的控制流。这类重复在中期会演变成维护漂移。

### 2.5 测试在保护 wiring，而不只是保护行为

当前存在一些超大测试文件，说明很多测试在验证对象接线和调用顺序，而不是纯业务结果。
这种现象通常说明 orchestration 层过胖、边界不够清楚。

---

## 3. 重构目标

重构后的结构应满足下面五条：

1. 新读者只看 2 到 3 个文件，就能理解 daily / weekly 主路径。
2. 报告模型字段与实际产物语义一致，不存在“有字段但不要信”的情况。
3. CLI 只负责参数解析，不再承载大量业务。
4. 业务编排只保留一层，不再出现 `pipeline -> workflow -> service` 多级包装。
5. 测试更多验证输入输出行为，减少对内部调用链的依赖。

---

## 4. 目标目录结构

建议最终收敛为：

```text
src/trendpluse/
  app/
    bootstrap.py
    daily.py
    weekly.py
    discovery.py
    issue_agent.py
  analyzers/
  collectors/
  discovery/
    sources/
      trending.py
      keyword.py
    quality.py
    classify.py
    dedup.py
    highlight.py
    reporter.py
  models/
    report_inputs.py
    signal.py
    ...
  reports/
    builder.py
    publisher.py
    markdown.py
  cli/
    run.py
    run_weekly.py
    discover_projects.py
    send_feishu_notification.py
    send_weekly_feishu.py
    generate_report_index.py
    add_repo.py
    bridge_discovery_to_monitoring.py
    sync_repos_to_docs.py
    normalize_daily_report_stats.py
  config.py
  logger.py
```

设计约束：

- `app/`：只放用例编排。
- `reports/`：只放报告构建和发布。
- `cli/`：只放命令入口。
- `discovery/`：只放项目发现相关逻辑。
- 不再保留 `workflows/`。
- 不再保留 `automation/`。

---

## 5. 模块边界定义

### 5.1 `app/`

职责：

- daily 主路径编排
- weekly 主路径编排
- discovery 主路径编排
- issue agent 任务协调

禁止事项：

- 不定义报告 Markdown 格式
- 不直接写 JSON 文件格式细节
- 不持有过多 helper 状态

### 5.2 `collectors/`

职责：

- 与 GitHub / GraphQL / 外部 API 交互
- 将外部数据转成内部原始材料

禁止事项：

- 不负责报告构建
- 不负责最终展示结构

### 5.3 `analyzers/`

职责：

- 对材料做 LLM 分析或规则分析
- 返回结构化结果

禁止事项：

- 不负责 I/O 落盘
- 不负责 CLI 输出

### 5.4 `reports/`

职责：

- 组装 `DailyReport` / `WeeklyReport`
- 渲染 Markdown
- 发布 Markdown / JSON / 通知

禁止事项：

- 不负责抓 GitHub 数据
- 不负责调度 issue agent

### 5.5 `cli/`

职责：

- 解析参数
- 构建 settings
- 调用 app 层
- 输出退出码

禁止事项：

- 不在 CLI 里编排主业务流程

---

## 6. Daily 流程蓝图

### 6.1 目标主路径

目标 daily 流程应该收敛成下面四步：

1. 收集输入
2. 执行分析
3. 构建报告
4. 发布报告

推荐接口形式：

```python
async def run_daily(services: DailyServices, date: datetime) -> DailyReport:
    inputs = await collect_daily_inputs(services, date)
    analysis = await analyze_daily_inputs(services, inputs, date)
    report = build_daily_report(services, analysis, date)
    await publish_daily_report(services, report, date)
    return report
```

### 6.2 需要迁出的逻辑

从现有 `pipeline.py` 中迁出：

- `_build_*` 依赖创建逻辑 -> `app/bootstrap.py`
- `_collect_daily_inputs_async` -> `app/daily.py`
- `_collect_pr_signals_async` -> `app/daily.py`
- `_build_daily_report_async` -> `reports/builder.py`
- `_get_output_path` -> `reports/publisher.py`

### 6.3 同步版本处理策略

建议内部统一成 async。

处理规则：

- 保留异步主实现
- CLI 使用 `asyncio.run(...)`
- 如有同步 collector，则局部 `asyncio.to_thread`
- 不再维护整套同步主流程

如果出于兼容性暂时不能删同步接口，可以保留一个极薄包装：

```python
def run_daily_sync(...):
    return asyncio.run(run_daily(...))
```

但这个同步接口不能再拥有独立业务实现。

---

## 7. Weekly 流程蓝图

当前 weekly 逻辑可以保留为独立用例，但不需要单独的 `Workflow` 命名。

目标结构：

- `app/weekly.py`：加载日报、聚合周报、发布周报
- `reports/builder.py`：如有需要，提供 `build_weekly_report(...)`
- `reports/publisher.py`：保存 markdown/json

建议保留 weekly 的独立性，因为它是一条真实存在的第二主路径。但它不应再通过 `pipeline -> weekly_workflow` 的方式绕一圈。

---

## 8. 报告层蓝图

### 8.1 新建 `reports/builder.py`

职责：

- 构建 `DailyReport`
- 构建空日报
- 计算 `ReportStats`
- 回填 activity / releases / issue insights

这部分应尽量纯函数化。

推荐函数：

- `build_daily_report(...)`
- `build_empty_daily_report(...)`
- `build_daily_stats(...)`
- `build_weekly_report(...)`

### 8.2 新建 `reports/publisher.py`

职责：

- 保存 markdown
- 保存 json
- 推送飞书

推荐类：

- `ReportPublisher`

说明：

- `publisher` 可以依赖 markdown renderer 和 notifier
- `publisher` 不参与报告内容组装

### 8.3 处理现有 `markdown_reporter.py`

建议迁移为 `reports/markdown.py`。

后续再拆分：

- `DailyMarkdownRenderer`
- `WeeklyMarkdownRenderer`

当前不建议第一阶段就重写渲染逻辑，只需先挪到更合理的边界上。

---

## 9. 模型修正蓝图

### 9.1 `DailyReport` 的语义修正

当前最需要纠正的是 `DailyReport` 的字段设计。

推荐方向：明确区分“原始信号”和“最终展示信号”。

建议字段形态：

```python
class DailyReport(BaseModel):
    date: str
    summary_brief: str
    engineering_signals: list[Signal]
    research_signals: list[Signal]
    raw_pr_signals: list[Signal]
    raw_commit_signals: list[Signal]
    raw_release_signals: list[Signal]
    stats: ReportStats
    activity: ActivityData | None
    releases: ReleasesData | None
    breaking_changes: list[dict] | None
    monitored_repos: list[str] | None
    issue_insights: IssueAgentReport | None
```

如果不想改字段太多，最低要求也应做到：

- 不再出现“字段存在但最终固定置空”
- `stats` 从真实字段推导

### 9.2 中间对象迁入 `models/`

当前 [`src/trendpluse/workflows/daily_pipeline_inputs.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/workflows/daily_pipeline_inputs.py) 本质上是模型，不是 workflow。

建议迁移为：

- `src/trendpluse/models/report_inputs.py`

推荐命名：

- `DailyAnalysisInputs`
- `DailyAnalysisResult`

这样更符合语义，也能减少 workflow 概念污染。

---

## 10. Workflow 层删除方案

### 10.1 删除目标

下面这些文件建议最终删除：

- `src/trendpluse/workflows/release_workflow.py`
- `src/trendpluse/workflows/issue_workflow.py`
- `src/trendpluse/workflows/daily_report_finalizer.py`
- `src/trendpluse/workflows/report_output.py`
- `src/trendpluse/workflows/weekly_report_workflow.py`
- `src/trendpluse/workflows/__init__.py`

### 10.2 对应迁移归宿

| 旧文件 | 新归宿 |
|---|---|
| `release_workflow.py` | `app/daily.py` 或 `app/release_processor.py` |
| `issue_workflow.py` | `app/daily.py` + `app/issue_agent.py` |
| `daily_report_finalizer.py` | `reports/builder.py` |
| `report_output.py` | `reports/publisher.py` |
| `weekly_report_workflow.py` | `app/weekly.py` |

### 10.3 判断原则

只有当一个模块满足下面任一条件，才值得独立存在：

- 有独立生命周期
- 有独立策略
- 有明确复用价值
- 能显著减少上层复杂度

如果只是“把 3 到 5 个调用包成一个类再起个名字”，那通常不值得保留。

---

## 11. CLI 与 automation 收敛方案

### 11.1 当前问题

当前存在大量模式：

- CLI 解析参数
- automation 执行主体
- utils 提供 I/O 或帮助函数

这会造成一件事要记三层位置。

### 11.2 目标方案

保留：

- `cli/`：命令行入口

删除：

- `automation/`

迁移目标：

- automation 中的主体函数迁入 `app/` 或 `reports/`

### 11.3 文件级迁移建议

| 旧文件 | 新文件 |
|---|---|
| `automation/generate_report_index.py` | `app/generate_report_index.py` |
| `automation/add_repo.py` | `app/add_repo.py` |
| `automation/bridge_discovery_to_monitoring.py` | `app/bridge_discovery.py` |
| `automation/sync_repos_to_docs.py` | `app/sync_repos_to_docs.py` |
| `automation/normalize_daily_report_stats.py` | `app/normalize_report_stats.py` |

### 11.4 CLI 的最终职责

CLI 文件应只保留：

- argparse
- settings 创建
- 调用 `app.*`
- `SystemExit` / 日志 / 控制台提示

禁止在 CLI 文件中直接写完整业务流程。

---

## 12. LLM 分析器重构方案

### 12.1 当前问题

[`src/trendpluse/analyzers/base.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/analyzers/base.py) 过于“大而全”，同时负责：

- client 创建
- instructor / non-instructor 模式
- sync / async 双客户端
- retry
- 响应文本提取
- JSON 清洗
- signal 验证

这种基类的问题不是不能用，而是会变成所有 analyzer 的复杂度中心。

### 12.2 目标方案

从继承转向组合，拆出下面几个小组件：

- `utils/llm_client_factory.py`
- `utils/llm_retry.py`
- `utils/llm_response_parser.py`
- `utils/signal_validation.py`

然后 analyzer 只组合自己需要的能力。

### 12.3 实施策略

第一阶段：

- 保留 `BaseLLMAnalyzer`
- 把 retry 抽出去
- 把 client 创建抽出去

第二阶段：

- 子类逐步不依赖基类通用逻辑
- 基类瘦到只剩很少内容

第三阶段：

- 如无必要，删除基类

---

## 13. Release 子系统重组方案

当前 release 相关逻辑分散在多个文件中：

- `release_analyzer.py`
- `release_summarizer.py`
- `breaking_changes_detector.py`
- `release_material_builder.py`
- `release_workflow.py`

建议收敛成明确子集：

```text
app/
  release_processor.py
analyzers/
  release_summary.py
  release_signals.py
  release_breaking_changes.py
collectors/
  release_material_builder.py
```

目标是让“release 的完整处理逻辑”可以被一眼定位，而不是散落在 workflow、analyzer、builder 之间。

---

## 14. Issue Agent 子系统重组方案

### 14.1 当前问题

当前 issue agent 逻辑被分散在：

- `collectors/issues.py`
- `workflows/issue_workflow.py`
- `workflows/issue_agent_runner.py`
- `utils/issue_io.py`
- `utils/issue_agent_io.py`

### 14.2 目标方案

建议改成：

```text
app/
  issue_agent.py
collectors/
  issues.py
utils/
  issue_io.py
  issue_agent_io.py
```

其中：

- `issues.py`：抓取
- `issue_io.py`：落盘
- `issue_agent.py`：决定是否执行分析、如何读取结果
- `issue_agent_runner.py`：迁入 `app/issue_agent.py` 或 `issue_agent/runner.py`

### 14.3 判断原则

issue agent 是一个附加能力，不应该把 daily 主路径扭成一层新框架。
它更适合作为 daily 用例中的一个可选分支，而不是单独 workflow。

---

## 15. Discovery 子系统重构方案

### 15.1 当前问题

discovery 现在既像脚本，又像半框架：

- 有 `BaseDiscoverer`
- 也有很重的 `cli/discover_projects.py`

这两者混在一起，说明边界没找准。

### 15.2 目标结构

建议改成：

```text
discovery/
  sources/
    trending.py
    keyword.py
  quality.py
  classify.py
  dedup.py
  highlight.py
  reporter.py
app/
  discovery.py
```

### 15.3 删除项

建议删除：

- `src/trendpluse/discovery/base.py`

原因：

- `BaseDiscoverer` 抽象太薄
- 没有形成稳定可替换协议
- 反而引入了“必须继承某个类”的框架味道

### 15.4 CLI 调整

将 [`src/trendpluse/cli/discover_projects.py`](/home/qy113/workspace/project/2603/TrendPluse/src/trendpluse/cli/discover_projects.py) 中的大量业务逻辑迁入：

- `src/trendpluse/app/discovery.py`

CLI 保留为薄壳。

---

## 16. 配置层方案

### 16.1 当前问题

当前同时存在：

- `Settings()`
- `get_settings()`

这会造成两种配置获取方式并存。

### 16.2 目标方案

推荐原则：

- 入口层创建一次 `Settings`
- 通过依赖传递给 app / service / helper
- 业务层不再主动获取全局单例

### 16.3 实施策略

第一阶段：

- 保留 `get_settings()` 兼容
- 但新增代码禁止调用

第二阶段：

- discovery / CLI 全部改成显式传参
- 删除 `get_settings()`

---

## 17. 测试迁移蓝图

### 17.1 测试目标

测试不应主要保护“对象接线方式”，而应主要保护：

- 输入输出语义
- 容错行为
- 关键副作用

### 17.2 目标结构

建议调整为：

```text
tests/
  unit/
    app/
    reports/
    analyzers/
    collectors/
    models/
    discovery/
  integration/
```

### 17.3 大文件拆分建议

| 当前文件 | 目标文件 |
|---|---|
| `test_pipeline.py` | `test_app_daily.py` / `test_app_weekly.py` |
| `test_pipeline_empty_report_summary.py` | `test_reports_builder.py` |
| `test_release_workflow_service.py` | `test_release_processor.py` |
| `test_issue_workflow_service.py` | `test_issue_agent_flow.py` |
| `test_report_output_service.py` | `test_report_publisher.py` |

### 17.4 测试策略调整

减少：

- mock 太多的 orchestration 测试
- 纯验证内部调用次数的测试

增加：

- builder 的纯函数测试
- publisher 的副作用测试
- app 主路径的少量集成测试

---

## 18. 分阶段实施计划

### 阶段 1：建立新骨架，不改行为

目标：

- 先把结构搭起来
- 旧实现先平移，不追求立刻优雅到底

任务：

- 新建 `app/bootstrap.py`
- 新建 `app/daily.py`
- 新建 `app/weekly.py`
- 新建 `reports/builder.py`
- 新建 `reports/publisher.py`
- `pipeline.py` 降级为 facade

完成标准：

- 所有现有命令仍可运行
- 测试基本不变或小幅迁移

### 阶段 2：统一 daily async 主路径

任务：

- 删掉同步 daily 实现的独立逻辑
- 统一使用 async 主流程
- CLI 用 `asyncio.run()`

完成标准：

- daily 主链路只保留一套真实实现

### 阶段 3：修正报告模型语义

任务：

- 修改 `DailyReport`
- 修改 builder / markdown / json 输出
- 修改相关测试

完成标准：

- 不再存在“字段存在但固定清空”的语义问题

### 阶段 4：删除 workflow 层

任务：

- 删除 `workflows/`
- 完成对应迁移

完成标准：

- 不再使用 `Workflow` / `Service` 作为主业务包装层

### 阶段 5：删除 automation 层

任务：

- 迁移 `automation/*` 到 `app/*`
- CLI 直接调用 app 层

完成标准：

- `automation/` 目录删除

### 阶段 6：拆解 LLM 基类与测试瘦身

任务：

- 拆 `BaseLLMAnalyzer`
- 重构超大测试文件

完成标准：

- analyzer 依赖更轻
- 测试更接近行为而非 wiring

---

## 19. 文件级迁移表

### 19.1 主路径相关

| 当前文件 | 动作 | 目标 |
|---|---|---|
| `src/trendpluse/pipeline.py` | 瘦身，最终删除或仅做 facade | `app/daily.py` / `app/weekly.py` |
| `src/trendpluse/workflows/daily_pipeline_inputs.py` | 迁移 | `models/report_inputs.py` |
| `src/trendpluse/workflows/daily_report_finalizer.py` | 删除 | `reports/builder.py` |
| `src/trendpluse/workflows/report_output.py` | 删除 | `reports/publisher.py` |
| `src/trendpluse/workflows/weekly_report_workflow.py` | 删除 | `app/weekly.py` |

### 19.2 release / issue

| 当前文件 | 动作 | 目标 |
|---|---|---|
| `src/trendpluse/workflows/release_workflow.py` | 删除 | `app/release_processor.py` |
| `src/trendpluse/workflows/issue_workflow.py` | 删除 | `app/issue_agent.py` |
| `src/trendpluse/workflows/issue_agent_runner.py` | 迁移 | `app/issue_agent.py` 或 `issue_agent/runner.py` |

### 19.3 文档和输出

| 当前文件 | 动作 | 目标 |
|---|---|---|
| `src/trendpluse/markdown_reporter.py` | 迁移 | `reports/markdown.py` |

### 19.4 CLI / automation

| 当前文件 | 动作 | 目标 |
|---|---|---|
| `src/trendpluse/automation/generate_report_index.py` | 迁移 | `app/generate_report_index.py` |
| `src/trendpluse/automation/add_repo.py` | 迁移 | `app/add_repo.py` |
| `src/trendpluse/automation/bridge_discovery_to_monitoring.py` | 迁移 | `app/bridge_discovery.py` |
| `src/trendpluse/automation/sync_repos_to_docs.py` | 迁移 | `app/sync_repos_to_docs.py` |
| `src/trendpluse/automation/normalize_daily_report_stats.py` | 迁移 | `app/normalize_report_stats.py` |

### 19.5 discovery

| 当前文件 | 动作 | 目标 |
|---|---|---|
| `src/trendpluse/discovery/base.py` | 删除 | 无 |
| `src/trendpluse/discovery/trending.py` | 迁移 | `discovery/sources/trending.py` |
| `src/trendpluse/discovery/keyword_searcher.py` | 迁移 | `discovery/sources/keyword.py` |
| `src/trendpluse/discovery/evaluator.py` | 重命名迁移 | `discovery/quality.py` |
| `src/trendpluse/discovery/classifier.py` | 重命名迁移 | `discovery/classify.py` |
| `src/trendpluse/discovery/deduplicator.py` | 重命名迁移 | `discovery/dedup.py` |
| `src/trendpluse/discovery/highlight_analyzer.py` | 重命名迁移 | `discovery/highlight.py` |

---

## 20. 风险与控制策略

### 20.1 最大风险

最大的风险不是“代码搬不动”，而是：

- 报告 JSON 结构变化影响历史报告兼容
- 测试大量依赖旧 wiring
- CLI 行为在重构中悄悄漂移

### 20.2 控制策略

建议每阶段都做下面三件事：

1. 保留旧入口的兼容壳。
2. 对 daily / weekly 产出做 JSON snapshot 对比。
3. 在重构阶段优先新增集成测试，而不是先删测试。

### 20.3 兼容策略

对于 `DailyReport` 的模型变更：

- 先支持旧字段反序列化
- 再迁移生成逻辑
- 最后再删除旧字段兼容

不要一步到位，否则历史报告读取很容易断。

---

## 21. 验收标准

如果重构完成，至少应达到下面结果：

- `pipeline.py` 不再是系统中心，或已经删除。
- `workflows/` 目录删除。
- `automation/` 目录删除。
- daily 主流程只保留一套 async 实现。
- `DailyReport` 字段语义和最终 JSON 一致。
- CLI 文件明显变薄。
- 超大测试文件被拆分。
- 新读者能在 `app/daily.py`、`reports/builder.py`、`reports/publisher.py` 中理解主要流程。

---

## 22. 推荐执行顺序

实际落地时，建议严格按下面顺序：

1. 建 `app/` 和 `reports/` 新骨架。
2. 把 `pipeline.py` 的装配迁入 `app/bootstrap.py`。
3. 统一 daily async 主流程。
4. 把 finalizer/output 迁到 `reports/`。
5. 修正 `DailyReport`。
6. 删除 `workflows/`。
7. 收敛 `automation/`。
8. 重组 discovery。
9. 拆 `BaseLLMAnalyzer`。
10. 做测试瘦身。

这个顺序的目的是：

- 先控制主复杂度
- 再清理概念债
- 最后处理风格债

---

## 23. 结论

这次重构不应追求“架构更高级”，而应追求三件事：

- 主路径更短
- 模型更诚实
- 目录更少解释成本

如果只保留一句总原则，就是：

**把现在的多层包装系统，收敛成 `app 编排 + collectors/analyzers 执行 + reports 输出 + cli 入口` 的四段式结构。**

这比继续增加 `workflow/service/base` 更接近一个长期可维护的形态。
