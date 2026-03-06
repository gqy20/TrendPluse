# 配置指南

## 环境变量

### 必需项

| 变量名 | 说明 | 默认值 |
|---|---|---|
| `ANTHROPIC_API_KEY` | 智谱 AI / Anthropic 兼容 API Key | 无 |

### GitHub 访问

`Settings.github_token` 当前支持 3 个别名，按优先级读取：

1. `PAT_TOKEN`
2. `GITHUB_PAT`
3. `GITHUB_TOKEN`

| 变量名 | 说明 | 默认值 |
|---|---|---|
| `PAT_TOKEN` | 推荐使用的 GitHub PAT 别名 | 无 |
| `GITHUB_PAT` | 兼容旧配置的 PAT 别名 | 无 |
| `GITHUB_TOKEN` | GitHub Actions 或本地 Token | 无 |

### 模型与运行参数

| 变量名 | 说明 | 默认值 |
|---|---|---|
| `ANTHROPIC_BASE_URL` | API Base URL | `https://open.bigmodel.cn/api/anthropic` |
| `ANTHROPIC_MODEL` | LLM 模型名 | `glm-4.7` |
| `MAX_CANDIDATES` | 每日流程最大候选数 | `20` |
| `DAYS_TO_LOOKBACK` | PR / Release 回溯天数 | `7` |
| `MAX_PARALLEL_WORKERS` | 并行采集线程数 | `8` |
| `DAILY_TOKEN_BUDGET` | 每日 token 预算 | `100000` |

### Issue / 飞书 / Release

| 变量名 | 说明 | 默认值 |
|---|---|---|
| `ENABLE_OPEN_PRS` | 是否包含 open PR | `false` |
| `MONITOR_RELEASES` | 是否监控 release | `true` |
| `INCLUDE_PRERELEASES` | 是否包含 prerelease | `false` |
| `FEISHU_WEBHOOK_URL` | 飞书 webhook | 空 |
| `FEISHU_SECRET` | 飞书签名密钥 | 空 |
| `FEISHU_AT_MOBILES` | 飞书提醒手机号，逗号分隔 | 空 |
| `FEISHU_MAX_SIGNALS` | 飞书卡片显示的信号数 | `5` |

## 仓库列表来源

项目默认从仓库根目录的 `repos.json` 加载监控仓库配置。

优先级如下：

1. 显式传入 `GITHUB_REPOS`
2. `GITHUB_REPOS_FILE` / `github_repos_file` 指向的 JSON 文件
3. 空列表

如果需要切换配置文件，可使用：

```bash
export GITHUB_REPOS_FILE=path/to/repos.json
```

`repos.json` 现在是 GitHub Actions 自动加仓库、discovery bridge apply 和本地 `trendpluse-add-repo` 的统一写入目标。

## `.env` 示例

```bash
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic

GITHUB_PAT=ghp_xxxxxxxxxxxx

FEISHU_WEBHOOK_URL=https://open.feishu.cn/open-apis/bot/v2/hook/...
FEISHU_SECRET=your_secret_here
FEISHU_AT_MOBILES=13800138000,13900139000

MAX_PARALLEL_WORKERS=8
DAILY_TOKEN_BUDGET=100000
```

## GitHub Actions Secrets

建议在仓库 Secrets 中配置：

- `ANTHROPIC_API_KEY`
- `ANTHROPIC_BASE_URL`
- `GITHUB_PAT` 或 `PAT_TOKEN`
- `FEISHU_WEBHOOK_URL`
- `FEISHU_SECRET`
- `FEISHU_AT_MOBILES`

## 输出目录

| 配置项 | 默认值 | 用途 |
|---|---|---|
| `output_dir` | `reports/daily` | 每日报告目录 |
| `snapshot_dir` | `data/snapshots` | 采集快照目录 |
| `issue_dump_dir` | `data/issues` | issue 明细落盘目录 |

## 推荐做法

- 本地开发优先使用 `.env`
- CI 中优先使用 `GITHUB_PAT` / `PAT_TOKEN`，不要依赖匿名 GitHub API 额度
- 仓库列表放在 `repos.json`，不要再通过直接修改 `config.py` 维护
- GitHub Actions 中与仓库列表相关的自动化流程，也应统一写入 `repos.json`
