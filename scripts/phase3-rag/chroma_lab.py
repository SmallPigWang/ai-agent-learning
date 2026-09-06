# ============================================================
# 练习: Chroma 搭本地向量库（3.3 第二仗）
#
# 从"查询时全量扫"升级为"编目一次、查目录 forever":
#   存入: 每块 bge 向量化 -> collection.add 三件套(文档/向量/ids) -> 落盘
#   查询: 只算问题向量 -> collection.query -> 秒回 top-k
#
# ⚠️ 运行环境: torch_env（依赖 chromadb + bge 模型）
#    python chroma_lab.py
#
# 你要实现:
#   1. build_collection(chunks, db_path) -> Collection
#      编目入库（幂等: 先删旧 collection，可反复重跑）:
#      a. client = chromadb.PersistentClient(path=db_path)   # 落盘客户端
#      b. try: client.delete_collection("study_notes") except: pass  # 删旧
#      c. col = client.get_or_create_collection("study_notes",
#              metadata={"hnsw:space": "cosine"})   # 度量选cosine(和手写版一致)
#      d. col.add(documents=chunks,
#                 embeddings=[bge_embed(c) for c in chunks],  # 每块向量化
#                 ids=[f"c{i}" for i in range(len(chunks))])
#
#   2. chroma_query(col, query, k=1) -> list[str]
#      查目录: res = col.query(query_embeddings=[bge_embed(query)], n_results=k)
#      返回 res["documents"][0]   # Chroma 结果套两层: {documents: [[块,...]]}
#
#   验收: 同一套测试集，Chroma 检索 hit rate 应与手写 retrieve+bge 打平
#
# ============================================================
# 知识点: 向量库三件套(存储/索引/过滤) | PersistentClient落盘 | add三件套(文档/向量/ids) | cosine空间 | ANN vs 暴力扫 | 幂等重建 | 工业件与手搓件等价性
# ============================================================
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from embedding_bakeoff import bge_embed  # 选手复用
from mini_rag import retrieve  # 手写版对照


def build_collection(chunks: list[str], db_path: str):
    """编目入库: 每块向量化 + add 三件套，落盘（幂等可重跑）"""
    import chromadb

    client = chromadb.PersistentClient(path=db_path)
    if "study_notes" in [c.name for c in client.list_collections()]:
        client.delete_collection("study_notes")  # 幂等: 有旧册才撕，先问一句胜过接异常

    col = client.get_or_create_collection(
        "study_notes",
        metadata={"hnsw:space": "cosine"},
    )
    col.add(
        documents=chunks,
        embeddings=[bge_embed(c) for c in chunks],  # 每块向量化
        ids=[f"c{i}" for i in range(len(chunks))],
    )

    return col


def chroma_query(col, query: str, k: int = 1) -> list[str]:
    """查目录: 问题向量化 -> query -> 返回 top-k 块原文"""
    res = col.query(
        query_embeddings=[bge_embed(query)],
        n_results=k,
    )
    return res["documents"][0]


if __name__ == "__main__":
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
    test_set = [
        ("流式输出怎么实现", 0),
        ("绿黄红是什么", 2),
        ("向量夹角怎么算", 5),
        ("机器死机了如何处理", 3),
        ("黑客在网页里埋了恶意命令", 4),
    ]

    col = build_collection(chunks, str(Path(__file__).parent / ".chroma_db"))
    print(f"PASS/FAIL 入库块数 -> {col.count()} | expected: 8")

    # 双引擎对比: 手写 retrieve+bge vs Chroma
    hand_hits = 0
    chroma_hits = 0
    print("\n===== 双引擎对决（k=1, 5题） =====")
    for q, idx in test_set:
        by_hand = retrieve(q, chunks, 1, embed=bge_embed)
        by_chroma = chroma_query(col, q, 1)
        h = chunks[idx] in by_hand
        c = chunks[idx] in by_chroma
        hand_hits += h
        chroma_hits += c
        agree = "同" if by_hand == by_chroma else "异"
        print(
            f"{q[:12]:12s} | 手写{'✓' if h else '✗'} Chroma{'✓' if c else '✗'} | 两引擎{agree}"
        )

    print(f"\n手写bge  命中率: {hand_hits}/{len(test_set)}")
    print(f"Chroma   命中率: {chroma_hits}/{len(test_set)}")
    print(f"PASS/FAIL Chroma满命中 -> {chroma_hits == len(test_set)} | expected: True")
    print(f"PASS/FAIL 与手写版打平 -> {chroma_hits == hand_hits} | expected: True")
