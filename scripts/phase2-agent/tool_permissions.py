# ============================================================
# 练习: 工具权限分级引擎（2.6 第二仗，威胁矩阵第2行的防御）
#
# 给 Agent 的工具注册表装"红绿灯":
#   🟢 green  只读无副作用 -> 自动放行
#   🟡 yellow 可写但可逆   -> 需要 auto_confirm 才放行
#   🔴 red    不可逆/高危  -> 一律拒绝（人工通道，Agent 无权）
#
# 两条铁律:
#   1. 默认拒绝: 没登记风险等级的工具按 red 处理（未知=危险）
#   2. 审计日志记"试图": 被拒的调用也要留痕——那是入侵警报
#
# 你要实现:
#   1. classify_tool(tool_name) -> str
#      查 RISK_TABLE 返回等级；没登记的返回 "red"（默认拒绝）
#
#   2. authorize(tool_name, auto_confirm=False) -> tuple[bool, str]
#      闸门决策:
#      - green            -> (True, "放行")
#      - yellow + auto_confirm  -> (True, "黄级已确认放行")
#      - yellow 无确认    -> (False, "黄级工具需人工确认")
#      - red（含未知）    -> (False, "红级工具禁止Agent调用")
#
#   3. run_tool(tool_name, args, tools, auto_confirm=False) -> str
#      带闸门的执行器（每一步都先过 ②，结果进审计日志）:
#      a. allowed, reason = authorize(...)
#      b. AUDIT_LOG.append((tool_name, allowed))   # 无论成败都留痕
#      c. 不放行 -> return f"❌ {reason}: {tool_name}"
#      d. 放行   -> return str(tools[tool_name](*args))   # 注册表分发+*args（老朋友）
#
# ============================================================
# 知识点: 工具权限分级(绿黄红) | 默认拒绝原则 | 审计日志记试图 | 可逆vs不可逆 | 闸门+执行分离 | 注册表分发复用
# ============================================================

RISK_TABLE = {
    "read_file": "green",
    "list_files": "green",
    "get_time": "green",
    "write_file": "yellow",
    "write_memory": "yellow",
    "delete_file": "red",
    "send_email": "red",
}

AUDIT_LOG: list[tuple[str, bool]] = []  # (工具名, 是否放行)——被拒也要记!


def classify_tool(tool_name: str) -> str:
    """查风险表返回 green/yellow/red；未登记返回 red（默认拒绝）"""
    return RISK_TABLE.get(tool_name, "red")


def authorize(tool_name: str, auto_confirm: bool = False) -> tuple[bool, str]:
    """闸门: green放行 / yellow需确认 / red一律拒"""

    level = classify_tool(tool_name)

    if level == "green":
        return (True, "放行")

    if level == "yellow":
        if auto_confirm:
            return (True, "黄级已确认放行")
        return (False, "黄级工具需人工确认")

    return (False, "红级工具禁止Agent调用")


def run_tool(
    tool_name: str, args: list, tools: dict, auto_confirm: bool = False
) -> str:
    """先过闸门(留审计痕)再执行；拒就带原因返回"""

    allowed, reason = authorize(tool_name, auto_confirm)
    AUDIT_LOG.append((tool_name, allowed))
    if not allowed:
        return f"❌ {reason}: {tool_name}"
    return str(tools[tool_name](*args))


if __name__ == "__main__":
    # ---- 工具注册表（脚手架，已写好）----
    def _read_file(path: str) -> str:
        return f"读取{path}: 你好世界"

    def _write_file(path: str, content: str) -> str:
        return f"写入{path}: {len(content)}字"

    def _delete_file(path: str) -> str:
        return f"删除{path}!"

    tools = {
        "read_file": _read_file,
        "write_file": _write_file,
        "delete_file": _delete_file,
    }

    # 测试1: classify_tool 定级
    print(f"PASS/FAIL 读文件绿 -> {classify_tool('read_file')} | expected: green")
    print(f"PASS/FAIL 写文件黄 -> {classify_tool('write_file')} | expected: yellow")
    print(f"PASS/FAIL 删文件红 -> {classify_tool('delete_file')} | expected: red")
    print(f"PASS/FAIL 未知工具默认红 -> {classify_tool('rmdir')} | expected: red")

    # 测试2: authorize 闸门
    print(f"PASS/FAIL 绿放行 -> {authorize('read_file')} | expected: (True, '放行')")
    print(
        f"PASS/FAIL 黄无确认拦 -> {authorize('write_file')} | expected: (False, '黄级工具需人工确认')"
    )
    print(
        f"PASS/FAIL 黄有确认放 -> {authorize('write_file', auto_confirm=True)} | expected: (True, '黄级已确认放行')"
    )
    print(
        f"PASS/FAIL 红一律拒 -> {authorize('delete_file', auto_confirm=True)} | expected: (False, '红级工具禁止Agent调用')"
    )

    # 测试3: run_tool 全链路
    print(
        f"PASS/FAIL 绿工具执行 -> {run_tool('read_file', ['a.txt'], tools)} | expected: 读取a.txt: 你好世界"
    )
    print(
        f"PASS/FAIL 黄未确认被拦 -> {run_tool('write_file', ['a.txt', '内容'], tools)} | expected: ❌ 黄级工具需人工确认: write_file"
    )
    print(
        f"PASS/FAIL 黄确认后执行 -> {run_tool('write_file', ['a.txt', '内容'], tools, auto_confirm=True)} | expected: 写入a.txt: 2字"
    )
    print(
        f"PASS/FAIL 红确认了也拒 -> {run_tool('delete_file', ['a.txt'], tools, auto_confirm=True)} | expected: ❌ 红级工具禁止Agent调用: delete_file"
    )
    print(
        f"PASS/FAIL 未注册工具拒 -> {run_tool('rmdir', [], tools)} | expected: ❌ 红级工具禁止Agent调用: rmdir"
    )

    # 测试4: 审计日志（含被拒记录）
    print(f"PASS/FAIL 审计共5条 -> {len(AUDIT_LOG)} | expected: 5")
    denied = [t for t, ok in AUDIT_LOG if not ok]
    print(
        f"PASS/FAIL 被拒记录3条 -> {denied} | expected: ['write_file', 'delete_file', 'rmdir']"
    )
