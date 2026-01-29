#!/usr/bin/env python3
"""GitHub 仓库深度分析脚本

从 GitHub URL 分析仓库趋势，生成 Markdown 报告。
用法: python scripts/analyze_repo.py <github_url> --output <output_file>
"""

import argparse
import re
import sys
from datetime import UTC, datetime, timedelta
from pathlib import Path

from anthropic import Anthropic

from trendpluse.collectors.activity import ActivityCollector
from trendpluse.collectors.github_events import GitHubEventsCollector
from trendpluse.collectors.releases import ReleaseCollector
from trendpluse.config import Settings


def parse_github_url(url: str) -> tuple[str, str] | None:
    """解析 GitHub URL，返回 (owner, repo)

    Args:
        url: GitHub URL，支持多种格式：
            - https://github.com/owner/repo
            - https://github.com/owner/repo.git
            - git@github.com:owner/repo.git
            - owner/repo

    Returns:
        (owner, repo) 元组，解析失败返回 None
    """
    # 移除 .git 后缀
    url = url.removesuffix(".git")

    # 处理 SSH 格式
    if url.startswith("git@github.com:"):
        url = url.replace("git@github.com:", "https://github.com/")

    # 匹配 https://github.com/owner/repo 格式
    match = re.match(r"https?://github\.com/([^/]+)/([^/]+)/?", url)
    if match:
        return match.group(1), match.group(2)

    # 匹配 owner/repo 格式
    match = re.match(r"^([^/]+)/([^/]+)$", url)
    if match:
        return match.group(1), match.group(2)

    return None


def analyze_repository(
    owner: str,
    repo: str,
    github_token: str,
    anthropic_api_key: str,
    anthropic_base_url: str = "",
    anthropic_model: str = "glm-4.7",
    days_back: int = 7,
) -> dict:
    """分析 GitHub 仓库

    Args:
        owner: 仓库所有者
        repo: 仓库名称
        github_token: GitHub 访问令牌
        anthropic_api_key: Anthropic API 密钥
        anthropic_base_url: API 基础 URL（可选）
        anthropic_model: 模型名称
        days_back: 回溯天数

    Returns:
        包含分析结果的字典
    """
    repo_path = f"{owner}/{repo}"
    since = datetime.now(UTC) - timedelta(days=days_back)

    print(f"🔍 分析仓库: {repo_path}")
    print(f"📅 时间范围: 最近 {days_back} 天")

    # 初始化 LLM 客户端
    if anthropic_base_url:
        llm_client = Anthropic(
            api_key=anthropic_api_key,
            base_url=anthropic_base_url,
        )
    else:
        llm_client = Anthropic(api_key=anthropic_api_key)

    result = {
        "repo": repo_path,
        "repo_url": f"https://github.com/{repo_path}",
        "analysis_date": datetime.now(UTC).isoformat(),
        "days_back": days_back,
        "error": None,
    }

    # 1. 采集活跃度数据
    print("📊 采集活跃度数据...")
    try:
        activity_collector = ActivityCollector(token=github_token)
        activity_data, _ = activity_collector.collect_activity(
            repos=[repo_path],
            since=since,
        )
        if activity_data.top_repos:
            repo_act = activity_data.top_repos[0]
            result["activity"] = {
                "commits": repo_act.commits,
                "top_contributors": repo_act.top_contributors,
            }
            print(
                f"  ✓ Commits: {result['activity']['commits']}"  # type: ignore[index]
            )
        else:
            result["activity"] = None
            print("  ✗ 无活跃度数据")
    except Exception as e:
        print(f"  ✗ 活跃度采集失败: {e}")
        result["activity"] = None
        result["error"] = str(e)

    # 2. 采集 Release 数据
    print("📦 采集 Release 数据...")
    try:
        release_collector = ReleaseCollector(token=github_token)
        releases_data, _ = release_collector.collect_releases(
            repos=[repo_path],
            since=since,
            include_prereleases=False,
        )
        result["releases"] = {
            "count": len(releases_data.releases),
            "latest": releases_data.releases[0].model_dump()
            if releases_data.releases
            else None,
            "all": [r.model_dump() for r in releases_data.releases],
        }
        print(f"  ✓ 找到 {result['releases']['count']} 个 Release")  # type: ignore[index]
    except Exception as e:
        print(f"  ✗ Release 采集失败: {e}")
        result["releases"] = None

    # 3. 采集 PR 事件（候选事件）
    print("🔎 采集 PR 事件...")
    try:
        events_collector = GitHubEventsCollector(token=github_token)
        events = events_collector.fetch_events(
            repos=[repo_path],
            since=since,
        )
        # 从事件中提取 PR 标题
        titles = []
        for event in events[:10]:
            pr = event.get("payload", {}).get("pull_request", {})
            title = pr.get("title", "")
            if title:
                titles.append(title)
        result["pr_events"] = {
            "count": len(events),
            "titles": titles,
        }
        print(f"  ✓ 找到 {result['pr_events']['count']} 个 PR 事件")  # type: ignore[index]
    except Exception as e:
        print(f"  ✗ PR 事件采集失败: {e}")
        result["pr_events"] = None

    # 4. 简单的 AI 摘要（使用 LLM 生成简要分析）
    if result["activity"] and (result["releases"] or result["pr_events"]):
        print("🤖 生成 AI 摘要...")
        try:
            summary = _generate_summary(
                llm_client,
                result,
                anthropic_model,
            )
            result["ai_summary"] = summary
            print("  ✓ 摘要生成完成")
        except Exception as e:
            print(f"  ✗ 摘要生成失败: {e}")
            result["ai_summary"] = None

    return result


def _generate_summary(
    client: Anthropic,
    data: dict,
    model: str = "glm-4.7",
) -> str:
    """使用 LLM 生成仓库分析摘要

    Args:
        client: Anthropic 客户端
        data: 分析数据
        model: 模型名称

    Returns:
        生成的摘要文本
    """
    # 构建上下文
    context_parts = []

    # 活跃度信息
    if data.get("activity"):
        act = data["activity"]
        top_contribs = ", ".join(act.get("top_contributors", [])[:3])
        context_parts.append(
            f"- 活跃度数据：\n"
            f"  - 总提交数: {act.get('commits', 0)}\n"
            f"  - Top 贡献者: {top_contribs or 'N/A'}\n"
        )

    # Release 信息
    if data.get("releases") and data["releases"].get("count", 0) > 0:
        rel = data["releases"]
        latest = rel.get("latest", {})
        context_parts.append(
            f"- 发布信息：\n"
            f"  - 发布数量: {rel['count']}\n"
            f"  - 最新版本: {latest.get('version', 'N/A')}\n"
            f"  - 发布时间: {latest.get('date', 'N/A')}\n"
        )

    # PR 事件
    if data.get("pr_events") and data["pr_events"].get("count", 0) > 0:
        pr = data["pr_events"]
        titles = pr.get("titles", [])[:5]  # 只取前 5 个
        context_parts.append(f"""
- PR 活动：
  - PR 数量: {pr["count"]}
  - 最近 PR 标题: {", ".join(titles) if titles else "N/A"}
""")

    context = "\n".join(context_parts)

    # 调用 LLM
    prompt = f"""请分析以下 GitHub 仓库数据，生成一份简洁的技术趋势摘要。

仓库: {data["repo"]}
分析时间范围: 最近 {data["days_back"]} 天

{context}

请提供：
1. 仓库活跃度概述（1-2 句话）
2. 最近的技术动向或重要更新（2-3 点）
3. 值得关注的信号（如有）

用中文回答，简洁专业，不超过 200 字。"""

    response = client.messages.create(
        model=model,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text  # type: ignore[no-any-return]


def generate_markdown_report(data: dict) -> str:
    """生成 Markdown 格式的分析报告

    Args:
        data: 分析结果数据

    Returns:
        Markdown 报告文本
    """
    lines = []

    # 标题
    lines.append("## 📊 仓库分析报告")
    lines.append("")
    lines.append(f"**仓库**: [{data['repo']}]({data['repo_url']})")
    analysis_time = datetime.fromisoformat(data["analysis_date"]).strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    lines.append(f"**分析时间**: {analysis_time} UTC")
    lines.append(f"**数据范围**: 最近 {data['days_back']} 天")
    lines.append("")

    # AI 摘要
    if data.get("ai_summary"):
        lines.append("---")
        lines.append("")
        lines.append("### 🤖 AI 分析摘要")
        lines.append("")
        lines.append(data["ai_summary"])
        lines.append("")

    # 活跃度数据
    lines.append("---")
    lines.append("")
    lines.append("### 📈 活跃度统计")
    lines.append("")

    if data.get("activity"):
        act = data["activity"]
        lines.append("| 指标 | 数值 |")
        lines.append("|------|------|")
        lines.append(f"| 💚 总提交数 | {act.get('commits', 0)} |")
        top_contribs = ", ".join(act.get("top_contributors", [])[:5])
        lines.append(f"| 🏆 Top 贡献者 | {top_contribs or 'N/A'} |")
    else:
        lines.append("*暂无活跃度数据*")

    lines.append("")

    # Release 信息
    lines.append("---")
    lines.append("")
    lines.append("### 🚀 发布动态")
    lines.append("")

    if data.get("releases") and data["releases"].get("count", 0) > 0:
        rel = data["releases"]
        lines.append(f"**共 {rel['count']} 个发布**")
        lines.append("")

        for release in rel.get("all", [])[:5]:  # 最多显示 5 个
            version = release.get("version", "N/A")
            url = release.get("url", "")
            if url:
                lines.append(f"#### [`{version}`]({url})")
            else:
                lines.append(f"#### `{version}`")
            lines.append("")

            # 发布日期
            if release.get("date"):
                lines.append(f"**发布日期**: {release['date']}  ")
            lines.append("")

            # 发布者
            if release.get("author"):
                lines.append(f"**发布者**: {release['author']}  ")
            lines.append("")

            # 摘要（如果有且不太长）
            summary = release.get("summary", "")
            if summary and len(summary) < 500:
                lines.append(f"**摘要**: {summary}  ")
                lines.append("")
    else:
        lines.append("*暂无发布数据*")

    lines.append("")

    # PR 活动
    lines.append("---")
    lines.append("")
    lines.append("### 🔀 PR 活动")
    lines.append("")

    if data.get("pr_events") and data["pr_events"].get("count", 0) > 0:
        pr = data["pr_events"]
        lines.append(f"**共 {pr['count']} 个 PR 事件**")
        lines.append("")
        lines.append("**最近 PR 标题**:")
        lines.append("")
        for title in pr.get("titles", [])[:10]:
            lines.append(f"- {title}")
    else:
        lines.append("*暂无 PR 数据*")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(
        f"*报告由 TrendPulse 自动生成 | [查看完整报告](https://github.com/{data['repo']})*"
    )

    return "\n".join(lines)


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="分析 GitHub 仓库并生成趋势报告",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python scripts/analyze_repo.py https://github.com/anthropics/claude-code
  python scripts/analyze_repo.py anthropics/claude-code --output report.md
  python scripts/analyze_repo.py anthropics/claude-code --days 30
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
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"✅ 报告已保存到: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
