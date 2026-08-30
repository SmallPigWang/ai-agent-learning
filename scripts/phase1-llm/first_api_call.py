# ============================================================
# 练习: 第一次 API 调用（DeepSeek API）
#
# 目标: 用 Python 代码调用 DeepSeek，完成一次对话
#
# 前置准备:
#   1. 去 platform.deepseek.com 注册，拿到 API Key
#   2. 把 Key 粘贴到 .env 文件: DEEPSEEK_API_KEY=sk-...
#   3. 确认安装了 requests 和 python-dotenv
#
# 你需要实现:
#   1. load_api_key()     — 从 .env 文件读取 API Key
#   2. call_deepseek()    — 发送 HTTP POST 请求，返回 AI 回答
#
# API 参考:
#   URL:  https://api.deepseek.com/chat/completions
#   Headers:
#     Authorization:  Bearer 你的APIKey
#     Content-Type:   application/json
#   Body (JSON):
#     {
#       "model":       "deepseek-chat",
#       "messages":    [{"role": "user", "content": "你的问题"}],
#       "max_tokens":  1024
#     }
#   响应: response.json()["choices"][0]["message"]["content"]
#
# ============================================================
# 知识点: HTTP POST | headers/body | requests | .env 环境变量 | API Key 安全 | messages 结构
# ============================================================

import os
import sys

from dotenv import load_dotenv

# ---------- 待实现 ----------


def load_api_key() -> str | None:
    """从 .env 文件加载 DeepSeek API Key 并返回"""
    load_dotenv()  # 加载env内容
    return os.getenv("DEEPSEEK_API_KEY")


def call_deepseek(prompt: str, api_key: str) -> str:
    """
    调用 DeepSeek API 发送 prompt 并返回 AI 的文本回答
    提示:
      1. URL = "https://api.deepseek.com/chat/completions"
      2. headers = {"Authorization": f"Bearer {api_key}", ...}
      3. body = {"model": ..., "messages": [...], "max_tokens": ...}
      4. response = requests.post(URL, headers=headers, json=body)
      5. return response.json()["choices"][0]["message"]["content"]
    """
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1024,
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    import requests

    all_pass = True

    # 测试1: API Key 加载
    key = load_api_key()
    if key and "把你的" not in key:
        masked = key[:8] + "..." + key[-4:]
        print(f"PASS API Key加载 -> {masked}")
    else:
        print("FAIL API Key未配置 -> 请编辑 .env 文件填入真实 DeepSeek Key")
        sys.exit(1)

    # 测试2: 模型连接性
    response = call_deepseek("你好，请用一句话介绍你自己", key)
    if response and len(response) > 5:
        print(f"PASS 模型连接 -> {response}")
    else:
        print(f"FAIL 模型连接 -> 返回为空或太短: {response!r}")
        all_pass = False

    # 测试3: 复杂问题
    response2 = call_deepseek("请用中文回答：1+1等于几？只回答数字", key)
    if response2 and "2" in response2:
        print(f"PASS 复杂问题 -> {response2}")
    else:
        print(f"FAIL 复杂问题 -> {response2!r}")
        all_pass = False

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
