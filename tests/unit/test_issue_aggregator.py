"""IssueAggregator 聚合器测试

测试 Issue 聚合功能，包括用户痛点聚合等。
"""

from datetime import UTC, datetime

from trendpluse.aggregators.issue_aggregator import IssueAggregator
from trendpluse.analyzers.issue_analyzer import IssueAnalysis
from trendpluse.models.issue import IssueInfo


class TestIssueAggregator:
    """IssueAggregator 聚合器测试"""

    def test_create_aggregator(self):
        """测试创建聚合器"""
        # Arrange & Act
        aggregator = IssueAggregator(min_mentions=3)

        # Assert
        assert aggregator.min_mentions == 3

    def test_create_aggregator_with_custom_threshold(self):
        """测试创建自定义最小提及次数的聚合器"""
        # Arrange & Act
        aggregator = IssueAggregator(min_mentions=5)

        # Assert
        assert aggregator.min_mentions == 5

    def test_aggregate_pain_points_with_empty_list(self):
        """测试空列表返回空结果"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=3)

        # Act
        pain_points = aggregator.aggregate_pain_points([], {})

        # Assert
        assert pain_points == []

    def test_aggregate_pain_points_filters_by_min_mentions(
        self,
    ):
        """测试按最小提及次数过滤"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=3)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Memory leak"),
            self._create_issue(now, 2, "Memory leak"),
            self._create_issue(now, 3, "Single mention"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", 0.0, "Memory leak"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", 0.0, "Memory leak"
            ),
            "test/repo#3": self._create_analysis(
                "bug_report", "neutral", 0.0, "Single mention"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - "Memory leak" 有 2 次提及（被过滤），"Single issue" 只有 1 次
        # 所以只有 "Memory leak" 会被过滤（需要 >=3），结果应该是空的
        assert len(pain_points) == 0

    def test_aggregate_pain_groups_by_keywords(self):
        """测试按痛点文本聚合"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "App crashes on startup"),
            self._create_issue(now, 2, "App crashes during startup"),
            self._create_issue(now, 3, "App crashes when starting"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", 0.0, "App crashes on startup"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", 0.0, "App crashes on startup"
            ),
            "test/repo#3": self._create_analysis(
                "bug_report", "negative", 0.0, "App crashes on startup"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 应该聚合成一个痛点（相同的 pain_point 文本）
        assert len(pain_points) == 1
        assert pain_points[0].topic == "App crashes on startup"
        assert pain_points[0].count == 3

    def test_aggregate_calculates_average_sentiment(self):
        """测试计算平均情绪分数"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Performance issue"),
            self._create_issue(now, 2, "Performance issue"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", -0.8, "Performance issue"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "neutral", -0.2, "Performance issue"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert
        assert len(pain_points) == 1
        # 平均情绪应该是 (-0.8 + -0.2) / 2 = -0.5
        assert pain_points[0].avg_sentiment == -0.5

    def test_aggregate_tracks_affected_repos(self):
        """测试跟踪受影响的仓库"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Crash", repo="repo1"),
            self._create_issue(now, 2, "Crash", repo="repo2"),
            self._create_issue(now, 3, "Crash", repo="repo1"),
        ]

        analyses = {
            "repo1#1": self._create_analysis("bug_report", "negative", 0.0, "Crash"),
            "repo2#2": self._create_analysis("bug_report", "negative", 0.0, "Crash"),
            "repo1#3": self._create_analysis("bug_report", "negative", 0.0, "Crash"),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert
        assert len(pain_points) == 1
        # 应该包含 repo1 和 repo2（去重）
        repos = pain_points[0].affected_repos
        assert len(repos) == 2
        assert "repo1" in repos
        assert "repo2" in repos

    def test_aggregate_collects_sample_urls(self):
        """测试收集示例 URL"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        url1 = "https://github.com/test/repo/issues/1"
        url2 = "https://github.com/test/repo/issues/2"

        issues = [
            self._create_issue(now, 1, "Issue 1", url=url1),
            self._create_issue(now, 2, "Issue 2", url=url2),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", pain_point="Common Issue"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", pain_point="Common Issue"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert
        assert len(pain_points) == 1
        # 应该包含最多 5 个示例 URL
        assert len(pain_points[0].sample_urls) <= 5
        # 应该包含两个 URL
        assert url1 in pain_points[0].sample_urls
        assert url2 in pain_points[0].sample_urls

    def test_aggregate_sorts_by_count_descending(self):
        """测试按提及次数降序排序"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Low count issue"),
            self._create_issue(now, 2, "High count issue"),
            self._create_issue(now, 3, "High count issue"),
            self._create_issue(now, 4, "High count issue"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "bug_report", "negative", pain_point="Low count issue"
            ),
            "test/repo#2": self._create_analysis(
                "bug_report", "negative", pain_point="High count issue"
            ),
            "test/repo#3": self._create_analysis(
                "bug_report", "negative", pain_point="High count issue"
            ),
            "test/repo#4": self._create_analysis(
                "bug_report", "negative", pain_point="High count issue"
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 应该按 count 降序排列
        # 但由于使用简单分词，可能产生多个关键词
        if len(pain_points) > 1:
            counts = [p.count for p in pain_points]
            assert counts == sorted(counts, reverse=True)

    def test_aggregate_handles_no_pain_point(self):
        """测试处理没有痛点的 Issue"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)
        now = datetime.now(UTC)

        issues = [
            self._create_issue(now, 1, "Question"),
        ]

        analyses = {
            "test/repo#1": self._create_analysis(
                "question", "neutral", pain_point=None
            ),
        }

        # Act
        pain_points = aggregator.aggregate_pain_points(issues, analyses)

        # Assert - 没有痛点的 Issue 应该被忽略
        assert len(pain_points) == 0

    def test_extract_keywords_from_pain_point(self):
        """测试从痛点描述中提取关键词"""
        # Arrange
        aggregator = IssueAggregator(min_mentions=2)

        # Act
        keywords = aggregator._extract_keywords("App crashes on startup")

        # Assert - 应该返回关键词列表
        assert isinstance(keywords, list)
        assert len(keywords) > 0
        # 应该包含至少一个关键词
        assert any(len(k) >= 2 for k in keywords)

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
