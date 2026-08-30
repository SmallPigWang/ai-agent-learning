# ============================================================
# 练习: 跨对话偏好记忆（长期记忆最小闭环 / 2.3 检验题）
#
# 背景: 窗口/摘要都只管"一场对话内部"（短期记忆）。
#       新对话一开，Agent 就失忆。长期记忆 = 把用户偏好
#       落盘成文件，新对话开始时自动装回 system。
#
# 三种记忆分工（对照着体会）:
#   - 短期记忆: messages + 窗口裁剪（已学）
#   - 长期记忆: 本练习——偏好档案 JSON 落盘，跨对话存活
#   - 工作记忆: AgentState（Day 5 已学）
#
# 长期记忆最小闭环:
#   对话中: 用户说"我喜欢Python" → 抽出(喜欢, Python) → 存档案 → 落盘
#   新对话: 读盘 → 拼进 system → Agent 开口就"记得你"
#
# 你要实现:
#   1. extract_preference(text) -> tuple[str, str] | None
#      从用户消息里抽取偏好（规则模拟 LLM 抽取，离线可测）
#      - "我喜欢X"   -> ("喜欢", "X")
#      - "我叫X"     -> ("称呼", "X")
#      - "我讨厌X"   -> ("讨厌", "X")
#      - 都不匹配   -> None
#      - X 为空字符串 -> None
#
#   2. remember_fact(memory, key, value) -> dict
#      把一条偏好放进档案，返回【新字典】，不修改原字典
#      - key 已存在时覆盖旧值（用户改口了）
#
#   3. build_system_with_memory(base_system, memory) -> dict
#      新对话的 system 消息生成器（返回完整消息 dict）
#      - 档案为空: {"role": "system", "content": base_system}
#      - 档案非空: content = base_system + "已知用户偏好: k1=v1; k2=v2"
#                  （; 分隔，顺序按档案插入顺序）
#
#   4. save_memory(filepath, memory) -> None
#      档案落盘: JSON 格式、utf-8 编码、缩进 2（json.dump 三件套）
#
#   5. load_memory(filepath) -> dict
#      读档案: 文件不存在返回 {}，文件损坏(json.JSONDecodeError)也返回 {}
#
# ============================================================
# 知识点: 三种记忆分工(短期/长期/工作) | 长期记忆持久化(json落盘) | 规则抽取模拟LLM | system注入点 | startswith前缀判断 | dict(...)拷贝构造不可变更新
# ============================================================
import json
from pathlib import Path


def extract_preference(text: str) -> tuple[str, str] | None:
    """
    从用户消息抽取偏好，规则:
    我喜欢X -> ("喜欢", X) / 我叫X -> ("称呼", X) / 我讨厌X -> ("讨厌", X)
    不匹配或 X 为空返回 None
    """
    for prefix, key in [("我喜欢", "喜欢"), ("我叫", "称呼"), ("我讨厌", "讨厌")]:
        if text.startswith(prefix):
            value = text[len(prefix) :]
            if not value:
                return None
            return (key, value)

    return None


def remember_fact(memory: dict, key: str, value: str) -> dict:
    """
    返回加入/更新一条偏好的【新】字典，不修改原字典
    """
    new_memory = dict(memory)
    new_memory[key] = value
    return new_memory


def build_system_with_memory(base_system: str, memory: dict) -> dict:
    """
    生成带长期记忆的 system 消息:
    档案空 -> {"role": "system", "content": base_system}
    档案非空 -> content 末尾追加 "已知用户偏好: k1=v1; k2=v2"
    """
    if not memory:
        return {"role": "system", "content": base_system}

    parts = [f"{k}={v}" for k, v in memory.items()]
    return {
        "role": "system",
        "content": base_system + "已知用户偏好： " + "; ".join(parts),
    }


def save_memory(filepath: str, memory: dict) -> None:
    """
    把档案以 JSON/utf-8/缩进2 写入文件
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=True, indent=2)


def load_memory(filepath: str) -> dict:
    """
    从文件读档案；文件不存在或 JSON 损坏都返回 {}
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


if __name__ == "__main__":
    import json

    # 测试1: extract_preference 规则抽取
    print(
        f"PASS/FAIL 抽取喜欢 -> {extract_preference('我喜欢Python')} | expected: ('喜欢', 'Python')"
    )
    print(
        f"PASS/FAIL 抽取称呼 -> {extract_preference('我叫小明')} | expected: ('称呼', '小明')"
    )
    print(
        f"PASS/FAIL 抽取讨厌 -> {extract_preference('我讨厌Java')} | expected: ('讨厌', 'Java')"
    )
    print(f"PASS/FAIL 无偏好 -> {extract_preference('今天天气不错')} | expected: None")
    print(f"PASS/FAIL 前缀无值 -> {extract_preference('我喜欢')} | expected: None")

    # 测试2: remember_fact 不可变更新
    m1 = remember_fact({}, "喜欢", "Python")
    print(f"PASS/FAIL 新增 -> {m1} | expected: {{'喜欢': 'Python'}}")
    m2 = remember_fact(m1, "称呼", "小明")
    print(f"PASS/FAIL 累加两条 -> {len(m2)} | expected: 2")
    print(f"PASS/FAIL 原字典未被修改 -> {m1 == {'喜欢': 'Python'}} | expected: True")
    m3 = remember_fact(m2, "喜欢", "Rust")
    print(f"PASS/FAIL 改口覆盖 -> {m3['喜欢']} | expected: Rust")
    print(f"PASS/FAIL 覆盖不改原 -> {m2['喜欢']} | expected: Python")

    # 测试3: build_system_with_memory 注入
    s1 = build_system_with_memory("你是StudyNote助手", {})
    print(f"PASS/FAIL 空档案role -> {s1['role']} | expected: system")
    print(f"PASS/FAIL 空档案content -> {s1['content']} | expected: 你是StudyNote助手")
    s2 = build_system_with_memory(
        "你是StudyNote助手", {"称呼": "小明", "喜欢": "Python"}
    )
    ok = (
        "已知用户偏好" in s2["content"]
        and "称呼=小明" in s2["content"]
        and "喜欢=Python" in s2["content"]
    )
    print(f"PASS/FAIL 档案注入system -> {ok} | expected: True")

    # 测试4: 落盘往返 + 容错
    tmp = str(Path(__file__).parent / "_pref_test.json")
    save_memory(tmp, {"称呼": "小明", "喜欢": "Python"})
    back = load_memory(tmp)
    print(
        f"PASS/FAIL 落盘往返 -> {back} | expected: {{'称呼': '小明', '喜欢': 'Python'}}"
    )
    Path(tmp).unlink()  # 删掉，顺便测缺文件
    print(f"PASS/FAIL 文件不存在 -> {load_memory(tmp)} | expected: {{}}")
    Path(tmp).write_text("这不是json{{{", encoding="utf-8")  # 写坏文件
    print(f"PASS/FAIL 文件损坏 -> {load_memory(tmp)} | expected: {{}}")

    # 测试5: E2E 跨对话记忆（2.3 检验题本体）
    # --- 对话1: 小明说三句话，最后一句不是偏好 ---
    memory: dict = {}
    for msg in ["我叫小明", "我喜欢Python", "今天天气不错"]:
        pref = extract_preference(msg)
        if pref is not None:
            memory = remember_fact(memory, pref[0], pref[1])
    save_memory(tmp, memory)

    # --- 对话2: 全新进程，只靠文件恢复记忆 ---
    restored = load_memory(tmp)
    sys_msg = build_system_with_memory("你是StudyNote助手", restored)
    e2e = (
        "小明" in sys_msg["content"]
        and "Python" in sys_msg["content"]
        and "天气" not in sys_msg["content"]
    )
    print(f"PASS/FAIL 跨对话记住偏好 -> {e2e} | expected: True")
    Path(tmp).unlink()  # 清理
