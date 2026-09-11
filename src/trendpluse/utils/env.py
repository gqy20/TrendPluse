"""环境变量加载工具

统一封装 python-dotenv 的加载行为，让 `.env` 的优先级高于进程已有的环境变量。

为什么必须覆盖（override=True）：

1. `pydantic-settings` 的取值优先级固定为
   `init 参数 > os.environ > .env 文件 > 默认值`，
   shell 里残留的旧变量会静默盖掉 `.env` 中的新配置。
2. `claude-agent-sdk` 会 fork 出 `claude` CLI 子进程（日报总结 Agent、
   Commit 分析 Agent、Issue Agent），子进程只继承 `os.environ`，
   完全不感知 pydantic 的配置源顺序。

因此只有在进程启动阶段就把 `.env` 写进 `os.environ` 并覆盖同名变量，
主进程与所有子进程才能看到同一份配置。
"""

import os
from pathlib import Path

from dotenv import load_dotenv


def load_env(
    dotenv_path: str | os.PathLike[str] | None = None,
    *,
    override: bool = True,
    interpolate: bool = True,
) -> bool:
    """加载 `.env` 到 `os.environ`，默认覆盖已存在的同名环境变量。

    Args:
        dotenv_path: `.env` 文件路径。为 None 时由 python-dotenv 从调用模块
            所在目录逐级向上查找，因此不依赖当前工作目录。
        override: 是否覆盖已存在的环境变量，默认 True（即 `.env` 优先）。
        interpolate: 是否展开 `${VAR}` 形式的引用，默认 True。

    Returns:
        bool: 是否成功读取到 `.env` 文件（文件不存在时返回 False，且不产生副作用）。
    """
    return bool(
        load_dotenv(
            dotenv_path=dotenv_path,
            override=override,
            interpolate=interpolate,
        )
    )


def load_env_from_project_root(
    filename: str = ".env",
    *,
    override: bool = True,
) -> bool:
    """从项目根目录（`src/` 的上一级）加载指定的 env 文件。

    适用于当前工作目录不在项目根、但仍希望读取仓库内 `.env` 的场景
    （例如从 `scripts/` 或子目录调用 CLI）。

    Args:
        filename: env 文件名，默认 `.env`。
        override: 是否覆盖已存在的环境变量，默认 True。

    Returns:
        bool: 是否成功读取到文件。
    """
    project_root = Path(__file__).resolve().parents[3]
    env_file = project_root / filename
    if not env_file.is_file():
        return load_env(override=override)
    return load_env(env_file, override=override)
