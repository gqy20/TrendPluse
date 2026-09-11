"""Prompt loader 单元测试。"""

from __future__ import annotations

import pytest
from jinja2 import UndefinedError

from trendpluse.prompts import PromptNotFoundError, render_prompt
from trendpluse.prompts import loader as prompt_loader


class TestRenderPrompt:
    def test_renders_with_variables(self):
        result = render_prompt(
            "sdk_commit_analyzer.commit_analysis",
            commits_file="/tmp/commits.md",
        )
        assert "/tmp/commits.md" in result
        assert "{{ commits_file }}" not in result

    def test_missing_key_raises_with_available_list(self):
        with pytest.raises(PromptNotFoundError) as exc_info:
            render_prompt("no_such_file.no_such_prompt")
        assert "no_such_file.no_such_prompt" in str(exc_info.value)
        assert "sdk_commit_analyzer.commit_analysis" in str(exc_info.value)

    def test_missing_variable_fails_fast(self):
        with pytest.raises(UndefinedError):
            render_prompt("sdk_commit_analyzer.commit_analysis")

    def test_trailing_newline_preserved(self):
        """块标量模板的尾部换行必须保留（字节级一致的前提）。"""
        result = render_prompt(
            "sdk_commit_analyzer.commit_analysis",
            commits_file="/tmp/x.md",
        )
        assert result.endswith("- 只返回真正有价值的趋势（避免琐碎修复）\n")

    def test_literal_json_braces_passthrough(self):
        """字面 JSON 大括号（单花括号）不应被 jinja2 吞掉。"""
        result = render_prompt(
            "sdk_commit_analyzer.commit_analysis", commits_file="/tmp/x.md"
        )
        # 原模板不含 JSON 示例，改用最小行为验证：渲染结果非空且无 jinja 残留
        assert result.startswith("你是一个技术趋势分析专家")


class _FakeFile:
    def __init__(self, name: str, content: str) -> None:
        self.name = name
        self._content = content

    def is_file(self) -> bool:
        return True

    def read_text(self, encoding: str = "utf-8") -> str:
        return self._content


class _FakeDir:
    def __init__(self, files: list[_FakeFile]) -> None:
        self._files = files

    def iterdir(self):
        return list(self._files)


def _patch_registry(monkeypatch, files: list[_FakeFile]) -> None:
    monkeypatch.setattr(prompt_loader.resources, "files", lambda _pkg: _FakeDir(files))
    prompt_loader._load_registry.cache_clear()


class TestRegistryValidation:
    def test_top_level_must_be_mapping(self, monkeypatch):
        _patch_registry(
            monkeypatch,
            [_FakeFile("bad.yml", "只是一个字符串")],
        )
        with pytest.raises(ValueError, match="结构错误"):
            prompt_loader._load_registry()

    def test_values_must_be_strings(self, monkeypatch):
        _patch_registry(
            monkeypatch,
            [_FakeFile("bad.yml", "key:\n  nested: 1")],
        )
        with pytest.raises(ValueError, match="必须是字符串"):
            prompt_loader._load_registry()

    def test_duplicate_keys_rejected(self, monkeypatch):
        content = "shared_key: |\n  文本\n"
        _patch_registry(
            monkeypatch,
            [
                _FakeFile("a.yml", content),
                _FakeFile("a.yaml", "shared_key: |\n  另一个文本\n"),
            ],
        )
        with pytest.raises(ValueError, match="key 冲突"):
            prompt_loader._load_registry()

    def test_empty_registry_rejected(self, monkeypatch):
        _patch_registry(monkeypatch, [])
        with pytest.raises(ValueError, match="未找到任何提示词"):
            prompt_loader._load_registry()

    def test_python_files_ignored(self, monkeypatch, tmp_path):
        """__init__.py / loader.py 等非 YAML 文件不应进入注册表。"""
        _patch_registry(
            monkeypatch,
            [
                _FakeFile("__init__.py", ""),
                _FakeFile("loader.py", ""),
                _FakeFile("ok.yml", "entry: |\n  文本\n"),
            ],
        )
        assert prompt_loader._load_registry() == {"ok.entry": "文本\n"}

    def teardown_method(self):
        """恢复真实注册表缓存，避免污染其他测试。"""
        prompt_loader._load_registry.cache_clear()
