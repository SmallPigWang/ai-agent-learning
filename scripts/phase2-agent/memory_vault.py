# ============================================================
# 🧩 独立挑战题: 多用户记忆金库（2.3 验收三件套之二）
#
# 背景: preference_memory.py 只有一个用户的档案。
#       真实 Agent 服务成千上万人——每人一份档案、各自隔离，
#       且档案不能无限膨胀: 超过 MAX_FACTS 条就淘汰最旧的。
#
# 契约声明（题目送给你的事实，不算提示）:
#   Python 3.7+ 的 dict 按【插入顺序】存放键——
#   档案里"最旧的偏好" = 第一个插入的键。
#
# 你要实现 5 个函数（vault = 整个金库, 形如 {"小明": {...}, "小红": {...}}）:
#
#   1. remember(vault, user, key, value) -> dict
#      给某用户记一条偏好，返回【新金库】，原金库不可被修改
#      - 新用户第一次记 → 为他建档案
#      - key 已存在 → 覆盖旧值（改口），【不】触发淘汰
#      - key 是新的且档案已满(>= MAX_FACTS) → 先踢掉最旧一条再写入
#
#   2. recall(vault, user) -> dict
#      取某用户的档案副本；没见过的用户返回 {}
#
#   3. forget(vault, user, key) -> dict
#      删掉某用户的一条偏好，返回【新金库】，原金库不可被修改
#      - key 不存在 → 原样返回（不报错）
#      - 用户不存在 → 原样返回
#
#   4. save_vault(filepath, vault) -> None
#      整库落盘（json / utf-8 / indent=2，与上午相同三件套）
#
#   5. load_vault(filepath) -> dict
#      读整库；文件不存在或损坏返回 {}
#
# 设计自由度: 内部想用嵌套 dict 还是别的结构随你——
#             但 remember/recall/forget 的【行为】必须过全部测试。
#
# ============================================================
# 知识点: （挑战题不预习知识点——通关后教练揭晓）
# ============================================================
import json

MAX_FACTS = 3  # 每用户档案容量上限


def remember(vault: dict, user: str, key: str, value: str) -> dict:
    """记一条偏好（新用户建档/改口覆盖/满则淘汰最旧），返回新金库"""
    profile = dict(vault.get(user, {}))

    if key not in profile and len(profile) >= MAX_FACTS:
        oldest = next(iter(profile))
        del profile[oldest]
    profile[key] = value

    return {**vault, user: profile}


def recall(vault: dict, user: str) -> dict:
    """取某用户档案；未见过的用户返回 {}"""
    return dict(vault[user]) if user in vault else {}


def forget(vault: dict, user: str, key: str) -> dict:
    """删一条偏好（key 或用户不存在则原样返回），返回新金库"""
    if user not in vault or key not in vault[user]:
        return vault

    profile = dict(vault[user])
    del profile[key]
    return {**vault, user: profile}


def save_vault(filepath: str, vault: dict) -> None:
    """整库以 json/utf-8/indent=2 落盘"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(vault, f, ensure_ascii=True, indent=2)


def load_vault(filepath: str) -> dict:
    """读整库；文件不存在或 JSON 损坏返回 {}"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


if __name__ == "__main__":
    from pathlib import Path

    # 测试1: 用户隔离 + 建档
    v1 = remember({}, "小明", "称呼", "小明")
    v2 = remember(v1, "小红", "称呼", "小红")
    print(f"PASS/FAIL 小明档案 -> {recall(v2, '小明')} | expected: {{'称呼': '小明'}}")
    print(f"PASS/FAIL 小红档案 -> {recall(v2, '小红')} | expected: {{'称呼': '小红'}}")
    print(f"PASS/FAIL 两人互不干扰(用户数) -> {len(v2)} | expected: 2")

    # 测试2: 未见过的用户
    print(f"PASS/FAIL 陌生用户 -> {recall(v2, '路人')} | expected: {{}}")

    # 测试3: 装满 3 条
    v3 = remember(v2, "小明", "喜欢", "Python")
    v4 = remember(v3, "小明", "城市", "北京")
    print(f"PASS/FAIL 满员3条 -> {len(recall(v4, '小明'))} | expected: 3")

    # 测试4: 第 4 条进来 → 踢掉最旧的"称呼"
    v5 = remember(v4, "小明", "讨厌", "Java")
    r5 = recall(v5, "小明")
    print(f"PASS/FAIL 淘汰最旧(称呼没了) -> {'称呼' not in r5} | expected: True")
    print(f"PASS/FAIL 淘汰后仍是3条 -> {len(r5)} | expected: 3")
    print(
        f"PASS/FAIL 剩余三条 -> {r5} | expected: {{'喜欢': 'Python', '城市': '北京', '讨厌': 'Java'}}"
    )

    # 测试5: 原金库不可被污染（重点检查点）
    print(
        f"PASS/FAIL 踢人后旧库v4的称呼还在 -> {recall(v4, '小明').get('称呼')} | expected: 小明"
    )

    # 测试6: 改口覆盖不触发淘汰
    v6 = remember(v5, "小明", "喜欢", "Rust")
    r6 = recall(v6, "小明")
    print(f"PASS/FAIL 改口生效 -> {r6.get('喜欢')} | expected: Rust")
    print(f"PASS/FAIL 改口不淘汰 -> {len(r6)} | expected: 3")
    print(
        f"PASS/FAIL 覆盖后旧库v5的喜欢还是Python -> {recall(v5, '小明').get('喜欢')} | expected: Python"
    )

    # 测试7: 小红不受小明家的事影响
    print(
        f"PASS/FAIL 小红没被波及 -> {recall(v6, '小红')} | expected: {{'称呼': '小红'}}"
    )

    # 测试8: forget 删一条 / 删不存在的
    v7 = forget(v6, "小明", "城市")
    print(f"PASS/FAIL 删除城市 -> {len(recall(v7, '小明'))} | expected: 2")
    v8 = forget(v7, "小明", "不存在的键")
    print(f"PASS/FAIL 删不存在的键原样 -> {v8 == v7} | expected: True")
    v9 = forget(v8, "陌生人", "随便")
    print(f"PASS/FAIL 删陌生用户原样 -> {v9 == v8} | expected: True")

    # 测试9: 整库落盘往返 + 容错
    tmp = str(Path(__file__).parent / "_vault_test.json")
    save_vault(tmp, v8)
    print(f"PASS/FAIL 落盘往返用户数 -> {len(load_vault(tmp))} | expected: 2")
    print(
        f"PASS/FAIL 落盘往返小明档案 -> {recall(load_vault(tmp), '小明')} | expected: {recall(v8, '小明')}"
    )
    Path(tmp).unlink()
    print(f"PASS/FAIL 缺文件 -> {load_vault(tmp)} | expected: {{}}")
    Path(tmp).write_text("}}}坏的", encoding="utf-8")
    print(f"PASS/FAIL 坏文件 -> {load_vault(tmp)} | expected: {{}}")
    Path(tmp).unlink()

    # 测试10: E2E 多用户场景
    vault: dict = {}
    for user, k, val in [
        ("小明", "称呼", "小明"),
        ("小明", "喜欢", "Python"),
        ("小红", "称呼", "小红"),
        ("小红", "讨厌", "早起"),
        ("小明", "城市", "北京"),
        ("小明", "讨厌", "Java"),
    ]:
        vault = remember(vault, user, k, val)
    m = recall(vault, "小明")
    h = recall(vault, "小红")
    ok = ("称呼" not in m) and m.get("城市") == "北京" and h.get("讨厌") == "早起"
    print(f"PASS/FAIL E2E多用户各自淘汰 -> {ok} | expected: True")
