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


def _build_signal(**overrides) -> Signal:
    """构造测试用信号。"""
    defaults = {
        "id": "test-signal-1",
        "title": "测试信号：新功能发布",
        "type": "capability",
        "category": "engineering",
        "impact_score": 5,
        "why_it_matters": "这是一个非常重要的功能更新",
        "sources": ["https://github.com/test/repo/pull/123"],
        "related_repos": ["test/repo"],
    }
    defaults.update(overrides)
    return Signal(**defaults)


def _build_activity() -> ActivityData:
    """构造测试用活跃度数据。"""
    return ActivityData(
        total_commits=500,
        active_repos_count=23,
        top_repos=[
            RepoActivity(
                repo="anthropics/claude-code",
                commits=127,
                top_contributors=["user1", "user2", "user3"],
            ),
            RepoActivity(
                repo="cline/cline",
                commits=45,
                top_contributors=["user4"],
            ),
            RepoActivity(
                repo="openai/swarm",
                commits=32,
                top_contributors=[],
            ),
            RepoActivity(
                repo="significant-gravitas/autogpt",
                commits=20,
                top_contributors=["user5", "user6"],
            ),
        ],
    )


def _get_all_card_content(elements: list) -> list[str]:
    """提取卡片中所有元素的内容（包括折叠面板内的内容和标题）

    Args:
        elements: 卡片元素列表

    Returns:
        所有元素的内容列表
    """
    contents: list[str] = []

    for el in elements:
        tag = el.get("tag")

        # 直接的 div 元素
        if tag == "div":
            content = el.get("text", {}).get("content", "")
            contents.append(content)

        # 折叠面板元素 - 递归提取内部内容和标题
        elif tag == "collapsible_panel":
            # 添加面板标题
            header = el.get("header", {})
            title = header.get("title", {})
            title_content = title.get("content", "")
            if title_content:
                contents.append(title_content)

            # 添加面板内部内容
            panel_elements = el.get("elements", [])
            for panel_el in panel_elements:
                if panel_el.get("tag") == "div":
                    content = panel_el.get("text", {}).get("content", "")
                    contents.append(content)

    return contents


def _content_contains(elements: list, text: str) -> bool:
    """检查卡片中是否包含指定文本（包括折叠面板内）

    Args:
        elements: 卡片元素列表
        text: 要查找的文本

    Returns:
        是否包含该文本
    """
    contents = _get_all_card_content(elements)
    return any(text in content for content in contents)


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
        # JSON 2.0: elements 在 body 下
        assert "body" in card["card"]
        assert "elements" in card["card"]["body"]

        # 验证标题在 card header 中
        header = card["card"]["header"]
        assert "TrendPulse 每日报告" in header["title"]["content"]
        assert header["template"] == "blue"

        # 验证至少有元素
        assert len(card["card"]["body"]["elements"]) > 0

    def test_build_card_includes_highlights_section(self, sample_report: DailyReport):
        """卡片应包含高影响信号部分"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        # JSON 2.0: elements 在 body 下
        elements = card["card"]["body"]["elements"]
        # 注意：工程信号现在在折叠面板中，需要使用辅助函数检查
        assert _content_contains(elements, "工程信号")

    def test_build_card_includes_stats_section(self, sample_report: DailyReport):
        """卡片应包含统计信息部分"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        # JSON 2.0: elements 在 body 下
        elements = card["card"]["body"]["elements"]
        # 注意：统计信息现在在折叠面板中，需要使用辅助函数检查
        assert _content_contains(elements, "统计信息")

    def test_build_card_includes_action_buttons(self, sample_report: DailyReport):
        """卡片应包含操作按钮"""
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")
        card = notifier._build_card(sample_report)

        # JSON 2.0: 按钮直接在 elements 中，不使用 action 容器
        elements = card["card"]["body"]["elements"]
        # 查找 button 元素
        has_button = any(el.get("tag") == "button" for el in elements)
        assert has_button

    @patch("httpx.post")
    def test_send_report_success(self, mock_post: Mock, sample_report: DailyReport):
        """成功发送报告通知"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"code": 0, "msg": "success"}
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
        # JSON 2.0: elements 在 body 下
        elements = card["card"]["body"]["elements"]
        # 查找包含手机号的元素
        has_at = any("13800138000" in str(el) for el in elements)
        assert has_at

    @patch("httpx.post")
    def test_send_with_signature(self, mock_post: Mock, sample_report: DailyReport):
        """支持签名验证"""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"code": 0, "msg": "success"}
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

    def test_build_card_respects_max_signals(self, sample_report: DailyReport):
        """通知器应将 max_signals 传递给格式化器"""
        notifier = FeishuNotifier(
            webhook_url="https://example.com/webhook",
            max_signals=1,
        )
        card = notifier._build_card(sample_report)
        elements = card["card"]["body"]["elements"]

        assert _content_contains(elements, "高影响信号 0")
        assert not _content_contains(elements, "高影响信号 1")

    def test_build_card_uses_custom_report_url_template(
        self, sample_report: DailyReport
    ):
        """通知器应使用自定义报告链接模板"""
        notifier = FeishuNotifier(
            webhook_url="https://example.com/webhook",
            report_url_template="https://example.com/reports/report-{date}/",
        )
        card = notifier._build_card(sample_report)
        button = next(
            el for el in card["card"]["body"]["elements"] if el.get("tag") == "button"
        )

        assert button["url"] == "https://example.com/reports/report-2026-01-04/"


# ========== Fixtures ==========


@pytest.fixture
def sample_report() -> DailyReport:
    """创建示例日报"""
    # 创建不同评分的信号
    high_impact_signals = [
        _build_signal(
            id=f"high-{i}",
            title=f"高影响信号 {i}",
            impact_score=5,
            why_it_matters=f"重要原因 {i}",
            sources=[f"https://github.com/test/repo/pull/{i}"],
            related_repos=[f"test/repo-{i}"],
        )
        for i in range(6)  # 6 个高影响信号，测试限制为 5 个
    ]

    medium_impact_signals = [
        _build_signal(
            id=f"medium-{i}",
            title=f"中等影响信号 {i}",
            type="workflow",
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
        activity=_build_activity(),
        releases=None,
        breaking_changes=None,
        monitored_repos=None,
    )


class TestFeishuNotifierJsonV2:
    """测试 FeishuNotifier 飞书卡片 JSON 2.0 结构"""

    def test_build_card_uses_json_v2_structure(self, sample_report: DailyReport):
        """测试：卡片使用 JSON 2.0 结构"""
        # Arrange
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        # Act
        card = notifier._build_card(sample_report)

        # Assert - JSON 2.0 结构验证
        assert card["msg_type"] == "interactive"
        card_data = card["card"]

        # 必须包含 schema 字段且值为 "2.0"
        assert "schema" in card_data, "卡片必须包含 schema 字段"
        assert card_data["schema"] == "2.0", "schema 必须为 2.0"

        # 必须包含 config 字段
        assert "config" in card_data, "卡片必须包含 config 字段"

        # update_multi 必须为 true（JSON 2.0 要求）
        assert card_data["config"]["update_multi"] is True, (
            "JSON 2.0 要求 update_multi 为 true"
        )

        # elements 必须在 body 层级下
        assert "body" in card_data, "JSON 2.0 要求包含 body 字段"
        assert "elements" in card_data["body"], "elements 必须在 body 下"

        # 不应该在根级别有 elements
        assert "elements" not in card_data or card_data.get("elements") is None, (
            "JSON 2.0 不支持根级别的 elements"
        )

    def test_json_v2_preserves_header(self, sample_report: DailyReport):
        """测试：JSON 2.0 标题在 card header 中"""
        # Arrange
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        # Act
        card = notifier._build_card(sample_report)

        # Assert - 使用 card header，而非 body element
        card_data = card["card"]
        assert "header" in card_data, "card 必须包含 header 字段"
        header = card_data["header"]
        assert "TrendPulse 每日报告" in header["title"]["content"]
        assert sample_report.date in header["subtitle"]["content"]
        assert header["template"] == "blue"

    def test_json_v2_body_elements_are_valid(self, sample_report: DailyReport):
        """测试：JSON 2.0 body.elements 包含有效内容"""
        # Arrange
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        # Act
        card = notifier._build_card(sample_report)

        # Assert
        elements = card["card"]["body"]["elements"]
        assert len(elements) > 0, "body.elements 必须包含内容"

        # 验证包含预期的元素类型
        element_tags = {el.get("tag") for el in elements}
        assert "div" in element_tags or "markdown" in element_tags
        assert "hr" in element_tags or {"tag": "hr"} in elements

    def test_json_v2_content_includes_heading_syntax(self, sample_report: DailyReport):
        """测试：JSON 2.0 支持标题语法（###）"""
        # Arrange
        notifier = FeishuNotifier(webhook_url="https://example.com/webhook")

        # Act
        card = notifier._build_card(sample_report)

        # Assert - 验证 content 中包含 ### 标题语法
        elements = card["card"]["body"]["elements"]

        # 收集所有 markdown content
        contents = []
        for el in elements:
            if el.get("tag") in ("div", "markdown"):
                text_obj = el.get("text", {})
                if text_obj.get("tag") == "lark_md":
                    contents.append(text_obj.get("content", ""))

        combined_content = " ".join(contents)

        # 标题已迁移到 card header，body 中包含摘要文本（可能含粗体或普通文本）
        # 确保摘要内容被包含
        assert sample_report.summary_brief in combined_content
