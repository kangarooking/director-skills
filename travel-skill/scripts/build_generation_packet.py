#!/usr/bin/env python3
"""Render a Markdown generation packet from a shot manifest."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def joined(value: object) -> str:
    if isinstance(value, list):
        return "；".join(str(item) for item in value) or "无"
    return str(value or "无")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"清单必须使用 JSON 兼容的 YAML 格式；解析失败：{exc}") from exc
    blocks = [f"# {data.get('project') or '文旅宣传片'}逐镜生成包\n"]

    for shot in data.get("shots") or []:
        spatial = shot.get("spatial_audit") or {}
        action = shot.get("action") or {}
        camera = shot.get("camera") or {}
        lighting = shot.get("lighting") or {}
        continuity = shot.get("continuity") or {}
        blocks.extend([
            f"## {shot.get('shot_id', '')}｜{shot.get('story_goal', '')}\n",
            f"- 时长：{shot.get('duration_seconds', '')} 秒",
            f"- 首帧：{shot.get('source_frame', '')}",
            f"- 前景/中景/背景：{joined(spatial.get('foreground'))} / {joined(spatial.get('midground'))} / {joined(spatial.get('background'))}",
            f"- 允许内容：{joined(spatial.get('allowed_content'))}",
            f"- 禁止新增：{joined(spatial.get('forbidden_additions'))}",
            f"- 分时段动作：{joined(action.get('timed_beats'))}",
            f"- CAMERA：{camera.get('framing', '')}；{camera.get('main_motion', '')}；{camera.get('secondary_motion', '')}；{camera.get('speed', '')}；跟随 {camera.get('tracking_subject', '')}；最终停在 {camera.get('camera_end', '')}。",
            f"- LIGHTING：光源依据 {lighting.get('motivation', '')}；主光 {lighting.get('key_source', '')}；方向 {lighting.get('direction', '')}；光质 {lighting.get('quality', '')}；光比 {lighting.get('ratio', '')}；补光/负补光 {lighting.get('fill_or_negative_fill', '')}；锁定曝光与白平衡。",
            f"- 预期尾帧：{continuity.get('subject_end_state', '')}",
            f"- 下一镜依赖：{continuity.get('next_shot_dependency', '')}\n",
        ])

    output = "\n".join(blocks).rstrip() + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
