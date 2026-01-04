"""测试 CommitAnalyzer SHA 匹配功能"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from dotenv import load_dotenv

from trendpluse.analyzers.commit_analyzer import CommitAnalyzer
from trendpluse.config import Settings

load_dotenv()


def test_sha_matching():
    """测试 SHA 匹配是否正确工作"""
    print("=" * 60)
    print("测试 CommitAnalyzer SHA 匹配")
    print("=" * 60)

    # 模拟真实的 commit 数据
    commits = [
        {
            "repo": "anthropic/claude-code",
            "sha": "abc123def456",
            "message": "Unimportant typo fix",
            "author": "user1",
            "timestamp": "2026-01-04T10:00:00Z",
        },
        {
            "repo": "cline/cline",
            "sha": "def456ghi789",
            "message": "Add agent memory feature",
            "author": "user2",
            "timestamp": "2026-01-04T11:00:00Z",
        },
        {
            "repo": "openai/swarm",
            "sha": "ghi789jkl012",
            "message": "Another minor fix",
            "author": "user3",
            "timestamp": "2026-01-04T12:00:00Z",
        },
    ]

    print(f"\n输入 commits 数量: {len(commits)}")
    print("Commit SHA 列表:")
    for i, c in enumerate(commits):
        print(f"  [{i}] {c['sha'][:12]}... - {c['message'][:40]}")

    # 初始化分析器
    settings = Settings()
    analyzer = CommitAnalyzer(
        api_key=settings.anthropic_api_key,
        model=settings.anthropic_model,
        base_url=settings.anthropic_base_url,
    )

    print(f"\n使用模型: {settings.anthropic_model}")
    print(f"API 端点: {settings.anthropic_base_url}")
    print("\n调用 LLM 分析...")

    # 分析 commits
    signals = analyzer.analyze_commits(commits)

    print(f"\n提取到 {len(signals)} 个信号:")
    for i, signal in enumerate(signals):
        print(f"\n信号 {i + 1}:")
        print(f"  标题: {signal.title}")
        print(f"  来源: {signal.sources}")
        print(f"  相关仓库: {signal.related_repos}")

        # 验证 SHA 匹配
        if signal.sources:
            source_url = signal.sources[0]
            # 从 URL 中提取 SHA
            if "/commit/" in source_url:
                extracted_sha = source_url.split("/commit/")[-1]
                # 检查是否在原始 commits 列表中
                original_shas = [c["sha"] for c in commits]
                if extracted_sha in original_shas:
                    print(f"  ✅ SHA 匹配正确: {extracted_sha[:12]}...")
                else:
                    print("  ❌ SHA 不匹配! URL 中的 SHA 不在输入列表中")
                    print(f"     期望的 SHA 列表: {original_shas}")

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)


if __name__ == "__main__":
    test_sha_matching()
