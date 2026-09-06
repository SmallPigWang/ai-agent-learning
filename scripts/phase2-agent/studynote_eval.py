# ============================================================
# 📊 STUDYNOTE_EVAL 评估集执行器（阶段 2 验收）
# 逐题拷问 StudyNote Agent，回答落盘待人工按 0/1/2 打分。
# 运行: python studynote_eval.py   (需 .env 的 ZHIPU_API_KEY)
# ============================================================
import os
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent.parent / ".tools" / "audiotools"
if _TOOLS.exists():
    sys.path.insert(0, str(_TOOLS))  # 自举: dotenv 免 PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent))

from dotenv import load_dotenv  # noqa: E402

from studynote_agent import run_agent  # noqa: E402

QUESTIONS = [
    "我之前一共学了哪几个阶段？进度如何？",
    "ReAct 循环是什么？和普通 tool_loop 有什么区别？",
    "Messages API 有哪四种角色？",
    "流式输出的关键是什么？",
    "我在 Day 2 踩过哪些坑？举两个",
    "什么是安检闸门校验模式？",
    "Prompt 的三种策略是什么？",
    "Pydantic 在 Agent 开发里起什么作用？",
    "@dataclass 解决了什么问题？",
    "我的下一个学习目标是什么？",
]

if __name__ == "__main__":
    load_dotenv()
    key = os.getenv("ZHIPU_API_KEY")
    if not key:
        sys.exit("请先在 .env 配置 ZHIPU_API_KEY")

    out = Path(__file__).parent.parent.parent / "audio_out"
    out.mkdir(exist_ok=True)
    report = out / "studynote_eval_answers.md"
    lines = ["# STUDYNOTE_EVAL 回答记录\n"]
    for i, q in enumerate(QUESTIONS, 1):
        print(f"\n===== 第{i}题: {q} =====", flush=True)
        ans = run_agent(q, key)
        print(f"💬 {ans[:120]}...", flush=True)
        lines.append(f"## 第{i}题: {q}\n\n**回答**:\n{ans}\n")
        report.write_text("\n".join(lines), encoding="utf-8")  # 每题落盘防中途失败
    print(f"\n✅ 全部落盘 -> {report}")
