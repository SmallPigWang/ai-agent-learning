# ============================================================
# 练习3: 成绩解析
#   实现 parse_scores(text) 函数
#   输入: "Alice:85, Bob:92, Charlie:78" 格式的字符串
#   输出: 一个字典 {"最高分": (名字, 分数), "平均分": 平均值}
#   空字符串返回 None，分数不是数字时跳过该条
#   平均值保留 2 位小数
# ============================================================

def parse_scores(text: str):
    """解析成绩字符串，返回最高分和平均分"""
    if not text:
        return None
    
    student = text.split(",")
    count = 0
    max_score = 0
    max_name = None
    total = 0
    for i in student:
        info = i.split(":")
        name = info[0].strip()
        try:
            score = float(info[1])
            count += 1
        except ValueError:
            continue

        if score > max_score:
            max_score = score
            max_name = name
        total += score
    
    avg = total / count
    return {"最高分": (max_name, max_score),"平均分":round(avg,2)}

    
# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    tests = [
        ("Alice:85, Bob:92, Charlie:78",
         {"最高分": ("Bob", 92), "平均分": 85.0}),
        ("张三:100",
         {"最高分": ("张三", 100), "平均分": 100.0}),
        ("",
         None),
        ("Tom:60, Jerry:abc, Spike:80",
         {"最高分": ("Spike", 80), "平均分": 70.0}),
    ]

    for text, expected in tests:
        result = parse_scores(text)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} parse_scores('{text}') -> {result} | expected: {expected}")
