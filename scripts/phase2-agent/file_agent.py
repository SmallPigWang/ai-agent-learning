# ============================================================
# 练习: 智能文件助手 Agent —— ReAct 循环实战
#
# 给 Agent 装上文件操作的"手": 读文件、写文件、列目录。
# 这是一个真正有用的 Agent —— 可以帮你整理笔记、生成报告。
#
# 你要实现:
#   1. 3 个文件工具: read_file / write_file / list_files
#   2. 状态追踪: AgentState 记录每轮做了什么
#   3. 终止条件: 无工具调用 + 最大轮数 + 连续错误
#   4. file_assistant_loop() — 带状态追踪的 ReAct 循环
# ============================================================
# 知识点: 文件工具三件套 | AgentState dataclass 状态追踪 | _safe_path 路径沙箱 | 多步链式任务
# ============================================================

import json as _json
import os as _os
import sys
from dataclasses import dataclass, field

import requests
from dotenv import load_dotenv

# ---------- 安全沙箱 ----------
WORKSPACE = _os.path.join(_os.path.dirname(__file__), "workspace")
# 自动创建工作目录
_os.makedirs(WORKSPACE, exist_ok=True)


def _safe_path(path: str) -> str:
    """安全路径校验: 所有文件操作限制在 WORKSPACE 内"""
    abs_path = _os.path.abspath(_os.path.join(WORKSPACE, path))
    if not abs_path.startswith(_os.path.abspath(WORKSPACE)):
        raise ValueError(f"非法路径: {path} (不允许访问工作区外文件)")
    return abs_path


# ---------- 待实现：文件操作工具 ----------


def read_file(path: str) -> str:
    """
    读取文件内容
    示例: read_file("notes.txt") → "文件内容..."
    """
    with open(_safe_path(path=path), mode="r") as f:
        return f.read()


def write_file(path: str, content: str) -> str:
    """
    写入文件（覆盖写入）
    示例: write_file("report.md", "# 报告\n...") → "文件已写入: report.md (123 字符)"
    """
    with open(_safe_path(path=path), mode="w", encoding="utf-8") as f:
        f.write(content)

    return f"文件已写入: {path} ({len(content)} 字符)"


def list_files(directory: str = ".") -> str:
    """
    列出目录下所有文件
    示例: list_files(".") → "notes.txt (1.2KB)\nreport.md (456B)"
    """
    safe_dir = _safe_path(directory)
    files = _os.listdir(safe_dir)
    lines = []
    for f in files:
        full_path = _os.path.join(safe_dir, f)
        size = _os.path.getsize(full_path)
        lines.append(f"{f} ({size} B)")
    return "\n".join(lines) if lines else "(空目录)"


# ---------- JSON Schema（参照之前的写法）----------

READ_FILE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "read_file",
        "description": "读取指定文件的内容",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "要读取的文件路径（相对于工作区）",
                }
            },
            "required": ["path"],
        },
    },
}

# TODO: 参照 READ_FILE_SCHEMA 写 WRITE_FILE_SCHEMA 和 LIST_FILES_SCHEMA
WRITE_FILE_SCHEMA = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "写入指定文件的内容",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "要写入的文件路径（相对于工作区）",
                },
                "content": {"type": "string", "description": "要写入的文件内容"},
            },
            "required": ["path", "content"],
        },
    },
}

LIST_FILES_SCHEMA = {
    "type": "function",
    "function": {
        "name": "list_files",
        "description": "列举路径下的所有文件及大小",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {"type": "string", "description": "要进入的文件夹路径"}
            },
            "required": ["directory"],
        },
    },
}


# ---------- 工具调度 ----------

TOOL_MAP = {
    "read_file": read_file,
    "write_file": write_file,
    "list_files": list_files,
}

ALL_TOOLS = [READ_FILE_SCHEMA, WRITE_FILE_SCHEMA, LIST_FILES_SCHEMA]


# ---------- 待实现：Agent 状态追踪 ----------


@dataclass
class AgentState:
    """
    追踪 Agent 每轮执行状态。
    提示: 参照你之前学的 dataclass（day-03 的 employee_system.py）
    """

    # TODO: 定义以下字段
    # messages: list[dict]  — 对话历史
    # iteration: int = 0    — 当前轮数
    # tool_calls_made: list[str] — 已调用的工具名列表（用于调试）
    # consecutive_errors: int = 0 — 连续错误次数
    messages: list[dict] = field(default_factory=list)
    iteration: int = 0
    tool_calls_made: list[str] = field(default_factory=list)
    consecutive_errors: int = 0


# ---------- 待实现：带状态的文件助手循环 ----------


def load_api_key(key_name: str) -> str | None:
    """从 .env 加载指定的 API Key"""
    load_dotenv()
    return _os.getenv(key_name)


def file_assistant_loop(
    prompt: str, tools: list[dict], key: str, max_iterations: int = 10
) -> tuple[str, AgentState]:
    """
    带状态追踪的文件助手 ReAct 循环。
    返回 (最终回答, 执行状态)。

    相比 react_loop 的升级:
      1. 使用 AgentState 记录每轮状态
      2. 工具执行出错时记录错误计数，连续 3 次错误 → 终止
      3. 返回 (回答, 状态) 二元组，方便调试

    """
    URL = "https://api.deepseek.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    state = AgentState(messages=[{"role": "user", "content": prompt}])

    for _ in range(max_iterations):
        state.iteration += 1
        body = {
            "model": "deepseek-chat",
            "messages": state.messages,
            "tools": tools,
        }
        resp = requests.post(url=URL, json=body, headers=headers)
        msg = resp.json()["choices"][0]["message"]

        if "tool_calls" not in msg:
            return (msg["content"], state)

        state.messages.append(msg)
        for tc in msg["tool_calls"]:
            name = tc["function"]["name"]
            args = _json.loads(tc["function"]["arguments"])
            try:
                result = TOOL_MAP[name](**args)
                state.consecutive_errors = 0  # 成功，重置
            except Exception as e:  # noqa: BLE001
                result = f"Error: {e}"
                state.consecutive_errors += 1
                if state.consecutive_errors >= 3:
                    return ("连续 3 次工具调用失败，终止", state)

            state.tool_calls_made.append(name)
            state.messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": result,
                }
            )

    return ("达到最大轮数", state)


# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    all_pass = True
    key = load_api_key("DEEPSEEK_API_KEY")
    if not key or "你的" in key:
        print("请先在 .env 中配置 DEEPSEEK_API_KEY")
        sys.exit(1)

    # ---------- 准备测试文件 ----------
    _os.makedirs(WORKSPACE, exist_ok=True)
    with open(_os.path.join(WORKSPACE, "hello.txt"), "w", encoding="utf-8") as f:
        f.write("Hello World\nThis is a test file.")

    # 测试1: read_file 本身
    r1 = read_file("hello.txt")
    r1_pass = "Hello" in r1
    print(
        f"{'PASS' if r1_pass else 'FAIL'} read_file(hello.txt) -> {r1!r} | expected: 含 Hello"
    )
    all_pass = all_pass and r1_pass

    # 测试2: write_file 本身
    r2 = write_file("test.txt", "Hello")
    r2_pass = "test.txt" in r2
    print(
        f"{'PASS' if r2_pass else 'FAIL'} write_file(test.txt) -> {r2!r} | expected: 含文件名"
    )
    all_pass = all_pass and r2_pass

    # 测试3: list_files 本身
    r3 = list_files(".")
    r3_pass = "test.txt" in r3 and "hello.txt" in r3
    print(
        f"{'PASS' if r3_pass else 'FAIL'} list_files(.) -> {r3!r} | expected: 含 test.txt + hello.txt"
    )
    all_pass = all_pass and r3_pass

    # 测试4: Agent 读取文件
    r4, s4 = file_assistant_loop(
        "帮我读一下 hello.txt 的内容，然后告诉我里面写了什么", ALL_TOOLS, key
    )
    r4_pass = "Hello" in r4
    print(
        f"{'PASS' if r4_pass else 'FAIL'} Agent(读文件) -> {r4[:80]!r}... | expected: 含文件内容"
    )
    print(f"     状态: 迭代 {s4.iteration} 轮, 调用工具 {s4.tool_calls_made}")
    all_pass = all_pass and r4_pass

    # 测试5: Agent 写文件
    r5, s5 = file_assistant_loop(
        "帮我创建一个文件 summary.txt，内容是: 今天学习ReAct循环，理解了多轮推理。",
        ALL_TOOLS,
        key,
    )
    r5_pass = "summary.txt" in r5 and _os.path.exists(
        _os.path.join(WORKSPACE, "summary.txt")
    )
    print(
        f"{'PASS' if r5_pass else 'FAIL'} Agent(写文件) -> {r5[:80]!r}... | expected: 文件创建成功"
    )
    print(f"     状态: 迭代 {s5.iteration} 轮, 调用工具 {s5.tool_calls_made}")
    all_pass = all_pass and r5_pass

    # 测试6: Agent 多步任务 — 列出文件 → 读取 → 总结
    r6, s6 = file_assistant_loop(
        "先列出当前目录有哪些文件，然后读取 hello.txt，最后把它的内容转成大写写进 hello_upper.txt",
        ALL_TOOLS,
        key,
    )
    r6_pass = _os.path.exists(_os.path.join(WORKSPACE, "hello_upper.txt"))
    print(
        f"{'PASS' if r6_pass else 'FAIL'} Agent(多步文件操作) -> {r6[:80]!r}... | expected: hello_upper.txt 存在"
    )
    print(f"     状态: 迭代 {s6.iteration} 轮, 调用工具 {s6.tool_calls_made}")
    all_pass = all_pass and r6_pass

    # 清理测试文件
    for f in ["test.txt", "summary.txt", "hello_upper.txt"]:
        p = _os.path.join(WORKSPACE, f)
        if _os.path.exists(p):
            _os.remove(p)

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
