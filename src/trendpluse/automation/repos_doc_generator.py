"""仓库文档生成器

从 config 生成监控仓库列表的 Markdown 文档。
"""

from dataclasses import dataclass

from trendpluse.models.repository import MonitoredRepo

# 定义仓库分类规则
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
    """仓库分类"""

    name: str
    repos: list[MonitoredRepo]


def parse_repos_from_config(repos: list[MonitoredRepo]) -> list[RepoCategory]:
    """从配置解析仓库列表到分类

    Args:
        repos: 结构化仓库配置列表

    Returns:
        仓库分类列表
    """
    # 初始化分类
    categories: dict[str, list[MonitoredRepo]] = {name: [] for name in REPO_CATEGORIES}

    # 分配仓库到分类
    for repo in repos:
        # 提取仓库名部分
        repo_name = repo.repo.split("/")[-1] if "/" in repo.repo else repo.repo

        # 查找匹配的分类
        assigned = False
        for category_name, patterns in REPO_CATEGORIES.items():
            # 检查完整匹配或模式匹配
            for pattern in patterns:
                if "/" in pattern:
                    # 完整匹配 owner/repo
                    if repo.repo == pattern:
                        categories[category_name].append(repo)
                        assigned = True
                        break
                else:
                    # 仓库名匹配
                    if repo_name == pattern:
                        categories[category_name].append(repo)
                        assigned = True
                        break
            if assigned:
                break

    # 转换为 RepoCategory 对象，过滤空分类
    return [
        RepoCategory(name=name, repos=repos)
        for name, repos in categories.items()
        if repos
    ]


def generate_repos_markdown(categories: list[RepoCategory]) -> str:
    """生成仓库列表的 Markdown

    Args:
        categories: 仓库分类列表

    Returns:
        Markdown 格式的仓库列表
    """
    # 统计总仓库数
    total_repos = sum(len(cat.repos) for cat in categories)

    lines = [
        "### 📋 监控项目\n",
        "\n",
        f"我们监控以下 **{total_repos} 个** GitHub 仓库，"
        f"涵盖 Anthropic 生态系统的核心项目：\n",
        "\n",
    ]

    # 生成每个分类的内容
    for category in categories:
        lines.append(f"#### {category.name}\n")
        lines.append("\n")

        for repo in category.repos:
            # 转义下划线（Markdown 特殊字符）
            escaped_repo = repo.repo.replace("_", "\\_")
            repo_link = f"[{escaped_repo}]({repo.url})"
            description = f": {repo.description}" if repo.description else ""
            lines.append(f"- **{repo_link}**{description}\n")

        lines.append("\n")

    return "".join(lines)
