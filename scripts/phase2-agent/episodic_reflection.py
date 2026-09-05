# ============================================================
# 🧩 独立挑战题: 跨试次情景记忆（2.5 验收三件套之二）
#
# 背景: reflection_loop 的 note 只能活在【一个任务内】——
#       反思循环跑完就丢。Reflexion 论文的 episodic memory 能把
#       任务A的教训带进任务B的开局。本题主补这个差距。
#
# 设计 = Day 7 长期记忆(落盘) + Day 8 反思(便签) 的组合:
#   任务结束(无论成败) → 提炼一条"教训"(lesson) → json 落盘
#   新任务开局 → 读盘 → 反思便签 = 过往教训 + 本轮问题
#
# 契约（题目的一部分）:
#   - note 拼接规则: 有历史教训时，note 以 "过往教训: " 开头，
#     后接 '; '.join(教训们)；每轮失败后再追加本轮反思
#     (测试的 smart 生成器靠 "过往教训" 四个字识别"我有经验"）
#   - lesson 格式:
#       成功 -> f"{task}: 通过, 用{rounds}轮"
#       失败 -> f"{task}: 失败, 问题: {'; '.join(最后一轮问题)}"
#   - 落盘: json / utf-8 / indent=2（老三件套），内容是字符串列表
#   - 容错: 缺文件、坏 json 都返回 []
#
# 你要实现:
#   1. load_lessons(filepath) -> list[str]
#      读教训库（json 字符串列表）；缺文件/坏 json -> []
#
#   2. save_lesson(filepath, lesson) -> None
#      追加一条教训并落盘（读旧 + append + 写回）
#
#   3. run_task_with_memory(task, generator, must_include, max_len,
#                          forbidden, lessons, max_rounds=3) -> dict
#      带情景记忆的反思引擎:
#      a. prefix = 有教训 ? "过往教训: " + '; '.join(lessons) : ""
#         note 起步 = prefix
#      b. 反思循环（骨架同 reflection_loop，复用 check_slogan/
#         build_reflection，from reflection_loop import）:
#         每轮 slogan=generator(note) -> 自评 -> 记录
#         过关 -> 成功返回 + lesson 按成功格式
#         不过 -> note = prefix(若有) + 本轮反思(build_reflection)
#      c. 预算尽 -> 失败返回 + lesson 按失败格式
#      返回: {"ok", "rounds", "attempts", "problems_history", "lesson"}
#
# ============================================================
# 知识点: （挑战题不预习——通关后教练揭晓）
# ============================================================
import json

from reflection_loop import build_reflection, check_slogan


def load_lessons(filepath: str) -> list[str]:
    """读教训库(json 字符串列表)；缺文件/坏 json -> []"""
    try:
        with open(filepath, encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_lesson(filepath: str, lesson: str) -> None:
    """追加一条教训并落盘（读旧 + append + 写回）"""
    lessons = load_lessons(filepath)
    lessons.append(lesson)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(lessons, f, ensure_ascii=False, indent=2)


def run_task_with_memory(
    task: str,
    generator,
    must_include: list[str],
    max_len: int,
    forbidden: list[str],
    lessons: list[str],
    max_rounds: int = 3,
) -> dict:
    """带情景记忆的反思引擎: 教训进便签、结束时提炼 lesson"""

    prefix = "过往教训: " + "; ".join(lessons) if lessons else ""
    note = prefix
    attempts: list[str] = []
    problems_history: list[list[str]] = []

    for round_no in range(1, max_rounds + 1):
        slogan = generator(note)
        problems = check_slogan(slogan, must_include, max_len, forbidden)
        attempts.append(slogan)
        problems_history.append(problems)

        if not problems:
            return {
                "ok": True,
                "rounds": round_no,
                "attempts": attempts,
                "problems_history": problems_history,
                "lesson": f"{task}: 通过, 用{round_no}轮",
            }

        note = prefix + ("; " if prefix else "") + build_reflection(problems)

    return {
        "ok": False,
        "rounds": max_rounds,
        "attempts": attempts,
        "problems_history": problems_history,
        "lesson": f"{task}: 失败, 问题: {'; '.join(problems_history[-1])}",
    }


if __name__ == "__main__":
    from pathlib import Path

    # 慢机器: 不管便签写啥，按剧本交稿（3轮才过）
    # 剧本必须放函数体外（闭包）——放体内会每次调用重发新剧本，永远交第一稿
    slow_calls = ["免费大甩卖", "免费AI助手", "AI助手"]

    def slow_gen(note: str) -> str:
        return slow_calls.pop(0) if slow_calls else "AI助手"

    # 智能机器: 看到便签里有"过往教训"就直接交合格稿，否则交烂稿
    def smart_gen(note: str) -> str:
        return "AI助手" if "过往教训" in note else "免费大甩卖"

    MUST, MAX_LEN, FORBID = ["AI"], 8, ["免费"]
    tmp = str(Path(__file__).parent / "_lessons_test.json")

    # 测试1: load_lessons 容错
    Path(tmp).unlink(missing_ok=True)
    print(f"PASS/FAIL 缺文件 -> {load_lessons(tmp)} | expected: []")
    Path(tmp).write_text("}}}坏的", encoding="utf-8")
    print(f"PASS/FAIL 坏json -> {load_lessons(tmp)} | expected: []")
    Path(tmp).unlink(missing_ok=True)

    # 测试2: save_lesson 追加落盘
    save_lesson(tmp, "第一条")
    save_lesson(tmp, "第二条")
    print(f"PASS/FAIL 追加两条 -> {load_lessons(tmp)} | expected: ['第一条', '第二条']")

    # 测试3: 无教训的任务A（慢机器 3 轮）
    ra = run_task_with_memory("任务A", slow_gen, MUST, MAX_LEN, FORBID, [])
    print(f"PASS/FAIL 任务A通过 -> {ra['ok']} | expected: True")
    print(f"PASS/FAIL 任务A用了3轮 -> {ra['rounds']} | expected: 3")
    print(f"PASS/FAIL 任务A的lesson -> {ra['lesson']} | expected: 任务A: 通过, 用3轮")
    print(
        f"PASS/FAIL 任务A便签无教训前缀 -> {ra['attempts'][0]} | expected: 免费大甩卖"
    )

    # 测试4: E2E 跨试次——教训落盘，任务B开局带记忆
    save_lesson(tmp, ra["lesson"])
    lessons_b = load_lessons(tmp)
    rb = run_task_with_memory("任务B", smart_gen, MUST, MAX_LEN, FORBID, lessons_b)
    print(f"PASS/FAIL 任务B通过 -> {rb['ok']} | expected: True")
    print(f"PASS/FAIL 任务B只要1轮 -> {rb['rounds']} | expected: 1")  # ← 灵魂断言
    print(f"PASS/FAIL 任务B一稿就好 -> {rb['attempts']} | expected: ['AI助手']")
    print(f"PASS/FAIL 任务B的lesson -> {rb['lesson']} | expected: 任务B: 通过, 用1轮")

    # 测试5: 反证——没有教训时智能机器照样交烂稿起跑
    rc = run_task_with_memory("任务C", smart_gen, MUST, MAX_LEN, FORBID, [])
    print(
        f"PASS/FAIL 无记忆任务C首轮烂稿 -> {rc['attempts'][0]} | expected: 免费大甩卖"
    )
    Path(tmp).unlink(missing_ok=True)
