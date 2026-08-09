# ============================================================
# 练习: JSON 深度实战 —— Agent 开发者的 JSON 肌肉记忆
#
# Agent 开发中 JSON 无处不在:
#   - API 请求体构造 (messages / tools / body)
#   - 响应解析 (深层嵌套取值)
#   - 工具 Schema 设计 (JSON Schema 规范)
#   - 工具参数序列化 (json.loads / json.dumps)
#   - 消息结构拼接 (role/content/tool_calls)
#
# 本练习聚焦 4 个核心技能:
#   1. safe_get() — 深层取值不崩
#   2. validate_tool_schema() — 校验工具定义是否合法
#   3. build_messages() — 动态拼接消息数组
#   4. parse_tool_arguments() — 安全解析工具参数
# ============================================================

import json as _json
from typing import Any


# ============================================================
# 任务1: safe_get() — 安全深层取值
#
# 场景: API 返回的 JSON 嵌套很深，中间任何一层 key 不存在就崩。
#       需要一个函数，按路径取值，缺了就返回默认值。
#
# 示例:
#   data = {"a": {"b": {"c": 42}}}
#   safe_get(data, "a", "b", "c") → 42
#   safe_get(data, "a", "x", "y") → None
#   safe_get(data, "a", "x", "y", default="N/A") → "N/A"
#   safe_get(data, "a", "b") → {"c": 42}  (非 dict 也正确返回)
# ============================================================

def safe_get(data: Any, *keys: str, default: Any = None) -> Any:
    """
    沿 *keys 路径逐层取值，中间任何一层失败返回 default。
    提示: 用 for 循环逐层 data = data.get(key)，用 try/except 兜底
    """
    for key in keys:
        if not isinstance(data,dict):
            return default
        
        if key in data:
            data = data.get(key)
        else:
            return default

    return data



# ============================================================
# 任务2: validate_tool_schema() — 校验工具 Schema
#
# 场景: 写 JSON Schema 容易漏字段。这个函数检查一个 tool schema
#       是否合法，返回 (is_valid, error_message)。
#
# 合法定义:
#   - 顶层必须有 "type": "function"
#   - "function" 必须是 dict
#   - "function" 里必须有 "name" (str) 和 "parameters" (dict)
#   - "parameters" 里必须有 "type": "object" 和 "properties" (dict)
#
# 提示: 安检闸门模式——逐条件查，不满足立即 return (False, "原因")
# ============================================================

def validate_tool_schema(schema: dict) -> tuple:
    """
    返回 (True, "OK") 或 (False, "具体错误描述")
    提示: schema.get("type") == "function" 开头
    """
    if schema.get("type") != "function":
        return False, "缺少 type 字段或 type 不是 function"

    fn = schema.get("function")
    if not isinstance(fn,dict):
        return False, "function 必须是字典"

    if not isinstance(fn.get("name"), str):
        return False, "缺少name字段"

    if not isinstance(fn.get("parameters"), dict):
        return False, "缺少parameters字段"

    para = fn.get("parameters")
    if not isinstance(para,dict):
        return False,"parameters不是字典"
    
    if para.get("type") != "object":
        return False, "parameters缺少 type:object"

    if not isinstance(para.get("properties"),dict):
        return False, "parameters缺少properties字段" 

    return True, "OK!"   


# ============================================================
# 任务3: build_messages() — 动态拼接消息数组
#
# 场景: tool_loop 里你手动拼 messages。这个函数把各种类型的消息
#       拼成一个标准 messages 列表。
#
# 规则:
#   - system: 只有一条，放第一
#   - user: 用户话
#   - assistant: AI 的话（content 可选，tool_calls 可选）
#   - tool: 工具结果（必须含 tool_call_id）
#
# 参数设计你自己定。最少支持 system + user 两条。
#
# 提示: 参照你在 tool_calling.py 里拼的 messages 结构。
# ============================================================

def build_messages(system_prompt: str, user_content: str) -> list[dict]:
    """
    构造包含 system + user 的标准 messages 列表
    返回 [{"role": "system", "content": ...}, {"role": "user", "content": ...}]
    """
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content},
    ]
    


# ============================================================
# 任务4: parse_tool_arguments() — 安全解析工具参数
#
# 场景: LLM 返回的 arguments 是 JSON 字符串，但不是总合法。
#       json.loads 遇到非法 JSON 直接崩，我们需要兜底返回 None。
#
# 要求:
#   - 合法 JSON → 返回 dict
#   - 非法 JSON → 返回 None（不抛异常）
#   - 空字符串 → 返回 None
#   - 已经是 dict → 直接返回
# ============================================================

def parse_tool_arguments(arguments: Any) -> dict | None:
    """
    安全解析工具参数，解析失败返回 None 而非抛异常
    提示: isinstance(arguments, dict) 先判断，再尝试 json.loads
    """
    if isinstance(arguments, dict):
        return arguments

    if not arguments:
        return None

    try:
        return _json.loads(arguments)
    except:
        return None


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True

    # --- 测试 safe_get ---
    data = {"a": {"b": {"c": 42}}}
    r1 = safe_get(data, "a", "b", "c")
    print(f"{'PASS' if r1 == 42 else 'FAIL'} safe_get → {r1!r} | expected: 42")
    all_pass = all_pass and r1 == 42

    r2 = safe_get(data, "a", "x", "y")
    print(f"{'PASS' if r2 is None else 'FAIL'} safe_get(缺失路径) → {r2!r} | expected: None")
    all_pass = all_pass and r2 is None

    r3 = safe_get(data, "a", "x", "y", default="N/A")
    print(f"{'PASS' if r3 == 'N/A' else 'FAIL'} safe_get(自定义默认值) → {r3!r} | expected: N/A")
    all_pass = all_pass and r3 == "N/A"

    expected_r4 = {"c": 42}
    r4 = safe_get(data, "a", "b")
    print(f"{'PASS' if r4 == expected_r4 else 'FAIL'} safe_get(中间层) → {r4!r} | expected: {expected_r4}")
    all_pass = all_pass and r4 == expected_r4

    # --- 测试 validate_tool_schema ---
    valid_schema = {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "计算数学表达式",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"]
            }
        }
    }
    ok, err = validate_tool_schema(valid_schema)
    print(f"{'PASS' if ok else 'FAIL'} validate(合法Schema) → {err!r} | expected: True")
    all_pass = all_pass and ok

    bad_no_type = {"function": {"name": "f", "parameters": {"type": "object", "properties": {}}}}
    ok, err = validate_tool_schema(bad_no_type)
    print(f"{'PASS' if not ok else 'FAIL'} validate(缺type) → {err!r} | expected: False")
    all_pass = all_pass and not ok

    bad_no_name = {
        "type": "function",
        "function": {"parameters": {"type": "object", "properties": {}}}
    }
    ok, err = validate_tool_schema(bad_no_name)
    print(f"{'PASS' if not ok else 'FAIL'} validate(缺name) → {err!r} | expected: False")
    all_pass = all_pass and not ok

    bad_params_no_type = {
        "type": "function",
        "function": {"name": "f", "parameters": {"properties": {}}}
    }
    ok, err = validate_tool_schema(bad_params_no_type)
    print(f"{'PASS' if not ok else 'FAIL'} validate(parameters缺type) → {err!r} | expected: False")
    all_pass = all_pass and not ok

    # --- 测试 build_messages ---
    msgs = build_messages("你是翻译官", "hello")
    r9 = len(msgs) == 2
    print(f"{'PASS' if r9 else 'FAIL'} build_messages(长度=2) → {len(msgs)} | expected: 2")
    all_pass = all_pass and r9

    r10 = msgs[0] == {"role": "system", "content": "你是翻译官"}
    print(f"{'PASS' if r10 else 'FAIL'} build_messages(system) → {msgs[0]!r} | expected: system消息")
    all_pass = all_pass and r10

    r11 = msgs[1] == {"role": "user", "content": "hello"}
    print(f"{'PASS' if r11 else 'FAIL'} build_messages(user) → {msgs[1]!r} | expected: user消息")
    all_pass = all_pass and r11

    # --- 测试 parse_tool_arguments ---
    expected_r12 = {"expression": "1+2"}
    r12 = parse_tool_arguments('{"expression": "1+2"}')
    print(f"{'PASS' if r12 == expected_r12 else 'FAIL'} parse(合法JSON) → {r12!r} | expected: {expected_r12}")
    all_pass = all_pass and r12 == expected_r12

    r13 = parse_tool_arguments("{这不是JSON}")
    print(f"{'PASS' if r13 is None else 'FAIL'} parse(非法JSON) → {r13!r} | expected: None")
    all_pass = all_pass and r13 is None

    r14 = parse_tool_arguments("")
    print(f"{'PASS' if r14 is None else 'FAIL'} parse(空字符串) → {r14!r} | expected: None")
    all_pass = all_pass and r14 is None

    expected_r15 = {"already": "dict"}
    r15 = parse_tool_arguments({"already": "dict"})
    print(f"{'PASS' if r15 == expected_r15 else 'FAIL'} parse(已是dict) → {r15!r} | expected: {expected_r15}")
    all_pass = all_pass and r15 == expected_r15

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
