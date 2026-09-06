# 🎓 AI Agent 学习进度追踪看板

> **开始日期**: 2026-07-18
> **目标**: 5-6 个月内完成全部阶段
> **更新**: 每次学习后更新本文档

---

## 📊 总览

```
阶段 0: 编程起步        [████████████████████] 100%  (5/5 模块) ✅
阶段 1: LLM 基础        [███████████████████░]  98%  (6/6 模块) ✅
阶段 2: Agent 核心      [████████████████████] 100%  (6/6 模块) ✅
阶段 3: RAG 专题        [░░░░░░░░░░░░░░░░░░░░]   0%  (0/7 模块)
阶段 4: 框架实战        [░░░░░░░░░░░░░░░░░░░░]   0%  (0/5 模块)
阶段 5: 工程化          [░░░░░░░░░░░░░░░░░░░░]   0%  (0/5 模块)
阶段 6: 进阶专题        [░░░░░░░░░░░░░░░░░░░░]   0%  (选学)
阶段 7: 元能力          [░░░░░░░░░░░░░░░░░░░░]   0%  (持续)
──────────────────────────────────────────────────────────
总体进度               [█████████████░░░░░░░]  47%  (条目口径, 与 check_progress.py 一致)
```

## 📅 学习日历

> 记录每个学习日，点击跳转到详细日志

| Day | 日期 | 时间段 | 核心内容 | 日志 |
|-----|------|--------|---------|------|
| 1 | 07-18 | — | Python 基础 + Git 入门 | [📝](logs/day-01.md) |
| 2 | 07-22 | — | 文件读写 + OOP 入门 | [📝](logs/day-02.md) |
| 3 | 07-31 | 08:00-09:10 | 继承 + dataclass + API 调用 | [📝](logs/day-03.md) |
| 4 | 08-01 | 06:00-11:05 | 阶段 1 全部通关 🏁 | [📝](logs/day-04.md) |
| 5 | 08-09 | — | 2.1 Tool Calling + 2.2 ReAct 循环 + 文件助手 | [📝](logs/day-05.md) |
| 6 | 08-16 | — | 复习 + 2.3 记忆系统（滑动窗口 + 摘要压缩） | [📝](logs/day-06.md) |
| 7 | 08-30 | 08:00-19:30 | 全仓规范整改 + 2.3 通关（对比实验/偏好记忆/挑战/阅读）+ 2.4 开荒 | [📝](logs/day-07.md) |
| 8 | 09-05 | 10:00-22:47 | 2.4+2.5 双封箱 + 2.6 前两仗（注入靶场/权限分级）+ 图谱前端改造 | [📝](logs/day-08.md) |
| 9 | 09-06 | 09:00-14:00 | **2.6 封箱 + 阶段 2 验收 20/20 🏆** + PML 音频支线通车 | [📝](logs/day-09.md) |
| 🔄 | — | — | 复习日（每 5 个学习日 1 次） | — |

**下一目标**: 阶段 3 RAG 专题（3.1 最简 RAG——给 StudyNote 装上语义检索）

> 🔄 复习日内容: 跑 🔴 核心脚本并解释原理 + 扫 PITFALLS Top 5 + 重测 STUDYNOTE_EVAL（阶段 2 后）

---

## 🎯 北极星项目: 📚 StudyNote 学习笔记 Agent

> 贯穿全程的主线项目：每个阶段学完，给它加一块能力，练习从"孤立作业"变成"给主线项目添砖"。

**定位**: 能读懂本仓库学习资料（logs + KNOWLEDGE_BASE）并回答学习问题的 Agent。

| 阶段完成时 | 给它加的能力 |
|-----------|-------------|
| 阶段 2 🟡 进行中 | 单 Agent 系统（读文件 + 工具 + ReAct）—— 雏形 `file_agent.py` |
| 阶段 3 | 装上 RAG：以 `logs/` + `KNOWLEDGE_BASE.md` 为语料，回答"我之前学过什么" |
| 阶段 4 | LangGraph 重写 / 提供 MCP Server |
| 阶段 5 | FastAPI + Docker 部署，可访问服务 |

---

## 🧪 阶段通关标准 & 学习方法

**每个模块/阶段通关必须满足三件套**:
1. ✅ 练习全部 PASS（`python xxx.py` 一次性验证）
2. 🧩 独立挑战题完成（AI 出一个不教的新题，独立实现——证明"会做没教过的"）
3. 📝 300 字费曼总结（把核心概念讲给外行听，写入当日日志）

**复习日机制**: 每 5 个学习日插入 1 个复习日:
- 跑一遍 🔴 核心脚本并解释其工作原理
- 扫一遍 `PITFALLS.md` Top 5
- 重测 `STUDYNOTE_EVAL`（阶段 2 完成后）

---

## 🏁 阶段 0: 编程起步 (预计 3-4 周)

### 0.1 编程思维入门（3-4天）
- [x] 理解什么是编程语言
- [x] 变量、数据类型、条件判断、循环、函数
- [x] 会使用终端/命令行
- [x] 🔧 练习：猜数字游戏 📎 `guess_game.py`
- [x] 🔧 练习：简单计算器 📎 `calculator.py`
- [x] ✅ 检验：能独立写 30 行的终端小程序

### 0.2 Python 基础语法（5-7天）
- [x] 字符串操作（拼接、切片、f-string）
- [x] list / tuple / dict / set 四种数据结构
- [x] 文件读写 open/read/write
- [x] 异常处理 try/except
- [x] 模块导入 import
- [x] pip 包管理器（conda 环境已掌握）
- [x] venv 虚拟环境（conda 环境已掌握）
- [x] 🔧 练习：待办事项命令行程序（score_parser 替代） 📎 `score_parser.py`
- [x] 🔧 练习：CSV 数据统计 📎 `csv_stats.py`
- [x] 🔧 练习：调用天气 API（合并到阶段 1.3）
- [x] ✅ 检验：独立写 100 行 Python 脚本 📎 `library_system.py` `employee_system.py`

### 0.3 Git 与命令行（2-3天）
- [x] 终端基本操作 cd/ls/mkdir/rm/pwd
- [x] Git 概念理解
- [x] git init / add / commit / status / log
- [x] GitHub 使用
- [x] push / pull / clone
- [x] .gitignore
- [x] 🔧 练习：所有代码推到 GitHub
- [x] ✅ 检验：能用 Git 管理代码版本

### 0.4 开发环境搭建（1天）
- [x] VS Code 安装与配置
- [x] 必装插件：Python, Pylance, GitLens
- [x] 终端集成
- [x] 调试器使用（断点、单步执行）
- [x] ✅ 检验：在 VS Code 里跑通一个 Python 脚本

### 0.5 面向对象基础（2-3天）
- [x] 类与对象概念
- [x] __init__ 构造函数
- [x] 实例方法 vs 静态方法
- [x] 继承
- [x] dataclass
- [x] Type hints 类型注解
- [x] 🔧 练习：图书馆管理系统 📎 `library_system.py`
- [x] ✅ 检验：理解类与对象的关系

### 阶段 0 全部完成标志 🏁
- [x] 所有子模块 ✅
- [x] GitHub 上有 ≥ 5 个练习项目（guess_game, calculator, list_stats, score_parser, csv_stats, library_system, employee_system, task_manager）
- [x] 能独立搭建 Python 开发环境（VS Code + conda + Git）
- [x] 能阅读中等复杂度的 Python 代码（继承链、dataclass、类型标注）

---

## 🤖 阶段 1: LLM 基础 (预计 3 周)

### 1.1 AI/ML/LLM 概念扫盲（2天）
- [x] AI → ML → DL → LLM → Agent 的层级关系
- [x] Token 概念理解
- [x] 参数（7B/70B）是什么
- [x] 上下文窗口概念
- [x] 幻觉是什么
- [x] 训练 vs 推理
- [x] 🔧 练习：在 Tokenizer 工具上实验 📎 `test_jiekou.py`（token 计数）
- [x] 🔧 练习：用不同 LLM 对比同一个问题 📎 `compare_models.py`
- [x] ✅ 检验：能用通俗语言解释 LLM 是什么

### 1.2 主流模型全景图（1天）
- [x] Claude / GPT / Gemini / Llama / DeepSeek / Qwen 对比
- [x] 注册 Anthropic Console
- [ ] 注册 OpenAI Platform（可选——DeepSeek+Claude 已够用）
- [x] 拿到第一把 API Key
- [x] ✅ 检验：知道什么场景选什么模型

### 1.3 第一次 API 调用（2-3天）
- [x] HTTP 请求基础（GET/POST/Header/Body/JSON）
- [x] API Key 安全（环境变量 .env）
- [x] Messages API 结构
- [x] system/user/assistant/tool 四个角色
- [x] max_tokens、temperature 参数
- [x] 读取返回结果和 usage
- [x] 🔧 练习：第一个 API 调用脚本 📎 `first_api_call.py`
- [x] 🔧 练习：多轮对话脚本 📎 `multi_turn_chat.py`
- [x] 🔧 练习：API Key 放 .env
- [x] ✅ 检验：用代码完成 3 轮以上对话 📎 `message_roles.py`

### 1.4 Streaming 流式输出（1-2天）
- [x] 为什么需要流式输出
- [x] SSE 原理
- [x] stream=True 用法
- [x] 🔧 练习：流式聊天机器人 📎 `stream_chat.py`
- [x] ✅ 检验：实现逐字输出效果

### 1.5 Prompt Engineering（3-4天）
- [x] System Prompt 设计四法则
- [x] Zero-shot / Few-shot / CoT
- [x] 结构化 Prompt（XML 标签）
- [x] 🔧 练习：同一任务，3 种 prompt 对比 📎 `prompt_engineering.py`
- [x] 🔧 练习：角色扮演实验 📎 `prompt_xml_role.py`
- [x] 🔧 练习：格式控制（强制 JSON 输出）📎 `prompt_engineering.py`
- [x] 📝 建立个人 Prompt 库 📎 `prompt_library.py`
- [x] ✅ 检验：能稳定控制 LLM 输出格式

### 1.6 Structured Output（1-2天）
- [x] JSON Mode 原理
- [x] Pydantic 定义数据结构
- [x] 约束 LLM 按 Schema 输出
- [x] 🔧 练习：让 LLM 输出结构化菜谱 📎 `structured_output.py`
- [x] ✅ 检验：LLM 输出可被代码安全消费

### 阶段 1 全部完成标志 🏁
- [x] 所有子模块 ✅
- [x] 能用代码调用至少 2 个不同厂商的 API
- [x] 有个人 Prompt 库
- [x] 能设计 System Prompt 让 LLM 扮演专业角色

---

## 🧠 阶段 2: Agent 核心 (预计 4 周)

### 2.1 Tool Calling 深入（3-4天）✅
- [x] 工具 = 函数 + JSON Schema
- [x] Schema 设计原则（命名、描述、参数）
- [x] 工具执行流程（tool_use → execute → tool_result）
- [x] 🔧 练习：定义 3 个工具并让 LLM 选择调用 📎 `tool_calling.py`
- [x] 🔧 练习：并行工具调用 📎 `parallel_tools.py`
- [x] 🔧 练习：JSON 深度实战 📎 `json_deep_dive.py`
- [x] ✅ 检验：Agent 能正确选择和使用工具（单工具+双工具选择+并行调用 7/7 PASS）

### 2.2 Agent 循环手写（3-4天）✅
- [x] ReAct 循环原理彻底理解
- [x] Agent 状态数据结构设计（AgentState dataclass）
- [x] 终止条件设计（max_iterations + consecutive_errors）
- [x] 🔧 练习：手写 100-150 行 Agent 循环 📎 `react_loop.py`
- [x] 🔧 练习：智能文件助手 Agent 📎 `file_agent.py`
- [x] 🔧 练习：测试 5-10 步完成多工具任务（测试6: 3步链式文件操作）
- [x] ✅ 检验：Agent 不会无限循环，能处理工具失败

### 2.3 记忆系统（3-4天）
- [x] 三种记忆分工（短期/长期/工作）
- [x] 滑动窗口 vs 摘要压缩 vs 混合策略
- [x] 🔧 练习：实现滑动窗口记忆 📎 `sliding_window_memory.py`
- [x] 🔧 练习：实现摘要压缩记忆 📎 `summary_compression_memory.py`
- [x] 🔧 练习：对比两种策略的效果 📎 `memory_strategy_compare.py`
- [x] ✅ 检验：Agent 能跨对话记住用户偏好 📎 `preference_memory.py`
- [x] 🧩 独立挑战题：多用户记忆金库 📎 `memory_vault.py`
- [x] ⏭️ 向量长期记忆 → 已确认延后至 3.3（见 3.3 回头补条目）
- [x] 📖 阅读: Anthropic《Effective context engineering for AI agents》

### 2.4 任务规划与分解（2-3天）
- [x] Plan-and-Execute 模式
- [x] 动态重规划
- [x] 🔧 练习：Agent 先规划再执行 📎 `plan_and_execute.py`
- [x] 🔧 练习：测试执行中受阻→自动调整 📎 `replan_loop.py`
- [x] ✅ 检验：复杂任务能被正确分解执行 📎 `plan_verify.py`
- [x] 📖 阅读: Anthropic《Building Effective Agents》（Plan-and-Execute 部分）
- [x] 🧩 独立挑战题：依赖感知执行器 📎 `dep_executor.py`

### 2.5 Reflection 反思机制（2天）
- [x] 反思循环：生成 → 自评 → 改进
- [x] 反思的成本效益分析
- [x] 🔧 练习：给 Agent 加自反思 📎 `reflection_loop.py`
- [x] 🔧 练习：对比开/关反思的质量和成本 📎 `reflection_cost_benefit.py`
- [x] ✅ 检验：理解反思何时值得用
- [x] 📖 阅读: Reflexion 论文（Shinn et al., 2023）
- [x] 🧩 独立挑战题：跨试次情景记忆 📎 `episodic_reflection.py`

### 2.6 安全与护栏入门（2-3天）
- [x] Agent 安全威胁矩阵
- [x] Prompt 注入理解
- [x] 工具权限分级（🟢🟡🔴）
- [x] 输出校验
- [x] 沙箱隔离
- [x] 🔧 练习：攻击自己的 Agent 📎 `prompt_injection_lab.py`
- [x] 🔧 练习：实现工具权限分级 📎 `tool_permissions.py`
- [x] ✅ 检验：能说出 5 种攻击手段和防御方案
- [x] 📖 阅读: OWASP LLM Top 10（初读）

### 阶段 2 全部完成标志 🏁
- [x] 所有子模块 ✅
- [x] 有一个可独立工作的单 Agent 系统
- [x] Agent 有记忆、能规划、会反思
- [x] Agent 有基本安全防护
- [x] 🎯 北极星: StudyNote Agent 雏形跑通（读 logs 目录 + 回答问题）
- [x] 📊 验收: 通过 STUDYNOTE_EVAL 评估集（**20/20** 🏆）📎 `studynote_eval.md` 📎 `studynote_agent.py`

---

## 📚 阶段 3: RAG 专题 (预计 3 周)

> 🎯 北极星落点: 给 StudyNote Agent 装上 RAG，用 logs + KNOWLEDGE_BASE 做语料

### 3.1 RAG 原理与最简实现（2-3天）
- [ ] LLM 三大缺陷 → RAG 的诞生
- [ ] 存入流程（文档→切块→向量化→存库）
- [ ] 查询流程（提问→向量化→检索→拼Prompt→回答）
- [ ] 🔧 练习：50 行代码实现最简 RAG
- [ ] ✅ 检验：理解 RAG 每个环节的作用
- [ ] 📖 阅读: RAG 原论文（Lewis et al., 2020）

### 3.2 文档解析与分块（2-3天）
- [ ] PDF/HTML/Office 解析
- [ ] 固定分块 vs 递归分块 vs 语义分块 vs 句子窗口
- [ ] 元数据的重要性
- [ ] 🔧 练习：3 种策略对比实验
- [ ] 🔧 练习：加来源标注
- [ ] ✅ 检验：能为真实文档选择合适的分块策略
- [ ] 📖 阅读: LangChain Text Splitters 文档

### 3.3 Embedding 与向量数据库（2-3天）
- [ ] 主流 Embedding 模型对比
- [ ] 向量数据库选型指南
- [ ] 🔧 练习：Chroma 搭本地向量库
- [ ] 🔧 练习：对比不同 Embedding 模型
- [ ] 📊 评估贯穿: 建测试查询集，每次练习记录检索命中率（hit rate）
- [ ] 🔄 回头补 2.3: 用 Embedding 给 StudyNote Agent 升级向量长期记忆
- [ ] ✅ 检验：算得出检索命中率
- [ ] 📖 阅读: ChromaDB Getting Started 文档

### 3.4 检索策略进阶（2-3天）
- [ ] 混合检索（稠密+稀疏）
- [ ] Query 变换（重写/分解/HyDE）
- [ ] Reranking 精排
- [ ] 🔧 练习：实现混合检索
- [ ] 🔧 练习：加 Reranker 对比效果
- [ ] ✅ 检验：检索准确率 ≥ 90%
- [ ] 📖 阅读: Pinecone《Hybrid Search》/ Qdrant hybrid search 文档

### 3.5 Agentic RAG（2-3天）
- [ ] 传统 RAG vs Agentic RAG
- [ ] Agent 自主决定何时检索、检索哪里
- [ ] 检索结果批判
- [ ] 🔧 练习：给 Agent 装上 RAG 工具
- [ ] 🔧 练习：实现检索不满意 → 自动重搜
- [ ] ✅ 检验：Agent 不盲信检索结果
- [ ] 📖 阅读: Anthropic《Contextual Retrieval》

### 3.6 Text-to-SQL（1-2天）🔹 选学（与主线项目无关，按兴趣安排）
- [ ] 表结构 → Schema → SQL → 执行 → 解读
- [ ] 防注入、权限控制
- [ ] 🔧 练习：Agent 查数据库回答问题
- [ ] ✅ 检验：Agent 能写对中等复杂度的 SQL

### 3.7 RAG 评估（1-2天）
- [ ] RAGAS 四大指标
- [ ] Faithfulness / Answer Relevance / Context Precision / Recall
- [ ] 🔧 练习：用 RAGAS 评估自己的 RAG
- [ ] ✅ 检验：能科学评估并改进 RAG
- [ ] 📖 阅读: RAGAS 官方文档

### 阶段 3 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] 有一个完整的 RAG 系统（文档→检索→回答）
- [ ] 检索质量 ≥ 90%
- [ ] 有评估报告（RAGAS 指标）

---

## 🔧 阶段 4: 框架实战 (预计 4 周)

> 🎯 北极星落点: 把 StudyNote Agent 迁移到 LangGraph + 提供 MCP Server

### 4.1 OpenAI 兼容 SDK 深入（3-4天）
- [ ] 工具调用最佳实践（并行 + 结构化参数）
- [ ] 流式事件处理（打字机效果 + tool_use 事件流）
- [ ] Prompt Caching
- [ ] Token counting
- [ ] 🔧 练习：用 SDK 重写 react_loop（含流式）
- [ ] 🔧 练习：测量 Cache 带来的成本差异
- [ ] 📖 对比: Anthropic SDK（ToolRunner 机制）仅作了解
- [ ] ✅ 检验：能用 SDK 最佳实践写 Agent

### 4.2 LangGraph 图式 Agent（4-5天）
- [ ] 从链到图的概念转变
- [ ] State / Node / Edge / Checkpointing
- [ ] 🔧 练习：手写循环迁移到 LangGraph
- [ ] 🔧 练习：人类确认节点
- [ ] 🔧 练习：断点恢复
- [ ] ✅ 检验：能用图建模复杂 Agent 流程
- [ ] 📖 阅读: LangGraph Quick Start 文档

### 4.3 MCP 协议（3-4天）
- [ ] MCP 解决什么问题
- [ ] Tools / Resources / Prompts 三大原语
- [ ] STDIO vs SSE/HTTP
- [ ] 🔧 练习：写一个 MCP Server
- [ ] 🔧 练习：写一个 MCP Client
- [ ] 🔧 练习：让 Claude Code 连你的 Server
- [ ] ✅ 检验：能开发实用的 MCP Server
- [ ] 📖 阅读: modelcontextprotocol.io 官方规范

### 4.4 多 Agent 协作（3-4天）
- [ ] 流水线/辩论/层级/黑板四种模式
- [ ] 什么时候该用多 Agent
- [ ] 🔧 练习：CrewAI 编编辑部
- [ ] 🔧 练习：AutoGen 代码审查组
- [ ] 🔧 练习：对比单 Agent vs 多 Agent
- [ ] ✅ 检验：能判断是否需要多 Agent
- [ ] 📖 阅读: Anthropic《How we built our multi-agent research system》

### 4.5 RAG 框架对比（2-3天）
- [ ] LlamaIndex 完整链路
- [ ] LangChain RAG 链式编排
- [ ] 选型指南
- [ ] 🔧 练习：主攻一个框架完整实现 RAG + 另一个仅读文档对比
- [ ] ✅ 检验：能根据场景选框架

### 阶段 4 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] 掌握至少 2 个框架
- [ ] 有 1 个 MCP Server
- [ ] 能独立评估和选择开发框架

---

## 🚀 阶段 5: 工程化 (预计 4 周)

> 🎯 北极星落点: StudyNote Agent 以 FastAPI + Docker 部署上线，带评估和监控

### 5.1 Agent 评估体系（4-5天）
- [ ] 评估金字塔（单元→自动→LLM Judge→人工）
- [ ] LLM-as-Judge 实现
- [ ] Prompt 回归测试（promptfoo）
- [ ] 🔧 练习：50 个测试用例 + LLM Judge
- [ ] 🔧 练习：搭建 Prompt 回归测试管道
- [ ] ✅ 检验：有可量化的 Agent 质量评估
- [ ] 📖 阅读: promptfoo 官方文档

### 5.2 可观测性（2-3天）
- [ ] 三层可观测（Log / Trace / Metrics）
- [ ] OpenTelemetry + 平台
- [ ] 🔧 练习：完整日志记录
- [ ] 🔧 练习：LangSmith Trace
- [ ] 🔧 练习：成本计算器
- [ ] ✅ 检验：能在 Trace 中看到完整 Agent 调用链路
- [ ] 📖 阅读: LangSmith / OpenTelemetry 文档

### 5.3 CI/CD for Agent（2天）
- [ ] Prompt 变更流水线设计
- [ ] 🔧 练习：GitHub Actions + promptfoo
- [ ] ✅ 检验：Eval 分数下降 → CI 自动拦截
- [ ] 📖 阅读: GitHub Actions 官方文档

### 5.4 安全深度（2-3天）
- [ ] 间接注入 / 多阶段注入 / 工具返回注入
- [ ] 分层防护架构
- [ ] 人机协同设计
- [ ] 🔧 练习：红队攻击自己的 Agent
- [ ] 🔧 练习：实现完整防护体系
- [ ] ✅ 检验：防御至少 3 种注入攻击
- [ ] 📖 阅读: OWASP LLM Top 10（深读）

### 5.5 生产部署（2-3天）
- [ ] 部署演进路径（本地→API→Docker→K8s）
- [ ] FastAPI + Docker
- [ ] 性能策略（Cache/并发/路由/流式）
- [ ] 🔧 练习：FastAPI 包装 Agent
- [ ] 🔧 练习：Docker 部署 + 压测
- [ ] ✅ 检验：Agent 作为 API 服务稳定运行
- [ ] 📖 阅读: FastAPI 官方教程

### 阶段 5 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] Agent 有评估、有监控、有 CI/CD
- [ ] Agent 通过安全红队测试
- [ ] Agent 可作为稳定 API 服务运行

---

## 🚁 阶段 6: 进阶专题 (选学，按兴趣挑)

### 6.1 多模态 Agent
- [ ] 视觉理解 API（图像输入/输出）
- [ ] 文生图集成
- [ ] 🔧 练习：看图说话的 Agent

### 6.2 Computer Use
- [ ] 浏览器/桌面操作 Agent 原理
- [ ] 工具局限与风险

### 6.3 语音 Agent
- [ ] ASR / TTS 接入
- [ ] 实时语音对话架构

### 6.4 代码 Agent
- [ ] Claude Code 原理
- [ ] SWE-bench 概念
- [ ] 🔧 练习：用 Agent 自动修 bug

### 6.5 本地模型
- [ ] Ollama + 开源模型
- [ ] 私有化部署场景

---

## 🧭 阶段 7: 元能力 (持续进行)

### 7.1 读论文
- [ ] 每周 1 篇 arxiv 论文 + 3 行总结（写入日志）

### 7.2 读源码
- [ ] 挑 chromadb / langgraph 一个核心模块读源码，画调用流程图

### 7.3 技术写作
- [ ] 每阶段结束写 1 篇博客/笔记（费曼式输出）

### 7.4 教别人
- [ ] 把学过的概念讲给外行/新手听，检验理解深度

---

## 📈 每日学习日志模板

```markdown
## 2026-07-XX

### 今天学了什么
-

### 今天写了什么代码
-

### 今天踩了什么坑
-

### 今天的一个收获
-

### 明天计划
-

```

---

## 🏆 里程碑地图

| 里程 | 阶段 | 标志 | 预计日期 | 状态 |
|------|------|------|----------|------|
| M1 🟢 | 0 完成 | 能独立写 Python 脚本 | 2026-07-31 | ✅ |
| M2 🔵 | 1 完成 | 第一次 API 调用成功 | 2026-08-01 | ✅ |
| M3 🟡 | 1 完成 | 流式聊天机器人 | 2026-08-01 | ✅ |
| M4 🟠 | 2 完成 | 手写 Agent 循环 | 2026-08-09 | ✅ |
| M5 🟣 | 2 完成 | StudyNote Agent 雏形 + 有记忆 | 2026-09-06 | ✅ |
| M6 📗 | 3 完成 | StudyNote 最简 RAG 版 | ___ | ⬜ |
| M7 📘 | 3 完成 | Agentic RAG（自主检索） | ___ | ⬜ |
| M8 🔴 | 4 完成 | 框架实战告捷（LangGraph + MCP） | ___ | ⬜ |
| M9 🏗️ | 5 完成 | 生产部署成功（FastAPI + Docker） | ___ | ⬜ |
| M10 🏆 | 全部完成 | StudyNote Agent 产品上线 | ___ | ⬜ |
