"""ReleaseSummarizer 并行化测试

使用 TDD 方法测试 Release 总结的并行处理功能。
"""

import time
from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.models.signal import ReleaseSummary


class TestReleaseSummarizerParallel:
    """ReleaseSummarizer 并行处理测试类"""

    @pytest.fixture
    def mock_summary(self):
        """Mock API 响应"""
        return ReleaseSummary(
            change_type="feature",
            key_changes=["测试变更"],
            summary_cn="这是一个测试总结",
            impact_level=3,
        )

    def test_summarize_releases_accepts_max_workers_parameter(self):
        """测试：summarize_releases 方法应接受 max_workers 参数"""
        summarizer = ReleaseSummarizer(
            api_key="test-key",
        )

        import inspect

        sig = inspect.signature(summarizer.summarize_releases)
        params = list(sig.parameters.keys())

        assert "max_workers" in params, "summarize_releases 应接受 max_workers 参数"

    def test_summarize_releases_parallel_speedup(self, mock_summary):
        """测试：并行处理应比串行处理更快"""
        # 创建 mock 客户端
        mock_client = MagicMock()

        # 创建带有延迟的 mock
        call_count = [0]

        def mock_create_with_delay(*args, **kwargs):
            call_count[0] += 1
            time.sleep(0.05)  # 模拟 API 延迟
            return mock_summary

        mock_client.chat.completions.create.side_effect = mock_create_with_delay

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        releases = [
            {
                "repo": f"test/repo{i}",
                "tag_name": f"v1.0.{i}",
                "body": f"Release notes for version {i}",
            }
            for i in range(6)  # 6 个 releases
        ]

        # 串行处理（max_workers=1）
        call_count[0] = 0
        start = time.time()
        summaries_serial = summarizer.summarize_releases(  # type: ignore[call-arg]
            releases, max_workers=1
        )
        serial_time = time.time() - start

        # 并行处理（max_workers=3）
        call_count[0] = 0
        start = time.time()
        summaries_parallel = summarizer.summarize_releases(  # type: ignore[call-arg]
            releases, max_workers=3
        )
        parallel_time = time.time() - start

        # 验证结果一致
        assert len(summaries_serial) == len(summaries_parallel)
        assert len(summaries_serial) == 6

        # 并行应该更快（至少快 1.3 倍，考虑到开销）
        assert parallel_time < serial_time / 1.3, (
            f"并行处理 ({parallel_time:.2f}s) 应该显著快于串行 ({serial_time:.2f}s)"
        )

    def test_summarize_releases_empty_list_with_max_workers(self):
        """测试：空列表时 max_workers 参数不应导致错误"""
        summarizer = ReleaseSummarizer(api_key="test-key")

        summaries = summarizer.summarize_releases([], max_workers=3)  # type: ignore[call-arg]

        assert summaries == {}

    def test_summarize_releases_single_release_with_max_workers(self):
        """测试：单个 release 时 max_workers=3 应正常工作"""
        summarizer = ReleaseSummarizer(api_key="test-key")

        release = {
            "repo": "test/repo",
            "tag_name": "v1.0.0",
            "body": "",
        }

        summaries = summarizer.summarize_releases([release], max_workers=3)  # type: ignore[call-arg]

        assert len(summaries) == 1
        assert "test/repo@v1.0.0" in summaries

    def test_summarize_releases_handles_individual_failures_gracefully(
        self, mock_summary
    ):  # type: ignore[no-any-unimported]
        """测试：单个 release 失败不应影响其他 releases"""
        # 创建 mock 客户端
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_sometimes_fails(*args, **kwargs):
            call_count[0] += 1
            time.sleep(0.02)  # 模拟 API 延迟
            # 第 3 个调用失败
            if call_count[0] == 3:
                raise Exception("模拟 API 失败")
            return mock_summary

        mock_client.chat.completions.create.side_effect = mock_create_sometimes_fails

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        releases = [
            {
                "repo": f"test/repo{i}",
                "tag_name": f"v1.0.{i}",
                "body": "test",
            }
            for i in range(5)
        ]

        summaries = summarizer.summarize_releases(releases, max_workers=3)  # type: ignore[call-arg]

        # 应该成功处理 4 个（1 个失败）
        assert len(summaries) == 4

    def test_summarize_releases_default_max_workers(self, mock_summary):
        """测试：不提供 max_workers 时应使用默认值"""
        # 创建 mock 客户端
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_summary

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        releases = [
            {
                "repo": "test/repo",
                "tag_name": "v1.0.0",
                "body": "test",
            }
        ]

        # 应该能正常调用（使用默认 max_workers）
        summaries = summarizer.summarize_releases(releases)

        assert len(summaries) == 1
