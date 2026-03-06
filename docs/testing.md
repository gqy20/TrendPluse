# 测试说明

## 测试结构

当前测试主要分为两层：

```text
tests/
  test_*.py        顶层基础测试
  unit/            细粒度单元与工作流测试
  integration/     保留给外部依赖或更重的流程测试
```

## 重点覆盖面

### 配置与环境

- `test_config.py`
- `test_github_actions_config.py`

重点保证：

- 环境变量别名兼容
- CI 环境下行为稳定
- `.env` 与默认值逻辑一致

### CLI 与应用入口

- `test_cli_help_smoke.py`
- `test_send_feishu_notification.py`
- `test_add_repo.py`

重点保证所有 `pyproject.toml` 中注册的 CLI 至少能正常展示 `--help`，并覆盖关键入口行为。

### 核心分析器

- `test_analyzer.py`
- `test_async_analyzers.py`
- `test_release_summarizer*.py`
- `test_trend_analyzer*.py`

重点覆盖同步/异步路径、重试、并行与兼容包装方法。

### 主编排与应用流程

- `test_pipeline.py`
- `test_pipeline_weekly.py`
- `test_report_output_service.py`
- `test_issue_workflow_service.py`

重点保证 `app.pipeline`、`app.weekly`、issue 分析流程和输出链路行为稳定。

## 运行方式

```bash
# 全量测试
make test

# 覆盖率
make test-cov

# 单文件
uv run pytest tests/unit/test_pipeline.py

# 关键回归集
uv run pytest tests/unit/test_async_analyzers.py tests/unit/test_pipeline.py -q
```

## 当前测试策略

### 1. 环境隔离优先

涉及环境变量的测试必须显式设置/清理相关变量，不能依赖开发机或 CI 的外部状态。

### 2. 冒烟测试保护 CLI 收口

由于项目已将命令入口统一收口到 `cli/`，CLI 冒烟测试是防止入口回退或 `pyproject.toml` 漏改的重要保护。

## 推荐新增测试时机

- 新增 CLI 入口时：同步更新 `test_cli_help_smoke.py`
- 新增环境变量兼容逻辑时：同步更新配置测试
- 新增应用编排时：优先补 `app/` 层测试，再补 CLI 或集成测试
