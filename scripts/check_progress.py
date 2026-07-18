"""
学习进度检测脚本
运行方式: python scripts/check_progress.py
"""
import re
from pathlib import Path
from datetime import datetime, date

TRACKER = Path(__file__).parent.parent / "LEARNING_TRACKER.md"


def count_checkboxes(text: str) -> tuple[int, int]:
    """统计已完成和总计 checkbox"""
    all_items = re.findall(r'- \[[ xX]\]', text)
    done = len([x for x in all_items if x.strip() in ('- [x]', '- [X]')])
    return done, len(all_items)


def count_modules(text: str) -> tuple[int, int]:
    """统计各阶段的模块完成情况"""
    # 找到每个 ### 开头的模块
    modules = re.findall(r'### \d+\.\d+ .+?\n((?:.*?\n)*?)(?=###|\Z)', text)
    done_modules = 0
    for mod in modules:
        done, total = count_checkboxes(mod)
        if total > 0 and done == total:
            done_modules += 1
    return done_modules, len(modules)


def progress_bar(done: int, total: int, width: int = 20) -> str:
    """生成进度条"""
    if total == 0:
        return "[░░░░░░░░░░░░░░░░░░░░] 0%"
    pct = done / total
    filled = int(width * pct)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {pct:.0%}"


def main():
    if not TRACKER.exists():
        print("❌ 找不到 LEARNING_TRACKER.md，请先运行学习路线初始化")
        return

    text = TRACKER.read_text(encoding="utf-8")

    # 统计各阶段
    phases = {
        "阶段 0: 编程起步": r"## 🏁 阶段 0",
        "阶段 1: LLM 基础": r"## 🤖 阶段 1",
        "阶段 2: Agent 核心": r"## 🧠 阶段 2",
        "阶段 3: RAG 专题": r"## 📚 阶段 3",
        "阶段 4: 框架实战": r"## 🔧 阶段 4",
        "阶段 5: 工程化": r"## 🚀 阶段 5",
    }

    phase_done = {}
    phase_total = {}

    for name, marker in phases.items():
        match = re.search(marker, text)
        if match:
            # 提取从标记到下一阶段的内容
            start = match.start()
            next_marker = re.search(r'## (🏁|🤖|🧠|📚|🔧|🚀|🏆|📈)', text[start + len(marker):])
            if next_marker:
                end = start + len(marker) + next_marker.start()
            else:
                end = len(text)
            phase_text = text[start:end]
            done, total = count_checkboxes(phase_text)
            phase_done[name] = done
            phase_total[name] = total

    total_done = sum(phase_done.values())
    total_all = sum(phase_total.values())

    # 计算学习天数
    start_match = re.search(r'开始日期\*\*: (\d{4}-\d{2}-\d{2})', text)
    days = 0
    if start_match:
        start_date = date.fromisoformat(start_match.group(1))
        days = (date.today() - start_date).days + 1

    # 计算预估完成时间
    if total_done > 0 and days > 0:
        items_per_day = total_done / days
        remaining = total_all - total_done
        if items_per_day > 0:
            est_days = remaining / items_per_day
        else:
            est_days = float('inf')
    else:
        est_days = None

    print("=" * 60)
    print("   🎓 AI Agent 学习进度报告")
    print(f"   📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"   📆 已学习 {days} 天")
    print("=" * 60)

    for name in phase_done:
        bar = progress_bar(phase_done[name], phase_total[name])
        print(f"  {name:<20} {bar}  ({phase_done[name]}/{phase_total[name]})")

    print("-" * 60)
    total_bar = progress_bar(total_done, total_all)
    print(f"  {'🎯 总进度':<20} {total_bar}  ({total_done}/{total_all})")

    if est_days and est_days != float('inf'):
        print(f"\n  ⏱️  按当前速度，预计还需 {est_days:.0f} 天完成全部阶段")
    elif total_done == 0:
        print(f"\n  💡 还没有开始标记完成项。今天就开始第一个模块吧！")

    # 下一步建议
    for name in phase_done:
        if phase_total[name] > 0 and phase_done[name] < phase_total[name]:
            print(f"\n  👉 下一步: {name} 还有 {phase_total[name] - phase_done[name]} 项待完成")
            break

    # 鼓励
    if total_done == 0:
        print("\n  🌟 万事开头难，从 阶段 0.1 第一个 checkbox 开始吧！")
    elif total_done < 10:
        print("\n  🌱 好的开始是成功的一半，继续保持节奏！")
    elif total_done < 30:
        print("\n  🚀 势头不错，你正在稳步构建 Agent 开发能力！")
    else:
        print("\n  🔥 太强了，你离成为一个 Agent 工程师越来越近了！")

    print("=" * 60)


if __name__ == "__main__":
    main()
