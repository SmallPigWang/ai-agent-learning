# 📚 知识点总库（KNOWLEDGE_BASE）

> 按模块汇总所有已学知识点，复习时 5 分钟扫一遍。
> 来源：`logs/day-01.md` ~ `day-06.md`；配套踩坑清单见 `PITFALLS.md`。
> 更新规则：每完成一个新模块，在此追加一节。

---

## 0. Python 基础

### 0.1 语法与数据结构
| 知识点 | 一句话说明 |
|--------|-----------|
| 变量与数据类型 | int/float/str/bool，类型由值决定 |
| 条件判断 | if/elif/else 分支，elif 可多个 |
| 循环 | while（条件循环）/ for（遍历循环）+ break/continue |
| 四种数据结构 | list（有序可变）/ tuple（有序不可变）/ dict（键值对）/ set（去重） |
| 内置函数 | sum/max/min/len/round/float 等 |
| 字符串操作 | split() 切分、strip() 去空格、f-string 格式化 |
| 卫语句 | 空值/非法输入提前 return，减少嵌套 |
| 异常处理 | try/except + 具体异常类型（ValueError/FileNotFoundError） |

### 0.2 文件读写
| 知识点 | 一句话说明 |
|--------|-----------|
| with open() | 自动管理资源，不用手动 close |
| 读取模式 | read() 全读 / readlines() 按行列表 / 逐行 for 遍历 |
| CSV 解析套路 | 读行 → strip → split → 类型转换 → 收集 |
| 跳过表头 | `lines[1:]` 切片 |
| 脏数据跳过 | try/except 包裹类型转换，失败 continue |

### 0.3 面向对象
| 知识点 | 一句话说明 |
|--------|-----------|
| class + __init__ | 类定义与构造方法，self 指实例本身 |
| 实例属性 vs 方法 | 属性不加括号，方法要加括号调用 |
| __repr__ | 魔法方法，控制 print(obj) 的输出 |
| 布尔状态管理 | 用 available 等布尔属性控制状态（借/还） |
| 继承 | `class A(B):`，子类复用父类接口 |
| super().__init__() | 调父类构造，不传 self |
| 方法覆盖 | 子类重写父类方法，各自实现 |
| isinstance() | 验证继承关系 |
| @dataclass | 自动生成 __init__/__repr__/__eq__，省 80% 样板代码 |
| field(default_factory=list) | 可变默认值的正确写法 |
| Optional[str] | 字段可为 str 或 None（= str \| None） |
| Literal[1,2,3] | 限制取值只能是字面量集合 |
| 类型注解 vs 赋值 | `变量: 类型 = 值`，冒号管类型、等号管值 |

### 0.4 Git 与工具
| 知识点 | 一句话说明 |
|--------|-----------|
| Git 三区模型 | 工作区(add)→暂存区(commit)→本地仓库(push)→远程 |
| .gitignore | 排除缓存/虚拟环境/IDE 配置 |
| conda + pip | 环境管理；pip 用清华镜像加速 |
| PYTHONUTF8=1 | 环境变量根治 Windows GBK 终端编码问题 |

---

## 1. LLM 基础

### 1.1 概念
| 知识点 | 一句话说明 |
|--------|-----------|
| AI→ML→DL→LLM→Agent | 俄罗斯套娃层级关系 |
| Token | LLM 最小计数单位，1 token ≈ 1 英文词 ≈ 0.6 中文字 |
| 参数（7B/70B） | 模型"脑容量"，越大越强越贵 |
| 训练 vs 推理 | 训练=大厂烧钱造模型；推理=你用 API 答题 |
| 幻觉 | LLM 本质是"预测下一个词"，不是查数据库 |
| 上下文窗口 | 一次能处理的 token 上限 |

### 1.2 模型全景
| 知识点 | 一句话说明 |
|--------|-----------|
| 六家对比 | Claude（安全/代码）/ GPT（生态/多模态）/ Gemini（搜索）/ Llama（开源）/ DeepSeek（性价比/中文）/ Qwen（中文） |
| 选模型口诀 | 日常 DeepSeek、写代码 Claude、多模态 GPT/Gemini、私有化 Llama/Qwen |
| 中转平台 | 大陆调 Claude 的替代方案（jiekou.vip 等，OpenAI 兼容格式） |

### 1.3 API 调用
| 知识点 | 一句话说明 |
|--------|-----------|
| HTTP 基础 | GET/POST/Header/Body/JSON |
| API Key 安全 | 放 .env，用 python-dotenv 加载，绝不写进代码 |
| Messages 结构 | 统一 messages 数组，换 base_url 即可换模型 |
| 四角色 | system（宪法，第一条）/ user（用户话）/ assistant（AI 回填）/ tool（工具结果） |
| 参数 | max_tokens、temperature |
| 返回结构 | `response.json()["choices"][0]["message"]["content"]` |
| usage | 看 token 消耗（~84 token 固定开销） |
| 跨轮记忆 | LLM 无状态，把整个 history 塞回 messages = 记忆 |

### 1.4 流式输出
| 知识点 | 一句话说明 |
|--------|-----------|
| SSE 协议 | 每行 `data: {JSON}`，`data: [DONE]` 结束 |
| 两处 stream | body `"stream": True` + 请求 `stream=True` |
| yield 生成器 | 产出后暂停，流式的灵魂 |
| iter_lines() | 逐行读取 SSE 数据块 |
| delta vs message | 流式取 delta（增量），非流式取 message（完整） |
| reasoning_content | DeepSeek 推理模型的思考字段，需兜底取值 |

### 1.5 Prompt Engineering
| 知识点 | 一句话说明 |
|--------|-----------|
| System Prompt 四法则 | 角色+边界 / 输出格式约束 / 正向指令>负向 / Few-shot 锚定 |
| Zero-shot | 不举例直接问 |
| Few-shot | 给 2-3 个例子，AI 自动模仿 |
| CoT | 加"一步步思考"→ 推理能力飙升 |
| XML 标签 | `<system>` `<rules>` `<input>` 划分指令区域，遵守率更高 |
| 深度角色 | 描述性格+风格+知识边界+典型反应（4-5 行） |
| 水平差异化 | 同一 topic 不同 student_level 用不同讲解方式 |
| JSON 剥壳 | AI 包 ```json 代码块时用正则 re.sub 兜底 |

### 1.6 结构化输出
| 知识点 | 一句话说明 |
|--------|-----------|
| Pydantic BaseModel | 类定义数据结构，自动校验类型和必填 |
| Field(description=) | 字段说明文档 |
| `Recipe(**dict)` | 字典解包成 Pydantic 对象（Agent 底座：代码可安全消费 LLM 输出） |

---

## 2. Agent 核心

### 2.1 Tool Calling
| 知识点 | 一句话说明 |
|--------|-----------|
| 工具的本质 | 普通 Python 函数 + JSON Schema（给 LLM 的说明书） |
| 执行流程 | tool_use → execute → tool_result |
| 核心循环 | 构造 tools → 调用 → 判断 tool_calls → 执行 → 回填 → 二次调用回答 |
| 消息顺序 | user → assistant(tool_calls) → tool 结果们 → assistant(final)，assistant 必须在 tool 之前 |
| tool_call_id | 回填 tool 消息时必须带上，一一对应 |
| 并行调用 | `for tc in tool_calls` 逐个执行+回填多条 tool 消息 |
| Schema 设计 | type→function→name/parameters/properties 层级 |
| safe_get() | 逐层 isinstance + key in dict 检查，缺层返回 default |
| 安检闸门模式 | 逐条件 return False，全过才 True |
| parse_tool_arguments() | dict 直接用；字符串 try json.loads；失败返回 None |

### 2.2 Agent 循环手写（ReAct）
| 知识点 | 一句话说明 |
|--------|-----------|
| ReAct 原理 | Reasoning + Acting 交替：思考→行动→观察→再思考→完成 |
| tool_loop vs ReAct | 固定 1 轮 vs 动态 N 轮（for/while 包住整段） |
| body 重建 | 每轮 messages 变了，body 必须重新构造 |
| 终止条件 | max_iterations 上限 + consecutive_errors ≥ 3 连续错误终止 |
| AgentState | @dataclass 记录 messages/iteration/tool_calls_made/consecutive_errors |
| 路径沙箱 | _safe_path() 限制工具只能访问白名单目录 |

### 2.3 记忆系统
| 知识点 | 一句话说明 |
|--------|-----------|
| 滑动窗口 | 只保留 system + 最近 N 轮，旧消息丢弃，省空间 |
| system 常驻豁免 | system 是“宪法”，永远保留且在最前 |
| 轮（turn） | 1 轮 = 1 user + 1 assistant，裁剪按“轮”不按“条” |
| 摘要压缩 | 旧消息压成一段摘要，保留要点，不直接丢光 |
| 摘要合并进 system | 把摘要拼进 system 内容，让 LLM 每轮都能看到旧要点 |
| 混合策略 | 旧对话用摘要，新对话用窗口，兼顾省空间和记忆 |
| token 粗估 | role + content 字符数相加，粗略判断离上下文上限多远 |
| 三种记忆分工 | 短期=对话内 messages；长期=跨对话落盘档案；工作=AgentState 任务状态 |
| 对比实验设计 | 控制变量（同数据同窗口）+ 固定指标（token 占用/信息保留率）+ 基线对照 |
| 埋事实测记忆 | 数据里预埋"关键事实"，裁剪后数还剩几条 → 记忆力变成 0~1 数字 |
| 回调函数注入 | summarize 等作为参数传入，测试传离线 fake、生产传 LLM，接口不变 |
| 长期记忆闭环 | 抽取 → 入档 → 落盘 → 新对话读盘 → 注入 system |
| 抽取 | 人话（非结构化）→ 表格（结构化），长期记忆的第一环 |
| 规则抽取 vs LLM 抽取 | 写死的 if 免费/死板；LLM 什么话都懂但花钱联网，接口相同时可互换 |
| system 注入点 | 记忆拼进 system（常驻第一条），比拼 user 消息更稳 |
| json 落盘 | dict ↔ 文件往返：dump/load 吃文件，dumps/loads 吃字符串（d 写 l 读，带 s 换字符串） |
| ensure_ascii=False + indent=2 | json 中文原样落盘 + 缩进可读 |
| 容错兜底 | FileNotFoundError / JSONDecodeError 都返回空档案，坏一块不崩全部 |
| 不可变更新 | dict(old) 复印后改复印件，原件留快照、无副作用 |
| 表驱动 | (前缀, 键名) 规则卡 + 循环，加规则只加数据不改逻辑 |
| startswith() | 前缀判断，替代手数长度的切片比较（新规范点名） |
| assert 断言收窄 | assert x is not None 让类型检查器确认"此处不为 None"，修 Pylance 报错 |
| 过严断言 | 测试只验证意图（startswith+in），不耦合与目标无关的格式细节（如全半角标点） |
| 浅拷贝陷阱 | dict(vault) 只复印外层，内层档案仍是原件——两层结构要两层都复印 |
| {**d, k: v} 合并 | 字典解包合并：老库倒进新库+替换一个键，一行完成外层复印 |
| dict 保持插入顺序 | Python 3.7+ 字典键按插入顺序存放，next(iter(d)) = 最旧的键 |
| FIFO 淘汰 | 容量满时踢掉最先进入的条目（LRU 缓存的雏形），覆盖不算新条目 |
| del 语句 | del d[key] 删除字典的键，d[k]=v 的反面 |
| 卫语句双条件 | user not in vault or key not in vault[user]——两种"不用干活"提前返回 |

### 2.4 任务规划与分解
| 知识点 | 一句话说明 |
|--------|-----------|
| Plan-and-Execute 模式 | 先生成完整计划再逐步执行，vs ReAct 走一步看一步（边炒菜边想 vs 先看菜谱） |
| 计划即数据 | plan 是 list[dict]，可校验、可打印、可给人过目 |
| 静态清单循环 vs 动态决定 | P&E 循环一个静态列表，ReAct 每轮问 LLM——前者省调用、可审计 |
| 工具注册表分发 | {"动作名": 函数}，按 action 查表调用，加工具只加表项 |
| *args 调用侧解包 | fn(*[2,3]) = fn(2,3)；safe_get 的 *keys 是签名侧收拢，一体两面 |
| 优雅降级 | 未知操作返回错误字符串不崩溃，引擎继续跑 |
| 校验器参数放宽 | 安检员天生要接"可能不合法"的输入，签名用 list 而非 list[dict] |
| 动态重规划 | 受阻→重算【剩余】路线→继续，已完成的结果不回滚（导航改道不回出发点） |
| 重规划预算 max_replans | 防庸医 replanner 无限变道烧钱，max_iterations 的直系亲戚 |
| 错误即数据 | 优雅降级的产出（未知操作字符串）= 上游系统的触发信号 |
| while+手动索引 | 循环对象要中途整体替换时，for 锁死迭代对象，while 才能边跑边换 |
| import 自己的模块 | 同目录 from plan_and_execute import ...，DRY 复用零件 |
| 失败痕迹保留 | results 记录每次失败——审计时能看到在哪改的道 |
| planner vs replanner | 出发前盲规划(只知任务) vs 受阻时知情改道(知任务+进度+故障)，只管剩余 |
| 共享黑板 state | 步骤间数据流走闭包 dict，不走返回值（框架 checkpoint 思想） |
| zip 拉链配对 | zip(a,b) 按位置咬合成对，配权重/配对计算一步到位 |
| CWD vs 脚本目录 | 相对路径跟着"从哪运行"走；Path(__file__).parent 锚定"文件在哪" |
| Workflow vs Agent | 流程固定（下一步听代码）vs 动态流程（下一步听 LLM）——run_plan vs react_loop |
| gate 闸门思想 | 步骤之间加检查点：validate_plan 拦进门计划、is_failed 拦半路结果，脏数据不流向下一步 |
| 何时该用 Agent | 任务步骤无法预知、需现场决策才上 Agent；宁简勿繁，从最简单方案开始 |
| 依赖感知执行（拓扑排序朴素版） | 每步声明 needs，循环挑"依赖全就位"的步骤执行，清单顺序≠执行顺序 |
| 死锁检测 | 还有剩余但挑不出任何就绪步骤 = 依赖成环，报告终止而非挂死 |
| done 用 set | 已完成 id 集合用 set——`n in done` 是 O(1) 查询，list 是 O(n) |
| sorted(key=lambda) | 排 dict 列表给一把"尺子"：key=lambda s: s["id"] 量哪个字段 |
| all() / any() | 全都成立吗 / 有一个成立吗——all 管闸门全过才放行，any 管警报有一个就响 |

### 2.5 Reflection 反思机制
| 知识点 | 一句话说明 |
|--------|-----------|
| 反思循环 | 生成→自评→改进：ReAct 对外行动，反思对内检讨自己上一稿 |
| 批评家=规则代码 | 硬约束检查用代码不用 LLM——免费、确定、可测试（离线可验的逻辑不花钱） |
| 反思便签=工作记忆 | 问题清单翻译成便签喂回下一轮生成器，note 跨轮传递 |
| 问题收敛曲线 | problems_history 里问题数递减（如 [2,1,0]）——反思有效的数字证据 |
| critic 返回问题清单 | 比 bool 信息量大：清单直接变成下一轮的改进指令（错误即数据第三次登场） |
| 预算即圈数 | for range(max_rounds)：每圈必然消耗预算，放学铃必须存在 |
| 语言强化学习 | 不改权重改文字记忆——不做脑手术，改贴便利贴（Reflexion） |
| Actor/Evaluator/Self-reflection | = generator/check_slogan/build_reflection，我写过 Reflexion 迷你版 |
| episodic memory | 反思跨试次（任务）存活；note 只在单任务内——长期记忆+反思便签的合体 |
| 反思按需付费 | 第 1 轮=裸奔，一稿过零成本，烂稿才补轮——怕翻倍不敢开是错觉 |

### 7.1 论文阅读（元能力）
| 知识点 | 一句话说明 |
|--------|-----------|
| 三遍寻宝法 | 侦察(摘要/图表/结论5分钟)→挖宝(Intro末段+方法+Figure1)→按需拆解(复现时才精读) |
| Figure 1 定律 | Agent 论文 90% 精华在架构图——先看懂图再看字 |
| 代码锚定法 | 把论文组件翻译成自己写过的函数，概念立刻落地 |
| 费曼检验 | 写不出 3 行总结=没读懂，回去重读 Figure 1 |

| episodic memory 实现 | 长期记忆(落盘教训库)×反思(便签)的组合——lesson 跨任务传递 |
| 读旧+append+写回 | 追加式落盘三步：复用 load 读旧库，别只写新条目（会覆盖历史） |
| 容错返回同形状 | 异常路径返回值类型必须与正常路径一致（[] 而非 False，否则下游 .append 爆炸） |
| 剧本放闭包外 | 脚本化 fake 的剧本必须定义在函数体外——体内=每次调用重发剧本永远第一稿 |

### 2.6 安全与护栏
| 知识点 | 一句话说明 |
|--------|-----------|
| 威胁矩阵 | 5 大攻击面: 注入/越权工具/数据泄露/输出投毒/供应链——对应防御: 过滤/分级/校验/校验/沙箱 |
| Prompt 注入 | 指令藏在数据里（留言板/网页/文件）——LLM 眼里数据和指令都是文字，天生分不清 |
| 大小写归一化 | 文本检测先 text.lower()——否则 DISREGARD 大写攻击直接穿防 |
| 表驱动特征检测 | 危险短语进 PATTERNS 表 + 循环，加特征零改逻辑 |
| 过滤 vs 拦截 | sanitize 消毒放行（柔和）vs guard 命中即拒（强硬）——纵深防御两层都上 |
| 规则模拟 LLM | 用 if 模拟"被劫持的 LLM"——离线靶场不花 API 钱 |
| 遍历字符串陷阱 | for x in "字符串" 拆成逐字符——遍历名单要遍历【列表】 |
| 绿黄红权限分级 | 按副作用: 无副作用(绿自动放行)/可逆(黄需确认)/不可逆(红人工通道) |
| 默认拒绝 Default Deny | 未登记=红——dict.get(k, 'red') 一行落地，宁可误拒不可误放 |
| 审计记裁决不记申报 | 日志记闸门的 allowed，不是申请人的 auto_confirm——被拒的试图才是警报 |
| 闸门与执行分离 | authorize 只决策，run_tool 先闸后执行——安检员不搬货 |
| 输出校验(出口安检) | Agent 产物流进下游前的最后一道闸：SQL只读/单语句/无破坏词 |
| 检查优先级=契约 | 多规则同时踩线先报哪个由契约(测试)定——多语句是注入最本质签名优先报 |
| resolve后再验身 | 永不信字面路径: ../先展开再 is_relative_to 比对，伪装即失效 |
| 纵深防御代码形状 | 两道闸串联(各自独立可测)，authorize→run_tool 同构第三台 |
| OWASP LLM Top 10 | 业界十大病清单——注入/输出处理/过度代理/供应链我防过，泄露/DoS/数据投毒是新面孔 |
| 5攻5防口诀 | 进口过滤、手分级、出口校验、范围圈死、来源审查 |
| LLM输出=概率猜测 | 不是可信结果——过度依赖(LLM09)的病根，进出口设闸的总依据 |
| 文字版ReAct协议 | ACTION/OBSERVATION/ANSWER 文本协议——不依赖API原生tool_calls，与手写react_loop同构 |
| 脚本自举模式 | sys.path.insert挂载.tools/——仓库自带依赖，裸python3直跑，/tmp蒸发免疫 |
| Agent可靠性来源 | 不是模型聪明，是每个进出口设闸+引擎逼它先查资料再开口 |

## 📖 Day 8 高频变量词表（教练命名 → 中文语义）

| 名字 | 语义 | 登场文件 |
|------|------|---------|
| `planner` | 计划师：出发前盲规划，只知任务 | plan_and_execute |
| `replanner` | 重规划师：受阻时知情改道（知任务+进度+故障） | replan_loop |
| `plan` / `step` | 计划=数据（list[dict]）；step=其中一步 | 2.4 全家 |
| `order` | 执行顺序（重排的证据） | dep_executor |
| `done` | 已完成 id 集合（set，O(1) 查询） | dep_executor |
| `ready` | 就绪步骤（依赖全就位且未跑） | dep_executor |
| `is_failed` | 故障信号（降级消息当触发器） | replan_loop |
| `note` | 反思便签（喂给下一轮生成器） | reflection_loop |
| `problems` | 问题清单（批评家输出，空=合格） | 2.5 全家 |
| `prefix` | 便签前缀段（"过往教训: "固定开头） | episodic_reflection |
| `lesson` | 教训（跨任务存进情景记忆的那句话） | episodic_reflection |
| `attempts` | 每一稿的记录 | reflection_loop |
| `problems_history` | 每轮问题清单的历史 | reflection_loop |
| `rounds` | 用了几轮（成本代理） | 2.5 全家 |
| `factory` | 造机器的厂（调用产全新生成器） | cost_benefit |
| `generator` | 发电机（产出候选的那位） | 2.5 全家 |
| `critic` | 批评家（硬规则挑毛病） | reflection_loop |
| `board_text` | 留言板文本（间接注入的藏身处） | prompt_injection_lab |
| `INJECTION_PATTERNS` | 注入特征表（表驱动检测） | prompt_injection_lab |
| `sanitize` | 消毒员（替换危险词后放行） | prompt_injection_lab |
| `RISK_TABLE` | 工具风险等级表 | tool_permissions |
| `AUDIT_LOG` | 审计日志（记试图，含被拒） | tool_permissions |
| `allowed` | 闸门的裁决：准不准 | tool_permissions |
| `auto_confirm` | 申请人的申报：我确认了（≠裁决） | tool_permissions |
| `level` | 风险等级（green/yellow/red） | tool_permissions |
| 成本效益决策 | 约束可编程(critic免费)+失败代价高→开反思；约束主观+任务一次性→别开 |
| calls 成本代理 | 生成器调用次数≈LLM token 钱；裸奔恒 1，反思=rounds |
| 对照组实验(方法论复用) | 和 2.3 记忆对比同款：基线+实验组+同一剧本，结论三态：白设/赚了/纯亏 |
| 工厂模式 | factory() 每次产全新生成器——两组各用各的，剧本不串 |
| 厂子vs机器 | factory 调用→得发电机；generator 调用→得标语；传机器不传产物 |

---

## 🔜 待补充模块
- 2.4 任务规划（Plan-and-Execute）
- 2.5 Reflection（生成→自评→改进）
- 2.6 安全护栏
- 阶段 3：RAG 全流程
- 阶段 4：框架（SDK / LangGraph / MCP / 多 Agent）
- 阶段 5：工程化（评估 / 可观测 / CI/CD / 部署）


### 3.1 RAG 原理与最简实现
| 知识点 | 一句话说明 |
|--------|-----------|
| RAG=开卷考试 | 不靠背(模型权重)靠翻书(检索)——治知识冻结/私有盲区/幻觉三病 |
| 存入/查询两流程 | 存入:切块→embed→库；查询:embed→相似度→TopK→拼prompt |
| 语义vs子串检索 | 向量认"意思近"(共享bigram→同格亮灯)，子串要求整串连续相同 |
| bigram哈希embedding | 相邻字对哈希计数向量——免费确定的离线替身，生产换真API(回调第4次) |
| 哈希三性格 | 确定性(同入同出)/均匀(散开)/会撞车(碰撞可容忍) |
| ord/chr | 字→Unicode座位号 / 反向；哈希公式的原料 |
| ×31多项式哈希 | 乘法保序防交换撞车(流式≠式流)，31是祖传素数 |
| cosine余弦相似度 | 点积÷双模=夹角；只认方向不认长度，1.0最像0.0无关 |
| dim=256经验值 | 维度太低→生日悖论撞车→假共享盖过真共享→排名翻转 |
| Top-K检索 | 记分板(分数,块)降序取前k，剥分数只交原文 |
| 天然chunks | KNOWLEDGE_BASE表格行/logs段落/PITFALLS坑行——仓库自带切块 |
| 参数vs非参数记忆 | 知识进权重(凝固/难溯源) vs 进外部语料库(可更新/有出处)——RAG创世动机 |
| 刀距vs刀长 | step管range刀序(下一刀起点)，size管切片刀长(这一刀多长)——混用=零重叠铺砖 |
| 拼回原文铁律 | "".join(chunks)==text——切块一个字不能丢，丢字=丢证据 |
| 三策略实验结论 | 行切top1=纯知识块(省token/准/可引用)；硬切和窗口混装多主题 |
| 元数据溯源 | 块带户口{source}——答案能答"这话哪来的"，无户口=传闻 |
| 分块决策树 | 有天然结构→按行切(实验证明最纯)；连续长文→窗口+重叠；定长硬切几乎不用 |
| Recursive分块 | 刀法优先级队列：段落→句子→词逐级降级，守块大小且沿语义边界 |
| 框架vs手写 | LangChain价值=工程封装(默认值/边界调好)；手写过=祛魅，知其非魔法 |
| hit rate评估 | 命中数÷总题数——RAG的单元测试；测试集要含同义陷阱题才拉开差距 |
| 懒加载单例 | 贵资源(模型)全局空位装一次复用；函数内赋值全局必须global声明 |
| 分布式语义假设 | 词义在上下文分布不在字面——宕机vs死机零共享字但bge给0.54 |
| bge-small-zh-v1.5 | 本地免费512维中文embedding，SentenceTransformer加载 |
| 回调即检测器 | 写死hash_embed在单一选手下隐身，第二选手上场立即现形——对照实验的隐藏价值 |
| zip静默截断 | zip按短序列截断不报错——维度错配产出合法垃圾分数，比崩溃更险 |
| 向量库三件套 | 向量存储+相似度索引(HNSW/ANN)+元数据过滤——替代查询时O(N)暴力扫 |
| 选型口诀 | 学Chroma/产Qdrant/海量Milvus/懒人Pinecone；Chroma=嵌入式落盘文件夹 |
| add三件套 | documents原文+embeddings向量+ids编号——入库时算向量，查询只算问题 |
| query套娃 | res["documents"][0]两层壳——外dict内list(支持批量查询) |
| hnsw:space=cosine | 建collection时指定度量与手写版对齐，否则默认L2排名可能漂移 |
| 编目一次forever查 | 向量库本质:预计算+索引，重复embed全部块是手写版的原罪 |
| PersistentClient vs HttpClient | 嵌入式落盘文件库 vs 连服务端——SQLite vs MySQL |
| add vs upsert | 撞id报错 vs 有则更新无则插入(幂等正解)；全删重建是块多时的下策 |
| where元数据过滤 | 相似度搜索+结构筛选=混合检索雏形——tag_source户口的兑现 |
| query vs get | 按相似度搜(给向量) vs 按条件取(给id/where) |
| bge官方查询前缀 | 检索查询带'为这个句子生成表示以用于检索相关文章：'，文档不带——出厂设置 |
| 静态None守卫 | 类型说可能None就要兜底: or [[]] + if m is not None——满足Pylance+防御未来 |
| 661块真实语料 | KNOWLEDGE_BASE+PITFALLS+logs 按行收割(滤标题/分隔线)——仓库自带RAG语料 |
| 终极对决 | 子串武器对同义整句扑空；语义武器bge一击命中(注入靶场行)——RAG价值实证 |
| Retriever+Generator | 论文两件套：DPR找资料+BART生成；我的retrieve+build_prompt同构 |
| embedding=文本→向量 | 让"意思近"变"夹角小"可计算；hash只是替身手法，向量才是产物 |