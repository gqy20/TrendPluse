#!/usr/bin/env python3
"""测试使用 extra_body 传入 response_format 的实际效果"""

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


from anthropic import Anthropic
from pydantic import BaseModel, ValidationError

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
    except:
        pass

BASE_URL = "https://open.bigmodel.cn/api/anthropic"
MODEL = "glm-4.7"


class ContactInfo(BaseModel):
    """测试模型"""

    name: str
    email: str
    interest: str
    demo_requested: bool


print("\n" + "=" * 70)
print("  测试: 使用 extra_body 传入 response_format")
print("=" * 70)

client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "interest": {"type": "string"},
        "demo_requested": {"type": "boolean"},
    },
    "required": ["name", "email", "interest", "demo_requested"],
}

# 测试 1: 使用 extra_body 传入 response_format
print("\n--- 测试 1: response_format 通过 extra_body 传入 ---")
try:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "提取联系人信息到 JSON：张三，邮箱 zhangsan@example.com，对 AI 感兴趣",
            }
        ],
        extra_body={"response_format": {"type": "json_schema", "schema": schema}},
    )

    text_content = response.content[0].text
    print("✅ 调用成功")
    print(f"  - 响应长度: {len(text_content)} 字符")
    print(f"  - 响应内容:\n{text_content}")

    # 尝试解析为 JSON
    try:
        parsed = json.loads(text_content)
        print(f"  - JSON 解析成功: {parsed}")

        # 尝试验证为 Pydantic 模型
        try:
            contact = ContactInfo(**parsed)
            print(f"  ✓ Pydantic 验证成功: {contact}")
        except ValidationError as ve:
            print(f"  ❌ Pydantic 验证失败: {ve}")
            print(
                "     原因: JSON 响应没有遵循 schema（智谱 AI 只保证 JSON 格式，不保证 schema）"
            )

    except json.JSONDecodeError as je:
        print(f"  ❌ JSON 解析失败: {je}")

except Exception as e:
    print(f"❌ 调用失败: {type(e).__name__}: {e}")
    import traceback

    traceback.print_exc()

# 测试 2: 检查智谱 AI 是否真的强制 schema
print("\n--- 测试 2: 检查是否强制 schema（故意发送错误格式）---")
try:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "返回以下数据（故意不遵循 schema）：张三"}
        ],
        extra_body={"response_format": {"type": "json_schema", "schema": schema}},
    )

    text_content = response.content[0].text
    print("✅ 调用成功")
    print(f"  - 响应内容:\n{text_content}")

    # 尝试验证
    try:
        parsed = json.loads(text_content)
        ContactInfo(**parsed)  # 应该失败
        print("  ⚠️ 意外：Pydantic 验证成功（智谱 AI 强制了 schema？）")
    except ValidationError as ve:
        print(f"  ✓ 预期的验证失败（智谱 AI 没有强制 schema）: {ve}")
    except json.JSONDecodeError as je:
        print(f"  - JSON 解析失败: {je}")

except Exception as e:
    print(f"❌ 调用失败: {type(e).__name__}: {e}")

# 测试 3: 测试 response_format=json_object
print("\n--- 测试 3: response_format=json_object（简化的 JSON 模式）---")
try:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {"role": "user", "content": '返回 JSON: {"name": "赵六", "age": 30}'}
        ],
        extra_body={"response_format": {"type": "json_object"}},
    )

    text_content = response.content[0].text
    print("✅ 调用成功")
    print(f"  - 响应内容:\n{text_content}")

except Exception as e:
    print(f"❌ 调用失败: {e}")

print("\n" + "=" * 70)
print("  最终结论")
print("=" * 70)
print("""
智谱 AI 的 Structured Outputs 实际表现：

1. ✅ API 层面支持 response_format 参数（通过 extra_body）
   - response_format={"type": "json_object"} 简单 JSON 模式
   - response_format={"type": "json_schema", "schema": ...} Schema 模式

2. ❌ 不是强制的 schema 验证
   - 模型可能会返回不符合 schema 的 JSON
   - 需要在应用层使用 Pydantic 验证

3. ⚠️ beta.messages.parse() 方法
   - 不支持 response_format 参数
   - 没有自动解析 Pydantic 对象的功能
   - 只是普通的 API 调用包装

4. 与 Anthropic 官方方案的区别
   - Anthropic: constrained decoding（API 层强制）+ SDK 自动验证
   - 智谱 AI: prompt 引导（模型层尝试）+ 需要手动验证

建议：
   使用智谱 AI 的 response_format 时，必须在应用层添加 Pydantic 验证
""")
