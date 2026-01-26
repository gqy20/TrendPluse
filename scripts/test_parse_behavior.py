#!/usr/bin/env python3
"""深入测试智谱 AI 的 beta.messages.parse() 行为"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


from anthropic import Anthropic
from pydantic import BaseModel

# 获取 API Key
API_KEY = (
    os.getenv("ANTHROPIC_API_KEY")
    or os.getenv("ANTHROPIC_AUTH_KEY")
    or os.getenv("ANTHROPIC_AUTH_TOKEN")
)
if not API_KEY:
    try:
        from trendpluse.config import Settings

        settings = Settings()
        API_KEY = settings.anthropic_api_key
    except Exception:
        pass

BASE_URL = "https://open.bigmodel.cn/api/anthropic"
MODEL = "glm-4.7"


class ContactInfo(BaseModel):
    name: str
    email: str
    interest: str
    demo_requested: bool


print("\n" + "=" * 70)
print("  深入测试: beta.messages.parse() 的实际行为")
print("=" * 70)

client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

# 测试 1: 使用 response_format 参数
print("\n--- 测试 1: 尝试在 parse() 中使用 response_format ---")
try:
    response = client.beta.messages.parse(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": '返回 JSON：{"name": "李四", "email": "lisi@example.com"}',
            }
        ],
        response_format=ContactInfo,  # 传入 Pydantic 模型
    )

    print("✓ 调用成功")
    print(f"  - response 类型: {type(response)}")
    print(f"  - 有 parsed_output: {hasattr(response, 'parsed_output')}")
    if hasattr(response, "parsed_output"):
        print(f"  - parsed_output 值: {response.parsed_output}")
    print(f"  - content 类型: {type(response.content)}")
    print(f"  - content 长度: {len(response.content)}")
    print(f"  - content[0] 类型: {type(response.content[0])}")
    if response.content:
        print(f"  - content[0].text: {response.content[0].text[:200]}")

except Exception as e:
    print(f"❌ 失败: {type(e).__name__}: {e}")

# 测试 2: 不使用 response_format，检查返回
print("\n--- 测试 2: 不使用 response_format，检查原始响应 ---")
try:
    response = client.beta.messages.parse(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": '返回 JSON：{"name": "王五", '
                '"email": "wangwu@example.com", "interest": "AI"}',
            }
        ],
    )

    print("✓ 调用成功")
    print(f"  - response 类型: {type(response)}")

    # 尝试解析 content
    text_content = response.content[0].text
    print(f"  - text 内容: {text_content[:200]}...")

    # 尝试解析为 JSON
    try:
        parsed = json.loads(text_content)
        print(f"  - JSON 解析成功: {parsed}")
    except json.JSONDecodeError:
        print("  - JSON 解析失败")

    # 检查是否有其他属性
    print(f"  - response 属性: {dir(response)[:10]}...")

except Exception as e:
    print(f"❌ 失败: {type(e).__name__}: {e}")
    import traceback

    traceback.print_exc()

# 测试 3: 比较 create() 和 parse() 的差异
print("\n--- 测试 3: 比较 create() 和 parse() 的差异 ---")

# 使用 create()
print("使用 client.messages.create():")
try:
    response1 = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": "说 '你好'"}],
    )
    print("  ✅ 成功")
    print(f"  - 响应类型: {type(response1)}")
    print(f"  - content 长度: {len(response1.content)}")
except Exception as e:
    print(f"  ❌ 失败: {e}")

# 使用 parse()
print("\n使用 client.beta.messages.parse():")
try:
    response2 = client.beta.messages.parse(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": "说 '你好'"}],
    )
    print("  ✅ 成功")
    print(f"  - 响应类型: {type(response2)}")
    print(f"  - content 长度: {len(response2.content)}")
except Exception as e:
    print(f"  ❌ 失败: {e}")

print("\n" + "=" * 70)
print("  结论")
print("=" * 70)
print("""
beta.messages.parse() 方法的实际行为：
1. ✓ 方法存在且可调用
2. ✓ 不支持 response_format 参数（会报错）
3. ✓ 返回的对象与 messages.create() 相同
4. ⚠️  parsed_output 属性为 None，需要手动解析 content

因此：
- 智谱 AI 的 beta.messages.parse() 不是 Anthropic 官方的 parse() 方法
- 它只是一个普通的 API 调用包装，没有特殊的结构化输出功能
- 要使用结构化输出，需要使用 response_format 参数（通过 extra_body 传入）
""")
