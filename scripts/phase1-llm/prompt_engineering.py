# ============================================================
# 练习: Prompt Engineering —— 同一任务，3 种 Prompt 对比
#
# 核心认知: 同一个模型、同一个问题，Prompt 写法不同 → 效果天差地别
#
# 你要实现:
#   prompt_zero_shot(prompt, key)         — Zero-shot: 直接问
#   prompt_few_shot(examples, query, key) — Few-shot: 先给例子再问
#   prompt_cot(question, key)             — CoT: 让 AI 一步步思考
#
# 三个函数都调 DeepSeek（串行即可），返回 AI 回答
#
# 新知识: Prompt 是 LLM 的"编程语言"
#   - Zero-shot = 不给例子直接问（最基础）
#   - Few-shot  = 给 2-3 个例子，AI 自动模仿格式
#   - CoT       = 加 "让我们一步步思考" → 推理能力飙升
#
# ============================================================

import os
import requests
from dotenv import load_dotenv

# ---------- 复用 ----------

def load_api_key(key_name: str) -> str | None:
    load_dotenv()
    return os.getenv(key_name)


def call_ds(prompt: str, key: str) -> str:
    """快捷调用 DeepSeek（你 compare_models.py 里已经有 call_model，搬过来）"""
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    body = {
        "model": "deepseek-v4-flash",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 512,
    }
    r = requests.post(url, headers=headers, json=body)
    return r.json()["choices"][0]["message"]["content"]


# ---------- 待实现 ----------

def prompt_zero_shot(task: str, key: str) -> str:
    """
    Zero-shot: 直接问，不给例子
    例子: task="把 Hello 翻译成中文" → 直接返回 AI 翻译结果
    """
    return call_ds(prompt=task, key=key)


def prompt_few_shot(examples: list[tuple[str, str]], query: str, key: str) -> str:
    """
    Few-shot: 先给例子，再提问
    examples = [("Hello", "你好"), ("Thank you", "谢谢")]
    query = "Goodbye"
    流程:
      1. 把 examples 格式化成 "输入 → 输出" 的多行字符串
      2. 拼到 prompt 前面: "将英文翻译成中文:\nHello → 你好\nThank you → 谢谢\nGoodbye →"
      3. 调 API 返回结果
    """
    examples_lines = []
    for inp, out in examples:
        examples_lines.append(f"{inp} → {out}")

    examples_text = "\n".join(examples_lines)

    prompt = f"将英文翻译成中文:\n{examples_text}\n{query} →"

    return call_ds(prompt=prompt, key=key)


def prompt_cot(question: str, key: str) -> str:
    """
    CoT (Chain of Thought): 让 AI 逐步推理
    流程:
      1. 在 question 后面追加 "让我们一步步思考。先分析问题，再给出答案。"
      2. 调 API 返回结果
    """
    return call_ds(prompt=question+ "让我们一步步思考。先分析问题，再给出答案。", key=key)


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        exit(1)

    # 测试1: Zero-shot — 翻译
    r1 = prompt_zero_shot("把 'Good morning' 翻译成中文", key)
    print(f"{'PASS' if '早' in r1 else 'FAIL'} Zero-shot -> {r1!r}")
    all_pass = all_pass and "早" in r1

    # 测试2: Few-shot — 翻译（给例子锚定格式）
    examples = [("Hello", "你好"), ("Thank you", "谢谢")]
    r2 = prompt_few_shot(examples, "Goodbye", key)
    print(f"{'PASS' if '再见' in r2 or 'bye' in r2.lower() else 'FAIL'} Few-shot -> {r2!r}")
    all_pass = all_pass and ("再见" in r2 or "bye" in r2.lower())

    # 测试3: Zero-shot vs CoT — 同一个推理题
    question = "小明有 5 个苹果，给了小红 2 个，又买了 3 个，现在有几个？"

    r3_zero = prompt_zero_shot(question + " 直接回答数字", key)
    print(f"Zero-shot: {r3_zero!r}")

    r3_cot = prompt_cot(question + " 直接回答数字", key)
    print(f"CoT:       {r3_cot!r}")

    r3_pass = "6" in r3_zero or "6" in r3_cot
    print(f"{'PASS' if r3_pass else 'FAIL'} CoT 对比 -> 至少一个答对")
    all_pass = all_pass and r3_pass

    # 测试4: 格式控制 — 强制 JSON 输出
    r4 = prompt_zero_shot(
        "列出 3 种水果，用 JSON 数组返回，每个元素有 name 和 emoji 字段。"
        "只输出纯 JSON，不要用 ``` 包裹，不要加任何解释。",
        key
    )
    import json as _json
    import re as _re
    try:
        # 兜底：如果 AI 还是加了代码块，自动剥掉
        clean = _re.sub(r"^```(?:json)?\s*\n?", "", r4.strip())
        clean = _re.sub(r"\n?```\s*$", "", clean)
        parsed = _json.loads(clean)
        r4_pass = isinstance(parsed, list) and len(parsed) == 3
    except Exception:
        r4_pass = False
    print(f"{'PASS' if r4_pass else 'FAIL'} JSON格式控制 -> {r4[:80]!r}...")
    all_pass = all_pass and r4_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
