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

    class _AnthropicStub:
        def __init__(self, *args, **kwargs):
            self.messages = _MessagesStub()

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
