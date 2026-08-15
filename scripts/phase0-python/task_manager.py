# ============================================================
# 练习: 任务管理系统（dataclass + Type hints）
#
# 背景: 在 employee_system.py 里你手写了 3 个类的 __init__ 和 __repr__，
#       每个类至少 10 行样板代码。@dataclass 可以一行搞定。
#
# 实现要求:
#
#   Part 1 — TaskItem (dataclass)
#     用 @dataclass 定义任务数据类，字段:
#       title: str            — 任务标题
#       priority: int = 1     — 优先级 1-5，默认 1
#       done: bool = False    — 是否完成，默认 False
#       tags: list[str] = field(default_factory=list)  — 标签列表，默认空列表
#     ⚠️ 可变默认值不能用 default=[]，必须用 default_factory=list
#     dataclass 自动生成 __init__ / __repr__ / __eq__，不需要手写
#
#   Part 2 — 普通类 vs dataclass 对比
#     class TaskOld — 手写 __init__ + __repr__（和 Day 2/3 一样）
#     然后测试 TaskItem 和 TaskOld 创建出来的对象是否相等
#
#   Part 3 — Type hints 类型进阶
#     from typing import Literal, Optional
#     - Optional[str] 等价于 str | None（可选值）
#     - Literal["high", "medium", "low"] 限制只能选这几个字符串
#
#     在 TaskItem 上添加:
#       category: Optional[str] = None   — 可选分类，默认为空
#       把 priority 从 int 改成 Literal[1, 2, 3, 4, 5] 限制范围
#
# ============================================================
# 知识点: @dataclass | field(default_factory=list) | 可变默认参数陷阱 | Optional | Literal | 类型注解 vs 赋值
# ============================================================

from dataclasses import dataclass, field
from typing import Optional, Literal

# ---------- Part 1: dataclass 版本 ----------

@dataclass
class TaskItem:
    """任务数据类 — 用 @dataclass 省去样板代码"""
    title: str
    priority: Literal[1,2,3,4,5] = 1 # 限定选择并给予默认值
    done: bool = False 
    tags: list[str] = field(default_factory=list) # 对于可变类型参数的写法
    category: Optional[str] = None

# ---------- Part 2: 手写版本（对比用）----------

class TaskOld:
    """手写 __init__ + __repr__ 的传统类"""
    def __init__(self, title: str, priority: int = 1, done: bool = False):
        self.title = title
        self.priority = priority
        self.done = done
        self.tags: list[str] = []

    def __repr__(self):
        return f"TaskOld(title={self.title!r}, priority={self.priority}, done={self.done})"

# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True

    # 测试1: 基本创建 + 默认值
    t1 = TaskItem(title="学 dataclass")
    if t1.title == "学 dataclass" and t1.priority == 1 and t1.done == False:
        print(f"PASS 默认值创建 -> {t1}")
    else:
        print(f"FAIL 默认值创建 -> title={t1.title}, priority={t1.priority}, done={t1.done}")
        all_pass = False

    # 测试2: 指定全部字段
    t2 = TaskItem(title="写代码", priority=5, done=True)
    if t2.priority == 5 and t2.done == True:
        print(f"PASS 全字段创建 -> {t2}")
    else:
        print(f"FAIL 全字段创建 -> {t2}")
        all_pass = False

    # 测试3: tags 默认是空列表
    if t1.tags == []:
        print(f"PASS tags默认空列表 -> {t1.tags}")
    else:
        print(f"FAIL tags默认空列表 -> {t1.tags}")
        all_pass = False

    # 测试4: tags 各自独立（可变默认参数陷阱验证）
    t3 = TaskItem(title="任务A")
    t4 = TaskItem(title="任务B")
    t3.tags.append("urgent")
    if t4.tags == []:
        print(f"PASS tags独立 -> t3={t3.tags}, t4={t4.tags}")
    else:
        print(f"FAIL tags互相污染 -> t4.tags={t4.tags} | expected: []")
        all_pass = False

    # 测试5: 自动生成的 __repr__
    r = repr(t2)
    if "写代码" in r and "priority=5" in r and "done=True" in r:
        print(f"PASS 自动__repr__ -> {r}")
    else:
        print(f"FAIL 自动__repr__ -> {r}")
        all_pass = False

    # 测试6: 自动生成的 __eq__
    t5 = TaskItem(title="学 dataclass")  # 默认 priority=1, done=False
    if t1 == t5:
        print(f"PASS 自动__eq__ -> t1 == t5")
    else:
        print(f"FAIL 自动__eq__ -> t1 != t5")
        all_pass = False

    # 测试7: TaskOld 手写类 vs TaskItem dataclass 对比
    old = TaskOld(title="学 dataclass")
    # TaskOld 创建的对象应该和 t1 有相同的 title
    if old.title == t1.title:
        print(f"PASS TaskOld基础 -> {old.title}")
    else:
        print(f"FAIL TaskOld基础")
        all_pass = False

    # 测试8: Optional 字段默认 None
    if t1.category is None:
        print(f"PASS category默认None -> {t1.category}")
    else:
        print(f"FAIL category默认None -> {t1.category}")
        all_pass = False

    # 测试9: Optional 字段可赋值
    t1.category = "Python学习"
    if t1.category == "Python学习":
        print(f"PASS category赋值 -> {t1.category}")
    else:
        print(f"FAIL category赋值 -> {t1.category}")
        all_pass = False

    # 测试10: Literal 类型限制（运行时不会报错，但 type checker 会提示）
    # 确认 priority 可以是 1-5 的整数
    valid = all(t.priority in [1,2,3,4,5] for t in [t1, t2, t3, t4, t5])
    if valid:
        print(f"PASS priority范围验证 -> 所有任务的priority都在1-5")
    else:
        print(f"FAIL priority范围验证")
        all_pass = False

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
