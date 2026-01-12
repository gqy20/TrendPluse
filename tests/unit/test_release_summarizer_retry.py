"""ReleaseSummarizer 重试机制测试

使用 TDD 方法测试 AI 调用失败后的自动重试功能。
"""

from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.models.signal import ReleaseSummary


class TestReleaseSummarizerRetry:
    """ReleaseSummarizer 重试机制测试类"""

    @pytest.fixture
    def mock_summary(self):
        """Mock API 响应"""
        return ReleaseSummary(
            change_type="feature",
            key_changes=["测试变更"],
            summary_cn="这是一个测试总结",
            impact_level=3,
        )

    def test_retry_on_transient_failure(self, mock_summary):
        """测试：临时失败时应重试并最终成功"""
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_fails_then_succeeds(*args, **kwargs):
            call_count[0] += 1
            # 前两次失败，第三次成功
            if call_count[0] < 3:
                from anthropic import APITimeoutError

                raise APITimeoutError("模拟 API 超时")
            return mock_summary

        mock_client.chat.completions.create.side_effect = (
            mock_create_fails_then_succeeds
        )

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        release = {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "body": "Test release notes",
        }

        # 应该在重试后成功
        summary = summarizer._summarize_single_release(release)

        # 验证调用了 3 次（初始调用 + 2 次重试）
        assert call_count[0] == 3
        assert summary.change_type == "feature"

    def test_retry_exhausted_gives_up(self):
        """测试：超过最大重试次数后应放弃并返回默认值"""
        mock_client = MagicMock()

        def mock_create_always_fails(*args, **kwargs):
            from anthropic import APITimeoutError

            raise APITimeoutError("持续 API 超时")

        mock_client.chat.completions.create.side_effect = mock_create_always_fails

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        release = {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "body": "Test release notes",
        }

        # 应该在重试耗尽后返回默认值
        summary = summarizer._summarize_single_release(release)

        # 验证返回了默认值
        assert summary.change_type == "other"
        assert "分析失败" in summary.summary_cn or "发布" in summary.summary_cn

    def test_no_retry_on_permanent_error(self):
        """测试：永久性错误不应重试（如认证错误）"""
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_auth_error(*args, **kwargs):
            call_count[0] += 1
            from anthropic import AuthenticationError

            raise AuthenticationError("无效的 API 密钥")

        mock_client.chat.completions.create.side_effect = mock_create_auth_error

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        release = {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "body": "Test release notes",
        }

        # 认证错误应该快速失败（不重试或只重试一次）
        try:
            summarizer._summarize_single_release(release)
        except Exception:
            pass

        # 验证只调用了一次（没有重试）
        assert call_count[0] == 1
