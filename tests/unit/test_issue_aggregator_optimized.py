"""IssueAggregator 优化功能测试

测试 Issue 聚合器的优化功能：
1. 时间窗口调整为 5 天
2. 痛点为 null 时 fallback 到标题
3. 痛点文本归一化（去重）
"""

from datetime import UTC, datetime

from trendpluse.aggregators.issue_aggregator import IssueAggregator
from trendpluse.analyzers.issue_analyzer import IssueAnalysis
from trendpluse.models.issue import IssueInfo


class TestIssueAggregatorOptimized:
    """IssueAggregator 优化功能测试"""

    def test_fallback_to_title_when_pain_point_is_null(self):
        """测试：痛点为 null 时应 fallback 到 Issue 标题"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "App crashes on startup"),
            self._create_issue(now, 2, "App crashes on startup"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report",
                "negative",
                -0.5,
                pain_point=None,  # ← pain_point 为 null
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", -0.3, pain_point=None
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 应该使用标题作为痛点，而不是跳过
        assert len(pain_points) == 1
        assert pain_points[0].topic == "App crashes on startup"
        assert pain_points[0].count == 2

    def test_normalize_pain_point_merges_similar_issues(self):
        """测试：归一化痛点文本应合并相似的痛点"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "402 error no quota"),
            self._create_issue(now, 2, "402 error no quota"),
            self._create_issue(now, 3, "402 error，没有剩余额度"),
            self._create_issue(now, 4, "402 error，没有剩余配额"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", -0.5, "402 错误，没有剩余配额"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", -0.3, "402错误没有剩余额度"
            ),
            "test/repo#3": self._create_analysis(
                "bug_report", "negative", -0.4, "402 错误 没有剩余配额"
            ),
            "test/repo#4": self._create_analysis(
                "bug_report", "negative", -0.6, "402错误没有剩余配额"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 四个相似的痛点应该被归一化合并为一个
        assert len(pain_points) == 1
        # 归一化后的主题应该去除空格和标点
        normalized_topic = pain_points[0].topic
        assert "402" in normalized_topic.lower()
        assert pain_points[0].count == 4

    def test_normalize_removes_punctuation_and_spaces(self):
        """测试：归一化应移除标点和空格"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)

        # Act
        normalized1 = aggregator._normalize_pain_point("402 错误，没有剩余配额")
        normalized2 = aggregator._normalize_pain_point("402错误没有剩余额度")
        normalized3 = aggregator._normalize_pain_point("402 error no quota")

        # Assert - 应该被归一化为相同的结果
        assert normalized1 == normalized2
        # normalized3 是英文，可能不会完全匹配，但至少包含核心关键词
        assert "402" in normalized1 or "402" in normalized3

    def test_normalize_preserves_meaningful_content(self):
        """测试：归一化应保留有意义的内容"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)

        # Act
        normalized = aggregator._normalize_pain_point("无法使用 AI 助手完成工作")

        # Assert - 核心关键词应该被保留
        assert "无法" in normalized or "use" in normalized.lower()
        assert "ai" in normalized.lower()
        assert "工作" in normalized or "work" in normalized.lower()

    def test_aggregate_with_mixed_null_and_valid_pain_points(self):
        """测试：混合 null 和有效痛点的场景"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Payment failed"),
            self._create_issue(now, 2, "Payment failed"),
            self._create_issue(now, 3, "Login timeout"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report",
                "negative",
                -0.5,
                pain_point=None,  # null
            ),
            "test/repo#2": self._create_analysis(
                "bug_report",
                "negative",
                -0.3,
                pain_point=None,  # null
            ),
            "test/repo#3": self._create_analysis(
                "bug_report",
                "negative",
                -0.4,
                pain_point="Login timeout",  # 有效
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert
        # "Payment failed" 出现 2 次（使用标题 fallback）
        # "Login timeout" 只有 1 次，低于 min_mentions=2，所以不计入
        assert len(pain_points) == 1

        # null pain_point 的 Issues 应该被计入（使用标题）
        payment_point = pain_points[0]
        assert "payment" in payment_point.topic.lower()
        assert payment_point.count == 2

    def test_original_text_preserved_for_display(self):
        """测试：原始文本应被保留用于展示"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=1)  # 降低阈值
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "402 error"),
        ]

        original_pain_point = "402 错误，没有剩余配额"
        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", -0.5, pain_point=original_pain_point
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 展示时应该使用原始文本，不是归一化后的文本
        assert len(pain_points) == 1
        # 原始文本应被保留（用于生成报告）
        assert pain_points[0].topic == original_pain_point

    # 辅助方法
    def _create_issue(
        self,
        now: datetime,
        issue_id: int,
        title: str,
        repo: str = "test/repo",
        url: str = "https://github.com/test/repo/issues/1",
    ) -> IssueInfo:
        """创建测试用 Issue"""
        return IssueInfo(
            repo=repo,
            issue_id=issue_id,
            title=title,
            body=None,
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=[],
            url=url,
            last_comment_days=0,
            is_recently_active=False,
        )

    def _create_analysis(
        self,
        category: str = "bug_report",
        sentiment: str = "neutral",
        sentiment_score: float = 0.0,
        pain_point: str | None = None,
    ) -> IssueAnalysis:
        """创建测试用分析结果"""
        return IssueAnalysis(
            category=category,
            sentiment=sentiment,
            sentiment_score=sentiment_score,
            pain_point=pain_point,
            affected_area=None,
            feature_description=None,
            priority="medium",
            tech_tags=[],
        )


class TestIssueCollectorTimeWindow:
    """IssueCollector 时间窗口测试"""

    def test_create_window_days_should_be_5(self):
        """测试：创建时间窗口应设置为 5 天"""
        # Arrange & Act
        from trendpluse.collectors.issues import IssueCollector

        # Assert
        assert IssueCollector.CREATE_WINDOW_DAYS == 5
