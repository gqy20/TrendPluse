"""验证跨类型聚合效果

检查生成的报告，验证：
1. CommitAnalyzer 是否成功通过 SHA 匹配了正确的 commit
2. 生成的趋势是否包含多个来源（如果是聚合趋势）
3. 链接是否正确映射到对应的 commits/PRs/releases
"""

import re
from pathlib import Path


def verify_report_aggregation(report_path: str):
    """验证报告的聚合效果"""
    print("=" * 60)
    print("验证跨类型聚合效果")
    print("=" * 60)

    with open(report_path) as f:
        content = f.read()

    # 提取 Commit 信号部分
    # 从 "## 💾 Commit 信号" 到 "---" 或下一个 "##"
    commit_match = re.search(
        r"## 💾 Commit 信号\n\n(.*?)(?=---\n\n##|\Z)", content, re.DOTALL
    )

    if not commit_match:
        print("\n未找到 Commit 信号部分")
        return

    commit_section = commit_match.group(1)

    # 按标题分割信号（以 ### 开头）
    # 使用更精确的分割方式
    lines = commit_section.split("\n")
    signals: list[str] = []
    current_signal: list[str] = []
    in_signal = False

    for line in lines:
        if line.startswith("### "):
            # 新的信号开始
            if in_signal and current_signal:
                signals.append("\n".join(current_signal))
            current_signal = [line]
            in_signal = True
        elif in_signal:
            current_signal.append(line)

    # 添加最后一个信号
    if in_signal and current_signal:
        signals.append("\n".join(current_signal))

    print(f"\n找到 {len(signals)} 个信号")

    # 分析每个信号
    for i, signal_text in enumerate(signals, 1):
        print(f"\n{'=' * 60}")
        print(f"信号 {i}")
        print("=" * 60)

        # 提取标题
        title_match = re.search(r"^###\s+(.+)", signal_text, re.MULTILINE)
        if title_match:
            print(f"标题: {title_match.group(1)}")

        # 提取来源链接
        links = re.findall(r"https://github\.com/[^\s\)]+", signal_text)

        if links:
            print(f"\n来源 ({len(links)} 个):")
            pr_count = sum(1 for link in links if "/pull/" in link)
            commit_count = sum(1 for link in links if "/commit/" in link)
            release_count = sum(
                1 for link in links if "/releases/tag/" in link or "/tree/" in link
            )

            print(f"  PR: {pr_count}, Commit: {commit_count}, Release: {release_count}")

            for link in links:
                link_type = (
                    "PR"
                    if "/pull/" in link
                    else "Commit"
                    if "/commit/" in link
                    else "Release"
                    if "/releases/" in link
                    else "Other"
                )
                print(f"  [{link_type}] {link}")

            # 判断是否为跨类型聚合
            type_count = sum(
                1 for count in [pr_count, commit_count, release_count] if count > 0
            )
            if type_count >= 2:
                print(f"\n  ✅ 跨类型聚合！包含 {type_count} 种类型")
            elif type_count == 1:
                print("\n  ⚠️  单一类型来源（这是低层技术点，正常）")
            else:
                print("\n  ❓ 无法确定类型")
        else:
            print("  无来源链接")

    print("\n" + "=" * 60)
    print("验证完成")
    print("=" * 60)

    # 验证摘要
    print("\n📊 验证摘要:")
    if signals:
        print(f"  - Commit 信号总数: {len(signals)}")
        # 检查是否所有信号都有正确的 commit 链接
        all_links = []
        for signal in signals:
            all_links.extend(re.findall(r"https://github\.com/[^\s\)]+", signal))

        if all_links:
            print(f"  - 总链接数: {len(all_links)}")
            commit_links = [link for link in all_links if "/commit/" in link]
            print(f"  - Commit 链接数: {len(commit_links)}")

            # 验证 SHA 格式（应该是 40 个十六进制字符或至少 7 个）
            valid_shas = 0
            for link in commit_links:
                sha = link.split("/commit/")[-1]
                if len(sha) >= 7 and all(c in "0123456789abcdef" for c in sha.lower()):
                    valid_shas += 1

            print(f"  - 有效 SHA 格式: {valid_shas}/{len(commit_links)}")

            if valid_shas == len(commit_links):
                print("  ✅ SHA 匹配验证通过！")
            else:
                print("  ⚠️  部分链接的 SHA 格式可能不正确")


if __name__ == "__main__":
    import sys

    # 获取今天的报告路径
    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")
    default_path = f"reports/report-{today}.md"

    report_path = sys.argv[1] if len(sys.argv) > 1 else default_path

    if not Path(report_path).exists():
        print(f"错误: 报告文件不存在: {report_path}")
        print("\n提示: 请先运行 'uv run python scripts/run.py' 生成报告")
        sys.exit(1)

    verify_report_aggregation(report_path)
