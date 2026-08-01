# ============================================================
# 练习: Structured Output —— 让 LLM 输出可被代码安全消费的 JSON
#
# 核心认知:
#   LLM 的文本输出 → json.loads → dict → 代码安全使用
#   关键不是"让 LLM 输出 JSON"（你已经会），而是"输出一定合法"
#
# Pydantic 新知识:
#   BaseModel = 一个类，定义数据"长什么样"
#   字段名: 类型 = 默认值 → 自动校验、自动转换
#   例子:
#     class Person(BaseModel):
#         name: str              # 必须有，必须是 str
#         age: int = 0           # 必须是 int，默认 0
#     p = Person(name="小明")    # ✅ 自动校验
#     p = Person(name=123)       # ❌ ValidationError
#
# 你要实现:
#   generate_recipe(dish, key) — LLM 生成菜谱 → Pydantic 校验 → 返回 Recipe 对象
#
# ============================================================

import os
import json as _json
import re as _re
import requests
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# ---------- Schema 定义 ----------

class Ingredient(BaseModel):
    """食材"""
    name: str = Field(description="食材名称")
    amount: str = Field(description="用量，如 '200g'、'2个'")


class Recipe(BaseModel):
    """菜谱"""
    dish_name: str = Field(description="菜名")
    cooking_time: str = Field(description="烹饪时间，如 '30分钟'")
    difficulty: str = Field(description="难度: 简单/中等/困难")
    ingredients: list[Ingredient] = Field(description="食材列表")
    steps: list[str] = Field(description="烹饪步骤")


# ---------- 复用 ----------

def load_api_key(key_name: str) -> str | None:
    load_dotenv()
    return os.getenv(key_name)


def call_ds(prompt: str, key: str, system: str = "") -> str:
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = {"model": "deepseek-v4-flash", "messages": messages, "max_tokens": 1024}
    r = requests.post(url, headers=headers, json=body)
    return r.json()["choices"][0]["message"]["content"]


# ---------- 待实现 ----------

def generate_recipe(dish: str, key: str) -> Recipe | None:
    """
    LLM 生成菜谱 → 解析 → Pydantic 校验 → 返回 Recipe 对象
    流程:
      1. 用 system prompt 告诉 LLM: 你是厨师，只输出 JSON
      2. 在 prompt 中嵌入 JSON Schema（把 Recipe 的字段结构描述出来）
      3. 调 call_ds → 拿到文本回复
      4. 清洗回复（去掉 ``` 代码块）
      5. json.loads 解析 → dict
      6. Recipe(**dict) Pydantic 校验 → Recipe 对象
      7. 如果任何一步失败，返回 None
    提示: Pydantic 可以自动把 dict 转成对象: recipe = Recipe(**parsed_dict)
    """
    # 第 1 步: system prompt
    system = "你是一个专业厨师。只输出 JSON，不加解释，不用 ```。"

    # 第 2 步: 在 prompt 里描述 Schema
    prompt = f"""请为{dish}生成菜谱，严格按以下 JSON 格式输出：
    {{
      "dish_name": "菜名",
      "cooking_time": "30分钟",
      "difficulty": "简单/中等/困难",
      "ingredients": [
        {{"name": "鸡蛋", "amount": "3个"}}
      ],
      "steps": ["第一步...", "第二步..."]
    }}"""

    # 第 3 步: 调 API
    text = call_ds(prompt, key, system=system)

    # 第 4 步: 清洗（去掉 ```json 包裹）正则化语言描述
    text = _re.sub(r"^```(?:json)?\s*\n?", "", text.strip())
    text = _re.sub(r"\n?```\s*$", "", text)

    # 第 5 步: JSON 解析
    data = _json.loads(text)

    # 第 6 步: Pydantic 校验（** 是 Day 1 学过的字典解包）
    return Recipe(**data)




# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        exit(1)

    # 测试1: 生成菜谱 → Pydantic 校验通过
    recipe = generate_recipe("番茄炒蛋", key)
    r1_pass = recipe is not None
    print(f"{'PASS' if r1_pass else 'FAIL'} 生成菜谱 -> {recipe!r}")
    all_pass = all_pass and r1_pass

    if recipe:
        # 测试2: 字段类型校验
        r2_pass = (isinstance(recipe.dish_name, str) and
                   isinstance(recipe.cooking_time, str) and
                   isinstance(recipe.difficulty, str) and
                   isinstance(recipe.ingredients, list) and
                   isinstance(recipe.steps, list))
        print(f"{'PASS' if r2_pass else 'FAIL'} 字段类型 -> dish_name:{type(recipe.dish_name).__name__} "
              f"ingredients:[{len(recipe.ingredients)}] steps:[{len(recipe.steps)}]")
        all_pass = all_pass and r2_pass

        # 测试3: 第一个食材有 name 和 amount
        if recipe.ingredients:
            ing = recipe.ingredients[0]
            r3_pass = hasattr(ing, "name") and hasattr(ing, "amount")
            print(f"{'PASS' if r3_pass else 'FAIL'} Ingredient字段 -> name={ing.name!r} amount={ing.amount!r}")
            all_pass = all_pass and r3_pass

        # 测试4: 必填字段不为空
        r4_pass = all([
            recipe.dish_name,
            recipe.cooking_time,
            recipe.difficulty in ("简单", "中等", "困难"),
            len(recipe.ingredients) >= 2,
            len(recipe.steps) >= 2,
        ])
        print(f"{'PASS' if r4_pass else 'FAIL'} 内容完整 -> "
              f"难度={recipe.difficulty} 食材数={len(recipe.ingredients)} 步骤数={len(recipe.steps)}")
        all_pass = all_pass and r4_pass

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
