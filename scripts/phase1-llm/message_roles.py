# ============================================================
# 练习: Messages API 四个角色
#
# 核心认知: messages 数组里每个元素都有 role 字段，共 4 种角色
#
#   role       含义                          谁写的
#   -------    ---------------------------   --------
#   system     设定 AI 身份/行为/规则        开发者（常驻第一条）
#   user       用户说的话                    用户/程序
#   assistant  AI 的回复（历史回填）         AI → 你回填
#   tool       工具执行结果（阶段2才用）     程序
#
# 你要实现:
#   1. validate_roles(messages) — 纯逻辑校验 messages 结构是否合法
#   2. chat_with_system(...)    — 带 system 角色 + 历史的多轮对话
#
# 规则:
#   - 函数体中只用 return，禁止 print
#   - 复用 first_api_call.py / multi_turn_chat.py 的调用方式
#
# ============================================================
# 知识点: 消息四角色 system/user/assistant/tool | 安检闸门校验模式 | 跨轮记忆回填
# ============================================================

import os
import requests
from dotenv import load_dotenv

# ---------- 复用（从 multi_turn_chat.py 搬过来）----------

def load_api_key() -> str | None:
    """从 .env 文件加载 API Key"""
    load_dotenv()
    return os.getenv("DEEPSEEK_API_KEY")


# ---------- 待实现 ----------

def validate_roles(messages: list[dict]) -> bool:
    """
    校验 messages 是否符合角色规则，全部满足才返回 True:
      1. messages 非空列表
      2. 每个元素必须是 dict 且有 "role" 字段
      3. role 的值必须是 "system" / "user" / "assistant" / "tool" 之一
      4. system 最多出现一次
      5. system 如果存在，必须位于第一条（位置 0）
    """
    if not messages:
        return False

    for msg in messages:
        if not isinstance(msg, dict) or "role" not in msg: # 检查是否类型为dict以及字段是否包含role
            return False

        if msg["role"] not in ["system", "user", "assistant", "tool"]:
            return False

    roles = [msg["role"] for msg in messages]
    if roles.count("system") > 1:
        return False
    if "system" in roles and roles[0] != "system":
        return False

    return True
 


def chat_with_system(system_prompt: str, history: list[dict],
                     user_msg: str, api_key: str) -> str:
    """
    带 system 角色 + 历史的多轮对话，返回 AI 回复文本
    流程:
      1. messages = [{"role": "system", "content": system_prompt}]
      2. 把 history 里的历史消息全部追加进 messages
      3. 再追加 [{"role": "user", "content": user_msg}]
      4. 发送给 DeepSeek（URL/headers/body 同 multi_turn_chat.py）
      5. return AI 回复
    """
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    messages = [{"role":"system", "content":system_prompt}] + history + [{"role": "user", "content":user_msg}]
    body = {
        "model": "deepseek-v4-flash",
        "messages": messages,
        "max_tokens": 1024
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]




# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True

    # ---------- Part 1: validate_roles 纯逻辑测试 ----------

    # 测试1: 合法消息 → True
    valid = [
        {"role": "system", "content": "你是一个友好的助手"},
        {"role": "user", "content": "你好"},
        {"role": "assistant", "content": "你好！有什么可以帮你？"},
        {"role": "tool", "content": "{\"result\": 42}"},
    ]
    r1 = validate_roles(valid)
    print(f"{'PASS' if r1 else 'FAIL'} validate_roles(合法4角色) -> {r1} | expected: True")
    all_pass = all_pass and r1

    # 测试2: 非法 role 值 → False
    bad_role = [{"role": "system", "content": "x"}, {"role": "boss", "content": "y"}]
    r2 = validate_roles(bad_role)
    print(f"{'PASS' if not r2 else 'FAIL'} validate_roles(非法role) -> {r2} | expected: False")
    all_pass = all_pass and not r2

    # 测试3: system 不在首位 → False
    wrong_pos = [{"role": "user", "content": "你好"}, {"role": "system", "content": "x"}]
    r3 = validate_roles(wrong_pos)
    print(f"{'PASS' if not r3 else 'FAIL'} validate_roles(system不在首位) -> {r3} | expected: False")
    all_pass = all_pass and not r3

    # 测试4: 重复 system → False
    dup_sys = [{"role": "system", "content": "a"}, {"role": "system", "content": "b"}]
    r4 = validate_roles(dup_sys)
    print(f"{'PASS' if not r4 else 'FAIL'} validate_roles(重复system) -> {r4} | expected: False")
    all_pass = all_pass and not r4

    # ---------- Part 2: 带 system 角色的 API 测试 ----------

    key = load_api_key()
    if not key or "你的" in key:
        print("请先在 .env 文件中配置 DEEPSEEK_API_KEY")
        exit(1)

    # 测试5: system 设定角色 — 英语老师
    reply5 = chat_with_system("你是一位严格的英语老师，用英文回答所有问题",
                              [], "早上好怎么说？", key)
    print(f"{'PASS' if 'good morning' in reply5.lower() else 'FAIL'} "
          f"chat_with_system(英语老师) -> {reply5!r} | expected: 含 good morning")
    all_pass = all_pass and ("good morning" in reply5.lower())

    # 测试6: system 设定角色 — 翻译官
    reply6 = chat_with_system("你是一个中译英翻译官，只输出英文译文",
                              [], "我喜欢学习编程", key)
    print(f"{'PASS' if reply6 and all(ord(c) < 128 for c in reply6) else 'FAIL'} "
          f"chat_with_system(翻译官) -> {reply6!r} | expected: 纯英文输出")
    all_pass = all_pass and reply6 and all(ord(c) < 128 for c in reply6)

    # 测试7: history 回填 assistant — AI 跨轮记忆
    history = [
        {"role": "user", "content": "我叫小红"},
        {"role": "assistant", "content": "你好小红！很高兴认识你"},
    ]
    reply7 = chat_with_system("你是一个友好的助手", history, "我叫什么名字？", key)
    print(f"{'PASS' if '小红' in reply7 else 'FAIL'} "
          f"chat_with_system(带历史) -> {reply7!r} | expected: 含 小红")
    all_pass = all_pass and ("小红" in reply7)

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
