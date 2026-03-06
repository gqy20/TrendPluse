"""测试 SHA 匹配失败时的信号来源处理

验证当 LLM 返回的 commit_sha 在 commits 列表中找不到时，
应该回退到索引匹配，而不是使用空 sources 列表。
"""

import json
from unittest.mock import Mock, patch


class TestSHAMismatch:
    """测试 SHA 匹配失败处理"""

    @patch("trendpluse.app.pipeline.Settings")
    @patch("trendpluse.app.pipeline.CommitAnalyzer")
    def test_fallback_to_index_matching_when_sha_not_found(
        self, mock_commit_analyzer, mock_settings
    ):
        """测试：SHA 找不到时应回退到索引匹配"""
        # Arrange - 设置 mock settings
        mock_settings_instance = Mock()
        mock_settings_instance.github_token = "test_token"
        mock_settings_instance.anthropic_api_key = "test_api_key"
        mock_settings_instance.anthropic_model = "glm-4.7"
        mock_settings_instance.anthropic_base_url = (
            "https://open.bigmodel.cn/api/anthropic"
        )
        mock_settings_instance.github_repos = ["anthropics/skills"]
        mock_settings_instance.max_candidates = 20
        mock_settings_instance.days_to_lookback = 1
        mock_settings_instance.feishu_webhook_url = None
        mock_settings.return_value = mock_settings_instance

        # 准备 commits 数据
        commits = [
            {
                "sha": "abc123",
                "repo": "test/repo",
                "message": "First commit",
                "author": "test",
                "date": "2026-01-02",
            },
            {
                "sha": "def456",
                "repo": "test/repo",
                "message": "Second commit",
                "author": "test",
                "date": "2026-01-02",
            },
        ]

        # LLM 返回的 JSON（包含一个不存在的 SHA）
        llm_response = json.dumps(
            [
                {
                    "title": "Test Signal",
                    "type": "capability",
                    "category": "engineering",
                    "impact_score": 4,
                    "why_it_matters": "Test signal with wrong SHA",
                    "commit_sha": "wrongsha123",  # 这个 SHA 不在 commits 中
                    "related_repos": ["test/repo"],
                }
            ]
        )

        # Act - 调用 CommitAnalyzer
        from trendpluse.analyzers.commit_analyzer import CommitAnalyzer

        analyzer = CommitAnalyzer(api_key="test_key", model="test-model", base_url=None)
        signals = analyzer._parse_signals(llm_response, commits)

        # Assert - 验证信号有 sources（通过索引匹配回退）
        assert len(signals) == 1
        assert len(signals[0].sources) > 0, "即使 SHA 匹配失败，也应该有 sources"
        assert "https://github.com/test/repo/commit/abc123" in signals[0].sources[0], (
            "应该回退到索引匹配，使用第一个 commit 的 SHA"
        )
