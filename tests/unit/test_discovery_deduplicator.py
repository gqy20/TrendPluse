"""Deduplicator 测试

测试项目去重功能。
"""

from datetime import datetime, timedelta

import pytest

from trendpluse.discovery.deduplicator import Deduplicator
from trendpluse.discovery.evaluator import QualityEvaluator
from trendpluse.models.discovery import DiscoveredProject


class TestDeduplicator:
    """Deduplicator 测试"""

    @pytest.fixture
    def sample_projects(self):
        """示例项目列表（包含重复）"""
        projects = [
            DiscoveredProject(
                repo="owner/repo1",
                name="repo1",
                description="First occurrence",
                stars=1000,
                language="Python",
                topics=["ai"],
                license="MIT",
                open_issues=10,
                forks=50,
                watchers=20,
                last_commit_at=datetime.now() - timedelta(days=5),
                discovery_source="trending",
                discovery_reason="Trending",
            ),
            DiscoveredProject(
                repo="owner/repo1",  # 重复
                name="repo1",
                description="Second occurrence",
                stars=1100,  # 更新的 star 数
                language="Python",
                topics=["ai", "ml"],  # 更多 topics
                license="MIT",
                open_issues=12,
                forks=55,
                watchers=22,
                last_commit_at=datetime.now() - timedelta(days=3),
                discovery_source="keyword",
                discovery_reason="Keyword: AI",
            ),
            DiscoveredProject(
                repo="owner/repo2",
                name="repo2",
                description="Unique repo",
                stars=2000,
                language="TypeScript",
                topics=["web"],
                license="Apache-2.0",
                open_issues=5,
                forks=30,
                watchers=15,
                last_commit_at=datetime.now() - timedelta(days=10),
                discovery_source="keyword",
                discovery_reason="Keyword: web",
            ),
            DiscoveredProject(
                repo="other/repo1",
                name="repo1",
                description="Different owner",
                stars=500,
                language="Python",
                topics=[],
                license=None,
                open_issues=0,
                forks=5,
                watchers=2,
                last_commit_at=datetime.now() - timedelta(days=1),
                discovery_source="trending",
                discovery_reason="Trending",
            ),
        ]
        # 先通过质量评估器评分，使去重有依据
        evaluator = QualityEvaluator()
        return evaluator.evaluate(projects)

    def test_deduplicate_removes_duplicate_repos(self, sample_projects):
        """测试去重移除重复仓库"""
        deduplicator = Deduplicator()
        result = deduplicator.deduplicate(sample_projects)

        # 4 个输入，2 个 owner/repo1 重复，应该剩 3 个
        assert len(result) == 3

    def test_deduplicate_keeps_highest_quality(self, sample_projects):
        """测试去重保留质量分数最高的"""
        deduplicator = Deduplicator()
        result = deduplicator.deduplicate(sample_projects)

        repo1 = next(p for p in result if p.repo == "owner/repo1")
        # 应该保留有质量分数的（第二次出现）
        assert repo1.quality_score > 0

    def test_deduplicate_combines_discovery_sources(self, sample_projects):
        """测试去重合并发现来源"""
        deduplicator = Deduplicator()
        result = deduplicator.deduplicate(sample_projects)

        repo1 = next(p for p in result if p.repo == "owner/repo1")
        # 应该在 discovery_reason 中包含多个来源信息
        assert "[" in repo1.discovery_reason
        assert (
            "trending" in repo1.discovery_reason.lower()
            or "keyword" in str(repo1.discovery_reason).lower()
        )

    def test_deduplicate_empty_list(self):
        """测试空列表处理"""
        deduplicator = Deduplicator()
        result = deduplicator.deduplicate([])

        assert result == []

    def test_deduplicate_single_project(self):
        """测试单个项目处理"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="Test",
            stars=100,
            language="Python",
            topics=[],
            license=None,
            open_issues=0,
            forks=1,
            watchers=1,
            last_commit_at=datetime.now(),
            discovery_source="trending",
            discovery_reason="Test",
        )

        deduplicator = Deduplicator()
        result = deduplicator.deduplicate([project])

        assert len(result) == 1
        assert result[0].repo == "owner/repo"

    def test_deduplicate_all_unique(self):
        """测试全部唯一项目"""
        projects = [
            DiscoveredProject(
                repo=f"owner/repo{i}",
                name=f"repo{i}",
                description=f"Test {i}",
                stars=100 * i,
                language="Python",
                topics=[],
                license=None,
                open_issues=0,
                forks=1,
                watchers=1,
                last_commit_at=datetime.now(),
                discovery_source="keyword",
                discovery_reason=f"Keyword{i}",
            )
            for i in range(5)
        ]

        deduplicator = Deduplicator()
        result = deduplicator.deduplicate(projects)

        assert len(result) == 5

    def test_deduplicate_returns_count(self, sample_projects):
        """测试返回去重计数"""
        deduplicator = Deduplicator()
        result, count = deduplicator.deduplicate_with_count(sample_projects)

        assert count == 1  # 移除了 1 个重复
        assert len(result) == 3

    def test_deduplicate_preserves_best_attributes(self, sample_projects):
        """测试去重保留最佳属性"""
        deduplicator = Deduplicator()
        result = deduplicator.deduplicate(sample_projects)

        repo1 = next(p for p in result if p.repo == "owner/repo1")
        # 应该保留最新的 star 数
        assert repo1.stars == 1100
