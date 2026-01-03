"""配置管理模块

使用 pydantic-settings 管理配置，支持环境变量和 .env 文件。
"""

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """配置管理类，支持环境变量和 .env 文件"""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="",  # 移除前缀，直接使用变量名
        extra="ignore",
    )

    # GitHub 配置
    github_token: str = Field(default="", description="GitHub Personal Access Token")
    github_repos: list[str] = Field(
        default=[
            # Anthropic 核心产品
            "anthropics/claude-code",
            "anthropics/skills",
            "anthropics/claude-cookbooks",
            "anthropics/claude-quickstarts",
            "anthropics/courses",
            "anthropics/prompt-eng-interactive-tutorial",
            # Anthropic SDK & Agent
            "anthropics/claude-agent-sdk-python",
            "anthropics/claude-agent-sdk-typescript",
            "anthropics/claude-agent-sdk-demos",
            "anthropics/anthropic-sdk-python",
            "anthropics/anthropic-sdk-typescript",
            "anthropics/anthropic-sdk-go",
            "anthropics/anthropic-sdk-java",
            # Anthropic 工具与集成
            "anthropics/claude-code-action",
            "anthropics/claude-code-security-review",
            "anthropics/claude-plugins-official",
            "anthropics/devcontainer-features",
            # Anthropic 研究与评估
            "anthropics/evals",
            "anthropics/political-neutrality-eval",
            "anthropics/hh-rlhf",
            # AI 编程助手
            "cline/cline",
            "paul-gauthier/aider",
            "continuedev/continue",
            "openai/openai-python",
            "openai/openai-quickstart-python",
            "danielmiessler/fabric",
            "ErikBjare/gptme",
            # Agent 框架
            "TransformerOptimus/SuperAGI",
            "Significant-Gravitas/AutoGPT",
            "OpenDevin/OpenDevin",
            "langchain-ai/langchain",
            "langgenius/dify",
            "run-llama/llama_index",
            "microsoft/autogen",
            "google-gemini/gemini-cli",
            "agentscope-ai/agentscope",
            "agno-agi/agno",
        ],
        description="要追踪的仓库列表",
    )
    github_base_url: str = "https://api.github.com"

    # Anthropic/智谱 AI 配置
    anthropic_api_key: str = Field(description="Anthropic/智谱 AI API Key")
    anthropic_base_url: str = Field(
        default="https://open.bigmodel.cn/api/anthropic",
        description="API Base URL (智谱AI: https://open.bigmodel.cn/api/anthropic)",
    )
    anthropic_model: str = Field(
        default="glm-4.7", description="模型名称 (glm-4.7, claude-sonnet-4-20250514 等)"
    )
    anthropic_max_tokens: int = 8000
    anthropic_timeout: int = 120

    # 筛选规则
    candidate_labels: list[str] = [
        "feature",
        "enhancement",
        "eval",
        "tooling",
        "agent",
        "workflow",
        "safety",
    ]
    max_candidates: int = 20
    days_to_lookback: int = 1

    # Release 监控配置
    monitor_releases: bool = Field(default=True, description="是否监控 Releases")
    include_prereleases: bool = Field(
        default=False, description="是否包含预发布版本（alpha/beta/rc）"
    )

    # 成本控制
    daily_token_budget: int = 100_000
    max_retries: int = 3

    # 输出配置
    output_dir: str = "reports/daily"
    snapshot_dir: str = "data/snapshots"

    @field_validator("github_repos")
    @classmethod
    def validate_repos(cls, v: list[str]) -> list[str]:
        """验证仓库格式：必须是 owner/repo 格式"""
        for repo in v:
            if "/" not in repo or len(repo.split("/")) != 2:
                raise ValueError(f'Invalid repo format: "{repo}". Must be "owner/repo"')
        return v


# 全局配置实例（延迟初始化）
_settings_instance = None


def get_settings() -> Settings:
    """获取全局配置实例

    Returns:
        Settings 实例
    """
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance


# 为了向后兼容，保留 settings 属性
class _SettingsProxy:
    """Settings 代理，支持延迟初始化"""

    def __getattr__(self, name: str):
        return getattr(get_settings(), name)

    def __setattr__(self, name: str, value):
        setattr(get_settings(), name, value)


settings = _SettingsProxy()
