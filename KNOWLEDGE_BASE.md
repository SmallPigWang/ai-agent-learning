# 📚 知识点总库（KNOWLEDGE_BASE）

> 按模块汇总所有已学知识点，复习时 5 分钟扫一遍。
> 来源：`logs/day-01.md` ~ `day-05.md`；配套踩坑清单见 `PITFALLS.md`。
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

### 2.2 JSON 实战
| 知识点 | 一句话说明 |
|--------|-----------|
| safe_get() | 逐层 isinstance + key in dict 检查，缺层返回 default |
| 安检闸门模式 | 逐条件 return False，全过才 True |
| parse_tool_arguments() | dict 直接用；字符串 try json.loads；失败返回 None |

### 2.3 ReAct 循环
| 知识点 | 一句话说明 |
|--------|-----------|
| ReAct 原理 | Reasoning + Acting 交替：思考→行动→观察→再思考→完成 |
| tool_loop vs ReAct | 固定 1 轮 vs 动态 N 轮（for/while 包住整段） |
| body 重建 | 每轮 messages 变了，body 必须重新构造 |
| 终止条件 | max_iterations 上限 + consecutive_errors ≥ 3 连续错误终止 |
| AgentState | @dataclass 记录 messages/iteration/tool_calls_made/consecutive_errors |
| 路径沙箱 | _safe_path() 限制工具只能访问白名单目录 |

---

## 🔜 待补充模块
- 2.3 记忆系统（滑动窗口 / 摘要压缩 / 向量存储）
- 2.4 任务规划（Plan-and-Execute）
- 2.5 Reflection（生成→自评→改进）
- 2.6 安全护栏
- 阶段 3：RAG 全流程
- 阶段 4：框架（SDK / LangGraph / MCP / 多 Agent）
- 阶段 5：工程化（评估 / 可观测 / CI/CD / 部署）
