# Day 2 — 2026-07-22

## 今天学了什么
- 文件读写进阶：`with open()` 自动管理资源、`f.readlines()` 读所有行
- 异常处理双重用法：`FileNotFoundError` + `ValueError` 分别处理不同异常
- CSV 解析套路：读行 → strip → split → 类型转换 → 收集
- 面向对象基础：`class` 定义类、`__init__` 构造方法、`self` 的含义
- 实例属性 vs 实例方法：属性不加括号，方法要加
- `__repr__` 魔法方法：控制 `print(obj)` 的输出
- 对象列表操作：遍历列表中的对象，访问对象属性
- 状态管理：用布尔属性 `available` 控制借还状态
- 继承概念：`class A(B):`、`super().__init__()`、方法覆盖（骨架已出）

## 今天写了什么代码
- csv_stats.py — CSV 数据统计（文件读写 + 异常处理 + 脏数据跳过），5/5 测试通过
- library_system.py — 图书馆管理系统（Book 类 + Library 类），16/16 测试通过
- employee_system.py — 员工管理系统骨架（继承练习），下次完成

## 今天踩了什么坑
- `FileExistsError` 写成 `FileNotFoundError` 的反义词 → 异常名必须精确
- `if lines <= 1` 列表和整数直接比较 → 容器用 `len()` 取长度
- `for line in lines` 没加 `[1:]` 跳过表头 → 列名被当数据处理
- 找最高分写成 `if score < max_score` → 比较方向想清楚再写
- `self.books = None` 不能遍历 → 容器属性初始化为空列表 `[]`
- `b.title()` 把属性当方法调 → 属性不加括号
- `return False` 缩进在 for 循环里面 → 找完才能返回，缩进决定逻辑归属
- 测试用例设计：搜拼音搜不到中文书名 → 测试数据要真实可达
- Windows 终端 GBK 编码不认 emoji → `✅` `❌` 换成英文标记

## 今天的一个收获
- 从"函数思维"过渡到"对象思维"：函数只做一件事，对象是"数据 + 行为"打包
- 找 bug 不再靠猜，靠跑测试 + 读报错堆栈，效率和信心都上来了
- 同一个坑不踩两次：缩进问题、遍历前判空、异常名写对，今天都内化了

## 明天计划
- 完成 employee_system.py（继承 + super() + 方法覆盖）
- 推进到 dataclass 或 Type hints
- 更新 LEARNING_TRACKER.md checkbox
- 记得 git add / commit / push

## 自我评分 (1-5)
- 理解程度: 4
- 完成度: 4
- 投入度: 5
