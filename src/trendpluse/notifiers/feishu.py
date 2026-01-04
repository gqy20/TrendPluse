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
from trendpluse.notifiers.formatters import FeishuFormatter


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
        self.formatter = FeishuFormatter()

    def send(self, title: str, content: str, url: str | None = None) -> bool:
        """发送简单文本通知

        Args:
            title: 通知标题
            content: 通知内容（支持 Markdown）
            url: 可选的跳转链接（会作为链接添加到内容末尾）

        Returns:
            是否发送成功
        """
        # 如果提供了 URL，将其作为链接添加到内容末尾
        if url:
            content += f"\n\n🔗 **[查看详情]({url})**"

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
                            "tag": "lark_md",
                            "content": content,
                        },
                    },
                ],
            },
        }

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
        # 使用 FeishuFormatter 构建基础卡片
        card = self.formatter.format_card(report)

        # 添加 @ 提醒（如果配置）
        if self.at_mobiles:
            # JSON 2.0 结构：elements 在 body 下
            elements = card["card"]["body"]["elements"]
            at_list = " ".join(
                f'<at user_id="{mobile}"></at>' for mobile in self.at_mobiles
            )

            # 在按钮之前插入 @ 提醒
            # 找到最后一个 hr 元素（在按钮前）
            for i in range(len(elements) - 1, -1, -1):
                if elements[i].get("tag") == "hr":
                    elements.insert(
                        i + 1,
                        {
                            "tag": "div",
                            "text": {
                                "tag": "lark_md",
                                "content": at_list,
                            },
                        },
                    )
                    break

        return card

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

            # 检查飞书响应体的错误码
            # 飞书成功响应: {"code": 0, "msg": "success"}
            # 飞书错误响应: {"code": 99999, "msg": "错误信息"}
            data = response.json()
            code = data.get("code", -1)
            if code != 0:
                print(f"[DEBUG] 飞书返回错误: code={code}, msg={data.get('msg')}")
                return False

            return True
        except httpx.HTTPError as e:
            print(f"[DEBUG] HTTP 请求失败: {e}")
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
