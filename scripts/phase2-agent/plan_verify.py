# ============================================================
# ✅ 检验题: 复杂任务能被正确分解执行（2.4 验收）
#
# 任务: "读取成绩数据 → 按权重算加权总分 → 写入报告文件"
# 难点: 三步之间有【数据依赖】——但 execute_step 各步独立、不传结果。
# 解法: 共享黑板 state（闭包可见的 dict）——
#       load 写成绩上黑板，weighted_total 取成绩算总分再写回，
#       report 取总分写文件。数据流走黑板，不走返回值。
#
# 演习剧本（考验你的完整引擎 replan_loop.run_plan_with_replan）:
#   1. planner 出 4 步计划，其中第 2 步动作名写错("wsum"，模拟计划过时)
#   2. 引擎执行: 第 1 步成功 → 第 2 步封路 → replanner 修正剩余路线
#   3. 修正后跑完全程，报告文件落盘，E2E 校验内容
#
# 你要实现 3 个工具函数（填空）:
#   1. load(scores)      成绩写上黑板，返回 "已读取N条"
#   2. weighted_total(weights)  从黑板取成绩，zip 配对算加权总分，
#                               总分写回黑板，返回 str(总分)
#   3. report(path)      从黑板取总分，写入文件(utf-8)，返回 "报告已写入"
#
# ============================================================
# 知识点: 共享黑板(步骤间数据流) | zip 拉链配对 | 生成器表达式求加权和 | 复用完整引擎 | E2E文件校验
# ============================================================
from pathlib import Path

from replan_loop import run_plan_with_replan

state: dict = {}  # 共享黑板：所有工具函数都看得见（闭包）


def load(scores: list[float]) -> str:
    """把成绩写上黑板，返回 "已读取N条\""""
    state["scores"] = scores
    return f"已读取{len(scores)}条"


def weighted_total(weights: list[float]) -> str:
    """从黑板取成绩，与权重 zip 配对算加权总分；总分写回黑板，返回 str(总分)"""
    scores = state["scores"]
    total = sum(s * w for s, w in zip(scores, weights))
    state["total"] = total
    return str(total)


def report(path: str) -> str:
    """从黑板取总分写入文件(utf-8)，返回 "报告已写入\""""
    target = Path(__file__).parent / path
    target.write_text(f"加权总分: {state['total']}", encoding="utf-8")
    return "报告已写入"


if __name__ == "__main__":
    tools = {"load": load, "weighted_total": weighted_total, "report": report}

    # 过时计划: 第 2 步动作名拼错（模拟计划过时/工具改名）
    def outdated_planner(task: str) -> list[dict]:
        return [
            {"id": 1, "action": "load", "args": [[80, 90, 100]]},
            {
                "id": 2,
                "action": "wsum",
                "args": [[0.5, 0.3, 0.2]],
            },  # ← 应为 weighted_total
            {"id": 3, "action": "report", "args": ["_verify_report.txt"]},
            {"id": 4, "action": "echo", "args": ["完成"]},
        ]

    # 修正导航: 剩余路线换成正确动作
    def fix_replanner(task: str, done: list, failed_step: dict) -> list[dict]:
        return [
            {"id": 1, "action": "weighted_total", "args": [[0.5, 0.3, 0.2]]},
            {"id": 2, "action": "report", "args": ["_verify_report.txt"]},
            {"id": 3, "action": "echo", "args": ["完成"]},
        ]

    def _echo(msg: str) -> str:
        return msg

    tools["echo"] = _echo

    # ---- E2E: 完整引擎跑复杂任务 ----
    r = run_plan_with_replan(
        "读取成绩→算加权总分→写报告", outdated_planner, fix_replanner, tools
    )

    print(f"PASS/FAIL 任务完成 -> {r['ok']} | expected: True")
    print(f"PASS/FAIL 改道1次 -> {r['replans']} | expected: 1")
    print(
        f"PASS/FAIL 执行痕迹 -> {r['results']} | expected: "
        "['已读取3条', '未知操作: wsum', '87.0', '报告已写入', '完成']"
    )

    # ---- 文件层面的最终校验 ----
    p = Path(__file__).parent / "_verify_report.txt"
    content = p.read_text(encoding="utf-8") if p.exists() else "(文件不存在)"
    print(f"PASS/FAIL 报告落盘 -> {content} | expected: 加权总分: 87.0")
    p.unlink(missing_ok=True)  # 清理
    print("E2E 完成，检验文件已清理")
