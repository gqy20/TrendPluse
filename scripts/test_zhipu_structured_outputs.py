#!/usr/bin/env python3
"""测试智谱 AI Anthropic 兼容端点的 structured outputs 支持

Usage:
    python scripts/test_zhipu_structured_outputs.py
"""

import os
import sys
from pathlib import Path

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


from anthropic import Anthropic
from pydantic import BaseModel

# 从环境变量获取 API Key
API_KEY = (
    os.getenv("ANTHROPIC_API_KEY")
    or os.getenv("ANTHROPIC_AUTH_KEY")
    or os.getenv("ANTHROPIC_AUTH_TOKEN")
)

# 如果仍然没有，尝试从项目配置加载
if not API_KEY:
    try:
        from trendpluse.config import Settings

        settings = Settings()
        API_KEY = settings.anthropic_api_key
        print(f"✓ 从项目配置加载 API Key: {API_KEY[:10]}...")
    except Exception:
        pass

if not API_KEY:
    print("❌ 错误: 未找到 API Key")
    print("   请设置以下环境变量之一：")
    print("   - ANTHROPIC_API_KEY")
    print("   - ANTHROPIC_AUTH_KEY")
    print("   - ANTHROPIC_AUTH_TOKEN")
    print("   或在 .env 文件中配置")
    sys.exit(1)

# 智谱 AI Anthropic 兼容端点
BASE_URL = "https://open.bigmodel.cn/api/anthropic"
MODEL = "glm-4.7"


# 定义测试用的 Pydantic 模型
class ContactInfo(BaseModel):
    """简单的联系人信息模型"""

    name: str
    email: str
    interest: str
    demo_requested: bool


class SentimentAnalysis(BaseModel):
    """情感分析模型"""

    sentiment: str
    confidence: float
    keywords: list[str]


def print_test_header(title: str):
    """打印测试标题"""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}")


def print_result(success: bool, message: str):
    """打印测试结果"""
    symbol = "✅" if success else "❌"
    print(f"{symbol} {message}")


def test_1_basic_api():
    """测试 1: 基础 Anthropic Messages API 是否可用"""
    print_test_header("测试 1: 基础 API 连通性")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "请简短回答：什么是人工智能？用一句话总结。",
                }
            ],
        )

        result = message.content[0].text
        print_result(True, f"基础 API 可用\n响应内容: {result[:100]}...")
        return True

    except Exception as e:
        print_result(False, f"基础 API 调用失败: {type(e).__name__}: {e}")
        return False


def test_2_response_format_json_object():
    """测试 2: response_format 参数（json_object）"""
    print_test_header("测试 2: response_format=json_object 参数")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": '请返回 JSON 格式：{"name": "张三", "age": 25}',
                }
            ],
            # 尝试使用 response_format
            extra_body={"response_format": {"type": "json_object"}},
        )

        result = message.content[0].text
        print_result(True, f"response_format 参数可用\n响应: {result[:100]}...")
        return True

    except Exception as e:
        print_result(False, f"response_format 参数失败: {type(e).__name__}: {e}")
        return False


def test_3_output_format_json_schema():
    """测试 3: output_format 参数（json_schema）"""
    print_test_header("测试 3: output_format=json_schema 参数")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        # 定义 JSON schema
        schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "email": {"type": "string"},
            },
            "required": ["name", "age"],
        }

        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "请提取以下信息并转换为 JSON：张三，25岁，zhangsan@example.com"
                    ),
                }
            ],
            extra_body={"output_format": {"type": "json_schema", "schema": schema}},
        )

        result = message.content[0].text
        print_result(True, f"output_format=json_schema 可用\n响应: {result[:100]}...")
        return True

    except Exception as e:
        print_result(False, f"output_format=json_schema 失败: {type(e).__name__}: {e}")
        return False


def test_4_betas_header():
    """测试 4: betas 参数"""
    print_test_header("测试 4: betas 参数")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        message = client.messages.create(
            model=MODEL,
            max_tokens=1024,
            messages=[{"role": "user", "content": "你好"}],
            # 尝试使用 betas 参数
            extra_headers={"anthropic-beta": "structured-outputs-2025-11-13"},
        )

        result = message.content[0].text
        print_result(True, f"betas header 可用\n响应: {result[:100]}...")
        return True

    except Exception as e:
        print_result(False, f"betas header 失败: {type(e).__name__}: {e}")
        return False


def test_5_beta_messages_endpoint():
    """测试 5: client.beta.messages 端点"""
    print_test_header("测试 5: client.beta.messages 端点")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        # 尝试使用 beta 端点
        message = client.beta.messages.create(
            model=MODEL,
            max_tokens=1024,
            betas=["structured-outputs-2025-11-13"],
            messages=[{"role": "user", "content": "你好，请简短回复。"}],
        )

        result = message.content[0].text
        print_result(True, f"beta.messages 端点可用\n响应: {result[:100]}...")
        return True

    except Exception as e:
        print_result(False, f"beta.messages 端点失败: {type(e).__name__}: {e}")
        # 打印详细错误信息
        import traceback

        print(f"\n详细错误:\n{traceback.format_exc()}")
        return False


def test_6_parse_with_pydantic():
    """测试 6: client.beta.messages.parse() 方法（不带 response_format）"""
    print_test_header(
        "测试 6: client.beta.messages.parse() 方法（不带 response_format）"
    )

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        # 尝试不使用 response_format 参数
        response = client.beta.messages.parse(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": (
                        "提取联系人信息到 JSON：张三，邮箱是 zhangsan@example.com"
                    ),
                }
            ],
        )

        # 检查响应
        if hasattr(response, "parsed_output"):
            result = response.parsed_output
            print_result(
                True,
                f"parse() 有 parsed_output 属性\n"
                f"类型: {type(result)}\n"
                f"内容: {str(result)[:100]}...",
            )
        else:
            result = response.content[0].text
            print_result(
                True, f"parse() 可用但无 parsed_output\n响应: {result[:100]}..."
            )
        return True

    except Exception as e:
        print_result(False, f"parse() 方法失败: {type(e).__name__}: {e}")
        return False


def test_7_parse_with_array():
    """测试 7: parse() 方法处理数组（不带 response_format）"""
    print_test_header("测试 7: parse() 方法处理数组（不带 response_format）")

    try:
        client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

        response = client.beta.messages.parse(
            model=MODEL,
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "分析这段文本的情感（返回 JSON）：今天天气真好！",
                }
            ],
        )

        # 检查响应
        if hasattr(response, "parsed_output"):
            result = response.parsed_output
            print_result(True, f"parse() 数组处理可用\n解析结果: {result}")
        else:
            result = response.content[0].text
            print_result(
                True, f"parse() 数组可用但无 parsed_output\n响应: {result[:100]}..."
            )
        return True

    except Exception as e:
        print_result(False, f"parse() 数组处理失败: {type(e).__name__}: {e}")
        return False


def main():
    """主测试函数"""
    print("\n" + "=" * 60)
    print("  智谱 AI Anthropic 兼容端点 Structured Outputs 测试")
    print(f"  端点: {BASE_URL}")
    print(f"  模型: {MODEL}")
    print("=" * 60)

    # 运行所有测试
    results = {
        "基础 API 连通性": test_1_basic_api(),
        "response_format=json_object": test_2_response_format_json_object(),
        "output_format=json_schema": test_3_output_format_json_schema(),
        "betas header": test_4_betas_header(),
        "beta.messages 端点": test_5_beta_messages_endpoint(),
        "beta.messages.parse() (不带参数)": test_6_parse_with_pydantic(),
        "parse() 数组处理 (不带参数)": test_7_parse_with_array(),
    }

    # 汇总结果
    print("\n" + "=" * 60)
    print("  测试结果汇总")
    print("=" * 60)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        symbol = "✅" if result else "❌"
        print(f"{symbol} {test_name}")

    print(f"\n通过率: {passed}/{total} ({passed / total * 100:.1f}%)")

    if passed == total:
        print("\n🎉 所有测试通过！智谱 AI 完全支持 Anthropic 的 structured outputs！")
    elif passed >= total * 0.7:
        print(
            f"\n⚠️  部分测试通过 ({passed}/{total})，智谱 AI 部分支持 structured outputs"
        )
    else:
        print("\n❌ 大部分测试失败，智谱 AI 不支持或不完全支持 structured outputs")


if __name__ == "__main__":
    main()
