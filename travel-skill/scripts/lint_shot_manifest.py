#!/usr/bin/env python3
"""Validate the structured shot manifest used by the skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def empty(value: object) -> bool:
    return value is None or value == "" or value == [] or value == {}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"清单必须使用 JSON 兼容的 YAML 格式；解析失败：{exc}") from exc
    defaults = data.get("model_defaults", {})
    max_seconds = float(defaults.get("max_seconds") or 0)
    shots = data.get("shots") or []
    errors: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()

    for i, shot in enumerate(shots, start=1):
        shot_id = str(shot.get("shot_id") or f"row-{i}")
        if shot_id in seen:
            errors.append(f"镜头 ID 重复：{shot_id}")
        seen.add(shot_id)
        for key in ("story_goal", "duration_seconds", "source_frame"):
            if empty(shot.get(key)):
                errors.append(f"{shot_id} 缺少 {key}。")

        duration = float(shot.get("duration_seconds") or 0)
        if duration <= 0:
            errors.append(f"{shot_id} duration_seconds 必须大于 0。")
        elif max_seconds and duration > max_seconds:
            warnings.append(f"{shot_id} 超过默认单次生成时长 {max_seconds:g} 秒。")

        spatial = shot.get("spatial_audit") or {}
        camera = shot.get("camera") or {}
        lighting = shot.get("lighting") or {}
        for key in ("foreground", "midground", "background", "camera_start", "allowed_content", "forbidden_additions"):
            if empty(spatial.get(key)):
                warnings.append(f"{shot_id} 空间审计字段 {key} 为空。")
        for key in ("main_motion", "tracking_subject", "camera_end"):
            if empty(camera.get(key)):
                warnings.append(f"{shot_id} 运镜字段 {key} 为空。")
        for key in ("motivation", "key_source", "direction"):
            if empty(lighting.get(key)):
                warnings.append(f"{shot_id} 布光字段 {key} 为空。")
        if not lighting.get("exposure_lock", False):
            warnings.append(f"{shot_id} 未锁定曝光。")
        if not lighting.get("white_balance_lock", False):
            warnings.append(f"{shot_id} 未锁定白平衡。")

        if not spatial.get("subjects_present") and not spatial.get("allowed_entries"):
            warnings.append(f"{shot_id} 首帧无主体且没有允许的进入路径。")

    print(f"shots={len(shots)} errors={len(errors)} warnings={len(warnings)}")
    for item in errors:
        print(f"ERROR: {item}")
    for item in warnings:
        print(f"WARN: {item}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
