"""CommitAnalyzer 重构测试

测试重构后的行为：
1. CommitAnalyzer 提取"技术点"而非"趋势"
2. 每个信号对应单个 commit（1:1 映射）
3. 链接正确映射到对应的 commit
"""

from unittest.mock import MagicMock, patch

from trendpluse.analyzers.commit_analyzer import CommitAnalyzer


class TestCommitAnalyzerRefactored:
    """测试重构后的 CommitAnalyzer"""

    def test_analyze_commits_returns_technical_points_not_trends(self):
        """测试：返回的是技术点而非趋势"""
        # Arrange
        analyzer = CommitAnalyzer(
            api_key="test-key",
            model="claude-sonnet-4-20250514",
        )

        commits = [
            {
                "repo": "anthropic/claude-code",
                "sha": "abc123def456",
                "message": "Add multi-file editing support",
                "author": "user1",
                "timestamp": "2026-01-04T10:00:00Z",
            },
            {
                "repo": "cline/cline",
                "sha": "789ghi012jkl",
                "message": "Fix agent memory leak",
                "author": "user2",
                "timestamp": "2026-01-04T11:00:00Z",
            },
        ]

        # Mock LLM 响应 - 返回技术点，每个对应单个 commit
        llm_response = """```json
[
  {
    "title": "多文件编辑功能",
    "type": "capability",
    "category": "engineering",
    "impact_score": 4,
    "why_it_matters": "支持同时编辑多个文件，提升用户体验",
    "related_repos": ["anthropic/claude-code"],
    "commit_sha": "abc123def456"
  },
  {
    "title": "Agent 内存修复",
    "type": "safety",
    "category": "engineering",
    "impact_score": 3,
    "why_it_matters": "修复长时间运行的内存泄漏问题",
    "related_repos": ["cline/cline"],
    "commit_sha": "789ghi012jkl"
  }
]
```"""

        # Act
        with patch.object(analyzer.client.messages, "create") as mock_create:
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text=llm_response)]
            mock_create.return_value = mock_response

            signals = analyzer.analyze_commits(commits)

        # Assert
        assert len(signals) == 2

        # 验证第一个信号
        signal1 = signals[0]
        assert signal1.title == "多文件编辑功能"
        assert signal1.type == "capability"
        assert signal1.sources == [
            "https://github.com/anthropic/claude-code/commit/abc123def456"
        ]
        assert signal1.related_repos == ["anthropic/claude-code"]

        # 验证第二个信号
        signal2 = signals[1]
        assert signal2.title == "Agent 内存修复"
        assert signal2.sources == ["https://github.com/cline/cline/commit/789ghi012jkl"]

    def test_signal_maps_to_correct_commit_by_sha_not_index(self):
        """测试：通过 SHA 匹配而不是索引匹配"""
        # Arrange
        analyzer = CommitAnalyzer(api_key="test-key")

        commits = [
            {"repo": "repo/a", "sha": "aaa111", "message": "Unimportant fix"},
            {"repo": "repo/b", "sha": "bbb222", "message": "Important feature"},
            {"repo": "repo/c", "sha": "ccc333", "message": "Another fix"},
        ]

        # LLM 只提取有价值的 commit（bbb222）
        llm_response = """```json
[
  {
    "title": "重要新功能",
    "type": "capability",
    "category": "engineering",
    "impact_score": 5,
    "why_it_matters": "这是一个关键功能",
    "related_repos": ["repo/b"],
    "commit_sha": "bbb222"
  }
]
```"""

        # Act
        with patch.object(analyzer.client.messages, "create") as mock_create:
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text=llm_response)]
            mock_create.return_value = mock_response

            signals = analyzer.analyze_commits(commits)

        # Assert
        assert len(signals) == 1
        # 关键断言：链接应该指向 bbb222，而不是按索引的 aaa111
        assert signals[0].sources == ["https://github.com/repo/b/commit/bbb222"]

    def test_returns_empty_list_when_no_valuable_commits(self):
        """测试：当没有有价值的技术点时返回空列表"""
        # Arrange
        analyzer = CommitAnalyzer(api_key="test-key")

        commits = [
            {"repo": "repo/a", "sha": "aaa111", "message": "fix typo"},
            {"repo": "repo/b", "sha": "bbb222", "message": "update readme"},
        ]

        llm_response = """```json
[]
```"""

        # Act
        with patch.object(analyzer.client.messages, "create") as mock_create:
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text=llm_response)]
            mock_create.return_value = mock_response

            signals = analyzer.analyze_commits(commits)

        # Assert
        assert signals == []

    def test_includes_commit_sha_in_prompt(self):
        """测试：Prompt 包含 commit SHA 供 LLM 引用"""
        # Arrange
        analyzer = CommitAnalyzer(api_key="test-key")

        commits = [
            {"repo": "test/repo", "sha": "abc123", "message": "Test commit"},
        ]

        # Act
        with patch.object(analyzer.client.messages, "create") as mock_create:
            mock_create.return_value = MagicMock(content=[MagicMock(text="[]")])

            analyzer.analyze_commits(commits)

            # Assert
            call_args = mock_create.call_args
            prompt = call_args.kwargs["messages"][0]["content"]

            # 验证 prompt 包含 commits 的 JSON（包含 sha 字段）
            assert "abc123" in prompt
            assert '"sha"' in prompt

    def test_fallback_to_index_mapping_if_sha_missing(self):
        """测试：如果 LLM 没有返回 commit_sha，回退到索引匹配（向后兼容）"""
        # Arrange
        analyzer = CommitAnalyzer(api_key="test-key")

        commits = [
            {"repo": "test/repo", "sha": "abc123", "message": "Test"},
        ]

        # LLM 没有返回 commit_sha
        llm_response = """```json
[
  {
    "title": "测试",
    "type": "capability",
    "category": "engineering",
    "impact_score": 3,
    "why_it_matters": "测试"
  }
]
```"""

        # Act
        with patch.object(analyzer.client.messages, "create") as mock_create:
            mock_response = MagicMock()
            mock_response.content = [MagicMock(text=llm_response)]
            mock_create.return_value = mock_response

            signals = analyzer.analyze_commits(commits)

        # Assert - 应该回退到索引匹配（旧行为）
        assert len(signals) == 1
        assert signals[0].sources == ["https://github.com/test/repo/commit/abc123"]
