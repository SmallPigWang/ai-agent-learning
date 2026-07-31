# ============================================================
# 练习2: 列表统计
#   实现 stats(numbers) 函数
#   输入: 一个数字列表，如 [3, 1, 7, 5, 9]
#   输出: 一个字典，包含 sum(总和), avg(平均值), max(最大值), min(最小值)
#   空列表返回 None
#   平均值保留 2 位小数
# ============================================================

def stats(numbers: list):
    """输入数字列表，返回统计字典"""
    # 列表为空
    if not numbers:
        return None
    
    n = len(numbers)
    total = sum(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    
    avg = total / n
    
    return {"sum": total, "avg":round(avg,2),"max":max_val,"min":min_val}
    
    

    


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    tests = [
        ([3, 1, 7, 5, 9], {"sum": 25, "avg": 5.0, "max": 9, "min": 1}),
        ([100], {"sum": 100, "avg": 100.0, "max": 100, "min": 100}),
        ([], None),
        ([-5, 0, 5], {"sum": 0, "avg": 0.0, "max": 5, "min": -5}),
    ]

    for nums, expected in tests:
        result = stats(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} stats({nums}) -> {result} | expected: {expected}")
