"""Discovery 模块基础测试。"""

import pytest

from trendpluse.models.discovery import DiscoveredProject, DiscoveryReport


class TestDiscoveredProject:
    """DiscoveredProject 模型测试"""

    def test_create_minimal_project(self):
        """测试创建最小项目模型"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="test-repo",
            description="A test repository",
            stars=1000,
            language="Python",
            discovery_source="trending",
            discovery_reason="Test project",
        )

        assert project.repo == "owner/repo"
        assert project.name == "test-repo"
        assert project.stars == 1000
        assert project.quality_score == 0  # 默认值

    def test_project_with_growth_metrics(self):
        """测试带增长指标的项目"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="test-repo",
            description="A test repository",
            stars=5000,
            stars_growth_7d=500,
            stars_growth_30d=1500,
            language="Python",
            discovery_source="keyword",
            discovery_reason="AI agent",
        )

        assert project.stars_growth_7d == 500
        assert project.stars_growth_30d == 1500

    def test_quality_score_validation(self):
        """测试质量评分范围验证"""
        with pytest.raises(ValueError):
            DiscoveredProject(
                repo="owner/repo",
                name="test-repo",
                description="Test",
                stars=100,
                language="Python",
                discovery_source="trending",
                discovery_reason="Test",
                quality_score=150,  # 超出范围
            )

    def test_activity_level_validation(self):
        """测试活跃度等级验证"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="test-repo",
            description="Test",
            stars=100,
            language="Python",
            discovery_source="trending",
            discovery_reason="Test",
            activity_level="high",
        )

        assert project.activity_level == "high"

    def test_default_recommended_false(self):
        """测试默认不推荐"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="test-repo",
            description="Test",
            stars=100,
            language="Python",
            discovery_source="trending",
            discovery_reason="Test",
        )

        assert project.recommended is False
        assert project.recommendation_priority == "medium"


class TestDiscoveryReport:
    """DiscoveryReport 模型测试"""

    def test_create_empty_report(self):
        """测试创建空报告"""
        report = DiscoveryReport(
            date="2026-01-31",
            total_discovered=0,
            passed_quality=0,
            high_priority=0,
            candidates=[],
        )

        assert report.date == "2026-01-31"
        assert report.total_discovered == 0
        assert len(report.candidates) == 0

    def test_create_report_with_candidates(self):
        """测试带候选项目的报告"""
        candidates = [
            DiscoveredProject(
                repo=f"owner/repo{i}",
                name=f"repo-{i}",
                description=f"Repository {i}",
                stars=1000 * (i + 1),
                language="Python",
                discovery_source="trending",
                discovery_reason=f"Reason {i}",
            )
            for i in range(3)
        ]

        report = DiscoveryReport(
            date="2026-01-31",
            total_discovered=3,
            passed_quality=2,
            high_priority=1,
            candidates=candidates,
        )

        assert len(report.candidates) == 3
        assert report.total_discovered == 3

    def test_source_breakdown_calculation(self):
        """测试来源统计"""
        candidates = [
            DiscoveredProject(
                repo="owner/repo1",
                name="repo1",
                description="Test",
                stars=1000,
                language="Python",
                discovery_source="trending",
                discovery_reason="Test",
            ),
            DiscoveredProject(
                repo="owner/repo2",
                name="repo2",
                description="Test",
                stars=500,
                language="TypeScript",
                discovery_source="keyword",
                discovery_reason="AI agent",
            ),
        ]

        DiscoveryReport(
            date="2026-01-31",
            total_discovered=2,
            passed_quality=2,
            high_priority=0,
            candidates=candidates,
        )

        # 手动计算来源统计
        source_count: dict[str, int] = {}
        for c in candidates:
            source_count[c.discovery_source] = (
                source_count.get(c.discovery_source, 0) + 1
            )

        assert source_count["trending"] == 1
        assert source_count["keyword"] == 1


@pytest.mark.integration
@pytest.mark.skip(reason="TrendingCollector 尚未实现，将在 Phase 2 实现")
class TestDiscoveryIntegration:
    """集成测试（需要 GitHub API）"""

    @pytest.fixture
    def real_github_token(self):
        """获取真实的 GitHub token"""
        import os

        token = os.getenv("GITHUB_TOKEN")
        if not token:
            pytest.skip("GITHUB_TOKEN not set for integration test")
        return token

    def test_discover_with_real_api(self, real_github_token):
        """测试使用真实 API 发现项目"""
        # 这个测试需要真实的 GitHub token，只在 CI 环境运行
        # TrendingCollector 将在 Phase 2 实现
        from trendpluse.discovery import trending

        collector = trending.TrendingCollector(github_token=real_github_token)
        results = collector.discover(languages=["python"], days=30)

        # 验证返回结果
        assert isinstance(results, list)
        assert len(results) > 0

        # 验证第一个结果的格式
        first = results[0]
        assert isinstance(first, DiscoveredProject)
        assert "/" in first.repo
        assert first.stars > 0
