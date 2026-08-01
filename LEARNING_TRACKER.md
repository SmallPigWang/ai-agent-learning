# 🎓 AI Agent 学习进度追踪看板

> **开始日期**: 2026-07-18
> **目标**: 5-6 个月内完成全部阶段
> **更新**: 每次学习后更新本文档

---

## 📊 总览

```
阶段 0: 编程起步        [████████████████████] 100%  (5/5 模块) ✅
阶段 1: LLM 基础        [████████████████████] 100%  (6/6 模块) ✅
阶段 2: Agent 核心      [░░░░░░░░░░░░░░░░░░░░]   0%  (0/6 模块)
阶段 3: RAG 专题        [░░░░░░░░░░░░░░░░░░░░]   0%  (0/7 模块)
阶段 4: 框架实战        [░░░░░░░░░░░░░░░░░░░░]   0%  (0/5 模块)
阶段 5: 工程化          [░░░░░░░░░░░░░░░░░░░░]   0%  (0/5 模块)
阶段 6: 进阶专题        [░░░░░░░░░░░░░░░░░░░░]   0%  (选学)
阶段 7: 元能力          [░░░░░░░░░░░░░░░░░░░░]   0%  (持续)
──────────────────────────────────────────────────────────
总体进度               [█████████░░░░░░░░░░░]  32%
```

## 📅 学习日历

> 记录每个学习日，点击跳转到详细日志

| Day | 日期 | 时间段 | 核心内容 | 日志 |
|-----|------|--------|---------|------|
| 1 | 07-18 | — | Python 基础 + Git 入门 | [📝](logs/day-01.md) |
| 2 | 07-22 | — | 文件读写 + OOP 入门 | [📝](logs/day-02.md) |
| 3 | 07-31 | 08:00-09:10 | 继承 + dataclass + API 调用 | [📝](logs/day-03.md) |
| 4 | 08-01 | 06:00-11:05 | 阶段 1 全部通关 🏁 | [📝](logs/day-04.md) |
| 5 | — | — | 阶段 2: Tool Calling | — |

**下一目标**: 阶段 2.1 Tool Calling 深入

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

### 2.1 Tool Calling 深入（3-4天）
- [ ] 工具 = 函数 + JSON Schema
- [ ] Schema 设计原则（命名、描述、参数）
- [ ] 工具执行流程（tool_use → execute → tool_result）
- [ ] 🔧 练习：定义 3 个工具并让 LLM 选择调用
- [ ] 🔧 练习：并行工具调用
- [ ] ✅ 检验：Agent 能正确选择和使用工具

### 2.2 Agent 循环手写（3-4天）
- [ ] ReAct 循环原理彻底理解
- [ ] Agent 状态数据结构设计
- [ ] 终止条件设计
- [ ] 🔧 练习：手写 100-150 行 Agent 循环
- [ ] 🔧 练习：智能文件助手 Agent
- [ ] 🔧 练习：测试 5-10 步完成多工具任务
- [ ] ✅ 检验：Agent 不会无限循环，能处理工具失败

### 2.3 记忆系统（3-4天）
- [ ] 三种记忆分工（短期/长期/工作）
- [ ] 滑动窗口 vs 摘要压缩 vs 混合策略
- [ ] 向量存储长期记忆
- [ ] 🔧 练习：实现滑动窗口记忆
- [ ] 🔧 练习：实现摘要压缩记忆
- [ ] 🔧 练习：对比两种策略的效果
- [ ] ✅ 检验：Agent 能跨对话记住用户偏好

### 2.4 任务规划与分解（2-3天）
- [ ] Plan-and-Execute 模式
- [ ] 动态重规划
- [ ] 🔧 练习：Agent 先规划再执行
- [ ] 🔧 练习：测试执行中受阻→自动调整
- [ ] ✅ 检验：复杂任务能被正确分解执行

### 2.5 Reflection 反思机制（2天）
- [ ] 反思循环：生成 → 自评 → 改进
- [ ] 反思的成本效益分析
- [ ] 🔧 练习：给 Agent 加自反思
- [ ] 🔧 练习：对比开/关反思的质量和成本
- [ ] ✅ 检验：理解反思何时值得用

### 2.6 安全与护栏入门（2-3天）
- [ ] Agent 安全威胁矩阵
- [ ] Prompt 注入理解
- [ ] 工具权限分级（🟢🟡🔴）
- [ ] 输出校验
- [ ] 沙箱隔离
- [ ] 🔧 练习：攻击自己的 Agent
- [ ] 🔧 练习：实现工具权限分级
- [ ] ✅ 检验：能说出 5 种攻击手段和防御方案

### 阶段 2 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] 有一个可独立工作的单 Agent 系统
- [ ] Agent 有记忆、能规划、会反思
- [ ] Agent 有基本安全防护

---

## 📚 阶段 3: RAG 专题 (预计 3 周)

### 3.1 RAG 原理与最简实现（2-3天）
- [ ] LLM 三大缺陷 → RAG 的诞生
- [ ] 存入流程（文档→切块→向量化→存库）
- [ ] 查询流程（提问→向量化→检索→拼Prompt→回答）
- [ ] 🔧 练习：50 行代码实现最简 RAG
- [ ] ✅ 检验：理解 RAG 每个环节的作用

### 3.2 文档解析与分块（2-3天）
- [ ] PDF/HTML/Office 解析
- [ ] 固定分块 vs 递归分块 vs 语义分块 vs 句子窗口
- [ ] 元数据的重要性
- [ ] 🔧 练习：3 种策略对比实验
- [ ] 🔧 练习：加来源标注
- [ ] ✅ 检验：能为真实文档选择合适的分块策略

### 3.3 Embedding 与向量数据库（2-3天）
- [ ] 主流 Embedding 模型对比
- [ ] 向量数据库选型指南
- [ ] 🔧 练习：Chroma 搭本地向量库
- [ ] 🔧 练习：对比不同 Embedding 模型
- [ ] ✅ 检验：算得出检索命中率

### 3.4 检索策略进阶（2-3天）
- [ ] 混合检索（稠密+稀疏）
- [ ] Query 变换（重写/分解/HyDE）
- [ ] Reranking 精排
- [ ] 🔧 练习：实现混合检索
- [ ] 🔧 练习：加 Reranker 对比效果
- [ ] ✅ 检验：检索准确率 ≥ 90%

### 3.5 Agentic RAG（2-3天）
- [ ] 传统 RAG vs Agentic RAG
- [ ] Agent 自主决定何时检索、检索哪里
- [ ] 检索结果批判
- [ ] 🔧 练习：给 Agent 装上 RAG 工具
- [ ] 🔧 练习：实现检索不满意 → 自动重搜
- [ ] ✅ 检验：Agent 不盲信检索结果

### 3.6 Text-to-SQL（1-2天）
- [ ] 表结构 → Schema → SQL → 执行 → 解读
- [ ] 防注入、权限控制
- [ ] 🔧 练习：Agent 查数据库回答问题
- [ ] ✅ 检验：Agent 能写对中等复杂度的 SQL

### 3.7 RAG 评估（1-2天）
- [ ] RAGAS 四大指标
- [ ] Faithfulness / Answer Relevance / Context Precision / Recall
- [ ] 🔧 练习：用 RAGAS 评估自己的 RAG
- [ ] ✅ 检验：能科学评估并改进 RAG

### 阶段 3 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] 有一个完整的 RAG 系统（文档→检索→回答）
- [ ] 检索质量 ≥ 90%
- [ ] 有评估报告（RAGAS 指标）

---

## 🔧 阶段 4: 框架实战 (预计 4 周)

### 4.1 Anthropic SDK 深入（3-4天）
- [ ] ToolRunner 机制
- [ ] 并行工具调用
- [ ] Prompt Caching
- [ ] Token counting
- [ ] 🔧 练习：并行工具调用 Agent
- [ ] 🔧 练习：测量 Cache 带来的成本差异
- [ ] ✅ 检验：能用 SDK 最佳实践写 Agent

### 4.2 LangGraph 图式 Agent（4-5天）
- [ ] 从链到图的概念转变
- [ ] State / Node / Edge / Checkpointing
- [ ] 🔧 练习：手写循环迁移到 LangGraph
- [ ] 🔧 练习：人类确认节点
- [ ] 🔧 练习：断点恢复
- [ ] ✅ 检验：能用图建模复杂 Agent 流程

### 4.3 MCP 协议（3-4天）
- [ ] MCP 解决什么问题
- [ ] Tools / Resources / Prompts 三大原语
- [ ] STDIO vs SSE/HTTP
- [ ] 🔧 练习：写一个 MCP Server
- [ ] 🔧 练习：写一个 MCP Client
- [ ] 🔧 练习：让 Claude Code 连你的 Server
- [ ] ✅ 检验：能开发实用的 MCP Server

### 4.4 多 Agent 协作（3-4天）
- [ ] 流水线/辩论/层级/黑板四种模式
- [ ] 什么时候该用多 Agent
- [ ] 🔧 练习：CrewAI 编编辑部
- [ ] 🔧 练习：AutoGen 代码审查组
- [ ] 🔧 练习：对比单 Agent vs 多 Agent
- [ ] ✅ 检验：能判断是否需要多 Agent

### 4.5 RAG 框架对比（2-3天）
- [ ] LlamaIndex 完整链路
- [ ] LangChain RAG 链式编排
- [ ] 选型指南
- [ ] 🔧 练习：同一 RAG 用两个框架实现
- [ ] ✅ 检验：能根据场景选框架

### 阶段 4 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] 掌握至少 2 个框架
- [ ] 有 1 个 MCP Server
- [ ] 能独立评估和选择开发框架

---

## 🚀 阶段 5: 工程化 (预计 4 周)

### 5.1 Agent 评估体系（4-5天）
- [ ] 评估金字塔（单元→自动→LLM Judge→人工）
- [ ] LLM-as-Judge 实现
- [ ] Prompt 回归测试（promptfoo）
- [ ] 🔧 练习：50 个测试用例 + LLM Judge
- [ ] 🔧 练习：搭建 Prompt 回归测试管道
- [ ] ✅ 检验：有可量化的 Agent 质量评估

### 5.2 可观测性（2-3天）
- [ ] 三层可观测（Log / Trace / Metrics）
- [ ] OpenTelemetry + 平台
- [ ] 🔧 练习：完整日志记录
- [ ] 🔧 练习：LangSmith Trace
- [ ] 🔧 练习：成本计算器
- [ ] ✅ 检验：能在 Trace 中看到完整 Agent 调用链路

### 5.3 CI/CD for Agent（2天）
- [ ] Prompt 变更流水线设计
- [ ] 🔧 练习：GitHub Actions + promptfoo
- [ ] ✅ 检验：Eval 分数下降 → CI 自动拦截

### 5.4 安全深度（2-3天）
- [ ] 间接注入 / 多阶段注入 / 工具返回注入
- [ ] 分层防护架构
- [ ] 人机协同设计
- [ ] 🔧 练习：红队攻击自己的 Agent
- [ ] 🔧 练习：实现完整防护体系
- [ ] ✅ 检验：防御至少 3 种注入攻击

### 5.5 生产部署（2-3天）
- [ ] 部署演进路径（本地→API→Docker→K8s）
- [ ] FastAPI + Docker
- [ ] 性能策略（Cache/并发/路由/流式）
- [ ] 🔧 练习：FastAPI 包装 Agent
- [ ] 🔧 练习：Docker 部署 + 压测
- [ ] ✅ 检验：Agent 作为 API 服务稳定运行

### 阶段 5 全部完成标志 🏁
- [ ] 所有子模块 ✅
- [ ] Agent 有评估、有监控、有 CI/CD
- [ ] Agent 通过安全红队测试
- [ ] Agent 可作为稳定 API 服务运行

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

### 自我评分 (1-5)
- 理解程度: 
- 完成度: 
- 投入度: 
```

---

## 🏆 里程碑地图

| 里程 | 阶段 | 标志 | 预计日期 | 状态 |
|------|------|------|----------|------|
| M1 🟢 | 0 完成 | 能独立写 Python 脚本 | 2026-07-31 | ✅ |
| M2 🔵 | 1 完成 | 第一次 API 调用成功 | 2026-08-01 | ✅ |
| M3 🟡 | 1 完成 | 流式聊天机器人 | 2026-08-01 | ✅ |
| M4 🟠 | 2 完成 | 手写 Agent 循环 | ___ | ⬜ |
| M5 🟣 | 2 完成 | 有记忆的 Agent | ___ | ⬜ |
| M6 📗 | 3 完成 | 最简 RAG 系统 | ___ | ⬜ |
| M7 📘 | 3 完成 | Agentic RAG | ___ | ⬜ |
| M8 🔴 | 4 完成 | 框架实战告捷 | ___ | ⬜ |
| M9 🏗️ | 5 完成 | 生产部署成功 | ___ | ⬜ |
| M10 🏆 | 全部完成 | 完整 Agent 产品上线 | ___ | ⬜ |
