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
        env_prefix="TRENDPULSE_",
        extra="ignore",
    )

    # GitHub 配置
    github_token: str = Field(description="GitHub Personal Access Token")
    github_repos: list[str] = Field(
        default=[
            "anthropics/skills",
            "anthropics/claude-quickstarts",
            "anthropics/claude-agent-sdk-python",
            "anthropics/claude-code-security-review",
            "anthropics/anthropic-sdk-python",
        ],
        description="要追踪的仓库列表",
    )
    github_base_url: str = "https://api.github.com"

    # Anthropic 配置
    anthropic_api_key: str = Field(description="Anthropic API Key")
    anthropic_model: str = "claude-sonnet-4-5"
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


# 全局配置实例
settings = Settings()
