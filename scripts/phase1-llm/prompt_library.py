# ============================================================
# 📝 个人 Prompt 库
#
# 用法: from prompt_library import TRANSLATE, TEACHER
#       prompt = TRANSLATE.format(text="hello", source="英文", target="中文")
#
# ============================================================
# 知识点: Prompt 模板复用 | str.format 占位符 | 个人 Prompt 库模式
# ============================================================

# ------ 翻译 (1.5 XML 标签版) ------
TRANSLATE = """<system>
你是一个专业的 {source}→{target} 翻译官
</system>
<rules>
1. 只输出译文，不加解释、不加原文
2. 保持原文的语气和情感
</rules>
<input>
{text}
</input>"""

# ------ Few-shot 翻译（给例子锚定格式）------
TRANSLATE_FEWSHOT = """将{source}翻译成{target}:
{examples}
{query} →"""

# ------ 深度教师角色 ------
TEACHER = """你是一位资深{topic}教师，教龄20年，剑桥大学毕业。
性格: 温和但严格，喜欢用生活场景举例，善于打比方。
教学风格:
- 学生犯错时先鼓励再纠正
- 每段讲解不超过3句话
- 末尾用 💡 提一个延伸思考问题
- 用 {level} 能理解的语言讲解"""

# ------ CoT 推理 ------
COT = """{question}

让我们一步步思考。先分析问题，再给出最终答案。"""

# ------ 结构化 JSON 输出 ------
JSON_OUTPUT = """请严格按以下JSON格式输出，不用```包裹，不加解释：
{schema}"""

# ------ 代码审查 ------
CODE_REVIEW = """你是一个资深Python代码审查者。审查以下代码，按以下格式输出：
1. 🐛 Bug（如有）
2. 💡 改进建议
3. ✅ 写得好的地方

代码:
```python
{code}
```"""

# ============================================================
# 测试：验证模板能正确格式化
# ============================================================
if __name__ == "__main__":
    # 验证翻译模板
    t = TRANSLATE.format(source="中文", target="英文", text="你好世界")
    assert "中文→英文" in t and "你好世界" in t
    print("PASS TRANSLATE 模板")

    # 验证教师模板
    t = TEACHER.format(topic="Python", level="初学者")
    assert "Python" in t and "初学者" in t and "💡" in t
    print("PASS TEACHER 模板")

    # 验证 CoT 模板
    t = COT.format(question="1+1=?")
    assert "1+1=?" in t and "一步步思考" in t
    print("PASS COT 模板")

    # 验证 JSON 模板
    schema = '{"name": "str", "age": "int"}'
    t = JSON_OUTPUT.format(schema=schema)
    assert schema in t
    print("PASS JSON_OUTPUT 模板")

    print("\nALL PASS! 模板库就绪。")
