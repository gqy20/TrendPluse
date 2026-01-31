"""项目发现集成测试

测试完整的项目发现流程。
"""

from datetime import UTC, datetime
from unittest.mock import Mock, patch

import pytest

from scripts.discover_projects import discover, load_monitored_repos
from trendpluse.models.discovery import DiscoveredProject


class TestDiscoverProjectsIntegration:
    """项目发现集成测试"""

    @patch("scripts.discover_projects.TrendingCollector")
    @patch("scripts.discover_projects.KeywordSearcher")
    @patch("scripts.discover_projects.load_monitored_repos")
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
            DiscoveredProject(
                repo="owner/trending1",
                name="trending1",
                description="Trending project 1",
                stars=3000,
                language="Python",
                topics=["ai"],
                license="MIT",
                open_issues=20,
                forks=100,
                watchers=50,
                last_commit_at=datetime.now(UTC),
                discovery_source="trending",
                discovery_reason="Trending",
            ),
            DiscoveredProject(
                repo="owner/monitored",  # 已监控
                name="monitored",
                description="Already monitored",
                stars=5000,
                language="Python",
                topics=[],
                license="MIT",
                open_issues=10,
                forks=50,
                watchers=20,
                last_commit_at=datetime.now(UTC),
                discovery_source="trending",
                discovery_reason="Trending",
            ),
        ]

        # Mock Keyword 结果
        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        mock_keyword.discover.return_value = [
            DiscoveredProject(
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
                last_commit_at=datetime.now(UTC),
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

    @patch("scripts.discover_projects.TrendingCollector")
    @patch("scripts.discover_projects.KeywordSearcher")
    @patch("scripts.discover_projects.load_monitored_repos")
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

        assert len(md_files) == 1
        assert len(json_files) == 1

        # 验证文件内容
        md_content = md_files[0].read_text()
        assert "# 项目发现报告" in md_content

        import json

        json_content = json.loads(json_files[0].read_text())
        assert "date" in json_content
        assert "candidates" in json_content

    @patch("scripts.discover_projects.TrendingCollector")
    @patch("scripts.discover_projects.KeywordSearcher")
    @patch("scripts.discover_projects.load_monitored_repos")
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

    @patch("scripts.discover_projects.TrendingCollector")
    @patch("scripts.discover_projects.KeywordSearcher")
    @patch("scripts.discover_projects.load_monitored_repos")
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
        project = DiscoveredProject(
            repo="owner/duplicate",
            name="duplicate",
            description="Duplicate project",
            stars=1000,
            language="Python",
            topics=["ai"],
            license="MIT",
            open_issues=5,
            forks=20,
            watchers=10,
            last_commit_at=datetime.now(UTC),
            discovery_source="trending",
            discovery_reason="Trending",
        )

        mock_trending = Mock()
        mock_trending_collector.return_value = mock_trending
        mock_trending.discover.return_value = [project]

        mock_keyword = Mock()
        mock_keyword_searcher.return_value = mock_keyword
        # 关键词也返回同一个项目（不同来源）
        duplicate_project = DiscoveredProject(
            repo="owner/duplicate",
            name="duplicate",
            description="From keyword search",
            stars=1100,
            language="Python",
            topics=["ai"],
            license="MIT",
            open_issues=5,
            forks=22,
            watchers=11,
            last_commit_at=datetime.now(UTC),
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
