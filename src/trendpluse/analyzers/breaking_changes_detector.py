"""Breaking Changes 检测器

使用 AI 分析 release notes，检测 breaking changes 和不兼容更新。
"""

import json
from typing import Any

from anthropic import Anthropic


class BreakingChangesDetector:
    """Breaking Changes 检测器

    分析 release notes，检测 breaking changes 和不兼容更新。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str | None = None,
    ):
        """初始化检测器

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

    def detect_breaking_changes(self, releases: dict[str, Any]) -> list[dict]:
        """检测 breaking changes

        Args:
            releases: release 数据字典

        Returns:
            breaking changes 列表
        """
        # 获取详细的 release 列表
        detailed_releases = releases.get("detailed_releases", [])

        # 处理空列表
        if not detailed_releases:
            print("[DEBUG] BreakingChangesDetector: 收到空 release 列表")
            return []

        print(
            f"[DEBUG] BreakingChangesDetector: 开始分析 "
            f"{len(detailed_releases)} 个 releases"
        )

        try:
            # 调用 LLM 分析
            print("[DEBUG] BreakingChangesDetector: 调用 LLM 分析...")
            llm_response = self._call_llm(detailed_releases)
            print(
                f"[DEBUG] BreakingChangesDetector: LLM 响应长度: "
                f"{len(llm_response)} 字符"
            )

            # 解析响应
            breaking_changes = self._parse_response(llm_response)
            print(
                f"[DEBUG] BreakingChangesDetector: 检测到 "
                f"{len(breaking_changes)} 个 breaking changes"
            )

            return breaking_changes

        except Exception as e:
            # 出错时返回空列表
            print(
                f"[DEBUG] BreakingChangesDetector: 检测失败 - {type(e).__name__}: {e}"
            )
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

        prompt = f"""你是一个技术分析专家。请分析以下 GitHub Releases，\
识别 breaking changes（不兼容更新）。

## Release 数据

{releases_text}

## 分析要求

请识别以下内容：

1. **Breaking Changes 判断标准**：
   - API 移除或重命名
   - 函数签名变更
   - 行为不兼容改变
   - 配置格式变更
   - 依赖版本要求改变

2. **影响等级评估**：
   - high：需要大量代码迁移，影响核心功能
   - medium：需要少量代码调整
   - low：配置或轻微行为变更

3. **分类**：
   - API：接口相关
   - Config：配置相关
   - Behavior：行为变更
   - Dependency：依赖变更

## 输出格式

请以 JSON 数组格式返回，**只包含有 breaking changes 的 releases**：

```json
[
  {{
    "repo": "仓库名",
    "tag_name": "版本标签",
    "has_breaking": true,
    "changes": [
      {{
        "description": "变更描述（简短）",
        "impact": "影响等级（high/medium/low）",
        "category": "分类（API/Config/Behavior/Dependency）"
      }}
    ]
  }}
]
```

注意：
- **只返回有 breaking changes 的版本**
- **如果某个版本没有 breaking changes，不要包含在结果中**
- **如果没有任何 breaking changes，返回空数组 []**
"""

        return prompt

    def _parse_response(self, llm_response: str) -> list[dict]:
        """解析 LLM 响应

        Args:
            llm_response: LLM 响应文本

        Returns:
            breaking changes 列表
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

            # 验证返回的是列表
            if not isinstance(data, list):
                return []

            return data

        except (json.JSONDecodeError, TypeError, ValueError):
            # 解析失败时返回空列表
            return []
