"""同步首页监控仓库区块测试。"""

from pathlib import Path

from trendpluse.app.sync_repos_to_docs import (
    SECTION_END_MARKER,
    SECTION_START_MARKER,
    find_monitored_repos_section,
)


def test_find_monitored_repos_section_supports_marker_block() -> None:
    """标记区块应优先被识别。"""
    content = "\n".join(
        [
            "# 页面标题",
            SECTION_START_MARKER,
            "## 监控范围概览",
            "动态内容",
            SECTION_END_MARKER,
            "## 其他内容",
        ]
    )

    section = find_monitored_repos_section(content)

    assert section is not None
    start, end = section
    assert content[start:end] == "\n".join(
        [
            SECTION_START_MARKER,
            "## 监控范围概览",
            "动态内容",
            SECTION_END_MARKER,
        ]
    )


def test_index_contains_monitored_repo_markers() -> None:
    """首页模板必须保留动态同步标记。"""
    index_path = Path(__file__).resolve().parents[2] / "docs" / "index.md"
    content = index_path.read_text(encoding="utf-8")

    assert SECTION_START_MARKER in content
    assert SECTION_END_MARKER in content
    assert "[查看完整监控仓库清单](monitored-repos.md)" in content
