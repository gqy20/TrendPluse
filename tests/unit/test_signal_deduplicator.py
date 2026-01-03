"""SignalDeduplicator 单元测试

测试信号去重器的核心功能。
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest

from trendpluse.models.signal import Signal


class TestSignalDeduplicator:
    """SignalDeduplicator 测试类"""

    @pytest.fixture
    def mock_llm_client(self):
        """Mock LLM 客户端"""
        client = MagicMock()
        return client

    @pytest.fixture
    def deduplicator(self, mock_llm_client):
        """创建去重器实例"""
        from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator

        return SignalDeduplicator(
            llm_client=mock_llm_client,
            lookback_days=7,
            history_path="/tmp/test_signal_history.json",
        )

    @pytest.fixture
    def sample_signals(self):
        """创建示例信号"""
        return [
            Signal(
                id="signal-1",
                title="Agent 上下文感知",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="AI Agent 从被动执行向主动感知演进",
                sources=["https://github.com/test/repo/pull/123"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="signal-2",
                title="Agent 安全增强",
                type="safety",
                category="engineering",
                impact_score=4,
                why_it_matters="提升 AI Agent 安全性",
                sources=["https://github.com/test/repo/pull/124"],
                related_repos=["test/repo"],
            ),
            Signal(
                id="signal-3",
                title="Agent 上下文感知",
                type="capability",
                category="engineering",
                impact_score=5,
                why_it_matters="AI Agent 从被动执行向主动感知演进",
                sources=["https://github.com/test/repo/pull/125"],
                related_repos=["test/repo"],
            ),
        ]

    def test_init_creates_deduplicator(self, deduplicator):
        """测试：正确初始化去重器"""
        # Assert
        assert deduplicator.lookback_days == 7
        assert deduplicator.history_path == "/tmp/test_signal_history.json"

    def test_compute_fingerprint_same_signal(self, deduplicator, sample_signals):
        """测试：相同信号应产生相同指纹"""
        # Arrange
        signal1 = sample_signals[0]
        signal3 = sample_signals[2]  # 与 signal1 标题相同

        # Act
        fingerprint1 = deduplicator.compute_fingerprint(signal1)
        fingerprint3 = deduplicator.compute_fingerprint(signal3)

        # Assert
        assert fingerprint1 == fingerprint3

    def test_compute_fingerprint_different_signal(self, deduplicator, sample_signals):
        """测试：不同信号应产生不同指纹"""
        # Arrange
        signal1 = sample_signals[0]
        signal2 = sample_signals[1]

        # Act
        fingerprint1 = deduplicator.compute_fingerprint(signal1)
        fingerprint2 = deduplicator.compute_fingerprint(signal2)

        # Assert
        assert fingerprint1 != fingerprint2

    def test_is_duplicate_with_exact_fingerprint_match(
        self, deduplicator, sample_signals
    ):
        """测试：指纹完全匹配应判定为重复"""
        # Arrange
        new_signal = sample_signals[2]  # 与 signal-1 标题相同
        history = [sample_signals[0]]  # signal-1 在历史中

        # Act
        is_dup = deduplicator._is_duplicate(new_signal, history)

        # Assert
        assert is_dup is True

    def test_is_duplicate_with_different_fingerprint(
        self, deduplicator, sample_signals
    ):
        """测试：指纹不同应判定为不重复"""
        # Arrange
        new_signal = sample_signals[1]  # "Agent 安全增强"
        history = [sample_signals[0]]  # "Agent 上下文感知"

        # Act
        is_dup = deduplicator._is_duplicate(new_signal, history)

        # Assert
        assert is_dup is False

    def test_is_duplicate_calls_llm_for_similar_titles(
        self, deduplicator, sample_signals, mock_llm_client
    ):
        """测试：标题相似时应调用 LLM 判断"""
        # Arrange
        # 创建一个标题相似的信号（编辑距离 <= 2）
        similar_signal = Signal(
            id="signal-new",
            title="Agent 上下文",  # 与 "Agent 上下文感知" 相似
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="测试",
            sources=["https://github.com/test/repo/pull/126"],
            related_repos=["test/repo"],
        )

        history = [sample_signals[0]]

        # Mock LLM 返回非重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="UNIQUE")]
        )

        # Act
        is_dup = deduplicator._is_duplicate(similar_signal, history)

        # Assert
        assert is_dup is False
        # 验证 LLM 被调用
        mock_llm_client.messages.create.assert_called_once()

    def test_deduplicate_removes_duplicates(
        self, deduplicator, sample_signals, mock_llm_client
    ):
        """测试：去重应移除重复信号"""
        # Arrange
        # Mock LLM 返回重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="DUPLICATE")]
        )

        # Act
        unique_signals = deduplicator.deduplicate(sample_signals)

        # Assert
        # signal-1 和 signal-3 是重复的，应该只保留一个
        assert len(unique_signals) == 2
        # 验证保留的是第一个
        assert unique_signals[0].id == "signal-1"
        assert unique_signals[1].id == "signal-2"

    def test_deduplicate_saves_to_history(
        self, deduplicator, sample_signals, mock_llm_client, tmp_path
    ):
        """测试：去重后应保存到历史文件"""
        # Arrange
        import tempfile

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            history_path = f.name

        deduplicator.history_path = history_path

        # Mock LLM 返回非重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="UNIQUE")]
        )

        # Act
        deduplicator.deduplicate(sample_signals)

        # Assert
        import json

        with open(history_path) as f:
            saved_data = json.load(f)

        assert len(saved_data["signals"]) == 3
        assert saved_data["signals"][0]["title"] == "Agent 上下文感知"

    def test_load_history_returns_signals(self, deduplicator, sample_signals, tmp_path):
        """测试：应能从文件加载历史信号"""
        # Arrange
        import json
        import tempfile

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            history_path = f.name
            # 保存测试数据
            json.dump(
                {
                    "signals": [
                        {
                            "id": "old-signal",
                            "title": "旧信号",
                            "type": "capability",
                            "category": "engineering",
                            "impact_score": 3,
                            "why_it_matters": "旧",
                            "sources": ["https://github.com/test/old"],
                            "related_repos": ["test/repo"],
                            "timestamp": (
                                datetime.now(UTC) - timedelta(days=1)
                            ).isoformat(),
                        }
                    ],
                    "last_updated": datetime.now(UTC).isoformat(),
                },
                f,
            )

        deduplicator.history_path = history_path

        # Act
        history = deduplicator._load_history()

        # Assert
        assert len(history) == 1
        assert history[0].title == "旧信号"

    def test_filter_old_signals_removes_expired(self, deduplicator, sample_signals):
        """测试：应过滤超过时间窗口的旧信号"""
        # Arrange
        base_time = datetime.now(UTC)

        old_signal = Signal(
            id="old",
            title="旧信号",
            type="capability",
            category="engineering",
            impact_score=3,
            why_it_matters="测试",
            sources=["https://github.com/test/old"],
            related_repos=["test/repo"],
        )

        # 添加时间戳属性（用于测试）
        old_signal.timestamp = (base_time - timedelta(days=10)).isoformat()

        recent_signals = sample_signals  # 默认没有 timestamp，视为最近

        all_signals = [old_signal] + recent_signals

        # Act
        filtered = deduplicator._filter_old_signals(all_signals)

        # Assert
        # 旧信号应被过滤掉
        assert len(filtered) == 3
        assert all(s.id != "old" for s in filtered)

    def test_llm_check_duplicate_returns_true_for_duplicate(
        self, deduplicator, mock_llm_client
    ):
        """测试：LLM 应正确识别重复信号"""
        # Arrange
        new_signal = Signal(
            id="new",
            title="Agent 优化",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="测试",
            sources=["https://github.com/test/new"],
            related_repos=["test/repo"],
        )

        existing_signal = Signal(
            id="existing",
            title="Agent 改进",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="测试",
            sources=["https://github.com/test/existing"],
            related_repos=["test/repo"],
        )

        # Mock LLM 返回重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="DUPLICATE")]
        )

        # Act
        is_dup = deduplicator._llm_check_duplicate(new_signal, [existing_signal])

        # Assert
        assert is_dup is True

    def test_llm_check_duplicate_returns_false_for_unique(
        self, deduplicator, mock_llm_client
    ):
        """测试：LLM 应正确识别非重复信号"""
        # Arrange
        new_signal = Signal(
            id="new",
            title="Agent 上下文感知",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="新特性",
            sources=["https://github.com/test/new"],
            related_repos=["test/repo"],
        )

        existing_signal = Signal(
            id="existing",
            title="Agent 安全增强",
            type="safety",
            category="engineering",
            impact_score=4,
            why_it_matters="安全改进",
            sources=["https://github.com/test/existing"],
            related_repos=["test/repo"],
        )

        # Mock LLM 返回非重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="UNIQUE")]
        )

        # Act
        is_dup = deduplicator._llm_check_duplicate(new_signal, [existing_signal])

        # Assert
        assert is_dup is False
