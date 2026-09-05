# ============================================================
# 练习: 对比开/关反思的质量和成本（2.5 第二步）
#
# 方法论: 和 2.3 记忆策略对比实验同款——
#   控制变量(同一套约束/同一个生成器剧本) + 指标(质量ok/成本calls) + 两对照组
#
# 两组:
#   裸奔组(基线): 不反思，一稿定生死 → calls 恒为 1
#   反思组(实验): run_reflection 循环 → calls = rounds（真 LLM 场景=真金白银）
#
# 三个剧本(生成器工厂，每次调用产一个全新生成器):
#   easy      永远一稿过        → 反思没机会上场
#   slow      前两稿烂第三稿好  → 反思花 2 次调用买回合格(赚)
#   hopeless  永远不合格        → 反思烧完预算纯亏 2 次
#
# 你要实现:
#   1. no_reflection_attempt(generator, must_include, max_len, forbidden) -> dict
#      裸奔模式: generator("") 生成一稿 → check_slogan 评一次
#      返回 {"ok": 是否合格, "calls": 1, "slogan": 这稿, "problems": 问题清单}
#
#   2. compare_modes(factory, must_include, max_len, forbidden) -> dict
#      对比实验: 同一个工厂，裸奔/反思各跑一遍(注意: 各要一个【全新】生成器)
#      返回 {"no_reflection": {"ok", "calls", "problems"},
#            "with_reflection": {"ok", "calls", "problems"}}
#      - 反思组复用 run_reflection（import 进来），calls = rounds
#      - 两组的 problems 都取"最后一轮的问题清单"
#        (反思组的 run_reflection 返回里，哪个字段装着每轮问题清单？取最后一个)
#
# ============================================================
# 知识点: 成本效益实验 | 对照组设计(基线/实验) | 工厂模式(每实验一个新生成器) | calls作为成本代理 | 复用反思引擎
# ============================================================
from reflection_loop import check_slogan, run_reflection


def no_reflection_attempt(
    generator, must_include: list[str], max_len: int, forbidden: list[str]
) -> dict:
    """裸奔模式: 不反思，一稿定生死，calls 恒为 1"""
    slogan = generator("")
    problems = check_slogan(slogan, must_include, max_len, forbidden)
    return {
        "ok": not problems,  # 问题清单空 = 合格（怎么把空列表变 bool）
        "calls": 1,
        "slogan": slogan,
        "problems": problems,
    }


def compare_modes(
    factory, must_include: list[str], max_len: int, forbidden: list[str]
) -> dict:
    """对比实验: 同一工厂，裸奔组/反思组各跑一遍全新生成器"""
    plain = no_reflection_attempt(factory(), must_include, max_len, forbidden)
    r = run_reflection(factory(), must_include, max_len, forbidden)

    return {
        "no_reflection": {"ok": plain["ok"], "calls": 1, "problems": plain["problems"]},
        "with_reflection": {
            "ok": r["ok"],
            "calls": r["rounds"],  # 成本 = 用了几轮
            "problems": r["problems_history"][-1],
        },
    }


if __name__ == "__main__":
    # ---- 三个生成器剧本（工厂，已写好，不用动）----

    def easy_factory():
        def generator(note: str) -> str:
            return "AI助手"  # 永远一稿过

        return generator

    def slow_factory():
        calls = ["免费大甩卖", "免费AI助手", "AI助手"]  # 第三稿才合格

        def generator(note: str) -> str:
            return calls.pop(0) if calls else "AI助手"

        return generator

    def hopeless_factory():
        def generator(note: str) -> str:
            return "便宜货"  # 永远缺关键词

        return generator

    MUST, MAX_LEN, FORBID = ["AI"], 8, ["免费"]

    # 测试1: no_reflection_attempt 裸奔模式
    a1 = no_reflection_attempt(easy_factory(), MUST, MAX_LEN, FORBID)
    print(f"PASS/FAIL 裸奔一稿过 -> {a1['ok']} | expected: True")
    print(f"PASS/FAIL 裸奔成本恒1 -> {a1['calls']} | expected: 1")
    a2 = no_reflection_attempt(slow_factory(), MUST, MAX_LEN, FORBID)
    print(f"PASS/FAIL 裸奔撞烂稿 -> {a2['ok']} | expected: False")
    print(
        f"PASS/FAIL 裸奔烂稿问题 -> {a2['problems']} | expected: ['缺少关键词: AI', '含违禁词: 免费']"
    )

    # 测试2: compare_modes 三剧本对比
    e = compare_modes(easy_factory, MUST, MAX_LEN, FORBID)
    print(
        f"PASS/FAIL easy两组合格 -> {e['no_reflection']['ok'] and e['with_reflection']['ok']} | expected: True"
    )
    print(f"PASS/FAIL easy反思没上场 -> {e['with_reflection']['calls']} | expected: 1")

    s = compare_modes(slow_factory, MUST, MAX_LEN, FORBID)
    print(f"PASS/FAIL slow裸奔挂 -> {s['no_reflection']['ok']} | expected: False")
    print(f"PASS/FAIL slow反思救回 -> {s['with_reflection']['ok']} | expected: True")
    print(f"PASS/FAIL slow反思成本3 -> {s['with_reflection']['calls']} | expected: 3")

    h = compare_modes(hopeless_factory, MUST, MAX_LEN, FORBID)
    print(
        f"PASS/FAIL hopeless全挂 -> {not h['no_reflection']['ok'] and not h['with_reflection']['ok']} | expected: True"
    )
    print(
        f"PASS/FAIL hopeless反思白烧3 -> {h['with_reflection']['calls']} | expected: 3"
    )

    # ---- 成本效益结论表（肉眼判读） ----
    print("\n===== 反思成本效益实验报告 =====")
    for name, exp in (("easy", e), ("slow", s), ("hopeless", h)):
        n, w = exp["no_reflection"], exp["with_reflection"]
        verdict = (
            "反思白设"
            if n["ok"] and w["ok"]
            else ("反思赚了" if w["ok"] else "反思纯亏")
        )
        print(
            f"{name:9s} | 裸奔: ok={n['ok']} calls=1 | 反思: ok={w['ok']} calls={w['calls']} | {verdict}"
        )
