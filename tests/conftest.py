"""Pytest 配置。

确保 src layout 在测试运行时可被导入。
仅在依赖缺失时注入轻量 stub，避免覆盖真实依赖。
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import UTC, datetime
from functools import wraps
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any
from unittest.mock import Mock

import pytest


def _ensure_src_on_path() -> None:
    root = Path(__file__).resolve().parents[1]
    src_path = root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


_ensure_src_on_path()


@pytest.fixture
def temp_dir(tmp_path: Path) -> Path:
    return tmp_path


@pytest.fixture
def temp_file(tmp_path: Path) -> Path:
    return tmp_path / "weekly-2026-W05.md"


@pytest.fixture
def mock_github(monkeypatch: pytest.MonkeyPatch):
    class _MockGithubHelper:
        def __init__(self):
            self.mock_repo = Mock()
            self.mock_client = Mock()
            self.mock_client.get_repo.return_value = self.mock_repo

        def mock_repo_issues(self, issues):
            self.mock_repo.get_issues.return_value = issues

        def create_issue(
            self,
            number: int = 1,
            title: str = "Issue",
            body: str = "",
            state: str = "open",
            created_at=None,
            updated_at=None,
            closed_at=None,
            comments: int = 0,
            labels=None,
            url: str | None = None,
            user_login: str = "test_user",
        ):
            created_at = created_at or datetime.now(UTC)
            updated_at = updated_at or created_at
            url = url or f"https://github.com/owner/repo/issues/{number}"
            label_objs = []
            if labels:
                for label in labels:
                    if hasattr(label, "name"):
                        label_objs.append(label)
                    else:
                        label_objs.append(SimpleNamespace(name=str(label)))

            issue = SimpleNamespace(
                number=number,
                title=title,
                body=body,
                state=state,
                created_at=created_at,
                updated_at=updated_at,
                closed_at=closed_at,
                comments=comments,
                labels=label_objs,
                html_url=url,
                user=SimpleNamespace(login=user_login),
                pull_request=None,
            )
            return issue

    helper = _MockGithubHelper()

    import trendpluse.collectors.base as base

    monkeypatch.setattr(base, "Github", lambda *args, **kwargs: helper.mock_client)
    return helper


@pytest.fixture
def mock_env_vars(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test_key")
    monkeypatch.setenv("GITHUB_TOKEN", "test_token")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", "https://api.test.com")
    monkeypatch.setenv("ANTHROPIC_MODEL", "test-model")
    return True


def _maybe_stub(module_name: str, builder):
    if importlib.util.find_spec(module_name) is None:
        sys.modules[module_name] = builder()
        return True
    return False


# PyGithub


def _build_github_stub() -> ModuleType:
    stub = ModuleType("github")

    class GithubException(Exception):  # noqa: N818
        def __init__(self, status=None, data=None, headers=None):
            super().__init__(status, data, headers)
            self.status = status
            self.data = data
            self.headers = headers

    class RateLimitExceededException(GithubException):
        pass

    class _AuthStub:
        class Token:
            def __init__(self, *args, **kwargs):
                pass

    stub.Auth = _AuthStub  # type: ignore[attr-defined]

    class _GithubStub:
        def __init__(self, *args, **kwargs):
            pass

    stub.Github = _GithubStub  # type: ignore[attr-defined]
    stub.GithubException = GithubException  # type: ignore[attr-defined]
    stub.RateLimitExceededException = RateLimitExceededException  # type: ignore[attr-defined]

    github_exception_module = ModuleType("github.GithubException")
    github_exception_module.GithubException = GithubException  # type: ignore[attr-defined]
    github_exception_module.RateLimitExceededException = RateLimitExceededException  # type: ignore[attr-defined]
    sys.modules["github.GithubException"] = github_exception_module
    return stub


_maybe_stub("github", _build_github_stub)


# gql


def _build_gql_stub() -> ModuleType:
    stub = ModuleType("gql")

    class _GraphQLRequest:
        def __init__(self, query: str):
            self.query = query

        def __str__(self):
            return self.query

    def _gql_stub(query: str, *_args, **_kwargs):
        return _GraphQLRequest(query)

    class _ClientStub:
        def __init__(self, *args, **kwargs):
            self.transport = kwargs.get("transport")

        def execute(self, *_args, **_kwargs):
            return {}

    stub.Client = _ClientStub  # type: ignore[attr-defined]
    stub.gql = _gql_stub  # type: ignore[attr-defined]

    transport_stub = ModuleType("gql.transport")
    requests_stub = ModuleType("gql.transport.requests")

    class _RequestsHTTPTransport:
        def __init__(self, *args, **kwargs):
            pass

    requests_stub.RequestsHTTPTransport = _RequestsHTTPTransport  # type: ignore[attr-defined]
    sys.modules["gql.transport"] = transport_stub
    sys.modules["gql.transport.requests"] = requests_stub
    return stub


_maybe_stub("gql", _build_gql_stub)


# instructor


def _build_instructor_stub() -> ModuleType:
    stub = ModuleType("instructor")

    class _CompletionsStub:
        def create(self, *args, **kwargs):
            response_model = kwargs.get("response_model")
            if response_model is None:
                return None
            model_name = getattr(response_model, "__name__", "")
            if model_name == "ReleaseSummary":
                return response_model(
                    change_type="other",
                    key_changes=[],
                    summary_cn="模拟总结",
                    impact_level=1,
                )
            if model_name == "ProjectHighlight":
                return response_model(
                    recommendation_reason="模拟推荐理由",
                    technical_highlights=["模拟亮点"],
                    use_cases=["模拟场景"],
                )
            # 尝试为常见字段提供默认值
            try:
                fields = getattr(response_model, "model_fields", {})
                payload: dict[str, object] = {}
                for name, field in fields.items():
                    annotation = getattr(field, "annotation", None)
                    if annotation in (str,):
                        payload[name] = "模拟值"
                    elif annotation in (int,):
                        payload[name] = 1
                    elif annotation in (bool,):
                        payload[name] = False
                    elif annotation in (list[str], list):
                        payload[name] = []
                    else:
                        payload[name] = None
                return response_model(**payload)
            except Exception:
                return None

    class _ChatStub:
        def __init__(self):
            self.completions = _CompletionsStub()

    class _InstructorStub:
        def __init__(self, *args, **kwargs):
            self.chat = _ChatStub()

    def _from_anthropic(_client):
        return _InstructorStub()

    stub.Instructor = _InstructorStub  # type: ignore[attr-defined]
    stub.from_anthropic = _from_anthropic  # type: ignore[attr-defined]
    return stub


_maybe_stub("instructor", _build_instructor_stub)


# anthropic


def _build_anthropic_stub() -> ModuleType:
    stub = ModuleType("anthropic")

    class _MessagesStub:
        def create(self, *args, **kwargs):
            return None

    class _AsyncMessagesStub:
        async def create(self, *args, **kwargs):
            return None

    class _AnthropicStub:
        def __init__(self, *args, **kwargs):
            self.messages = _MessagesStub()

    class _AsyncAnthropicStub:
        def __init__(self, *args, **kwargs):
            self.messages = _AsyncMessagesStub()

    class APITimeoutError(Exception):
        pass

    class RateLimitError(Exception):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.response = kwargs.get("response")
            self.body = kwargs.get("body")

    class APIConnectionError(Exception):
        pass

    class InternalServerError(Exception):
        pass

    class AuthenticationError(Exception):
        pass

    stub.Anthropic = _AnthropicStub  # type: ignore[attr-defined]
    stub.AsyncAnthropic = _AsyncAnthropicStub  # type: ignore[attr-defined]
    stub.APITimeoutError = APITimeoutError  # type: ignore[attr-defined]
    stub.RateLimitError = RateLimitError  # type: ignore[attr-defined]
    stub.APIConnectionError = APIConnectionError  # type: ignore[attr-defined]
    stub.InternalServerError = InternalServerError  # type: ignore[attr-defined]
    stub.AuthenticationError = AuthenticationError  # type: ignore[attr-defined]

    types_stub = ModuleType("anthropic.types")

    class TextBlock:
        def __init__(self, text: str):
            self.text = text

    types_stub.TextBlock = TextBlock  # type: ignore[attr-defined]
    sys.modules["anthropic.types"] = types_stub
    return stub


_maybe_stub("anthropic", _build_anthropic_stub)


# tenacity


def _build_tenacity_stub() -> ModuleType:
    stub = ModuleType("tenacity")

    class _StopAfterAttempt:
        def __init__(self, max_attempts: int):
            self.max_attempts = max_attempts

    class _RetryIfExceptionType:
        def __init__(self, exc_types):
            self.exc_types = exc_types

        def __call__(self, exc: Exception) -> bool:
            return isinstance(exc, self.exc_types)

    def retry(
        stop=None,
        wait=None,
        retry=None,
        reraise: bool = False,
    ):
        def decorator(func):
            def wrapper(*args, **kwargs):
                attempts = getattr(stop, "max_attempts", 1)
                for attempt in range(1, attempts + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as exc:
                        should_retry = True
                        if retry is not None:
                            should_retry = retry(exc)
                        if not should_retry or attempt >= attempts:
                            if reraise:
                                raise
                            return None
                return None

            return wrapper

        return decorator

    stub.retry = retry  # type: ignore[attr-defined]
    stub.stop_after_attempt = _StopAfterAttempt  # type: ignore[attr-defined]
    stub.wait_exponential = lambda *_a, **_k: None  # type: ignore[attr-defined]
    stub.retry_if_exception_type = _RetryIfExceptionType  # type: ignore[attr-defined]
    return stub


_maybe_stub("tenacity", _build_tenacity_stub)


# freezegun


def _build_freezegun_stub() -> ModuleType:
    stub = ModuleType("freezegun")

    class _FreezeTime:
        def __init__(self, *_args, **_kwargs):
            pass

        def __enter__(self):
            return self

        def __exit__(self, *_exc):
            return False

        def __call__(self, func):
            @wraps(func)
            def _wrapped(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapped

    def _freeze_time(*_args, **_kwargs):
        return _FreezeTime()

    stub.freeze_time = _freeze_time  # type: ignore[attr-defined]
    return stub


_maybe_stub("freezegun", _build_freezegun_stub)


# claude_agent_sdk


def _build_claude_agent_sdk_stub() -> ModuleType:
    stub = ModuleType("claude_agent_sdk")

    # ResultMessage mock
    class ResultMessage:
        def __init__(
            self,
            session_id: str = "test-session",
            structured_output: Any = None,
            result: str | None = None,
            num_turns: int = 1,
            duration_ms: int = 1000,
            duration_api_ms: int = 500,
            total_cost_usd: float = 0.01,
            usage: dict | None = None,
        ):
            self.session_id = session_id
            self.structured_output = structured_output
            self.result = result
            self.num_turns = num_turns
            self.duration_ms = duration_ms
            self.duration_api_ms = duration_api_ms
            self.total_cost_usd = total_cost_usd
            self.usage = usage or {"input_tokens": 100, "output_tokens": 50}

    # AssistantMessage mock
    class AssistantMessage:
        def __init__(self, content: Any = None):
            self.content = content or []

    # TextBlock mock
    class TextBlock:
        def __init__(self, text: str = ""):
            self.text = text

    # ClaudeAgentOptions mock
    class ClaudeAgentOptions:
        def __init__(
            self,
            model: str | None = None,
            allowed_tools: list | None = None,
            output_format: dict | None = None,
            max_turns: int = 50,
            max_budget_usd: float = 10.0,
            stderr: Any = None,
        ):
            self.model = model
            self.allowed_tools = allowed_tools
            self.output_format = output_format
            self.max_turns = max_turns
            self.max_budget_usd = max_budget_usd
            self.stderr = stderr

    # ClaudeSDKError
    class ClaudeSDKError(Exception):
        pass

    # query async generator
    async def _query_generator(prompt: str, options: ClaudeAgentOptions):
        yield ResultMessage(
            session_id="test-session",
            structured_output=None,
            result='{"summary_brief": "测试摘要"}',
        )

    # 存储最后一次调用参数
    _last_query_call: dict = {}

    class _QueryStub:
        def __init__(self):
            self._structured_output = None
            self._result = None

        def set_response(
            self,
            structured_output: Any = None,
            result: str | None = None,
        ):
            self._structured_output = structured_output
            self._result = result

        async def __call__(self, prompt: str, options: ClaudeAgentOptions):
            _last_query_call["prompt"] = prompt
            _last_query_call["options"] = options
            if self._structured_output is not None:
                yield ResultMessage(
                    session_id="test-session",
                    structured_output=self._structured_output,
                    result=self._result,
                )
            elif self._result is not None:
                yield ResultMessage(
                    session_id="test-session",
                    structured_output=None,
                    result=self._result,
                )
            else:
                yield ResultMessage(
                    session_id="test-session",
                    structured_output=None,
                    result=None,
                )

    query = _QueryStub()
    stub.query = query  # type: ignore[attr-defined]
    stub.ResultMessage = ResultMessage  # type: ignore[attr-defined]
    stub.AssistantMessage = AssistantMessage  # type: ignore[attr-defined]
    stub.TextBlock = TextBlock  # type: ignore[attr-defined]
    stub.ClaudeAgentOptions = ClaudeAgentOptions  # type: ignore[attr-defined]
    stub.ClaudeSDKError = ClaudeSDKError  # type: ignore[attr-defined]
    stub.ClaudeSDKClient = Mock  # type: ignore[attr-defined]

    return stub


_maybe_stub("claude_agent_sdk", _build_claude_agent_sdk_stub)


# ============ 配置隔离：让测试不受本机 .env 与 shell 环境变量影响 ============

# `Settings` 通过 pydantic-settings 读取 `.env`（仓库根目录），且
# `load_alternative_api_key` / `monitored_repo_configs` 会直接读 os.environ。
# 开发者本机的 `.env`（含真实密钥）与 shell 里残留的 ANTHROPIC_* 变量
# 会静默污染配置类断言，因此这里统一在每个测试前隔离。
_EXTRA_ENV_NAMES = frozenset(
    {
        # config.py 中的备选 API Key 读取路径
        "ANTHROPIC_AUTH_KEY",
        "ANTHROPIC_AUTH_TOKEN",
        # github_token 的别名链
        "PAT_TOKEN",
        "GITHUB_PAT",
    }
)


def _collect_settings_env_names() -> frozenset[str]:
    """收集 Settings 所有字段对应的环境变量名（含 validation_alias）。"""
    from pydantic import AliasChoices, AliasPath

    from trendpluse.config import Settings

    names: set[str] = set(_EXTRA_ENV_NAMES)
    for field_name, field_info in Settings.model_fields.items():
        names.add(field_name.upper())
        alias = field_info.validation_alias
        if isinstance(alias, str):
            names.add(alias)
        elif isinstance(alias, AliasChoices):
            for choice in alias.choices:
                if isinstance(choice, str):
                    names.add(choice)
                elif isinstance(choice, AliasPath):  # pragma: no cover
                    continue
    return frozenset(names)


@pytest.fixture(autouse=True)
def isolate_settings_env(monkeypatch: pytest.MonkeyPatch) -> None:
    """禁用 .env 文件源并清理相关环境变量，保证配置测试可重复。

    测试内部若需要特定取值，仍可用 `monkeypatch.setenv(...)` 显式设置，
    本 fixture 会先于测试体执行，不会覆盖测试自身的设置。
    """
    from trendpluse.config import Settings

    monkeypatch.setitem(Settings.model_config, "env_file", None)
    for name in _collect_settings_env_names():
        monkeypatch.delenv(name, raising=False)


# ============ 输出目录隔离：把测试模块的 _OUTPUT_DIR 指向 tmp_path ============

# 约定：测试模块若定义模块级 `_OUTPUT_DIR`，本 fixture 会在每个用例前把它
# 重定向到 tmp_path，从而避免 mock settings 里写死的 "reports/daily"
# 把测试产物落盘到仓库内（配合下方的会话级守卫使用）。


@pytest.fixture(autouse=True)
def isolate_module_output_dir(
    request: pytest.FixtureRequest,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """把测试模块的 `_OUTPUT_DIR` 重定向到临时目录。"""
    module = request.module
    if module is not None and hasattr(module, "_OUTPUT_DIR"):
        monkeypatch.setattr(
            module,
            "_OUTPUT_DIR",
            str(tmp_path / "reports" / "daily"),
        )


# ============ 产物守卫：单测不得写入仓库内 reports/ 与 data/ ============

# 历史问题：部分用例把 mock settings 的 output_dir 写成仓库真实路径
# "reports/daily"，ReportPublisher._save_json 会覆盖已跟踪的
# report-*.json（并洗掉末尾换行符），导致每次跑测试都产生脏 diff。
# 这里加一道会话级守卫：只要有测试改动这两个目录，就在收尾时直接失败。
_GUARDED_ARTIFACT_DIRS = ("reports", "data")


def _snapshot_artifacts() -> dict[str, tuple[int, int]]:
    """记录守卫目录下所有文件的大小与 mtime。"""
    root = Path(__file__).resolve().parents[1]
    snapshot: dict[str, tuple[int, int]] = {}
    for relative_dir in _GUARDED_ARTIFACT_DIRS:
        base = root / relative_dir
        if not base.is_dir():
            continue
        for path in base.rglob("*"):
            if not path.is_file():
                continue
            stat = path.stat()
            snapshot[str(path.relative_to(root))] = (stat.st_size, stat.st_mtime_ns)
    return snapshot


@pytest.fixture(autouse=True, scope="session")
def guard_repo_artifacts():
    """会话级守卫：确保测试跑完后仓库产物目录未被改动。"""
    before = _snapshot_artifacts()
    yield
    after = _snapshot_artifacts()

    changed = sorted(
        name for name in before.keys() & after.keys() if before[name] != after[name]
    )
    added = sorted(after.keys() - before.keys())
    removed = sorted(before.keys() - after.keys())

    problems: list[str] = []
    if changed:
        problems.append(f"被修改 {len(changed)} 个: {changed[:5]}")
    if added:
        problems.append(f"被新增 {len(added)} 个: {added[:5]}")
    if removed:
        problems.append(f"被删除 {len(removed)} 个: {removed[:5]}")

    assert not problems, (
        "单元测试污染了仓库产物目录（reports/ 或 data/）。"
        "请把测试用的 output_dir / snapshot_dir / issue_dump_dir 指向 tmp_path，"
        "不要写死仓库相对路径。\n  " + "\n  ".join(problems)
    )
