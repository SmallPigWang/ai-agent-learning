# ============================================================
# 练习: 分块策略对比实验 + 来源标注（3.2）
#
# 背景: mini_rag 的 chunks 是手写的。真实 RAG 要把整篇文档
#       切成块——切法直接决定检索质量: 块界切在语义中间=信息腰斩。
#
# 三种切块策略:
#   fixed_chunks  固定字数硬切（无视野结构）
#   line_chunks   按行切（markdown 表格行=天然知识块）
#   window_chunks 滑动窗口+重叠（骑刀口的信息在邻块还活着）
#
# 你要实现:
#   1. fixed_chunks(text, size=60) -> list[str]
#      每 size 字一刀: text[0:size], text[size:2*size], ...
#      最后一块可以短；拼回来必须等于原文（"".join(chunks)==text）
#
#   2. line_chunks(text) -> list[str]
#      按 \n 切，丢掉空行——每条非空行就是一个块
#
#   3. window_chunks(text, size=60, overlap=20) -> list[str]
#      步长 step = size - overlap；起点 0, step, 2*step, ...
#      直到取完；最后一块不足 size 也照切
#      特性: 相邻块有 overlap 字重叠（chunks[1][:overlap]==chunks[0][step:]）
#
#   4. tag_source(chunks, source) -> list[dict]
#      给每块上户口: [{"text": 块, "source": 来源名}, ...]
#      （元数据：检索命中后要能回答"这话哪来的"）
#
#   5. compare_chunking(query, doc) -> dict
#      对比实验: 三种切法各自成块 -> 各自用 mini_rag 的 retrieve 检索
#      -> 返回 {"fixed": top1块, "line": top1块, "window": top1块}
#      （from mini_rag import retrieve——跨模块复用！）
#
# ============================================================
# 知识点: 固定分块 | 按行/结构切 | 滑动窗口重叠 | 步长公式 | 元数据溯源 | 三策略对比实验 | 跨模块import
# ============================================================
from mini_rag import retrieve


def fixed_chunks(text: str, size: int = 60) -> list[str]:
    """固定字数硬切，拼回等于原文"""
    return [text[i : size + i] for i in range(0, len(text), size)]


def line_chunks(text: str) -> list[str]:
    """按行切，丢空行——每条非空行一个块"""
    return [line for line in text.split("\n") if line]


def window_chunks(text: str, size: int = 60, overlap: int = 20) -> list[str]:
    """滑动窗口+重叠: 步长 = size-overlap，起点 0/step/2step/..."""
    step = size - overlap
    return [text[i : i + size] for i in range(0, len(text), step)]


def tag_source(chunks: list[str], source: str) -> list[dict]:
    """给每块上户口: {"text": 块, "source": 来源名}"""
    return [{"text": c, "source": source} for c in chunks]


def compare_chunking(query: str, doc: str) -> dict:
    """三策略各自切块检索，返回各自的 top1 块"""
    strategies = {
        "fixed": fixed_chunks(doc, 60),
        "line": line_chunks(doc),
        "window": window_chunks(doc, 60, 20),
    }

    result = {}
    for name, chunks in strategies.items():
        hits = retrieve(query, chunks, k=1)
        result[name] = hits[0]
    return result


if __name__ == "__main__":
    doc = (
        "滑动窗口记忆只保留最近N轮对话，省空间但丢细节\n"
        "摘要压缩记忆把旧消息压成一段摘要保留要点\n"
        "工具权限分级把工具分成绿黄红三个风险等级\n"
        "余弦相似度衡量两个向量的夹角，只认方向不认长度\n"
        "prompt注入是指令藏在数据里的经典攻击手法"
    )

    # 测试1: fixed_chunks 硬切
    fc = fixed_chunks(doc, 60)
    print(f"PASS/FAIL 固定切拼回原文 -> {''.join(fc) == doc} | expected: True")
    print(f"PASS/FAIL 每块不超上限 -> {all(len(c) <= 60 for c in fc)} | expected: True")

    # 测试2: line_chunks 按行
    lc = line_chunks(doc)
    print(f"PASS/FAIL 行块数 -> {len(lc)} | expected: 5")
    print(f"PASS/FAIL 首块内容 -> {lc[0][:6]} | expected: 滑动窗口记忆")

    # 测试3: window_chunks 滑动窗口
    wc = window_chunks(doc, 60, 20)
    step = 60 - 20
    print(
        f"PASS/FAIL 窗口块数 -> {len(wc)} | expected: {1 + -(-(len(doc) - 60) // step)}"
    )
    print(f"PASS/FAIL 相邻块真重叠 -> {wc[1][:20] == wc[0][step:]} | expected: True")

    # 测试4: tag_source 户口
    tagged = tag_source(lc, "KNOWLEDGE_BASE.md")
    ok = len(tagged) == 5 and all(
        t["source"] == "KNOWLEDGE_BASE.md" and t["text"] for t in tagged
    )
    print(f"PASS/FAIL 每块带户口 -> {ok} | expected: True")

    # 测试5: 三策略检索对比（query 目标: 第一行的记忆知识）
    r = compare_chunking("记忆保留对话怎么办", doc)
    print(
        f"PASS/FAIL 行切命中完整知识 -> {r['line']} | expected: 滑动窗口记忆只保留最近N轮对话，省空间但丢细节"
    )
    print("\n===== 三策略对比报告（肉眼判读） =====")
    for name, top1 in r.items():
        pure = top1 in lc  # top1 恰好是完整一行 = 纯块
        print(f"{name:7s} | top1({len(top1)}字): {top1[:30]}... | 纯块: {pure}")
