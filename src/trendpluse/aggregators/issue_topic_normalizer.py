"""Issue 痛点主题归一化（LLM 驱动）"""

from __future__ import annotations

from trendpluse.analyzers.base import BaseLLMAnalyzer
from trendpluse.logger import get_logger

logger = get_logger(__name__)


class IssueTopicNormalizer(BaseLLMAnalyzer):
    """使用 LLM 将痛点主题归一化为短中文主题"""

    def __init__(
        self,
        api_key: str,
        model: str,
        base_url: str | None = None,
        retry_max_attempts: int = 3,
        retry_wait_min: int = 1,
        retry_wait_max: int = 10,
    ) -> None:
        super().__init__(
            api_key=api_key,
            model=model,
            base_url=base_url,
            use_instructor=False,
            retry_max_attempts=retry_max_attempts,
            retry_wait_min=retry_wait_min,
            retry_wait_max=retry_wait_max,
        )

    def normalize_topics(self, topics: list[str]) -> dict[str, str]:
        if not topics:
            return {}

        prompt = """你是一个问题归纳专家。请将以下用户痛点主题归一化为短中文主题。

要求：
- 每个主题只保留 8-16 个中文字符
- 去掉公告/宣传/发布类内容
- 如果主题无意义或是营销内容，返回空字符串

输出格式：严格 JSON 对象，key 为原主题，value 为归一化中文主题。

主题列表：
""" + "\n".join(f"- {topic}" for topic in topics)

        def _call():
            return self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.2,
                messages=[{"role": "user", "content": prompt}],
            )

        try:
            response = self._run_with_llm_retry(_call)
            text = self._extract_text_from_response(response)
            return self._parse_json(text)
        except Exception as exc:
            logger.debug(f"主题归一化失败: {exc}")
            return {}

    def _parse_json(self, text: str) -> dict[str, str]:
        import json

        cleaned = self._extract_json_from_markdown(text)
        try:
            data = json.loads(cleaned)
        except json.JSONDecodeError:
            return {}
        if not isinstance(data, dict):
            return {}
        return {str(k): str(v) for k, v in data.items()}
