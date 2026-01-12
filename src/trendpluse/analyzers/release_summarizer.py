"""Release 总结器

使用 AI 分析 Release Notes，生成结构化的中文总结。
"""

from openai import OpenAI  # type: ignore[import-not-found]

from trendpluse.models.signal import ReleaseSummary


class ReleaseSummarizer:
    """Release 总结器

    使用 AI 分析 Release Notes，提取关键变更信息并生成中文总结。
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
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model = model

    def summarize_releases(
        self, detailed_releases: list[dict]
    ) -> dict[str, ReleaseSummary]:
        """批量总结 Releases

        Args:
            detailed_releases: 详细 Release 信息列表

        Returns:
            {version: ReleaseSummary} 字典
        """
        summaries: dict[str, ReleaseSummary] = {}

        for release in detailed_releases:
            # 使用 version + repo 作为唯一标识
            key = f"{release['repo']}@{release['tag_name']}"
            summary = self._summarize_single_release(release)
            summaries[key] = summary

        return summaries

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
- 优先识别 Breaking Changes（影响级别应为 5）
- 如果是主版本升级（如 v1.0.0 到 v2.0.0），通常意味着 Breaking Changes
- 新功能优先于修复，修复优先于改进
"""

        # 使用 instructor 获取结构化输出
        try:
            from instructor import Mode, from_openai

            client = from_openai(self.client)
            summary = client.chat.completions.create(
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
                mode=Mode.JSON,
            )
            return summary  # type: ignore[no-any-return]
        except Exception:
            # 如果 AI 调用失败，返回默认总结
            return ReleaseSummary(
                change_type="other",
                key_changes=[],
                summary_cn=f"{repo} {tag_name} 发布",
                impact_level=1,
            )
