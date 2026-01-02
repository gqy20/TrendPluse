"""pytest 的配置和 fixture。"""

import os
import tempfile
from pathlib import Path

import pytest


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
