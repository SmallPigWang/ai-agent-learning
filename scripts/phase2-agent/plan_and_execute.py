# ============================================================
# 练习: Plan-and-Execute —— 先规划后执行（2.4 第一步）
#
# 背景: ReAct 每轮问 LLM"下一步干嘛"，走一步看一步。
#       Plan-and-Execute 反过来: 先生成完整计划（一份数据），
#       再照着计划逐步执行。计划可以被校验、打印、给人过目。
#
# 计划的数据结构（计划 = 数据，和 messages 同等待遇）:
#   plan = [
#       {"id": 1, "action": "add",  "args": [2, 3]},      # 2+3
#       {"id": 2, "action": "mul",  "args": [10, 4]},     # 10*4
#       {"id": 3, "action": "echo", "args": ["完成"]},    # 原样返回
#   ]
#
# 你要实现:
#   1. validate_plan(plan) -> bool
#      计划安检闸门（复用 Day 5 的逐条件 return False 模式）:
#      - 必须是非空列表
#      - 每步是 dict，且同时有 "id" / "action" / "args" 三个键
#      - action 是 str，args 是 list
#      - id 必须从 1 开始连续编号（1, 2, 3...，断号/乱序都不行）
#
#   2. execute_step(step, tools) -> str
#      执行单步: 按 action 在 tools 注册表里找到函数，用 args 调用
#      - 找不到这个 action -> 返回 "未知操作: {action}"（优雅降级，不崩）
#      - 正常 -> 返回 str(结果)
#      提示: tools = {"add": 函数, "mul": 函数, ...}，
#            tools[action](*step["args"]) 里的 * 是"列表拆开当参数"
#            （safe_get 的 *keys 是它的亲戚，一个在签名、一个在调用）
#
#   3. run_plan(task, planner, tools) -> dict
#      完整引擎，三段:
#      a. plan = planner(task)                  ← 规划（回调注入）
#      b. 计划不过安检 -> {"ok": False, "reason": "计划不合法", "results": []}
#      c. 逐步执行收集结果 -> {"ok": True, "task": task,
#                              "steps": 步数, "results": [每步结果]}
#
# ============================================================
# 知识点: Plan-and-Execute模式 | 计划即数据 | 安检闸门复用 | 工具注册表分发 | *args调用侧解包 | 回调注入(规划器) | 优雅降级
# ============================================================


def validate_plan(plan: list) -> bool:  # 校验器收"可能不合法"输入，参数类型放宽
    """校验计划是否合法: 非空、每步含 id/action/args、类型正确、id 从 1 连续"""
    if not plan:
        return False

    for i, step in enumerate(plan):
        if not isinstance(step, dict):
            return False
        for key in ("id", "action", "args"):
            if key not in step:
                return False
        if not isinstance(step["action"], str) or not isinstance(step["args"], list):
            return False
        if step["id"] != i + 1:
            return False

    return True


def execute_step(step: dict, tools: dict) -> str:
    """执行单步: 注册表查函数 -> *args 解包调用；未知操作优雅降级"""

    action = step["action"]

    if action not in set(tools):
        return f"未知操作: {action}"

    return str(tools[action](*step["args"]))


def run_plan(task: str, planner, tools: dict) -> dict:
    """Plan-and-Execute 引擎: 规划(回调) -> 安检 -> 逐步执行 -> 汇总"""

    plan = planner(task)

    if not validate_plan(plan):
        return {"ok": False, "reason": "计划不合法", "results": []}

    results = [execute_step(step, tools) for step in plan]
    return {"ok": True, "task": task, "steps": len(plan), "results": results}


if __name__ == "__main__":
    # ---- 测试脚手架（已写好，不用动）----

    # 工具注册表: 动作名 -> 函数
    def _add(a: int, b: int) -> int:
        return a + b

    def _mul(a: int, b: int) -> int:
        return a * b

    def _echo(msg: str) -> str:
        return msg

    tools = {"add": _add, "mul": _mul, "echo": _echo}

    # 合法计划（fake 规划器返回的，模拟 LLM 规划结果）
    good_plan = [
        {"id": 1, "action": "add", "args": [2, 3]},
        {"id": 2, "action": "mul", "args": [10, 4]},
        {"id": 3, "action": "echo", "args": ["完成"]},
    ]

    def good_planner(task: str) -> list[dict]:
        return good_plan

    def bad_planner(task: str) -> list[dict]:
        return [
            {"id": 1, "action": "add", "args": [1, 1]},
            {"id": 3, "action": "fly"},
        ]  # id断号+缺args

    # 测试1: validate_plan 安检
    print(f"PASS/FAIL 合法计划 -> {validate_plan(good_plan)} | expected: True")
    print(f"PASS/FAIL 空计划 -> {validate_plan([])} | expected: False")
    no_args = [{"id": 1, "action": "add"}]
    print(f"PASS/FAIL 缺args键 -> {validate_plan(no_args)} | expected: False")
    bad_id = [
        {"id": 1, "action": "add", "args": [1]},
        {"id": 3, "action": "mul", "args": [2]},
    ]
    print(f"PASS/FAIL id断号 -> {validate_plan(bad_id)} | expected: False")
    not_dict = ["not a dict"]
    print(f"PASS/FAIL 步骤不是dict -> {validate_plan(not_dict)} | expected: False")

    # 测试2: execute_step 分发
    s1 = execute_step({"id": 1, "action": "add", "args": [2, 3]}, tools)
    print(f"PASS/FAIL 加法步 -> {s1} | expected: 5")
    s2 = execute_step({"id": 1, "action": "mul", "args": [10, 4]}, tools)
    print(f"PASS/FAIL 乘法步 -> {s2} | expected: 40")
    s3 = execute_step({"id": 1, "action": "fly", "args": [1]}, tools)
    print(f"PASS/FAIL 未知操作 -> {s3} | expected: 未知操作: fly")

    # 测试3: run_plan 完整引擎
    r1 = run_plan("算 2+3，再把结果乘 10 倍，最后报告完成", good_planner, tools)
    print(f"PASS/FAIL 引擎ok -> {r1['ok']} | expected: True")
    print(f"PASS/FAIL 步数 -> {r1['steps']} | expected: 3")
    print(f"PASS/FAIL 结果按序 -> {r1['results']} | expected: ['5', '40', '完成']")
    r2 = run_plan("坏计划任务", bad_planner, tools)
    print(f"PASS/FAIL 坏计划被拦 -> {r2['ok']} | expected: False")
    print(f"PASS/FAIL 拦截原因 -> {r2['reason']} | expected: 计划不合法")
    print(f"PASS/FAIL 拦截后无结果 -> {r2['results']} | expected: []")
