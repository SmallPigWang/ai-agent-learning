# ============================================================
# 练习: 员工管理系统（继承 + super() + 方法覆盖）
#
# 实现三层类:
#
#   Employee — 基类
#     __init__(self, name: str, emp_id: str, salary: float)
#       属性: name 姓名, emp_id 工号, salary 月薪
#     get_bonus(self) → 返回年终奖 = salary * 0.1（10%）
#     __repr__(self) → 返回 "name (emp_id) - ¥salary/月"
#       薪资金额保留 0 位小数，如 ¥15000/月
#
#   Manager(Employee) — 经理，继承 Employee
#     __init__(self, name: str, emp_id: str, salary: float, team_size: int = 0)
#       通过 super() 调用父类 __init__，再添加 team_size 属性
#     get_bonus(self) → 覆盖父类方法，年终奖 = salary * 0.2 + team_size * 1000
#     add_team_member(self) → team_size + 1，无返回值
#     __repr__(self) → "name (emp_id) - Manager | ¥salary/月 | team: team_size人"
#
#   Developer(Employee) — 开发者，继承 Employee
#     __init__(self, name: str, emp_id: str, salary: float, skills: list = None)
#       通过 super() 调用父类 __init__，skills 默认为空列表
#       注意: skills 不能用可变默认参数 skills=[]，要用 skills=None + if skills is None
#     get_bonus(self) → 覆盖父类方法，年终奖 = salary * 0.15 + 掌握的技能数 * 2000
#     add_skill(self, skill: str) → 添加技能到列表，无返回值
#     __repr__(self) → "name (emp_id) - Developer | ¥salary/月 | skills: [skill1, skill2]"
# ============================================================
# 知识点: 继承 class A(B) | super().__init__ | 方法覆盖 | 可变默认参数 None 处理 | join 拼接列表
# ============================================================
from __future__ import annotations


class Employee:
    """基类: 普通员工"""

    def __init__(self, name: str, emp_id: str, salary: float):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def get_bonus(self) -> float:
        return self.salary * 0.1

    def __repr__(self):
        return f"{self.name} ({self.emp_id}) - ¥{self.salary:.0f}/月"


class Manager(Employee):
    """经理，继承 Employee"""

    def __init__(self, name: str, emp_id: str, salary: float, team_size: int = 0):
        super().__init__(name=name, emp_id=emp_id, salary=salary)
        self.team_size = team_size

    def get_bonus(self) -> float:
        return self.salary * 0.2 + self.team_size * 1000

    def add_team_member(self) -> None:
        self.team_size += 1

    def __repr__(self):
        return (
            f"{self.name} ({self.emp_id}) - Manager"
            f" | ¥{self.salary:.0f}/月 | team: {self.team_size}人"
        )


class Developer(Employee):
    """开发者，继承 Employee"""

    def __init__(
        self, name: str, emp_id: str, salary: float, skills: list[str] | None = None
    ):
        super().__init__(name, emp_id, salary)
        self.skills: list[str] = skills if skills is not None else []

    def get_bonus(self) -> float:
        return self.salary * 0.15 + len(self.skills) * 2000

    def add_skill(self, skill: str) -> None:
        self.skills.append(skill)

    def __repr__(self):
        return (
            f"{self.name} ({self.emp_id}) - Developer"
            f" | ¥{self.salary:.0f}/月 | skills: [{', '.join(self.skills)}]"
        )


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True

    # 测试1: Employee 基本属性
    e1 = Employee("张三", "E001", 8000)
    if e1.name == "张三" and e1.emp_id == "E001" and e1.salary == 8000:
        print(f"PASS Employee属性 -> {e1.name}, {e1.emp_id}, {e1.salary}")
    else:
        print(
            f"FAIL Employee属性 -> name={e1.name}, id={e1.emp_id}, salary={e1.salary}"
        )
        all_pass = False

    # 测试2: Employee.get_bonus()
    bonus = e1.get_bonus()
    if bonus == 800.0:
        print(f"PASS Employee年终奖 -> {bonus}")
    else:
        print(f"FAIL Employee年终奖 -> {bonus} | expected: 800.0")
        all_pass = False

    # 测试3: Employee.__repr__()
    if repr(e1) == "张三 (E001) - ¥8000/月":
        print(f"PASS Employee.__repr__ -> {e1!r}")
    else:
        print(f"FAIL Employee.__repr__ -> {e1!r} | expected: 张三 (E001) - ¥8000/月")
        all_pass = False

    # 测试4: Manager 继承属性
    m1 = Manager("李四", "M001", 15000, team_size=5)
    if (
        m1.name == "李四"
        and m1.emp_id == "M001"
        and m1.salary == 15000
        and m1.team_size == 5
    ):
        print(f"PASS Manager继承属性 -> {m1.name}, team_size={m1.team_size}")
    else:
        print(
            f"FAIL Manager继承属性 -> {m1.name}, {m1.emp_id}, {m1.salary}, team_size={m1.team_size}"
        )
        all_pass = False

    # 测试5: Manager 默认 team_size
    m2 = Manager("王五", "M002", 12000)
    if m2.team_size == 0:
        print("PASS Manager默认team_size -> 0")
    else:
        print(f"FAIL Manager默认team_size -> {m2.team_size} | expected: 0")
        all_pass = False

    # 测试6: Manager.get_bonus() 覆盖
    # salary=15000, team_size=5 → 15000*0.2 + 5*1000 = 3000 + 5000 = 8000
    if m1.get_bonus() == 8000.0:
        print(f"PASS Manager年终奖 -> {m1.get_bonus()}")
    else:
        print(f"FAIL Manager年终奖 -> {m1.get_bonus()} | expected: 8000.0")
        all_pass = False

    # 测试7: Manager.add_team_member()
    m2.add_team_member()
    m2.add_team_member()
    if m2.team_size == 2:
        print(f"PASS Manager扩团队 -> team_size={m2.team_size}")
    else:
        print(f"FAIL Manager扩团队 -> {m2.team_size} | expected: 2")
        all_pass = False

    # 测试8: Manager.__repr__()
    if repr(m1) == "李四 (M001) - Manager | ¥15000/月 | team: 5人":
        print(f"PASS Manager.__repr__ -> {m1!r}")
    else:
        print(
            f"FAIL Manager.__repr__ -> {m1!r} | expected: 李四 (M001) - Manager | ¥15000/月 | team: 5人"
        )
        all_pass = False

    # 测试9: Developer 继承 + 默认 skills
    d1 = Developer("赵六", "D001", 20000)
    if d1.name == "赵六" and d1.skills == []:
        print(f"PASS Developer空技能 -> {d1.name}, skills={d1.skills}")
    else:
        print(f"FAIL Developer空技能 -> name={d1.name}, skills={d1.skills}")
        all_pass = False

    # 测试10: Developer 带技能初始化
    d2 = Developer("钱七", "D002", 18000, skills=["Python", "Java"])
    if d2.skills == ["Python", "Java"]:
        print(f"PASS Developer技能初始化 -> {d2.skills}")
    else:
        print(f"FAIL Developer技能初始化 -> {d2.skills} | expected: ['Python', 'Java']")
        all_pass = False

    # 测试11: Developer.get_bonus() 覆盖
    # d2: salary=18000, 2个技能 → 18000*0.15 + 2*2000 = 2700 + 4000 = 6700
    if d2.get_bonus() == 6700.0:
        print(f"PASS Developer年终奖 -> {d2.get_bonus()}")
    else:
        print(f"FAIL Developer年终奖 -> {d2.get_bonus()} | expected: 6700.0")
        all_pass = False

    # 测试12: Developer.add_skill()
    d1.add_skill("JavaScript")
    d1.add_skill("TypeScript")
    if d1.skills == ["JavaScript", "TypeScript"]:
        print(f"PASS Developer添加技能 -> {d1.skills}")
    else:
        print(
            f"FAIL Developer添加技能 -> {d1.skills} | expected: ['JavaScript', 'TypeScript']"
        )
        all_pass = False

    # 测试13: Developer.__repr__()
    if repr(d2) == "钱七 (D002) - Developer | ¥18000/月 | skills: [Python, Java]":
        print(f"PASS Developer.__repr__ -> {d2!r}")
    else:
        print(
            f"FAIL Developer.__repr__ -> {d2!r} | expected: 钱七 (D002) - Developer | ¥18000/月 | skills: [Python, Java]"
        )
        all_pass = False

    # 测试14: isinstance 验证继承关系
    if isinstance(m1, Employee) and isinstance(d2, Employee):
        print("PASS 继承链验证 -> Manager和Developer都是Employee的子类")
    else:
        print("FAIL 继承链验证")
        all_pass = False

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
