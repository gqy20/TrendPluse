# TrendPulse 优化路线图

> 本文档整理 2026-09-11 一轮排查（网关切换 + 配置治理 + 采集复跑）中发现的全部待优化项。
> 每项均标注**现象 / 根因 / 影响 / 建议方案 / 涉及文件**，可直接作为独立任务认领。
>
> 优先级定义：
> - **P0** 用户可见的正确性缺陷，应尽快修
> - **P1** 可观测性与成本治理缺失，影响决策质量
> - **P2** 工程卫生问题，不影响功能但持续制造噪音
> - **P3** 待决策项或收益/风险需权衡的改动

---

## 已完成（本轮，已推送 origin/main）

| Commit | 内容 |
|---|---|
| `5fe15b3` | `.env` 优先级高于进程环境变量：新增 `utils/env.py` 封装 `load_env(override=True)`，替换三处裸 `load_dotenv()` |
| `e0af25a` | commit 分析 Agent 预算可配置：`COMMIT_AGENT_MAX_BUDGET_USD`（原硬编码 `$3.0`，535 commits 分 3 批时爆预算丢 1 批） |
| `8e3c5a9` | 周报聚合器改用配置模型（原硬编码 `glm-4.7`，换网关后 `503 model_not_found`）+ 修复异步路径 `await` 同步 client |
| `835e201` | 测试隔离：`.env` 泄漏进配置断言 + 会话级产物守卫（`reports/`、`data/` 被写即失败） |
| `0c71d02` | `_save_json` 落盘补末尾换行（`report-*.json` 反复产生脏 diff 的根因） |
| `62541e7` | 删除测试误提交的两个假日报 JSON |
| `d0ec899` | 移除失效仓库 `openclaw/skills`（404 且不保留 301） |
| `639f8bb` | 忽略 `data/` 运行态缓存 |
| `a70fc81` | `load_daily_history_index` 返回类型标注（消除 `no-any-return`） |

## 已完成（第二轮实施，2026-09-11）

| Commit | 内容 |
|---|---|
| `e541639` | prompt 全量外置 YAML（golden test 字节级锁定）+ research 信号聚合修复（判定标准 + `_resolve_sources_from_ids` 覆盖 research） |
| `9d45f5a` | **P0-2** 悬空 ID 剔除（定性为 LLM 幻觉，`pr-418` 类脏引用不再落盘）；**P0-1** 前端 release 卡片 `[object Object]`；**P2-3** 前端 5 处 `z.unknown()` 换真实 zod schema + 组件类型推导；附带发现并修复 `top_pain_points` 对象误渲染 |
| `ed7f9de` | **P1-1/2/3** 全流程 LLM usage 记录（6 个直连分析器 + commit 分析 + daily_llm_usage 汇总 + 历史索引 token 字段 + budget 软限制）；model=null 从 `ResultMessage.model_usage` 源头修复；名义成本标注 |
| `ff6943b` | **P1-4/P3-2.2** repos.json 8 个转移仓库更新（gh api 确认，省 301 跳转）；retry 补 SSLError/TransportError；**P3-2.1 待决策**：`openclaw/agent-skills` 是否纳入监控 |
| `f4974e5` | **P2-1** actionable/bridge-result 落盘收敛到 `data/discovery/` + git rm 191 个历史中间产物 + JSON/MD 配对校验脚本接入 smoke CI；**P2-2** AGENTS.md 过期陈述修正 |

当前基线：`755 passed / 4 skipped`，ruff、ruff format、mypy（97 文件）、astro check/build 全绿。

---

## P0-1 前端 release 卡片全部显示 `[object Object]`

**现象**
网页「🎯 发布动态」区块，每张卡片的摘要位置渲染成字面量 `[object Object]`。今日报告 30 条 release **全部命中**（30/30），不是个别数据问题。

**根因**
`ai_summary` 在后端是嵌套对象，前端按字符串渲染：

- 数据形状由 `src/trendpluse/models/signal.py:53` 的 `ReleaseSummary` 定义：
  `change_type`（Literal）、`key_changes`（list[str]）、`summary_cn`（str）、`impact_level`（int 1-5）
- `web/src/components/report/ReleaseList.astro:10` 却声明 `ai_summary?: string`
- `ReleaseList.astro:41-42` 渲染 `{r.ai_summary || r.summary}` —— 对象是 truthy，永远压过 `summary`，
  进文本插值后被 JS 隐式 `String(obj)` → `[object Object]`

**为什么构建期没拦住**

| 防线 | 实际情况 |
|---|---|
| 组件内 TS interface | 手写 `ai_summary?: string`，与真实数据不符 |
| `web/src/content.config.ts:53` | `releases: z.record(z.string(), z.unknown()).nullish()` —— `z.unknown()` 等于不校验 |
| 运行时 | 无兜底 |

**对照证据**：`src/trendpluse/notifiers/feishu_formatter.py:435-458` 消费同一字段但写法正确
（按对象访问 `.change_type`、遍历 `.key_changes`、取 `.summary_cn`）。所以飞书卡片正常，只有网页坏 ——
属前端单方面未跟上后端模型，数据本身没错。

**建议方案**
1. `ReleaseList.astro`：interface 改为对象类型；渲染 `r.ai_summary?.summary_cn || r.summary`；
   `key_changes` 渲染为列表，`change_type` / `impact_level` 做徽章（可直接复用飞书侧的 emoji 映射逻辑）。
2. `content.config.ts`：为 releases 补真实 zod schema，替掉 `z.unknown()`，让 `astro check` 与构建期能拦住类型不符。

**涉及文件**：`web/src/components/report/ReleaseList.astro`、`web/src/content.config.ts`
**参考实现**：`src/trendpluse/notifiers/feishu_formatter.py:435-458`

---

## P0-2 聚合信号引用不存在的信号 ID

**现象**
两次独立采集运行均出现同一告警：

```
WARNING  聚合信号引用了不存在的 ID: pr-418    trend_analyzer.py:703
```

> 注：日志里的 `703` 是采集运行时（rebase 前的旧基线 `c1af179`，该文件 762 行）的行号；
> 上游 157 个提交重构过此文件（现为 675 行），**当前 HEAD 对应行号为 616**。

**影响**
LLM 在趋势聚合时产出了指向不存在信号的 `signal_ids`。当前代码只告警不阻断，
意味着前端「核心趋势」卡片可能出现**点击无对应信号 / 关联数量对不上**的情况，
且趋势的 `signal_ids` 计数与真实证据链脱节。

**待查方向**
- `pr-418` 是 LLM 幻觉，还是去重阶段（`Deduplication done, signals=20`）把该 ID 合并/丢弃后未同步给聚合器？
- 聚合器拿到的候选 ID 列表与最终落盘的信号集合是否同一份快照？

**建议方案**
先定位是「输入不一致」还是「模型幻觉」：
- 若输入不一致 → 修正传给聚合器的 ID 集合，从源头消除；
- 若属幻觉 → 保留告警，但在报告落盘前**剔除悬空 ID**，避免脏引用进前端与历史索引。

**涉及文件**：`src/trendpluse/analyzers/trend_analyzer.py:616`（旧基线为 `:703`）及其调用方

---

## P1-1 Token 消耗记录覆盖不全（最大缺口）

**现状**
项目**有**记录能力，集中在 `src/trendpluse/models/agent_usage.py`：

| 模型 | 字段 |
|---|---|
| `AgentUsageBreakdown` | input/output/cache_creation/cache_read/total tokens、tool_uses、duration_ms |
| `AgentRunMetrics` | model、session_id、num_turns、duration_ms、duration_api_ms、total_cost_usd、usage、raw_usage |
| `AgentMetricsSummary` | run_count、models、各项 total、聚合 usage |

落盘位置：日报 JSON 的 `daily_summary_agent_run_metrics`、`agent_metrics_summary`
（`models/signal.py:231,235`）；Issue 侧 `agent_run_metrics`、`agent_metrics_summary`
（`models/issue_agent.py:103,145`）。

今日实测数据（仅日报总结 agent 一项）：

```
num_turns 19 | duration 245.4s（API 149.5s）
input 519,736 + output 4,367 = total 524,103 tokens
cache 全 0 | tool_uses 0 | total_cost_usd 2.707855
```

历史累计：191 个日报 JSON 中仅 **52 个**含指标，合计 `25,641,344 tokens / $89.64`（且只覆盖一个 agent）。

**缺口清单**

1. **`src/trendpluse/analyzers/base.py` 完全不记录**
   直连 Anthropic SDK 的 5 个分析器（`TrendAnalyzer`、`ReleaseAnalyzer`、`ReleaseSummarizer`、
   `BreakingChangesDetector`、`IssueGlobalSummarizer`）里 `usage`/`tokens`/`cost` 零命中；
   `_extract_text_from_response` 只取文本就丢弃响应。而这些正是 PR 分析、release 分析、趋势聚合的主力消耗。

2. **`src/trendpluse/analyzers/structured_query.py` 拿到了却扔掉**
   `SDKCommitAnalyzer` 走这条路径，`ResultMessage` 本身携带 usage 与 total_cost_usd，
   但代码只取了 `structured_output` 和 `session_id`（`structured_query.py:96-115`，
   第 115 行 `return QueryResult(output=..., session_id=...)` 即丢弃点）。
   讽刺的是 commit 分析恰恰是单次最贵的一环（今日 461.83s、预算上限 $20），**一分钱消耗都没留痕**。

3. **`daily_token_budget` 是死配置**
   `src/trendpluse/config.py:159` 定义（默认 50M，`.env` 里写的 100000），
   但全项目 grep 下来**没有任何地方读取它** —— 不限流、不告警、不统计。

4. **无跨天视角**
   - `data/history/daily-report-index.json`（122 条）字段为 date/summary_brief/各类 titles/top_repos/signal_count，**无任何 token 字段**
   - 周报模型（`WeeklyReport`）无 metrics 字段，最新 `weekly-2026-W36.json` 确认无
   - 前端 `web/src` 对 usage/cost **零引用**
   - 运行日志中 token 关键字命中 **0 行**
   → 没有任何地方能回答「今天/这周一共花了多少 token」

5. `issue_insights.agent_metrics_summary` 为 `null`（因 `enable_issue_agent_analysis=False`，属预期）

**建议方案（按性价比排序）**

1. **`structured_query.py` 提取 usage** —— 数据本来就在 `ResultMessage` 里，补上即覆盖最贵的 commit 分析。约 10 行改动，收益最大。
2. **`base.py` 记录 usage** —— 直连 SDK 的响应对象自带 `usage`，在 `_extract_text_from_response` 旁加累加器即可覆盖其余 5 个分析器。
3. **流程级汇总** —— 把两路 usage 汇成 `daily_llm_usage` 写进日报 JSON，这样才有「今日总消耗」这个数；再往历史索引加字段，即可看跨天趋势。
4. **让 `daily_token_budget` 真正生效**，或直接删除该配置项，避免继续误导。

**涉及文件**：`analyzers/structured_query.py`、`analyzers/base.py`、`models/agent_usage.py`、`history/daily_report_history.py`、`config.py`

---

## P1-2 指标里 `model` 为 null，无法区分模型

**现象**
今日记录中 `daily_summary_agent_run_metrics.model = null`、`agent_metrics_summary.models = []`。

**根因**
`daily_summary_agent.py:56` 的 `self.model = model`，取值来自 `daily_summary_agent_model`；
`.env:69` 该行是注释状态（`# DAILY_SUMMARY_AGENT_MODEL=...`）→ 传入 `None`。

**影响**
记录了消耗却不知道**用的是哪个模型**。跨网关、跨模型的历史数据无法对比，
也无法验证「切到 deepseek-v4-flash 后成本/质量如何变化」这类问题。

**建议方案**
`from_sdk_result` 的 `model` 参数在为空时回落到 `settings.anthropic_model`
（即实际生效的模型），而不是留 `None`。这样即便不单独配置 agent 模型，指标也能自解释。

**涉及文件**：`analyzers/daily_summary_agent.py`、`analyzers/issue_agent_runner.py`、`models/agent_usage.py`

---

## P1-3 `total_cost_usd` 不是真实成本，且影响预算语义

**现象与验算**
今日记录 `total_cost_usd = 2.707855`。按各档价目反推：

| 假定价目 | 计算结果 |
|---|---|
| **$5/M in + $25/M out** | **$2.707855 ← 与记录值完全吻合** |
| Claude Sonnet $3/$15 | $1.624713 |
| Claude Opus $15/$75 | $8.123565 |
| Claude Haiku $1/$5 | $0.541571 |

说明 claude-agent-sdk 对 `deepseek-v4-flash-aistar` 这个它不认识的模型名，套用了某套**内置默认价目表**。

**影响**
1. 历史累计的 `$89.64` 是名义值，**不等于真实支出**（deepseek-v4-flash 实际单价远低于此）。
2. `max_budget_usd` 熔断阈值基于同一套名义价格 —— 上轮的 `Reached maximum budget ($3)`
   与现在的 `COMMIT_AGENT_MAX_BUDGET_USD=20.0`，含义都是「按 Claude 价目折算的额度」。
   它能有效限制消耗（是个可用代理指标），但**不能当成本核算用**。

**建议方案**
- 短期：在文档与 `.env.example` 注明该字段为名义估算值，避免误读。
- 中期：成本核算**以 token 数为准**（token 是网关无关的客观量），
  如需真实金额，按网关实际单价另行换算，不依赖 SDK 的 `total_cost_usd`。
- 预算熔断继续使用 `max_budget_usd`，但需知悉其单位是「Claude 名义美元」。

**涉及文件**：`.env.example`、`models/agent_usage.py`（可考虑增加 `is_nominal_cost` 标注或注释）

---

## P1-4 采集耗时分布：candidate collection 占一半

> **测量前提**：下列数据来自 2026-09-11 的完整运行，当时代码处于 rebase 前的旧基线
> `c1af179`。上游 157 个提交已重构过部分采集/分析逻辑（例：`trend_analyzer.py`
> 762 行 → 675 行），因此**具体秒数仅供参考，阶段占比与瓶颈结论需在当前 HEAD 重测后再定优化方案**。

**实测数据（本次完整运行，总 2170.65s ≈ 36 分钟）**

| 阶段 | 耗时 | 占比 |
|---|---|---|
| Activity collection | 11.49s | 0.5% |
| Release collection | 18.77s | 0.9% |
| Async analysis（commit，535 commits / 3 批） | 461.83s | 21.3% |
| **Candidate collection（80 仓库 PR）** | **1100.52s** | **50.7%** |
| PR detail fetch（20 PR） | 6.42s | 0.3% |
| PR analysis | 59.86s | 2.8% |
| Deduplication | 0.68s | 0.03% |
| Aggregation | 73.29s | 3.4% |

**观察**
- Candidate collection 是绝对大头（>50%），且随监控仓库数线性增长（当前 80 个）。
- 日志中大量 `Following Github server redirection from /repos/X to /repositories/NNN`
  （aider、gptme、OpenDevin、claude-flow、Auto-Claude、open-interpreter、goose、ai-chatbot 等）——
  这些仓库已改名/转移，每次请求都多一跳重定向。
- 另有瞬时网络错误：`anthropics/devcontainer-features` GraphQL 查询 `SSLError(UNEXPECTED_EOF_WHILE_READING)`。

**建议方案**
1. **消除重定向开销**：把 `repos.json` 里已转移的仓库更新为当前名（或直接用 repository ID），省掉每次 301 跳转。
2. **评估并行度**：`MAX_PARALLEL_WORKERS=8`（上限 32），candidate collection 是否受此限制、提高是否触发限流，需实测。
3. **网络抖动重试**：确认 GraphQL 采集路径是否已被 `create_github_retry_decorator` 覆盖（注意其只重试 429 + 5xx，`SSLError` 不在可重试范围内）。

**涉及文件**：`repos.json`、`collectors/github_events.py`、`collectors/activity.py`、`utils/retry.py`

---

## P2-1 报告文件格式：不建议合并，但需收敛派生产物

**现状盘点**

| 目录 | json | md | 其他 | 体量 |
|---|---|---|---|---|
| `reports/daily/` | 191 | 195 | — | 70M |
| `reports/weekly/` | 26 | 27 | — | 848K |
| `reports/discovery/` | 218 | 218 | **190 个 `-actionable.json`** + 1 个 `bridge-result.json` | 72M |

单日单份日报：**json 401.3 KB vs md 58.1 KB（约 7 倍差）**。`reports/` 合计 142M。

**消费方梳理**

- **JSON（机器真源，4 个消费方）**：Astro 前端 `glob('report-*.json')`（`content.config.ts:139`）、
  `history/daily_report_history.py:31` 据此构建历史索引、飞书通知 `find_daily_report_json`、
  smoke CI 的 `validate_smoke_daily_summary`
- **MD（3 个消费方）**：`run-daily-smoke.yml:70` 断言 `test -f "$REPORT_MD"`、
  `discover-projects.yml:142` 上传 `discovery-*.md` 作 artifact、GitHub 网页人工浏览
  （workflow 注释原话「md 作为 GitHub 浏览兜底」）
- **前端完全不读 md**（`web/src` 零引用）
- `DailySummaryAgent` 拿到「历史日报原文目录」+ Read/Glob 工具，两种都能读 ——
  而 **md 只有 json 的 1/7 大小**，回读历史时 token 成本差约 7 倍（与 P1-1 直接相关）

**结论：不要只保留一种**

- 删 md → smoke CI 断言失败、discovery artifact 上传失败、GitHub 上只剩 401KB 不可读 JSON、agent 回读成本涨 7 倍
- 删 json → 前端、历史索引、飞书、smoke 校验全断；且 md 无法反向还原结构化数据
  （`feishu_notifications.py` 注释明确写了「不再从 Markdown 反向解析」，说明这条路试过并放弃了）

**正确定位：JSON = 真源，MD = 派生视图**（md 可由 `MarkdownReporter` 随时重生成，反之不行）。

**真正该收敛的三件事**

1. **`discovery-*-actionable.json`（190 个，纯中间产物）**
   只被 `app/bridge_discovery_to_monitoring.py:29-36` 消费一次，是 discovery → repos.json 的桥接输入，
   无长期归档价值。建议改落到 `data/`（已 gitignore）或干脆不入库。**这是最干净的一刀。**

2. **5 个孤儿 md**（有 md 无 json，前端与历史索引都看不到这些日期）
   - daily：`report-2026-01-02`、`01-03`、`01-04`、`01-12`
   - weekly：`weekly-2026-W04`
   其中 01-02 与 01-12 是本轮删除假 JSON 造成；01-03、01-04 历史上就从未有过 json（存量孤儿）。
   注意 `report-2026-01-12.md` 是 CI 生成的**真报告**（6990 bytes，含 6 个 commit 信号），
   其 json 当时只有 22 bytes 的测试污染内容。
   → 建议加**一致性校验**（有 json 必有 md；反之允许缺，但需能被检出）。

3. **可选：前端对「仅有 md」的日期降级展示原文**，让 01-12 这类真报告在网页上仍可达。

**涉及文件**：`app/discovery.py:190-196`、`app/bridge_discovery_to_monitoring.py`、
`reports/publisher.py`、`.github/workflows/discover-projects.yml`、`web/src/content.config.ts`

---

## P2-2 AGENTS.md 存在过期陈述

**问题**

| AGENTS.md 陈述 | 实际情况 |
|---|---|
| 第 8 行：`` `docs/` and `mkdocs.yml`: documentation sources and MkDocs config`` | **两者均不存在** |
| 第 21 行：`make docs` / `make docs-serve`: build or serve MkDocs | Makefile **无任何 docs 目标**（实际只有 venv / install / check / format / typecheck / test / test-cov / run / clean / all / help） |
| 项目结构未提及 | `web/` 是 Astro 前端（Pages 站点真源），`site/` 是遗留 MkDocs 构建产物（8.7M，未跟踪） |

**影响**
AGENTS.md 是给 AI agent 与新贡献者的首要指引，过期陈述会导致：
按文档执行 `make docs` 直接失败；误以为存在 MkDocs 文档体系而找不到 `docs/`；
不知道 `web/` 才是站点真源。

**建议方案**
1. 删除 `docs/` + `mkdocs.yml` + `make docs` 相关陈述，或补齐缺失的目标与目录（二选一，取决于是否还要 MkDocs）。
2. 项目结构补充 `web/`（Astro + Tailwind + GSAP，部署到 GitHub Pages 子路径 `/TrendPluse/`）。
3. `site/`（8.7M 遗留产物）建议删除或加入 `.gitignore`。

**涉及文件**：`AGENTS.md`、`Makefile`、`.gitignore`、`site/`

---

## P2-3 前端 schema 校验缺口（`[object Object]` 的同类风险）

**现象**
`web/src/content.config.ts` 有 5 处用 `z.unknown()` 放行任意结构：

| 行 | 字段 |
|---|---|
| 44 | `stats: z.record(z.string(), z.unknown()).default({})` |
| 53 | `releases: z.record(z.string(), z.unknown()).nullish()` ← **P0-1 的直接成因** |
| 54 | `breaking_changes: z.unknown().nullish()` |
| 56 | `issue_insights: z.record(z.string(), z.unknown()).nullish()` |
| 122 | `highlight: z.record(z.string(), z.unknown()).nullish()` |

**影响**
后端 pydantic 模型演进（如 `ai_summary` 从 str 变对象）时，前端**不会在构建期报错**，
而是静默渲染出 `[object Object]` 或 `undefined`。P0-1 就是这个机制的既成事故。

**建议方案**
按后端 `models/signal.py` 的 pydantic 定义，为上述字段补真实 zod schema（至少覆盖会被渲染的字段），
并把组件内手写的 interface 改为从 collection 推导（`content.config.ts` 已导出 `Signal`、`DailyReport` 等类型别名，可直接复用），
消除「组件 interface 与 schema 各写一套」的漂移。

**涉及文件**：`web/src/content.config.ts`、`web/src/components/report/*.astro`
**参照**：`src/trendpluse/models/signal.py`

---

## P3-1 Dependabot 38 项告警（含 2 critical）——建议暂不升级

**告警构成**

| 级别 | 内容 |
|---|---|
| critical ×2 | `astro` AVIF 图片优化 RCE（GHSA-26w7-cxv4-gfx2），受影响 `< 7.2.8`，修复版 **7.2.8** |
| high ×19 | `astro` 的 Host header SSRF、反射型 XSS；`fast-uri` 的 host 混淆 / SSRF 系列（多为传递依赖） |
| moderate ×12 / low ×5 | 其余 |

**实际暴露面评估：低**

| 因素 | 结论 |
|---|---|
| 漏洞触发前提 | 需要运行时的图片优化服务在响应请求 |
| 本项目形态 | `web/astro.config.mjs` **无 `output` 配置、无任何 adapter** → Astro 默认 **static 静态输出**，线上无 Node 服务进程 |
| 代码使用面 | `web/src` 中 `astro:assets` / `<Image>` / `image=` **零处使用** → 连构建期也不碰该功能 |
| 当前版本 | `pnpm-lock.yaml` 锁定 `astro@5.18.2` |
| 与 Python 链路关系 | `pyproject.toml` 无任何 JS 依赖，**采集/分析链路与 astro 完全解耦** |

**建议方案**
- **不建议现在升 astro 5 → 7**：跨两个大版本的破坏性升级，风险（可能弄坏 Pages 站点）远高于收益（漏洞功能未使用、无服务端暴露）。
- 可选低风险动作：`pnpm audit --fix` 只处理兼容范围内的传递依赖（如 `fast-uri`）。
- 若要根治，应安排一次**独立的前端升级窗口**，配套站点回归验证，而非夹带在功能提交里。
- 注：`astro` 位于 `dependencies` 而非 `devDependencies`；对纯 SSG 而言这个区分意义不大
  （CI 用 `pnpm install --frozen-lockfile` 两者都会装），但语义上更准确的位置是 `devDependencies`。

**涉及文件**：`web/package.json`、`web/pnpm-lock.yaml`

---

## P3-2 监控清单待决策

1. **是否加入 `openclaw/agent-skills`**
   已删除的 `openclaw/skills`（404、不保留 301）疑似由它替代：1082 stars，
   描述 "Useful skills for agents and claws."，同属 `openclaw` org。
   属监控范围变更，需明确决策后再动 `repos.json`。

2. **已转移仓库的名录更新**（与 P1-4 相关）
   采集日志显示以下仓库仍在走 301 重定向，说明 `repos.json` 里是旧名：
   `paul-gauthier/aider`、`ErikBjare/gptme`、`OpenDevin/OpenDevin`、`ruvnet/claude-flow`、
   `AndyMik90/Auto-Claude`、`openinterpreter/open-interpreter`、`block/goose`、`vercel/ai-chatbot`。
   更新为当前名可省掉每次请求的额外跳转。

**涉及文件**：`repos.json`

---

## 附：本轮验证过的事实基线（供后续对比）

- 网关：`https://newapi.tashan.chat`，模型 `deepseek-v4-flash-aistar`
  （`.tashan` 原写的 `deepseek-v4-flash-aistarZZ` 返回 `503 model_not_found`，group vip 下无可用 channel）
- 网关可用模型（14 个，均标注 `supported_endpoint_types: ['openai']`，但 `/v1/messages` 实测可用）：
  `DeepSeek-V4-Flash-0731`、`DeepSeek-V4-Pro-0813`、`GLM-5.3`、`Kimi-K3`、`Qwen3.8-Max`、
  `deepseek-v4-flash-aistar`、`glm-5.3-flash`、`glm5.2`、`minimax-m3`、`qwen3.6-27b` 等
- 监控仓库：80 个（由 `repos.json` 提供结构化 url + description；`.env` 中 `GITHUB_REPOS` 保持注释，
  因为设置它会覆盖 `repos.json` 的结构化配置）
- 今日报告：总信号 41→47、高影响 15→20、commit 信号 11→14、release 10→13；
  批次失败 1→0；总耗时 2170.65s
- `commit_signals` 字段落盘为 0 属**设计如此**（`reports/builder.py:42` 聚合后清空以避免重复展示），
  真实计数看 `stats.commit_count`
