# ============================================================
# 练习: 并行工具调用 —— LLM 一次叫多个工具
#
# 核心认知:
#   单工具: tool_calls[0] → 执行 → 回填一条 tool 消息 → 回答
#   多工具: for tc in tool_calls → 逐个执行 → 回填多条 tool 消息 → 回答
#
# 场景:
#   用户: "现在几点了？顺便帮我算 100*50"
#   LLM: "我要调 get_current_time 和 calculator 两个工具！"
#   → tool_calls 数组里有 2 条，你需要全部执行+回填
#
# 你要实现:
#   1. 新建 parallel_tool_loop()——支持 N 个 tool_calls
#   2. 加一个 get_weather(city) 工具（模拟返回天气字符串）
#   3. 3 工具同时可选 + 并行调用测试
# ============================================================
# 知识点: for tc in tool_calls 并行执行 | 多条 tool 消息回填 | assistant 在 tool 之前
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


# ---------- 工具函数 ----------


def calculator(expression: str) -> str:
    """安全计算数学表达式"""
    allowed = set("0123456789+-*/().% ")
    if not all(c in allowed for c in expression):
        return "Error: 非法字符"
    try:
        return str(eval(expression))
    except Exception as e:  # noqa: BLE001
        return f"Error: {e}"


def get_current_time() -> str:
    """获取当前时间"""
    return datetime.now().strftime("%H:%M:%S")  # noqa: DTZ005


# TODO: 实现第 3 个工具
def get_weather(city: str) -> str:
    """
    模拟获取城市天气（不需要真实 API，返回固定字符串即可）
    示例: get_weather("北京") → "北京: 晴, 25°C"
    """
    return f"{city}: 晴，25℃"


# ---------- JSON Schema ----------

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

TIME_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_current_time",
        "description": "获取当前北京时间",
        "parameters": {"type": "object", "properties": {}},
    },
}

# TODO: 参照上面两个写 WEATHER_SCHEMA（有一个参数: city 字符串）
WEATHER_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取当地天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名称：如北京、上海"}
            },
            "required": ["city"],
        },
    },
}


# ---------- 工具调度表 ----------

TOOL_MAP = {
    "calculator": calculator,
    "get_current_time": get_current_time,
    "get_weather": get_weather,
}

ALL_TOOLS = [CALCULATOR_SCHEMA, TIME_SCHEMA, WEATHER_SCHEMA]


# ---------- 待实现：并行工具调用循环 ----------


def parallel_tool_loop(prompt: str, tools: list[dict], key: str) -> str:
    """
    支持并行工具调用: tool_calls 数组里可能有 1~N 个工具调用。
    关键差异: 不是 tool_calls[0]，而是 for tc in tool_calls 逐个处理。

    流程:
      1. messages = [{"role": "user", "content": prompt}]
      2. body = {..., "messages": messages, "tools": tools}
      3. resp = requests.post(URL, ...)
      4. msg = resp.json()["choices"][0]["message"]
      5. if "tool_calls" in msg:
           for tc in msg["tool_calls"]:              # ← 循环！不是只取 [0]
               name = tc["function"]["name"]
               args = _json.loads(tc["function"]["arguments"])
               result = TOOL_MAP[name](**args)
               # 每条工具调用单独 append 一条 tool 消息
               messages.append({
                   "role": "tool",
                   "tool_call_id": tc["id"],
                   "content": result
               })
           messages.append(msg)   # assistant 消息（含全部 tool_calls）
           第二次调 API
         else:
           return msg["content"]

    提示: 对照你之前 tool_calling.py 里的 tool_loop，改动只有 3 处:
          tool_calls[0] → for tc in tool_calls
          单条 messages.append → for 循环里多条 messages.append
          messages.append(msg) 移到 for 循环之后（先加工具结果，再加 assistant 消息）
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
        messages.append(msg)
        # 执行工具，回弹消息
        for tc in msg["tool_calls"]:
            tool_name = tc["function"]["name"]
            args = _json.loads(tc["function"]["arguments"])
            result = TOOL_MAP[tool_name](**args)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": result,
                }
            )
    else:
        return msg["content"]

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

    URL = "https://api.deepseek.com/v1/chat/completions"
    HEADERS = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    # 测试1: get_weather 函数本身
    r1 = get_weather("北京")
    r1_pass = "北京" in r1 and "25" in r1
    print(
        f"{'PASS' if r1_pass else 'FAIL'} get_weather(北京) -> {r1!r} | expected: 含 北京+25°C"
    )
    all_pass = all_pass and r1_pass

    # 测试2: 单工具 — 不退化（parallel 版也能处理单个 tool_call）
    r2 = parallel_tool_loop("1+2+3+4+5等于多少？", ALL_TOOLS, key)
    r2_pass = "15" in r2
    print(
        f"{'PASS' if r2_pass else 'FAIL'} parallel(单工具-计算) -> {r2!r} | expected: 含15"
    )
    all_pass = all_pass and r2_pass

    # 测试3: 单工具 — 不影响不需要工具的情况
    r3 = parallel_tool_loop("你好，用一句话介绍你自己", ALL_TOOLS, key)
    r3_pass = r3 is not None and len(r3) > 0
    print(
        f"{'PASS' if r3_pass else 'FAIL'} parallel(闲聊) -> {r3[:60]!r}... | expected: 正常回答"
    )
    all_pass = all_pass and r3_pass

    # 测试4: ★ 并行 — 一问问两个工具
    r4 = parallel_tool_loop("现在几点了？顺便帮我算 100*50", ALL_TOOLS, key)
    r4_has_time = ":" in r4 or "点" in r4
    r4_has_calc = "5000" in r4
    r4_pass = r4_has_time and r4_has_calc
    print(
        f"{'PASS' if r4_pass else 'FAIL'} parallel(时间+计算) -> {r4!r} | expected: 含时间+5000"
    )
    all_pass = all_pass and r4_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
