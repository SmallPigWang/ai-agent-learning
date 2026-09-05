# Day 4 — 2026-08-01（06:00-11:05）

## 今天学了什么

### 消息角色（1.3 补完）
- Messages API 四个角色：`system`(宪法/身份) / `user`(用户话) / `assistant`(AI回填) / `tool`(工具结果)
- system 只出现一次、必须位于第一条；assistant 手动回填实现跨轮记忆
- `validate_roles` 校验模式：安检闸门——逐条件检查，任一不满足 `return False`

### 流式输出（1.4）
- 等快递 vs 边送边收：普通调用等完整回答；流式逐块推送，打字机效果
- SSE 原理：每行 `data: {...JSON...}`，`data: [DONE]` 结束
- 两处 stream：body 里 `"stream": True`（告诉服务器）+ 请求里 `stream=True`（告诉 requests）
- `yield` 生成器：函数产出多个值，产出后暂停继续等——流式的灵魂
- `response.iter_lines()` 逐行读取 SSE 数据块
- `json.loads()` 手动解析：bytes → decode → 砍前缀 → JSON 解析 → 挖 content
- delta vs message：流式取 `delta["content"]`（增量），等快递取 `message["content"]`（完整）
- DeepSeek v4 推理模型的 `reasoning_content` 字段（需兼顾取 content 或 reasoning_content）

### DeepSeek vs Claude JSON 返回结构对比
- 两个模型都返回 OpenAI 兼容格式（共同的骨架）：`id` / `object` / `model` / `choices` / `usage`
- 非流式取 `response.json()["choices"][0]["message"]["content"]`
- 流式取 `data["choices"][0]["delta"]["content"]`（增量）
- **DeepSeek v4**：`message` 里有 `content` + `reasoning_content`（推理过程），需 `delta.get("content") or delta.get("reasoning_content")` 兜底
- **Claude（jiekou 中转）**：只有 `content`，无 `reasoning_content`，无 `logprobs`，结构更简洁
- Token 效率对比：同样 `1+1=?`，DeepSeek 消耗 103 token（含推理），Claude 消耗 26 token
- 关键差异只在字段兼容上（`reasoning_content` 有 vs 无），核心骨架一模一样
- jiekou 中转的价值：Claude 原生 Anthropic 格式完全不同，中转帮你转成 OpenAI 兼容格式

### AI/ML/LLM 概念（1.1）
- AI → ML → DL → LLM → Agent 俄罗斯套娃层级关系
- Token：LLM 最小计数单位，1 token ≈ 1英文词 ≈ 0.6中文字
- 参数（7B/70B）= 模型的"脑容量"，数字越大越强越贵
- 训练（大厂烧钱造模型）vs 推理（你用API答题）
- 幻觉：LLM 会一本正经胡说八道，因为它本质是"预测下一个词"不是查数据库
- API 返回的消息结构有 ~84 token 固定开销，短文本大部分开销在这

### 主流模型全景（1.2）
- 六家对比：Claude（安全/代码）/ GPT（生态/多模态）/ Gemini（搜索整合）/ Llama（开源）/ DeepSeek（性价比/中文）/ Qwen（中文/阿里）
- 选模型口诀：日常 DeepSeek、写代码 Claude、多模态 GPT/Gemini、私有化 Llama/Qwen
- 大陆用户调 Claude API 的困境：Anthropic 不认银联/支付宝
- jiekou.vip 中转方案：国内直连、支付宝充值、$1 起充、base_url=`api.highwayapi.ai`
- OpenRouter / jiekou 等中转平台对比

### Prompt Engineering 入门（1.5 上半场）
- Prompt 是 LLM 的"编程语言"——同一个模型、同一个问题，prompt 写法不同效果天差地别
- **System Prompt 四法则**：
  1. 角色 + 边界：明确"你是谁"和"做什么/不做什么"
  2. 输出格式约束：指定 JSON/CSV/列表等精确格式
  3. 正向指令 > 负向指令：告诉 AI 要什么，不要说不要什么
  4. Few-shot 锚定行为：给 2-3 个例子，AI 自动模仿
- **三种 Prompt 策略**：
  - Zero-shot：不举例直接问，适合简单任务
  - Few-shot：给例子锚定格式和风格
  - CoT（思维链）：加"一步步思考"→ 推理能力飙升
- Few-shot 实现：遍历 examples → 格式化成 `"输入 → 输出"` → `"\n".join()` 拼多行
- **经典坑**：即使提示词要求"只输出 JSON"，AI 仍可能包 ` ```json ` 代码块 → 正则兜底剥壳

### Prompt Engineering 进阶（1.5 下半场 —— 结构化 + 角色扮演）
- **XML 标签**：用 `<system>` `<rules>` `<input>` 精确划分指令区域，AI 遵守率高于裸写
- **深度角色**：system 不只是"你是老师"一句话——要描述性格、教学风格、知识边界、典型反应（4-5 行）
- **水平差异化**：同一 topic 不同 student_level → 讲解方式完全不同（小学生用比喻、程序员用术语）
- f-string 漏 `f` 前缀：普通字符串不替换变量 → AI 收到字面量 `{student_level}`

### Structured Output（1.6）
- Pydantic `BaseModel`：用类定义数据结构，自动校验类型和必填字段
- `Field(description=...)`：给字段加说明文档
- `Recipe(**dict)`：字典解包成 Pydantic 对象，`**` 语法跟 dataclass 一样
- LLM 输出 JSON → `json.loads` → dict → `Recipe(**data)` → 类型安全的 Python 对象
- 这就是 Agent 底座：LLM 输出不再是一坨文本，代码可直接 `.ingredients[0].name` 安全取值
- `import xxx as _xxx`：`_` 前缀约定表示内部别名，避免命名冲突

## 🏁 阶段 1 全部完成

| 模块 | 内容 |
|------|------|
| ✅ 1.1 | AI/ML/LLM 概念扫盲 |
| ✅ 1.2 | 六家模型全景 + jiekou 注册 |
| ✅ 1.3 | 消息四角色 + 首次 API 调用 |
| ✅ 1.4 | 流式输出 SSE |
| ✅ 1.5 | Prompt Engineering 四法则 + 三策略 + XML标签 + 角色扮演 |
| ✅ 1.6 | Structured Output + Pydantic 校验 |

### 环境编码问题彻底解决
- `sys.stdout.reconfigure(encoding='utf-8')` 解决 Windows GBK 终端 emoji 崩溃
- `PYTHONUTF8=1` 环境变量（setx 用户级）一劳永逸根治，所有脚本自动 UTF-8
- WSL2 中 Python 默认已 UTF-8，设了也不影响
- Pylance 类型标注误报：运行时存在但类型定义未声明的方法会标红
- `.vscode/settings.json` 中 `python.analysis.typeCheckingMode: "basic"` 消除噪音告警

## 今天写了什么代码
- message_roles.py — validate_roles（5 闸门校验）+ chat_with_system（system角色+history+多轮对话），7/7 测试通过
- stream_chat.py — stream_chat 流式生成器（yield 逐块产出），4/4 测试通过，36 块分片、66 字完整拼回
- test_jiekou.py — 验证 Claude API 可用性（Key 从 .env 读取），1/1 测试通过
- compare_models.py — call_model 通用客户端 + compare_models 双模型对比 + stream_compare 流式对比，4/4 测试通过
- inspect_json.py — 抓取 DeepSeek / Claude 原始 JSON 返回结构，直观对比差异
- prompt_engineering.py — Zero-shot / Few-shot / CoT 三种策略对比 + JSON 格式控制，4/4 测试通过
- prompt_xml_role.py — XML 标签约束翻译 + 深度角色扮演（水平差异化），4/4 测试通过
- structured_output.py — Pydantic Schema 定义 + LLM 生成结构化菜谱 + 自动校验，4/4 测试通过

## 今天踩了什么坑
- 列表推导变量名不匹配（`msg` vs `m`）：for 循环变量泄漏到循环外，导致 roles 全相同值
- `text[6:]` 砍前缀后没赋值回 text → json.loads 崩
- `text == "DONE"` 少写中括号 → 永远不会触发结束
- DeepSeek base_url 已经是完整路径，call_model 里重复拼 `/chat/completions` → 404
- Claude 流式最后一块 choices 为空列表 → IndexError，需 `data.get("choices", [])` 防护
- 变量名写错：`deepseek_key` 当成回复塞进返回 dict，应该用 `deepseek_reply`
- 模型 ID 格式：`claude-haiku-4-5` 不是 `claude-haiku-4.5`
- AI 回复含 emoji 在 GBK 终端崩溃 → PYTHONUTF8 根治
- deepseek-v4-flash 是推理模型，流式 content 在 `reasoning_content` 字段
- 提示词要求"只输出 JSON"，AI 仍包 ` ```json ` 代码块 → 正则 `re.sub` 剥壳兜底
- f-string 漏写 `f` 前缀 → `{变量}` 不被替换，AI 收到字面量

## 今天的一个收获
- 代码校验 = 安检闸门模式，逐个条件 return False，全过才 True
- 流式输出不是"更快"，而是"不让人等"——用户感知体验的质变
- 类型标注 ≠ 运行时行为，Pylance 标红不一定是代码错了
- API 是通用的：同一个 messages 结构、同一个请求模式，换 URL 就能调不同模型
- `setx PYTHONUTF8 1` 只加一个环境变量，不可能弄坏 conda；VS Code 路径转义问题是 Git Bash 的老毛病

