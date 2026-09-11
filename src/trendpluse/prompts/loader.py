"""Prompt 模板加载与渲染。

所有发给 LLM 的提示词统一存放在本包的 YAML 文件中（每个分析器一份），
通过 :func:`render_prompt` 渲染。模板使用 jinja2 语法（``{{ var }}``），
字面 JSON 大括号无需转义。

key 命名为 ``文件名.条目名``，例如 ``trend_analyzer.aggregation``。
"""

from __future__ import annotations

from functools import cache, lru_cache
from importlib import resources
from typing import Any

import yaml
from jinja2 import Environment, StrictUndefined, Template


class PromptNotFoundError(Exception):
    """提示词 key 不存在。"""


@lru_cache(maxsize=1)
def _load_registry() -> dict[str, str]:
    """加载包内所有 YAML 提示词文件（进程内缓存）。

    Returns:
        key 到模板文本的映射。

    Raises:
        ValueError: YAML 结构非法或 key 冲突。
    """
    registry: dict[str, str] = {}
    root = resources.files("trendpluse.prompts")
    for entry in sorted(root.iterdir(), key=lambda e: e.name):
        name = entry.name
        if not (name.endswith((".yml", ".yaml")) and entry.is_file()):
            continue
        data = yaml.safe_load(entry.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError(f"提示词文件结构错误（顶层必须是映射）: {name}")
        stem = name.rsplit(".", 1)[0]
        for key, value in data.items():
            if not isinstance(value, str):
                raise ValueError(f"提示词必须是字符串: {name}:{key}")
            full_key = f"{stem}.{key}"
            if full_key in registry:
                raise ValueError(f"提示词 key 冲突: {full_key}")
            registry[full_key] = value
    if not registry:
        raise ValueError("未找到任何提示词 YAML 文件")
    return registry


@cache
def _get_template(key: str) -> Template:
    """编译并缓存模板（StrictUndefined，缺变量渲染时直接报错）。

    使用自定义定界符 ``{$ var $}`` 而非 jinja2 默认的 ``{{ var }}``，
    因为提示词中常含字面 JSON 双花括号（如返回示例），默认定界符会冲突。
    """
    env = Environment(
        undefined=StrictUndefined,
        keep_trailing_newline=True,
        autoescape=False,
        variable_start_string="{$",
        variable_end_string="$}",
    )
    return env.from_string(_load_registry()[key])


def render_prompt(key: str, /, **context: Any) -> str:
    """渲染提示词模板。

    Args:
        key: 提示词 key，格式 ``文件名.条目名``。
        **context: 模板变量（f-string 中的表达式应在调用侧预计算后传入）。

    Returns:
        渲染后的提示词文本。

    Raises:
        PromptNotFoundError: key 不存在（错误信息中列出全部可用 key）。
        UndefinedError: 缺少模板变量（fail-fast，绝不静默渲染成空串）。
    """
    registry = _load_registry()
    if key not in registry:
        raise PromptNotFoundError(f"提示词不存在: {key}（可用: {sorted(registry)}）")
    return _get_template(key).render(**context)


def available_prompts() -> list[str]:
    """列出全部可用提示词 key（主要用于测试和排障）。"""
    return sorted(_load_registry())
