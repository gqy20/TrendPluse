"""项目发现集成测试

测试完整的项目发现流程。
"""

import json
from datetime import UTC, datetime
from unittest.mock import Mock, patch

import pytest

from trendpluse.app.discovery import discover, load_monitored_repos
from trendpluse.models.discovery import DiscoveredProject


def _build_project(**overrides) -> DiscoveredProject:
    """构造测试用发现项目。"""
    defaults = {
        "repo": "owner/project",
        "name": "project",
        "description": "Test project",
        "stars": 1000,
        "language": "Python",
        "topics": ["ai"],
        "license": "MIT",
        "open_issues": 10,
        "forks": 20,
        "watchers": 10,
        "last_commit_at": datetime.now(UTC),
        "discovery_source": "trending",
        "discovery_reason": "Trending",
    }
    defaults.update(overrides)
    return DiscoveredProject(**defaults)


def _build_highlight_settings(**overrides) -> Mock:
    """构造 discovery 用的 settings mock。"""
    settings = Mock(
        anthropic_api_key="",
        anthropic_model="glm-4.7",
        anthropic_base_url="",
        llm_retry_max_attempts=3,
        llm_retry_wait_min=1,
        llm_retry_wait_max=10,
    )
    for key, value in overrides.items():
        setattr(settings, key, value)
    return settings


class TestDiscoverProjectsIntegration:
    """项目发现集成测试"""

    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_discover_full_workflow(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        tmp_path,
    ):
        """测试完整发现流程"""
        # Mock 已监控仓库
        mock_load_monitored.return_value = {"owner/monitored"}

        # Mock Trending 结果
        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = [
            _build_project(
                repo="owner/trending1",
                name="trending1",
                description="Trending project 1",
                stars=3000,
                open_issues=20,
                forks=100,
                watchers=50,
            ),
            _build_project(
                repo="owner/monitored",  # 已监控
                name="monitored",
                description="Already monitored",
                stars=5000,
                topics=[],
                open_issues=10,
                forks=50,
                watchers=20,
            ),
        ]

        # Mock Keyword 结果
        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = [
            _build_project(
                repo="owner/keyword1",
                name="keyword1",
                description="Keyword project 1",
                stars=2000,
                language="TypeScript",
                topics=["web"],
                license="Apache-2.0",
                open_issues=10,
                forks=30,
                watchers=15,
                discovery_source="keyword",
                discovery_reason="Keyword: AI",
            ),
        ]

        # 执行发现
        report = discover(
            github_token="test_token",
            languages=["python"],
            keywords=["AI"],
            min_quality_score=50.0,
            days=30,
            output_dir=tmp_path,
        )

        # 验证报告
        assert report.total_discovered == 3
        assert report.already_monitored == 1
        assert len(report.candidates) == 2  # 去重后剩余 2 个

    def test_load_monitored_repos(self):
        """测试加载已监控仓库"""
        repos = load_monitored_repos()

        assert isinstance(repos, set)
        # 应该包含一些默认仓库（如果有的话）
        for repo in repos:
            assert "/" in repo

    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_saves_reports_to_files(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        tmp_path,
    ):
        """测试保存报告到文件"""
        mock_load_monitored.return_value = set()

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = []

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = []

        discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        # 检查文件已创建
        md_files = list(tmp_path.glob("*.md"))
        json_files = list(tmp_path.glob("*.json"))
        actionable_files = list(tmp_path.glob("*-actionable.json"))

        assert len(md_files) == 1
        assert len(json_files) == 2
        assert len(actionable_files) == 1

        # 验证文件内容
        md_content = md_files[0].read_text()
        assert "# 项目发现报告" in md_content

        base_report_file = next(
            file for file in json_files if not file.name.endswith("-actionable.json")
        )
        json_content = json.loads(base_report_file.read_text())
        assert "date" in json_content
        assert "candidates" in json_content

    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_handles_empty_discovery(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        tmp_path,
    ):
        """测试处理空发现结果"""
        mock_load_monitored.return_value = set()

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = []

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = []

        report = discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        assert report.total_discovered == 0
        assert report.passed_quality == 0
        assert len(report.candidates) == 0

    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_deduplicates_across_sources(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        tmp_path,
    ):
        """测试跨来源去重"""
        mock_load_monitored.return_value = set()

        # 同一个项目来自不同来源
        project = _build_project(
            repo="owner/duplicate",
            name="duplicate",
            description="Duplicate project",
            open_issues=5,
            forks=20,
            watchers=10,
        )

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = [project]

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        # 关键词也返回同一个项目（不同来源）
        duplicate_project = _build_project(
            repo="owner/duplicate",
            name="duplicate",
            description="From keyword search",
            stars=1100,
            open_issues=5,
            forks=22,
            watchers=11,
            discovery_source="keyword",
            discovery_reason="Keyword: AI",
        )
        mock_keyword.discover.return_value = [duplicate_project]

        report = discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        # 应该去重，只剩 1 个
        assert len(report.candidates) == 1
        assert report.duplicates_removed == 1

    @patch("trendpluse.app.discovery.get_settings")
    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_saves_actionable_candidates_file(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        mock_get_settings,
        tmp_path,
    ):
        """测试：保存可执行候选清单（仅 high/medium）"""
        mock_load_monitored.return_value = set()
        mock_get_settings.return_value = _build_highlight_settings()

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = [
            _build_project(
                repo="owner/high-priority",
                name="high-priority",
                description="AI agent project",
                stars=15000,
                topics=["agent", "ai"],
                open_issues=20,
                forks=800,
                watchers=100,
            )
        ]

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = [
            _build_project(
                repo="owner/low-priority",
                name="low-priority",
                description="",
                stars=10,
                language="Unknown",
                topics=[],
                license=None,
                open_issues=0,
                forks=0,
                watchers=0,
                last_commit_at=None,
                discovery_source="keyword",
                discovery_reason="Keyword: test",
            )
        ]

        discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        actionable_files = list(tmp_path.glob("discovery-*-actionable.json"))
        assert len(actionable_files) == 1

        data = json.loads(actionable_files[0].read_text(encoding="utf-8"))
        assert "candidates" in data
        assert len(data["candidates"]) == 1
        assert data["candidates"][0]["repo"] == "owner/high-priority"

    @patch("trendpluse.app.discovery.get_settings")
    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_actionable_candidates_respect_default_limit_10(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        mock_get_settings,
        tmp_path,
    ):
        """测试：actionable 默认最多输出 10 个"""
        mock_load_monitored.return_value = set()
        mock_get_settings.return_value = _build_highlight_settings()

        # 生成 12 个高优先级候选，默认应只输出 10 个
        trending_projects = []
        for i in range(12):
            trending_projects.append(
                _build_project(
                    repo=f"owner/high-{i}",
                    name=f"high-{i}",
                    description="AI agent project",
                    stars=12000 - i * 100,
                    topics=["agent", "ai"],
                    open_issues=10,
                    forks=200,
                    watchers=50,
                )
            )

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = trending_projects

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = []

        discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        actionable_file = next(tmp_path.glob("discovery-*-actionable.json"))
        data = json.loads(actionable_file.read_text(encoding="utf-8"))
        assert data["selected_count"] == 10
        assert len(data["candidates"]) == 10

    @patch("trendpluse.app.discovery.ProjectHighlightAnalyzer")
    @patch("trendpluse.app.discovery.get_settings")
    @patch("trendpluse.app.discovery.TrendingCollector")
    @patch("trendpluse.app.discovery.KeywordSearcher")
    @patch("trendpluse.app.discovery.load_monitored_repos")
    def test_highlight_analysis_respects_default_limit_10(
        self,
        mock_load_monitored,
        mock_keyword_searcher,
        mock_trending_collector,
        mock_get_settings,
        mock_highlight_analyzer,
        tmp_path,
    ):
        """测试：AI 亮点分析默认最多分析 10 个项目"""
        mock_load_monitored.return_value = set()
        mock_get_settings.return_value = _build_highlight_settings(
            anthropic_api_key="test-key",
        )

        trending_projects = []
        for i in range(15):
            trending_projects.append(
                _build_project(
                    repo=f"owner/high-highlight-{i}",
                    name=f"high-highlight-{i}",
                    description="AI agent project",
                    stars=15000 - i * 50,
                    topics=["agent", "ai"],
                    open_issues=10,
                    forks=300,
                    watchers=100,
                )
            )

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = trending_projects

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = []

        analyzer_instance = Mock()
        analyzer_instance.analyze_batch.return_value = {}
        mock_highlight_analyzer.return_value = analyzer_instance

        discover(
            github_token="test_token",
            output_dir=tmp_path,
        )

        analyze_args = analyzer_instance.analyze_batch.call_args[0][0]
        assert len(analyze_args) == 10


@pytest.mark.integration
@pytest.mark.skip(reason="需要真实 GitHub API")
class TestDiscoverProjectsRealAPI:
    """真实 API 集成测试"""

    def test_discover_with_real_api(self, tmp_path):
        """测试真实 API 发现"""
        import os

        from trendpluse.models.discovery import DiscoveryReport

        token = os.getenv("GITHUB_TOKEN")
        if not token:
            pytest.skip("GITHUB_TOKEN not set")

        # 类型断言：token 在此时非 None
        assert token is not None
        report = discover(
            github_token=token,
            languages=["python"],
            keywords=["test"],
            days=7,
            min_quality_score=50.0,
            output_dir=tmp_path,
        )

        assert isinstance(report, DiscoveryReport)
        assert report.total_discovered >= 0
