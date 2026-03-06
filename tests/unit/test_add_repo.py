"""测试添加仓库到监控配置。"""

from __future__ import annotations

import json
from pathlib import Path


def _write_repo_config(path: Path) -> None:
    path.write_text(
        json.dumps(
            [
                {
                    "url": "https://github.com/anthropics/claude-code",
                    "description": "Claude Code",
                },
                {
                    "url": "https://github.com/openai/swarm",
                    "description": "Swarm",
                    "category": "Agentic AI 核心框架",
                },
                {
                    "url": "https://github.com/cline/cline",
                    "description": "Cline",
                },
            ],
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


class TestAddRepo:
    """测试 add_repo.py 功能。"""

    def test_add_repo_to_category(self, tmp_path: Path):
        """测试：仓库可写入 repos.json 配置。"""
        config_file = tmp_path / "repos.json"
        _write_repo_config(config_file)

        from trendpluse.app.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="openai/codex",
            category="Agentic AI 核心框架",
        )

        assert result is True

        updated_entries = json.loads(config_file.read_text(encoding="utf-8"))
        urls = [entry["url"] for entry in updated_entries]
        assert "https://github.com/openai/codex" in urls

        codex_entry = next(
            entry
            for entry in updated_entries
            if entry["url"] == "https://github.com/openai/codex"
        )
        assert codex_entry["category"] == "Agentic AI 核心框架"

    def test_add_duplicate_repo_returns_false(self, tmp_path: Path):
        """测试：添加已存在的仓库返回 False。"""
        config_file = tmp_path / "repos.json"
        _write_repo_config(config_file)

        from trendpluse.app.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="anthropics/claude-code",
            category="Anthropic 核心产品",
        )

        assert result is False

    def test_add_repo_invalid_category(self, tmp_path: Path):
        """测试：无效分类返回 False。"""
        config_file = tmp_path / "repos.json"
        config_file.write_text("[]\n", encoding="utf-8")

        from trendpluse.app.add_repo import add_repo_to_config

        result = add_repo_to_config(
            config_file=str(config_file),
            repo="test/repo",
            category="不存在的分类",
        )

        assert result is False

    def test_validate_repo_format(self):
        """测试：仓库格式验证。"""
        from trendpluse.app.add_repo import validate_repo_format

        assert validate_repo_format("anthropics/claude-code") is True
        assert validate_repo_format("openai/swarm") is True
        assert validate_repo_format("a/b") is True

        assert validate_repo_format("anthropics-claude-code") is False
        assert validate_repo_format("anthropics/claude/code") is False
        assert validate_repo_format("/claude-code") is False
        assert validate_repo_format("anthropics/") is False
        assert validate_repo_format("") is False

    def test_parse_issue_body(self):
        """测试：解析 Issue 表单内容。"""
        from trendpluse.app.add_repo import parse_issue_body

        body = """
        ### GitHub 仓库

        openai/codex

        ### 分类

        Agentic AI 核心框架

        ### 添加理由

        这是一个终端编程代理工具
        """

        result = parse_issue_body(body)

        assert result["repo"] == "openai/codex"
        assert result["category"] == "Agentic AI 核心框架"
        assert "终端编程代理" in result["reason"]

    def test_category_to_marker_mapping(self):
        """测试：分类校验映射存在。"""
        from trendpluse.app.add_repo import get_category_markers

        markers = get_category_markers("Agentic AI 核心框架")
        assert markers is not None
        assert "start" in markers
        assert "end" in markers

        assert get_category_markers("不存在的分类") is None

    def test_batch_add_repos_to_config(self, tmp_path: Path):
        """测试：批量添加仓库，返回结构化结果。"""
        config_file = tmp_path / "repos.json"
        _write_repo_config(config_file)

        from trendpluse.app.add_repo import batch_add_repos_to_config

        result = batch_add_repos_to_config(
            config_file=str(config_file),
            items=[
                {
                    "repo": "openai/codex",
                    "category": "Agentic AI 核心框架",
                },
                {
                    "repo": "anthropics/claude-code",
                    "category": "Anthropic 核心产品",
                },
                {
                    "repo": "invalid-format",
                    "category": "Anthropic 核心产品",
                },
                {
                    "repo": "foo/bar",
                    "category": "不存在的分类",
                },
            ],
        )

        assert "openai/codex" in result["added"]
        assert "anthropics/claude-code" in result["duplicates"]
        assert "invalid-format" in result["invalid_format"]
        assert "foo/bar" in result["invalid_category"]

        updated_entries = json.loads(config_file.read_text(encoding="utf-8"))
        urls = [entry["url"] for entry in updated_entries]
        assert "https://github.com/openai/codex" in urls
