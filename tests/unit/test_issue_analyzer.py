"""IssueAnalyzer 分析器测试

测试 Issue 分析功能，包括分类、情绪分析、痛点提取等。
"""

from datetime import UTC, datetime

from trendpluse.analyzers.issue_analyzer import IssueAnalyzer
from trendpluse.models.issue import IssueAnalysis, IssueInfo


class TestIssueAnalysis:
    """IssueAnalysis 数据模型测试"""

    def test_create_bug_report_analysis(self):
        """测试创建 Bug 报告分析"""
        # Arrange & Act
        analysis = IssueAnalysis(
            category="bug_report",
            sentiment="negative",
            sentiment_score=-0.7,
            pain_point="App crashes on startup",
            affected_area="startup process",
            feature_description=None,
            priority="high",
            tech_tags=["crash", "startup"],
        )

        # Assert
        assert analysis.category == "bug_report"
        assert analysis.sentiment == "negative"
        assert analysis.sentiment_score == -0.7
        assert analysis.pain_point == "App crashes on startup"
        assert analysis.feature_description is None
        assert analysis.priority == "high"

    def test_create_feature_request_analysis(self):
        """测试创建功能请求分析"""
        # Arrange & Act
        analysis = IssueAnalysis(
            category="feature_request",
            sentiment="neutral",
            sentiment_score=0.0,
            pain_point=None,
            affected_area=None,
            feature_description="Add dark mode support",
            priority="medium",
            tech_tags=["ui", "theme"],
        )

        # Assert
        assert analysis.category == "feature_request"
        assert analysis.feature_description == "Add dark mode support"

    def test_feature_description_null_string_is_sanitized(self):
        """测试 feature_description 为无效字符串时自动清洗为 None"""
        analysis = IssueAnalysis(
            category="feature_request",
            sentiment="neutral",
            sentiment_score=0.0,
            pain_point=None,
            affected_area=None,
            feature_description="null",
            priority="medium",
            tech_tags=[],
        )

        assert analysis.feature_description is None

    def test_sentiment_score_validation(self):
        """测试情绪分数范围验证"""
        # Arrange & Act
        analysis = IssueAnalysis(
            category="discussion",
            sentiment="positive",
            sentiment_score=1.0,
            pain_point=None,
            feature_description=None,
            priority="low",
            tech_tags=[],
        )

        # Assert
        assert -1.0 <= analysis.sentiment_score <= 1.0

    def test_default_values(self):
        """测试默认值"""
        # Arrange & Act
        analysis = IssueAnalysis(
            category="question",
            sentiment="neutral",
            sentiment_score=0.0,
            pain_point=None,
            feature_description=None,
            priority="medium",
            tech_tags=[],
        )

        # Assert
        assert analysis.pain_point is None
        assert analysis.feature_description is None
        assert analysis.tech_tags == []


class TestIssueAnalyzer:
    """IssueAnalyzer 分析器测试"""

    def test_create_analyzer(self):
        """测试创建分析器"""
        # Arrange & Act
        analyzer = IssueAnalyzer(
            api_key="test_key",
            model="glm-4.7",
            base_url="https://api.example.com",
        )

        # Assert
        assert analyzer.api_key == "test_key"
        assert analyzer.model == "glm-4.7"
        assert analyzer.base_url == "https://api.example.com"
        assert analyzer.use_instructor is True

    # LLM 分析的集成测试需要真实 API 或复杂的 mock，这里省略
    # 实际的 LLM 调用测试在集成测试中覆盖
    def test_analyze_batch_with_empty_list(self):
        """测试批量分析空列表"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")

        # Act
        results = analyzer.analyze_batch([])

        # Assert
        assert results == {}

    def test_extract_signals_with_empty_analyses(self):
        """测试从空分析结果提取信号"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")
        issues: list[IssueInfo] = []
        analyses: dict[str, IssueAnalysis] = {}

        # Act
        signals = analyzer.extract_signals(issues, analyses)

        # Assert
        assert signals == []

    def test_extract_signals_filters_low_value_issues(self):
        """测试过滤低价值 Issue"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")
        now = datetime.now(UTC)

        issue = IssueInfo(
            repo="test/repo",
            issue_id=1,
            title="Minor typo",
            body="There is a typo in the docs",
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=0,
            labels=[],
            url="https://example.com",
            last_comment_days=0,
            is_recently_active=False,
        )

        analysis = IssueAnalysis(
            category="discussion",
            sentiment="neutral",
            sentiment_score=0.0,
            pain_point=None,
            feature_description=None,
            priority="low",
            tech_tags=[],
        )

        # Act
        signals = analyzer.extract_signals([issue], {"test/repo#1": analysis})

        # Assert - 低价值 Issue 不生成信号
        assert signals == []

    def test_extract_signals_from_high_priority_feature(self):
        """测试从高优先级功能请求提取信号"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")
        now = datetime.now(UTC)

        issue = IssueInfo(
            repo="test/repo",
            issue_id=1,
            title="Add API support",
            body="Please add REST API support",
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=15,
            labels=["enhancement"],
            url="https://example.com",
            last_comment_days=0,
            is_recently_active=True,
        )

        analysis = IssueAnalysis(
            category="feature_request",
            sentiment="neutral",
            sentiment_score=0.0,
            pain_point=None,
            affected_area=None,
            feature_description="Add REST API support",
            priority="high",
            tech_tags=["api"],
        )

        # Act
        signals = analyzer.extract_signals([issue], {"test/repo#1": analysis})

        # Assert
        assert len(signals) == 1
        assert signals[0].type == "capability"
        assert signals[0].category == "engineering"

    def test_extract_signals_from_negative_bug(self):
        """测试从负面情绪的 Bug 提取信号"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")
        now = datetime.now(UTC)

        issue = IssueInfo(
            repo="test/repo",
            issue_id=1,
            title="Memory leak",
            body="App leaks memory over time",
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=8,
            labels=["bug"],
            url="https://example.com",
            last_comment_days=0,
            is_recently_active=True,
        )

        analysis = IssueAnalysis(
            category="bug_report",
            sentiment="negative",
            sentiment_score=-0.6,
            pain_point="Memory leak causes crashes",
            affected_area="memory management",
            feature_description=None,
            priority="high",
            tech_tags=["memory"],
        )

        # Act
        signals = analyzer.extract_signals([issue], {"test/repo#1": analysis})

        # Assert
        assert len(signals) == 1
        assert signals[0].type == "workflow"

    def test_calculate_impact_score(self):
        """测试影响评分计算"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test_key")

        # 测试用例：(comments, priority, sentiment) -> 预期评分
        test_cases = [
            (20, "critical", "negative", 5),  # 最高分
            (10, "high", "negative", 4),
            (5, "medium", "neutral", 3),
            (2, "low", "positive", 2),
            (0, "low", "positive", 1),  # 最低分
        ]

        for comments, priority, sentiment, expected in test_cases:
            # Arrange
            from trendpluse.models.issue import IssueInfo

            issue = IssueInfo(
                repo="test/repo",
                issue_id=1,
                title="Test",
                body="Test",
                state="open",
                author="user",
                created_at=datetime.now(UTC),
                updated_at=datetime.now(UTC),
                closed_at=None,
                comments=comments,
                labels=[],
                url="https://example.com",
                last_comment_days=0,
                is_recently_active=False,
            )

            analysis = IssueAnalysis(
                category="bug_report",
                sentiment=sentiment,
                sentiment_score=0.0,
                pain_point=None,
                feature_description=None,
                priority=priority,
                tech_tags=[],
            )

            # Act
            score = analyzer._calculate_impact_score(issue, analysis)

            # Assert
            assert score == expected, (
                f"Failed for comments={comments}, priority={priority}, "
                f"sentiment={sentiment}: got {score}, expected {expected}"
            )
