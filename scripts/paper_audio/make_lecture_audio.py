"""PML 教材 -> 中文讲课口播稿 -> 章节音频（DeepSeek 改写 + edge-tts 合成）。

与 make_audio.py 的区别: 中间加了 LLM 讲稿化——书本原文变成"老师讲课"的
中文口吻，公式口语化、术语带英文、有过渡句，专为耳朵优化。

用法:
  python scripts/paper_audio/make_lecture_audio.py --chapters 2 --sample  # 第2章开头试听版(~5分钟)
  python scripts/paper_audio/make_lecture_audio.py --chapters 2           # 整章
  python scripts/paper_audio/make_lecture_audio.py --chapters all         # 全书

依赖: .env 里配 DEEPSEEK_API_KEY（网络已验证可达）
"""

import argparse
import asyncio
import os
import sys
import time
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent.parent / ".tools" / "audiotools"
if _TOOLS.exists():
    sys.path.insert(0, str(_TOOLS))  # 自举: python3 直接可跑

import edge_tts  # noqa: E402
import requests  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

sys.path.insert(0, str(Path(__file__).parent))
from make_audio import (  # noqa: E402
    OUT_DIR,
    PDF,
    chapter_text,
    chunk_text,
    extract_chapters,
    merge_mp3,
)

API_URL = "https://open.bigmodel.cn/api/coding/paas/v4/chat/completions"
MODEL = "glm-5.3"  # 旗舰(思考型)，走 coding 专线；被限流可换 glm-5-turbo
EN_VOICE = "en-US-GuyNeural"
REWRITE_CHUNK = 2500  # 原文字符/次改写

SYSTEM_PROMPT = """You are a world-class ML lecturer (think StatQuest meets Mark Schmidt) turning a
machine-learning textbook into a SPOKEN lecture. Rewrite the excerpt as natural spoken English:
1. INTUITION FIRST: before any formal definition, give the intuitive idea or a tiny concrete
   example ("Imagine rolling a die..."). Define only after motivating.
2. EXAMPLES SPOKEN ALOUD: walk through the book's examples step by step, saying the numbers.
3. SIGNPOSTING: use verbal transitions that explain WHY we move on
   ("We just saw X; the natural question now is Y, because...").
4. Formulas: NEVER read verbatim. Explain what each part means in words, or say
   "it can be shown that". Skip mangled fragments entirely.
5. RECAP: when a major concept closes, add one plain-sentence summary
   ("So in short, ...").
6. Keep every concept/definition/example; never invent content beyond the text.
7. Output ONLY the narration: no headings, numbering, markdown, or preamble.
Target length: 60-100% of the original."""


def rewrite(text: str, api_key: str, retries: int = 2) -> str:
    """单块教材 -> 中文讲稿（DeepSeek）。"""
    for attempt in range(retries + 1):
        try:
            resp = requests.post(
                API_URL,
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": text},
                    ],
                    "temperature": 0.3,
                    "max_tokens": 8192,
                },
                timeout=180,
            )
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:  # noqa: BLE001 网络重试兜底
            if attempt == retries:
                raise
            wait = 15 * (attempt + 1) if "429" in str(e) else 3  # 限流长退避
            print(f"  改写失败重试({attempt + 1}) 等{wait}s: {e}", flush=True)
            time.sleep(wait)
    return ""  # 不可达


async def synth(chunk: str, voice: str, out: Path) -> None:
    """中文讲稿块 -> mp3。"""
    comm = edge_tts.Communicate(chunk, voice)
    await comm.save(str(out))


async def make_chapter(num: int, api_key: str, voice: str, sample: bool) -> None:
    """整章流水线: 抽取 -> LLM 讲稿化 -> 合成 -> 合并。"""
    OUT_DIR.mkdir(exist_ok=True)
    raw = chapter_text(num)
    if sample:
        raw = raw[: REWRITE_CHUNK * 2]  # 试听版只取开头两块
        tag = "sample"
    else:
        tag = ""

    en_chunks = chunk_text(raw, REWRITE_CHUNK)
    print(f"== 第{num}章: {extract_chapters()[num][0]} | {len(en_chunks)} 块 {'(试听版)' if sample else ''}")

    lecture_parts: list[str] = []
    tmp = OUT_DIR / f".tmp_lec{num:02d}"
    tmp.mkdir(exist_ok=True)
    parts: list[Path] = []
    for i, chunk in enumerate(en_chunks):
        print(f"  讲稿化 {i + 1}/{len(en_chunks)}...", flush=True)
        zh = rewrite(chunk, api_key)
        lecture_parts.append(zh)
        p = tmp / f"{i:03d}.mp3"
        print(f"  合成   {i + 1}/{len(en_chunks)} ({len(zh)} 字)...", flush=True)
        await synth(zh, voice, p)
        parts.append(p)

    stem = f"PML_Lecture_Ch{num:02d}{'_' + tag if tag else ''}"
    (OUT_DIR / f"{stem}.txt").write_text("\n\n".join(lecture_parts), encoding="utf-8")
    mp3 = OUT_DIR / f"{stem}.mp3"
    merge_mp3(parts, mp3)
    for p in parts:
        p.unlink()
    tmp.rmdir()
    print(f"✅ -> {mp3.name} ({mp3.stat().st_size // 1024} KB)")


def main() -> None:
    load_dotenv()
    key = os.getenv("ZHIPU_API_KEY")
    if not key:
        sys.exit("请先在 .env 配置 ZHIPU_API_KEY（open.bigmodel.cn 控制台获取）")

    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", default="2")
    ap.add_argument("--sample", action="store_true", help="只做开头试听版")
    ap.add_argument("--voice", default=EN_VOICE)
    args = ap.parse_args()

    nums = sorted(extract_chapters()) if args.chapters == "all" else [
        int(x) for x in args.chapters.split(",") if x.strip()
    ]
    for n in nums:
        asyncio.run(make_chapter(n, key, args.voice, args.sample))


if __name__ == "__main__":
    main()
