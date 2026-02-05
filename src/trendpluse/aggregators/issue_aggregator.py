"""Issue 聚合器

从多个 Issues 中聚合用户痛点。
"""

from collections import defaultdict
from typing import Protocol

from trendpluse.logger import get_logger
from trendpluse.models.issue import (
    IssueAnalysis,
    IssueInfo,
    IssueQualityDecision,
    UserPainPoint,
)
from trendpluse.utils.text import sanitize_optional_text

logger = get_logger(__name__)


class IssueTopicNormalizer(Protocol):
    def normalize_topics(self, topics: list[str]) -> dict[str, str]: ...


class IssueQualityGate(Protocol):
    def evaluate(self, issues: list[IssueInfo]) -> dict[str, IssueQualityDecision]: ...


class IssueAggregator:
    """Issue 聚合器

    从多个 Issues 中聚合用户痛点。
    """

    def __init__(
        self,
        min_mentions: int = 3,
        topic_normalizer: IssueTopicNormalizer | None = None,
        quality_gate: IssueQualityGate | None = None,
    ):
        """初始化聚合器

        Args:
            min_mentions: 最小提及次数阈值
        """
        self.min_mentions = min_mentions
        self.topic_normalizer = topic_normalizer
        self.quality_gate = quality_gate

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
        # 使用归一化后的痛点文本作为 key 进行聚合
        pain_point_map: dict[str, list[int]] = defaultdict(list)
        sentiment_scores: dict[str, list[float]] = defaultdict(list)
        affected_repos: dict[str, set[str]] = defaultdict(set)
        sample_issues: dict[str, list[str]] = defaultdict(list)
        # 保留原始文本（归一化 key → 原始文本）
        original_text_map: dict[str, str] = {}
        stats = {
            "total": len(issues),
            "missing_analysis": 0,
            "excluded_quality": 0,
            "excluded_heuristic": 0,
            "missing_pain_point": 0,
            "included": 0,
        }

        quality_decisions = self._evaluate_issue_quality(issues)

        for issue in issues:
            key = f"{issue.repo}#{issue.issue_id}"
            analysis = analyses.get(key)

            if not analysis:
                stats["missing_analysis"] += 1
                continue

            decision = quality_decisions.get(key)
            if decision is not None:
                if not decision.include:
                    stats["excluded_quality"] += 1
                    continue
            elif not self._should_include_issue(issue, analysis):
                stats["excluded_heuristic"] += 1
                continue

            # 获取痛点，优先使用 pain_point，fallback 到标题
            pain_point = sanitize_optional_text(analysis.pain_point)
            if not pain_point and decision is not None:
                pain_point = sanitize_optional_text(decision.normalized_topic)
            if not pain_point:
                pain_point = issue.title
            if not pain_point:
                stats["missing_pain_point"] += 1
                continue

            # 归一化痛点文本用于聚合
            normalized_topic = self._normalize_pain_point(pain_point)
            pain_point_map[normalized_topic].append(issue.issue_id)
            sentiment_scores[normalized_topic].append(analysis.sentiment_score)
            affected_repos[normalized_topic].add(issue.repo)
            sample_issues[normalized_topic].append(issue.url)

            # 保留原始文本（第一个出现的）
            if normalized_topic not in original_text_map:
                original_text_map[normalized_topic] = pain_point
            stats["included"] += 1

        # 构建痛点列表
        pain_points = []
        normalized_topics = self._normalize_topics_with_llm(list(pain_point_map.keys()))
        below_threshold = sum(
            1
            for issue_ids in pain_point_map.values()
            if len(issue_ids) < self.min_mentions
        )
        for normalized_topic, issue_ids in pain_point_map.items():
            if len(issue_ids) >= self.min_mentions:
                # 计算平均情绪分数
                scores = sentiment_scores[normalized_topic]
                avg_sentiment = sum(scores) / len(scores) if scores else 0.0

                # 使用原始文本作为展示主题
                original_topic = original_text_map.get(
                    normalized_topic, normalized_topic
                )
                normalized_display = normalized_topics.get(normalized_topic)
                display_topic = normalized_display or original_topic

                pain_points.append(
                    UserPainPoint(
                        topic=display_topic,
                        count=len(issue_ids),
                        avg_sentiment=avg_sentiment,
                        affected_repos=list(affected_repos[normalized_topic]),
                        sample_urls=list(sample_issues[normalized_topic])[:5],
                    )
                )

        # 按提及次数排序
        pain_points.sort(key=lambda p: p.count, reverse=True)

        logger.info(
            "痛点聚合完成: %s 个痛点 (最低提及次数: %s) | "
            "issues=%s included=%s missing_analysis=%s excluded_quality=%s "
            "excluded_heuristic=%s missing_pain_point=%s below_threshold=%s "
            "normalized_topics=%s",
            len(pain_points),
            self.min_mentions,
            stats["total"],
            stats["included"],
            stats["missing_analysis"],
            stats["excluded_quality"],
            stats["excluded_heuristic"],
            stats["missing_pain_point"],
            below_threshold,
            len(normalized_topics),
        )

        return pain_points

    def _evaluate_issue_quality(
        self, issues: list[IssueInfo]
    ) -> dict[str, IssueQualityDecision]:
        if not self.quality_gate or not issues:
            return {}

        try:
            return self.quality_gate.evaluate(issues)
        except Exception as exc:
            logger.debug(f"Issue 质量判定失败: {exc}")
            return {}

    def _should_include_issue(self, issue: IssueInfo, analysis: IssueAnalysis) -> bool:
        title = (issue.title or "").lower()
        blocked_keywords = ("announcement", "release", "protocol")
        if any(keyword in title for keyword in blocked_keywords):
            return False

        if not issue.labels:
            return analysis.category in {"bug_report", "feature_request", "question"}

        allowed_keywords = ("bug", "feature", "question")
        if any(
            keyword in label.lower()
            for label in issue.labels
            for keyword in allowed_keywords
        ):
            return True

        return False

    def _normalize_topics_with_llm(self, topics: list[str]) -> dict[str, str]:
        if not topics or not self.topic_normalizer:
            return {}

        try:
            normalized = self.topic_normalizer.normalize_topics(topics)
        except Exception as exc:
            logger.debug(f"痛点主题 LLM 归一化失败: {exc}")
            return {}

        if not isinstance(normalized, dict):
            return {}

        return {k: v for k, v in normalized.items() if v}

    def _normalize_pain_point(self, pain_point: str) -> str:
        """归一化痛点文本

        处理常见的重复模式：
        - 移除空格和标点符号
        - 统一常见同义词（配额/额度）
        - 小写化处理

        Args:
            pain_point: 原始痛点文本

        Returns:
            归一化后的文本
        """
        import re

        # 转小写
        normalized = pain_point.lower()

        # 统一同义词（在移除空格前处理，避免双重否定）
        synonym_map = {
            "配额": "额度",
            "额度": "配额",  # 统一为同一个词
            "剩余": "剩余",
            "导致无法": "无法",
            "无法使用": "无法",
        }

        # 替换同义词（只替换一次）
        for old, new in synonym_map.items():
            if old in normalized:
                normalized = normalized.replace(old, new)

        # 移除所有空格
        normalized = normalized.replace(" ", "")

        # 移除常见中英文标点
        normalized = re.sub(r"[,，。！!？?、；;:：()]", "", normalized)

        return normalized

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
