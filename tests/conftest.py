"""Pytest 配置。

确保 src layout 在测试运行时可被导入。
"""

from __future__ import annotations

import sys
from pathlib import Path
from types import ModuleType


def _ensure_src_on_path() -> None:
    root = Path(__file__).resolve().parents[1]
    src_path = root / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


_ensure_src_on_path()


def _ensure_github_stub() -> None:
    if "github" in sys.modules:
        return
    stub = ModuleType("github")
    stub.Auth = object  # type: ignore[attr-defined]
    stub.Github = object  # type: ignore[attr-defined]
    stub.GithubException = Exception  # type: ignore[attr-defined]
    sys.modules["github"] = stub


_ensure_github_stub()


def _ensure_gql_stub() -> None:
    if "gql" in sys.modules:
        return

    def _gql_stub(*_args, **_kwargs):
        return None

    stub = ModuleType("gql")
    stub.Client = object  # type: ignore[attr-defined]
    stub.gql = _gql_stub  # type: ignore[attr-defined]
    sys.modules["gql"] = stub

    transport_stub = ModuleType("gql.transport")
    requests_stub = ModuleType("gql.transport.requests")
    requests_stub.RequestsHTTPTransport = object  # type: ignore[attr-defined]
    sys.modules["gql.transport"] = transport_stub
    sys.modules["gql.transport.requests"] = requests_stub


_ensure_gql_stub()


def _ensure_instructor_stub() -> None:
    if "instructor" in sys.modules:
        return

    class _InstructorStub:
        def __init__(self, *args, **kwargs):
            pass

    def _from_anthropic(_client):
        return _InstructorStub()

    stub = ModuleType("instructor")
    stub.Instructor = _InstructorStub  # type: ignore[attr-defined]
    stub.from_anthropic = _from_anthropic  # type: ignore[attr-defined]
    sys.modules["instructor"] = stub


_ensure_instructor_stub()


def _ensure_anthropic_stub() -> None:
    if "anthropic" in sys.modules:
        return

    class _AnthropicStub:
        def __init__(self, *args, **kwargs):
            pass

    stub = ModuleType("anthropic")
    stub.Anthropic = _AnthropicStub  # type: ignore[attr-defined]
    stub.APITimeoutError = type("APITimeoutError", (Exception,), {})  # type: ignore[attr-defined]
    stub.RateLimitError = type("RateLimitError", (Exception,), {})  # type: ignore[attr-defined]
    stub.APIConnectionError = type("APIConnectionError", (Exception,), {})  # type: ignore[attr-defined]
    stub.InternalServerError = type("InternalServerError", (Exception,), {})  # type: ignore[attr-defined]
    sys.modules["anthropic"] = stub

    types_stub = ModuleType("anthropic.types")
    types_stub.TextBlock = object  # type: ignore[attr-defined]
    sys.modules["anthropic.types"] = types_stub


_ensure_anthropic_stub()


def _ensure_tenacity_stub() -> None:
    if "tenacity" in sys.modules:
        return

    def _identity(func=None, **_kwargs):
        if func is None:
            return lambda f: f
        return func

    stub = ModuleType("tenacity")
    stub.retry = _identity  # type: ignore[attr-defined]
    stub.stop_after_attempt = lambda *_a, **_k: None  # type: ignore[attr-defined]
    stub.wait_exponential = lambda *_a, **_k: None  # type: ignore[attr-defined]
    stub.retry_if_exception_type = lambda *_a, **_k: None  # type: ignore[attr-defined]
    sys.modules["tenacity"] = stub


_ensure_tenacity_stub()
