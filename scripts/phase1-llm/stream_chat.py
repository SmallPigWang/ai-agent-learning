# ============================================================
# 练习: Streaming 流式输出
#
# 核心认知: 普通调用 = "等快递"（一次性收完整回答）
#          流式调用   = "边送边收"（AI 生成一个字推一个字）
#
# 你之前写的 chat_with_system 是"等快递"模式:
#   requests.post() 会一直等，AI 说完整个回答才返回
#   回答越长等得越久，用户只能干瞪眼
#
# 流式只需要改 3 处:
#   1. body 里加 "stream": True           ← 告诉服务器"我要流式"
#   2. 请求时加 stream=True                ← 告诉 requests"别一次读完"
#   3. 用 iter_lines() 逐行读，每行是个 SSE 数据块
#
# SSE 数据格式（服务器推过来的每一行）:
#   data: {"choices":[{"delta":{"content":"你"}}]}   ← 一个字/词
#   data: {"choices":[{"delta":{"content":"好"}}]}   ← 又一个
#   ...
#   data: [DONE]                                     ← 结束信号，读到就停
#
# 你要实现:
#   stream_chat(messages, api_key) — 流式对话生成器
#     逐块 yield AI 回复的文本片段
#
# 新知识: yield（生成器）
#   return  = 函数结束，返回一个值
#   yield   = 函数暂停，先交出这个值；下次调用继续往下走
#   流式输出天生就该用 yield —— 产出一个字，交出去，再等下一个
#
# 规则:
#   - 函数体里禁止 print —— 用 yield 把每个字块交出去
#   - 测试块负责打印，拼出完整回复
#
# ============================================================
# 知识点: SSE 协议 | 两处 stream=True | yield 生成器 | iter_lines 逐行读 | delta vs message | reasoning_content 兜底
# ============================================================

import json
import os
import sys
from collections.abc import Iterator

import requests
from dotenv import load_dotenv

# ---------- 复用（从 message_roles.py 搬过来）----------


def load_api_key() -> str | None:
    """从 .env 文件加载 API Key"""
    load_dotenv()
    return os.getenv("DEEPSEEK_API_KEY")


# ---------- 待实现 ----------


def stream_chat(messages: list[dict], api_key: str) -> Iterator[str]:
    """
    流式对话生成器：逐块 yield AI 回复的文本片段
    流程:
      1. url/headers 同 message_roles.py
      2. body 里加 "stream": True
      3. response = requests.post(url, headers=headers, json=body, stream=True)
      4. for line in response.iter_lines():
           a. 跳过空行（服务器会发空行分隔）
           b. line 是 bytes 类型，先解码: line.decode("utf-8")
           c. 去掉 "data: " 前缀（前 6 个字符）→ 剩下是 JSON 字符串
           d. 如果是 "[DONE]" → break 结束
           e. 否则 json.loads(剩下的) 解析，
              取 data["choices"][0]["delta"]["content"] → yield 它
              （注意: 有的 delta 没有 content 字段，要跳过）
    """
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    body = {
        "model": "deepseek-v4-flash",
        "messages": messages,
        "max_tokens": 1024,
        "stream": True,
    }
    response = requests.post(url, headers=headers, json=body, stream=True)

    # 流式输出
    for line in response.iter_lines():
        # 跳过空行
        if not line:
            continue

        # bytes -> 字符串
        text = line.decode("utf-8")

        # 只处理 data 行，跳过注释等
        if not text.startswith("data: "):
            continue

        # 去除 "data: " 前缀
        text = text[6:]

        # 结束判断
        if text == "[DONE]":
            break

        # 解析 JSON
        data = json.loads(text)
        delta = data["choices"][0]["delta"]

        content = delta.get("content") or delta.get("reasoning_content")
        if content:
            yield content


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key()
    if not key or "你的" in key:
        print("请先在 .env 文件中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # 测试1: 逐字输出效果（先看效果，再验证）
    messages = [{"role": "user", "content": "用一句话介绍你自己"}]
    chunks = []
    print("AI: ", end="", flush=True)
    for chunk in stream_chat(messages, key):
        chunks.append(chunk)
        print(chunk, end="", flush=True)  # end="" 不换行, flush=True 立即显示
    print()

    # 测试2: 真的流式了吗? — 分块数 > 1 才算流式
    r2 = len(chunks) > 1
    print(f"{'PASS' if r2 else 'FAIL'} 流式分块 -> {len(chunks)} 块 | expected: > 1")
    all_pass = all_pass and r2

    # 测试3: 内容完整性 — 拼起来是完整回复
    full = "".join(chunks)
    r3 = len(full) > 10
    print(f"{'PASS' if r3 else 'FAIL'} 内容完整 -> {len(full)} 字 | expected: > 10")
    all_pass = all_pass and r3

    # 测试4: 多轮对话 + 流式
    history = [
        {"role": "user", "content": "我叫小红"},
        {"role": "assistant", "content": "你好小红！"},
    ]
    full4 = ""
    for chunk in stream_chat(
        history + [{"role": "user", "content": "我叫什么？"}], key
    ):
        full4 += chunk
    r4 = "小红" in full4
    print(f"{'PASS' if r4 else 'FAIL'} 多轮+流式 -> {full4!r} | expected: 含 小红")
    all_pass = all_pass and r4

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
