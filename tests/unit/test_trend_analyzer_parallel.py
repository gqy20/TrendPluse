"""TrendAnalyzer 并行化测试

使用 TDD 方法测试 PR 分析的并行处理功能。
"""

import time
from unittest.mock import MagicMock

import pytest

from trendpluse.analyzers.trend_analyzer import TrendAnalyzer
from trendpluse.models.signal import Signal


class TestTrendAnalyzerParallel:
    """TrendAnalyzer 并行处理测试类"""

    @pytest.fixture
    def mock_signal(self):
        """Mock API 响应 - 返回一个信号"""
        return Signal(
            id="test-1",
            title="测试 PR",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="这是一个测试 PR",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

    @pytest.fixture
    def sample_prs(self):
        """示例 PR 数据"""
        return [
            {
                "repo_name": f"test/repo{i}",
                "number": i,
                "title": f"Test PR {i}",
                "body": f"Test body {i}",
                "author": f"user{i}",
                "url": f"https://github.com/test/repo{i}/pull/{i}",
            }
            for i in range(6)
        ]

    def test_analyze_prs_accepts_max_workers_parameter(self):
        """测试：analyze_prs 方法应接受 max_workers 参数"""
        analyzer = TrendAnalyzer(
            api_key="test-key",
        )

        import inspect

        sig = inspect.signature(analyzer.analyze_prs)
        params = list(sig.parameters.keys())

        assert "max_workers" in params, "analyze_prs 应接受 max_workers 参数"

    def test_analyze_prs_parallel_speedup(self, sample_prs, mock_signal):
        """测试：并行处理应比串行处理更快"""
        # 创建 mock 客户端
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_with_delay(*args, **kwargs):
            call_count[0] += 1
            time.sleep(0.05)  # 模拟 API 延迟
            return mock_signal

        mock_client.chat.completions.create.side_effect = mock_create_with_delay

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        # 串行处理（max_workers=1）
        call_count[0] = 0
        start = time.time()
        signals_serial = analyzer.analyze_prs(sample_prs, max_workers=1)
        serial_time = time.time() - start

        # 并行处理（max_workers=3）
        call_count[0] = 0
        start = time.time()
        signals_parallel = analyzer.analyze_prs(sample_prs, max_workers=3)
        parallel_time = time.time() - start

        # 验证结果一致
        assert len(signals_serial) == len(signals_parallel)
        assert len(signals_serial) == 6

        # 并行应该更快（至少快 1.3 倍，考虑到开销）
        assert parallel_time < serial_time / 1.3, (
            f"并行处理 ({parallel_time:.2f}s) 应该显著快于串行 ({serial_time:.2f}s)"
        )

    def test_analyze_prs_empty_list_with_max_workers(self):
        """测试：空列表时 max_workers 参数不应导致错误"""
        analyzer = TrendAnalyzer(api_key="test-key")

        signals = analyzer.analyze_prs([], max_workers=3)

        assert signals == []

    def test_analyze_prs_single_pr_with_max_workers(self, mock_signal):
        """测试：单个 PR 时 max_workers=3 应正常工作"""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_signal

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        pr = {
            "repo_name": "test/repo",
            "number": 1,
            "title": "Test PR",
            "body": "Test body",
            "author": "user1",
            "url": "https://github.com/test/repo/pull/1",
        }

        signals = analyzer.analyze_prs([pr], max_workers=3)

        assert len(signals) == 1

    def test_analyze_prs_handles_individual_failures_gracefully(self, mock_signal):
        """测试：单个 PR 失败不应影响其他 PRs"""
        mock_client = MagicMock()

        call_count = [0]

        def mock_create_sometimes_fails(*args, **kwargs):
            call_count[0] += 1
            time.sleep(0.02)  # 模拟 API 延迟
            # 第 3 个调用失败
            if call_count[0] == 3:
                raise Exception("模拟 API 失败")
            return mock_signal

        mock_client.chat.completions.create.side_effect = mock_create_sometimes_fails

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        prs = [
            {
                "repo_name": f"test/repo{i}",
                "number": i,
                "title": f"Test PR {i}",
                "body": "Test body",
                "author": f"user{i}",
                "url": f"https://github.com/test/repo{i}/pull/{i}",
            }
            for i in range(5)
        ]

        signals = analyzer.analyze_prs(prs, max_workers=3)

        # 应该成功处理至少 4 个（1 个失败）
        assert len(signals) >= 4

    def test_analyze_prs_default_max_workers(self, sample_prs, mock_signal):
        """测试：不提供 max_workers 时应使用默认值"""
        mock_client = MagicMock()
        mock_client.chat.completions.create.return_value = mock_signal

        analyzer = TrendAnalyzer(api_key="test-key")
        analyzer.client = mock_client

        # 应该能正常调用（使用默认 max_workers）
        signals = analyzer.analyze_prs(sample_prs)

        assert len(signals) == 6
