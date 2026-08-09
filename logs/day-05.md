# Day 5 — 2026-08-09（Tool Calling 深入 + JSON 实战）

## 今天学了什么

### Tool Calling 核心循环（2.1）
- **工具本质**：工具 = Python 函数 + JSON Schema（给 LLM 看的说明书）
- **执行流程**：`tool_use → execute → tool_result`——LLM 决定调工具 → 你执行 → 结果回填 messages → LLM 基于结果回答
- **核心循环**：
  1. 构造 messages + body（带 `"tools"` 参数）
  2. 第一次 API 调用 → LLM 回复含 `tool_calls`
  3. 判断 `"tool_calls" in msg`：有→执行工具，无→直接返回纯文本
  4. 回填两条消息：assistant（含 tool_calls）+ tool（含执行结果 + tool_call_id）
  5. 第二次 API 调用（不带 tools）→ LLM 翻译成自然语言回答
- **并行工具调用**：`tool_calls[0]` → `for tc in tool_calls` 循环处理 N 个工具
- **消息顺序**：user → assistant(tool_calls) → tool(result1) → tool(result2) → assistant(final)
  - assistant 消息必须在 tool 结果**之前**

### JSON 深度实战
- **safe_get()**：`for key in keys` + `isinstance(data, dict)` + `key in data` 逐层安全取值
  - 关键：非 dict 就 `return default`，key 不在也 `return default`
- **validate_tool_schema()**：安检闸门模式逐层检查 `type→function→name/parameters→properties`
- **build_messages()**：封装 `[{"role": "system", ...}, {"role": "user", ...}]`
- **parse_tool_arguments()**：`isinstance(dict)`→直接返回, `if not`→None, `try json.loads`→解析, `except`→None

### 踩坑记录
- f-string 内 `{'c': 42}` 格式冲突：Python 把 `: 42}` 当 format specifier → 先存变量再放 f-string
- Pylance 类型缩窄：`fn.get("parameters")` 调两次 Pylance 不跟踪 → 调一次存变量 `para`
- `isinstance` 检查后 Pylance 仍报警告：同一变量 Pylance 能跟踪，但两次独立函数调用不行
- 消息回填顺序错误：assistant 放在 tool 结果后面 → API 报 `KeyError: 'choices'`，必须 `assistant → tool → tool`
- `return False` 缺错误消息 → Pylance 报返回值类型不匹配（函数签名 `-> tuple`）

## 今天写了什么代码
- `tool_calling.py` — tool_loop 单工具调用循环（calculator + get_current_time），7/7 测试通过
- `json_deep_dive.py` — safe_get / validate_tool_schema / build_messages / parse_tool_arguments，15/15 测试通过
- `parallel_tools.py` — parallel_tool_loop 并行工具调用（+ get_weather 第 3 个工具），4/4 测试通过

### Agent 循环手写 + 文件助手（2.2）
- **ReAct 原理**：Reasoning + Acting 交替——思考→行动→观察→再思考→...→完成
- **tool_loop vs ReAct**：tool_loop 固定 1 轮工具调用 → ReAct 动态 N 轮，`for _ in range(max)` 包住整段
- **关键改造**：API 调用放进循环 + body 每次重建（messages 变了）+ if 分支 continue 不 return
- **AgentState 状态追踪**：用 `@dataclass` 记录 messages/iteration/tool_calls_made/consecutive_errors
- **连续错误终止**：`try/except` 执行工具 → 成功重置计数，失败+1 → ≥3 次终止
- **文件 Agent**：read_file / write_file / list_files 三个工具 + `_safe_path()` 路径沙箱
- **多步链式任务**：测试6 Agent 自主完成"列目录→读文件→转大写→写文件" 3步操作
- `react_loop.py` — ReAct 多轮循环（天气→条件计算），4/4 测试通过
- `file_agent.py` — 智能文件助手（读/写/列目录 + AgentState），6/6 测试通过

## 今天的一个收获
- **Agent 心脏 = tool_loop**：感知（发 API）→ 决策（LLM 选工具）→ 执行（你跑函数）→ 反馈（回填结果）→ 回答（二次调用）。你就是 LLM 和真实世界的中间人——LLM 负责"想"，你负责"做"。
- JSON 是 Agent 开发的"通用语"——API 请求体、工具 Schema、LLM 响应、消息结构全是 JSON，必须形成肌肉记忆。
- DeepSeek 模型 `deepseek-chat`（实际跑的是 v4-flash），tools 参数是 `"tools"` 不是 `"functions"`。

## 自我评分 (1-5)
- 理解程度: 5
- 完成度: 5
- 投入度: 5
