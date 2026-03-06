"""ReleaseSummarizer 并行化测试

使用 TDD 方法测试 Release 总结的并行处理功能。
"""

import time
from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.release_summarizer import ReleaseSummarizer
from trendpluse.models.signal import ReleaseSummary
from trendpluse.models.source import AnalysisMaterial


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

    def test_summarize_materials_accepts_max_workers_parameter(self):
        """测试：summarize_materials 方法应接受 max_workers 参数"""
        summarizer = ReleaseSummarizer(
            api_key="test-key",
        )

        import inspect

        sig = inspect.signature(summarizer.summarize_materials)
        params = list(sig.parameters.keys())

        assert "max_workers" in params, "summarize_materials 应接受 max_workers 参数"

    def test_summarize_materials_parallel_speedup(self, mock_summary):
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

        materials = [
            AnalysisMaterial.from_release_details(
                {
                    "repo": f"test/repo{i}",
                    "tag_name": f"v1.0.{i}",
                    "body": f"Release notes for version {i}",
                }
            )
            for i in range(6)
        ]

        # 串行处理（max_workers=1）
        call_count[0] = 0
        start = time.time()
        summaries_serial = summarizer.summarize_materials(materials, max_workers=1)
        serial_time = time.time() - start

        # 并行处理（max_workers=3）
        call_count[0] = 0
        start = time.time()
        summaries_parallel = summarizer.summarize_materials(materials, max_workers=3)
        parallel_time = time.time() - start

        # 验证结果一致
        assert len(summaries_serial) == len(summaries_parallel)
        assert len(summaries_serial) == 6

        # 并行应该更快（至少快 1.3 倍，考虑到开销）
        assert parallel_time < serial_time / 1.3, (
            f"并行处理 ({parallel_time:.2f}s) 应该显著快于串行 ({serial_time:.2f}s)"
        )

    def test_summarize_materials_empty_list_with_max_workers(self):
        """测试：空列表时 max_workers 参数不应导致错误"""
        summarizer = ReleaseSummarizer(api_key="test-key")

        summaries = summarizer.summarize_materials([], max_workers=3)

        assert summaries == {}

    def test_summarize_materials_single_release_with_max_workers(self):
        """测试：单个 release 材料时 max_workers=3 应正常工作"""
        summarizer = ReleaseSummarizer(api_key="test-key")

        materials = [
            AnalysisMaterial.from_release_details(
                {"repo": "test/repo", "tag_name": "v1.0.0", "body": ""}
            )
        ]

        summaries = summarizer.summarize_materials(materials, max_workers=3)

        assert len(summaries) == 1
        assert "test/repo@v1.0.0" in summaries

    def test_summarize_materials_handles_individual_failures_gracefully(
        self, mock_summary
    ):
        """测试：单个 release 失败不应影响其他 releases"""
        from unittest.mock import patch

        summarizer = ReleaseSummarizer(api_key="test-key")

        def mock_summarize_with_one_failure(release):
            """Mock 方法：test/repo2 失败"""
            time.sleep(0.02)  # 模拟 API 延迟
            # test/repo2 失败
            if release["repo"] == "test/repo2":
                raise Exception("模拟 API 失败")
            # 其他返回成功
            return mock_summary

        with patch.object(
            summarizer,
            "_summarize_single_release",
            side_effect=mock_summarize_with_one_failure,
        ):
            materials = [
                AnalysisMaterial.from_release_details(
                    {
                        "repo": f"test/repo{i}",
                        "tag_name": f"v1.0.{i}",
                        "body": "test",
                    }
                )
                for i in range(5)
            ]

            summaries = summarizer.summarize_materials(materials, max_workers=3)

            # 所有 5 个都应有结果（失败的返回默认值）
            assert len(summaries) == 5
            # 其中 4 个是成功的（change_type='feature'），1 个是默认值
            success_count = sum(
                1
                for s in summaries.values()
                if s is not None and s.change_type == "feature"
            )
            assert success_count == 4, f"应该有 4 个成功，实际有 {success_count} 个"

    def test_summarize_materials_default_max_workers(self, mock_summary):
        """测试：不提供 max_workers 时应使用默认值"""
        # 创建 mock 客户端
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_summary

        summarizer = ReleaseSummarizer(api_key="test-key")
        summarizer.client = mock_client

        materials = [
            AnalysisMaterial.from_release_details(
                {"repo": "test/repo", "tag_name": "v1.0.0", "body": "test"}
            )
        ]

        # 应该能正常调用（使用默认 max_workers）
        summaries = summarizer.summarize_materials(materials)

        assert len(summaries) == 1
