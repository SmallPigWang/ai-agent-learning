# ============================================================
# 练习: 结构化 Prompt + 角色扮演
#
# 核心认知:
#   - XML 标签 = 给 AI 的"代码注释"，精确划分指令区域
#   - 深度角色 = 不只用 system 说"你是谁"，而是描述性格+规则+典型反应
#
# 你要实现:
#   xml_translate(text, source, target, key)  — XML 标签约束翻译
#   roleplay_tutor(topic, student_level, key)  — 深度角色扮演教学
#
# ============================================================
# 知识点: XML 标签划分指令区域 | 深度角色四要素 | 水平差异化教学 | f-string 前缀
# ============================================================

import os
import requests
from dotenv import load_dotenv

# ---------- 复用 ----------

def load_api_key(key_name: str) -> str | None:
    load_dotenv()
    return os.getenv(key_name)


def call_ds(prompt: str, key: str, system: str = "") -> str:
    """快捷调用 DeepSeek，可选 system prompt"""
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = {"model": "deepseek-v4-flash", "messages": messages, "max_tokens": 512}
    r = requests.post(url, headers=headers, json=body)
    return r.json()["choices"][0]["message"]["content"]


# ---------- 待实现 ----------

def xml_translate(text: str, source: str, target: str, key: str) -> str:
    """
    用 XML 标签结构约束翻译行为，返回纯译文
    流程:
      1. 构造 prompt，用 <system>、<rules>、<input> 三个标签包裹
      2. system: 你是一个专业的 {source}→{target} 翻译官
      3. rules:
         - 只输出译文，不加解释、不加原文
         - 保持原文的语气和情感
      4. input: {text}
      5. 调 call_ds(prompt, key, system="") → 直接返回
    提示: 用三引号字符串 + f-string 构造 XML 结构
    """
    # XML格式引入 要三个引号导入
    prompt = f"""<system>
    你是一个专业的 {source}→{target} 翻译官
    </system>
    <rules>
    1. 只输出译文，不加解释、不加原文
    2. 保持原文的语气和情感
    </rules>
    <input>
    {text}
    </input>"""
    return call_ds(prompt=prompt, key=key)


def roleplay_tutor(topic: str, student_level: str, key: str) -> str:
    """
    深度角色扮演：AI 扮演一位资深教师来讲解知识点
    流程:
      1. 用 system prompt 设定角色: 资深教师，教龄 20 年，风格温和严格
      2. 规则: 先鼓励再纠错、每段 ≤ 3 句话、末尾加 💡 延申问题
      3. 用 user prompt 问: "请给一位 {student_level} 水平的学生讲解: {topic}"
      4. 调 call_ds(prompt, key, system=角色描述) → 返回
    提示: system 字数不够多不叫深度角色——至少 4-5 行描述性格+规则
    """

    system = f"""你是一位资深{topic}教师，教龄 20 年，剑桥大学毕业。
    性格: 温和但严格，喜欢用生活场景举例，善于打比方。
    教学风格:
    - 学生犯错时先鼓励再纠正
    - 每段讲解不超过 3 句话
    - 末尾用 💡 提一个延伸思考问题
    - 用 {student_level} 能理解的语言讲解"""

    prompt = f"请给一位 {student_level} 水平的学生讲解: {topic}"

    return call_ds(prompt=prompt, key=key, system=system)


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        exit(1)

    # 测试1: XML 翻译 — 中译英
    r1 = xml_translate("今天天气真好，我们出去玩吧！",
                       source="中文", target="英文", key=key)
    # 译文应该不包含中文字
    has_chinese = any('一' <= c <= '鿿' for c in r1)
    r1_pass = r1 and not has_chinese
    print(f"{'PASS' if r1_pass else 'FAIL'} XML翻译 -> {r1!r}")
    print(f"  {'✅ 纯译文' if not has_chinese else '❌ 混入中文'}")
    all_pass = all_pass and r1_pass

    # 测试2: XML 翻译 — 语气保留（感叹号保留）
    r2 = xml_translate("救命啊！帮帮我！",
                       source="中文", target="英文", key=key)
    r2_pass = "！" not in r2 and ("!" in r2 or "help" in r2.lower())
    print(f"{'PASS' if r2_pass else 'FAIL'} XML翻译(语气) -> {r2!r}")
    all_pass = all_pass and r2_pass

    # 测试3: 角色扮演 — 讲概念
    r3 = roleplay_tutor("递归函数", "初学者", key)
    print(f"角色扮演(递归): {r3[:120]!r}...")
    r3_pass = ("递归" in r3 or "recursion" in r3.lower()) and len(r3) > 50
    print(f"{'PASS' if r3_pass else 'FAIL'} 角色扮演 -> 内容充足且相关")
    all_pass = all_pass and r3_pass

    # 测试4: 角色扮演 — 不同水平不同讲解方式
    beginner = roleplay_tutor("for 循环", "小学生", key)
    advanced = roleplay_tutor("for 循环", "资深程序员", key)
    # 小学生版本应该更通俗，两者不应完全一致
    r4_pass = len(beginner) > 30 and len(advanced) > 30 and beginner != advanced
    print(f"小学生版: {beginner[:60]!r}...")
    print(f"程序员版: {advanced[:60]!r}...")
    print(f"{'PASS' if r4_pass else 'FAIL'} 角色扮演(水平差异) -> 两个版本不同")
    all_pass = all_pass and r4_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
