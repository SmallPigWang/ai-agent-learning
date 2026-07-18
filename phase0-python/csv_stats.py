# ============================================================
# 练习4: CSV 数据统计（文件读写 + f-string）
#   实现 csv_stats(filepath) 函数
#     1. 打开并读取 CSV 文件（第一行是列名，跳过）
#     2. 解析每行数据，格式: "姓名,年龄,分数"
#     3. 年龄不是整数或分数不是数字 → 跳过该行
#     4. 文件不存在 → 返回 None
#     5. 文件为空（只有表头或无内容）→ 返回 None
#   输出: {"总人数": N, "平均年龄": x.x, "最高分": (名字, 分数)}
#   平均值保留 1 位小数
# ============================================================

def csv_stats(filepath: str):
    """读取 CSV 文件，返回年龄和分数的统计数据"""


# ============================================================
# 测试用例（自动创建临时文件 → 测试 → 清理）
# ============================================================
if __name__ == "__main__":
    import os

    def _write_csv(filepath: str, content: str):
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    test_dir = os.path.dirname(os.path.abspath(__file__))

    # 测试1: 正常 CSV
    path1 = os.path.join(test_dir, "_test_normal.csv")
    _write_csv(path1, "姓名,年龄,分数\nAlice,25,85.5\nBob,30,92.0\nCharlie,22,78.0")

    # 测试2: 包含脏数据
    path2 = os.path.join(test_dir, "_test_dirty.csv")
    _write_csv(path2, "姓名,年龄,分数\nTom,20,88.0\nJerry,abc,76.0\nSpike,25,xyz\nMickey,30,95.5")

    # 测试3: 不存在的文件
    path3 = os.path.join(test_dir, "_not_exist.csv")

    # 测试4: 空文件（只有表头）
    path4 = os.path.join(test_dir, "_test_header_only.csv")
    _write_csv(path4, "姓名,年龄,分数")

    # 测试5: 完全空文件
    path5 = os.path.join(test_dir, "_test_empty.csv")
    _write_csv(path5, "")

    tests = [
        (path1, {"总人数": 3, "平均年龄": 25.7, "最高分": ("Bob", 92.0)}),
        (path2, {"总人数": 2, "平均年龄": 25.0, "最高分": ("Mickey", 95.5)}),
        (path3, None),
        (path4, None),
        (path5, None),
    ]

    for filepath, expected in tests:
        result = csv_stats(filepath)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} csv_stats('{filepath}') -> {result} | expected: {expected}")

    # 清理临时文件
    for p in [path1, path2, path4, path5]:
        if os.path.exists(p):
            os.remove(p)
