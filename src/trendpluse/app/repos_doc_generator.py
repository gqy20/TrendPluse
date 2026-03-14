"""仓库文档生成器。"""

from dataclasses import dataclass

from trendpluse.models.repository import MonitoredRepo

REPO_CATEGORIES: dict[str, list[str]] = {
    "Anthropic 核心产品": [
        "claude-code",
        "skills",
        "claude-cookbooks",
        "claude-quickstarts",
        "courses",
        "prompt-eng-interactive-tutorial",
    ],
    "Anthropic SDK & Agent": [
        "claude-agent-sdk-python",
        "claude-agent-sdk-typescript",
        "claude-agent-sdk-demos",
        "anthropic-sdk-python",
        "anthropic-sdk-typescript",
        "anthropic-sdk-go",
        "anthropic-sdk-java",
    ],
    "Anthropic 工具与集成": [
        "claude-code-action",
        "claude-code-security-review",
        "claude-plugins-official",
        "devcontainer-features",
    ],
    "Anthropic 研究与评估": [
        "evals",
        "political-neutrality-eval",
        "hh-rlhf",
    ],
    "AI 编程助手": [
        "cline/cline",
        "paul-gauthier/aider",
        "continuedev/continue",
        "openai/openai-python",
        "openai/openai-quickstart-python",
        "danielmiessler/fabric",
        "ErikBjare/gptme",
    ],
    "Agent 框架": [
        "TransformerOptimus/SuperAGI",
        "Significant-Gravitas/AutoGPT",
        "OpenDevin/OpenDevin",
        "langchain-ai/langchain",
        "langchain-ai/langgraph",
        "langchain-ai/deepagents",
        "langgenius/dify",
        "run-llama/llama_index",
        "microsoft/autogen",
        "microsoft/semantic-kernel",
        "google-gemini/gemini-cli",
        "agentscope-ai/agentscope",
        "agno-agi/agno",
        "crewAIInc/crewAI",
        "huggingface/smolagents",
        "openai/swarm",
    ],
    "自主 AI 编程": [
        "anomalyco/opencode",
        "zed-industries/zed",
        "AndyMik90/Auto-Claude",
    ],
    "AI 编程模型": [
        "openai/codex",
        "TabbyML/tabby",
    ],
    "其他工具": [
        "openinterpreter/open-interpreter",
        "ruvnet/claude-flow",
        "bytedance/deer-flow",
    ],
}


@dataclass
class RepoCategory:
    """仓库分类。"""

    name: str
    repos: list[MonitoredRepo]


def parse_repos_from_config(repos: list[MonitoredRepo]) -> list[RepoCategory]:
    """从配置解析仓库列表到分类。"""
    categories: dict[str, list[MonitoredRepo]] = {name: [] for name in REPO_CATEGORIES}

    for repo in repos:
        repo_name = repo.repo.split("/")[-1] if "/" in repo.repo else repo.repo
        assigned = False
        for category_name, patterns in REPO_CATEGORIES.items():
            for pattern in patterns:
                if "/" in pattern:
                    if repo.repo == pattern:
                        categories[category_name].append(repo)
                        assigned = True
                        break
                else:
                    if repo_name == pattern:
                        categories[category_name].append(repo)
                        assigned = True
                        break
            if assigned:
                break

    return [
        RepoCategory(name=name, repos=repos)
        for name, repos in categories.items()
        if repos
    ]


def generate_repos_markdown(categories: list[RepoCategory]) -> str:
    """生成仓库列表的 Markdown。"""
    total_repos = sum(len(cat.repos) for cat in categories)

    lines = [
        "### 📋 监控项目\n",
        "\n",
        f"我们监控以下 **{total_repos} 个** GitHub 仓库，"
        f"涵盖 Anthropic 生态系统的核心项目：\n",
        "\n",
    ]

    for category in categories:
        lines.append(f"#### {category.name}\n")
        lines.append("\n")
        lines.append('<div class="tp-entry-grid">\n')

        for repo in category.repos:
            display_name = repo.repo
            description = (
                repo.description if repo.description else "趋势追踪与动向监控项目中..."
            )
            # 生成 HTML 卡片
            lines.append(f'  <a class="tp-entry-card" href="{repo.url}">\n')
            lines.append(f"    <strong>{display_name}</strong>\n")
            lines.append(f"    <p>{description}</p>\n")
            lines.append("  </a>\n")

        lines.append("</div>\n\n")

    return "".join(lines)


def generate_homepage_repos_section(categories: list[RepoCategory]) -> str:
    """生成首页监控仓库概览区块。"""
    total_repos = sum(len(category.repos) for category in categories)
    total_categories = len(categories)

    lines = [
        "## 监控范围概览\n",
        "\n",
        f"当前监控 **{total_repos}** 个 GitHub 仓库，覆盖 "
        f"**{total_categories}** 个主要方向。\n",
        "\n",
        '<div class="tp-coverage-grid">\n',
    ]

    for category in categories:
        lines.append(f'  <div class="tp-coverage-pill">{category.name}</div>\n')

    lines.extend(
        [
            "</div>\n",
            "\n",
            "[查看完整监控仓库清单](monitored-repos.md)\n",
        ]
    )
    return "".join(lines)
