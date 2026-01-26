"""测试格式化工具模块"""

from trendpluse.models.signal import Signal
from trendpluse.utils.formatters import (
    filter_high_impact,
    format_source_url,
    get_impact_emoji,
    get_release_type_emoji,
)


class TestFormatSourceUrl:
    """测试 GitHub URL 格式化"""

    def test_formats_commit_url(self):
        """应该格式化 commit URL 为 repo@sha 格式"""
        url = "https://github.com/anthropics/claude-code/commit/abc123def456"
        result = format_source_url(url)
        assert result == "anthropics/claude-code@abc123d"

    def test_formats_pull_request_url(self):
        """应该格式化 PR URL 为 repo#number 格式"""
        url = "https://github.com/anthropics/claude-code/pull/42"
        result = format_source_url(url)
        assert result == "anthropics/claude-code#42"

    def test_formats_plain_repo_url(self):
        """应该格式化普通仓库 URL"""
        url = "https://github.com/anthropics/claude-code"
        result = format_source_url(url)
        assert result == "anthropics/claude-code"

    def test_returns_link_for_unknown_format(self):
        """未知格式应该返回 '链接'"""
        url = "https://example.com/page"
        result = format_source_url(url)
        assert result == "链接"

    def test_handles_commit_url_with_query_params(self):
        """应该正确处理带查询参数的 commit URL"""
        url = "https://github.com/owner/repo/commit/abc123?diff=unified"
        result = format_source_url(url)
        # SHA 只有 6 位，应该全部显示
        assert result == "owner/repo@abc123"

    def test_handles_http_url(self):
        """应该正确处理 HTTP URL"""
        url = "http://github.com/owner/repo/commit/abc123"
        result = format_source_url(url)
        # SHA 只有 6 位，应该全部显示
        assert result == "owner/repo@abc123"


class TestFilterHighImpact:
    """测试高影响信号筛选"""

    def test_filters_signals_by_impact_score(self):
        """应该根据影响评分筛选信号"""
        signals = [
            Signal(
                id="1",
                title="低影响",
                type="capability",
                category="engineering",
                impact_score=2,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
            Signal(
                id="2",
                title="高影响",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
            Signal(
                id="3",
                title="中等影响",
                type="capability",
                category="engineering",
                impact_score=4,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
        ]

        result = filter_high_impact(signals, threshold=4)

        assert len(result) == 2
        assert {s.title for s in result} == {"高影响", "中等影响"}

    def test_returns_empty_list_when_no_signals_meet_threshold(self):
        """没有信号达到阈值时应该返回空列表"""
        signals = [
            Signal(
                id="1",
                title="低影响",
                type="capability",
                category="engineering",
                impact_score=1,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
        ]

        result = filter_high_impact(signals, threshold=4)

        assert result == []

    def test_returns_empty_list_for_empty_input(self):
        """空输入应该返回空列表"""
        result = filter_high_impact([])
        assert result == []

    def test_respects_custom_threshold(self):
        """应该使用自定义阈值"""
        signals = [
            Signal(
                id="1",
                title="信号1",
                type="capability",
                category="engineering",
                impact_score=3,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
            Signal(
                id="2",
                title="信号2",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="测试",
                sources=[],
                related_repos=[],
            ),
        ]

        result = filter_high_impact(signals, threshold=3)

        assert len(result) == 2
        result = filter_high_impact(signals, threshold=5)

        assert len(result) == 1
        assert result[0].title == "信号2"


class TestGetImpactEmoji:
    """测试 Breaking Changes 影响 emoji 获取"""

    def test_returns_red_emoji_for_high_impact(self):
        """高影响应该返回红色圆圈"""
        assert get_impact_emoji("high") == "🔴"

    def test_returns_yellow_emoji_for_medium_impact(self):
        """中等影响应该返回黄色圆圈"""
        assert get_impact_emoji("medium") == "🟡"

    def test_returns_green_emoji_for_low_impact(self):
        """低影响应该返回绿色圆圈"""
        assert get_impact_emoji("low") == "🟢"

    def test_returns_white_emoji_for_unknown_impact(self):
        """未知影响应该返回白色圆圈"""
        assert get_impact_emoji("unknown") == "⚪"
        assert get_impact_emoji("critical") == "⚪"
        assert get_impact_emoji("") == "⚪"


class TestGetReleaseTypeEmoji:
    """测试 Release 版本类型 emoji 获取"""

    def test_returns_rocket_for_major_version(self):
        """主版本升级应该返回火箭"""
        assert get_release_type_emoji("v2.0.0", 0) == "🚀"
        assert get_release_type_emoji("v1.0.0", 5) == "🚀"

    def test_returns_bolt_for_release_with_assets(self):
        """有资产的版本应该返回闪电"""
        assert get_release_type_emoji("v1.2.3", 3) == "⚡"
        assert get_release_type_emoji("v2.1.0", 1) == "⚡"

    def test_returns_package_for_patch_version(self):
        """补丁版本应该返回包裹"""
        assert get_release_type_emoji("v1.2.4", 0) == "📦"
        assert get_release_type_emoji("v1.0.1", 0) == "📦"

    def test_handles_non_standard_version_format(self):
        """非标准版本格式应该返回包裹"""
        assert get_release_type_emoji("1.0.0", 0) == "📦"
        assert get_release_type_emoji("latest", 5) == "⚡"
