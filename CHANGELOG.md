# Changelog

本项目所有显著变更记录于此。格式参照 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，
提交遵循 Conventional Commits。

## 2026-09-11（第二轮：ROADMAP 全量实施 + 报告治理）

### Added
- **提示词外置 YAML 统一管理**（`e541639`）：新增 `src/trendpluse/prompts/` 包
  （9 个 YAML / 12 条 prompt，jinja2 自定义定界符 `{$ $}` 规避 JSON 大括号冲突，
  StrictUndefined 缺变量即报错）；四对 sync/async 复制合并为共享模板；
  golden test 字节级锁定（17 个 fixture + `UPDATE_GOLDEN=1` 显式更新流程）。
- **research 信号聚合修复**（`e541639`）：`research_signals` 恒为 0 的根因——
  上游 prompt 无 category 判定标准 + 聚合 prompt"可为空"暗示 +
  `_resolve_sources_from_ids` 不处理 research。三处修复 + 3 个测试。
- **全流程 LLM usage 记录**（`ed7f9de`）：6 个直连分析器走
  `create_with_completion` 记录 usage；`StructuredQuery` 从 `ResultMessage`
  提取 metrics（覆盖最贵的 commit 分析）；日报新增 `daily_llm_usage`
  全流程汇总；历史索引新增 `total_tokens`/`total_cost_usd` 跨天字段；
  `daily_token_budget` 死配置激活为软限制（超限告警不熔断）。
- **JSON/MD 配对一致性校验**（`f4974e5`）：`scripts/check_report_consistency.py`
  接入 smoke CI（有 JSON 必有同名 MD，孤儿 MD 仅告警）。

### Fixed
- **聚合信号悬空 ID 剔除**（`9d45f5a`，P0-2）：定性为 LLM 幻觉（聚合候选 ID
  为 `pr-{idx}` 重新编号，`pr-418` 不可能来自输入），落盘前从
  `source_signal_ids` 剔除，脏引用不再进前端与历史索引。
- **前端 release 卡片 `[object Object]`**（`9d45f5a`，P0-1）：`ai_summary`
  改对象渲染（summary_cn + key_changes 列表 + change_type/impact_level 徽章）。
- **前端 `top_pain_points` 对象误渲染**（`9d45f5a`，附带发现）：445 条历史数据
  全为对象而非 string[]，"共性问题"区块渲染 `[object Object]`，改为
  topic/count/priority + 例证链接。
- **指标 `model` 为 null**（`ed7f9de`，P1-2）：`from_sdk_result` 新增
  `model_usage` 参数，从 SDK `ResultMessage.model_usage` 提取实际生效模型名。
- **网络异常不可重试**（`ff6943b`，P1-4）：GitHub 重试补
  `ssl.SSLError`/`httpx.TransportError`/`ConnectionError`
  （原只认 GithubException 429/5xx，GraphQL 的 SSLError 直接穿透）。

### Changed
- **前端 schema 校验补全**（`9d45f5a`，P2-3）：`content.config.ts` 5 处
  `z.unknown()` 替换为对齐后端 pydantic 的真实 zod schema；
  组件手写 interface 改从 schema 推导，消除"各写一套"漂移。
- **仓库名录更新消除 301 重定向**（`ff6943b`，P1-4/P3-2.2）：8 个已转移仓库
  更新为当前名（gh api 逐一确认），candidate collection 每请求省一跳 301。
- **discovery 中间产物收敛**（`f4974e5`，P2-1）：actionable/bridge-result
  落盘从 `reports/discovery/` 移到 `data/discovery/`（gitignored）；
  workflow 路径同步，JSON artifact glob 收紧为精确日期模式。
- **AGENTS.md 过期陈述修正**（`f4974e5`，P2-2）：删除不存在的 MkDocs 相关
  陈述，结构补齐 `web/`（Astro 前端）、`src/trendpluse/prompts`、`data/`。

### Removed
- **191 个 discovery 中间产物**（`f4974e5`）：190 个 `-actionable.json` +
  1 个 `bridge-result.json`（纯桥接输入，无归档价值）。
- **64 份旧格式日报**（`5e98d75`）：2026-03-17 及之前、缺统一格式总结增强
  字段的 JSON+MD 成对删除；5 个无 JSON 的孤儿 MD 一并清理。
- **44 份无 AI 分析结果的空日报**（`ea76cb6`）：2026-07-26 ~ 2026-09-10
  连续段，信号全空 + 无 AI metrics + 默认占位文案
  （04-25/04-26 有 AI 增强的周末分析，保留）。

## 2026-09-11（第一轮：网关切换 + 配置治理排查修复）

### Added
- `.env` 优先级高于进程环境变量（`5fe15b3`）：`utils/env.py` 封装
  `load_env(override=True)`，替换三处裸 `load_dotenv()`。
- commit 分析 Agent 预算可配置（`e0af25a`）：`COMMIT_AGENT_MAX_BUDGET_USD`
  （原硬编码 $3.0，535 commits 分 3 批时爆预算丢 1 批）。

### Fixed
- 周报聚合器改用配置模型（`8e3c5a9`）：原硬编码 `glm-4.7` 换网关后
  `503 model_not_found`；修复异步路径 `await` 同步 client。
- `_save_json` 落盘补末尾换行（`0c71d02`）：消除 `report-*.json` 反复脏 diff。
- `load_daily_history_index` 返回类型标注（`a70fc81`）：消除 `no-any-return`。

### Changed
- 测试隔离（`835e201`）：`.env` 泄漏进配置断言修复 + 会话级产物守卫
  （`reports/`、`data/` 被写即失败）。

### Removed
- 测试误提交的两个假日报 JSON（`62541e7`）。
- 失效仓库 `openclaw/skills`（`d0ec899`，404 且不保留 301）。
- `data/` 运行态缓存纳入 gitignore（`639f8bb`）。
