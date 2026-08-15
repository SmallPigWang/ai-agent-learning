# -*- coding: utf-8 -*-
"""知识图谱生成器 —— 力导向图形式：核心知识点节点 + 直接关联。

数据源（只读，不修改）:
  - KNOWLEDGE_BASE.md    阶段 / 子模块 / 知识点表格
  - PITFALLS.md          踩坑清单表格
  - LEARNING_TRACKER.md  阶段进度百分比

输出:
  - knowledge-graph/data.js   window.KB_DATA

图结构:
  - nodes   阶段枢纽 / 模块枢纽 / 知识点节点（核心内容）/ 待补充（虚线）
  - edges   contain(归属聚类) + path(学习顺序) + related(知识点直接关联,带关键词) + planned
  - 前端用力导向布局：同一模块的知识点自然聚成一簇，直接关联跨簇连线

用法:
  python scripts/knowledge-graph/gen_knowledge_graph.py

# 知识点: 文件解析 | 正则表达式 | 关键词抽取 | 关联打分 | 图建模 | 静态站点生成
"""

import json
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "knowledge-graph" / "data.js"

ID_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
VER_RE = re.compile(r"\d+\.\d+")
CJK_RE = re.compile(r"[\u4e00-\u9fff]+")

STOP = {
    "the", "and", "for", "with", "from", "that", "this", "you", "are", "not",
    "def", "import", "your", "can", "how", "use", "get", "set", "all", "our",
}


def tokenize(text, weight=1.0, cjk_weight=0.35):
    out = defaultdict(float)
    for m in ID_RE.finditer(text):
        w = m.group(0).lower()
        if len(w) >= 3 and w not in STOP:
            out[w] += 1.3 * weight
    for m in VER_RE.finditer(text):
        out[m.group(0)] += 1.0 * weight
    for m in CJK_RE.finditer(text):
        run = m.group(0)
        for i in range(len(run) - 1):
            out["c:" + run[i : i + 2]] += cjk_weight * weight
    return out


def add_tokens(dst, src):
    for t, v in src.items():
        dst[t] = dst.get(t, 0) + v


def overlap(a, b):
    return sum(min(a[t], b[t]) for t in set(a) & set(b))


def guess_planned_code(item):
    m = re.match(r"^阶段\s*(\d+)", item)
    if m:
        return {"stage": m.group(1)}
    m = re.match(r"^(\d+\.\d+)", item)
    if m:
        return {"module": m.group(1)}
    return {}


def prettify(tok):
    if tok.startswith("c:"):
        return tok[2:]
    return tok[:14]


# ---------- 解析 KNOWLEDGE_BASE.md ----------

def parse_kb(text):
    stages, modules, knowledge, planned = [], [], [], []
    stage, module, in_pending, header_seen = None, None, False, False
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            title = line[3:].strip()
            in_pending = "待补充" in title
            stage = module = None
            header_seen = False
            if in_pending:
                continue
            m = re.match(r"^(\d+)\.\s*(.+)$", title)
            if m:
                stage = {"code": m.group(1), "name": title, "modules": []}
                stages.append(stage)
            continue
        if line.startswith("### "):
            header_seen = False
            if in_pending:
                continue
            m = re.match(r"^(\d+\.\d+)\s+(.+)$", line[4:].strip())
            if m and stage is not None:
                module = {"code": m.group(1), "name": m.group(2),
                          "stage": stage["code"], "knowledge": []}
                stage["modules"].append(module)
                modules.append(module)
            continue
        if in_pending and line.startswith("- "):
            planned.append({"text": line[2:].strip(), "code": guess_planned_code(line[2:].strip())})
            continue
        if line.startswith("|") and line.endswith("|"):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if module is None or not cells:
                continue
            if not header_seen:
                header_seen = "知识点" in cells[0]
                continue
            if len(cells) == 2 and cells[0] and cells[1] and set(cells[0]) != {"-"}:
                k = {"name": cells[0], "desc": cells[1],
                     "module": module["code"], "stage": stage["code"],
                     "pitfalls": []}
                module["knowledge"].append(k)
                knowledge.append(k)
    return stages, modules, knowledge, planned


# ---------- 解析 PITFALLS.md ----------

def parse_pitfalls(text):
    pitfalls, category = [], None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("## "):
            title = line[3:].strip()
            category = title if re.match(r"^\d+\.", title) else None
            continue
        if line.startswith("|") and category is not None:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) != 4 or not re.match(r"^\d+$", cells[0]):
                continue
            pitfalls.append({"num": int(cells[0]), "category": category,
                             "err": cells[1], "why": cells[2], "fix": cells[3]})
    return pitfalls


# ---------- 解析 LEARNING_TRACKER.md 的阶段进度 ----------

def parse_progress(text):
    out = {}
    for m in re.finditer(r"阶段\s*(\d+)\s*:\s*(.+?)\[.*?\]\s*(\d+)%", text):
        out[m.group(1)] = int(m.group(3))
    return out


# ---------- 解析 logs/day-XX.md ----------

def parse_days(logs_dir):
    days = []
    for f in sorted(logs_dir.glob("day-*.md")):
        m = re.match(r"day-(\d+)\.md$", f.name)
        if not m:
            continue
        text = f.read_text(encoding="utf-8")
        first = next((l for l in text.splitlines() if l.strip().startswith("# ")), "")
        dm = re.search(r"(\d{4}-\d{2}-\d{2})", first)
        title = re.sub(r"^#\s*Day\s*\d+\s*[—\-–]*\s*", "", first).strip()
        title = title.strip("（）() ")
        days.append({"num": int(m.group(1)), "date": dm.group(1) if dm else "",
                     "title": title, "text": text})
    return days


def parse_checked(text):
    """LEARNING_TRACKER 中每个模块的已勾选行文本: {'0.1': '变量 数据类型 ...'}"""
    out = defaultdict(str)
    cur = None
    for raw in text.splitlines():
        line = raw.strip()
        m = re.match(r"^###\s*(\d+\.\d+)", line)
        if m:
            cur = m.group(1)
            continue
        if line.startswith("## "):
            cur = None
            continue
        if cur is not None and line.startswith("- [x]"):
            out[cur] += " " + line[5:].strip()
    return out


def name_variants(name):
    """拆出知识点名称的匹配变体：核心名 / 去虚词名 / 标识符 / 中文四字组 / 数字字母串"""
    full = name.replace("`", "")
    core = re.sub(r"[（(].*?[)）]", "", full).strip()
    compact = re.sub(r"[的了与和及、\s]", "", core)
    ids = [t.lower() for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", full) if len(t) >= 3]
    grams = [full[i : i + 4] for i in range(len(full) - 3)] if len(full) >= 4 else []
    nums = [t.lower() for t in re.findall(r"\d+[A-Za-z]+\d*", full)]
    return core.lower(), compact.lower(), ids, grams, nums


def match_name(core, compact, ids, grams, nums, text):
    """名称是否出现在某段文本中：
    核心名（≥3 字，或 2 字纯中文） / 去虚词名（≥4 字） / 全部标识符 / 任一四字组 / 数字字母串
    """
    if core and (len(core) >= 3 or (len(core) == 2 and re.search(r"[\u4e00-\u9fff]", core))) and core in text:
        return True
    if compact and len(compact) >= 4 and compact in text:
        return True
    if ids and all(i in text for i in ids):
        return True
    if grams and any(g in text for g in grams):
        return True
    if nums and any(n in text for n in nums):
        return True
    return False


def desc_hits(desc, text):
    """说明中的长标识符（≥5 字符）出现在文本中 → 视为学过"""
    for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]*", desc):
        if len(t) >= 5 and t.lower() in text:
            return True
    return False


def kid(k):
    return "k:%s:%s" % (k["module"], k["name"])


# ---------- 组装图 ----------

def build():
    kb = (ROOT / "KNOWLEDGE_BASE.md").read_text(encoding="utf-8")
    pf = (ROOT / "PITFALLS.md").read_text(encoding="utf-8")
    tr = (ROOT / "LEARNING_TRACKER.md").read_text(encoding="utf-8")
    stages, modules, knowledge, planned = parse_kb(kb)
    pitfalls = parse_pitfalls(pf)
    progress = parse_progress(tr)
    days = parse_days(ROOT / "logs")
    log_all = " ".join(d["text"].lower() for d in days)
    checked = parse_checked(tr)

    # 知识点关键词（名称 ×2，说明 ×1）
    ktok = {}
    for k in knowledge:
        t = tokenize(k["name"], weight=2.0)
        add_tokens(t, tokenize(k["desc"], weight=1.0))
        ktok[k["name"]] = t

    # 知识点直接关联（跨模块 ≥1.9；同模块 ≥3.4；每节点最多 4 条）
    rel_candidates = []
    for i in range(len(knowledge)):
        for j in range(i + 1, len(knowledge)):
            a, b = knowledge[i], knowledge[j]
            score = overlap(ktok[a["name"]], ktok[b["name"]])
            thresh = 3.4 if a["module"] == b["module"] else 1.9
            if score >= thresh:
                rel_candidates.append((score, a, b))
    rel_candidates.sort(key=lambda x: -x[0])
    rel_deg = defaultdict(int)
    related = []
    for score, a, b in rel_candidates:
        if rel_deg[a["name"]] >= 4 or rel_deg[b["name"]] >= 4:
            continue
        rel_deg[a["name"]] += 1
        rel_deg[b["name"]] += 1
        shared = set(ktok[a["name"]]) & set(ktok[b["name"]])
        label = ""
        if shared:
            label = prettify(max(shared, key=lambda t: min(ktok[a["name"]][t], ktok[b["name"]][t])))
        related.append({"source": kid(a), "target": kid(b), "label": label})

    # 踩坑 -> 知识点 归属
    ptok = {}
    for p in pitfalls:
        t = tokenize(p["err"], weight=1.5)
        add_tokens(t, tokenize(p["why"] + " " + p["fix"], weight=1.0))
        ptok[p["num"]] = t
    for p in pitfalls:
        hits = []
        for k in knowledge:
            score = overlap(ptok[p["num"]], ktok[k["name"]])
            if score >= 1.6:
                hits.append((score, k))
        hits.sort(key=lambda x: -x[0])
        for score, k in hits[:2]:
            k["pitfalls"].append({"num": p["num"], "err": p["err"], "fix": p["fix"]})

    # 已学状态：知识点名称出现在学习日志 或 该模块的已勾选行中
    dtok = {}
    for d in days:
        dtok[d["num"]] = tokenize(d["text"], weight=1.0)
    for k in knowledge:
        core, compact, ids, grams, nums = name_variants(k["name"])
        k["learned"] = (
            match_name(core, compact, ids, grams, nums, log_all)
            or match_name(core, compact, ids, grams, nums, checked[k["module"]].lower())
            or desc_hits(k["desc"], log_all)
        )
        # 学习日关联：日志与知识点关键词共现，最多 3 天
        hits = []
        for d in days:
            score = overlap(dtok[d["num"]], ktok[k["name"]])
            if score >= 2.5:
                hits.append((score, d["num"]))
        hits.sort(key=lambda x: -x[0])
        k["days"] = [n for score, n in hits[:3]]

    # 待补充
    stage_codes = {s["code"] for s in stages}
    out_planned = []
    for i, pl in enumerate(planned):
        sc = pl["code"].get("stage") or (pl["code"].get("module", "")[:1])
        out_planned.append({
            "id": "x:%d" % i, "name": pl["text"],
            "stage": sc if sc in stage_codes else None,
        })

    # 学习主线顺序：阶段 → 模块 → 知识点，规划项接在所属阶段之后
    path = []
    for s in stages:
        for m in s["modules"]:
            for k in m["knowledge"]:
                path.append(kid(k))
        for pl in out_planned:
            if pl["stage"] == s["code"]:
                path.append(pl["id"])
    for pl in out_planned:
        if pl["stage"] is None:
            path.append(pl["id"])

    # ---- 节点 ----
    nodes = []
    for s in stages:
        nodes.append({"id": "s:" + s["code"], "type": "stage", "name": s["name"],
                      "code": s["code"], "progress": progress.get(s["code"])})
    for m in modules:
        nodes.append({"id": "m:" + m["code"], "type": "module",
                      "name": m["code"] + " " + m["name"],
                      "code": m["code"], "stage": m["stage"]})
    for k in knowledge:
        nodes.append({"id": kid(k), "type": "knowledge", "name": k["name"],
                      "desc": k["desc"], "module": k["module"], "stage": k["stage"],
                      "pitfalls": k["pitfalls"], "learned": k["learned"], "days": k["days"]})
    for pl in out_planned:
        nodes.append({"id": pl["id"], "type": "planned", "name": pl["name"],
                      "stage": pl["stage"]})

    # ---- 边 ----
    edges = []
    edge_seen = set()

    def edge(s, t, e):
        key = (s, t, e)
        if key not in edge_seen:
            edge_seen.add(key)
            edges.append({"source": s, "target": t, "type": e})

    for s in stages:
        for m in s["modules"]:
            edge("s:" + s["code"], "m:" + m["code"], "contain")
    for m in modules:
        for k in m["knowledge"]:
            edge("m:" + m["code"], kid(k), "contain")
    for i in range(len(path) - 1):
        edge(path[i], path[i + 1], "path")
    for e in related:
        edge(e["source"], e["target"], "related")
    for pl in out_planned:
        if pl["stage"] in stage_codes:
            edge("s:" + pl["stage"], pl["id"], "planned")

    # 给 related 边补充 label（边字典与 related 列表对应）
    edge_by_pair = {(e["source"], e["target"]): e for e in edges if e["type"] == "related"}
    for e in related:
        key = (e["source"], e["target"])
        if key in edge_by_pair:
            edge_by_pair[key]["label"] = e["label"]

    return {
        "generatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "nodes": nodes,
        "edges": edges,
        "stages": [{"code": s["code"], "name": s["name"],
                    "progress": progress.get(s["code"])} for s in stages],
        "modules": [{"id": "m:" + m["code"], "code": m["code"], "name": m["name"],
                     "stage": m["stage"],
                     "points": [kid(k) for k in m["knowledge"]]} for m in modules],
        "points": [{"id": kid(k), "name": k["name"], "desc": k["desc"],
                    "module": k["module"], "stage": k["stage"],
                    "pitfalls": k["pitfalls"], "learned": k["learned"],
                    "days": k["days"]} for k in knowledge],
        "planned": out_planned,
        "path": path,
        "related": related,
        "days": [{"num": d["num"], "date": d["date"], "title": d["title"]} for d in days],
        "stats": {
            "stages": len(stages),
            "modules": len(modules),
            "knowledge": len(knowledge),
            "pitfalls": len(pitfalls),
            "planned": len(out_planned),
            "related": len(related),
        },
    }


def main():
    data = build()
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(
        "window.KB_DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )
    print(f"✅ 已生成 {OUT.relative_to(ROOT)}")
    print(f"   统计: {data['stats']}")
    from collections import Counter
    print(f"   节点: {dict(Counter(n['type'] for n in data['nodes']))}")
    print(f"   连线: {dict(Counter(e['type'] for e in data['edges']))}")


if __name__ == "__main__":
    main()
