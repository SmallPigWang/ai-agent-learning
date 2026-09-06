# Day 9 — 2026-09-06（08:45-14:39）

## 今天学了什么（半天封五箱，史诗级）
- **2.6 收官**：输出校验+沙箱（output_guard 11/11）→ 5攻5防检验 → OWASP LLM Top 10
- **🎯 阶段 2 验收**：StudyNote Agent（文字ReAct + GLM-5.3 + 五工具）**STUDYNOTE_EVAL 20/20 碾压通过**
- **3.1 RAG 原理**：mini_rag 11/11（hash embedding/cosine/Top-K/亿级语义）；hash 撞车案 #57（64→256）
- **3.2 分块策略**：chunking_lab 8/8（固定/按行/窗口对比实验：行切=纯块）；RAG 论文 + LangChain 卡片
- **3.3 Embedding ×3 连击**：对比擂台（hash 60% vs **bge 100%**，#58 写死回调案）→ Chroma 搭库（双引擎 5/5 打平）→ **压轴 StudyNote 向量记忆**（661 块真实语料入库 + 终极对决：子串扑空 vs 语义一击命中）
- **职业方向**：算法转型确认（动机双驱动/数学可捡/硕士/平日有余力=四项全绿）→ **双轨制**：主线应用 + PML 理论长跑
- **音频支线**：PML PDF → 章节 mp3 流水线两代（直读 111min/章 + GLM 讲稿化英文口播 v3）

## 今天写了什么代码（9 个 .py + 2 配置，全部归档）
- `studynote_agent.py` + `studynote_eval.py` — 北极星雏形 + 考卷执行器（EVAL 20/20）
- `output_guard.py` — 11/11（2.6 收官：SQL出口安检+路径沙箱）
- `mini_rag.py` — 11/11（hash embedding → 语义检索全套）
- `chunking_lab.py` — 8/8（三刀法对比实验 + tag_source 户口）
- `embedding_bakeoff.py` — 3/3（hit rate 评估 + bge vs hash 100% vs 60%）
- `chroma_lab.py` — 8/8（Chroma 编目 + 双引擎打平）
- `studynote_rag.py` — 压轴（load_corpus 661 块 / build_index 四件套 / vector_search 懒加载单例+官方前缀）
- `make_audio.py` / `make_lecture_audio.py` — 音频流水线（.tools 自举根治）
- `pyrightconfig.json` / `mypy.ini` — 跨目录 import 静态解析白名单

## 今天踩了什么坑（#58-60 入册）
- #58 检索器里查询向量写死 hash_embed——单选手隐身，bge 上场现形（zip 静默截断）
- #59 bge 出厂设置：检索查询必须带"为这个句子生成表示以用于检索相关文章："前缀
- #60 跨目录 sys.path import：运行时 OK、Pylance/mypy 看不见——pyrightconfig/mypy_path 白名单
- 常规续集：/tmp 蒸发×2→.tools 自举根治；429 限流→coding 端点+长退避；编辑器缓冲区覆盖×4-5；测试 expected 手滑×N（教练第 5-7 案）；`studynotes` vs `studynote` 撕错册名

## 今天的一个收获
> 回调注入不只是复用技巧——今天它客串了缺陷检测仪：写死 hash_embed 的 retrieve 在单一选手下隐身，第二位选手（bge）一上场就把它炸出来。#58 是"对照组实验隐藏价值"的完美教材。

## 📝 费曼总结（3.x 双模块 + 北极星换芯）
**RAG 是什么（3.1-3.3）**：LLM 的知识在权重里，凝固又爱编。RAG 让它在回答前"开卷考试"——把文档切成块（3.2 发现我的仓库每行表格就是天然块）、每块算成向量（3.3 用 bge 把"宕机"和"死机"放进同一片语义区）、建索引编目、提问时只算问题向量查目录取最像的几块，拼进提示词作答。我亲手证明了：换真 embedding 命中率 60%→100%，差距全在"字面不同意思相同"的陷阱题；工业件 Chroma 和我手写版 5/5 打平，证明手搓出了正确缩影。最后给北极星换芯：661 块真实知识入库，子串武器扑空的同义句，语义武器一击命中。

## 明天计划
- EVAL 复测（coding plan 配额恢复后）：北极星 RAG 版双指标——20/20 保持？工具调用 15 次下降？
- 3.3 收尾 → 3.4 检索策略进阶 / 3.5 Agentic RAG
- PML 支线第 2 章音频通勤听 + 音频批量（第 2-6 章待 verdict）
