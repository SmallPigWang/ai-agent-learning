# ============================================================
# 🧩 独立挑战题: 依赖感知执行器（2.4 验收三件套之二）
#
# 背景: run_plan / run_plan_with_replan 都是照清单【顺序】执行。
#       真实任务的步骤之间有依赖——切菜必须等备菜，下锅必须等切菜+烧水。
#       这题给计划装上 needs 字段，引擎自己排出合法执行顺序。
#
# 计划的新长相（多了 "needs" 键）:
#   plan = [
#       {"id": 3, "action": "echo", "args": ["下锅"], "needs": [4]},
#       {"id": 1, "action": "echo", "args": ["备菜"], "needs": []},
#       {"id": 4, "action": "add",  "args": [2, 3],   "needs": [1]},
#       {"id": 2, "action": "mul",  "args": [10, 4],  "needs": [1]},
#   ]
#   合法执行顺序: 1 → 2 → 4 → 3（列表顺序≠执行顺序！）
#
# 契约（题目的一部分）:
#   - 就绪: needs 里的 id 全部已完成、且自己没跑过
#   - 确定性: 多步同时就绪时按 id 从小到大执行
#   - 死锁: 还有剩余步骤但挑不出任何就绪步骤（有环/依赖黑洞）→ 终止报告
#
# 你要实现:
#   1. validate_deps(plan) -> bool
#      依赖合法性: 每个 needs 里的 id 都必须真实存在；不许依赖自己
#
#   2. ready_steps(plan, done) -> list[dict]
#      挑出"现在就能跑"的步骤（按 id 升序返回）:
#      needs ⊆ done 且自己的 id 不在 done 里
#
#   3. run_dep_plan(task, planner, tools) -> dict
#      依赖感知引擎:
#      a. plan = planner(task)；先过 validate_plan（从 plan_and_execute import）
#         再过 validate_deps，任一不过 ->
#         {"ok": False, "reason": "计划不合法" / "依赖不合法", "order": [], "results": []}
#      b. 循环: 挑就绪步骤（没有就绪且还有剩余 -> 死锁终止:
#         {"ok": False, "reason": "依赖死锁", "order": 已完成id序, "results": [...]})
#         执行它(复用 execute_step)，记录 order(执行id顺序) 和 results
#      c. 全部完成 ->
#         {"ok": True, "task": task, "order": [...], "results": [...]}
#
# ============================================================
# 知识点: （挑战题不预习——通关后教练揭晓）
# ============================================================
from plan_and_execute import execute_step


def validate_deps(plan: list) -> bool:
    """依赖合法性: 每个 needs 的 id 都存在；不许自依赖"""
    if not plan:
        return False

    ids = {step["id"] for step in plan}

    for i, step in enumerate(plan):
        if not isinstance(step, dict):
            return False
        for key in ("id", "action", "args"):
            if key not in step:
                return False
        if not isinstance(step["action"], str) or not isinstance(step["args"], list):
            return False

        needs = step.get("needs", [])
        for n in needs:
            if n not in ids:
                return False
            if n == step["id"]:
                return False
    return True


def ready_steps(plan: list[dict], done: set[int]) -> list[dict]:
    """挑出就绪步骤（按 id 升序）: needs 全在 done 且自己未完成"""
    ready: list[dict] = []

    for step in plan:
        if step["id"] in done:
            continue
        needs = step.get("needs", [])
        if all(n in done for n in needs):
            ready.append(step)

    return sorted(ready, key=lambda s: s["id"])


def run_dep_plan(task: str, planner, tools: dict) -> dict:
    """依赖感知引擎: 循环挑就绪→执行；无就绪且有剩余→死锁终止"""
    # ---- a. 初次规划 + 安检（今天的一体化安检 validate_deps）----
    plan = planner(task)

    if not validate_deps(plan):
        return {"ok": False, "reason": "依赖不合法", "order": [], "results": []}

    # ---- b. 执行循环: 收齐了吗？→ 挑就绪 → 一个没有=死锁 → 执行第一个 ----
    order: list[int] = []
    results: list[str] = []
    done: set[int] = set()

    while len(done) < len(plan):
        ready = ready_steps(plan=plan, done=done)
        if not ready:
            return {
                "ok": False,
                "reason": "依赖死锁",
                "order": order,
                "results": results,
            }

        step = ready[0]
        results.append(execute_step(step=step, tools=tools))
        order.append(step["id"])
        done.add(step["id"])

    # ---- c. 跑完全程，汇总报告（replans 让调用方看到改了几次道）----
    return {
        "ok": True,
        "task": task,
        "order": order,
        "results": results,
    }


if __name__ == "__main__":
    # ---- 测试脚手架（已写好，不用动）----

    def _add(a: int, b: int) -> int:
        return a + b

    def _mul(a: int, b: int) -> int:
        return a * b

    def _echo(msg: str) -> str:
        return msg

    tools = {"add": _add, "mul": _mul, "echo": _echo}

    # 乱序计划: 列表顺序和执行顺序故意不一致
    shuffled_plan = [
        {"id": 3, "action": "echo", "args": ["下锅"], "needs": [4]},
        {"id": 1, "action": "echo", "args": ["备菜"], "needs": []},
        {"id": 4, "action": "add", "args": [2, 3], "needs": [1]},
        {"id": 2, "action": "mul", "args": [10, 4], "needs": [1]},
    ]

    def shuffled_planner(task: str) -> list[dict]:
        return shuffled_plan

    def deadlock_planner(task: str) -> list[dict]:
        return [
            {"id": 1, "action": "echo", "args": ["A"], "needs": [2]},
            {"id": 2, "action": "echo", "args": ["B"], "needs": [1]},  # 互相等 = 环
        ]

    # 测试1: validate_deps
    print(f"PASS/FAIL 合法依赖 -> {validate_deps(shuffled_plan)} | expected: True")
    missing = [{"id": 1, "action": "echo", "args": ["x"], "needs": [9]}]
    print(f"PASS/FAIL 依赖黑洞(9不存在) -> {validate_deps(missing)} | expected: False")
    selfdep = [{"id": 1, "action": "echo", "args": ["x"], "needs": [1]}]
    print(f"PASS/FAIL 自依赖 -> {validate_deps(selfdep)} | expected: False")

    # 测试2: ready_steps
    done_empty: set[int] = set()
    r = ready_steps(shuffled_plan, done_empty)
    print(f"PASS/FAIL 开局只有1就绪 -> {[s['id'] for s in r]} | expected: [1]")
    r2 = ready_steps(shuffled_plan, {1})
    print(f"PASS/FAIL 备菜后2和4就绪 -> {[s['id'] for s in r2]} | expected: [2, 4]")
    r3 = ready_steps(shuffled_plan, {1, 2, 4})
    print(f"PASS/FAIL 只剩3就绪 -> {[s['id'] for s in r3]} | expected: [3]")

    # 测试3: 乱序计划的执行顺序（引擎自己排）
    out = run_dep_plan("做菜", shuffled_planner, tools)
    print(f"PASS/FAIL 任务完成 -> {out['ok']} | expected: True")
    print(f"PASS/FAIL 执行顺序重排 -> {out['order']} | expected: [1, 2, 4, 3]")
    print(
        f"PASS/FAIL 结果按执行序 -> {out['results']} | expected: ['备菜', '40', '5', '下锅']"
    )

    # 测试4: 死锁检测（环）
    out2 = run_dep_plan("死锁任务", deadlock_planner, tools)
    print(f"PASS/FAIL 死锁被拦 -> {out2['ok']} | expected: False")
    print(f"PASS/FAIL 死锁原因 -> {out2['reason']} | expected: 依赖死锁")
    print(f"PASS/FAIL 死锁时零执行 -> {out2['order']} | expected: []")
