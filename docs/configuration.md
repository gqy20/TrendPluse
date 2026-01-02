# 配置指南

## 环境变量配置

### 必需配置

| 变量名 | 说明 | 示例值 |
|--------|------|--------|
| `ANTHROPIC_API_KEY` | 智谱 AI API 密钥 | `your_api_key_here` |
| `ANTHROPIC_BASE_URL` | API 基础 URL | `https://open.bigmodel.cn/api/anthropic` |

### 可选配置

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| `GITHUB_TOKEN` | GitHub 访问令牌 | 无（匿名访问） |
| `ANTHROPIC_MODEL` | 使用的模型 | `glm-4.7` |
| `GITHUB_REPOS` | 追踪的仓库列表 | 见下方默认值 |

## 默认追踪仓库

```python
DEFAULT_REPOS = [
    "anthropics/anthropic-sdk-python",
    "anthropics/claude-quickstarts",
    "anthropics/skills",
]
```

## 配置文件

### 方式 1: 使用 .env 文件

创建项目根目录下的 `.env` 文件：

```bash
# .env
ANTHROPIC_API_KEY=your_api_key_here
ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic
GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

### 方式 2: 使用系统环境变量

```bash
# Linux/Mac
export ANTHROPIC_API_KEY="your_api_key_here"
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"

# Windows (PowerShell)
$env:ANTHROPIC_API_KEY="your_api_key_here"
$env:ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"
```

### 方式 3: GitHub Secrets（CI/CD）

在 GitHub 仓库设置中添加 Secrets：

1. 进入仓库 Settings
2. 选择 Secrets and variables → Actions
3. 点击 New repository secret
4. 添加以下 secrets：
   - `ANTHROPIC_API_KEY`
   - `ANTHROPIC_BASE_URL`（可选）
   - `GITHUB_TOKEN`（可选）

## 高级配置

### 自定义追踪仓库

编辑 `src/trendpluse/config.py`：

```python
class Settings(BaseSettings):
    github_repos: list[str] = [
        "anthropics/anthropic-sdk-python",
        "your-org/your-repo",  # 添加自定义仓库
    ]
    max_candidates: int = 20  # 最大候选数量
```

### 调整分析参数

```python
class Settings(BaseSettings):
    # 影响评分阈值
    impact_threshold: int = 4

    # 日期范围（天）
    date_range_days: int = 1
```

### GitHub Actions 配置

编辑 `.github/workflows/daily-analysis.yml`：

```yaml
- name: Run TrendPulse analysis
  env:
    ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
    ANTHROPIC_BASE_URL: ${{ secrets.ANTHROPIC_BASE_URL }}
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: uv run python scripts/run.py
```

## 日志配置

### 调试模式

```bash
# 启用详细日志
export RUST_LOG=debug
uv run python scripts/run.py
```

### 日志级别

- `ERROR`: 仅错误
- `WARN`: 警告和错误
- `INFO`: 一般信息（默认）
- `DEBUG`: 详细调试信息

## 验证配置

运行以下命令验证配置是否正确：

```bash
# 检查环境变量
uv run python -c "from trendpluse.config import Settings; s = Settings(); print(s)"

# 测试 API 连接
uv run python -c "from trendpluse.config import Settings; from anthropic import Anthropic; s = Settings(); client = Anthropic(api_key=s.anthropic_api_key, base_url=s.anthropic_base_url); print('API 连接成功')"

# 测试 GitHub 连接
uv run python -c "from trendpluse.config import Settings; from github import Github; s = Settings(); g = Github(s.github_token); print('GitHub 连接成功')"
```

## 故障排查

!!! error "API 认证失败"
    检查 API Key 是否正确：
    ```bash
    echo $ANTHROPIC_API_KEY
    ```

!!! error "GitHub 速率限制"
    使用 Personal Access Token 提高限制：
    - 默认: 60次/小时
    - 使用 Token: 5000次/小时

!!! error "报告未生成"
    检查日志输出，确认是否有符合条件的 PR
