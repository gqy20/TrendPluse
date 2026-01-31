"""质量评估器

根据多维度指标评估项目质量。
"""

from datetime import datetime
from typing import Literal

from trendpluse.logger import get_logger
from trendpluse.models.discovery import DiscoveredProject

logger = get_logger(__name__)


class QualityEvaluator:
    """质量评估器

    根据多个维度评估项目质量：
    - Star 数量 (20%)
    - 活跃度 (30%)
    - 社区健康度 (20%)
    - 代码质量 (15%)
    - 相关性 (15%)
    """

    def __init__(self, min_quality_score: float = 60.0) -> None:
        """初始化质量评估器

        Args:
            min_quality_score: 最低质量分数阈值，默认 60.0
        """
        self.min_quality_score = min_quality_score

    def evaluate(
        self,
        candidates: list[DiscoveredProject],
    ) -> list[DiscoveredProject]:
        """批量评估项目质量

        Args:
            candidates: 候选项目列表

        Returns:
            评估后的项目列表（quality_score 等字段已填充）
        """
        results = []
        for project in candidates:
            # 计算各项分数
            star_score = self._calculate_star_score(project.stars)
            activity_score = self._calculate_activity_score(project.last_commit_at)
            community_score = self._calculate_community_score(
                project.forks, project.watchers
            )
            code_quality_score = self._calculate_code_quality_score(
                has_license=project.license is not None,
                has_description=bool(project.description),
                # 简化：用 description 代替 README
                has_readme=bool(project.description),
            )
            relevance_score = self._calculate_relevance_score(project)

            # 总分
            total_score = (
                star_score
                + activity_score
                + community_score
                + code_quality_score
                + relevance_score
            )

            project.quality_score = min(total_score, 100.0)
            project.activity_level = self._get_activity_level(activity_score)
            project.recommended = project.quality_score >= self.min_quality_score

            # 设置推荐优先级
            if project.quality_score >= 80:
                project.recommendation_priority = "high"
            elif project.quality_score >= 60:
                project.recommendation_priority = "medium"
            else:
                project.recommendation_priority = "low"

            results.append(project)

        logger.info(
            f"质量评估完成: {len(results)} 个项目, "
            f"{sum(1 for p in results if p.recommended)} 个推荐"
        )
        return results

    def _calculate_star_score(self, stars: int) -> float:
        """计算 Star 分数 (0-20)

        Args:
            stars: star 数量

        Returns:
            分数 0-20
        """
        if stars >= 10000:
            return 20
        elif stars >= 5000:
            return 15
        elif stars >= 1000:
            return 10
        elif stars >= 500:
            return 5
        else:
            return 0

    def _calculate_activity_score(self, last_commit: datetime | None) -> float:
        """计算活跃度分数 (0-30)

        Args:
            last_commit: 最后提交时间

        Returns:
            分数 0-30
        """
        if last_commit is None:
            return 0

        days_since = (datetime.now() - last_commit).days

        if days_since <= 7:
            return 30
        elif days_since <= 30:
            return 20
        elif days_since <= 90:
            return 10
        else:
            return 0

    def _calculate_community_score(self, forks: int, watchers: int) -> float:
        """计算社区健康度分数 (0-20)

        Args:
            forks: fork 数
            watchers: watcher 数

        Returns:
            分数 0-20
        """
        score = 0

        # Forks 分数 (最高 10 分)
        if forks >= 100:
            score += 10
        elif forks >= 50:
            score += 5
        elif forks >= 10:
            score += 2

        # Watchers 分数 (最高 10 分)
        if watchers >= 50:
            score += 10
        elif watchers >= 20:
            score += 5
        elif watchers >= 5:
            score += 2

        return score

    def _calculate_code_quality_score(
        self,
        has_license: bool,
        has_description: bool,
        has_readme: bool,
    ) -> float:
        """计算代码质量分数 (0-15)

        Args:
            has_license: 是否有许可证
            has_description: 是否有描述
            has_readme: 是否有 README

        Returns:
            分数 0-15
        """
        score = 0

        if has_license:
            score += 5
        if has_description:
            score += 5
        if has_readme:
            score += 5

        return score

    def _calculate_relevance_score(self, project: DiscoveredProject) -> float:
        """计算相关性分数 (0-15)

        Args:
            project: 项目对象

        Returns:
            分数 0-15
        """
        # 相关主题词
        relevant_topics = {
            "agent",
            "ai",
            "llm",
            "rag",
            "claude",
            "autonomous",
            "multi-agent",
            "vector",
            "database",
            "ml",
            "machine-learning",
        }

        # 检查 topics 是否包含相关词
        topic_score = 0
        for topic in project.topics:
            if topic.lower() in relevant_topics:
                topic_score += 5
                if topic_score >= 15:
                    break

        # 检查描述中是否包含相关词
        description_score = 0
        if project.description:
            desc_lower = project.description.lower()
            for keyword in ["agent", "ai", "llm", "claude"]:
                if keyword in desc_lower:
                    description_score += 3
                    if description_score >= 15:
                        break

        return min(topic_score + description_score, 15)

    def _get_activity_level(
        self,
        activity_score: float,
    ) -> Literal["high", "medium", "low"]:
        """根据活跃度分数获取活跃度等级

        Args:
            activity_score: 活跃度分数

        Returns:
            活跃度等级
        """
        # 活跃度分数最高 30，所以按比例划分
        if activity_score >= 25:  # 83% 以上
            return "high"
        elif activity_score >= 15:  # 50% 以上
            return "medium"
        else:  # 低于 50%
            return "low"
