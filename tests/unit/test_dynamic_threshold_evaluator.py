"""动态阈值评估器测试

测试 DynamicThresholdEvaluator 的功能。
"""

from datetime import UTC, datetime, timedelta

import pytest

from trendpluse.discovery.dynamic_evaluator import DynamicThresholdEvaluator
from trendpluse.models.discovery import DiscoveredProject


class TestDynamicThresholdEvaluator:
    """动态阈值评估器测试"""

    @pytest.fixture
    def sample_projects(self):
        """创建示例项目列表（不同质量水平）"""
        projects = []
        now = datetime.now(UTC)

        # 高质量项目（高 stars、高活跃度、完整元数据）
        for i in range(4):
            project = DiscoveredProject(
                repo=f"test/high-{i}",
                name=f"high-{i}",
                description=f"High quality project {i} with AI and LLM features",
                stars=50000 - i * 5000,  # 50000, 45000, 40000, 35000
                language="Python",
                topics=["ai", "llm", "agent", "rag"],
                license="MIT",
                open_issues=50,
                forks=5000 - i * 500,
                watchers=50000 - i * 5000,
                last_commit_at=now - timedelta(days=i),  # 最近活跃
                discovery_source="trending",
                discovery_reason=f"High quality AI project {i}",
            )
            projects.append(project)

        # 中等质量项目
        for i in range(5):
            project = DiscoveredProject(
                repo=f"test/medium-{i}",
                name=f"medium-{i}",
                description=f"Medium quality project {i}",
                stars=5000 - i * 500,
                language="Python",
                topics=["ai"],
                license="MIT",
                open_issues=100,
                forks=500 - i * 50,
                watchers=5000 - i * 500,
                last_commit_at=now - timedelta(days=15 + i * 5),
                discovery_source="keyword",
                discovery_reason=f"Medium project {i}",
            )
            projects.append(project)

        # 低质量项目（低 stars、较少活跃）
        for i in range(4):
            project = DiscoveredProject(
                repo=f"test/low-{i}",
                name=f"low-{i}",
                description=f"Lower quality project {i}",
                stars=800 - i * 100,
                language="JavaScript",
                topics=["web"],
                license=None,  # 无许可证
                open_issues=200,
                forks=50,
                watchers=800,
                last_commit_at=now - timedelta(days=60 + i * 10),
                discovery_source="keyword",
                discovery_reason=f"Lower project {i}",
            )
            projects.append(project)

        return projects

    def test_calculate_percentile_thresholds(self):
        """测试百分位阈值计算"""
        scores: list[float] = [95, 90, 88, 85, 83, 80, 78, 75, 72, 70, 68, 65, 60]
        evaluator = DynamicThresholdEvaluator()

        high_threshold, medium_threshold = evaluator._calculate_percentile_thresholds(
            scores
        )

        # 前 30% (13 * 0.3 = 3.9 → 索引 3) 为 85
        assert high_threshold == 85.0

        # 前 70% (13 * 0.7 = 9.1 → 索引 9) 为 70
        assert medium_threshold == 70.0

    def test_evaluate_sets_priorities_by_distribution(self, sample_projects):
        """测试评估器按分布设置优先级

        验证：
        - 高优先级阈值高于中优先级阈值
        - 所有项目都被正确分类
        - 分数高的项目优先级也高
        """
        evaluator = DynamicThresholdEvaluator(min_quality_score=40.0)
        evaluated = evaluator.evaluate(sample_projects)

        # 验证阈值被正确设置
        assert evaluator.last_high_threshold is not None
        assert evaluator.last_medium_threshold is not None
        assert evaluator.last_high_threshold > evaluator.last_medium_threshold

        # 验证所有项目都被分类
        high_priority = [p for p in evaluated if p.recommendation_priority == "high"]
        medium_priority = [
            p for p in evaluated if p.recommendation_priority == "medium"
        ]
        low_priority = [p for p in evaluated if p.recommendation_priority == "low"]
        assert len(high_priority) + len(medium_priority) + len(low_priority) == len(
            evaluated
        )

        # 验证高优先级项目的分数都 >= 阈值
        if high_priority and evaluator.last_high_threshold is not None:
            for p in high_priority:
                assert p.quality_score >= evaluator.last_high_threshold

        # 验证中优先级项目的分数在阈值之间
        if medium_priority and evaluator.last_medium_threshold is not None:
            for p in medium_priority:
                assert (
                    evaluator.last_medium_threshold
                    <= p.quality_score
                    < evaluator.last_high_threshold
                )

        # 验证低优先级项目的分数 < 中优先级阈值
        if low_priority and evaluator.last_medium_threshold is not None:
            for p in low_priority:
                assert p.quality_score < evaluator.last_medium_threshold

    def test_thresholds_are_calculated_and_stored(self, sample_projects):
        """测试阈值被正确计算和存储"""
        evaluator = DynamicThresholdEvaluator()
        evaluator.evaluate(sample_projects)

        # 验证阈值被计算并存储
        assert evaluator.last_high_threshold is not None
        assert evaluator.last_medium_threshold is not None
        assert evaluator.last_high_threshold > evaluator.last_medium_threshold

    def test_evaluate_with_small_sample(self):
        """测试小样本评估"""
        projects = []
        now = datetime.now(UTC)
        for i in range(3):
            project = DiscoveredProject(
                repo=f"test/repo-{i}",
                name=f"repo-{i}",
                description=f"Test {i}",
                stars=10000 - i * 2000,
                language="Python",
                topics=["ai"],
                license="MIT",
                open_issues=10,
                forks=500,
                watchers=10000,
                last_commit_at=now - timedelta(days=i),
                discovery_source="trending",
                discovery_reason=f"Test {i}",
            )
            projects.append(project)

        evaluator = DynamicThresholdEvaluator()
        evaluated = evaluator.evaluate(projects)

        # 小样本也应该正确分类
        priorities = [p.recommendation_priority for p in evaluated]
        assert "high" in priorities

        # 验证阈值被设置
        assert evaluator.last_high_threshold is not None

    def test_custom_percentiles(self):
        """测试自定义百分位"""
        projects = []
        now = datetime.now(UTC)
        for i in range(20):
            project = DiscoveredProject(
                repo=f"test/repo-{i}",
                name=f"repo-{i}",
                description="Test",
                stars=20000 - i * 1000,
                language="Python",
                topics=["ai"],
                license="MIT",
                open_issues=10,
                forks=2000,
                watchers=20000,
                last_commit_at=now - timedelta(days=i // 2),
                discovery_source="trending",
                discovery_reason="Test",
            )
            projects.append(project)

        # 自定义百分位: 前 20% high, 前 60% medium
        evaluator = DynamicThresholdEvaluator(
            high_percentile=0.2,
            medium_percentile=0.6,
        )
        evaluated = evaluator.evaluate(projects)

        # 验证自定义百分位被应用
        assert evaluator.last_high_threshold is not None
        assert evaluator.last_medium_threshold is not None

        # 验证阈值关系
        assert evaluator.last_high_threshold > evaluator.last_medium_threshold

        # 验证至少有一些高优先级项目
        high_count = sum(1 for p in evaluated if p.recommendation_priority == "high")
        assert high_count > 0

    def test_quality_scores_are_calculated(self, sample_projects):
        """测试质量分数被正确计算"""
        evaluator = DynamicThresholdEvaluator()
        evaluated = evaluator.evaluate(sample_projects)

        # 验证所有项目都有质量分数
        for project in evaluated:
            assert 0 <= project.quality_score <= 100
            assert project.activity_level in ("high", "medium", "low")

        # 高质量项目应该有更高的分数
        high_projects = [p for p in evaluated if p.stars >= 30000]
        low_projects = [p for p in evaluated if p.stars < 2000]

        if high_projects and low_projects:
            avg_high = sum(p.quality_score for p in high_projects) / len(high_projects)
            avg_low = sum(p.quality_score for p in low_projects) / len(low_projects)
            assert avg_high > avg_low
