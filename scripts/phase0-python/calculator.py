# ============================================================
# 练习1: 命令行计算器
#   实现 calculate(expression) 函数
#   输入: "12 + 5"  输出: 17.0
#   支持 + - * /，除数为0返回 "错误: 除数不能为零"
#   不支持的运算符返回 "不支持的运算符"
# ============================================================

def calculate(expression: str):
    """
    输入一个算式字符串，返回计算结果
    格式: "数字 运算符 数字"（空格隔开）
    """
    parts = expression.split()
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "错误: 除数不能为零"
        result = num1 / num2
    else:
        return "不支持的运算符"

    return round(result, 4)


# ============================================================
# 测试用例（跑一遍就知道对不对）
# ============================================================
if __name__ == "__main__":
    tests = [
        ("12 + 5", 17.0),
        ("100 - 30", 70.0),
        ("8 * 7", 56.0),
        ("10 / 3", 3.3333),
        ("10 / 0", "错误: 除数不能为零"),
        ("12 ^ 5", "不支持的运算符"),
    ]

    for expr, expected in tests:
        result = calculate(expr)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} calculate('{expr}') -> {result} | expected: {expected}")
