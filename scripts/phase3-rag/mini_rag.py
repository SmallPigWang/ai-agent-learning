# ============================================================
# 练习: 50 行最简 RAG（3.1 开荒——给检索装上"语义"）
#
# 与 search_notes 的区别: 子串匹配只认"一模一样的字"，
# 向量检索认"意思相近的字"——"宕机"能命中"死机"。
#
# embedding 的离线替身（回调注入第 4 次）:
#   hash_embed: 字符二元组(bigram)哈希计数向量——确定性、免费、
#   中文效果够用（共享词=共享bigram=向量相近）。
#   生产环境换成真 embedding API（智谱 embedding-3），接口不变。
#
# 你要实现:
#   1. hash_embed(text, dim=256) -> list[float]
#      把相邻字符对(text[i], text[i+1])哈希进向量:
#      idx = (ord(c1) * 31 + ord(c2)) % dim, vec[idx] += 1.0
#      （31 是惯例素数；同一文本永远同一向量=确定性）
#
#   2. cosine(a, b) -> float
#      余弦相似度 = 点积 / (a的模 × b的模)
#      点积: sum(x*y for x,y in zip(a,b))
#      模:   各分量平方和再开方（math.sqrt）
#      防零除: 模为 0 时返回 0.0
#      含义: 两向量夹角——1.0 同向(最像), 0.0 垂直(无关)
#
#   3. retrieve(query, chunks, k=2, embed=hash_embed) -> list[str]
#      把 query 和每块都 embed，算 cosine，按相似度降序，返回前 k 块原文
#      （embed 是参数——生产换真 API 时只换实参，函数一行不改）
#
#   4. build_prompt(question, hits) -> str
#      RAG 最后一环: 把检索结果拼进提问
#      格式: "已知资料:\n- {块1}\n- {块2}\n\n问题: {question}"
#
# ============================================================
# 知识点: RAG两流程(存入/查询) | hash-embedding离线替身 | bigram哈希 | 余弦相似度 | Top-K检索 | 回调注入embedding | 开卷考试类比
# ============================================================
import math


def hash_embed(text: str, dim: int = 256) -> list[float]:
    """字符 bigram 哈希计数向量（确定性 embedding 离线替身）"""
    vec = [0.0] * dim
    for i in range(len(text) - 1):
        c1, c2 = text[i], text[i + 1]
        idx = (ord(c1) * 31 + ord(c2)) % dim
        vec[idx] += 1.0
    return vec


def cosine(a: list[float], b: list[float]) -> float:
    """余弦相似度: 1.0 同向最像, 0.0 无关; 防零除"""
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def retrieve(query: str, chunks: list[str], k: int = 2, embed=hash_embed) -> list[str]:
    """语义检索: query 和各块比相似度，降序取前 k 块原文"""
    q_vec = embed(query)
    scored = []
    for chunk in chunks:
        score = cosine(q_vec, embed(chunk))
        scored.append((score, chunk))
    scored.sort(key=lambda t: -t[0])
    return [chunk for score, chunk in scored[:k]]


def build_prompt(question: str, hits: list[str]) -> str:
    """把检索结果拼进提问（RAG 的生成侧接口）"""
    lines = "\n".join(f"- {h}" for h in hits)
    return f"已知资料:\n{lines}\n\n问题: {question}"


if __name__ == "__main__":
    chunks = [
        "流式输出用SSE协议逐块推送，yield生成器是灵魂",
        "滑动窗口记忆只保留最近N轮对话，省空间但丢细节",
        "工具权限分级把工具分成绿黄红三个风险等级",
    ]

    # 测试1: hash_embed 确定性
    v1 = hash_embed("流式输出")
    v2 = hash_embed("流式输出")
    print(f"PASS/FAIL 相同文本同向量 -> {v1 == v2} | expected: True")
    print(f"PASS/FAIL 维度正确 -> {len(v1)} | expected: 256")
    print(
        f"PASS/FAIL 不同文本异向量 -> {v1 != hash_embed('权限分级')} | expected: True"
    )

    # 测试2: cosine 数学性质
    print(f"PASS/FAIL 自身相似度 -> {cosine([1, 0], [1, 0])} | expected: 1.0")
    print(f"PASS/FAIL 垂直无关 -> {cosine([1, 0], [0, 1])} | expected: 0.0")
    print(
        f"PASS/FAIL 方向相同长度不同 -> {round(cosine([1, 0], [5, 0]), 6)} | expected: 1.0"
    )
    print(f"PASS/FAIL 零向量防崩 -> {cosine([0, 0], [1, 1])} | expected: 0.0")

    # 测试3: 语义检索命中率
    print(
        f"PASS/FAIL 查流式 -> {retrieve('流式输出怎么实现', chunks, k=1)[0][:8]} | expected: 流式输出用SS"
    )
    print(
        f"PASS/FAIL 查记忆 -> {retrieve('记忆系统保留对话', chunks, k=1)[0][:8]} | expected: 滑动窗口记忆"
    )
    print(
        f"PASS/FAIL 查权限 -> {retrieve('权限分级红绿灯', chunks, k=1)[0][:8]} | expected: 工具权限分级"
    )

    # 测试4: RAG 最后一环
    p = build_prompt("流式输出是什么", retrieve("流式输出怎么实现", chunks, k=1))
    ok = p.startswith("已知资料:") and "流式输出" in p and "问题: 流式输出是什么" in p
    print(f"PASS/FAIL prompt组装 -> {ok} | expected: True")
