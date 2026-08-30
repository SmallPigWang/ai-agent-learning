"""抓取 DeepSeek 和 Claude 的原始 JSON 返回结构"""

# 知识点: OpenAI 兼容返回骨架 id/object/model/choices/usage | DeepSeek reasoning_content | 诊断类脚本
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
dk = os.getenv("DEEPSEEK_API_KEY")
ck = os.getenv("JIEKOU_API_KEY")
cb = os.getenv("JIEKOU_BASE_URL", "https://api.highwayapi.ai/openai/v1")
prompt = "1+1=?"

print("=" * 60)
print("=== DeepSeek 完整 JSON 返回 ===")
print("=" * 60)
r = requests.post(
    "https://api.deepseek.com/chat/completions",
    headers={"Authorization": f"Bearer {dk}", "Content-Type": "application/json"},
    json={
        "model": "deepseek-v4-flash",
        "max_tokens": 100,
        "messages": [{"role": "user", "content": prompt}],
    },
)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))

print("\n" + "=" * 60)
print("=== Claude (via jiekou) 完整 JSON 返回 ===")
print("=" * 60)
r = requests.post(
    f"{cb}/chat/completions",
    headers={"Authorization": f"Bearer {ck}", "Content-Type": "application/json"},
    json={
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 100,
        "messages": [{"role": "user", "content": prompt}],
    },
)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))
