# ============================================================
# 🎯 北极星项目: StudyNote 学习笔记 Agent（阶段 2 毕业设计）
#
# 定位: 读懂本仓库 logs/ + KNOWLEDGE_BASE.md，回答学习问题。
# 引擎: 文字版 ReAct——GLM 回 "ACTION: 工具名(参数)" 我们执行并回填
#       OBSERVATION，直到它给 "ANSWER: ..." 或迭代上限。
# 安全: 工具全绿级（只读），路径锚定仓库——2.6 权限分级的工程化。
#
# 工具（复用件，已写好）:
#   list_days()            列出 logs/day-*.md 及标题
#   read_day(n)            读第 n 天日志
#   read_kb()              读 KNOWLEDGE_BASE.md
#   read_tracker()         读 LEARNING_TRACKER.md 的进度/下一目标
#   search_notes(keyword)  跨日志+知识库关键词搜索（阶段 3 RAG 的前身!）
#
# 你要实现（引擎骨架，见下）:
#   call_llm(messages) -> str        调 GLM 拿回复文本
#   parse_action(reply) -> tuple|None 解析 "ACTION: 名(参数)"，无则 None
#   run_agent(question) -> str       ReAct 主循环（填空见骨架内注释）
#
# 运行: python studynote_agent.py "我之前学了什么?"（无参数跑冒烟测试）
# ============================================================
# 知识点: 文字ReAct协议 | ACTION/ANSWER解析 | 对话回填循环 | 工具注册表(全绿级) | search即雏形RAG | 迭代上限防失控
# ============================================================
import os
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent.parent / ".tools" / "audiotools"
if _TOOLS.exists():
    sys.path.insert(0, str(_TOOLS))  # 自举: requests/dotenv 免 PYTHONPATH

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent.parent
API_URL = "https://open.bigmodel.cn/api/coding/paas/v4/chat/completions"
MODEL = "glm-5.3"
MAX_ITERATIONS = 6

SYSTEM_PROMPT = """你是 StudyNote 学习助手，帮助学员回顾这个 AI Agent 学习仓库的内容。
你可以使用以下工具（每次回复只能用一个动作）：

list_days() -> 列出所有学习日及标题
read_day(n) -> 读取第 n 天的学习日志（n 是数字）
read_kb() -> 读取知识库全表（所有已学知识点）
read_tracker() -> 读取学习看板（各阶段进度、下一目标）
search_notes(keyword) -> 跨所有日志和知识库搜索关键词（子串匹配，短词可用）
vector_search(keyword) -> 语义检索全仓库 661 块知识（bge+Chroma，意思相近即可命中——优先用它）

规则：
- 需要资料时，回复格式必须是：ACTION: 工具名(参数)
- 拿到 OBSERVATION 后继续思考，可以继续 ACTION 或给出最终答案
- 资料足够时，回复格式必须是：ANSWER: <用中文回答，要点准确>
- 不要编造仓库里没有的内容；答不上来就说明缺什么资料"""


# ---------- 工具（复用件，已写好，不用动） ----------


def list_days() -> str:
    """列出所有学习日及标题。"""
    days = sorted((ROOT / "logs").glob("day-*.md"))
    lines = []
    for d in days:
        title = d.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ")
        lines.append(f"{d.stem}: {title}")
    return "\n".join(lines) or "(无日志)"


def read_day(n: int) -> str:
    """读取第 n 天的学习日志。"""
    p = ROOT / "logs" / f"day-{int(n):02d}.md"
    return (
        p.read_text(encoding="utf-8") if p.exists() else f"(day-{int(n):02d}.md 不存在)"
    )


def read_kb() -> str:
    """读取知识库全表。"""
    return (ROOT / "KNOWLEDGE_BASE.md").read_text(encoding="utf-8")


def read_tracker() -> str:
    """读取学习看板（只取总览和日历部分，避免超长）。"""
    text = (ROOT / "LEARNING_TRACKER.md").read_text(encoding="utf-8")
    cut = text.find("## 🎯 北极星")
    return text[:cut] if cut > 0 else text[:4000]


def search_notes(keyword: str) -> str:
    """跨日志+知识库搜关键词，返回命中的文件和行。"""
    hits: list[str] = []
    for p in [
        ROOT / "KNOWLEDGE_BASE.md",
        ROOT / "PITFALLS.md",
        *sorted((ROOT / "logs").glob("day-*.md")),
    ]:
        for i, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
            if keyword in line:
                hits.append(f"{p.name}:{i}: {line.strip()[:100]}")
                if len(hits) >= 30:
                    return "\n".join(hits) + "\n(截断，命中过多)"
    return "\n".join(hits) if hits else f"(没有找到含 '{keyword}' 的内容)"


from collections.abc import Callable

TOOLS: dict[str, Callable] = {
    "list_days": list_days,
    "read_day": read_day,
    "read_kb": read_kb,
    "read_tracker": read_tracker,
    "search_notes": search_notes,
}

# ── 压轴换装（3.3）：挂上语义检索武器（需 torch_env：bge+chromadb）──
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "phase3-rag"))
from studynote_rag import vector_search

TOOLS["vector_search"] = vector_search


# ---------- 引擎（你要实现） ----------


def call_llm(messages: list[dict], api_key: str) -> str:
    """调 GLM 返回回复文本（content 字段）"""
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": MODEL,
            "messages": messages,
            "max_tokens": 4096,
            "temperature": 0.3,
        },
        timeout=180,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]


def parse_action(reply: str) -> tuple[str, list] | None:
    """解析 "ACTION: 工具名(参数...)" -> (工具名, [参数表])；没有 ACTION 行返回 None"""
    m = re.search(r"ACTION:\s*(\w+)\(([^)]*)\)", reply)
    if not m:
        return None
    name = m.group(1)
    raw_args = [a.strip().strip("'\"") for a in m.group(2).split(",") if a.strip()]
    args: list = []
    for a in raw_args:
        args.append(int(a) if a.isdigit() else a)  # read_day(2) 的 2 要变 int
    return name, args


def run_agent(question: str, api_key: str) -> str:
    """ReAct 主循环: 问→ACTION→执行→OBSERVATION回填→...→ANSWER"""
    messages: list[dict] = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]

    for _ in range(MAX_ITERATIONS):
        reply = call_llm(messages, api_key)  # ① 问大脑

        action = parse_action(reply)  # ② 解析动作
        if action is None:  #    没有 ACTION → 是答案或违规
            m = re.search(r"ANSWER:\s*(.+)", reply, re.DOTALL)
            return (
                m.group(1).strip()
                if m
                else f"(引擎: 未见 ACTION/ANSWER，原话={reply[:200]})"
            )

        name, args = action
        fn = TOOLS.get(name)  # ③ 注册表查工具
        if fn is None:
            observation = f"(未知工具: {name}，可用: {list(TOOLS)})"
        else:
            observation = str(fn(*args)) if args else str(fn())  # ④ 执行(带参/无参)

        print(f"  🔧 {name}({args}) -> {observation[:80]}...")  # 行动轨迹
        messages.append({"role": "assistant", "content": reply})
        messages.append({"role": "user", "content": f"OBSERVATION: {observation}"})

    return "(引擎: 达到迭代上限，未能给出答案)"


if __name__ == "__main__":
    load_dotenv()
    key = os.getenv("ZHIPU_API_KEY")
    if not key:
        sys.exit("请先在 .env 配置 ZHIPU_API_KEY")

    q = sys.argv[1] if len(sys.argv) > 1 else "我之前一共学了哪几个阶段？现在进度如何？"
    print(f"❓ {q}\n---")
    print(f"\n💬 {run_agent(q, key)}")
