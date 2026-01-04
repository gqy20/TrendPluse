"""通知模块测试

测试通知器基类和飞书通知器。
"""

from unittest.mock import Mock, patch

import httpx
import pytest

from trendpluse.models.signal import (
    ActivityData,
    DailyReport,
    RepoActivity,
    Signal,
)
from trendpluse.notifiers.base import BaseNotifier
from trendpluse.notifiers.feishu import FeishuNotifier


class TestBaseNotifier:
    """测试 BaseNotifier 抽象基类"""

    def test_base_notifier_is_abstract(self):
        """BaseNotifier 不能直接实例化"""
        with pytest.raises(TypeError):
            BaseNotifier()

    def test_base_notifier_requires_send_method(self):
        """子类必须实现 send 方法"""

        class IncompleteNotifier(BaseNotifier):
            pass

        with pytest.raises(TypeError):
            IncompleteNotifier()


class TestFeishuNotifier:
    """测试 FeishuNotifier 飞书通知器"""

    def test_init_requires_webhook_url(self):
        """初始化需要 webhook_url"""
        with pytest.raises(ValueError):
            FeishuNotifier(webhook_url="")

    def test_build_card_generates_valid_structure(self, sample_report: DailyReport):
        """构建的卡片应符合飞书格式"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        # 验证基本结构
        assert card["msg_type"] == "interactive"
        assert "card" in card
        assert "header" in card["card"]
        assert "elements" in card["card"]

        # 验证 header
        header = card["card"]["header"]
        assert "title" in header
        assert header["title"]["tag"] == "plain_text"

        # 验证至少有元素
        assert len(card["card"]["elements"]) > 0

    def test_build_card_includes_highlights_section(self, sample_report: DailyReport):
        """卡片应包含高影响信号部分"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        elements = card["card"]["elements"]
        # 查找高影响信号部分（包含 "高影响信号" 或 "🔥"）
        has_highlights = any(
            "高影响信号" in str(el.get("text", {})) or "🔥" in str(el)
            for el in elements
        )
        assert has_highlights

    def test_build_card_includes_stats_section(self, sample_report: DailyReport):
        """卡片应包含统计信息部分"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        elements = card["card"]["elements"]
        has_stats = any("统计信息" in str(el) or "📊" in str(el) for el in elements)
        assert has_stats

    def test_build_card_includes_action_buttons(self, sample_report: DailyReport):
        """卡片应包含操作按钮"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        elements = card["card"]["elements"]
        # 查找 action 元素
        has_action = any(el.get("tag") == "action" for el in elements)
        assert has_action

    @patch("httpx.post")
    def test_send_report_success(self, mock_post: Mock, sample_report: DailyReport):
        """成功发送报告通知"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"StatusCode": 0, "StatusMessage": "success"}
        mock_post.return_value = mock_response

        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        result = notifier.send_report(sample_report)

        assert result is True
        mock_post.assert_called_once()

    @patch("httpx.post")
    def test_send_report_network_failure(
        self, mock_post: Mock, sample_report: DailyReport
    ):
        """网络失败时返回 False"""
        mock_post.side_effect = httpx.HTTPError("Network error")

        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        result = notifier.send_report(sample_report)

        assert result is False

    @patch("httpx.post")
    def test_send_report_api_error(self, mock_post: Mock, sample_report: DailyReport):
        """API 返回错误时返回 False"""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response

        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        result = notifier.send_report(sample_report)

        assert result is False

    def test_send_with_custom_at_mobiles(self, sample_report: DailyReport):
        """支持自定义 @ 提醒用户"""
        notifier = FeishuNotifier(
            webhook_url="https://example.com/webhook", at_mobiles=["13800138000"]
        )
        card = notifier._build_card(sample_report)

        # 验证卡片包含 @ 信息
        elements = card["card"]["elements"]
        # 查找包含手机号的元素
        has_at = any("13800138000" in str(el) for el in elements)
        assert has_at

    @patch("httpx.post")
    def test_send_with_signature(self, mock_post: Mock, sample_report: DailyReport):
        """支持签名验证"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        notifier = FeishuNotifier(
            webhook_url="https://example.com/webhook",
            secret="test_secret_123",
        )
        result = notifier.send_report(sample_report)

        assert result is True
        # 验证发送时包含了 timestamp 和 sign
        call_args = mock_post.call_args
        card = call_args.kwargs["json"]
        assert "timestamp" in card
        assert "sign" in card
        assert int(card["timestamp"]) > 0

    def test_gen_sign(self):
        """签名生成正确性"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        # 测试固定值
        timestamp = "1704067200"
        secret = "test_secret"
        sign = notifier._gen_sign(timestamp, secret)

        # 验证签名格式（base64）
        assert len(sign) > 0
        # 验证签名一致性
        sign2 = notifier._gen_sign(timestamp, secret)
        assert sign == sign2

    def test_gen_sign_different_inputs(self):
        """不同输入生成不同签名"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        sign1 = notifier._gen_sign("1704067200", "secret1")
        sign2 = notifier._gen_sign("1704067201", "secret1")
        sign3 = notifier._gen_sign("1704067200", "secret2")

        # 不同 timestamp 或 secret 应该产生不同签名
        assert sign1 != sign2
        assert sign1 != sign3


# ========== Fixtures ==========


@pytest.fixture
def sample_signal() -> Signal:
    """创建示例信号"""
    return Signal(
        id="test-signal-1",
        title="测试信号：新功能发布",
        type="capability",
        category="engineering",
        impact_score=5,
        why_it_matters="这是一个非常重要的功能更新",
        sources=["https://github.com/test/repo/pull/123"],
        related_repos=["test/repo"],
    )


@pytest.fixture
def sample_report() -> DailyReport:
    """创建示例日报"""
    # 创建不同评分的信号
    high_impact_signals = [
        Signal(
            id=f"high-{i}",
            title=f"高影响信号 {i}",
            type="capability",
            category="engineering",
            impact_score=5,
            why_it_matters=f"重要原因 {i}",
            sources=[f"https://github.com/test/repo/pull/{i}"],
            related_repos=[f"test/repo-{i}"],
        )
        for i in range(6)  # 6 个高影响信号，测试限制为 5 个
    ]

    medium_impact_signals = [
        Signal(
            id=f"medium-{i}",
            title=f"中等影响信号 {i}",
            type="workflow",
            category="engineering",
            impact_score=3,
            why_it_matters=f"原因 {i}",
            sources=[f"https://github.com/test/repo/pull/{i + 10}"],
            related_repos=[f"test/repo-{i}"],
        )
        for i in range(3)
    ]

    return DailyReport(
        date="2026-01-04",
        summary_brief=(
            "今日发现 9 个重要信号，涵盖 AI 编程工具、Agent 框架等多个领域的更新。"
        ),
        engineering_signals=high_impact_signals + medium_impact_signals,
        research_signals=[],
        commit_signals=[],
        release_signals=[],
        stats={
            "total_prs_analyzed": 45,
            "total_releases": 8,
            "high_impact_signals": 6,
            "total_commits_analyzed": 120,
        },
        activity=ActivityData(
            total_commits=500,
            active_repos_count=23,
            new_contributors=5,
            top_repos=[
                RepoActivity(
                    repo="anthropics/claude-code",
                    commits=127,
                    new_contributors=3,
                    top_contributors=["user1", "user2", "user3"],
                ),
                RepoActivity(
                    repo="cline/cline",
                    commits=45,
                    new_contributors=1,
                    top_contributors=["user4"],
                ),
                RepoActivity(
                    repo="openai/swarm",
                    commits=32,
                    new_contributors=0,
                    top_contributors=[],
                ),
                RepoActivity(
                    repo="significant-gravitas/autogpt",
                    commits=20,
                    new_contributors=2,
                    top_contributors=["user5", "user6"],
                ),
            ],
        ),
        releases=None,
        breaking_changes=None,
        monitored_repos=None,
    )
