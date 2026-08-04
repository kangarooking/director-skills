#!/usr/bin/env python3
"""Lint an AI travel-film prompt for common generation failures."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


EDITING_WORDS = {
    "切到": "生成提示词出现剪辑语言，模型可能硬切。",
    "硬切": "不要在生成提示词中要求硬切。",
    "独立段落": "独立段落会被理解为新镜头，请改写为同一空间中的连续状态。",
    "转为另一个地点": "跨地点应拆分生成或使用剪辑衔接。",
    "突然出现": "主体或物体必须在首帧存在或有可见进入路径。",
}

MOTION_GROUPS = {
    "pan": ["横摇", "pan"],
    "tilt": ["俯仰", "抬头", "tilt"],
    "dolly": ["推进", "后拉", "dolly", "push-in", "pull-out"],
    "truck": ["横移", "truck"],
    "pedestal": ["垂直上升", "垂直下降", "pedestal"],
    "orbit": ["环绕", "绕拍", "orbit", "arc"],
    "drone": ["无人机", "航拍", "drone", "aerial"],
    "zoom": ["变焦", "zoom"],
    "follow": ["跟拍", "follow", "tracking"],
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--model", default="unspecified")
    parser.add_argument("--max-chars", type=int, default=0)
    args = parser.parse_args()

    text = args.prompt.read_text(encoding="utf-8")
    warnings: list[str] = []

    if args.max_chars and len(text) > args.max_chars:
        warnings.append(f"字符数 {len(text)} 超过限制 {args.max_chars}。")

    for word, message in EDITING_WORDS.items():
        positions = (match.start() for match in re.finditer(re.escape(word), text))
        if any(not re.search(r"(?:无|不|禁止)\s*$", text[max(0, pos - 4):pos]) for pos in positions):
            warnings.append(f"“{word}”：{message}")

    motions = []
    lower = text.lower()
    for name, terms in MOTION_GROUPS.items():
        if any(term.lower() in lower for term in terms):
            motions.append(name)
    if len(motions) > 2:
        warnings.append("检测到多个运镜族：" + ", ".join(motions) + "。单次生成建议一个主运镜，最多一个自然衔接动作。")

    volume_requested = (
        ("体积光" in text and not re.search(r"(?:无|不使用|禁止)\s*体积光", text))
        or "volumetric" in lower
        or "god rays" in lower
    )
    medium_present = re.search(r"雾|尘|烟|蒸汽|雨|mist|fog|dust|smoke|steam|rain", lower)
    medium_negated = re.search(r"(?:没有|无)\s*(?:真实|可见)?\s*(?:雾|尘|烟|蒸汽|雨)", text)
    if volume_requested and (not medium_present or medium_negated):
        warnings.append("使用体积光但没有可见的雾、尘、烟、蒸汽或雨等真实介质。")

    if re.search(r"完美皮肤|无瑕|塑料皮肤|perfect skin|flawless skin", lower):
        warnings.append("皮肤词可能产生塑料感；改为真实纹理、自然漫反射与柔和高光。")

    if "锁定机位" in text and re.search(r"推进|后拉|横移|环绕|dolly|truck|orbit", lower):
        warnings.append("“锁定机位”与整体摄影机移动互相矛盾。")

    print(f"model={args.model} chars={len(text)} warnings={len(warnings)}")
    for item in warnings:
        print(f"WARN: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
