# ============================================================
# 🎯 压轴: StudyNote 向量记忆（2.3 欠账 × 3.2 切块 × 3.3 bge+Chroma 总装）
#
# 使命: 给 studynote_agent 造一件语义检索武器 vector_search，
#       替代 search_notes 的子串匹配（就是 EVAL 第6题扑空那位）。
#
# ⚠️ 运行环境: torch_env（bge + chromadb 都住那里）
#
# 你要实现:
#   1. load_corpus() -> list[tuple[str, str]]
#      收集真实仓库知识块（source文件名, 非空行）:
#      - 文件: KNOWLEDGE_BASE.md + PITFALLS.md + logs/day-*.md
#      - 过滤: strip 后长度>=8；跳过 # 开头标题；跳过 |---| 表格分隔线
#        （判断分隔线: 行去掉 -|: 和空格后为空）
#
#   2. build_index(db_path) -> tuple[col, list[str]]
#      编目入库（chroma_lab 同款 + 新增 metadatas 户口）:
#      a. PersistentClient + 幂等删旧 "studynote"
#      b. collection cosine 空间
#      c. add 四件套: documents=texts / embeddings=bge批量 /
#         ids=c0.. / metadatas=[{"source": 来源}]  ← 新: where 过滤的底气
#      d. return (col, texts)
#
#   3. vector_search(keyword, k=3) -> str
#      Agent 的新武器（懒加载单例——首次调用建库，之后查目录）:
#      a. 全局 _INDEX=None; 首次: corpus=load_corpus(); _INDEX=build_index(...)
#      b. res = col.query(query_embeddings=[bge_embed(keyword)],
#                        n_results=k, include=["documents", "metadatas"])
#      c. 返回 "来源: 内容" 逐行拼接（和 search_notes 同格式，Agent 无缝换装）
#
# ============================================================
# 知识点: 真实仓库切块 | add四件套(metadatas) | 懒加载单例复用 | 工具同格式换装 | 子串vs语义终极对决
# ============================================================
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from chroma_lab import chroma_query  # noqa: F401 复用检查（同目录）
from embedding_bakeoff import bge_embed

ROOT = Path(__file__).resolve().parent.parent.parent
DB_PATH = str(Path(__file__).parent / ".studynote_db")

_INDEX = None  # 懒加载单例: (col, texts)


def load_corpus() -> list[tuple[str, str]]:
    """收集真实仓库知识块: (source文件名, 非空有效行)"""
    files = [
        ROOT / "KNOWLEDGE_BASE.md",
        ROOT / "PITFALLS.md",
        *sorted((ROOT / "logs").glob("day-*.md")),
    ]

    pairs: list[tuple[str, str]] = []
    for f in files:
        for line in f.read_text("utf-8").split("\n"):
            t = line.strip()
            if len(t) < 8:
                continue
            if t.startswith("#") or not t.strip("-|:"):
                continue
            pairs.append((f.name, t))
    return pairs


def build_index(db_path: str):
    """真实仓库编目入库: bge向量 + metadatas户口，返回 (col, texts)"""
    import chromadb

    corpus = load_corpus()
    texts = [t for _, t in corpus]
    sources = [s for s, _ in corpus]
    client = chromadb.PersistentClient(path=db_path)
    if "studynote" in [
        c.name for c in client.list_collections()
    ]:  # 名字必须与库名逐字一致
        client.delete_collection("studynote")
    col = client.get_or_create_collection(
        "studynote", metadata={"hnsw:space": "cosine"}
    )
    col.add(
        documents=texts,
        embeddings=[bge_embed(t) for t in texts],  # ⑥ 每块向量化（哪位选手）
        ids=[f"c{i}" for i in range(len(texts))],
        metadatas=[{"source": s} for s in sources],
    )

    return col, texts


def vector_search(keyword: str, k: int = 3) -> str:
    """Agent 新武器: 语义检索全仓库（首次建库，之后查目录）"""
    global _INDEX
    if _INDEX is None:
        print("(首次建库中，约10秒...)")
        _INDEX = build_index(DB_PATH)
    col, _ = _INDEX
    # bge 出厂设置: 检索查询必须带官方任务前缀（文档不带，仅查询带）——
    # 训练时如此，生产查询要还原同一格式，否则查询向量偏离分布、排名漂移
    QUERY_PREFIX = "为这个句子生成表示以用于检索相关文章："
    res = col.query(
        query_embeddings=[bge_embed(QUERY_PREFIX + keyword)],
        n_results=k,
        include=["documents", "metadatas"],
    )
    docs = (res.get("documents") or [[]])[0]   # 静态防御: chroma 类型说可能 None，运行时总在
    metas = (res.get("metadatas") or [None])[0]
    lines = [
        f"{m['source']}: {d}" if m is not None else d  # m 可为 None(按 chroma 类型定义)，None 守卫
        for d, m in zip(docs, metas)
    ]
    return "\n".join(lines) if lines else "(没有找到相关内容)"


if __name__ == "__main__":
    # 测试1: 语料收集
    corpus = load_corpus()
    print(f"PASS/FAIL 语料量>400行 -> {len(corpus) > 400} | 实际: {len(corpus)}")
    ok_src = all(s.endswith((".md",)) for s, _ in corpus)
    ok_len = all(len(t) >= 8 for _, t in corpus)
    print(f"PASS/FAIL 来源合法且行长合规 -> {ok_src and ok_len} | expected: True")

    # 测试2: 编目入库
    col, texts = build_index(DB_PATH)
    print(f"PASS/FAIL 入库数=语料数 -> {col.count() == len(texts)} | expected: True")

    # 测试3: 语义武器 vs 子串武器（终极对决）
    q = "怎么防止Agent被恶意指令劫持"

    def substring_search(query: str) -> str:
        """子串武器（search_notes 同款逻辑，作对照）"""
        hits = []
        for f in [
            ROOT / "KNOWLEDGE_BASE.md",
            ROOT / "PITFALLS.md",
            *sorted((ROOT / "logs").glob("day-*.md")),
        ]:
            for line in f.read_text("utf-8").split("\n"):
                if query in line:
                    hits.append(f"{f.name}: {line.strip()[:60]}")
        return "\n".join(hits[:3])

    print(f"\n===== 终极对决: {q} =====")
    old = substring_search(q)
    new = vector_search(q, k=2)
    print(f"子串武器(search_notes同款): {old[:60] or '(扑空)'}")
    print(f"语义武器(vector_search)  : {new.split(chr(10))[0][:60]}")
    print(
        f"PASS/FAIL 语义武器命中注入主题 -> {'注入' in new or '劫持' in new} | expected: True"
    )
