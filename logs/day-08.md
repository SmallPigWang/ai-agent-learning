# Day 8 — 2026-09-05（10:00-22:47，含午休/出门/晚饭）

## 今天学了什么
- **2.4 任务规划与分解 ✅ 封箱**：Plan-and-Execute（计划即数据/安检/注册表分发/*args 调用侧解包）→ 动态重规划（触发信号=降级消息复用、只重算剩余、max_replans 预算）→ 依赖感知执行（拓扑排序朴素版、死锁检测、done 用 set、sorted key=、all()）
- **2.5 Reflection ✅ 封箱**：反思循环（生成→自评→改进，批评家=规则代码）→ 成本效益（三态：白设/赚了/纯亏；按需付费洞察：第1轮=裸奔）→ Reflexion 论文（语言强化学习、episodic memory、三遍阅读法）
- **2.6 安全与护栏（2/5）**：威胁矩阵（5 攻 5 防）→ Prompt 注入靶场（表驱动检测/lower 归一化/过滤 vs 拦截/纵深防御）→ 工具权限分级（绿黄红/默认拒绝/审计记裁决）
- **阅读 ×2**：Building Effective Agents（workflow vs agent/gate/宁简勿繁）+ Reflexion（卡片法）
- **计划外**：知识图谱前端改造（知识点两行折行完整显示）、教练测试翻车现场 4 次（测试也是代码）

## 今天写了什么代码（9 文件 126 项全绿）
- `plan_and_execute.py` — 14 行（P&E 引擎：validate/execute/run_plan）
- `replan_loop.py` — 16 行（重规划引擎 + 注释补全讲解）
- `plan_verify.py` — 4 行（2.4 检验：黑板共享状态 + CWD 坑修复）
- `dep_executor.py` — 12 行（🧩 2.4 挑战：依赖拓扑执行，引导密度最高）
- `reflection_loop.py` — 13 行（反思引擎，问题收敛曲线 [2,1,0]）
- `reflection_cost_benefit.py` — 11 行（开关反思对比实验）
- `episodic_reflection.py` — 12 行（🧩 2.5 带练挑战：跨试次记忆，任务B 3轮→1轮）
- `prompt_injection_lab.py` — 11 行（注入靶场：检测/消毒/劫持模拟/拦截）
- `tool_permissions.py` — 15 行（权限引擎：定级/闸门/审计）

## 今天踩了什么坑（→ PITFALLS #53-56）
- `for pattern in lowered` 遍历字符串=逐字符，任何输入都 True（#53）
- `.find()` 当 `.replace()` 用——返回下标不是新串（#54）
- 整段复制昨天引擎进今天函数，replanner/文案/键名全没适配（#55）
- 语义相近名字串门：审计记 auto_confirm（申报）不记 allowed（裁决）、guard 把活交给 sanitize（#56）
- 教练侧翻车 ×4（字符数/输入词/闭包剧本/前10字）——"测试也是代码，actual≠expected 先数一遍"

## 今天的一个收获
> 变量名是压缩的语义：`auto_confirm` 装着"申请人申报"一整句话，`allowed` 装着"闸门裁决"——名字没解码，逻辑就写串。起不出好名字=没想清楚逻辑。（附：教练补建《高频变量词表》，骨架交付从今起附命名说明）

## 📖 阅读 3 行总结 ×2
**Building Effective Agents**：
1. Workflow 和 Agent 的区别是流程固定 vs 动态流程（下一步听代码的 vs 听 LLM 的）；我的 run_plan 是 workflow，react_loop 是 agent。
2. gate（闸门）对应我的 validate_plan（进门拦计划）和 is_failed（半路拦结果）。
3. 该用 Agent 的标准是任务步骤无法预知、需现场决策；原则是从最简单的方案开始（宁简勿繁）。

**Reflexion**：
1. 语言强化学习 = 不改权重，改文字记忆——不做脑手术，改贴便利贴。
2. Actor/Evaluator/Self-reflection = 我的 generator/check_slogan/build_reflection——我写过它的迷你版。
3. 反思存进 episodic 记忆，能跨试次（任务）存活；我的 note 只在单任务内传递。

## 📝 费曼总结（2.4 + 2.5 双封箱）
**任务规划（2.4）**：Agent 干活两种队形——ReAct 走一步看一步，每轮问 LLM"下一步干嘛"，灵活费钱没全局；Plan-and-Execute 先列完整计划再照单执行，省钱可审计但计划赶不上变化。补救是动态重规划：失败时让重规划师看着"已完成+卡在哪"重算剩余路线，设变道预算防死循环——像导航封路就地改道，不开回出发点。还学了依赖执行：每步声明要等谁，引擎自己排出合法顺序，挑不出就绪就是死锁。

**反思机制（2.5）**：让 Agent 改自己的稿子——生成一稿、批评家（规则代码，免费确定）挑问题清单、问题变便签喂回下一轮，预算到点收工。实验证明三态：稳机器开反思白设、会改的赚（2 次调用买回合格）、改不动的纯亏。所以先问：约束能否写成代码？失败贵不贵？机器改得动吗？Reflexion 论文叫它语言强化学习——不改权重改文字记忆，教训还能跨任务存（我实现的任务B从3轮降到1轮）。

