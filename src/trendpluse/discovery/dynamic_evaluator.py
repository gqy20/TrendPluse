"""动态阈值质量评估器

根据项目分数分布动态计算优先级阈值。
"""

from trendpluse.discovery.evaluator import QualityEvaluator
from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)


class DynamicThresholdEvaluator(QualityEvaluator):
    """动态阈值质量评估器

    基于分数分布动态计算优先级阈值，避免固定阈值导致的偏态分布问题。

    默认配置:
    - 前 30% 项目为高优先级
    - 前 70% 项目为中优先级及以上
    - 剩余为低优先级

    Attributes:
        high_percentile: 高优先级百分位 (0-1)
        medium_percentile: 中优先级百分位 (0-1)
        last_high_threshold: 上次计算的高优先级阈值
        last_medium_threshold: 上次计算的中优先级阈值
    """

    def __init__(
        self,
        min_quality_score: float = 60.0,
        high_percentile: float = 0.3,
        medium_percentile: float = 0.7,
    ) -> None:
        """初始化动态阈值评估器

        Args:
            min_quality_score: 最低质量分数阈值
            high_percentile: 高优先级百分位 (0-1)，默认 0.3 (前 30%)
            medium_percentile: 中优先级百分位 (0-1)，默认 0.7 (前 70%)
        """
        super().__init__(min_quality_score=min_quality_score)
        self.high_percentile = high_percentile
        self.medium_percentile = medium_percentile
        self.last_high_threshold: float | None = None
        self.last_medium_threshold: float | None = None

    def _calculate_percentile_thresholds(
        self, scores: list[float]
    ) -> tuple[float, float]:
        """计算百分位阈值

        Args:
            scores: 质量分数列表

        Returns:
            (high_threshold, medium_threshold) 元组
        """
        if not scores:
            return 80.0, 60.0  # 默认阈值

        # 降序排序
        sorted_scores = sorted(scores, reverse=True)
        n = len(sorted_scores)

        # 计算百分位阈值（使用索引确保有界）
        high_idx = max(0, min(int(n * self.high_percentile), n - 1))
        medium_idx = max(0, min(int(n * self.medium_percentile), n - 1))

        high_threshold = sorted_scores[high_idx]
        medium_threshold = sorted_scores[medium_idx]

        return high_threshold, medium_threshold

    def set_priorities_only(
        self,
        candidates: list[DiscoveredProject],
    ) -> list[DiscoveredProject]:
        """仅设置优先级（不重新计算质量分数）

        用于已经有质量分数的情况，只重新计算优先级。

        Args:
            candidates: 已有质量分数的项目列表

        Returns:
            优先级已设置的项目列表
        """
        # 提取已有的质量分数
        scores = [p.quality_score for p in candidates if p.quality_score is not None]

        if not scores:
            logger.warning("没有有效的质量分数，无法计算动态阈值")
            return candidates

        # 计算动态阈值
        high_threshold, medium_threshold = self._calculate_percentile_thresholds(scores)

        self.last_high_threshold = high_threshold
        self.last_medium_threshold = medium_threshold

        logger.info(
            f"动态阈值计算完成: "
            f"高优先级 >= {high_threshold:.1f}, "
            f"中优先级 >= {medium_threshold:.1f}"
        )

        # 根据动态阈值设置优先级
        for project in candidates:
            if project.quality_score is None:
                project.recommendation_priority = "low"
            elif project.quality_score >= high_threshold:
                project.recommendation_priority = "high"
            elif project.quality_score >= medium_threshold:
                project.recommendation_priority = "medium"
            else:
                project.recommendation_priority = "low"

        # 统计各优先级数量
        high_count = sum(1 for p in candidates if p.recommendation_priority == "high")
        medium_count = sum(
            1 for p in candidates if p.recommendation_priority == "medium"
        )
        low_count = sum(1 for p in candidates if p.recommendation_priority == "low")

        total = len(candidates)
        logger.info(
            f"优先级分布: high={high_count} ({high_count / total * 100:.1f}%), "
            f"medium={medium_count} ({medium_count / total * 100:.1f}%), "
            f"low={low_count} ({low_count / total * 100:.1f}%)",
        )

        return candidates

    def evaluate(
        self,
        candidates: list[DiscoveredProject],
    ) -> list[DiscoveredProject]:
        """批量评估项目质量并设置动态优先级

        Args:
            candidates: 候选项目列表

        Returns:
            评估后的项目列表（quality_score 和 priority 已设置）
        """
        # 先调用父类方法计算基础分数
        evaluated = super().evaluate(candidates)

        # 使用动态阈值重新设置优先级
        return self.set_priorities_only(evaluated)
