# ============================================================
# 练习: ReAct 循环 —— 手写 Agent 核心引擎
#
# ReAct = Reasoning + Acting（思考 + 行动）
#
# 你的 tool_loop 是一轮游: 用户问 → 调工具 → 回答 → 结束
# ReAct 是多轮循环:  用户问 → 思考 → 调工具 → 观察结果 →
#                     再思考 → 再调工具 → ... → 最终回答
#
# 场景:
#   用户: "帮我查北京天气，晴天就算 365*24，雨天就算 365*12"
#   → 第1轮: get_weather("北京") → "晴天"
#   → 第2轮: calculator("365*24") → "8760"
#   → 第3轮: 结束，回答 "晴天！一年有 8760 小时"
#
# 你要实现:
#   react_loop(prompt, tools, key) — 支持多轮工具调用的 Agent 循环
#   关键: while 循环 + 终止条件
# ============================================================
# 知识点: ReAct 思考-行动循环 | 动态 N 轮工具调用 | 终止条件（max_iterations + consecutive_errors） | body 每次重建
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


# ---------- 工具函数（复用 + 新增）----------


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


def get_weather(city: str) -> str:
    """模拟获取城市天气"""
    weather_db = {
        "北京": "晴天, 25°C",
        "上海": "多云, 28°C",
        "深圳": "雨天, 22°C",
        "杭州": "阴天, 20°C",
    }
    w = weather_db.get(city)
    if w:
        return f"{city}: {w}"
    return f"{city}: 未查到天气数据"


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

WEATHER_SCHEMA = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "查询指定城市的天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "城市名称，如 '北京'"}
            },
            "required": ["city"],
        },
    },
}


# ---------- 工具调度 ----------

TOOL_MAP = {
    "calculator": calculator,
    "get_current_time": get_current_time,
    "get_weather": get_weather,
}

ALL_TOOLS = [CALCULATOR_SCHEMA, TIME_SCHEMA, WEATHER_SCHEMA]


# ---------- 待实现：ReAct 循环 ----------


def react_loop(
    prompt: str, tools: list[dict], key: str, max_iterations: int = 10
) -> str:
    """
    多轮工具调用循环。和 parallel_tool_loop 的区别:
      - 不是调一次工具就结束，而是持续循环
      - 每次 LLM 可以调工具 or 直接回答
      - 调工具 → 回填结果 → 继续下一轮
      - 不调工具 → 这就是最终答案，结束

    流程:
      messages = [{"role": "user", "content": prompt}]

      for _ in range(max_iterations):      # ← 安全上限
          resp = requests.post(URL, ..., json={messages, tools})
          msg = resp.json()["choices"][0]["message"]

          if "tool_calls" not in msg:
              return msg["content"]          # ← 没有工具调用 = 任务完成

          # 有工具调用 → 执行 + 回填
          messages.append(msg)
          for tc in msg["tool_calls"]:
              name = tc["function"]["name"]
              args = _json.loads(tc["function"]["arguments"])
              result = TOOL_MAP[name](**args)
              messages.append({
                  "role": "tool",
                  "tool_call_id": tc["id"],
                  "content": result
              })
          # 继续下一轮循环（不 return！）

      return "Error: 超过最大迭代次数"       # 安全兜底

    提示: 就是把你 parallel_tool_loop 里的 if/else 包一层 for 循环。
          区别: else 不是 return（继续循环），
              只在 LLM 不调工具时 return（循环内唯一的出口）。
    """
    messages = [{"role": "user", "content": prompt}]

    URL = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    for _ in range(max_iterations):
        body = {
            "model": "deepseek-chat",
            "messages": messages,
            "tools": tools,
        }
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

    return "Error:超过最大迭代次数"


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # 测试1: 单步任务 — 简单计算，1轮搞定
    r1 = react_loop("1+2+3+4+5等于多少？", ALL_TOOLS, key)
    r1_pass = "15" in r1
    print(f"{'PASS' if r1_pass else 'FAIL'} react(单步计算) -> {r1!r} | expected: 含15")
    all_pass = all_pass and r1_pass

    # 测试2: 多步任务 ★ — 查天气→根据结果计算
    r2 = react_loop(
        "帮我查一下北京天气。如果是晴天，就算 365*24 等于多少；如果不是，就算 365*12。把天气和计算结果都告诉我。",
        ALL_TOOLS,
        key,
    )
    r2_has_weather = "北京" in r2 and ("晴" in r2 or "25" in r2)
    r2_has_calc = "8760" in r2
    r2_pass = r2_has_weather and r2_has_calc
    print(f"{'PASS' if r2_pass else 'FAIL'} react(天气+条件计算) -> {r2!r}")
    print(
        f"    天气: {'OK' if r2_has_weather else 'MISS'}, 计算: {'OK' if r2_has_calc else 'MISS'}"
    )
    all_pass = all_pass and r2_pass

    # 测试3: 多步任务 — 查两个城市天气 + 计算时间差
    r3 = react_loop("帮我查北京和深圳的天气。然后告诉我现在几点。", ALL_TOOLS, key)
    r3_has_bj = "北京" in r3 and ("晴" in r3 or "25" in r3)
    r3_has_sz = "深圳" in r3 and ("雨" in r3 or "22" in r3)
    r3_has_time = ":" in r3 or "点" in r3
    r3_pass = r3_has_bj and r3_has_sz and r3_has_time
    print(f"{'PASS' if r3_pass else 'FAIL'} react(双天气+时间) -> {r3!r}")
    print(
        f"    北京: {'OK' if r3_has_bj else 'MISS'}, 深圳: {'OK' if r3_has_sz else 'MISS'}, 时间: {'OK' if r3_has_time else 'MISS'}"
    )
    all_pass = all_pass and r3_pass

    # 测试4: 闲聊 — 不需要工具，0轮直接回答
    r4 = react_loop("你好，介绍一下你自己", ALL_TOOLS, key)
    r4_pass = r4 is not None and len(r4) > 0
    print(
        f"{'PASS' if r4_pass else 'FAIL'} react(闲聊) -> {r4[:60]!r}... | expected: 正常回答"
    )
    all_pass = all_pass and r4_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
