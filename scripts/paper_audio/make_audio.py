"""PML PDF -> 章节音频转换器（edge-tts + ffmpeg）。

用法:
  python scripts/paper_audio/make_audio.py --list
  python scripts/paper_audio/make_audio.py --chapters 2          # 试点单章
  python scripts/paper_audio/make_audio.py --chapters 2,3 --voice en-US-AriaNeural
  python scripts/paper_audio/make_audio.py --chapters all        # 全书（耗时）

产出（audio_out/）:
  PML_Intro_Ch02.mp3  章节音频（可调语速见 --rate）
  PML_Intro_Ch02.txt  清洗后的文本（喂 NotebookLM 或跟读用）
"""

import argparse
import asyncio
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent.parent.parent / ".tools" / "audiotools"
if _TOOLS.exists():
    sys.path.insert(0, str(_TOOLS))  # 自举: python3 直接可跑，无需 PYTHONPATH

import edge_tts  # noqa: E402
import pymupdf  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
PDF = ROOT / "papers" / "ProbabilisticMachineLearning_An Introduction.pdf"
OUT_DIR = ROOT / "audio_out"
VOICE = "en-US-GuyNeural"
RATE = "+0%"
CHUNK_CHARS = 3000
FOOTER_MARK = "Author: Kevin P. Murphy"

FOOTER_RE = re.compile(r"CC-BY-NC-ND license", re.I)
EQNUM_RE = re.compile(r"^\(\d+\.\d+\)$")  # (2.4) 行内公式编号
PAGENUM_RE = re.compile(r"^\d{1,3}$")
HEADNUM_RE = re.compile(r"^(\d+\.)+\d*$")  # 独立小节号 2.1.3.4
GREEKISH = set("≜∨∈⊥∀∃∂∇∑∏√≤≥≠≈±×·→←↔⊕⊗∼∝∠")


def letter_ratio(line: str) -> float:
    """字母（含空格）占比——公式行占比低，用于过滤。"""
    s = line.replace(" ", "")
    if not s:
        return 0.0
    alpha = sum(1 for c in s if c.isalpha())
    return alpha / len(s)


def clean_page(text: str) -> str:
    """清洗单页文本: 去页眉页脚/公式行/编号行，拼回段落。"""
    lines: list[str] = []
    for raw in text.split("\n"):
        line = unicodedata.normalize("NFKC", raw).strip()
        if not line:
            lines.append("")
            continue
        if FOOTER_MARK in line or FOOTER_RE.search(line):
            continue
        if EQNUM_RE.match(line) or PAGENUM_RE.match(line) or HEADNUM_RE.match(line):
            continue
        if any(c in GREEKISH for c in line) and letter_ratio(line) < 0.5:
            continue  # 含数学符号的低字母行=公式
        if letter_ratio(line) < 0.45:
            continue  # 纯符号公式行
        lines.append(line)

    # 段落重建: 断行拼接（下行小写开头且上行非句尾 -> 并入）
    out: list[str] = []
    for line in lines:
        if out and line and out[-1] and not out[-1].endswith((".", ":", "?", "!", ";")):
            if line[0].islower() or line[0] in "(∈≜":
                out[-1] += " " + line
                continue
        out.append(line)
    return "\n".join(out)


def extract_chapters() -> dict[int, tuple[str, int, int]]:
    """从 TOC 提取 {章号: (标题, 起页, 止页)}。"""
    doc = pymupdf.open(PDF)
    toc = doc.get_toc()
    chapters: list[tuple[int, str, int]] = []
    for _lvl, title, page in toc:
        m = re.match(r"^(\d+)\s+(.+)$", title)
        if m and int(m.group(1)) <= 30:  # 章级条目（排除 Part/附录）
            chapters.append((int(m.group(1)), m.group(2).strip(), page))
    result: dict[int, tuple[str, int, int]] = {}
    for i, (num, title, start) in enumerate(chapters):
        end = chapters[i + 1][2] - 1 if i + 1 < len(chapters) else doc.page_count
        result[num] = (title, start, end)
    doc.close()
    return result


def chapter_text(num: int) -> str:
    """抽取并清洗整章文本，开头补章节播报。"""
    doc = pymupdf.open(PDF)
    title, start, end = extract_chapters()[num]
    parts: list[str] = [f"Chapter {num}. {title}."]
    for pno in range(start - 1, min(end, doc.page_count)):
        parts.append(clean_page(doc[pno].get_text()))
    doc.close()
    text = "\n\n".join(parts)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return re.sub(r"[ \t]{2,}", " ", text)


def chunk_text(text: str, size: int = CHUNK_CHARS) -> list[str]:
    """按段落边界切块，供 TTS 分段合成。"""
    paras = text.split("\n\n")
    chunks: list[str] = []
    buf = ""
    for p in paras:
        if len(buf) + len(p) > size and buf:
            chunks.append(buf)
            buf = p
        else:
            buf = f"{buf}\n\n{p}" if buf else p
    if buf:
        chunks.append(buf)
    return chunks


async def synth_chunk(idx: int, text: str, voice: str, rate: str, tmp: Path) -> Path:
    """单块合成 mp3（网络调用，串行执行防止限流）。"""
    out = tmp / f"{idx:03d}.mp3"
    comm = edge_tts.Communicate(text, voice, rate=rate)
    await comm.save(str(out))
    return out


def merge_mp3(files: list[Path], out_file: Path) -> None:
    """ffmpeg concat 合并分块。"""
    lst = out_file.parent / f"{out_file.stem}_list.txt"
    lst.write_text("\n".join(f"file '{f}'" for f in files), encoding="utf-8")
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
         "-i", str(lst), "-c", "copy", str(out_file)],
        check=True,
    )
    lst.unlink()


async def make_chapter(num: int, voice: str, rate: str) -> Path:
    """整章流水线: 抽取 -> 清洗 -> 分块 -> 合成 -> 合并。"""
    OUT_DIR.mkdir(exist_ok=True)
    text = chapter_text(num)
    txt_out = OUT_DIR / f"PML_Intro_Ch{num:02d}.txt"
    txt_out.write_text(text, encoding="utf-8")

    chunks = chunk_text(text)
    tmp = OUT_DIR / f".tmp_ch{num:02d}"
    tmp.mkdir(exist_ok=True)
    parts: list[Path] = []
    for i, chunk in enumerate(chunks):
        print(f"  合成 {i + 1}/{len(chunks)} 块（{len(chunk)} 字符）...", flush=True)
        parts.append(await synth_chunk(i, chunk, voice, rate, tmp))

    mp3_out = OUT_DIR / f"PML_Intro_Ch{num:02d}.mp3"
    merge_mp3(parts, mp3_out)
    for p in parts:
        p.unlink()
    tmp.rmdir()
    print(f"✅ 第{num}章完成 -> {mp3_out} ({mp3_out.stat().st_size // 1024} KB)")
    return mp3_out


def main() -> None:
    ap = argparse.ArgumentParser(description="PML PDF -> 章节音频")
    ap.add_argument("--list", action="store_true", help="列出章节")
    ap.add_argument("--chapters", default="2", help="章号: 2 / 2,3 / all")
    ap.add_argument("--voice", default=VOICE, help="edge-tts 音色")
    ap.add_argument("--rate", default=RATE, help="语速 如 -10%")
    args = ap.parse_args()

    chapters = extract_chapters()
    if args.list:
        for num in sorted(chapters):
            t, s, e = chapters[num]
            print(f"Ch{num:2d}  p{s:3d}-{e:3d}  {t}")
        return

    nums = sorted(chapters) if args.chapters == "all" else [
        int(x) for x in args.chapters.split(",") if x.strip()
    ]
    for n in nums:
        print(f"== 第 {n} 章: {chapters[n][0]} ==")
        asyncio.run(make_chapter(n, args.voice, args.rate))


if __name__ == "__main__":
    sys.exit(main())
