# ============================================================
# 练习: 动态重规划 —— 计划赶不上变化时，就地改道（2.4 第二步）
#
# 背景: run_plan 是静态引擎——计划某步失败（未知操作），
#       引擎要么带着伤疤继续，要么干瞪眼。真实世界计划会过时:
#       文件被移走、API 改版、依赖的中间结果不符合预期。
#       动态重规划 = 执行中受阻 → 让 replanner 生成"剩余工作的新计划"
#       → 安检 → 从新计划第一步继续。
#
# 类比: 车载导航——封路就地重算剩余路线，不从家重新出发。
#
# 复用昨天的零件（同目录 import 自己的模块，今天的新操作）:
#   from plan_and_execute import validate_plan, execute_step
#
# 你要实现:
#   1. is_failed(result) -> bool
#      故障检测: 结果以 "未知操作" 开头 → True（昨天的降级消息=今天的信号）
#
#   2. run_plan_with_replan(task, planner, replanner, tools, max_replans=2) -> dict
#      带重规划的完整引擎:
#      a. plan = planner(task)，不过安检 -> {"ok": False, "reason": "计划不合法",
#                                            "results": [], "replans": 0}
#      b. 从头逐步执行 execute_step，while i < len(plan):
#         - 结果正常 -> 记入 results，i 前进
#         - 结果失败(is_failed):
#           * 重规划预算用完(replans >= max_replans) ->
#             记入失败痕迹，返回 {"ok": False, "reason": "重规划次数用尽",
#                                  "results": results, "replans": replans}
#           * 让 replanner(task, results, plan[i]) 出新计划
#             新计划不过安检 -> 记入失败痕迹，返回
#             {"ok": False, "reason": "重规划后的计划不合法", "results": results,
#              "replans": replans + 1}
#             新计划合法 -> 失败痕迹记入 results，plan 换成新计划，
#             replans + 1，i 归零，继续
#      c. 全部跑完 -> {"ok": True, "task": task, "steps": len(results),
#                      "results": results, "replans": replans}
#
# ============================================================
# 知识点: 动态重规划 | 触发信号(降级消息复用) | 只重规划剩余部分 | 重规划预算(防死循环) | while索引循环 | import自己的模块 | 回调再+1(replanner)
# ============================================================
from plan_and_execute import execute_step, validate_plan


def is_failed(result: str) -> bool:
    """故障检测: 结果以"未知操作"开头即失败（昨天的降级消息=今天的信号）"""
    # 优雅降级的产出 = 上游系统的输入：execute_step 遇到没登记的动作时
    # 不崩溃而是返回"未知操作: xxx"，这条消息今天被当作重规划的触发信号
    return result.startswith("未知操作")


def run_plan_with_replan(
    task: str, planner, replanner, tools: dict, max_replans: int = 2
) -> dict:
    """带重规划预算的执行引擎: 受阻→重算剩余→继续；预算用尽或新计划非法则终止"""

    # ---- a. 初次规划 + 安检：脏计划进不了引擎（复用今早的 validate_plan）----
    plan = planner(task)

    if not validate_plan(plan):
        return {"ok": False, "reason": "计划不合法", "results": [], "replans": 0}

    # ---- b. 执行循环 ----
    # 用 while 而不是 for：plan 可能在循环中途被整个换掉（重规划），
    # for 在开跑时就锁死了迭代对象，while + 手动索引才能边跑边换地图
    results: list[str] = []  # 全程执行痕迹，失败也记录——审计时能看到在哪改的道
    replans = 0  # 已用掉的重规划次数（预算计数器）
    i = 0  # 当前执行到计划的第几步

    while i < len(plan):
        result = execute_step(step=plan[i], tools=tools)  # 执行当前步（优雅降级，不崩）

        if is_failed(result=result):  # —— 此路不通（封路了）——
            if replans >= max_replans:
                # 预算用尽：庸医 replanner 越改越错时会无限变道烧钱，
                # 所以强制收车——和 ReAct 的 max_iterations 同一个思想
                results.append(result)  # 最后一道失败痕迹也留下
                return {
                    "ok": False,
                    "reason": "重规划次数用尽",
                    "results": results,
                    "replans": replans,
                }

            # 预算内：让 replanner 重算【剩余路线】——
            # 传三个参数让它知情决策：任务是什么 / 已完成什么 / 卡在哪一步
            new_plan = replanner(task, results, plan[i])

            if not validate_plan(new_plan):
                # 换出来的新地图也必须合法——校验器对谁都一视同仁
                results.append(result)
                return {
                    "ok": False,
                    "reason": "重规划后的计划不合法",
                    "results": results,
                    "replans": replans + 1,
                }

            # 改道三连：留痕 → 换地图 → 从新计划第一步重开
            # 注意已完成的结果不回滚——导航改道不会让你开回出发点
            results.append(result)  # 失败痕迹（审计用）
            plan = new_plan  # 换地图
            replans += 1  # 消耗一次预算
            i = 0  # 从新计划的第一步继续
            continue

        # —— 正常路况：记录结果，前进到下一步 ——
        results.append(result)
        i += 1

    # ---- c. 跑完全程，汇总报告（replans 让调用方看到改了几次道）----
    return {
        "ok": True,
        "task": task,
        "steps": len(results),
        "results": results,
        "replans": replans,
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

    # 干净计划: 顺利跑完
    def clean_planner(task: str) -> list[dict]:
        return [
            {"id": 1, "action": "add", "args": [1, 2]},
            {"id": 2, "action": "echo", "args": ["完成"]},
        ]

    # 过时计划: 第 2 步的动作不存在（模拟计划过时）
    def outdated_planner(task: str) -> list[dict]:
        return [
            {"id": 1, "action": "add", "args": [2, 3]},
            {"id": 2, "action": "fly", "args": [1]},  # ← 封路了
            {"id": 3, "action": "echo", "args": ["完成"]},
        ]

    # 好导航: 换一条能走的剩余路线
    def good_replanner(task: str, done: list, failed_step: dict) -> list[dict]:
        return [
            {"id": 1, "action": "mul", "args": [10, 4]},
            {"id": 2, "action": "echo", "args": ["完成"]},
        ]

    # 庸医: 开出的还是封的那条路
    def stubborn_replanner(task: str, done: list, failed_step: dict) -> list[dict]:
        return [{"id": 1, "action": "fly", "args": [1]}]

    # 江湖郎中: 开出的计划本身不合法（id 不从 1 开始）
    def bad_replanner(task: str, done: list, failed_step: dict) -> list[dict]:
        return [{"id": 5, "action": "echo", "args": ["x"]}]

    # 测试1: is_failed 故障检测
    print(f"PASS/FAIL 未知操作算失败 -> {is_failed('未知操作: fly')} | expected: True")
    print(f"PASS/FAIL 数字结果不算 -> {is_failed('5')} | expected: False")
    print(f"PASS/FAIL 普通文本不算 -> {is_failed('完成')} | expected: False")

    # 测试2: 全程顺畅，不触发重规划
    r1 = run_plan_with_replan("干净任务", clean_planner, good_replanner, tools)
    print(f"PASS/FAIL 顺畅ok -> {r1['ok']} | expected: True")
    print(f"PASS/FAIL 顺畅零重规划 -> {r1['replans']} | expected: 0")
    print(f"PASS/FAIL 顺畅结果 -> {r1['results']} | expected: ['3', '完成']")

    # 测试3: 受阻→重规划→继续到终点
    r2 = run_plan_with_replan("过时计划任务", outdated_planner, good_replanner, tools)
    print(f"PASS/FAIL 改道后ok -> {r2['ok']} | expected: True")
    print(f"PASS/FAIL 重规划1次 -> {r2['replans']} | expected: 1")
    print(
        f"PASS/FAIL 失败痕迹保留 -> {r2['results']} | expected: ['5', '未知操作: fly', '40', '完成']"
    )

    # 测试4: 庸医replanner → 预算用尽强制终止
    r3 = run_plan_with_replan(
        "过时计划任务", outdated_planner, stubborn_replanner, tools
    )
    print(f"PASS/FAIL 预算用尽ok为False -> {r3['ok']} | expected: False")
    print(f"PASS/FAIL 终止原因 -> {r3['reason']} | expected: 重规划次数用尽")
    print(f"PASS/FAIL 预算2次 -> {r3['replans']} | expected: 2")
    print(
        f"PASS/FAIL 三条失败痕迹 -> {r3['results'].count('未知操作: fly')} | expected: 3"
    )

    # 测试5: 新计划不合法 → 立即终止
    r4 = run_plan_with_replan("过时计划任务", outdated_planner, bad_replanner, tools)
    print(f"PASS/FAIL 非法新计划被拦 -> {r4['ok']} | expected: False")
    print(f"PASS/FAIL 拦截原因 -> {r4['reason']} | expected: 重规划后的计划不合法")
    print(
        f"PASS/FAIL 失败痕迹在 -> {'未知操作: fly' in r4['results']} | expected: True"
    )
