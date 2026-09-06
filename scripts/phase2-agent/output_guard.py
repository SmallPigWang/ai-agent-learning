# ============================================================
# 练习: 输出校验 + 沙箱隔离（2.6 第三仗，收官练习）
#
# 场景: Agent 替用户生成 SQL 并保存报告文件。两道出口防线:
#   输出校验: SQL 必须只读(SELECT)、单语句、无破坏词 —— 才许"执行"
#   路径沙箱: 保存路径必须落在允许目录内，../ 逃逸一律拒绝
#
# 你要实现:
#   1. validate_sql(sql) -> tuple[bool, str]
#      SQL 出口安检:
#      - 必须 SELECT 开头（不区分大小写，左边去空格）
#      - 整条里出现任一破坏词 -> (False, "含禁止关键词: {词}")
#        破坏词表: DROP / DELETE / INSERT / UPDATE / TRUNCATE
#        （关键词判断也不区分大小写）
#      - 含分号 ; （多语句注入）-> (False, "禁止多语句")
#      - 全过 -> (True, "只读SQL放行")
#
#   2. safe_path(path, allowed_root) -> str | None
#      路径沙箱:
#      - p = Path(path).resolve()          # 规范化：../ 全部展开
#      - root = Path(allowed_root).resolve()
#      - p 在 root 内部（用 p.is_relative_to(root)，送的）-> 返回 str(p)
#      - 逃逸 -> 返回 None
#
#   3. execute_report(sql, save_path, allowed_root) -> str
#      组合闸门（两道防线都要过）:
#      a. validate_sql 不过 -> return f"❌ SQL被拦: {原因}"
#      b. safe_path 返回 None -> return f"❌ 路径越狱: {save_path}"
#      c. 都过 -> return f"✅ 已执行并保存到 {规范化路径}"
#
# ============================================================
# 知识点: 输出校验(出口安检) | SQL注入面(多语句/破坏词) | 路径沙箱 | resolve规范化 | is_relative_to | 双防线纵深防御 | 安检闸门二次转正
# ============================================================
from pathlib import Path

DANGEROUS = ["DROP", "DELETE", "INSERT", "UPDATE", "TRUNCATE"]


def validate_sql(sql: str) -> tuple[bool, str]:
    """SQL 出口安检: 只读 SELECT、单语句、无破坏词"""
    lowered = sql.lower()
    if ";" in sql:
        return False, "禁止多语句"
    for word in DANGEROUS:
        if word.lower() in lowered:
            return False, f"含禁止关键词: {word}"

    if not lowered.lstrip().startswith("select"):
        return False, "只允许SELECT查询"

    return True, "只读SQL放行"


def safe_path(path: str, allowed_root: str) -> str | None:
    """路径沙箱: 规范化后在允许目录内 -> 绝对路径；逃逸 -> None"""
    p = Path(path).resolve()
    root = Path(allowed_root).resolve()
    if p.is_relative_to(root):
        return str(p)
    return None


def execute_report(sql: str, save_path: str, allowed_root: str) -> str:
    """组合闸门: SQL 校验 + 路径沙箱，双过才放行"""
    allowed, reason = validate_sql(sql)
    if not allowed:
        return f"❌ SQL被拦: {reason}"
    real_path = safe_path(save_path, allowed_root)
    if real_path is None:
        return f"❌ 路径越狱: {save_path}"
    return f"✅ 已执行并保存到 {real_path}"


if __name__ == "__main__":
    import os
    import tempfile

    # 沙箱根目录（用临时目录当"允许区"）
    root = tempfile.mkdtemp(prefix="sandbox_")

    # 测试1: validate_sql 出口安检
    print(
        f"PASS/FAIL 只读放行 -> {validate_sql('SELECT * FROM users')} | expected: (True, '只读SQL放行')"
    )
    print(
        f"PASS/FAIL 小写select也放 -> {validate_sql('select name from t')} | expected: (True, '只读SQL放行')"
    )
    print(
        f"PASS/FAIL 破坏词拦截 -> {validate_sql('SELECT * FROM users; DROP TABLE users')} | expected: (False, '禁止多语句')"
    )
    print(
        f"PASS/FAIL DROP裸奔拦截 -> {validate_sql('DROP TABLE users')} | expected: (False, '含禁止关键词: DROP')"
    )
    print(
        f"PASS/FAIL 藏在中间也拦 -> {validate_sql('SELECT * FROM t WHERE x=1 AND DELETE')} | expected: (False, '含禁止关键词: DELETE')"
    )

    # 测试2: safe_path 路径沙箱
    ok_path = os.path.join(root, "reports", "a.txt")
    p1 = safe_path(ok_path, root)
    print(
        f"PASS/FAIL 区内放行 -> {p1 is not None and p1.startswith(root)} | expected: True"
    )
    print(
        f"PASS/FAIL 相对逃逸拦截 -> {safe_path(os.path.join(root, '..', 'etc', 'passwd'), root)} | expected: None"
    )
    print(
        f"PASS/FAIL 嵌套逃逸拦截 -> {safe_path(os.path.join(root, 'reports', '..', '..', 'secret'), root)} | expected: None"
    )
    p2 = safe_path(os.path.join(root, "sub", "b.txt"), root)
    print(f"PASS/FAIL 子目录放行 -> {p2 is not None} | expected: True")

    # 测试3: execute_report 组合闸门
    print(
        f"PASS/FAIL 双过放行 -> {execute_report('SELECT 1', os.path.join(root, 'r.txt'), root)} | expected: ✅ 开头"
    )
    print(
        f"PASS/FAIL 坏SQL拦截 -> {execute_report('DELETE FROM t', os.path.join(root, 'r.txt'), root)} | expected: ❌ SQL被拦"
    )
    print(
        f"PASS/FAIL 越狱路径拦截 -> {execute_report('SELECT 1', os.path.join(root, '..', 'x.txt'), root)} | expected: ❌ 路径越狱"
    )
