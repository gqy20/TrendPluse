"""监控仓库配置加载测试。"""

import json

import pytest

from trendpluse.models.repository import MonitoredRepo
from trendpluse.utils.repo_config_loader import (
    load_monitored_repo_configs,
    parse_github_repo_url,
)


def test_parse_github_repo_url() -> None:
    """测试 GitHub URL 可被统一解析为 owner/repo。"""
    assert (
        parse_github_repo_url("https://github.com/anthropics/claude-code")
        == "anthropics/claude-code"
    )
    assert (
        parse_github_repo_url("https://github.com/anthropics/claude-code/")
        == "anthropics/claude-code"
    )
    assert (
        parse_github_repo_url("https://github.com/anthropics/claude-code.git")
        == "anthropics/claude-code"
    )


def test_parse_github_repo_url_rejects_invalid_url() -> None:
    """测试非法 GitHub URL 会被拒绝。"""
    with pytest.raises(ValueError):
        parse_github_repo_url("https://gitlab.com/anthropics/claude-code")


def test_load_monitored_repo_configs(tmp_path) -> None:
    """测试从 JSON 文件加载监控仓库配置。"""
    config_file = tmp_path / "repos.json"
    config_file.write_text(
        json.dumps(
            [
                {
                    "url": "https://github.com/anthropics/claude-code",
                    "description": "Claude Code 项目",
                }
            ]
        ),
        encoding="utf-8",
    )

    repos = load_monitored_repo_configs(str(config_file))

    assert repos == [
        MonitoredRepo(
            repo="anthropics/claude-code",
            url="https://github.com/anthropics/claude-code",
            description="Claude Code 项目",
        )
    ]


def test_load_monitored_repo_configs_missing_file(tmp_path) -> None:
    """测试配置文件缺失时返回空列表。"""
    repos = load_monitored_repo_configs(str(tmp_path / "missing.json"))

    assert repos == []


def test_load_monitored_repo_configs_rejects_invalid_json(tmp_path) -> None:
    """测试非法 JSON 会抛出错误。"""
    config_file = tmp_path / "repos.json"
    config_file.write_text("{invalid", encoding="utf-8")

    with pytest.raises(ValueError):
        load_monitored_repo_configs(str(config_file))
