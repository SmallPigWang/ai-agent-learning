# ============================================================
# 练习: Embedding 对比擂台 + 命中率评估（3.3 第一仗）
#
# 问题: 换真 embedding 到底值多少？用数字说话——
#   同一批知识块 + 同一组(查询, 标准答案)测试集，
#   hash_embed 和 bge 各跑一遍 retrieve，算各自命中率。
#
# ⚠️ 运行环境: torch_env（bge 模型住在那里）
#    python embedding_bakeoff.py
#
# 你要实现:
#   1. bge_embed(text) -> list[float]
#      包装本地 bge 模型（懒加载单例——模型加载慢，全程只加载一次）
#      a. 全局 _MODEL = None；函数里 if _MODEL is None 才加载
#      b. 加载: SentenceTransformer("BAAI/bge-small-zh-v1.5")
#      c. 返回: m.encode(text).tolist()
#
#   2. hit_rate(embed_fn, chunks, test_set, k=1) -> float
#      命中率 = 答对数 / 总题数:
#      a. 对每题 (query, expected_idx): hits = retrieve(query, chunks, k, embed=embed_fn)
#      b. 命中判定: chunks[expected_idx] 在 hits 里（用 in，k>1 时任一命中即算对）
#      c. return 命中数 / len(test_set)
#
#   3. run_bakeoff(chunks, test_set) -> dict
#      两位选手各测一次: {"hash": 命中率, "bge": 命中率}
#
# ============================================================
# 知识点: hit rate评估 | (query,标准答案)测试集 | 懒加载单例 | 对照实验(玩具vs真语义) | 同义陷阱题设计 | 复用retrieve回调
# ============================================================
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from mini_rag import retrieve  # 跨模块复用: 引擎一行不改

_MODEL = None  # 懒加载单例的空位（模型加载要几秒，全程只做一次）


def bge_embed(text: str) -> list[float]:
    """本地 bge-small-zh 真语义 embedding（512 维）"""
    global _MODEL  # ① 新语法：声明动全局（不声明=白装）
    if _MODEL is None:  # ② 空位还空着才装载（第一次）
        from sentence_transformers import SentenceTransformer

        _MODEL = SentenceTransformer("BAAI/bge-small-zh-v1.5")
    return _MODEL.encode(text).tolist()


def hit_rate(
    embed_fn, chunks: list[str], test_set: list[tuple[str, int]], k: int = 1
) -> float:
    """命中率 = 标准答案块出现在 top-k 里的题数 / 总题数"""
    hits_count = 0
    for query, expected_idx in test_set:
        hits = retrieve(query, chunks, k, embed=embed_fn)
        if chunks[expected_idx] in hits:
            hits_count += 1

    return hits_count / len(test_set)


def run_bakeoff(chunks: list[str], test_set: list[tuple[str, int]]) -> dict:
    """hash vs bge 两位选手各测一次命中率"""
    from mini_rag import hash_embed

    return {
        "hash": hit_rate(hash_embed, chunks, test_set),
        "bge": hit_rate(bge_embed, chunks, test_set),
    }


if __name__ == "__main__":
    from mini_rag import hash_embed

    chunks = [
        "流式输出用SSE协议逐块推送，yield生成器是灵魂",
        "滑动窗口记忆只保留最近N轮对话，省空间但丢细节",
        "工具权限分级把工具分成绿黄红三个风险等级",
        "服务器宕机需要检查日志并重启服务",
        "prompt注入是指令藏在数据里的攻击手法",
        "余弦相似度衡量向量夹角，只认方向不认长度",
        "摘要压缩记忆把旧消息压成一段摘要保留要点",
        "Pydantic把LLM文本输出变成类型安全的对象",
    ]

    # 测试集: (查询, 标准答案的块下标)——前3题字面重叠多，后2题是同义陷阱
    test_set = [
        ("流式输出怎么实现", 0),
        ("绿黄红是什么", 2),
        ("向量夹角怎么算", 5),
        ("机器死机了如何处理", 3),  # 死机 vs 宕机：hash 的天堑
        ("黑客在网页里埋了恶意命令", 4),  # 埋命令 vs 藏指令：paraphrase
    ]

    r = run_bakeoff(chunks, test_set)
    print(
        f"PASS/FAIL hash命中率在合理区间 -> {0.0 <= r['hash'] < 1.0} | expected: True"
    )
    print(f"PASS/FAIL bge命中率不低于0.8 -> {r['bge'] >= 0.8} | expected: True")
    print(f"PASS/FAIL bge胜过hash -> {r['bge'] > r['hash']} | expected: True")

    print("\n===== Embedding 对比擂台（k=1, 5题） =====")
    for name, fn in (("hash", hash_embed), ("bge", bge_embed)):
        rate = hit_rate(fn, chunks, test_set)
        mark = " ".join(
            "✓" if chunks[idx] in retrieve(q, chunks, 1, embed=fn) else "✗"
            for q, idx in test_set
        )
        print(f"{name:5s} | 命中率 {rate:.0%} | 逐题: {mark}")
