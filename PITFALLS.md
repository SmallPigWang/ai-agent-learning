# 🕳️ 踩坑清单（PITFALLS）

> 汇总所有学习日志中的踩坑记录，按类别整理，复习时快速过一遍。
> 原则：同一个坑不踩两次。遇到新坑 → 记日志 → 同步到这里。

---

## 1. 语法陷阱

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 1 | IndentationError | 顶层代码有空格 | 顶层代码顶格写，缩进只在块内 |
| 2 | `self.tags = list[str] = []` 语法错误 | 冒号是类型注解，等号是赋值，不能混 | `self.tags: list[str] = []` |
| 3 | `self.tags : list[str] = []` 报错 | 冒号前不能有空格 | 冒号紧跟变量名 |
| 4 | f-string 输出带引号 `'a', 'b'` | `{列表}` 默认 str() 带引号 | `', '.join(list)` 手动拼 |
| 5 | f-string 内 `{'c': 42}` 格式冲突 | `: 42}` 被当成 format specifier | 先存变量再放进 f-string |
| 6 | `text == "DONE"` 永远不触发 | 少写中括号，比较对象错了 | `text == "[DONE]"` 写完整 |
| 7 | f-string 输出 `{student_level}` 字面量 | 漏写 f 前缀 | 检查字符串前有 f |
| 8 | `¥` 显示不对 | 全角 ￥ 和半角 ¥ 不是同一字符 | 复制粘贴，别手打 |

## 2. 逻辑错误

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 9 | 列名被当数据处理 | 遍历 lines 没跳过表头 | `for line in lines[1:]` |
| 10 | 最高分永远是第一个 | `if score < max_score` 方向写反 | 找最大用 `if score > max_score` |
| 11 | 找到第一条就 return False | return 缩进在 for 循环里面 | 循环结束后再 return 结果 |
| 12 | 列表推导结果全是同一个值 | 循环变量名泄漏（msg vs m） | 推导式变量名与循环一致 |
| 13 | json.loads 崩溃 | `text[6:]` 砍前缀后没赋值回变量 | `text = text[6:]` |
| 14 | 返回了 API Key 而不是回复 | 变量名写错（deepseek_key vs deepseek_reply） | 命名语义化，返回前核对 |
| 15 | 奖金算错 | 手误（0.25 vs 需求 0.15） | 写完对照需求注释复查数字 |
| 16 | 容器属性报"不能遍历" | 初始化为 None | 容器属性初始化为空列表 `[]` |

## 3. 类型与 Pylance

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 17 | `if lines <= 1` TypeError | 列表和整数直接比较 | 容器用 `len(lines) <= 1` |
| 18 | 把属性当方法调（b.title()） | 属性与方法混淆 | 属性不加括号 |
| 19 | `self.books = None` 后遍历报错 | None 不可迭代 | 初始化为 `[]` |
| 20 | `takes no arguments` | __init__ 有隐藏字符 | 删除重写该函数 |
| 21 | Pylance 类型缩窄告警 | `fn.get("parameters")` 调两次不跟踪 | 调一次存变量 `para = fn.get(...)` |
| 22 | return False 报类型不匹配 | 函数签名是 `-> tuple` | 按签名返回 (False, 错误消息) |
| 23 | 变量名 max/min 行为诡异 | 盖掉了内置函数 | 别用内置函数名做变量名 |
| 24 | Pylance 标红但运行正常 | 类型定义未声明的方法 | 类型标注 ≠ 运行时行为，`basic` 模式减噪 |

## 4. API 调用

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 25 | 404 错误 | base_url 已是完整路径，又拼了 /chat/completions | 先确认 base_url 是否含路径 |
| 26 | 流式最后一块 IndexError | 最后 choices 为空列表 | `data.get("choices", [])` 防护 |
| 27 | 模型不存在 | 模型 ID 格式错（4.5 vs 4-5） | 模型 ID 用连字符：`claude-haiku-4-5` |
| 28 | 流式没有 content | 推理模型的思考在 reasoning_content | `delta.get("content") or delta.get("reasoning_content")` |
| 29 | 提示词要求 JSON 仍带代码块 | LLM 习惯性包 ```json | 正则 re.sub 剥壳兜底 |
| 30 | KeyError: 'choices' | 消息回填顺序错（tool 在 assistant 前） | 顺序必须 assistant(tool_calls) → tool 结果 → assistant(final) |

## 5. 编码与终端

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 31 | 终端输出 emoji 崩溃 | Windows 终端默认 GBK 编码 | `setx PYTHONUTF8 1` 根治 |
| 32 | 测试标记乱码 | 同上 | 或换成英文 PASS/FAIL 标记 |
| 33 | CMD 长命令被截断 | 命令行长度限制 | 用配置文件代替命令行参数 |

## 6. 工具与 Git

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 34 | Pylance 自动补全不弹窗 | editor.quickSuggestions 被关 | 检查 VS Code 设置 |
| 35 | conda 环境混乱 | 原始源和清华镜像混装 | 只用一个源 |
| 36 | git push 慢/超时 | 国内连 GitHub 网络问题 | 正常现象，小项目可接受；必要时走代理 |
| 37 | 第一次 push 卡住 | 需要浏览器授权 | 按提示完成 OAuth 授权 |

---

## 📌 高频坑 Top 5（重点复习）

1. **消息回填顺序** — assistant(tool_calls) 必须在 tool 结果之前（API 直接报错）
2. **可变默认参数** — `def f(lst=[])` 共享同一 list，用 `None + 判空` 或 `default_factory`
3. **容器判空** — 先 `if not x` 卫语句，再遍历
4. **编码问题** — Windows 终端一律靠 `PYTHONUTF8=1` 兜底
5. **类型标注 vs 赋值** — 冒号管类型、等号管值，不混用

---

## 🆕 新坑登记区

> 每次踩坑后按格式追加到这里，并补进上方对应分类：

```
- [ ] 日期: 错误表现 | 原因 | 正确做法
```
