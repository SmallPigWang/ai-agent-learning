# Day 3 — 2026-07-31（08:00-09:10）

## 今天学了什么

### 上午：继承
- 继承完整三件套：`class A(B):` 继承语法、`super().__init__()` 调父类构造、方法覆盖
- `super()` 调父类时不传 `self`，自动处理
- `isinstance(obj, Class)` 验证继承关系
- Python 可变默认参数陷阱：`def f(lst=[])` → 所有调用共享同一 list，用 `lst=None` + 内部判空
- `:.0f` 格式化浮点数 → 不显示小数位
- 列表格式化：`', '.join(list)` 拼字符串，不用默认 `str(list)`（会带引号）

### 下午：dataclass + Type hints
- `@dataclass` 装饰器：自动生成 `__init__` / `__repr__` / `__eq__`，省掉 80% 样板代码
- `field(default_factory=list)`：可变默认值的正确写法，每次创建实例时调 `list()` 生成新空列表
- dataclass vs 手写类对比：4 行 vs 10 行，且 dataclass 自带 `__eq__`
- `Optional[str]`：声明字段可以是 str 或 None，IDE 不再标黄
- `Literal[1,2,3,4,5]`：限制值只能是这几个字面量，IDE/mypy 检查，运行时不管
- 泛型容器：`list[str]` 不是 `list`，Pylance 要求指明元素类型
- 类型标注 vs 赋值：`变量名: 类型 = 值`，冒号管类型，等号管值

## 今天写了什么代码
- employee_system.py — 三层继承系统（Employee → Manager/Developer），14/14 测试通过
  - Employee 基类：属性 + get_bonus(10%) + __repr__
  - Manager：super().__init__ + 覆盖 get_bonus(20%+团队) + add_team_member
  - Developer：可变默认参数处理 + 覆盖 get_bonus(15%+技能) + add_skill
- task_manager.py — dataclass + Type hints 练习，10/10 测试通过
- first_api_call.py — 第一次 API 调用（DeepSeek），3/3 测试通过
- multi_turn_chat.py — 多轮对话，AI 跨轮记住用户名，3/3 测试通过
  - Part 1: @dataclass TaskItem（4行字段声明，自动生成 3 个魔法方法）
  - Part 2: TaskOld 手写类（对比 dataclass 省了多少代码）
  - Part 3: Optional + Literal 类型进阶

## 今天踩了什么坑
- ￥（全角人民币符号）和 ¥（半角日元符号）不是同一个字符
- Developer.get_bonus 手误写成 0.25，需求是 0.15
- f-string 里 `{列表}` 输出带引号，需用 `', '.join()` 手动拼
- `self.tags = list[str] = []` 语法错误 → 冒号做类型注解，等号做赋值，不能混用
- `self.tags : list[str] = []` 冒号前有空格 → 冒号必须紧跟变量名
- TaskOld.__init__ 有隐藏字符导致 `takes no arguments` → 删除重写解决

## 今天的一个收获
- 继承的本质不是"复用代码"，而是"复用接口"——父类定义契约，子类各自实现
- dataclass 不止是少写代码，更重要的是**语义表达**：一眼看出是纯数据类，字段即契约
- 制定了新规则：练习聚焦当次学习目标，避免因格式细节分心

