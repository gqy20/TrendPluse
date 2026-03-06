"""监控仓库配置加载工具。"""

import json
from pathlib import Path
from urllib.parse import urlparse

from trendpluse.models.repository import MonitoredRepo


def parse_github_repo_url(url: str) -> str:
    """将 GitHub URL 解析为 owner/repo。"""
    normalized_url = url.strip()
    if not normalized_url:
        raise ValueError("GitHub URL 不能为空")

    parsed = urlparse(normalized_url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc != "github.com":
        raise ValueError(f"Invalid GitHub URL: {url}")

    path = parsed.path.strip("/")
    if path.endswith(".git"):
        path = path[:-4]

    parts = [part for part in path.split("/") if part]
    if len(parts) < 2:
        raise ValueError(f"Invalid GitHub repository URL: {url}")

    return f"{parts[0]}/{parts[1]}"


def load_monitored_repo_configs(path: str) -> list[MonitoredRepo]:
    """从 JSON 文件加载监控仓库配置。"""
    config_path = Path(path)
    if not config_path.exists():
        return []

    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid repo config JSON: {config_path}") from exc

    if not isinstance(data, list):
        raise ValueError("Repo config must be a JSON array")

    repos: list[MonitoredRepo] = []
    for index, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Repo config entry #{index} must be an object")

        url = str(item.get("url", "")).strip()
        description = str(item.get("description", "")).strip()
        repo = parse_github_repo_url(url)
        repos.append(
            MonitoredRepo(
                repo=repo,
                url=url,
                description=description,
            )
        )

    return repos
