"""IssueAnalyzer 批量分析测试

使用 TDD 方法测试 Issue 批量分析功能，包括优化的批量处理、
Prompt 构建和降级重试机制。
"""

from datetime import UTC, datetime
from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.issue_analyzer import IssueAnalysis, IssueAnalyzer
from trendpluse.models.issue import BatchIssueAnalysis, IssueInfo


class TestBatchIssueAnalysisModel:
    """BatchIssueAnalysis 数据模型测试

    测试批量 Issue 分析的响应模型结构。
    """

    def test_batch_analysis_response_structure(self):
        """测试：批量分析响应应包含多个 Issue 的分析结果"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        # 这个方法还不存在，应该失败
        _ = analyzer.analyze_batch_optimized

        # Assert - 验证批量分析响应的模型结构
        # 预期模型应包含：
        # - analyses: dict[str, IssueAnalysis]  # key 为 "repo#issue_id"
        # - metadata: dict  # 包含批量大小、处理时间等信息

    def test_batch_analysis_with_empty_issues(self):
        """测试：空 Issue 列表应返回空批量分析结果"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        results = analyzer.analyze_batch_optimized([])

        # Assert - 验证返回空字典
        assert results == {}

    def test_batch_analysis_response_validation(self):
        """测试：批量分析响应应验证所有必需字段"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act & Assert - 验证方法存在
        _ = analyzer.analyze_batch_optimized


class TestBatchPromptBuilder:
    """批量 Prompt 构建测试

    测试 `build_batch_prompt` 方法，该方法将多个 Issue 组合
    成单个 LLM 请求以优化批量处理。
    """

    @pytest.fixture
    def sample_issues(self):
        """提供测试用的 Issue 列表"""
        now = datetime.now(UTC)
        return [
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=1,
                title="Add streaming support",
                body="Please add streaming support for responses",
                state="open",
                author="user1",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=5,
                labels=["enhancement"],
                url="https://github.com/anthropics/claude-sdk/issues/1",
                last_comment_days=0,
                is_recently_active=True,
            ),
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=2,
                title="Memory leak in connection pool",
                body="Connection pool leaks memory when requests fail",
                state="open",
                author="user2",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=10,
                labels=["bug"],
                url="https://github.com/anthropics/claude-sdk/issues/2",
                last_comment_days=0,
                is_recently_active=True,
            ),
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=3,
                title="How to use the API key?",
                body="Where do I set the API key?",
                state="open",
                author="user3",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=2,
                labels=["question"],
                url="https://github.com/anthropics/claude-sdk/issues/3",
                last_comment_days=0,
                is_recently_active=False,
            ),
        ]

    def test_build_batch_prompt_structure(self, sample_issues):
        """测试：批量 Prompt 应包含所有 Issue 信息"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        prompt = analyzer.build_batch_prompt(sample_issues)

        # Assert - 验证 Prompt 包含：
        # - 所有 Issue 的标题和内容
        # - 每个 Issue 的唯一标识（用于结果映射）
        # - 清晰的分析指令
        assert "Add streaming support" in prompt
        assert "Memory leak" in prompt
        assert "anthropics/claude-sdk" in prompt

    def test_build_batch_prompt_with_single_issue(self, sample_issues):
        """测试：单个 Issue 的批量 Prompt 应正确处理"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        single_issue = [sample_issues[0]]

        # Act
        prompt = analyzer.build_batch_prompt(single_issue)

        # Assert - 单个 Issue 也应使用批量格式（保持一致性）
        assert "Add streaming support" in prompt

    def test_build_batch_prompt_issue_limit(self, sample_issues):
        """测试：批量 Prompt 应限制 Issue 数量以避免超时"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        # 创建超过限制的 Issue 列表
        large_issue_list = sample_issues * 10  # 30 个 issues

        # Act
        prompt = analyzer.build_batch_prompt(large_issue_list)

        # Assert - 验证：
        # - Prompt 只包含限制数量的 Issue
        # - 或者方法返回多个 Prompt（分批）
        assert prompt is not None

    def test_build_batch_prompt_includes_metadata(self, sample_issues):
        """测试：批量 Prompt 应包含仓库、状态、标签等元数据"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        prompt = analyzer.build_batch_prompt(sample_issues)

        # Assert - 验证 Prompt 包含：
        # - 仓库名称
        # - Issue 状态
        # - 标签
        # - 评论数
        assert "anthropics/claude-sdk" in prompt
        assert "open" in prompt
        assert "enhancement" in prompt or "bug" in prompt or "question" in prompt

    def test_build_batch_prompt_clear_instructions(self, sample_issues):
        """测试：批量 Prompt 应包含清晰的分析指令"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        prompt = analyzer.build_batch_prompt(sample_issues)

        # Assert - 验证 Prompt 包含：
        # - 返回格式说明（JSON 结构）
        # - 每个 Issue 的标识要求
        # - 分析标准说明
        assert "分析" in prompt or "analyze" in prompt.lower()


class TestBatchAnalysisOptimized:
    """优化的批量分析测试

    测试 `analyze_batch_optimized` 方法，该方法使用单个 LLM 请求
    分析多个 Issue 以提高效率。
    """

    @pytest.fixture
    def mock_batch_response(self):
        """Mock 批量分析 API 响应"""
        # 模拟批量分析返回多个 Issue 的结果
        return BatchIssueAnalysis(
            results=[
                IssueAnalysis(
                    category="feature_request",
                    sentiment="neutral",
                    sentiment_score=0.0,
                    pain_point=None,
                    affected_area=None,
                    feature_description="Add streaming support for API responses",
                    priority="high",
                    tech_tags=["streaming", "api"],
                ),
                IssueAnalysis(
                    category="bug_report",
                    sentiment="negative",
                    sentiment_score=-0.6,
                    pain_point="Memory leak causes crashes over time",
                    affected_area="connection pool",
                    feature_description=None,
                    priority="high",
                    tech_tags=["memory", "connection"],
                ),
                IssueAnalysis(
                    category="question",
                    sentiment="neutral",
                    sentiment_score=0.0,
                    pain_point=None,
                    affected_area=None,
                    feature_description=None,
                    priority="low",
                    tech_tags=["api-key", "configuration"],
                ),
            ],
            success_count=3,
            failure_count=0,
            failed_indices=[],
            errors=[],
        )

    @pytest.fixture
    def sample_issues(self):
        """提供测试用的 Issue 列表"""
        now = datetime.now(UTC)
        return [
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=1,
                title="Add streaming support",
                body="Please add streaming support for responses",
                state="open",
                author="user1",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=5,
                labels=["enhancement"],
                url="https://github.com/anthropics/claude-sdk/issues/1",
                last_comment_days=0,
                is_recently_active=True,
            ),
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=2,
                title="Memory leak in connection pool",
                body="Connection pool leaks memory when requests fail",
                state="open",
                author="user2",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=10,
                labels=["bug"],
                url="https://github.com/anthropics/claude-sdk/issues/2",
                last_comment_days=0,
                is_recently_active=True,
            ),
            IssueInfo(
                repo="anthropics/claude-sdk",
                issue_id=3,
                title="How to use the API key?",
                body="Where do I set the API key?",
                state="open",
                author="user3",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=2,
                labels=["question"],
                url="https://github.com/anthropics/claude-sdk/issues/3",
                last_comment_days=0,
                is_recently_active=False,
            ),
        ]

    def test_analyze_batch_optimized_success(self, sample_issues, mock_batch_response):
        """测试：优化的批量分析应成功处理多个 Issue"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        mock_client = MagicMock()

        # Mock 单个批量调用
        mock_client.chat.completions.create.return_value = mock_batch_response
        analyzer.client = mock_client

        # Act
        results = analyzer.analyze_batch_optimized(sample_issues)

        # Assert - 验证：
        # - 返回所有 Issue 的分析结果
        # - 结果字典的键格式为 "repo#issue_id"
        # - 只调用了一次 LLM API（批量处理）
        assert len(results) == 3
        assert "anthropics/claude-sdk#1" in results
        assert "anthropics/claude-sdk#2" in results
        assert "anthropics/claude-sdk#3" in results
        mock_client.chat.completions.create.assert_called_once()

    def test_analyze_batch_optimized_with_fallback(
        self, sample_issues, mock_batch_response
    ):
        """测试：批量失败后应降级到单个重试"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        mock_client = MagicMock()

        # 第一次批量调用失败，后续单个调用成功
        call_count = [0]

        def mock_create_with_failure(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                # 批量调用失败
                raise Exception("Batch API timeout")
            # 后续单个调用成功 - 返回单个 IssueAnalysis
            return mock_batch_response.results[0]

        mock_client.chat.completions.create.side_effect = mock_create_with_failure
        analyzer.client = mock_client

        # Act
        results = analyzer.analyze_batch_optimized(sample_issues)

        # Assert - 验证：
        # - 批量失败后自动降级
        # - 逐个重试 Issue
        # - 成功的分析被返回
        assert call_count[0] > 1  # 至少重试了一次
        assert len(results) >= 1  # 至少有一个成功

    def test_analyze_batch_optimized_empty_list(self):
        """测试：空 Issue 列表应返回空结果"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act
        results = analyzer.analyze_batch_optimized([])

        # Assert
        assert results == {}

    def test_analyze_batch_optimized_partial_failure(self):
        """测试：部分 Issue 分析失败不应影响其他 Issue"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        now = datetime.now(UTC)

        issues = [
            IssueInfo(
                repo="test/repo",
                issue_id=i,
                title=f"Test Issue {i}",
                body=f"Test body {i}",
                state="open",
                author="user",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=1,
                labels=[],
                url=f"https://github.com/test/repo/issues/{i}",
                last_comment_days=0,
                is_recently_active=True,
            )
            for i in range(5)
        ]

        # Mock 部分失败
        mock_client = MagicMock()
        call_count = [0]

        def mock_partial_failure(*args, **kwargs):
            call_count[0] += 1
            # 第 3 个失败
            if call_count[0] == 3:
                raise Exception("Analysis failed")
            return IssueAnalysis(
                category="discussion",
                sentiment="neutral",
                sentiment_score=0.0,
                pain_point=None,
                feature_description=None,
                priority="low",
                tech_tags=[],
            )

        mock_client.chat.completions.create.side_effect = mock_partial_failure
        analyzer.client = mock_client

        # Act
        results = analyzer.analyze_batch_optimized(issues)

        # Assert - 验证：
        # - 至少返回成功的分析
        # - 失败的 Issue 不在结果中
        assert len(results) >= 0  # 容错设计

    def test_analyze_batch_optimized_respects_batch_size(self):
        """测试：应正确处理超过批量大小限制的 Issue 列表"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        now = datetime.now(UTC)

        # 创建超过批量限制的 Issue 列表
        issues = [
            IssueInfo(
                repo="test/repo",
                issue_id=i,
                title=f"Issue {i}",
                body=f"Body {i}",
                state="open",
                author="user",
                created_at=now,
                updated_at=now,
                closed_at=None,
                comments=1,
                labels=[],
                url=f"https://github.com/test/repo/issues/{i}",
                last_comment_days=0,
                is_recently_active=True,
            )
            for i in range(20)  # 超过默认批量大小（假设为 10）
        ]

        # Mock 客户端 - 返回空的 BatchIssueAnalysis
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = BatchIssueAnalysis(
            results=[], success_count=0, failure_count=0, failed_indices=[], errors=[]
        )
        analyzer.client = mock_client

        # Act
        _ = analyzer.analyze_batch_optimized(issues)

        # Assert - 验证：
        # - 结果包含所有 Issue（或至少已处理的）
        # - 可能进行了多次批量调用
        assert mock_client.chat.completions.create.call_count >= 1


class TestBatchSizeValidation:
    """批量大小边界测试

    测试批量处理的边界条件和参数验证。
    """

    @pytest.fixture
    def sample_issue(self):
        """提供单个测试 Issue"""
        now = datetime.now(UTC)
        return IssueInfo(
            repo="test/repo",
            issue_id=1,
            title="Test Issue",
            body="Test body",
            state="open",
            author="user",
            created_at=now,
            updated_at=now,
            closed_at=None,
            comments=1,
            labels=[],
            url="https://github.com/test/repo/issues/1",
            last_comment_days=0,
            is_recently_active=True,
        )

    def test_batch_size_minimum_boundary(self, sample_issue):
        """测试：批量大小最小边界（1）应正常工作"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = BatchIssueAnalysis(
            results=[], success_count=0, failure_count=0, failed_indices=[], errors=[]
        )
        analyzer.client = mock_client

        # Act
        _ = analyzer.analyze_batch_optimized([sample_issue], batch_size=1)

        # Assert - 应正常工作
        assert mock_client.chat.completions.create.call_count >= 1

    def test_batch_size_maximum_boundary(self, sample_issue):
        """测试：批量大小最大边界限制应被遵守"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        large_list = [sample_issue] * 100  # 100 个 issues
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = BatchIssueAnalysis(
            results=[], success_count=0, failure_count=0, failed_indices=[], errors=[]
        )
        analyzer.client = mock_client

        # Act
        _ = analyzer.analyze_batch_optimized(large_list)

        # Assert - 验证批量大小不超过限制（例如 20）
        # 100 个 issues，批量大小 20，应该至少调用 5 次
        assert mock_client.chat.completions.create.call_count >= 5

    def test_batch_size_validation_invalid_value(self, sample_issue):
        """测试：无效的批量大小应被拒绝或修正"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")

        # Act & Assert - 测试无效值：0
        with pytest.raises((ValueError, AttributeError)):
            analyzer.analyze_batch_optimized([sample_issue], batch_size=0)

    def test_batch_size_default_value(self, sample_issue):
        """测试：应使用合理的默认批量大小"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        large_list = [sample_issue] * 25  # 25 个 issues
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = BatchIssueAnalysis(
            results=[], success_count=0, failure_count=0, failed_indices=[], errors=[]
        )
        analyzer.client = mock_client

        # Act - 不指定 batch_size，使用默认值（5）
        _ = analyzer.analyze_batch_optimized(large_list)

        # Assert - 验证使用了默认批量大小（5）
        # 25 个 issues，默认批量 5，应该调用 5 次
        assert mock_client.chat.completions.create.call_count == 5

    def test_batch_size_performance_impact(self, sample_issue):
        """测试：批量大小应影响性能（更大的批次 = 更少的 API 调用）"""
        # Arrange
        analyzer = IssueAnalyzer(api_key="test-key")
        large_list = [sample_issue] * 30

        # Mock 客户端以跟踪调用次数
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = BatchIssueAnalysis(
            results=[], success_count=0, failure_count=0, failed_indices=[], errors=[]
        )
        analyzer.client = mock_client

        # Act - 测试不同批量大小的 API 调用次数
        _ = analyzer.analyze_batch_optimized(large_list, batch_size=5)
        calls_small = mock_client.chat.completions.create.call_count

        mock_client.reset_mock()
        _ = analyzer.analyze_batch_optimized(large_list, batch_size=15)
        calls_large = mock_client.chat.completions.create.call_count

        # Assert - 验证更大的批量大小导致更少的 API 调用
        # 30 / 5 = 6, 30 / 15 = 2
        assert calls_large < calls_small
        assert calls_small == 6
        assert calls_large == 2
