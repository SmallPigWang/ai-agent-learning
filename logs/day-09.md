# Day 9 — 2026-09-06（09:00-14:00 前后）

## 今天学了什么
- **2.6 收官三连**：输出校验+沙箱（output_guard 12/12——SQL出口安检/resolve卸妆/纵深防御）→ 检验问答（5 攻 5 防，口诀：进口过滤、手分级、出口校验、范围圈死、来源审查）→ OWASP LLM Top 10 卡片初读（四大病亲手防过；总根源：LLM 输出=概率猜测不是可信结果）
- **🎯 阶段 2 验收：STUDYNOTE_EVAL 20/20 碾压通过**——北极星 Agent 雏形跑通
- **方向对齐（职业规划）**：转型算法工程师意愿确认（动机双驱动/数学不排斥/硕士/平日有余力——四项全绿），定**双轨制**：主线应用不变 + PML 支线长跑（d2l/Karpathy 备选 → 最终选定 PML 教材主干）
- **音频支线建成**：PML PDF → 章节音频流水线两代（直读版 111 分钟/章 + GLM 讲稿化英文口播版 v3）

## 今天写了什么代码
- `output_guard.py` — 12 行 PASS（validate_sql 出口安检 + safe_path 沙箱 + 组合闸门）
- `studynote_agent.py` — **北极星雏形**：文字版 ReAct 协议（ACTION/OBSERVATION/ANSWER）+ GLM-5.3 + 五件只读工具（list_days/read_day/read_kb/read_tracker/search_notes——最后一件是 RAG 前身）
- `studynote_eval.py` — 评估集执行器（10 题落盘）
- `scripts/paper_audio/make_audio.py` — PDF→章节mp3（TOC 切章/公式清洗/edge-tts/ffmpeg 合并）
- `scripts/paper_audio/make_lecture_audio.py` — GLM 讲稿化版（v3 prompt：直觉先行/例子开口念/路标句/段尾小结）
- 音频产出：PML 第 2 章直读版 111 分钟 + 讲稿试听版 5.3 分钟

## 🏆 今天的高光（值得单独一节）
1. **北极星第一次睁眼**：冒烟测试中 Agent 自己 `read_tracker` → 结构化回答 → **还发现了看板进度条滞后于实际进度**（"实际进展可能比进度条更新"）——它不仅查账，还核账
2. **考卷上的自我纠错**：第 6 题第一次搜索空手，自动换关键词重搜命中——ReAct 循环的容错活了
3. **第 5 题引用的坑能在 PITFALLS 对上号**（#18 属性当方法）——Agent 没有编造，真的读懂了仓库
4. **STUDYNOTE_EVAL 20/20**（通过线 16；考卷原文预期答案"下一目标是2.3"已过期，Agent 答的是当下真相——考卷自己成了被审计对象）

## 今天踩了什么坑
- /tmp 依赖两次蒸发（重启即失）→ 根治：仓库 `.tools/` + 脚本自举（make_audio/studynote_agent/eval 三处补挂）
- GLM 429 限流（与主环境共享配额池）→ 换 coding 专线端点 + 15s 长退避
- eval 脚本漏自举（ModuleNotFoundError 三连环）→ 新规则：**新脚本默认带自举块**
- 骨架/测试不一致第 5 案（检查顺序 vs 期望文案）→ 契约=测试，多语句优先报

## 今天的一个收获
> Agent 的可靠性不是"模型聪明"，是**把每个进出口都设闸**：进口过滤、手分级、出口校验、范围圈死、来源审查——LLM 输出是概率猜测，闸门才是确定性的来源。北极星 20/20 靠的不是 GLM 知得多，是 ReAct 引擎逼它**先查仓库再开口**。

## 📖 OWASP 3 行总结
1. 十大病里我亲手防过四个：prompt注入、输出处理、过度代理、供应链风险。
2. 新面孔最该记住：敏感信息泄露（.env 从 Day 1 就是它的伏笔）。
3. 共同根源：LLM 输出是概率猜测不是可信结果——每个进出口都要设闸。

## 明天计划
- 阶段 3 RAG 开荒：3.1 最简 RAG（50 行版）——给 StudyNote 的 search_notes 升级成语义检索
- 支线：PML 第 2 章讲稿版整章 + 通勤听 sample v3 验收
