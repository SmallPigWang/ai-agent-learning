# ============================================================
# 练习: 滑动窗口记忆
#
# 背景: 对话越来越长 → messages 越来越长 → 上下文窗口塞满就崩。
#       滑动窗口策略: 只保留最近 max_turns 轮对话，老的丢弃。
#       但 system 消息（宪法/身份）必须永远保留——常驻第一条。
#
# 术语:
#   - 消息: 一个 dict，如 {"role": "user", "content": "..."}
#   - 轮(turn): 一次完整问答 = 1 条 user + 1 条 assistant（成对）
#   - 窗口: 保留的最近 N 轮
#
# 你要实现:
#   1. trim_history(messages, max_turns) -> list
#      裁剪消息列表，只保留 system 消息 + 最近 max_turns 轮
#      - system 消息可能有也可能没有；有则保留且在最前面
#      - 不足 max_turns 轮时原样返回（不裁剪）
#      - 返回新列表，不能修改原列表
#
#   2. add_turn(messages, user_text, assistant_text, max_turns) -> list
#      添加一轮新对话（user + assistant），然后自动按窗口裁剪
#      - 复用 trim_history 实现
#
#   3. estimate_tokens(messages) -> int
#      粗略估算总 token 数: 每条消息的 role 和 content 字段字符数相加
#      （1 字符 ≈ 1 token，够用就行，不追求精确）
#
# ============================================================
# 知识点: 滑动窗口策略 | system 常驻豁免 | 列表切片 | 轮(turn)成对 | 上下文窗口限制
# ============================================================


def trim_history(messages: list[dict], max_turns: int) -> list[dict]:
    """
    只保留 system 消息 + 最近 max_turns 轮对话
    1 轮 = 1 条 user + 1 条 assistant
    """
    system_msg: dict | None = None
    rest = messages

    # 剔除system信息单独拿出
    if messages and messages[0].get("role") == "system":
        system_msg = messages[0]
        rest = messages[1:]

    # 最近的max_turn轮信息
    recent = rest[-2 * max_turns :]

    if system_msg is not None:
        return [system_msg] + recent

    return recent


def add_turn(
    messages: list[dict], user_text: str, assistant_text: str, max_turns: int
) -> list[dict]:
    """
    添加一轮对话（user + assistant），并裁剪到窗口大小
    返回新的消息列表
    """
    new_messages = messages + [
        {"role": "user", "content": user_text},
        {"role": "assistant", "content": assistant_text},
    ]

    return trim_history(new_messages, max_turns)


def estimate_tokens(messages: list[dict]) -> int:
    """
    估算总 token 数: role 字段 + content 字段的字符数总和
    1 字符 ≈ 1 token（粗略估算）
    """
    total = 0
    for msg in messages:
        total += len(msg["role"])
        total += len(msg["content"])
    return total


if __name__ == "__main__":
    sys_msg = {"role": "system", "content": "你是AI助手"}

    # 3 轮完整对话（共 7 条）
    msgs = [
        sys_msg,
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好"},
        {"role": "user", "content": "1+1?"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "再见"},
        {"role": "assistant", "content": "再见"},
    ]

    # 测试1: 窗口 1 轮 → system + 2 条 = 3 条
    r1 = trim_history(msgs, 1)
    print(f"PASS/FAIL 窗口1轮条数 -> {len(r1)} | expected: 3")
    print(f"PASS/FAIL system在前 -> {r1[0]['role']} | expected: system")
    print(f"PASS/FAIL 只留最后一轮 -> {r1[1]['content']} | expected: 再见")
    print(f"PASS/FAIL 不修改原列表 -> {len(msgs)} | expected: 7")

    # 测试2: 窗口 3 轮（正好 3 轮）→ 原样 7 条
    r2 = trim_history(msgs, 3)
    print(f"PASS/FAIL 窗口足够原样返回 -> {len(r2)} | expected: 7")

    # 测试3: 加 1 轮（变 4 轮）→ 裁剪到窗口 2 → system + 2 轮 = 5 条
    r3 = add_turn(msgs, "天气?", "晴", 2)
    print(f"PASS/FAIL 加轮+裁剪 -> {len(r3)} | expected: 5")
    print(f"PASS/FAIL 新user在倒数第2 -> {r3[-2]['content']} | expected: 天气?")

    # 测试4: 没有 system 消息也能处理
    r4 = trim_history(msgs[1:], 1)
    print(f"PASS/FAIL 无system -> {len(r4)} | expected: 2")

    # 测试5: token 粗估
    tiny = [
        {"role": "system", "content": "你"},
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "好"},
    ]
    t = estimate_tokens(tiny)
    print(f"PASS/FAIL token估算 -> {t} | expected: 23")
