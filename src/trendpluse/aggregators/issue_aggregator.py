"""Issue 聚合器

从多个 Issues 中聚合用户痛点。
"""

from collections import defaultdict

from trendpluse.analyzers.issue_analyzer import IssueAnalysis
from trendpluse.logger import get_logger
from trendpluse.models.issue import IssueInfo, UserPainPoint

logger = get_logger(__name__)


class IssueAggregator:
    """Issue 聚合器

    从多个 Issues 中聚合用户痛点。
    """

    def __init__(self, min_mentions: int = 3):
        """初始化聚合器

        Args:
            min_mentions: 最小提及次数阈值
        """
        self.min_mentions = min_mentions

    def aggregate_pain_points(
        self,
        issues: list[IssueInfo],
        analyses: dict[str, IssueAnalysis],
    ) -> list[UserPainPoint]:
        """聚合用户痛点

        Args:
            issues: Issue 列表
            analyses: 分析结果字典

        Returns:
            痛点列表（按提及次数排序）
        """
        # 使用完整 pain_point 文本作为 key 进行聚合
        pain_point_map: dict[str, list[int]] = defaultdict(list)
        sentiment_scores: dict[str, list[float]] = defaultdict(list)
        affected_repos: dict[str, set[str]] = defaultdict(set)
        sample_issues: dict[str, list[str]] = defaultdict(list)

        for issue in issues:
            key = f"{issue.repo}#{issue.issue_id}"
            analysis = analyses.get(key)

            if not analysis or not analysis.pain_point:
                continue

            # 使用完整的 pain_point 文本作为聚合 key
            pain_point = analysis.pain_point
            pain_point_map[pain_point].append(issue.issue_id)
            sentiment_scores[pain_point].append(analysis.sentiment_score)
            affected_repos[pain_point].add(issue.repo)
            sample_issues[pain_point].append(issue.url)

        # 构建痛点列表
        pain_points = []
        for topic, issue_ids in pain_point_map.items():
            if len(issue_ids) >= self.min_mentions:
                # 计算平均情绪分数
                scores = sentiment_scores[topic]
                avg_sentiment = sum(scores) / len(scores) if scores else 0.0

                pain_points.append(
                    UserPainPoint(
                        topic=topic,
                        count=len(issue_ids),
                        avg_sentiment=avg_sentiment,
                        affected_repos=list(affected_repos[topic]),
                        sample_urls=list(sample_issues[topic])[:5],  # 最多 5 个示例
                    )
                )

        # 按提及次数排序
        pain_points.sort(key=lambda p: p.count, reverse=True)

        logger.info(
            f"痛点聚合完成: {len(pain_points)} 个痛点 "
            f"(最低提及次数: {self.min_mentions})"
        )

        return pain_points

    def _extract_keywords(self, text: str) -> list[str]:
        """从文本中提取关键词

        Args:
            text: 输入文本

        Returns:
            关键词列表
        """
        # 简化实现：使用空格和标点分词
        # 移除常见的停用词
        words = text.split()
        keywords = []

        for word in words:
            # 清理单词
            clean_word = word.strip('.,!?;:()[]{}"\'"').lower()

            # 只保留长度 >= 2 的单词
            if len(clean_word) >= 2:
                keywords.append(clean_word)

        # 简单去重
        seen = set()
        unique_keywords = []
        for word in keywords:
            if word not in seen:
                seen.add(word)
                unique_keywords.append(word)

        return unique_keywords[:3]  # 返回前 3 个关键词
