"""监控仓库配置模型。"""

from pydantic import BaseModel, Field


class MonitoredRepo(BaseModel):
    """监控仓库配置。"""

    repo: str = Field(description="标准化后的仓库标识 owner/repo")
    url: str = Field(description="GitHub 仓库 URL")
    description: str = Field(default="", description="仓库简介")
