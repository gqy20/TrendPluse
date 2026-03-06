"""SignalDeduplicator 单元测试

测试信号去重器的核心功能。
"""

from datetime import UTC, datetime, timedelta
from unittest.mock import MagicMock

import pytest

from trendpluse.models.signal import Signal


def _build_signal(**overrides) -> Signal:
    """构造测试用信号。"""
    defaults = {
        "id": "signal-1",
        "title": "测试信号",
        "type": "capability",
        "category": "engineering",
        "impact_score": 4,
        "why_it_matters": "测试",
        "sources": ["https://github.com/test/repo/pull/1"],
        "related_repos": ["test/repo"],
    }
    defaults.update(overrides)
    return Signal(**defaults)


def _mock_llm_result(mock_llm_client, text: str) -> None:
    """配置 LLM 返回结果。"""
    mock_llm_client.messages.create.return_value = MagicMock(
        content=[MagicMock(text=text)]
    )


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
        import uuid

        from trendpluse.analyzers.signal_deduplicator import SignalDeduplicator

        # 使用唯一路径避免测试间互相干扰
        unique_path = f"/tmp/test_signal_history_{uuid.uuid4().hex[:8]}.json"

        return SignalDeduplicator(
            llm_client=mock_llm_client,
            lookback_days=7,
            history_path=unique_path,
        )

    @pytest.fixture
    def sample_signals(self):
        """创建示例信号"""
        return [
            _build_signal(
                id="signal-1",
                title="Agent 上下文感知",
                impact_score=5,
                why_it_matters="AI Agent 从被动执行向主动感知演进",
                sources=["https://github.com/test/repo/pull/123"],
            ),
            _build_signal(
                id="signal-2",
                title="Agent 安全增强",
                type="safety",
                impact_score=4,
                why_it_matters="提升 AI Agent 安全性",
                sources=["https://github.com/test/repo/pull/124"],
            ),
            _build_signal(
                id="signal-3",
                title="Agent 上下文感知",
                impact_score=5,
                why_it_matters="AI Agent 从被动执行向主动感知演进",
                sources=["https://github.com/test/repo/pull/125"],
            ),
        ]

    def test_init_creates_deduplicator(self, deduplicator):
        """测试：正确初始化去重器"""
        # Assert
        assert deduplicator.lookback_days == 7
        # history_path_str 应该以 /tmp/test_signal_history_ 开头
        assert deduplicator.history_path_str.startswith("/tmp/test_signal_history_")
        assert deduplicator.history_path_str.endswith(".json")

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
        similar_signal = _build_signal(
            id="signal-new",
            title="Agent 上下文",  # 与 "Agent 上下文感知" 相似
            impact_score=5,
            why_it_matters="测试",
            sources=["https://github.com/test/repo/pull/126"],
        )

        history = [sample_signals[0]]

        # Mock LLM 返回非重复
        _mock_llm_result(mock_llm_client, "UNIQUE")

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
        _mock_llm_result(mock_llm_client, "DUPLICATE")

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
        from pathlib import Path

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            history_path = f.name

        deduplicator.history_path_str = history_path
        deduplicator.history_path = Path(history_path)

        # Mock LLM 返回非重复
        _mock_llm_result(mock_llm_client, "UNIQUE")

        # Act
        deduplicator.deduplicate(sample_signals)

        # Assert
        import json

        with open(history_path) as f:
            saved_data = json.load(f)

        # signal-1 和 signal-3 是重复的，deduplicate 只保存了 2 个
        assert len(saved_data["signals"]) == 2
        assert saved_data["signals"][0]["title"] == "Agent 上下文感知"

    def test_load_history_returns_signals(self, deduplicator, sample_signals, tmp_path):
        """测试：应能从文件加载历史信号"""
        # Arrange
        import json
        import tempfile
        from pathlib import Path

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

        deduplicator.history_path_str = history_path
        deduplicator.history_path = Path(history_path)

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

        # 使用 object.__setattr__ 设置 _timestamp 属性（用于测试）
        object.__setattr__(
            old_signal, "_timestamp", (base_time - timedelta(days=10)).isoformat()
        )

        recent_signals = sample_signals  # 默认没有 _timestamp，视为最近

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
        new_signal = _build_signal(
            id="new",
            title="Agent 优化",
            impact_score=4,
            why_it_matters="测试",
            sources=["https://github.com/test/new"],
        )

        existing_signal = _build_signal(
            id="existing",
            title="Agent 改进",
            impact_score=4,
            why_it_matters="测试",
            sources=["https://github.com/test/existing"],
        )

        # Mock LLM 返回重复
        _mock_llm_result(mock_llm_client, "DUPLICATE")

        # Act
        is_dup = deduplicator._llm_check_duplicate(new_signal, [existing_signal])

        # Assert
        assert is_dup is True

    def test_llm_check_duplicate_returns_false_for_unique(
        self, deduplicator, mock_llm_client
    ):
        """测试：LLM 应正确识别非重复信号"""
        # Arrange
        new_signal = _build_signal(
            id="new",
            title="Agent 上下文感知",
            impact_score=5,
            why_it_matters="新特性",
            sources=["https://github.com/test/new"],
        )

        existing_signal = _build_signal(
            id="existing",
            title="Agent 安全增强",
            type="safety",
            impact_score=4,
            why_it_matters="安全改进",
            sources=["https://github.com/test/existing"],
        )

        # Mock LLM 返回非重复
        _mock_llm_result(mock_llm_client, "UNIQUE")

        # Act
        is_dup = deduplicator._llm_check_duplicate(new_signal, [existing_signal])

        # Assert
        assert is_dup is False

    # ==================== 跨类型去重测试 ====================

    def test_deduplicate_cross_type_pr_and_commit_signals(
        self, deduplicator, mock_llm_client
    ):
        """测试：PR 和 Commit 描述同一趋势时应合并为一个信号"""
        # Arrange
        # PR 提取的信号
        pr_signal = _build_signal(
            id="pr-1",
            title="流式处理支持",
            impact_score=5,
            why_it_matters="音频流处理能力",
            sources=["https://github.com/test/repo/pull/123"],
        )

        # Commit 提取的信号（描述同一趋势）
        commit_signal = _build_signal(
            id="commit-1",
            title="音频流处理支持",  # 标题略有不同但本质相同
            impact_score=4,
            why_it_matters="实现音频流功能",
            sources=["https://github.com/test/repo/commit/abc123"],
        )

        # Mock LLM 返回重复
        _mock_llm_result(mock_llm_client, "DUPLICATE")

        # Act
        unique_signals = deduplicator.deduplicate([pr_signal, commit_signal])

        # Assert - 应该合并为 1 个信号
        assert len(unique_signals) == 1
        # 应该聚合两个来源
        assert len(unique_signals[0].sources) == 2
        assert any("/pull/123" in s for s in unique_signals[0].sources)
        assert any("/commit/abc123" in s for s in unique_signals[0].sources)

    def test_deduplicate_keeps_highest_impact_score(
        self, deduplicator, mock_llm_client
    ):
        """测试：合并时应保留影响评分最高的信号"""
        # Arrange
        low_score_signal = _build_signal(
            id="low",
            title="MCP 集成",
            impact_score=3,
            why_it_matters="低评分",
            sources=["https://github.com/test/repo/commit/low"],
        )

        high_score_signal = _build_signal(
            id="high",
            title="MCP 资源协议集成",
            impact_score=5,
            why_it_matters="高评分",
            sources=["https://github.com/test/repo/pull/high"],
        )

        # Mock LLM 返回重复
        _mock_llm_result(mock_llm_client, "DUPLICATE")

        # Act
        unique_signals = deduplicator.deduplicate([low_score_signal, high_score_signal])

        # Assert
        assert len(unique_signals) == 1
        # 应该保留高评分的信号
        assert unique_signals[0].impact_score == 5
        assert unique_signals[0].id == "high"

    def test_deduplicate_aggregates_all_sources(self, deduplicator, mock_llm_client):
        """测试：合并时应聚合所有来源"""
        # Arrange
        pr_signal = _build_signal(
            id="pr-1",
            title="RAG 优化",
            type="performance",
            impact_score=4,
            why_it_matters="检索增强",
            sources=["https://github.com/test/repo/pull/100"],
        )

        commit_signal_1 = _build_signal(
            id="commit-1",
            title="RAG 性能优化",
            type="performance",
            impact_score=4,
            why_it_matters="提升检索速度",
            sources=["https://github.com/test/repo/commit/aaa"],
        )

        commit_signal_2 = _build_signal(
            id="commit-2",
            title="RAG 优化",
            type="performance",
            impact_score=3,
            why_it_matters="缓存优化",
            sources=["https://github.com/test/repo/commit/bbb"],
        )

        # Mock LLM 返回重复
        _mock_llm_result(mock_llm_client, "DUPLICATE")

        # Act
        unique_signals = deduplicator.deduplicate(
            [pr_signal, commit_signal_1, commit_signal_2]
        )

        # Assert
        assert len(unique_signals) == 1
        # 应该聚合所有 3 个来源
        assert len(unique_signals[0].sources) == 3
        assert any("/pull/100" in s for s in unique_signals[0].sources)
        assert any("/commit/aaa" in s for s in unique_signals[0].sources)
        assert any("/commit/bbb" in s for s in unique_signals[0].sources)

    def test_fingerprint_ignores_signal_type_for_deduplication(self, deduplicator):
        """测试：指纹计算应忽略信号类型，只基于业务本质"""
        # Arrange
        # PR 信号
        signal_from_pr = Signal(
            id="pr-1",
            title="MCP 集成",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters="协议支持",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        # Commit 信号（业务类型相同）
        signal_from_commit = Signal(
            id="commit-1",
            title="MCP 集成",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="协议实现",
            sources=["https://github.com/test/repo/commit/abc"],
            related_repos=["test/repo"],
        )

        # Act
        fingerprint_pr = deduplicator.compute_fingerprint(signal_from_pr)
        fingerprint_commit = deduplicator.compute_fingerprint(signal_from_commit)

        # Assert - 指纹应该相同（因为业务本质相同）
        assert fingerprint_pr == fingerprint_commit

    def test_deduplicate_pr_commit_release_same_trend(
        self, deduplicator, mock_llm_client
    ):
        """测试：PR、Commit、Release 描述同一趋势时应合并"""
        # Arrange
        pr_signal = Signal(
            id="pr-1",
            title="工作流引擎重构",
            type="abstraction",
            category="engineering",
            impact_score=5,
            why_it_matters="架构改进",
            sources=["https://github.com/test/repo/pull/50"],
            related_repos=["test/repo"],
        )

        commit_signal = Signal(
            id="commit-1",
            title="重构工作流引擎",
            type="abstraction",
            category="engineering",
            impact_score=4,
            why_it_matters="代码清理",
            sources=["https://github.com/test/repo/commit/xyz"],
            related_repos=["test/repo"],
        )

        release_signal = Signal(
            id="release-1",
            title="工作流引擎发布",
            type="abstraction",
            category="engineering",
            impact_score=5,
            why_it_matters="v2.0 发布",
            sources=["https://github.com/test/repo/releases/tag/v2.0.0"],
            related_repos=["test/repo"],
        )

        # Mock LLM 返回重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="DUPLICATE")]
        )

        # Act
        unique_signals = deduplicator.deduplicate(
            [pr_signal, commit_signal, release_signal]
        )

        # Assert
        assert len(unique_signals) == 1
        # 应该聚合 3 个来源
        assert len(unique_signals[0].sources) == 3
        assert any("/pull/50" in s for s in unique_signals[0].sources)
        assert any("/commit/xyz" in s for s in unique_signals[0].sources)
        assert any("/releases/tag/v2.0.0" in s for s in unique_signals[0].sources)

    def test_deduplicate_different_trends_not_merged(
        self, deduplicator, mock_llm_client
    ):
        """测试：不同趋势不应被合并"""
        # Arrange
        signal_1 = Signal(
            id="s1",
            title="MCP 集成",
            type="capability",
            category="engineering",
            impact_score=4,
            why_it_matters="协议支持",
            sources=["https://github.com/test/repo/pull/1"],
            related_repos=["test/repo"],
        )

        signal_2 = Signal(
            id="s2",
            title="RAG 优化",
            type="performance",
            category="engineering",
            impact_score=4,
            why_it_matters="检索增强",
            sources=["https://github.com/test/repo/pull/2"],
            related_repos=["test/repo"],
        )

        # Mock LLM 返回非重复
        mock_llm_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="UNIQUE")]
        )

        # Act
        unique_signals = deduplicator.deduplicate([signal_1, signal_2])

        # Assert
        assert len(unique_signals) == 2
        # 信号不应被合并
        assert len(unique_signals[0].sources) == 1
        assert len(unique_signals[1].sources) == 1
