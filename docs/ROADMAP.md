# TrendPulse 优化路线图

> 本文档只保留**未解决**的待办项。已完成的变更见 `CHANGELOG.md`。
>
> 优先级定义：
> - **P1** 可观测性与成本治理缺失，影响决策质量
> - **P3** 待决策项或收益/风险需权衡的改动

---

## P1-4（剩余）采集并行度调优——需实测

> 背景：2026-09-11 实测 candidate collection（80 仓库 PR 事件）占总耗时
> 50.7%（1100.52s / 2170.65s）。301 重定向开销与网络异常重试已修复
> （见 CHANGELOG），剩余并行度问题需在当前 HEAD 重测后再定。

**现状**
- `MAX_PARALLEL_WORKERS=8`（上限 32），直接决定 candidate collection 并行度
- 仓库数随 discovery 桥接持续增长（当前 80），采集耗时线性上涨

**待办**
1. 在当前 HEAD 重跑一次完整采集，确认 301 修复后的耗时占比变化
2. 逐步上调 `MAX_PARALLEL_WORKERS`（如 16），观察 403/429 限流告警
3. 如遇限流，评估 GitHub token 升级（Pro 更高配额）或分批采集

**涉及文件**：`.env`、`collectors/github_events.py`、`collectors/activity.py`

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

**涉及文件**：`repos.json`

---

## 附：事实基线（供后续对比）

- LLM 网关：第三方 OpenAI 兼容网关（地址与模型名见 `.env` / `.env.example`，不入库文档），
  曾因模型名拼写错误返回 `503 model_not_found`（group 下无可用 channel），修正后正常
- 网关可用模型（14 个，均标注 `supported_endpoint_types: ['openai']`，但 `/v1/messages` 实测可用），
  具体清单以网关 `/v1/models` 实时查询为准
- 监控仓库：80 个（由 `repos.json` 提供结构化 url + description；`.env` 中 `GITHUB_REPOS` 保持注释，
  因为设置它会覆盖 `repos.json` 的结构化配置）
- `commit_signals` 字段落盘为 0 属**设计如此**（`reports/builder.py` 聚合后清空以避免重复展示），
  真实计数看 `stats.commit_count`
- 当前测试基线：`755 passed / 4 skipped`，ruff、ruff format、mypy（97 文件）、astro check/build 全绿
