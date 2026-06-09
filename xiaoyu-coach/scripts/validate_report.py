#!/usr/bin/env python3
"""Validate Xiaoyu Coach HTML or Markdown reports.

Checks:
- required user-facing sections
- forbidden internal terms
- local HTML image paths

Usage:
  python scripts/validate_report.py path/to/report.html
  python scripts/validate_report.py path/to/report.md
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_TERMS = [
    "MediaPipe",
    "Mediapipe",
    "OpenPose",
    "OpenCV",
    "summary",
    "dense",
    "tracking pollution",
    "invalid frame",
    "model recognition error",
    "骨架追踪",
    "骨骼追踪污染",
    "污染帧",
    "数据作废",
    "筛选帧",
    "自动判断",
]

HTML_REQUIRED = [
    "总评",
    "安全优先级",
    "本次动作内容",
    "重点动作图文复盘",
    "下次训练重点",
    "教练收束",
]

MD_RECOMMENDED = [
    "训练量",
    "做对的事",
    "需改进",
    "红旗",
    "阶段性建议",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def check_forbidden_terms(text: str) -> list[str]:
    hits = []
    for term in FORBIDDEN_TERMS:
        if term in text:
            hits.append(f"Forbidden internal term found: {term}")
    return hits


def check_html(path: Path, text: str) -> list[str]:
    errors = []
    for section in HTML_REQUIRED:
        if section not in text:
            errors.append(f"Missing HTML section: {section}")

    root = path.parent
    for match in re.finditer(r'<img\s+[^>]*src=["\']([^"\']+)["\']', text, flags=re.I):
        src = match.group(1)
        if re.match(r"^[a-z]+://", src, flags=re.I) or src.startswith("data:"):
            continue
        img_path = (root / src.replace("/", "\\")).resolve()
        if not img_path.exists():
            errors.append(f"Missing image: {src}")

    return errors


def check_markdown(text: str) -> list[str]:
    warnings = []
    for section in MD_RECOMMENDED:
        if section not in text:
            warnings.append(f"Recommended Markdown section not found: {section}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Xiaoyu Coach reports.")
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    path = args.report
    if not path.exists():
        print(f"ERROR: file does not exist: {path}")
        return 2

    text = read_text(path)
    errors = check_forbidden_terms(text)
    warnings: list[str] = []

    suffix = path.suffix.lower()
    if suffix in {".html", ".htm"}:
        errors.extend(check_html(path, text))
    elif suffix in {".md", ".markdown"}:
        warnings.extend(check_markdown(text))
    else:
        warnings.append(f"Unknown report extension: {suffix}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1

    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
