"""`trendpluse.utils.env` 加载器测试。

重点验证 `.env` 优先级高于进程已有环境变量（override=True），
因为 claude-agent-sdk 会 fork `claude` CLI 子进程，子进程只认 os.environ。
"""

import os
from pathlib import Path

import pytest

from trendpluse.utils.env import load_env, load_env_from_project_root

TEST_VAR = "TRENDPLUSE_ENV_LOADER_TEST_VAR"
BASE_VAR = "TRENDPLUSE_ENV_LOADER_BASE_VAR"


@pytest.fixture(autouse=True)
def _cleanup_test_vars(monkeypatch: pytest.MonkeyPatch):
    """确保测试变量在用例前后都不残留。"""
    monkeypatch.delenv(TEST_VAR, raising=False)
    monkeypatch.delenv(BASE_VAR, raising=False)
    yield
    os.environ.pop(TEST_VAR, None)
    os.environ.pop(BASE_VAR, None)


def _write_env(tmp_path: Path, value: str) -> Path:
    """在临时目录写入只含 TEST_VAR 的 .env 文件。"""
    env_file = tmp_path / ".env"
    env_file.write_text(f"{TEST_VAR}={value}\n", encoding="utf-8")
    return env_file


class TestLoadEnv:
    """load_env 行为测试。"""

    def test_loads_values_into_environ(self, tmp_path: Path):
        """应把 .env 的键值写入 os.environ。"""
        env_file = _write_env(tmp_path, "from_dotenv")

        assert load_env(env_file) is True
        assert os.environ[TEST_VAR] == "from_dotenv"

    def test_dotenv_overrides_existing_environ_by_default(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ):
        """默认 override=True：.env 覆盖 shell 里已有的同名变量。"""
        monkeypatch.setenv(TEST_VAR, "from_shell")
        env_file = _write_env(tmp_path, "from_dotenv")

        assert load_env(env_file) is True
        assert os.environ[TEST_VAR] == "from_dotenv"

    def test_override_false_keeps_existing_environ(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ):
        """显式 override=False 时保留 shell 原值（旧行为）。"""
        monkeypatch.setenv(TEST_VAR, "from_shell")
        env_file = _write_env(tmp_path, "from_dotenv")

        assert load_env(env_file, override=False) is True
        assert os.environ[TEST_VAR] == "from_shell"

    def test_missing_file_returns_false(self, tmp_path: Path):
        """.env 不存在时返回 False 且不抛异常。"""
        assert load_env(tmp_path / "does-not-exist.env") is False

    def test_interpolates_referenced_variables(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ):
        """支持 ${VAR} 插值。"""
        monkeypatch.setenv(BASE_VAR, "base-value")
        env_file = tmp_path / ".env"
        env_file.write_text(
            f"{TEST_VAR}=${{{BASE_VAR}}}-suffix\n",
            encoding="utf-8",
        )

        assert load_env(env_file) is True
        assert os.environ[TEST_VAR] == "base-value-suffix"

    def test_interpolate_disabled_keeps_literal(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ):
        """interpolate=False 时保留 ${VAR} 字面量。"""
        monkeypatch.setenv(BASE_VAR, "base-value")
        env_file = tmp_path / ".env"
        env_file.write_text(f"{TEST_VAR}=${{{BASE_VAR}}}-suffix\n", encoding="utf-8")

        assert load_env(env_file, interpolate=False) is True
        assert os.environ[TEST_VAR] == f"${{{BASE_VAR}}}-suffix"


class TestLoadEnvFromProjectRoot:
    """load_env_from_project_root 行为测试。"""

    def test_reads_repo_root_env_file(self):
        """仓库根存在 .env 时应加载成功，否则回退查找且不报错。"""
        project_root = Path(__file__).resolve().parents[2]
        assert load_env_from_project_root() is (project_root / ".env").is_file()

    def test_falls_back_when_file_missing(self):
        """指定文件不存在时回退到 python-dotenv 的向上查找，不抛异常。"""
        assert load_env_from_project_root("no-such-env-file.env") in (True, False)
