"""pytest 的配置和 fixture。"""

import os
import tempfile
from datetime import UTC, datetime
from pathlib import Path

import pytest


@pytest.fixture
def now_utc():
    """返回当前 UTC aware datetime"""
    return datetime.now(UTC)


@pytest.fixture
def sample_data():
    """提供测试用的示例数据。"""
    return {"name": "测试用户", "age": 30, "email": "test@example.com"}


@pytest.fixture
def sample_numbers():
    """提供测试用的示例数字列表。"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def temp_file():
    """提供一个临时文件路径，测试后自动清理。

    用法:
        def test_something(temp_file):
            temp_file.write_text("content")
            assert temp_file.exists()
    """
    fd, path = tempfile.mkstemp(suffix=".tmp", prefix="test_")
    os.close(fd)
    yield Path(path)
    Path(path).unlink(missing_ok=True)


@pytest.fixture
def temp_dir():
    """提供一个临时目录路径，测试后自动清理。

    用法:
        def test_something(temp_dir):
            (temp_dir / "file.txt").write_text("content")
    """
    path = tempfile.mkdtemp(prefix="test_dir_")
    yield Path(path)
    # 递归删除目录
    import shutil

    shutil.rmtree(path, ignore_errors=True)


@pytest.fixture
def capture_logs(caplog):
    """捕获日志输出，配合 caplog fixture 使用。

    用法:
        def test_something(capture_logs):
            from trendpluse.logger import logger
            logger.info("test message")
            assert "test message" in capture_logs.text
    """
    import logging

    caplog.set_level(logging.DEBUG)
    return caplog


@pytest.fixture
def clean_env():
    """清理和恢复环境变量。

    用法:
        def test_something(clean_env):
            clean_env.set("MY_VAR", "value")
            assert os.getenv("MY_VAR") == "value"
            # 测试结束后自动恢复
    """
    original_env = os.environ.copy()

    class EnvManager:
        def set(self, key: str, value: str):
            os.environ[key] = value

        def unset(self, key: str):
            os.environ.pop(key, None)

    manager = EnvManager()
    yield manager
    # 恢复原始环境
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def mock_console():
    """模拟 Rich 控制台输出，用于测试日志显示。

    用法:
        def test_something(mock_console):
            from trendpluse.logger import print_success
            print_success("操作成功")
    """
    from unittest.mock import Mock

    mock_console = Mock()
    mock_console.print = Mock()
    return mock_console


@pytest.fixture
def sample_repos():
    """Anthropic 最火的 5 个仓库"""
    return [
        "anthropics/skills",
        "anthropics/claude-quickstarts",
        "anthropics/claude-agent-sdk-python",
        "anthropics/claude-code-security-review",
        "anthropics/anthropic-sdk-python",
    ]


@pytest.fixture
def mock_env_vars(monkeypatch):
    """Mock 必需的环境变量"""
    monkeypatch.setenv("TRENDPULSE_GITHUB_TOKEN", "test_github_token")
    monkeypatch.setenv("TRENDPULSE_ANTHROPIC_API_KEY", "test_anthropic_key")


@pytest.fixture
def mock_github(monkeypatch):
    """Mock GitHub API 相关对象

    提供模拟的 GitHub Issue 对象和仓库对象。
    """
    from datetime import UTC, datetime
    from unittest.mock import MagicMock, Mock, patch

    class MockGitHub:
        def __init__(self):
            self.mock_repo = MagicMock()
            self.issues_list = []
            self._patches = []

        def create_issue(
            self,
            number: int = 123,
            title: str = "Test Issue",
            body: str | None = "Test body",
            state: str = "open",
            created_at: datetime | None = None,
            updated_at: datetime | None = None,
            closed_at: datetime | None = None,
            comments: int = 0,
            labels: list | None = None,
        ):
            """创建模拟的 Issue 对象"""
            now = datetime.now(UTC)
            issue = Mock()
            issue.number = number
            issue.title = title
            issue.body = body
            issue.state = state
            issue.created_at = created_at or now
            issue.updated_at = updated_at or now
            issue.closed_at = closed_at
            issue.comments = comments
            issue.pull_request = None  # 默认不是 PR

            # Mock labels
            mock_labels = []
            if labels:
                for label_name in labels:
                    label = Mock()
                    label.name = label_name
                    mock_labels.append(label)
            issue.labels = mock_labels

            # Mock user
            issue.user = Mock()
            issue.user.login = "testuser"

            # Mock html_url
            issue.html_url = f"https://github.com/test/repo/issues/{number}"

            return issue

        def mock_repo_issues(self, issues: list):
            """设置仓库返回的 Issues 列表"""
            self.issues_list = issues

        def _get_repo_mock(self, repo_name: str):
            """获取仓库 mock，配置返回预设的 Issues"""
            mock_repo = MagicMock()
            mock_repo.get_issues.return_value = iter(self.issues_list)
            return mock_repo

    mock_gh = MockGitHub()

    # Mock Github class (在 base.py 中导入)
    # 需要接受 auth 参数或其他可能的参数
    def mock_github_class(*args, **kwargs):
        mock_client = MagicMock()
        mock_client.get_repo = mock_gh._get_repo_mock
        return mock_client

    patcher = patch("trendpluse.collectors.base.Github", mock_github_class)
    patcher.start()
    mock_gh._patches.append(patcher)

    yield mock_gh

    # 清理
    for p in mock_gh._patches:
        p.stop()
