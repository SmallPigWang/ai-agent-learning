# ============================================================
# 练习: 多轮对话
#
# 核心认知: LLM 每次调用都是"失忆"的——它不记得上一轮说了什么。
# 多轮对话的本质: 把历史消息全部塞进 messages 数组发回去。
#
# 你需要实现:
#   chat_loop() — 一个简易命令行聊天，支持连续对话
#     1. 初始化 messages = [] 空列表
#     2. 循环: 用户输入 → 添加到 messages → 调 API → 回复加到 messages
#     3. 输入 quit 退出
#     4. 每次调 API 都把整个 messages 发过去（这就是"记忆"）
#
# 提示: 复用 first_api_call.py 里的 load_api_key() 和 call_deepseek()
#       但 call_deepseek 需要改成接收 messages 列表，而不是单个 prompt
#
# ============================================================
# 知识点: LLM 无状态 | history 回填实现跨轮记忆 | messages 数组累积
# ============================================================

import os
import sys

import requests
from dotenv import load_dotenv

# ---------- 复用（从 first_api_call.py 搬过来）----------


def load_api_key() -> str | None:
    """从 .env 文件加载 API Key"""
    load_dotenv()
    return os.getenv("DEEPSEEK_API_KEY")


def chat_once(messages: list[dict], api_key: str) -> str:
    """
    发送完整对话历史到 DeepSeek，返回 AI 的回复
    body 里只改 messages 字段，其他和 first_api_call.py 一样
    """
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {"model": "deepseek-chat", "messages": messages, "max_tokens": 1024}
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]


# ---------- 待实现 ----------


def chat_loop(api_key: str) -> None:
    """
    命令行多轮对话
    流程:
      1. messages = []
      2. while True:
         a. 读取用户输入 input("You: ")
         b. 输入 "quit" → break
         c. 把 {"role": "user", "content": 输入} append 到 messages
         d. 调 chat_once(messages, api_key) 获取回复
         e. 打印回复
         f. 把 {"role": "assistant", "content": 回复} append 到 messages
    """
    messages: list[dict] = []
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            break
        messages.append({"role": "user", "content": user_input})
        reply = chat_once(messages=messages, api_key=api_key)
        print(f"AI: {reply}")
        messages.append({"role": "assistant", "content": reply})


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    key = load_api_key()
    if not key or "你的" in key:
        print("请先在 .env 文件中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # 基础测试: 手动构造 messages 验证多轮记忆
    messages = []

    # 第1轮
    messages.append({"role": "user", "content": "我叫小明，请记住我的名字"})
    reply1 = chat_once(messages, key)
    messages.append({"role": "assistant", "content": reply1})
    print(f"第1轮: {reply1}")
    if "小明" not in reply1:
        print("FAIL 第1轮没识别名字")
    else:
        print("PASS 第1轮")

    # 第2轮 — 问"我叫什么"，AI 应该回答"小明"
    messages.append({"role": "user", "content": "我刚才说我叫什么名字？"})
    reply2 = chat_once(messages, key)
    messages.append({"role": "assistant", "content": reply2})
    print(f"第2轮: {reply2}")
    if "小明" in reply2:
        print("PASS 第2轮 — AI 记住了!")
    else:
        print(f"FAIL 第2轮 — AI 失忆了: {reply2}")

    # 第3轮
    messages.append({"role": "user", "content": "再见"})
    reply3 = chat_once(messages, key)
    print(f"第3轮: {reply3}")
    if reply3:
        print("PASS 第3轮")
    else:
        print("FAIL 第3轮")

    print("\n多轮记忆测试完成。运行 chat_loop() 进入交互模式:")
    print("  (跳过交互，直接 Ctrl+C 退出)")
    # chat_loop(key)  # 取消注释可进入交互模式
