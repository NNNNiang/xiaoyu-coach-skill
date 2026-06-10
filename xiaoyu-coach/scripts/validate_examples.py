#!/usr/bin/env python3
"""Validate Xiaoyu Coach public example folders.

Checks that each example has:
- README.md
- expected_findings.md
- expected_report.html
- one sample video
- preview_contact_sheet.jpg

Usage:
  python xiaoyu-coach/scripts/validate_examples.py examples
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


VIDEO_SUFFIXES = {".mp4", ".mov", ".m4v"}


def validate_example(folder: Path) -> list[str]:
    errors: list[str] = []

    for required in ["README.md", "expected_findings.md", "expected_report.html", "preview_contact_sheet.jpg"]:
        if not (folder / required).exists():
            errors.append(f"{folder.name}: missing {required}")

    videos = [p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in VIDEO_SUFFIXES]
    if len(videos) != 1:
        errors.append(f"{folder.name}: expected exactly one video, found {len(videos)}")

    if (folder / "expected_findings.md").exists():
        text = (folder / "expected_findings.md").read_text(encoding="utf-8")
        required_phrases = [
            "中文验收要点",
            "English Baseline",
            "What This Sample Tests",
            "Required Observations",
            "Safety Priority Expectations",
            "Do Not Misjudge",
            "Expected Filming Advice",
        ]
        for phrase in required_phrases:
            if phrase not in text:
                errors.append(f"{folder.name}: expected_findings.md missing section '{phrase}'")

    if (folder / "expected_report.html").exists():
        text = (folder / "expected_report.html").read_text(encoding="utf-8")
        required_report_phrases = [
            "总评",
            "安全优先级",
            "本次动作内容",
            "重点动作图文复盘",
            "下次训练重点",
            "教练收束",
            "English Baseline",
            "preview_contact_sheet.jpg",
        ]
        for phrase in required_report_phrases:
            if phrase not in text:
                errors.append(f"{folder.name}: expected_report.html missing '{phrase}'")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Xiaoyu Coach examples.")
    parser.add_argument("examples_dir", type=Path, nargs="?", default=Path("examples"))
    args = parser.parse_args()

    examples_dir = args.examples_dir
    if not examples_dir.exists():
        print(f"ERROR: examples directory does not exist: {examples_dir}")
        return 2

    folders = [p for p in sorted(examples_dir.iterdir()) if p.is_dir()]
    errors: list[str] = []
    for folder in folders:
        errors.extend(validate_example(folder))

    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1

    print(f"OK: {len(folders)} example folders validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
