# GitHub Actions 配置指南

## Workflow 文件

### 1. CI Workflow (`.github/workflows/ci.yml`)

**触发条件：**
- Push 到 `main` 或 `develop` 分支
- Pull Request 到 `main` 或 `develop` 分支

**功能：**
- 代码检查 (ruff check & format)
- 运行单元测试
- 上传覆盖率报告

### 2. Daily Analysis Workflow (`.github/workflows/daily-analysis.yml`)

**触发条件：**
- 每天 UTC 0:00 (北京时间 8:00)
- 手动触发 (workflow_dispatch)

**功能：**
- 运行单元测试
- 执行 GitHub 趋势分析
- 上传报告为 artifact
- 提交报告到仓库

---

## 配置 Secrets

在 GitHub 仓库中配置以下 Secrets：

### 必需配置

| Secret 名称 | 说明 | 获取方式 |
|------------|------|----------|
| `ANTHROPIC_API_KEY` | 智谱 AI API Key | https://open.bigmodel.cn/usercenter/apikeys |

### 可选配置

| Secret 名称 | 说明 | 默认值 |
|------------|------|--------|
| `GITHUB_TOKEN` | GitHub Token | 自动提供 (1000 次/小时) |

**建议：** 使用 Personal Access Token 替代默认 `GITHUB_TOKEN` 获得 5000 次/小时限制

---

## 手动触发 Workflow

### 方式 1: GitHub UI

1. 进入仓库的 **Actions** 标签
2. 选择 **Daily Trend Analysis** workflow
3. 点击 **Run workflow** 按钮

### 方式 2: GitHub CLI

```bash
gh workflow run daily-analysis.yml
```

---

## 报告位置

### Artifacts

每次运行后，报告会上传为 artifact，保留 30 天：
- Actions → 选择运行 → Artifacts 部分

### 仓库提交

报告也会自动提交到 `reports/` 目录：
```
reports/
├── report-2026-01-02.md
├── report-2026-01-03.md
└── ...
```

---

## 本地测试 Workflow

使用 [act](https://github.com/nektos/act) 在本地测试 GitHub Actions：

```bash
# 安装 act
brew install act  # macOS
# 或
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# 运行测试
act -j test
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
   - 速率限制 → 使用 PAT 替代默认 GITHUB_TOKEN
   - 测试失败 → 本地运行 `uv run pytest` 确认

---

## 最佳实践

1. **使用 PAT 获得更高速率限制**
   - 创建 PAT: https://github.com/settings/tokens
   - 权限: `public_repo` 即可
   - 添加到 Secrets: `GITHUB_TOKEN`

2. **调整运行频率**
   - 修改 `cron` 表达式
   - 示例：`0 0 * * 1` (每周一运行)

3. **报告保留策略**
   - 默认保留 30 天
   - 修改 `retention-days` 参数调整
