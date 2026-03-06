#!/usr/bin/env python3
"""GitHub 仓库深度分析命令入口。"""

import argparse
import sys

from trendpluse.app.analyze_repo import (
    analyze_repository,
    generate_markdown_report,
    parse_github_url,
    save_report,
)
from trendpluse.config import Settings


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="分析 GitHub 仓库并生成趋势报告",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  uv run trendpluse-analyze-repo https://github.com/anthropics/claude-code
  uv run trendpluse-analyze-repo anthropics/claude-code --output report.md
  uv run trendpluse-analyze-repo anthropics/claude-code --days 30
        """,
    )
    parser.add_argument(
        "github_url",
        help="GitHub 仓库 URL 或 owner/repo 格式",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="输出文件路径（默认输出到 stdout）",
    )
    parser.add_argument(
        "--days",
        "-d",
        type=int,
        default=7,
        help="回溯天数（默认: 7）",
    )

    args = parser.parse_args()

    # 解析 URL
    parsed = parse_github_url(args.github_url)
    if not parsed:
        print(f"❌ 无效的 GitHub URL: {args.github_url}", file=sys.stderr)
        sys.exit(1)

    owner, repo = parsed

    # 加载配置
    settings = Settings()

    if not settings.anthropic_api_key:
        print("❌ 未设置 ANTHROPIC_API_KEY 环境变量", file=sys.stderr)
        sys.exit(1)

    # 执行分析
    try:
        result = analyze_repository(
            owner=owner,
            repo=repo,
            github_token=settings.github_token,
            anthropic_api_key=settings.anthropic_api_key,
            anthropic_base_url=settings.anthropic_base_url,
            anthropic_model=settings.anthropic_model,
            days_back=args.days,
        )
    except Exception as e:
        print(f"❌ 分析失败: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        sys.exit(1)

    # 生成报告
    report = generate_markdown_report(result)

    # 输出
    if args.output:
        save_report(report, args.output)
        print(f"✅ 报告已保存到: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
