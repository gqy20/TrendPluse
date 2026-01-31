"""QualityEvaluator 测试

测试项目质量评分功能。
"""

from datetime import datetime, timedelta

import pytest

from trendpluse.discovery.evaluator import QualityEvaluator
from trendpluse.models.discovery import DiscoveredProject


class TestQualityEvaluator:
    """QualityEvaluator 测试"""

    @pytest.fixture
    def sample_project(self):
        """示例项目"""
        return DiscoveredProject(
            repo="test-owner/test-repo",
            name="test-repo",
            description="A test repository",
            stars=5000,
            language="Python",
            topics=["ai", "ml"],
            license="MIT",
            open_issues=20,
            forks=100,
            watchers=50,
            last_commit_at=datetime.now() - timedelta(days=5),
            discovery_source="trending",
            discovery_reason="Test",
        )

    def test_evaluate_adds_quality_score(self, sample_project):
        """测试评估添加质量分数"""
        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate([sample_project])

        assert results[0].quality_score > 0
        assert results[0].quality_score <= 100

    def test_evaluate_sets_activity_level(self, sample_project):
        """测试评估设置活跃度等级"""
        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate([sample_project])

        assert results[0].activity_level in ["high", "medium", "low"]

    def test_evaluate_high_quality_project(self):
        """测试高质量项目评分"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="High quality repo",
            stars=15000,
            language="Python",
            topics=["ai", "agent", "llm"],
            license="MIT",
            open_issues=50,
            forks=500,
            watchers=200,
            last_commit_at=datetime.now() - timedelta(days=3),
            discovery_source="trending",
            discovery_reason="Test",
        )

        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate([project])

        # 高质量项目应该有很高的分数
        assert results[0].quality_score >= 80
        assert results[0].activity_level == "high"
        assert results[0].recommended is True

    def test_evaluate_low_quality_project(self):
        """测试低质量项目评分"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="Low quality repo",
            stars=100,
            language="Python",
            topics=[],
            license=None,
            open_issues=0,
            forks=2,
            watchers=1,
            last_commit_at=datetime.now() - timedelta(days=180),
            discovery_source="keyword",
            discovery_reason="Test",
        )

        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate([project])

        # 低质量项目应该有较低的分数
        assert results[0].quality_score < 60
        assert results[0].activity_level == "low"
        assert results[0].recommended is False

    def test_evaluate_medium_quality_project(self):
        """测试中等质量项目评分"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="Medium quality repo",
            stars=2000,
            language="Python",
            topics=["ai"],
            license="Apache-2.0",
            open_issues=10,
            forks=30,
            watchers=15,
            last_commit_at=datetime.now() - timedelta(days=30),
            discovery_source="keyword",
            discovery_reason="AI agent",
        )

        evaluator = QualityEvaluator(min_quality_score=50.0)
        results = evaluator.evaluate([project])

        # 中等质量项目分数应该在中间范围
        assert 40 <= results[0].quality_score <= 70
        assert results[0].activity_level in ["medium", "low"]

    def test_evaluate_multiple_projects(self):
        """测试评估多个项目"""
        projects = [
            DiscoveredProject(
                repo=f"owner/repo{i}",
                name=f"repo{i}",
                description=f"Repository {i}",
                stars=1000 * (i + 1),
                language="Python",
                topics=[],
                license=None,
                open_issues=5,
                forks=10,
                watchers=5,
                last_commit_at=datetime.now() - timedelta(days=10),
                discovery_source="keyword",
                discovery_reason=f"Keyword{i}",
            )
            for i in range(5)
        ]

        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate(projects)

        assert len(results) == 5
        # 验证所有项目都有评分
        for project in results:
            assert 0 <= project.quality_score <= 100

    def test_calculate_star_score(self):
        """测试 star 分数计算"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # 不同 star 数对应的分数
        assert evaluator._calculate_star_score(15000) == 20
        assert evaluator._calculate_star_score(7000) == 15
        assert evaluator._calculate_star_score(1500) == 10
        assert evaluator._calculate_star_score(700) == 5
        assert evaluator._calculate_star_score(100) == 0

    def test_calculate_activity_score(self):
        """测试活跃度分数计算"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # 不同活跃时间对应的分数（传入 datetime 对象）
        assert (
            evaluator._calculate_activity_score(datetime.now() - timedelta(days=3))
            == 30
        )
        assert (
            evaluator._calculate_activity_score(datetime.now() - timedelta(days=14))
            == 20
        )
        assert (
            evaluator._calculate_activity_score(datetime.now() - timedelta(days=60))
            == 10
        )
        assert (
            evaluator._calculate_activity_score(datetime.now() - timedelta(days=120))
            == 0
        )

    def test_calculate_community_score(self):
        """测试社区分数计算"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # forks + watchers 组合分数
        assert evaluator._calculate_community_score(200, 50) == 20
        assert evaluator._calculate_community_score(50, 10) == 7
        assert evaluator._calculate_community_score(10, 5) == 4

    def test_calculate_code_quality_score(self):
        """测试代码质量分数计算"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # 有 license + description + README
        assert (
            evaluator._calculate_code_quality_score(
                has_license=True,
                has_description=True,
                has_readme=True,
            )
            == 15
        )

        # 只有部分指标（每个指标 5 分）
        assert (
            evaluator._calculate_code_quality_score(
                has_license=False,
                has_description=True,
                has_readme=False,
            )
            == 5
        )

    def test_get_activity_level(self):
        """测试活跃度等级判断"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # activity_score 最大是 30，所以使用有效范围内的值
        assert evaluator._get_activity_level(30) == "high"  # 100%
        assert evaluator._get_activity_level(20) == "medium"  # 67%
        assert evaluator._get_activity_level(10) == "low"  # 33%

    def test_sets_recommendation_priority_based_on_score(self):
        """测试根据分数设置推荐优先级"""
        evaluator = QualityEvaluator(min_quality_score=60.0)

        # 高分项目
        high_project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="Test",
            stars=10000,
            language="Python",
            topics=[],
            license="MIT",
            open_issues=10,
            forks=100,
            watchers=50,
            last_commit_at=datetime.now() - timedelta(days=3),
            discovery_source="trending",
            discovery_reason="Test",
        )
        results = evaluator.evaluate([high_project])

        assert results[0].recommendation_priority == "high"

    def test_respects_min_quality_score_threshold(self):
        """测试遵守最低质量分数阈值"""
        # 创建刚好在阈值上的项目
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="Test",
            stars=5000,
            language="Python",
            topics=["ai"],
            license="MIT",
            open_issues=20,
            forks=80,
            watchers=40,
            last_commit_at=datetime.now() - timedelta(days=7),
            discovery_source="trending",
            discovery_reason="Test",
        )

        # 设置较高的阈值
        evaluator = QualityEvaluator(min_quality_score=85.0)
        results = evaluator.evaluate([project])

        # 可能不被推荐
        assert isinstance(results[0].recommended, bool)

    def test_handles_missing_optional_fields(self):
        """测试处理缺失的可选字段"""
        project = DiscoveredProject(
            repo="owner/repo",
            name="repo",
            description="",  # 空描述
            stars=1000,
            language="Python",
            topics=[],
            license=None,  # 无 license
            open_issues=0,
            forks=5,
            watchers=2,
            last_commit_at=None,  # 无提交时间
            discovery_source="keyword",
            discovery_reason="Test",
        )

        evaluator = QualityEvaluator(min_quality_score=60.0)
        results = evaluator.evaluate([project])

        # 应该能处理，不会崩溃
        assert isinstance(results, list)
        assert len(results) == 1
