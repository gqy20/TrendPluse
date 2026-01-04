"""飞书通知器

通过飞书自定义机器人 Webhook 发送卡片消息。
"""

import base64
import hashlib
import hmac
import time

import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
)

from trendpluse.models.signal import DailyReport
from trendpluse.notifiers.base import BaseNotifier
from trendpluse.notifiers.summary import ReportSummarizer


class FeishuNotifier(BaseNotifier):
    """飞书 Webhook 通知器

    使用飞书自定义机器人 Webhook 发送卡片消息。
    """

    def __init__(
        self,
        webhook_url: str,
        at_mobiles: list[str] | None = None,
        max_signals: int = 5,
        secret: str | None = None,
    ):
        """初始化飞书通知器

        Args:
            webhook_url: 飞书机器人 Webhook URL
            at_mobiles: @ 提醒的用户手机号列表
            max_signals: 卡片中显示的信号数量
            secret: 飞书机器人签名验证密钥（可选）

        Raises:
            ValueError: webhook_url 为空
        """
        if not webhook_url or not webhook_url.strip():
            raise ValueError("webhook_url 不能为空")
        self.webhook_url = webhook_url
        self.at_mobiles = at_mobiles or []
        self.max_signals = max_signals
        self.secret = secret
        self.summarizer = ReportSummarizer()

    def send(self, title: str, content: str, url: str | None = None) -> bool:
        """发送简单文本通知

        Args:
            title: 通知标题
            content: 通知内容
            url: 可选的跳转链接

        Returns:
            是否发送成功
        """
        card: dict = {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": title,
                    },
                },
                "elements": [
                    {
                        "tag": "div",
                        "text": {
                            "tag": "plain_text",
                            "content": content,
                        },
                    },
                ],
            },
        }

        if url:
            card_elements = card["card"]["elements"]
            if isinstance(card_elements, list):
                card_elements.append(
                    {
                        "tag": "action",
                        "actions": [
                            {
                                "tag": "button",
                                "text": {"tag": "plain_text", "content": "查看详情"},
                                "url": url,
                                "type": "default",
                            }
                        ],
                    }
                )

        return self._send_webhook(card)

    def send_report(self, report: DailyReport) -> bool:
        """发送日报通知

        Args:
            report: 每日报告对象

        Returns:
            是否发送成功
        """
        card = self._build_card(report)
        return self._send_webhook(card)

    def _build_card(self, report: DailyReport) -> dict:
        """构建飞书卡片

        Args:
            report: 每日报告对象

        Returns:
            飞书卡片字典
        """
        summary = self.summarizer.summarize(report)

        elements: list[dict] = []

        # 1. 摘要
        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": summary["summary"],
                },
            }
        )

        # 2. 高影响信号
        if summary["highlights"]:
            elements.append({"tag": "hr"})
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "### 🔥 高影响信号",
                    },
                }
            )

            for signal in summary["highlights"][: self.max_signals]:
                type_emoji = self._get_type_emoji(signal["type"])
                impact_stars = "⭐" * signal["impact_score"]
                repos = ", ".join(f"`{r}`" for r in signal["related_repos"])

                content = (
                    f"**{type_emoji} {signal['title']}**\n"
                    f"{impact_stars} | {repos}\n"
                    f"{signal['why_it_matters']}"
                )

                elements.append(
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": content,
                        },
                    }
                )

        # 3. 统计信息
        elements.append({"tag": "hr"})
        stats = summary["stats"]
        stats_content = (
            "### 📊 统计信息\n"
            f"• 分析 PR 数: {stats['total_prs_analyzed']}\n"
            f"• 高影响信号: {stats['high_impact_signals']}\n"
            f"• 新发布版本: {stats['total_releases']}\n"
            f"• 分析 Commit 数: {stats['total_commits_analyzed']}"
        )
        elements.append(
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": stats_content,
                },
            }
        )

        # 4. 活跃仓库 TOP 3
        if summary["top_repos"]:
            elements.append({"tag": "hr"})
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": "### 🔥 活跃仓库 TOP 3",
                    },
                }
            )

            for i, repo in enumerate(summary["top_repos"], 1):
                repo_content = f"{i}. **{repo['repo']}** ({repo['commits']} commits)\n"
                elements.append(
                    {
                        "tag": "div",
                        "text": {
                            "tag": "lark_md",
                            "content": repo_content,
                        },
                    }
                )

        # 5. @ 提醒
        if self.at_mobiles:
            at_list = " ".join(
                f'<at user_id="{mobile}"></at>' for mobile in self.at_mobiles
            )
            elements.append(
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": at_list,
                    },
                }
            )

        # 6. 操作按钮
        elements.append({"tag": "hr"})
        elements.append(
            {
                "tag": "action",
                "actions": [
                    {
                        "tag": "button",
                        "text": {"tag": "plain_text", "content": "📖 查看完整报告"},
                        "url": summary["report_url"],
                        "type": "primary",
                    }
                ],
            }
        )

        return {
            "msg_type": "interactive",
            "card": {
                "header": {
                    "title": {
                        "tag": "plain_text",
                        "content": summary["title"],
                    },
                },
                "elements": elements,
            },
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, max=10),
    )
    def _send_webhook(self, card: dict) -> bool:
        """发送 webhook 请求

        Args:
            card: 飞书卡片字典

        Returns:
            是否发送成功
        """
        try:
            # 如果配置了 secret，添加签名
            if self.secret:
                timestamp = str(int(time.time()))
                sign = self._gen_sign(timestamp, self.secret)
                card["timestamp"] = timestamp
                card["sign"] = sign

            response = httpx.post(
                self.webhook_url,
                json=card,
                timeout=3.0,
            )
            response.raise_for_status()
            # 检查状态码是否为 2xx
            if not (200 <= response.status_code < 300):
                return False
            return True
        except httpx.HTTPError:
            return False

    def _gen_sign(self, timestamp: str, secret: str) -> str:
        """生成飞书 webhook 签名

        Args:
            timestamp: 时间戳字符串
            secret: 签名密钥

        Returns:
            base64 编码的签名
        """
        # 拼接 timestamp 和 secret
        string_to_sign = f"{timestamp}\n{secret}"
        hmac_code = hmac.new(
            string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
        ).digest()

        # 对结果进行 base64 处理
        sign = base64.b64encode(hmac_code).decode("utf-8")
        return sign

    def _get_type_emoji(self, signal_type: str) -> str:
        """获取信号类型的表情

        Args:
            signal_type: 信号类型

        Returns:
            类型表情
        """
        emojis = {
            "capability": "🚀",
            "abstraction": "🎨",
            "workflow": "⚙️",
            "eval": "📊",
            "safety": "🛡️",
            "performance": "⚡",
            "commit": "💾",
            "release": "🎯",
        }
        return emojis.get(signal_type, "📌")
