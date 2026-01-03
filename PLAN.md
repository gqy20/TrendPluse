# Commit 链接显示优化计划

## 问题

当前 commit 链接显示不够直观：
- 链接文本只显示仓库名：`anthropics/claude-code-action`
- 实际链接指向具体 commit：`https://github.com/.../commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370`
- 用户无法从链接文本中看到具体的 commit SHA

## 解决方案

### 核心改动

1. **新增 `_format_source_url` 方法** (`markdown_reporter.py`)
   - 检测 URL 类型（commit/PR/Release/其他）
   - 对于 commit 链接：显示 `owner/repo@abc1234` 格式
   - 对于其他链接：保持原有逻辑

2. **更新 `render_signal` 方法** (`markdown_reporter.py`)
   - 使用 `_format_source_url` 替代 `_extract_repo_name`

### 显示效果对比

**改动前**：
```markdown
- [anthropics/claude-code-action](https://github.com/.../commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370)
```

**改动后**：
```markdown
- [anthropics/claude-code-action@b17b541] (https://github.com/.../commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370)
```

### 实现步骤

#### Step 1: 添加 `_format_source_url` 方法

```python
def _format_source_url(self, url: str) -> str:
    """格式化 source URL 显示文本

    Args:
        url: GitHub URL

    Returns:
        格式化的显示文本
    """
    if "github.com/" in url:
        # 移除 https:// 前缀
        clean_url = url.replace("https://github.com/", "").replace("http://github.com/", "")

        # 检测 commit 链接
        if "/commit/" in clean_url:
            parts = clean_url.split("/commit/")
            repo = parts[0]
            sha = parts[1].split("/")[0]  # 提取 SHA，可能后面有 ? 或 #
            short_sha = sha[:7]  # 显示前 7 位
            return f"{repo}@{short_sha}"

        # 检测 PR 链接
        elif "/pull/" in clean_url:
            parts = clean_url.split("/pull/")
            repo = parts[0]
            pr_num = parts[1].split("/")[0]
            return f"{repo}#{pr_num}"

        # 检测 Release 链接
        elif "/releases/" in clean_url or "/tags/" in clean_url:
            parts = clean_url.split("/releases/" if "/releases/" in clean_url else "/tags/")
            repo = parts[0]
            return f"{repo}"

        # 默认：提取仓库名
        else:
            parts = clean_url.split("/")
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}"

    return "链接"
```

#### Step 2: 更新 `render_signal` 方法

```python
def render_signal(self, signal: Signal) -> str:
    # ... 其他代码 ...

    sources_md = "\n".join(
        f"- [{self._format_source_url(url)}]({url})" for url in signal.sources
    )

    # ... 其他代码 ...
```

#### Step 3: 添加测试

在 `tests/unit/test_markdown_reporter.py` 中添加：

```python
def test_format_source_url_commit(self):
    """测试格式化 commit URL"""
    reporter = MarkdownReporter()

    url = "https://github.com/anthropics/claude-code-action/commit/b17b541bbc4d94ffa42edf2e2384ffe702e59370"
    result = reporter._format_source_url(url)

    assert result == "anthropics/claude-code-action@b17b541"

def test_format_source_url_pr(self):
    """测试格式化 PR URL"""
    reporter = MarkdownReporter()

    url = "https://github.com/anthropics/claude-code-action/pull/123"
    result = reporter._format_source_url(url)

    assert result == "anthropics/claude-code-action#123"

def test_format_source_url_repo(self):
    """测试格式化仓库 URL"""
    reporter = MarkdownReporter()

    url = "https://github.com/anthropics/claude-code-action"
    result = reporter._format_source_url(url)

    assert result == "anthropics/claude-code-action"
```

## 影响范围

- **文件修改**：`src/trendpluse/reporters/markdown_reporter.py`
- **测试新增**：`tests/unit/test_markdown_reporter.py`
- **影响功能**：所有信号的来源显示（PR、Commit、Release）
