# ============================================================
# 练习: 双模型对比 —— 同一问题，不同模型回答
#
# 核心认知: 不同模型对同一个问题有不同"理解"和"风格"
#          这不是 bug，是训练数据 + 架构 + 对齐策略的差异
#
# 你已经学过:
#   - Messages API 四角色（system/user/assistant/tool）
#   - 流式输出（stream=True + iter_lines + yield）
#   - API 调用通用结构（URL + headers + body）
#
# 你要实现:
#   compare_models(prompt, api_key_deepseek, api_key_claude) -> dict
#     同时调用 DeepSeek 和 Claude（串行即可），返回两个模型的回答
#     返回格式: {"deepseek": "...", "claude": "..."}
#
# 新知识: 不同模型的"人格"差异
#   - DeepSeek: 中文语感好、回答直接、性价比高
#   - Claude: 英文逻辑强、安全意识高、可能拒绝某些问题
#
# ============================================================
# 知识点: 双模型对比 | OpenAI 兼容格式通用客户端 | 模型人格差异 | 换 base_url 调不同模型
# ============================================================

import os
import requests
from dotenv import load_dotenv

# ---------- 复用 ----------

def load_api_key(key_name: str) -> str | None:
    """加载指定的 API Key"""
    load_dotenv()
    return os.getenv(key_name)


# ---------- 待实现 ----------

def call_model(prompt: str, api_key: str, model: str,
               base_url: str, system_prompt: str = "") -> str:
    """
    通用模型调用 —— 支持任何 OpenAI 兼容 API
    流程:
      1. 构造 messages: system(可选) + user(prompt)
      2. url = base_url + "/chat/completions"
      3. headers / body 同以往
      4. 发送并返回 AI 回复文本
    提示: 如果 system_prompt 为空字符串，不加 system 消息
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})

    url = base_url

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": model,
        "messages": messages,
        "max_tokens": 1024
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()["choices"][0]["message"]["content"]

    


def compare_models(prompt: str, deepseek_key: str, claude_key: str,
                   claude_base: str) -> dict[str, str]:
    """
    同时调用两个模型，返回对比结果
    流程:
      1. 调用 call_model(prompt, deepseek_key, "deepseek-v4-flash",
                         "https://api.deepseek.com/chat/completions")  ← 注意 deepseek url 已经是完整路径
      2. 调用 call_model(prompt, claude_key, "claude-haiku-4-5-20251001",
                         claude_base)
      3. return {"deepseek": deepseek回答, "claude": claude回答}
    提示: call_model 的 base_url 参数 DeepSeek 和 Claude 不一样——
          DeepSeek 的已经是完整 URL（含/chat/completions），
          Claude 的需要拼接 base_url + "/chat/completions"
          → 直接传 DeepSeek 完整 URL 即可，拼接逻辑在 call_model 里
    """
    # 调用deepseek
    deepseek_reply = call_model(
        prompt=prompt,
        api_key=deepseek_key,
        model="deepseek-v4-flash",
        base_url="https://api.deepseek.com/chat/completions"
    )

    # 调claude中转
    claude_reply = call_model(
        prompt=prompt,
        api_key=claude_key,
        model="claude-haiku-4-5-20251001",
        base_url=claude_base,
    )

    return {"deepseek": deepseek_reply, "claude": claude_reply}


def stream_compare(prompt: str, deepseek_key: str, claude_key: str,
                   claude_base: str):
    """
    流式对比 —— 先打 DeepSeek 流式输出，再打 Claude 流式输出
    流程:
      1. print "=== DeepSeek ==="
      2. 流式调用 DeepSeek，逐块 print（复用 stream_chat.py 的逻辑）
      3. print "\n=== Claude ==="
      4. 流式调用 Claude，逐块 print
    提示: 可以直接搬 stream_chat.py 的 stream_chat 函数
    """
    import json as _json

    # ---------- DeepSeek ----------
    print("=== DeepSeek ===")
    messages = [{"role": "user", "content": prompt}]
    body = {
        "model": "deepseek-v4-flash",
        "messages": messages,
        "max_tokens": 1024,
        "stream": True,
    }
    response = requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {deepseek_key}",
                 "Content-Type": "application/json"},
        json=body,
        stream=True,
    )
    for line in response.iter_lines():
        if not line:
            continue
        text = line.decode("utf-8")
        if not text.startswith("data: "):
            continue
        text = text[6:]
        if text == "[DONE]":
            break
        data = _json.loads(text)
        choices = data.get("choices", [])
        if not choices:
            continue
        delta = choices[0].get("delta", {})
        content = delta.get("content")
        if content:
            print(content, end="", flush=True)
    print()

    # ---------- Claude ----------
    print("=== Claude ===")
    body["model"] = "claude-haiku-4-5-20251001"
    body["messages"] = messages
    response = requests.post(
        claude_base,
        headers={"Authorization": f"Bearer {claude_key}",
                 "Content-Type": "application/json"},
        json=body,
        stream=True,
    )
    for line in response.iter_lines():
        if not line:
            continue
        text = line.decode("utf-8")
        if not text.startswith("data: "):
            continue
        text = text[6:]
        if text == "[DONE]":
            break
        data = _json.loads(text)
        choices = data.get("choices", [])
        if not choices:
            continue
        delta = choices[0].get("delta", {})
        content = delta.get("content")
        if content:
            print(content, end="", flush=True)
    print()
    print("=== DeepSeek")
    


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True

    dk = load_api_key("DEEPSEEK_API_KEY")
    ck = load_api_key("JIEKOU_API_KEY")
    cb = (load_api_key("JIEKOU_BASE_URL") or "https://api.highwayapi.ai/openai/v1") + "/chat/completions"

    if not dk or not ck or "你的" in dk or "你的" in ck:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY 和 JIEKOU_API_KEY")
        exit(1)

    # 测试1: call_model — DeepSeek 能调用
    r1 = call_model("1+1=？只回答数字", dk,
                    "deepseek-v4-flash", "https://api.deepseek.com/chat/completions")
    print(f"{'PASS' if '2' in r1 else 'FAIL'} DeepSeek -> {r1!r}")
    all_pass = all_pass and "2" in r1

    # 测试2: call_model — Claude 能调用
    r2 = call_model("1+1=？只回答数字", ck,
                    "claude-haiku-4-5-20251001", cb)
    print(f"{'PASS' if '2' in r2 else 'FAIL'} Claude -> {r2!r}")
    all_pass = all_pass and "2" in r2

    # 测试3: compare_models — 同时调用两个模型
    result = compare_models("用一句话介绍人工智能", dk, ck, cb)
    print(f"DeepSeek: {result.get('deepseek', '')[:50]!r}...")
    print(f"Claude:   {result.get('claude', '')[:50]!r}...")
    r3 = result.get("deepseek") and result.get("claude")
    print(f"{'PASS' if r3 else 'FAIL'} compare_models -> 两个都有回答")
    all_pass = all_pass and r3

    # 测试4: stream_compare — 流式对比
    print("\n=== 流式对比: 用一句话介绍你自己 ===")
    stream_compare("用一句话介绍你自己", dk, ck, cb)

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
