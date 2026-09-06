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
| 38 | 窗口保留条数不对 | 切片边界算错（用 keep_count 而不是 len-rest） | 用 `len(rest)-keep_count` 作为切点 |
| 42 | `int(msg["role"])` ValueError | int() 是类型转换，不是数长度 | 求字符数用 `len()` |
| 43 | `vault.items(user)` TypeError | items() 不带参数；按键取值+默认值是另一个方法 | `vault.get(user, {})` |
| 44 | `del profile[user]` KeyError | 删错层：vault 的键是用户名，profile 的键是偏好名 | 动手前先想清楚自己在哪一层 |
| 45 | 窗口保留了最旧消息、保留率 1.0 | 切片方向反：正索引从头丢（#38 方向版） | 窗口永远负索引从尾数 `rest[-N:]` |

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
| 39 | `merged + recent_messages[1:]` 报错 | dict 不能直接和 list 相加 | 用 `[merged] + recent_messages[1:]` 包成列表再拼接 |
| 40 | 摘要为空时返回 None | 测试期望空字符串 | 无旧消息时返回 `""` |
| 41 | 新建 system 消息 role 写成 recent | 把列表变量当角色名 | 固定写 `"system"` |
| 46 | mypy: Need type annotation for "x" | 空容器类型推断不出 | 空容器必须注解 `x: dict = {}` |

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
| 47 | `；` SyntaxError: invalid character | 中文分号混进 except 行尾 | 代码标点全英文半角；写代码切英文输入法（#8 家族） |

## 6. 工具与 Git

| # | 错误表现 | 原因 | 正确做法 |
|---|---------|------|---------|
| 34 | Pylance 自动补全不弹窗 | editor.quickSuggestions 被关 | 检查 VS Code 设置 |
| 35 | conda 环境混乱 | 原始源和清华镜像混装 | 只用一个源 |
| 36 | git push 慢/超时 | 国内连 GitHub 网络问题 | 正常现象，小项目可接受；必要时走代理 |
| 37 | 第一次 push 卡住 | 需要浏览器授权 | 按提示完成 OAuth 授权 |
| 48 | 外部脚本改的文件被编辑器覆盖（×3） | VS Code 缓冲区不知道磁盘已变 | 外部修改后先 Revert File 再动手 |
| 49 | 报告文件落在仓库根而不是脚本目录 | 相对路径跟着 CWD（从哪运行）走，不跟文件位置走 | `Path(__file__).parent / path` 锚定脚本目录 |
| 50 | `id in list[dict]` 永远 False 不报错 | 类型不匹配的 in 静默失效（int 查 dict 列表） | in 之前核对两边类型一致；查 id 集合用 set |
| 51 | 脚本化 fake 永远返回第一稿 | 剧本列表定义在函数体内，每次调用重置 | 剧本放函数体外（闭包），或用工厂每次产新机器 |
| 52 | 落盘 FileNotFoundError | open 忘写 "w" 模式，默认只读 | 写文件三件套：open(path, "w", encoding="utf-8") |
| 53 | detect 对干净输入也返回 True | for x in lowered 遍历字符串=逐字符，首字符必在自身 | 遍历名单要遍历【列表】(PATTERNS) |
| 54 | TypeError: slice indices | .find() 当 .replace() 用，find 返回下标 | 换内容用 replace(旧,新)；找位置才是 find |
| 55 | 复制旧引擎进新函数全盘报错 | 没改签名/键名/文案（replanner 根本不在参数里） | 复制模板后逐项核对：参数/返回键/文案契约 |
| 56 | 审计记错、guard 交给消毒员 | 语义相近名串门：申报(auto_confirm)≠裁决(allowed) | 用词表锚定角色语义，写前默念名字含义 |

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

- [x] 2026-08-16: 窗口保留条数不对 | 切片边界算错 | 用 `len(rest)-keep_count`
- [x] 2026-08-16: `merged + list` 报错 | dict 不能直接和 list 相加 | 用 `[merged] + list`
- [x] 2026-08-16: 摘要为空返回 None | 测试期望空字符串 | 返回 `""`
- [x] 2026-08-16: role 写成 recent | 把列表当角色名 | 固定写 `"system"`
- [ ] 2026-08-30: 测试对全角，/半角,逗号精确比对导致 FAIL | 过严断言——耦合了与学习目标无关的格式细节 | 断言验证"意图"（startswith + in），不逐字符比对；确需精确格式时从 expected 复制粘贴字符
- [x] 2026-08-30: int() 当 len() 用（ValueError 'user'） | 转换器当尺子用 | 字符数用 len → #42
- [x] 2026-08-30: vault.items(user) TypeError | items 不带参数 | get(user, {}) → #43
- [x] 2026-08-30: del profile[user] KeyError | 删错层 | del profile[key]，先想清楚在哪层 → #44
- [x] 2026-08-30: rest[6:] 保留最旧、保留率 1.0 | 切片方向反 | 窗口负索引从尾数 → #45
- [x] 2026-08-30: mypy Need type annotation ×2 | 空容器没注解 | x: dict = {} → #46
- [x] 2026-08-30: 全角分号 SyntaxError | 中文输入法标点混入代码 | 标点全英文半角 → #47
- [x] 2026-08-30: 编辑器覆盖外部修改 ×3 | VS Code 缓冲区未感知磁盘变化 | 先 Revert File → #48
| 57 | dim=64 检索排名翻转（查流式命中记忆块） | bigram 挤 64 格生日悖论撞车，假共享 0.44 > 真共享 0.43 | 维度加宽到 256+；或换真 embedding |
| 58 | 换bge后检索全错(bge 0/5) | retrieve里查询向量写死hash_embed，与回调块向量维度错配，zip静默截断 | 查询和块都走同一个embed回调；回调注入天然防写死 |
