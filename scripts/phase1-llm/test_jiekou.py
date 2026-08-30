"""测试 jiekou.vip Claude API Key 是否可用"""

# 知识点: 中转平台 | OpenAI 兼容格式 | .env 读取 Key | 连通性验证脚本
import os

import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("JIEKOU_API_KEY")
BASE_URL = os.getenv("JIEKOU_BASE_URL", "https://api.highwayapi.ai/openai/v1")

urls = [
    f"{BASE_URL}/chat/completions",
]

for url in urls:
    try:
        r = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "max_tokens": 50,
                "messages": [{"role": "user", "content": "say hi in 3 words"}],
            },
            timeout=15,
        )
        print(f"{url}")
        print(f"  status: {r.status_code}")
        if r.status_code == 200:
            content = r.json()["choices"][0]["message"]["content"]
            print(f"  ✅ SUCCESS: {content}")
            break
        else:
            print(f"  ❌ {r.text[:200]}")
    except Exception as e:  # noqa: BLE001
        print(f"{url}")
        print(f"  ❌ {e}")
