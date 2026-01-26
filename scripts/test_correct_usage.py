#!/usr/bin/env python3
"""测试智谱 AI response_format 的正确使用方式"""

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
    except Exception:
        pass

BASE_URL = "https://open.bigmodel.cn/api/anthropic"
MODEL = "glm-4.7"


class ContactInfo(BaseModel):
    name: str
    email: str
    interest: str
    demo_requested: bool


def extract_json_from_response(text: str) -> str:
    """从响应中提取纯 JSON（移除 ```json 标记）"""
    text = text.strip()

    # 移除开头的 ```json
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]

    # 移除结尾的 ```
    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


print("\n" + "=" * 70)
print("  智谱 AI response_format 正确使用方式测试")
print("=" * 70)

client = Anthropic(api_key=API_KEY, base_url=BASE_URL)

# 正确的请求方式
print("\n--- 正确的请求方式 ---")
try:
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": """请按照以下 JSON Schema 返回联系人信息：
{
  "type": "object",
  "properties": {
    "name": {"type": "string"},
    "email": {"type": "string", "format": "email"},
    "interest": {"type": "string"},
    "demo_requested": {"type": "boolean"}
  },
  "required": ["name", "email", "interest", "demo_requested"]
}

请提取以下信息：
张三，邮箱是 zhangsan@example.com，对 AI 感兴趣，希望预约演示。
""",
            }
        ],
        extra_body={"response_format": {"type": "json_object"}},
    )

    text_content = response.content[0].text
    print("✅ 调用成功")
    print(f"  - 原始响应:\n{text_content}")

    # 提取纯 JSON
    json_text = extract_json_from_response(text_content)
    print(f"\n  - 提取后的 JSON:\n{json_text}")

    # 解析为字典
    data = json.loads(json_text)
    print(f"\n  - 解析后的字典:\n{data}")

    # 验证为 Pydantic 模型
    try:
        contact = ContactInfo(**data)
        print("\n✅ Pydantic 验证成功！")
        print(f"   - name: {contact.name}")
        print(f"   - email: {contact.email}")
        print(f"   - interest: {contact.interest}")
        print(f"   - demo_requested: {contact.demo_requested}")
    except ValidationError as ve:
        print("\n❌ Pydantic 验证失败:")
        print(f"   {ve}")

except Exception as e:
    print(f"\n❌ 测试失败: {type(e).__name__}: {e}")
    import traceback

    traceback.print_exc()

print("\n" + "=" * 70)
print("  关键发现")
print("=" * 70)
print("""
1. 智谱 AI 的 response_format 会返回 ```json 包裹的内容
   需要手动移除 ```json 标记

2. response_format 不是强制的
   模型可能不遵循 schema，需要在应用层验证

3. 没有自动的 Pydantic 对象转换
   - Anthropic 的 parse() 方法：response_format=Model → 自动解析
   - 智谱 AI：需要手动 json.loads() + Pydantic 验证

4. 正确的使用流程：
   a) 使用 extra_body 传入 response_format
   b) 从响应中提取 JSON（移除 ```json 标记）
   c) 使用 json.loads() 解析
   d) 使用 Pydantic 模型验证

5. 这与 Anthropic 官方方案的对比：
   Anthropic: API 层 constrained decoding → 自动解析 → 强制验证
   智谱 AI: Prompt 引导 → 手动解析 → 手动验证
""")
