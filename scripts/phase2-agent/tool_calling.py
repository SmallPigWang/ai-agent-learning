# ============================================================
# 练习: Tool Calling —— 给 LLM 装上"手"
#
# 核心认知:
#   之前: LLM 只说话，自己心算
#   现在: LLM 可以"叫"外部函数帮它做事
#
#   工具 = 普通 Python 函数 + JSON Schema（给 LLM 看的说明书）
#   流程: 你发 Schema + 问题 → LLM 说"我要调XX工具" → 你执行 → 回填结果 → LLM 回答
#
# 你要实现:
#   1. 定义 2 个工具函数 + 它们的 JSON Schema
#   2. tool_loop(prompt, tools, schemas, key) — 一轮工具调用循环
#
# ============================================================
# 知识点: 工具=函数+JSON Schema | tool_use→execute→tool_result 循环 | 消息回填顺序 | tool_call_id
# ============================================================

import json as _json
import os
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

# ---------- 复用 ----------


def load_api_key(key_name: str) -> str | None:
    load_dotenv()
    return os.getenv(key_name)


# ---------- 待实现：工具函数 ----------


def calculator(expression: str) -> str:
    """
    安全计算数学表达式，返回结果字符串
    提示: 用 eval 最简单，但只允许数字和运算符
    """
    # 安全防护: 只允许数字、运算符、空格、小数点
    allowed = set("0123456789+-*/().% ")
    if not all(c in allowed for c in expression):
        return "Error: 非法字符"
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:  # noqa: BLE001
        return f"Error: {e}"


def get_current_time() -> str:
    """
    获取当前时间（模拟，实际可用 datetime）
    提示: from datetime import datetime → datetime.now().strftime(...)
    """
    return datetime.now().strftime("%H:%M:%S")  # noqa: DTZ005


# ---------- 待实现：JSON Schema ----------

CALCULATOR_SCHEMA = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "安全计算数学表达式。输入一个数学表达式字符串，返回计算结果。",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "数学表达式，如 '1+2*3'",
                }
            },
            "required": ["expression"],
        },
    },
}

# TODO: 参照 CALCULATOR_SCHEMA 写 TIME_SCHEMA
TIME_SCHEMA = {
    # 填这里
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "获取当前北京时间",
        "parameters": {
            "type": "object",
            "properties": {},
        },
    },
}


# ---------- 待实现：工具调度表 ----------

TOOL_MAP = {
    "calculator": calculator,
    "get_current_time": get_current_time,
}


# ---------- 待实现：工具调用循环 ----------


def tool_loop(prompt: str, tools: list[dict], key: str) -> str:
    """
    一轮工具调用: 发 prompt + 工具说明书 → LLM 决定是否调工具 → 执行 → 回填 → 最终回答
    流程:
      1. messages = [{"role": "user", "content": prompt}]
      2. body = {..., "messages": messages, "tools": tools}
         注意: DeepSeek 的 tools 参数是 `tools`，不是 `functions`！
      3. response = requests.post(URL, ...)
         → 如果 response 里有 tool_calls:
           a. 取 tool_calls[0]["function"]["name"] 和 arguments
           b. 调 TOOL_MAP[name](**json.loads(arguments)) 得到结果
           c. 把 LLM 的 assistant 消息 + tool 结果回填 messages
           d. 再次调 API，不带 tools（让 LLM 基于结果回答）
           e. return AI 最终回答
         → 如果没有 tool_calls:
           → return AI 的直接回答
    提示: 先 print 一下 response.json() 看看结构，再写解析逻辑
    """
    messages = [{"role": "user", "content": prompt}]
    body = {
        "model": "deepseek-chat",
        "messages": messages,
        "tools": tools,
    }
    URL = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    resp = requests.post(url=URL, json=body, headers=headers)
    msg = resp.json()["choices"][0]["message"]

    # 判断tool_calls是否存在
    if "tool_calls" in msg:
        # 执行工具，回弹消息
        tc = msg["tool_calls"][0]
        tool_name = tc["function"]["name"]
        args = _json.loads(tc["function"]["arguments"])
        result = TOOL_MAP[tool_name](**args)
    else:
        return msg["content"]

    # 回填消息
    messages.append(msg)
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tc["id"],
            "content": result,
        }
    )

    # 第二次API调用
    body2 = {
        "model": "deepseek-chat",
        "messages": messages,
    }
    resp2 = requests.post(url=URL, json=body2, headers=headers)
    return resp2.json()["choices"][0]["message"]["content"]


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # 测试1: calculator 工具本身
    r1 = calculator("2+3*4")
    print(
        f"{'PASS' if r1 == '14' else 'FAIL'} calculator(2+3*4) -> {r1} | expected: 14"
    )
    all_pass = all_pass and r1 == "14"

    # 测试2: calculator 安全防护
    r2 = calculator("__import__('os').system('dir')")
    print(
        f"{'PASS' if 'Error' in r2 else 'FAIL'} calculator(危险输入) -> {r2} | expected: Error"
    )
    all_pass = all_pass and "Error" in r2

    # 测试3: tool_loop — LLM 自动调 calculator
    r3 = tool_loop("1+2+3+4+5等于多少？", [CALCULATOR_SCHEMA], key)
    r3_pass = "15" in r3
    print(
        f"{'PASS' if r3_pass else 'FAIL'} tool_loop(1+2+3+4+5) -> {r3!r} | expected: 含 15"
    )
    all_pass = all_pass and r3_pass

    # 测试4: tool_loop — 不需要工具的问题
    r4 = tool_loop("你好，用一句话介绍你自己", [CALCULATOR_SCHEMA], key)
    r4_pass = r4 and "calculator" not in r4.lower()[:50]
    print(
        f"{'PASS' if r4_pass else 'FAIL'} tool_loop(闲聊) -> {r4[:60]!r}... | expected: 不调工具直接回答"
    )
    all_pass = all_pass and r4_pass

    # 测试5: tool_loop — 单工具：问时间→自动调 get_current_time
    r5 = tool_loop("现在北京时间几点？", [TIME_SCHEMA], key)
    r5_pass = ":" in r5
    print(
        f"{'PASS' if r5_pass else 'FAIL'} tool_loop(问时间, 单工具) -> {r5!r} | expected: 含时间"
    )
    all_pass = all_pass and r5_pass

    # 测试6: tool_loop — 双工具：问数学→LLM 应选 calculator 而非 get_current_time
    r6 = tool_loop("帮我算 100*50", [CALCULATOR_SCHEMA, TIME_SCHEMA], key)
    r6_pass = "5000" in r6
    print(
        f"{'PASS' if r6_pass else 'FAIL'} tool_loop(算100*50, 双工具) -> {r6!r} | expected: 含5000"
    )
    all_pass = all_pass and r6_pass

    # 测试7: tool_loop — 双工具：问时间→LLM 应选 get_current_time 而非 calculator
    r7 = tool_loop("现在几点了？", [CALCULATOR_SCHEMA, TIME_SCHEMA], key)
    r7_pass = ":" in r7 or "点" in r7
    print(
        f"{'PASS' if r7_pass else 'FAIL'} tool_loop(问时间, 双工具) -> {r7!r} | expected: 含时间"
    )
    all_pass = all_pass and r7_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
