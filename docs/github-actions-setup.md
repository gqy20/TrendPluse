# GitHub Actions 配置指南

## Workflow 文件

### 1. CI (`.github/workflows/ci.yml`)

- 触发：`push` / `pull_request`
- 功能：ruff、mypy、pytest、codecov

### 2. 每日分析 (`.github/workflows/run-daily.yml`)

- 触发：`schedule` + `workflow_dispatch`
- 功能：生成日报、同步索引、提交产物，并按配置发送日报飞书通知

### 3. 周报生成 (`.github/workflows/run-weekly.yml`)

- 触发：`schedule` + `workflow_dispatch`
- 功能：聚合日报生成周报并提交产物

### 4. 项目发现 (`.github/workflows/discover-projects.yml`)

- 触发：`schedule` + `workflow_dispatch` + `workflow_call`
- 功能：发现候选项目、生成 discovery 报告，并可将候选仓库写入 `repos.json`

### 5. Issue 仓库分析 (`.github/workflows/issue-analyzer.yml`)

- 触发：`issues` / `issue_comment`
- 功能：在 issue/comment 中识别 `@claude`，调用分析脚本并回帖

### 6. 仓库请求处理 (`.github/workflows/add-repo-request.yml`)

- 触发：Issue 表单/标签驱动
- 功能：自动处理新增监控仓库请求

### 7. Pages 部署 (`.github/workflows/deploy-pages.yml`)

- 触发：`push`（`docs/**`、`reports/**`、`mkdocs.yml`）+ `workflow_dispatch`
- 功能：构建 MkDocs 并部署 GitHub Pages

### 8. 飞书通知 (`.github/workflows/send-feishu.yml`)

- 触发：手动触发（支持指定日期）
- 功能：发送日报飞书通知

## 配置 Secrets

在 GitHub 仓库中配置以下 Secrets：

### 必需配置

| Secret 名称 | 说明 | 获取方式 |
|------------|------|----------|
| `ANTHROPIC_API_KEY` | 智谱 AI API Key | https://open.bigmodel.cn/usercenter/apikeys |

### 可选配置

| Secret 名称 | 说明 | 默认值 |
|------------|------|--------|
| `ANTHROPIC_BASE_URL` | API 基础 URL | `https://open.bigmodel.cn/api/anthropic` |
| `GITHUB_TOKEN` | GitHub Token | 自动提供 |
| `GITHUB_PAT` / `PAT_TOKEN` | 推荐使用的 GitHub PAT 别名 | 无 |
| `FEISHU_WEBHOOK_URL` | 飞书 Webhook URL | 无（不发送通知） |
| `FEISHU_SECRET` | 飞书签名验证密钥 | 无 |
| `FEISHU_AT_MOBILES` | 飞书 @ 提醒手机号 | 无 |

**建议：** 使用 `GITHUB_PAT` 或 `PAT_TOKEN` 配置 Personal Access Token，避免依赖默认 `GITHUB_TOKEN`

---

## 手动触发 Workflow

### 方式 1: GitHub UI

1. 进入仓库的 **Actions** 标签
2. 选择 **Run Daily Analysis** workflow
3. 点击 **Run workflow** 按钮
4. 按需填写输入参数并运行

### 方式 2: GitHub CLI

```bash
# 运行每日分析
gh workflow run run-daily.yml

# 运行每日分析并发送飞书通知
gh workflow run run-daily.yml -f send_notification=true

# 发送指定日期的飞书通知
gh workflow run send-feishu.yml -f report_date=2026-01-12
```

---

## 报告位置

### 仓库提交

报告也会自动提交到 `reports/` 目录：
```
reports/
├── daily/
│   ├── report-2026-01-02.md
│   └── report-2026-01-02.json
├── weekly/
│   └── weekly-2026-W08.md
└── discovery/
    └── discovery-2026-02-23.md
```

### GitHub Pages

报告自动发布到 GitHub Pages：
- https://home.gqy20.top/TrendPluse/

---

## 本地测试 Workflow

使用 [act](https://github.com/nektos/act) 在本地测试 GitHub Actions：

```bash
# 安装 act
brew install act  # macOS
# 或
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# 运行 CI
act -j lint

# 运行每日分析
act -j analyze
```

---

## 飞书通知配置

### 获取 Webhook URL

1. 在飞书群组中添加自定义机器人
2. 选择"自定义机器人" → "添加"
3. 复制 Webhook URL 到 `FEISHU_WEBHOOK_URL`

### 签名验证（可选）

1. 在机器人设置中启用"签名验证"
2. 复制签名密钥到 `FEISHU_SECRET`

### @ 提醒配置

添加手机号到 `FEISHU_AT_MOBILES`（逗号分隔）：
```
13800138000,13900139000
```

---

## 故障排查

### Workflow 失败

1. **检查 Secrets 配置**
   ```bash
   gh secret list
   ```

2. **查看运行日志**
   - Actions → 选择失败的运行 → 查看详细日志

3. **常见错误**
   - `ANTHROPIC_API_KEY` 未设置 → 添加 Secret
   - 速率限制 → 使用 `GITHUB_PAT` / `PAT_TOKEN`
   - 测试失败 → 本地运行 `uv run pytest` 确认

### 飞书通知失败

1. **检查飞书配置**
   ```bash
   gh secret list | grep FEISHU
   ```

2. **查看飞书卡片内容**
   - 下载 artifact `feishu-card-YYYY-MM-DD`
   - 检查 JSON 格式是否正确

3. **手动重发通知**
   ```bash
   gh workflow run send-feishu.yml -f report_date=2026-01-12
   ```

---

## 最佳实践

1. **使用 PAT 获得更高速率限制**
   - 创建 PAT: https://github.com/settings/tokens
   - 权限: `public_repo` 即可
   - 添加到 Secrets: `GITHUB_PAT` 或 `PAT_TOKEN`

2. **调整运行频率**
   - 编辑 `.github/workflows/run-daily.yml`
   - 修改 cron 表达式
   - 示例：`0 0 * * 1` (每周一运行)

3. **报告保留策略**
   - Artifact 默认保留 30 天
   - 修改 `retention-days` 参数调整

4. **飞书通知优化**
   - 使用折叠面板减少信息过载
   - 设置 `FEISHU_MAX_SIGNALS` 控制信号数量
   - 按需启用 @ 提醒功能

---

## 工作流状态徽章

[![CI](https://img.shields.io/badge/GitHub-Actions-blue)](https://github.com/gqy20/TrendPluse/actions)
