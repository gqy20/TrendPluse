"""格式化工具模块

提供报告和通知生成器使用的公共格式化函数。
"""

from trendpluse.models.signal import Signal


def format_source_url(url: str) -> str:
    """格式化 GitHub URL 显示文本

    提取并格式化 GitHub URL 中的关键信息（commit SHA 或 PR 号码）。

    Args:
        url: GitHub URL

    Returns:
        格式化的显示文本（包含 commit SHA 或 PR 号码）

    Examples:
        >>> format_source_url("https://github.com/owner/repo/commit/abc123def")
        'owner/repo@abc123d'
        >>> format_source_url("https://github.com/owner/repo/pull/42")
        'owner/repo#42'
        >>> format_source_url("https://github.com/owner/repo")
        'owner/repo'
    """
    if "github.com/" in url:
        # 移除协议前缀
        clean_url = url.replace("https://github.com/", "").replace(
            "http://github.com/", ""
        )

        # 检测 commit 链接
        if "/commit/" in clean_url:
            parts = clean_url.split("/commit/")
            repo = parts[0]
            # 移除查询参数和片段标识符
            sha_part = parts[1].split("?")[0].split("#")[0]
            # 显示前 7 位（如果 SHA 足够长）或全部
            short_sha = sha_part[:7] if len(sha_part) >= 7 else sha_part
            return f"{repo}@{short_sha}"

        # 检测 PR 链接
        elif "/pull/" in clean_url:
            parts = clean_url.split("/pull/")
            repo = parts[0]
            pr_num = parts[1].split("/")[0]
            return f"{repo}#{pr_num}"

        # 默认：提取仓库名
        else:
            parts = clean_url.split("/")
            if len(parts) >= 2:
                return f"{parts[0]}/{parts[1]}"

    return "链接"


def filter_high_impact(signals: list[Signal], threshold: int = 4) -> list[Signal]:
    """筛选高影响信号

    Args:
        signals: 信号列表
        threshold: 影响评分阈值（默认 4）

    Returns:
        高影响信号列表

    Examples:
        >>> from trendpluse.models.signal import Signal
        >>> signals = [
        ...     Signal(id="1", title="低影响", type="capability", category="engineering",
        ...           impact_score=2, why_it_matters="x", sources=[], related_repos=[]),
        ...     Signal(id="2", title="高影响", type="capability", category="engineering",
        ...           impact_score=5, why_it_matters="x", sources=[], related_repos=[]),
        ... ]
        >>> filtered = filter_high_impact(signals, threshold=4)
        >>> len(filtered)
        1
        >>> filtered[0].title
        '高影响'
    """
    return [s for s in signals if s.impact_score >= threshold]


def get_impact_emoji(impact: str) -> str:
    """获取 Breaking Changes 影响等级的表情

    Args:
        impact: 影响等级 (high/medium/low)

    Returns:
        对应的表情符号

    Examples:
        >>> get_impact_emoji("high")
        '🔴'
        >>> get_impact_emoji("medium")
        '🟡'
        >>> get_impact_emoji("unknown")
        '⚪'
    """
    emoji_map = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    return emoji_map.get(impact, "⚪")


def get_release_type_emoji(version: str, assets_count: int) -> str:
    """获取 Release 版本类型的表情

    Args:
        version: 版本号
        assets_count: 资产数量

    Returns:
        对应的表情符号

    Examples:
        >>> get_release_type_emoji("v2.0.0", 0)
        '🚀'
        >>> get_release_type_emoji("v1.2.3", 3)
        '⚡'
        >>> get_release_type_emoji("v1.2.4", 0)
        '📦'
    """
    # 主版本升级（如 v1.0.0 到 v2.0.0）
    if version.startswith("v") and ".0.0" in version:
        return "🚀"
    # 有资产的版本
    if assets_count > 0:
        return "⚡"
    # 其他版本
    return "📦"
