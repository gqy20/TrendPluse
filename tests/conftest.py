"""Pytest 配置。

确保 src layout 在测试运行时可被导入。
仅在依赖缺失时注入轻量 stub，避免覆盖真实依赖。
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _ensure_src_on_path() -> None:
    root = Path(__file__).resolve().parents[1]
    src_path = root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


_ensure_src_on_path()


def _maybe_stub(module_name: str, builder):
    if importlib.util.find_spec(module_name) is None:
        sys.modules[module_name] = builder()
        return True
    return False


# PyGithub


def _build_github_stub() -> ModuleType:
    stub = ModuleType("github")

    class _AuthStub:
        class Token:
            def __init__(self, *args, **kwargs):
                pass

    stub.Auth = _AuthStub  # type: ignore[attr-defined]

    class _GithubStub:
        def __init__(self, *args, **kwargs):
            pass

    stub.Github = _GithubStub  # type: ignore[attr-defined]
    stub.GithubException = Exception  # type: ignore[attr-defined]
    return stub


_maybe_stub("github", _build_github_stub)


# gql


def _build_gql_stub() -> ModuleType:
    stub = ModuleType("gql")

    def _gql_stub(*_args, **_kwargs):
        return None

    stub.Client = object  # type: ignore[attr-defined]
    stub.gql = _gql_stub  # type: ignore[attr-defined]

    transport_stub = ModuleType("gql.transport")
    requests_stub = ModuleType("gql.transport.requests")
    requests_stub.RequestsHTTPTransport = object  # type: ignore[attr-defined]
    sys.modules["gql.transport"] = transport_stub
    sys.modules["gql.transport.requests"] = requests_stub
    return stub


_maybe_stub("gql", _build_gql_stub)


# instructor


def _build_instructor_stub() -> ModuleType:
    stub = ModuleType("instructor")

    class _InstructorStub:
        def __init__(self, *args, **kwargs):
            self.chat = object()

    def _from_anthropic(_client):
        return _InstructorStub()

    stub.Instructor = _InstructorStub  # type: ignore[attr-defined]
    stub.from_anthropic = _from_anthropic  # type: ignore[attr-defined]
    return stub


_maybe_stub("instructor", _build_instructor_stub)


# anthropic


def _build_anthropic_stub() -> ModuleType:
    stub = ModuleType("anthropic")

    class _AnthropicStub:
        def __init__(self, *args, **kwargs):
            pass

    stub.Anthropic = _AnthropicStub  # type: ignore[attr-defined]
    stub.APITimeoutError = type("APITimeoutError", (Exception,), {})  # type: ignore[attr-defined]
    stub.RateLimitError = type("RateLimitError", (Exception,), {})  # type: ignore[attr-defined]
    stub.APIConnectionError = type("APIConnectionError", (Exception,), {})  # type: ignore[attr-defined]
    stub.InternalServerError = type("InternalServerError", (Exception,), {})  # type: ignore[attr-defined]

    types_stub = ModuleType("anthropic.types")
    types_stub.TextBlock = object  # type: ignore[attr-defined]
    sys.modules["anthropic.types"] = types_stub
    return stub


_maybe_stub("anthropic", _build_anthropic_stub)


# tenacity


def _build_tenacity_stub() -> ModuleType:
    stub = ModuleType("tenacity")

    def _identity(func=None, **_kwargs):
        if func is None:
            return lambda f: f
        return func

    stub.retry = _identity  # type: ignore[attr-defined]
    stub.stop_after_attempt = lambda *_a, **_k: None  # type: ignore[attr-defined]
    stub.wait_exponential = lambda *_a, **_k: None  # type: ignore[attr-defined]
    stub.retry_if_exception_type = lambda *_a, **_k: None  # type: ignore[attr-defined]
    return stub


_maybe_stub("tenacity", _build_tenacity_stub)
