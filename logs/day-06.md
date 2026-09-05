# Day 6 — 2026-08-16（复习 + 2.3 记忆系统）

## 今天学了什么
- 复习日：回顾 Day 1-5 核心知识，跑本地核心脚本，扫 PITFALLS Top 5
- 2.3 记忆系统（上）：
  - 三种记忆分工概念：短期 / 长期 / 工作（初步了解）
  - 滑动窗口：只保留 system + 最近 N 轮，旧消息丢弃
  - 摘要压缩：旧消息压成摘要，保留要点；摘要可合并进 system
  - 混合策略：旧对话用摘要，新对话用窗口
- 更新 CLAUDE.md：加入“卡壳时用填空式引导”，并把负面描述改成正向描述

## 今天写了什么代码
- `sliding_window_memory.py` — 滑动窗口记忆（trim_history / add_turn / estimate_tokens），9/9 PASS
- `summary_compression_memory.py` — 摘要压缩记忆（summarize_old_messages / compress_memory / build_context），15/15 PASS

## 今天踩了什么坑
- dict 和 list 不能直接相加：`merged + recent_messages[1:]` 报错，要用 `[merged] + ...`
- 切片边界算错：窗口保留数应是 `len(rest) - keep_count`，不是 `keep_count` 或 `keep_count+1`
- 没有旧消息时摘要应返回空字符串 `""`，不是 `None`
- 新建 system 消息时 role 固定为 `"system"`，不能写成列表变量

## 今天的一个收获
- 记忆不是“只有一种”：滑动窗口省空间但丢细节，摘要压缩保留要点但可能失真，实际 Agent 常把两者混合使用。

