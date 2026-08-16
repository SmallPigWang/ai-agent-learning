# ============================================================
# 练习: 摘要压缩记忆
#
# 背景: 滑动窗口会把旧消息直接丢掉，太“绝情”。
#       摘要压缩是更聪明的策略: 旧消息不丢光，而是压成一段摘要，
#       新对话继续用滑动窗口保留。
#
# 你要实现:
#   1. summarize_old_messages(old_messages) -> str
#      把旧消息列表压缩成一段摘要字符串
#      - 格式: "user:内容 | assistant:内容 | ..."
#      - 每条消息都转成 "角色:内容"，用 " | " 连接
#      - 没有消息时返回 ""
#
#   2. compress_memory(messages, max_turns) -> tuple[str, list]
#      把完整消息拆成“旧摘要 + 最近窗口”
#      - system 如果有，必须保留在最近窗口的最前面
#      - 最近 max_turns 轮 = 最近 max_turns * 2 条非 system 消息
#      - 超过窗口的部分交给 summarize_old_messages 生成摘要
#      - 返回 (summary, recent_messages)
#      - 没有旧消息时 summary 为 ""
#
#   3. build_context(summary, recent_messages) -> list[dict]
#      把摘要和最近窗口拼回可发送给 LLM 的 messages
#      - 没有摘要时直接返回 recent_messages
#      - 如果 recent_messages 第一条是 system，把摘要合并进这条 system
#      - 否则在最前面新增一条 system 消息存放摘要
#
# ============================================================
# 知识点: 摘要压缩策略 | 旧消息→摘要 | 摘要合并进 system | 滑动窗口+摘要混合策略
# ============================================================

def summarize_old_messages(old_messages):
    """
    把旧消息列表压缩成摘要字符串
    格式: "user:内容 | assistant:内容 | ..."
    没有消息返回 ""
    """
    parts = []
    for msg in old_messages:
        role = msg["role"]
        content = msg["content"]
        parts.append(role + ":" + content)

    return ' | '.join(parts)


def compress_memory(messages, max_turns):
    """
    返回 (summary, recent_messages)
    - system 如果有，保留在 recent_messages 最前面
    - 超过最近 max_turns 轮的旧消息生成 summary
    """
    system_msg = None
    rest = messages

    # 剔除system信息单独拿出
    if messages and messages[0].get("role") == 'system':
        system_msg = messages[0]
        rest = messages[1:]

    keep_count = max_turns * 2

    if len(rest) <= keep_count:
        if system_msg is not None:
            return "", [system_msg] + rest
        return "", rest

    # 窗口保留信息条数
    old = rest[:len(rest) - keep_count]
    recent = rest[len(rest) - keep_count:]

    # 摘要生成
    summary = summarize_old_messages(old_messages=old)

    if system_msg is not None:
        recent = [system_msg] + recent

    return summary, recent



def build_context(summary, recent_messages):
    """
    把摘要和最近窗口拼成可发送给 LLM 的 messages
    摘要优先合并进已有 system，没有 system 则新增 system
    """
    if not summary:
        return recent_messages

    if recent_messages and recent_messages[0].get("role") == "system":
        merged = dict(recent_messages[0])
        merged["content"] = merged["content"] + " 摘要：" + summary
        return [merged] + recent_messages[1:]  # 用合并后的消息替换第一条

    summary_msg = {"role": "system", "content": "摘要：" + summary}

    return [summary_msg] + recent_messages


if __name__ == "__main__":
    sys_msg = {"role": "system", "content": "你是AI助手"}

    # 4 轮完整对话（共 9 条）
    msgs = [
        sys_msg,
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好呀"},
        {"role": "user", "content": "今天天气如何"},
        {"role": "assistant", "content": "今天是晴天"},
        {"role": "user", "content": "1+1?"},
        {"role": "assistant", "content": "2"},
        {"role": "user", "content": "再见"},
        {"role": "assistant", "content": "再见"},
    ]

    # --- 测试 summarize_old_messages ---
    old = [
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好呀"},
    ]
    s = summarize_old_messages(old)
    print(f"PASS/FAIL 摘要含user -> {'user:你好' in s} | expected: True")
    print(f"PASS/FAIL 摘要含assistant -> {'assistant:你好呀' in s} | expected: True")
    print(f"PASS/FAIL 空摘要 -> {summarize_old_messages([]) == ''} | expected: True")

    # --- 测试 compress_memory ---
    summary, recent = compress_memory(msgs, 2)
    print(f"PASS/FAIL 最近窗口条数 -> {len(recent)} | expected: 5")
    print(f"PASS/FAIL system在最前 -> {recent[0]['role']} | expected: system")
    print(f"PASS/FAIL 最后一轮保留 -> {recent[-1]['content']} | expected: 再见")
    print(f"PASS/FAIL 旧消息进摘要 -> {'user:你好' in summary and '今天是晴天' in summary} | expected: True")

    # --- 测试 build_context ---
    ctx = build_context(summary, recent)
    print(f"PASS/FAIL 上下文第一条是system -> {ctx[0]['role']} | expected: system")
    print(f"PASS/FAIL system含摘要 -> {'摘要' in ctx[0]['content']} | expected: True")
    print(f"PASS/FAIL 上下文保留最近窗口 -> {len(ctx)} | expected: 5")

    # --- 测试没有旧消息 ---
    short = msgs[:5]  # system + 2 轮
    summary2, recent2 = compress_memory(short, 2)
    print(f"PASS/FAIL 无旧消息摘要为空 -> {summary2 == ''} | expected: True")
    print(f"PASS/FAIL 无旧消息原样返回 -> {len(recent2)} | expected: 5")

    # --- 测试没有 system ---
    no_sys = msgs[1:]
    summary3, recent3 = compress_memory(no_sys, 1)
    print(f"PASS/FAIL 无system窗口条数 -> {len(recent3)} | expected: 2")
    print(f"PASS/FAIL 无system也有摘要 -> {summary3 != ''} | expected: True")

    ctx2 = build_context(summary3, recent3)
    print(f"PASS/FAIL 无system时新增摘要system -> {ctx2[0]['role']} | expected: system")
