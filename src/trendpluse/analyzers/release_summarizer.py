"""Release 总结器

使用 AI 分析 Release Notes，生成结构化的中文总结。
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.logger import get_logger
from trendpluse.models.signal import ReleaseSummary
from trendpluse.utils.retry import create_anthropic_retry_decorator

logger = get_logger(__name__)

# 创建重试装饰器（统一配置）
_llm_retry = create_anthropic_retry_decorator()

# 可重试的临时错误类型
RETRYABLE_ERRORS = (anthropic.APITimeoutError, anthropic.RateLimitError)


class ReleaseSummarizer(BaseLLMAnalyzer):
    """Release 总结器

    使用 AI 分析 Release Notes，提取关键变更信息并生成中文总结。
    使用 instructor 模式，支持结构化输出（直接返回 Pydantic 模型）。
    """

    def __init__(
        self,
        api_key: str,
        model: str = "glm-4.7",
        base_url: str = "https://open.bigmodel.cn/api/anthropic",
    ):
        """初始化总结器

        Args:
            api_key: API 密钥
            model: 模型名称
            base_url: API 基础 URL
        """
        # 使用 instructor 模式（默认）
        super().__init__(
            api_key=api_key, model=model, base_url=base_url, use_instructor=True
        )

    def summarize_releases(
        self,
        detailed_releases: list[dict],
        max_workers: int = 3,
    ) -> dict[str, ReleaseSummary]:
        """批量总结 Releases（并行处理）

        Args:
            detailed_releases: 详细 Release 信息列表
            max_workers: 最大并行线程数（默认 3）

        Returns:
            {version: ReleaseSummary} 字典
        """
        # 处理空列表
        if not detailed_releases:
            return {}

        # 单个 release 时直接调用，避免线程池开销
        if len(detailed_releases) == 1:
            release = detailed_releases[0]
            key = f"{release['repo']}@{release['tag_name']}"
            return {key: self._summarize_single_release(release)}

        # 并行处理多个 releases
        summaries: dict[str, ReleaseSummary] = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 提交所有任务
            future_to_key: dict = {}
            for release in detailed_releases:
                key = f"{release['repo']}@{release['tag_name']}"
                future = executor.submit(self._summarize_single_release, release)
                future_to_key[future] = key

            # 收集结果
            for future in as_completed(future_to_key):
                key = future_to_key[future]
                try:
                    summaries[key] = future.result()
                except Exception as e:
                    # 单个失败不影响其他 releases
                    logger.debug(f"ReleaseSummarizer: 总结失败 {key} - {e}")
                    # 失败时添加一个默认的 ReleaseSummary
                    repo, tag_name = key.split("@")
                    summaries[key] = ReleaseSummary(
                        change_type="other",
                        key_changes=[],
                        summary_cn=f"{repo} {tag_name} 发布（分析失败）",
                        impact_level=1,
                    )

        return summaries

    @_llm_retry
    def _call_llm_for_summary(self, prompt: str) -> ReleaseSummary:
        """调用 LLM 生成 Release 总结（带重试机制）

        Args:
            prompt: 分析提示词

        Returns:
            ReleaseSummary 对象

        Raises:
            RETRYABLE_ERRORS: 可重试的错误（超时、速率限制）
            Exception: 其他错误向上传播
        """
        summary = self.client.chat.completions.create(
            model=self.model,
            response_model=ReleaseSummary,
            messages=[
                {
                    "role": "system",
                    "content": "你是一个专业的软件变更分析专家，"
                    "擅长分析 Release Notes 并提取关键信息。",
                },
                {"role": "user", "content": prompt},
            ],
            max_tokens=1000,
        )
        return summary  # type: ignore[no-any-return]

    def _summarize_single_release(self, release: dict) -> ReleaseSummary:
        """总结单个 Release

        Args:
            release: 单个 Release 的详细信息

        Returns:
            ReleaseSummary 对象
        """
        body = release.get("body", "")
        tag_name = release.get("tag_name", "")
        repo = release.get("repo", "")

        # 如果没有 body，返回默认总结
        if not body or body.strip() == "":
            return ReleaseSummary(
                change_type="other",
                key_changes=[],
                summary_cn=f"{repo} {tag_name} 发布，暂无详细说明。",
                impact_level=1,
            )

        # 构建 Prompt
        prompt = f"""分析以下 GitHub Release 的变更内容，生成结构化的中文总结。

仓库: {repo}
版本: {tag_name}

Release Notes:
{body[:2000]}

请分析并提取：
1. 变更类型（feature/fix/improvement/breaking/other）
2. 3-5 个关键变更点（简洁的中文描述）
3. 中文总结（2-3 句话概括主要变更）
4. 影响级别（1-5，5 为最高）

注意：
- **所有文本内容必须使用中文**（key_changes、summary_cn）
- 优先识别 Breaking Changes（影响级别应为 5）
- 如果是主版本升级（如 v1.0.0 到 v2.0.0），通常意味着 Breaking Changes
- 新功能优先于修复，修复优先于改进
"""

        # 使用 instructor 获取结构化输出（带重试机制）
        try:
            return self._call_llm_for_summary(prompt)  # type: ignore[no-any-return]
        except RETRYABLE_ERRORS as e:
            # 重试耗尽后的可重试错误
            logger.debug(
                f"ReleaseSummarizer: 重试耗尽 - {type(e).__name__}: {e}, "
                f"Release: {repo}@{tag_name}, Body 长度: {len(body)} 字符"
            )
            # 返回默认总结
            return ReleaseSummary(
                change_type="other",
                key_changes=[],
                summary_cn=f"{repo} {tag_name} 发布（重试失败）",
                impact_level=1,
            )
        except Exception as e:
            # 其他错误（如认证错误，不重试）
            logger.debug(
                f"ReleaseSummarizer: 分析失败 - {type(e).__name__}: {e}, "
                f"Release: {repo}@{tag_name}, Body 长度: {len(body)} 字符"
            )
            # 返回默认总结
            return ReleaseSummary(
                change_type="other",
                key_changes=[],
                summary_cn=f"{repo} {tag_name} 发布",
                impact_level=1,
            )
