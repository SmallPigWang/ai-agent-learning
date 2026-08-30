# ============================================================
# 练习: 对比两种记忆策略的效果（滑动窗口 vs 摘要压缩）
#
# 背景: 上两次练习分别实现了滑动窗口和摘要压缩，
#       但"哪个更好"不能靠感觉——要跑对比实验，用数字说话。
#
# 对比实验设计三要素:
#   1. 控制变量: 两种策略跑【同一段】对话、用【同一个】窗口大小
#   2. 固定指标:
#      - token 占用: 裁剪后上下文还有多少 token（越少越省钱）
#      - 信息保留率: 埋进去的关键事实还剩几条能找到（越多越好）
#   3. 基线(baseline): 不裁剪的完整对话也测一遍，作对照组
#
# 你要实现:
#   1. build_dialogue(n_turns, fact_interval) -> list
#      构造 system + n_turns 轮对话（实验数据，埋好关键事实）
#      - 第 i 轮: user = "第{i}轮问题"，assistant = "好的，第{i}轮已回答"
#      - 若 i 是 fact_interval 的倍数，user 末尾追加 "，请记住关键事实{i}"
#
#   2. estimate_tokens(messages) -> int
#      （复习）每条消息 role + content 的字符数总和
#
#   3. fact_retention(context, facts) -> float
#      关键事实保留率 = 还能在上下文里找到的事实数 / 总事实数
#      - 把 context 所有 content 拼成一个大字符串再逐个查找
#      - 返回 0.0 ~ 1.0（精确到小数即可）
#
#   4. window_strategy(messages, keep_turns) -> list
#      （复习）滑动窗口: system 常驻最前 + 最近 keep_turns 轮
#
#   5. summary_strategy(messages, keep_turns, summarize) -> list
#      摘要压缩: 旧消息交给 summarize 压成一段文字，拼进 system
#      - system 常驻最前，content 变为: 原内容 + " 摘要:" + 摘要文字
#      - 后面跟最近 keep_turns 轮
#      - summarize 是回调函数: summarize(old_messages) -> str
#        （真实项目传 LLM 调用，本测试传离线的 fake_summarize）
#      - 没有旧消息时摘要为 ""，system 保持原样
#
#   6. compare_strategies(messages, facts, keep_turns, summarize) -> dict
#      汇总实验报告，格式:
#      {"full":    {"tokens": int, "retention": float},
#       "window":  {"tokens": int, "retention": float},
#       "summary": {"tokens": int, "retention": float}}
#      - full = 不裁剪的原始 messages（基线）
#
# ============================================================
# 知识点: 对比实验设计 | 控制变量 | 评价指标(token占用/信息保留率) | 基线对比 | 埋事实测记忆 | 回调函数注入 | 策略权衡
# ============================================================
from collections.abc import Callable


def build_dialogue(n_turns: int, fact_interval: int) -> list[dict]:
    """
    构造 system + n_turns 轮对话，每隔 fact_interval 轮埋一条关键事实
    返回消息列表
    """
    messages: list[dict] = [{"role": "system", "content": "你是学习助手"}]

    for i in range(1, n_turns + 1):
        user_text = f"第{i}轮问题"

        if i % fact_interval == 0:
            user_text += f",请记住关键事实{i}"

        messages.append({"role": "user", "content": user_text})
        messages.append({"role": "assistant", "content": f"好的，第{i}轮已回答"})

    return messages


def estimate_tokens(messages: list[dict]) -> int:
    """
    估算总 token 数: 每条消息 role + content 字符数总和
    """
    total = 0
    for msg in messages:
        total += len(msg["role"])
        total += len(msg["content"])

    return total


def fact_retention(context: list[dict], facts: list[str]) -> float:
    """
    计算关键事实保留率: 能在上下文中找到的事实数 / 总事实数
    把所有 content 拼成大字符串后逐个查找，返回 0.0 ~ 1.0
    """
    big_text = " ".join(m["content"] for m in context)
    found = 0
    for fact in facts:
        if fact in big_text:
            found += 1
    return found / len(facts)


def window_strategy(messages: list[dict], keep_turns: int) -> list[dict]:
    """
    滑动窗口策略: system 常驻最前 + 最近 keep_turns 轮（keep_turns*2 条）
    返回新列表，不修改原列表
    """
    system_msg = None
    rest = messages
    if messages and messages[0].get("role") == "system":
        system_msg = messages[0]
        rest = messages[1:]

    recent = rest[-keep_turns * 2 :]
    if system_msg is not None:
        return [system_msg] + recent

    return recent


def summary_strategy(
    messages: list[dict], keep_turns: int, summarize: Callable[[list[dict]], str]
) -> list[dict]:
    """
    摘要压缩策略: 旧消息交给 summarize(old_messages) 压成摘要文字，
    拼进 system（原内容 + " 摘要:" + 摘要），再跟最近 keep_turns 轮
    没有旧消息时摘要为 ""，system 保持原样
    """
    system_msg = None
    rest = messages

    if messages and messages[0].get("role") == "system":
        system_msg = messages[0]
        rest = messages[1:]

    keep_count = keep_turns * 2
    if len(rest) <= keep_count:
        return [system_msg] + rest if system_msg else rest

    old = rest[: len(rest) - keep_count]
    recent = rest[-keep_count:]

    summary = summarize(old)
    # 断言输入的前提：走到这里 system_msg 必须存在（也让类型检查器收窄类型）
    assert system_msg is not None
    merged = dict(system_msg)
    merged["content"] = merged["content"] + " 摘要：" + summary

    return [merged] + recent


def compare_strategies(
    messages: list[dict],
    facts: list[str],
    keep_turns: int,
    summarize: Callable[[list[dict]], str],
) -> dict[str, dict[str, float | int]]:
    """
    跑三种情形并汇总报告: full(基线) / window(滑动窗口) / summary(摘要压缩)
    每种情形测两个指标: tokens(token 占用) + retention(信息保留率)
    """
    report = {}
    for name, ctx in [
        ("full", messages),
        ("window", window_strategy(messages=messages, keep_turns=keep_turns)),
        (
            "summary",
            summary_strategy(
                messages=messages, keep_turns=keep_turns, summarize=summarize
            ),
        ),
    ]:
        report[name] = {
            "tokens": estimate_tokens(ctx),
            "retention": fact_retention(context=ctx, facts=facts),
        }

    return report


if __name__ == "__main__":
    # 离线摘要器（测试脚手架，已写好，不用动）:
    # 模拟 LLM 摘要——只保留含"关键事实"的要点消息，丢弃闲聊（有损压缩）
    def fake_summarize(old_messages: list[dict]) -> str:
        keep = [m["content"] for m in old_messages if "关键事实" in m["content"]]
        return "；".join(keep)

    # --- 实验数据: 20 轮对话，每 5 轮埋 1 条关键事实（共 4 条） ---
    msgs = build_dialogue(20, 5)
    facts = [f"关键事实{i}" for i in (5, 10, 15, 20)]

    # 测试1: build_dialogue 数据构造
    print(f"PASS/FAIL 总条数(system+20轮) -> {len(msgs)} | expected: 41")
    print(f"PASS/FAIL 第一条是system -> {msgs[0]['role']} | expected: system")
    fact_count = len([m for m in msgs if "关键事实" in m["content"]])
    print(f"PASS/FAIL 埋了4条事实 -> {fact_count} | expected: 4")
    # 断言只验证意图（第20轮问题 + 事实20），不耦合标点全角/半角细节
    last_user = msgs[-2]["content"]
    ok = last_user.startswith("第20轮问题") and "关键事实20" in last_user
    print(f"PASS/FAIL 第20轮user含事实20(标点不敏感) -> {ok} | expected: True")

    # 测试2: estimate_tokens（复习）
    t = estimate_tokens([{"role": "user", "content": "你好"}])
    print(f"PASS/FAIL token估算 -> {t} | expected: 6")

    # 测试3: fact_retention
    ctx = [
        {"role": "system", "content": "你是助手"},
        {"role": "user", "content": "记得A和C"},
        {"role": "assistant", "content": "好的"},
    ]
    print(
        f"PASS/FAIL 保留率2/4 -> {fact_retention(ctx, ['A', 'B', 'C', 'D'])} | expected: 0.5"
    )
    print(f"PASS/FAIL 全丢保留率 -> {fact_retention(ctx, ['X', 'Y'])} | expected: 0.0")

    # 测试4: window_strategy（窗口 3 轮 → 只剩事实20）
    w = window_strategy(msgs, 3)
    print(f"PASS/FAIL 窗口条数 -> {len(w)} | expected: 7")
    print(f"PASS/FAIL system在前 -> {w[0]['role']} | expected: system")
    print(
        f"PASS/FAIL 窗口保留率(只剩事实20) -> {fact_retention(w, facts)} | expected: 0.25"
    )

    # 测试5: summary_strategy（旧轮事实5/10/15 进摘要）
    s = summary_strategy(msgs, 3, fake_summarize)
    print(f"PASS/FAIL 摘要版条数 -> {len(s)} | expected: 7")
    print(f"PASS/FAIL 第一条是system -> {s[0]['role']} | expected: system")
    print(f"PASS/FAIL system含摘要 -> {'摘要' in s[0]['content']} | expected: True")
    print(
        f"PASS/FAIL 旧事实5进摘要 -> {'关键事实5' in s[0]['content']} | expected: True"
    )
    print(f"PASS/FAIL 摘要版保留率(4/4) -> {fact_retention(s, facts)} | expected: 1.0")

    # 测试6: 没有旧消息时摘要为空、system 不变
    s2 = summary_strategy(msgs[:5], 2, fake_summarize)
    print(f"PASS/FAIL 无旧消息条数 -> {len(s2)} | expected: 5")
    print(
        f"PASS/FAIL 无旧消息不改system -> {'摘要' not in s2[0]['content']} | expected: True"
    )

    # 测试7: compare_strategies 实验报告
    report = compare_strategies(msgs, facts, 3, fake_summarize)
    print(f"PASS/FAIL 基线保留率 -> {report['full']['retention']} | expected: 1.0")
    print(f"PASS/FAIL 窗口保留率 -> {report['window']['retention']} | expected: 0.25")
    print(f"PASS/FAIL 摘要保留率 -> {report['summary']['retention']} | expected: 1.0")
    print(
        f"PASS/FAIL 窗口最省token -> {report['window']['tokens'] < report['summary']['tokens']} | expected: True"
    )
    print(
        f"PASS/FAIL 摘要比基线省 -> {report['summary']['tokens'] < report['full']['tokens']} | expected: True"
    )

    # --- 实验报告（肉眼可见的权衡） ---
    print("\n===== 记忆策略对比实验报告（窗口=3轮, 20轮对话, 4条关键事实） =====")
    for name in ("full", "window", "summary"):
        m = report[name]
        print(f"{name:8s} | tokens: {m['tokens']:5d} | 保留率: {m['retention']}")
