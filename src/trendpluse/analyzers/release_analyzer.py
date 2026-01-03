"""Release 分析器

使用 AI 分析 release 内容，提取版本升级趋势和重要特性。
"""

import json
from typing import Any

from anthropic import Anthropic

from trendpluse.models.signal import Signal


class ReleaseAnalyzer:
    """Release 分析器

    分析 release 内容，提取版本升级趋势和重要特性。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str | None = None,
    ):
        """初始化分析器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL（可选）
        """
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

        # 初始化 Anthropic 客户端
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url
        self.client = Anthropic(**client_kwargs)

    def analyze_releases(self, releases: dict[str, Any]) -> list[Signal]:
        """分析 release 列表

        Args:
            releases: release 数据字典

        Returns:
            信号列表
        """
        # 获取详细的 release 列表
        detailed_releases = releases.get("detailed_releases", [])

        # 处理空列表
        if not detailed_releases:
            print("[DEBUG] ReleaseAnalyzer: 收到空 release 列表")
            return []

        print(f"[DEBUG] ReleaseAnalyzer: 开始分析 {len(detailed_releases)} 个 releases")

        try:
            # 调用 LLM 分析
            print("[DEBUG] ReleaseAnalyzer: 调用 LLM 分析...")
            llm_response = self._call_llm(detailed_releases)
            print(f"[DEBUG] ReleaseAnalyzer: LLM 响应长度: {len(llm_response)} 字符")
            print(f"[DEBUG] ReleaseAnalyzer: LLM 响应预览: {llm_response[:500]}...")

            # 解析响应
            signals = self._parse_signals(llm_response, detailed_releases)
            print(f"[DEBUG] ReleaseAnalyzer: 解析得到 {len(signals)} 个信号")

            return signals

        except Exception as e:
            # 出错时返回空列表
            print(f"[DEBUG] ReleaseAnalyzer: 分析失败 - {type(e).__name__}: {e}")
            return []

    def _call_llm(self, releases: list[dict[str, Any]]) -> str:
        """调用 LLM 分析 releases

        Args:
            releases: release 数据列表

        Returns:
            LLM 响应文本
        """
        # 构建 prompt
        prompt = self._build_prompt(releases)

        # 调用 API
        message = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            temperature=0.3,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return message.content[0].text

    def _build_prompt(self, releases: list[dict[str, Any]]) -> str:
        """构建分析 prompt

        Args:
            releases: release 数据列表

        Returns:
            prompt 文本
        """
        releases_text = json.dumps(releases, ensure_ascii=False, indent=2)

        prompt = """\
你是一个技术趋势分析专家。请分析以下 GitHub Releases，提取有价值的\
版本升级趋势和重要特性信息。

## Release 数据

{releases_text}

## 分析要求

请识别以下内容：

1. **重大版本升级**：
   - 主版本升级（major version bump）
   - Breaking changes
   - 重大架构变更

2. **重要新特性**：
   - 新功能发布（capability）
   - 抽象层改进（abstraction）
   - 工作流优化（workflow）
   - 安全性增强（safety）
   - 性能优化（performance）

3. **评估标准**：
   - 优先关注主版本升级（如 v1.0.0 → v2.0.0）
   - 关注重要的次版本更新（如包含 breaking changes）
   - **过滤掉纯 bug 修复的补丁版本**（如 v1.0.0 → v1.0.1）
   - 关注影响范围广的特性
   - 关注技术创新点

## 输出格式

请以 JSON 数组格式返回，每个元素包含：

```json
[
  {{
    "title": "简短标题（5-10字）",
    "type": "信号类型（capability/abstraction/workflow/eval/safety/performance）",
    "category": "分类（engineering/research）",
    "impact_score": 影响评分（1-5）,
    "why_it_matters": "为什么重要（1-2句话）",
    "related_repos": ["相关仓库名"],
    "sources": ["release链接"]
  }}
]
```

注意：
- **只返回真正有价值的重大更新**
- **忽略纯 bug 修复的补丁版本**
- **如果没有重要更新，返回空数组 []**
- impact_score 基于影响范围和重要性（主版本升级通常 4-5 分）
"""

        return prompt.format(releases_text=releases_text)

    def _parse_signals(
        self, llm_response: str, releases: list[dict[str, Any]]
    ) -> list[Signal]:
        """解析 LLM 响应为信号列表

        Args:
            llm_response: LLM 响应文本
            releases: 原始 release 数据

        Returns:
            信号列表
        """
        try:
            # 移除可能的 markdown 代码块标记
            response_text = llm_response.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:]  # 移除 ```json
            elif response_text.startswith("```"):
                response_text = response_text[3:]  # 移除 ```
            if response_text.endswith("```"):
                response_text = response_text[:-3]  # 移除结尾的 ```
            response_text = response_text.strip()

            # 解析 JSON
            data = json.loads(response_text)

            # 处理空数组
            if not data:
                return []

            # 转换为 Signal 对象
            signals = []
            for idx, item in enumerate(data):
                # 构建来源链接
                if idx < len(releases):
                    repo = releases[idx].get("repo", "")
                    tag_name = releases[idx].get("tag_name", "")
                    release_url = f"https://github.com/{repo}/releases/tag/{tag_name}"
                    sources = [release_url]
                else:
                    sources = item.get("sources", [])

                signal = Signal(
                    id=f"release-{idx}",
                    title=item["title"],
                    type=item["type"],
                    category=item["category"],
                    impact_score=item["impact_score"],
                    why_it_matters=item["why_it_matters"],
                    sources=sources,
                    related_repos=item["related_repos"],
                )
                signals.append(signal)

            return signals

        except (json.JSONDecodeError, KeyError, TypeError):
            # 解析失败时返回空列表
            return []
