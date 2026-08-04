#!/usr/bin/env python3
"""Validate shot durations in a Markdown storyboard."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SHOT_RE = re.compile(r"^##\s+((?:S|分镜)\s*\d+|S\d+)", re.M | re.I)
DURATION_RE = re.compile(r"(?:时长|duration)\s*[：:]\s*(\d+(?:\.\d+)?)\s*(?:秒|s)", re.I)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("storyboard", type=Path)
    parser.add_argument("--max-shot-seconds", type=float, default=0)
    parser.add_argument("--expected-total", type=float, default=0)
    args = parser.parse_args()

    text = args.storyboard.read_text(encoding="utf-8")
    matches = list(SHOT_RE.finditer(text))
    errors: list[str] = []
    warnings: list[str] = []
    durations: list[tuple[str, float]] = []

    seen: set[str] = set()
    for index, match in enumerate(matches):
        shot_id = re.sub(r"\s+", "", match.group(1)).upper()
        if shot_id in seen:
            errors.append(f"镜头 ID 重复：{shot_id}")
        seen.add(shot_id)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end():end]
        duration = DURATION_RE.search(section)
        if not duration:
            warnings.append(f"{shot_id} 缺少明确时长。")
            continue
        seconds = float(duration.group(1))
        durations.append((shot_id, seconds))
        if seconds <= 0:
            errors.append(f"{shot_id} 时长必须大于 0。")
        if args.max_shot_seconds and seconds > args.max_shot_seconds:
            warnings.append(f"{shot_id} 为 {seconds:g} 秒，超过单次生成上限 {args.max_shot_seconds:g} 秒。")

    total = sum(value for _, value in durations)
    if args.expected_total and abs(total - args.expected_total) > 0.05:
        warnings.append(f"总时长 {total:g} 秒，与目标 {args.expected_total:g} 秒不一致。")

    print(f"shots={len(matches)} durations={len(durations)} total_seconds={total:g}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

