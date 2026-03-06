"""飞书通知 CLI 公共辅助。"""

from __future__ import annotations

import os
from dataclasses import dataclass

from rich.console import Console

from trendpluse.notifiers.feishu import FeishuNotifier


@dataclass(frozen=True)
class FeishuCliConfig:
    """飞书 CLI 配置。"""

    webhook_url: str
    secret: str
    at_mobiles: list[str]
    max_signals: int


def parse_at_mobiles(raw_value: str) -> list[str]:
    """解析逗号分隔的手机号列表。"""
    if not raw_value:
        return []
    return [mobile.strip() for mobile in raw_value.split(",") if mobile.strip()]


def parse_max_signals(raw_value: str) -> int:
    """解析飞书最大信号数配置。"""
    try:
        value = int(raw_value)
    except ValueError:
        return 5
    return max(1, min(10, value))


def load_feishu_cli_config() -> FeishuCliConfig:
    """从环境变量加载飞书 CLI 配置。"""
    return FeishuCliConfig(
        webhook_url=os.getenv("FEISHU_WEBHOOK_URL", ""),
        secret=os.getenv("FEISHU_SECRET", ""),
        at_mobiles=parse_at_mobiles(os.getenv("FEISHU_AT_MOBILES", "")),
        max_signals=parse_max_signals(os.getenv("FEISHU_MAX_SIGNALS", "5")),
    )


def ensure_webhook_configured(console: Console, config: FeishuCliConfig) -> None:
    """确保 webhook 已配置，否则直接退出。"""
    if config.webhook_url:
        return
    console.print("[yellow]FEISHU_WEBHOOK_URL 未配置，跳过通知[/yellow]")
    raise SystemExit(0)


def build_feishu_notifier(
    config: FeishuCliConfig,
    report_url_template: str | None = None,
) -> FeishuNotifier:
    """根据 CLI 配置创建飞书通知器。"""
    return FeishuNotifier(
        webhook_url=config.webhook_url,
        at_mobiles=config.at_mobiles,
        max_signals=config.max_signals,
        secret=config.secret or None,
        report_url_template=report_url_template,
    )


def print_feishu_target(console: Console, config: FeishuCliConfig) -> None:
    """打印飞书发送目标信息。"""
    console.print(f"  @ 提醒: {len(config.at_mobiles)} 个")
    console.print(
        f"  Webhook URL: {config.webhook_url[:30]}...{config.webhook_url[-10:]}"
    )
    console.print(f"  使用签名: {'是' if config.secret else '否'}")


def exit_on_send_failure(console: Console, success: bool) -> None:
    """根据发送结果输出并处理退出码。"""
    if success:
        console.print("[green]✓ 飞书通知发送成功[/green]")
        return
    console.print("[red]✗ 飞书通知发送失败[/red]")
    raise SystemExit(1)


def print_exception_and_exit(console: Console, exc: Exception) -> None:
    """打印异常并退出。"""
    console.print(f"[red]发送通知失败:[/red] {exc}")
    import traceback

    traceback.print_exc()
    raise SystemExit(1)
