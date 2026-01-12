"""Commit 分析器

使用 AI 分析 commit 内容，提取技术趋势和代码变更统计。
"""

import json
from typing import Any

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.models.signal import Signal


class CommitAnalyzer(BaseLLMAnalyzer):
    """Commit 分析器

    分析 commit 内容，提取技术趋势和代码变更统计。
    使用 Anthropic 模式（手动解析 JSON），因为需要处理多个 commit 的批量分析。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "claude-sonnet-4-20250514",
        base_url: str | None = None,
    ):
        """初始化分析器

        Args:
            api_key: Anthropic API Key
            model: 使用的模型
            base_url: API 基础 URL（可选）
        """
        # 使用 Anthropic 模式（手动解析 JSON）
        super().__init__(
            api_key=api_key, model=model, base_url=base_url, use_instructor=False
        )

    def analyze_commits(self, commits: list[dict[str, Any]]) -> list[Signal]:
        """分析 commit 列表

        Args:
            commits: commit 数据列表

        Returns:
            信号列表
        """
        # 处理空列表
        if not commits:
            print("[DEBUG] CommitAnalyzer: 收到空 commit 列表")
            return []

        print(f"[DEBUG] CommitAnalyzer: 开始分析 {len(commits)} 个 commits")

        try:
            # 调用 LLM 分析
            print("[DEBUG] CommitAnalyzer: 调用 LLM 分析...")
            llm_response = self._call_llm(commits)
            print(f"[DEBUG] CommitAnalyzer: LLM 响应长度: {len(llm_response)} 字符")
            print(f"[DEBUG] CommitAnalyzer: LLM 响应预览: {llm_response[:500]}...")

            # 解析响应
            signals = self._parse_signals(llm_response, commits)
            print(f"[DEBUG] CommitAnalyzer: 解析得到 {len(signals)} 个信号")

            return signals

        except Exception as e:
            # 出错时返回空列表
            print(f"[DEBUG] CommitAnalyzer: 分析失败 - {type(e).__name__}: {e}")
            return []

    def _call_llm(self, commits: list[dict[str, Any]]) -> str:
        """调用 LLM 分析 commits

        Args:
            commits: commit 数据列表

        Returns:
            LLM 响应文本
        """
        # 构建 prompt
        prompt = self._build_prompt(commits)

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

        # 使用基类方法提取文本
        return self._extract_text_from_response(message)

    def _build_prompt(self, commits: list[dict[str, Any]]) -> str:
        """构建分析 prompt

        Args:
            commits: commit 数据列表

        Returns:
            prompt 文本
        """
        commits_text = json.dumps(commits, ensure_ascii=False, indent=2)

        prompt = """\
你是一个技术趋势分析专家。请分析以下 GitHub commits，提取有价值的\
技术趋势和代码变更统计。

## Commit 数据

{commits_text}

## 分析要求

请识别以下内容：

1. **技术趋势**：
   - 新特性/功能（capability）
   - 抽象层改进（abstraction）
   - 工作流优化（workflow）
   - 评估/测试改进（eval）
   - 安全性增强（safety）
   - 性能优化（performance）

2. **代码变更统计**：
   - 文件类型分布
   - 修改规模
   - 代码复杂度

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
    "commit_sha": "从输入 commit 数据中精确复制对应的 sha 字段值",
    "related_repos": ["受此趋势影响或相关的仓库（可选，系统会自动添加当前commit仓库）"],
    "trends": ["趋势关键词"],
    "tech_details": {{
      "feature_type": "特性类型",
      "complexity": "复杂度（低/中/高）",
      "files_affected": "影响的文件类型"
    }}
  }}
]
```

注意：
- **commit_sha 必需**：必须从输入的 commit 数据中精确复制对应的 `sha` 字段值
- 精确匹配：确保信号与正确的 commit 关联，避免索引错位
- 只返回真正有价值的趋势（避免琐碎修复）
- impact_score 基于影响范围和重要性
- related_repos 可选：列出除当前仓库外，其他相关或影响的仓库
- 如果没有有价值的趋势，返回空数组 []
"""

        return prompt.format(commits_text=commits_text)

    def _parse_signals(
        self, llm_response: str, commits: list[dict[str, Any]]
    ) -> list[Signal]:
        """解析 LLM 响应为信号列表

        Args:
            llm_response: LLM 响应文本
            commits: 原始 commit 数据

        Returns:
            信号列表
        """
        try:
            # 使用基类方法提取 JSON
            response_text = self._extract_json_from_markdown(llm_response)

            # 解析 JSON
            data = json.loads(response_text)

            # 处理空数组
            if not data:
                return []

            # 转换为 Signal 对象
            signals = []
            for idx, item in enumerate(data):
                # 优先使用 LLM 返回的 commit_sha 进行匹配
                commit_sha = item.get("commit_sha")

                # 尝试通过 SHA 匹配
                matching_commit = None
                if commit_sha:
                    matching_commit = next(
                        (c for c in commits if c.get("sha") == commit_sha), None
                    )

                # 如果 SHA 匹配成功，使用精确匹配
                if matching_commit:
                    repo = matching_commit.get("repo", "")
                    commit_url = f"https://github.com/{repo}/commit/{commit_sha}"
                    sources = [commit_url]
                    related_repos = [repo]
                else:
                    # SHA 未提供或未找到，回退到索引匹配（向后兼容）
                    if idx < len(commits):
                        commit_sha_fallback = commits[idx].get("sha", "")
                        repo = commits[idx].get("repo", "")
                        commit_url = (
                            f"https://github.com/{repo}/commit/{commit_sha_fallback}"
                        )
                        sources = [commit_url]
                        related_repos = [repo]
                    else:
                        sources = []
                        related_repos = []

                # 使用基类方法创建 Signal
                signal = self._create_signal_from_dict(
                    item=item,
                    index=idx,
                    sources=sources,
                    related_repos=related_repos,
                )
                signals.append(signal)

            return signals

        except (json.JSONDecodeError, KeyError, TypeError):
            # 解析失败时返回空列表
            return []
