#!/usr/bin/env python3
"""周报生成脚本

从过去 7 天的日报聚合生成周报。
"""

import argparse
import os
from datetime import datetime, timedelta

from trendpluse.app.runtime import run_weekly_pipeline
from trendpluse.config import Settings
from trendpluse.logger import get_logger

logger = get_logger(__name__)


def resolve_weekly_reference_date(raw_week_id: str | None) -> datetime:
    """解析周报参考日期。

    若显式传入 `WEEK_ID`，则返回目标周之后一周的周一，
    以便现有“回看上一周”的逻辑稳定生成指定周报。
    """
    cleaned = (raw_week_id or "").strip()
    if not cleaned:
        return datetime.now()

    try:
        year_text, week_text = cleaned.split("-W", maxsplit=1)
        year = int(year_text)
        week = int(week_text)
        target_monday = datetime.fromisocalendar(year, week, 1)
    except ValueError as exc:
        raise ValueError(f"WEEK_ID 格式错误: {cleaned}，期望格式为 YYYY-Www") from exc

    return (target_monday + timedelta(days=7)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="运行 TrendPulse 周报生成")
    parser.parse_args()

    if os.getenv("GITHUB_ACTIONS") != "true":
        raise RuntimeError("周报生成仅支持通过 GitHub Actions 触发执行")

    logger.info("开始生成周报...")

    settings = Settings()

    try:
        reference_date = resolve_weekly_reference_date(os.getenv("WEEK_ID"))
        result = run_weekly_pipeline(settings=settings, date=reference_date)
        weekly_report = result.report
        logger.info(f"周报生成成功: {weekly_report.week_id}")
        logger.info(f"  - 包含日报: {weekly_report.daily_reports_count} 天")
        signal_count = len(
            weekly_report.engineering_signals + weekly_report.research_signals
        )
        logger.info(f"  - 趋势信号: {signal_count} 个")
        logger.info(f"  - 高影响信号: {weekly_report.high_impact_signals} 个")
        logger.info(f"  - 输出路径: {result.output_path}")
    except Exception as e:
        logger.error(f"周报生成失败: {e}")
        raise


if __name__ == "__main__":
    main()
