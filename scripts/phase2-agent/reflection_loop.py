# ============================================================
# 练习: 给 Agent 加自反思（2.5 第一步）
#
# 任务: 生成合格的产品标语——直到通过批评家安检或预算用尽
#
# 反思循环:
#   生成(generator) -> 自评(critic 挑问题) -> 反思(问题变便签)
#   -> 带着便签再生成 -> ...  问题清单空了 = 过关
#
# 三个角色:
#   generator(slogan 无关，吃"反思便签"返回新标语)  ← 回调，测试用脚本化 fake
#   check_slogan(...)  批评家: 硬规则挑毛病，[] = 合格  ← 你写，真逻辑
#   build_reflection(...) 把问题清单翻译成便签喂回 generator ← 你写
#
# 你要实现:
#   1. check_slogan(slogan, must_include, max_len, forbidden) -> list[str]
#      批评家（安检闸门第 N 次复用），返回问题清单，空 = 合格:
#      - 缺了必须包含的关键词 -> "缺少关键词: {word}"
#      - 长度超上限           -> "超长: {实际长度}/{max_len}"
#      - 含违禁词             -> "含违禁词: {word}"
#
#   2. build_reflection(problems) -> str
#      问题清单 -> 反思便签: "反思: 问题1; 问题2"（; 分隔）
#      空清单 -> ""
#
#   3. run_reflection(generator, must_include, max_len, forbidden, max_rounds=3) -> dict
#      反思引擎:
#      note = "" 起步
#      循环最多 max_rounds 轮:
#        slogan = generator(note)                  ← 带着便签生成
#        problems = check_slogan(...)              ← 自评
#        记录 attempts / problems_history
#        problems 为空 -> {"ok": True, "rounds": 用了几轮,
#                         "attempts": [...], "problems_history": [...]}
#        否则 note = build_reflection(problems) 进入下一轮
#      预算用完仍不合格 ->
#        {"ok": False, "rounds": max_rounds, "attempts": [...],
#         "problems_history": [...], "last_problems": 最后一轮的问题}
#
# ============================================================
# 知识点: 反思循环(生成→自评→改进) | 批评家=规则代码(免费确定) | 反思便签=工作记忆 | 预算(max_rounds) | 问题清单即数据 | 回调注入
# ============================================================


def check_slogan(
    slogan: str, must_include: list[str], max_len: int, forbidden: list[str]
) -> list[str]:
    """批评家: 硬规则挑毛病，返回问题清单，空列表 = 合格"""
    problems: list[str] = []

    for word in must_include:
        if word not in slogan:
            problems.append(f"缺少关键词: {word}")

    if len(slogan) > max_len:
        problems.append(f"超长: {len(slogan)}/{max_len}")

    for word in forbidden:
        if word in slogan:
            problems.append(f"含违禁词: {word}")

    return problems


def build_reflection(problems: list[str]) -> str:
    """问题清单 -> 反思便签 "反思: p1; p2"；空清单 -> """ ""
    if not problems:
        return ""
    return "反思: " + "; ".join(problems)


def run_reflection(
    generator,
    must_include: list[str],
    max_len: int,
    forbidden: list[str],
    max_rounds: int = 3,
) -> dict:
    """反思引擎: 带便签生成 → 自评 → 过关收工 / 不过关反思再来，预算用尽失败返回"""
    attempts: list[str] = []
    problems_history: list[list[str]] = []
    note = ""

    for round_no in range(1, max_rounds + 1):
        slogan = generator(note)
        problems = check_slogan(
            slogan=slogan,
            must_include=must_include,
            max_len=max_len,
            forbidden=forbidden,
        )

        attempts.append(slogan)
        problems_history.append(problems)

        if not problems:
            return {
                "ok": True,
                "rounds": round_no,  # ⑤ 用了几轮
                "attempts": attempts,
                "problems_history": problems_history,
            }

        note = build_reflection(problems)

    # 预算用尽仍不合格——失败也要带着全部现场返回
    return {
        "ok": False,
        "rounds": max_rounds,
        "attempts": attempts,
        "problems_history": problems_history,
        "last_problems": problems_history[-1],
    }  # ⑦ 最后一轮的问题


if __name__ == "__main__":
    # ---- 测试脚手架（已写好，不用动）----

    # 脚本化生成器: 前两次交烂稿，第三次交合格稿（闭包计数，黑板模式）
    def make_scripted_generator():
        calls: list[str] = ["免费大甩卖", "免费AI助手", "AI助手"]

        def generator(note: str) -> str:
            return calls.pop(0) if calls else "AI助手"

        return generator

    def always_bad_generator(note: str) -> str:
        return "便宜货"  # 永远缺关键词，永不合格

    # 测试1: check_slogan 批评家
    ok = check_slogan("AI助手", ["AI"], 8, ["免费"])
    print(f"PASS/FAIL 合格 -> {ok} | expected: []")
    p1 = check_slogan("免费大甩卖", ["AI"], 8, ["免费"])
    print(
        f"PASS/FAIL 缺关键词+违禁 -> {p1} | expected: ['缺少关键词: AI', '含违禁词: 免费']"
    )
    p2 = check_slogan("超级无敌AI智能助手帮手", ["AI"], 8, [])
    print(f"PASS/FAIL 超长 -> {p2} | expected: ['超长: 12/8']")
    p3 = check_slogan("免费AI", ["AI"], 8, ["免费"])
    print(f"PASS/FAIL 违禁 -> {p3} | expected: ['含违禁词: 免费']")

    # 测试2: build_reflection 便签
    print(
        f"PASS/FAIL 便签格式 -> {build_reflection(['缺A', '超长'])} | expected: 反思: 缺A; 超长"
    )
    print(f"PASS/FAIL 空清单 -> {build_reflection([])} | expected: (空字符串)")

    # 测试3: 反思引擎——第三次过关
    r1 = run_reflection(make_scripted_generator(), ["AI"], 8, ["免费"])
    print(f"PASS/FAIL 最终过关 -> {r1['ok']} | expected: True")
    print(f"PASS/FAIL 用了3轮 -> {r1['rounds']} | expected: 3")
    print(
        f"PASS/FAIL 三稿记录 -> {r1['attempts']} | expected: ['免费大甩卖', '免费AI助手', 'AI助手']"
    )
    print(
        f"PASS/FAIL 问题递减 -> {[len(p) for p in r1['problems_history']]} | expected: [2, 1, 0]"
    )

    # 测试4: 永不合格——预算用尽，失败返回
    r2 = run_reflection(always_bad_generator, ["AI"], 8, ["免费"], max_rounds=3)
    print(f"PASS/FAIL 预算用尽 -> {r2['ok']} | expected: False")
    print(f"PASS/FAIL 试满3轮 -> {r2['rounds']} | expected: 3")
    print(
        f"PASS/FAIL 最后的问题 -> {r2['last_problems']} | expected: ['缺少关键词: AI']"
    )
