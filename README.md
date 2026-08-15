# 🎓 AI Agent 学习项目

> 从零开始学习 AI Agent 开发：Python → LLM API → 手写 Agent → RAG → 框架 → 工程化。
> 目标：5-6 个月内从编程零基础到能独立开发、评估、部署一个完整的 Agent 产品。

![进度](https://img.shields.io/badge/进度-37%25-1a73e8)

## 📊 当前进度

| 阶段 | 内容 | 进度 | 状态 |
|------|------|------|------|
| 0 | 编程起步（Python + Git + OOP） | 100% | ✅ 完成 |
| 1 | LLM 基础（API / 流式 / Prompt / 结构化输出） | 100% | ✅ 完成 |
| 2 | Agent 核心（Tool Calling / ReAct / 记忆 / 规划 / 反思 / 安全） | 29% | 🟡 进行中 |
| 3 | RAG 专题 | 0% | ⬜ |
| 4 | 框架实战（SDK / LangGraph / MCP / 多 Agent） | 0% | ⬜ |
| 5 | 工程化（评估 / 可观测 / CI/CD / 部署） | 0% | ⬜ |

详细路线见 [`LEARNING_TRACKER.md`](LEARNING_TRACKER.md)

## 🎯 北极星项目

**📚 学习笔记 Agent（StudyNote Agent）** —— 贯穿全程的主线项目：

一个能读懂本仓库学习资料（日志、知识点库）并回答问题的 Agent。
每学一个阶段，就给它加一块能力：

- **阶段 2 完成**：单 Agent 系统（读文件 + 工具调用 + ReAct 循环）—— 雏形见 [`file_agent.py`](scripts/phase2-agent/file_agent.py)
- **阶段 3 完成**：装上 RAG（用 `logs/` + `KNOWLEDGE_BASE.md` 做语料库，回答"我之前学过什么"）
- **阶段 4 完成**：用 LangGraph 重写 / 提供 MCP Server
- **阶段 5 完成**：FastAPI + Docker 部署成可访问的服务

## 📁 目录结构

```
├── LEARNING_TRACKER.md      # 学习路线 + 进度看板
├── KNOWLEDGE_BASE.md        # 📚 知识点总库（按模块汇总）
├── PITFALLS.md              # 🕳️ 踩坑清单（按类别汇总）
├── requirements.txt         # 依赖清单（分组注释）
├── 每日学习日志.md           # 日志导航
├── logs/                    # 每日详细记录 day-01.md ~ day-05.md
└── scripts/
    ├── phase0-python/       # 阶段 0: Python 基础（8 个练习）
    ├── phase1-llm/          # 阶段 1: LLM 基础（11 个练习）
    ├── phase2-agent/        # 阶段 2: Agent 核心（5 个练习 + STUDYNOTE_EVAL 评估集）
    └── check_progress.py    # 进度检测脚本
```

## 🔴 核心基建文件（Agent 基石）

| 文件 | 作用 |
|------|------|
| [`react_loop.py`](scripts/phase2-agent/react_loop.py) | ReAct 多轮循环 —— Agent 引擎核心 |
| [`tool_calling.py`](scripts/phase2-agent/tool_calling.py) | 工具调用循环（tool_use → execute → tool_result） |
| [`file_agent.py`](scripts/phase2-agent/file_agent.py) | 文件助手 Agent + 状态追踪 + 路径沙箱 |
| [`structured_output.py`](scripts/phase1-llm/structured_output.py) | Pydantic 结构化输出 —— Agent 底座 |
| [`prompt_engineering.py`](scripts/phase1-llm/prompt_engineering.py) | Prompt 三策略 + 格式控制 |
| [`stream_chat.py`](scripts/phase1-llm/stream_chat.py) | SSE 流式输出 |

## 🚀 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置 API Key（复制模板并填入真实 Key）
cp .env.example .env

# 3. 查看学习进度
python scripts/check_progress.py

# 4. 运行练习（LeetCode 模式：函数 + 测试用例，保存即验证）
python scripts/phase2-agent/react_loop.py
```

## 📅 学习日历

| Day | 日期 | 核心内容 |
|-----|------|---------|
| 1 | 2026-07-18 | Python 基础 + Git 入门 |
| 2 | 2026-07-22 | 文件读写 + OOP 入门 |
| 3 | 2026-07-31 | 继承 + dataclass + 第一次 API 调用 |
| 4 | 2026-08-01 | 阶段 1 全部通关（流式 / Prompt / 结构化输出） |
| 5 | 2026-08-09 | Tool Calling + ReAct + 文件助手 Agent |

## 📝 项目规则

- 练习使用 **LeetCode 核心代码模式**：需求注释 + 函数骨架 + 测试用例，禁止 `input()` 交互
- 每个练习文件头部标注 📌 知识点清单（详见各 `.py` 头部注释）
- **阶段通关三件套**：练习全 PASS + 独立挑战题 + 300 字费曼总结
- **复习日**：每 5 个学习日 1 次（核心脚本 + 踩坑 Top 5 + 评估集重测）
- 学习记录联动：看板更新 → 当日日志同步 → 知识点/踩坑入库

> 新对话开场请先读 [`新对话启动提示词.txt`](新对话启动提示词.txt)
