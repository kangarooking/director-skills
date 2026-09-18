#!/usr/bin/env python3
"""miora 视频生成轮询哨兵 —— 完成信号来自"文件已落盘"，不来自接口返回。

为什么需要它
------------
miora 生成进程与对话进程是分离的：生成完成没有回调，无法反向唤起对话；而且生成接口
的返回值本身可能整体丢失——实测发生过：15 秒视频生成成功、成片已落盘，调用方却什么
也没收到。所以"没返回"不等于"没成功"，唯一可靠的完成信号是媒体目录里出现新文件。

状态外化到两处，都不依赖对话上下文：
  1) 媒体目录新增的 .mp4（主判据）
  2) 作业标记文件 ~/.workbuddy/miora-jobs/<job>.json（跨轮、跨会话、跨项目可见）

四个动作
--------
  --submit --job X [--since EPOCH]   发起生成**之前**登记作业
  --wait   --job X [--timeout SEC]   同轮阻塞等待落盘并回读规格
  --poll   --job X                   单次巡检，不阻塞
  --poll-all                         巡检全部作业（新会话恢复现场的入口）

外加一个显式认领入口
--------------------
  --claim <本地绝对路径> --job X     把生成调用返回值里的 localPath 直接绑定给本作业

判定规则（三条，都是踩过坑才定下来的）
------------------------------------
  * 取 since 之后**最早出现**的文件，而不是最新的。两个作业时间窗重叠时，
    取最新会把后提交作业的成片误认成前一个作业的结果。
  * **已被别的作业认领的文件要被排除。** 只靠"最早出现"在时间窗重叠时仍会撞车
    （实测：并发作业 22:42:22 提交、22:44:49 提交，前者 22:49:09 落盘的文件被
    后者的 --wait 认成了自己的结果）。所以扫描时跳过其他作业标记里已登记的 file。
  * **生成调用若返回了 localPath，那个绑定优先于上面两条启发式。** 用 --claim 落账；
    存疑时下载返回的 signedUrl 做 md5 与本地文件比对，能唯一确定归属。
  * `since` 一旦登记就永不丢失；无法确定 since 的标记一律标 unknown 并跳过扫描，
    绝不 fallback 到 0（那等于扫描全部历史文件，必然误报）。
"""

import argparse
import glob
import json
import os
import re
import struct
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

MEDIA_DIR = os.path.join(
    os.path.expanduser("~"), ".workbuddy", "plugins", "data", "mcp-miora", "miora-media"
)
# 标记放在用户级固定位置：与媒体目录同为全局，不随工作目录漂移。
MARKER_DIR = os.path.join(os.path.expanduser("~"), ".workbuddy", "miora-jobs")
POLL_INTERVAL = 10.0   # 轮询间隔（秒）
SETTLE = 1.0           # 体积稳定判定间隔（秒）
SETTLE_TOP = 3         # 只对最早出现的几个候选做稳定判定
JOB_NAME_RE = re.compile(r"^[\w.-]+$", re.UNICODE)


def valid_job_name(job):
    """限制标记文件名，避免路径分隔符或 .. 把文件写出 MARKER_DIR。"""
    return bool(job) and job not in {".", ".."} and JOB_NAME_RE.fullmatch(job) is not None


def probe(path):
    """读文件头得出真实规格：时长 / 分辨率 / 有无音轨。不采信生成方自报的值。"""
    info = {"duration_sec": None, "width": None, "height": None, "has_audio": None}
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return info

    i = data.rfind(b"mvhd")          # moov 可能放在文件尾
    if i != -1:
        try:
            if data[i + 4] == 0:
                ts, dur = struct.unpack(">II", data[i + 16 : i + 24])
            else:
                ts = struct.unpack(">I", data[i + 24 : i + 28])[0]
                dur = struct.unpack(">Q", data[i + 28 : i + 36])[0]
            if ts:
                info["duration_sec"] = round(dur / ts, 2)
        except struct.error:
            pass

    j = data.find(b"tkhd")
    while j != -1:
        try:
            end = j - 4 + struct.unpack(">I", data[j - 4 : j])[0]
            w, h = struct.unpack(">II", data[end - 8 : end])
            if w and h:
                info["width"] = round(w / 65536, 1)
                info["height"] = round(h / 65536, 1)
                break
        except (struct.error, IndexError):
            pass
        j = data.find(b"tkhd", j + 1)

    info["has_audio"] = b"mp4a" in data
    return info


# ---------- 作业标记 ----------
def marker_path(job):
    return os.path.join(MARKER_DIR, job + ".json")


def load_marker(job):
    """返回 (记录, 是否可读)。JSON 损坏时返回 (None, False)。"""
    try:
        with open(marker_path(job), "r", encoding="utf-8") as f:
            return json.load(f), True
    except FileNotFoundError:
        return None, True
    except (OSError, ValueError):
        return None, False


def save_marker(job, payload):
    os.makedirs(MARKER_DIR, exist_ok=True)
    with open(marker_path(job), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def claimed_by_others(job):
    """已被**别的**作业认领的成片路径集合。时间窗重叠时用它排除撞车误认。"""
    claimed = set()
    try:
        names = os.listdir(MARKER_DIR)
    except OSError:
        return claimed
    for name in names:
        if not name.endswith(".json"):
            continue
        other = os.path.splitext(name)[0]
        if other == job:
            continue
        rec, ok = load_marker(other)
        if ok and rec and rec.get("file"):
            claimed.add(os.path.normcase(os.path.abspath(rec["file"])))
    return claimed


def scan(media_dir, since, exclude=None):
    """返回 since 之后落盘、体积已稳定的 mp4，**按时间升序**（最早在前）。"""
    if not os.path.isdir(media_dir):
        return []
    exclude = exclude or set()
    cands = []
    for name in os.listdir(media_dir):
        if not name.lower().endswith(".mp4"):
            continue
        p = os.path.join(media_dir, name)
        if os.path.normcase(os.path.abspath(p)) in exclude:
            continue
        try:
            st = os.stat(p)
        except OSError:
            continue
        if st.st_mtime < since or st.st_size == 0:
            continue
        cands.append((st.st_mtime, st.st_size, p))
    cands.sort()                     # 升序：最早出现的排第一

    out = []
    for k, (mtime, size, p) in enumerate(cands):
        if k < SETTLE_TOP:           # 新文件才做体积稳定判定，排除半写文件
            time.sleep(SETTLE)
            try:
                if os.stat(p).st_size != size:
                    continue
            except OSError:
                continue
        out.append((mtime, size, p))
    return out


def report(job, status, media_dir, since, found=None):
    """写回标记并打印结果。since 一律显式传入并写回——这是链路不断的关键。"""
    prev, _ = load_marker(job) if job else (None, True)
    payload = {
        "job": job,
        "status": status,
        "since": since if since is not None else (prev or {}).get("since"),
        "checked_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "file": None,
        "size_mb": None,
        "probe": None,
    }
    if prev and prev.get("submitted_at"):
        payload["submitted_at"] = prev["submitted_at"]
    if found:
        mtime, size, path = found
        payload.update(
            file=path,
            finish_time=time.strftime("%H:%M:%S", time.localtime(mtime)),
            size_mb=round(size / 1048576, 2),
            probe=probe(path),
        )
    if job:
        save_marker(job, payload)
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def resolve_since(job, explicit):
    """确定作业起始时刻：显式 --since > 已登记标记。都没有则当场登记，绝不臆造。"""
    if explicit is not None:
        return explicit
    rec, ok = load_marker(job)
    if rec and "since" in rec:
        return rec["since"]
    since = time.time()
    save_marker(job, {
        "job": job,
        "status": "submitted",
        "since": since,
        "submitted_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "note": "未预先登记，从本次调用时刻起算" + ("" if ok else "（原标记文件已损坏）"),
    })
    return since


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", default="", help="作业名；除 --poll-all 外必填")
    ap.add_argument("--since", type=float, default=None, help="epoch 秒，只看此后的文件")
    ap.add_argument("--timeout", type=float, default=900)
    ap.add_argument("--media-dir", default=MEDIA_DIR)
    ap.add_argument("--claim", default=None,
                    help="生成调用返回的 localPath；显式绑定给本作业，优先级高于启发式扫描")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--submit", action="store_true")
    g.add_argument("--wait", action="store_true")
    g.add_argument("--poll", action="store_true")
    g.add_argument("--poll-all", action="store_true")
    args = ap.parse_args()

    if not args.poll_all and not valid_job_name(args.job):
        ap.error("--job 必填，且只能包含字母、数字、中文、下划线、点和连字符")

    if args.claim:
        path = os.path.abspath(args.claim)
        if not os.path.isfile(path):
            sys.stderr.write("claim 指定的文件不存在：%s\n" % path)
            print(json.dumps({"job": args.job, "status": "unknown",
                              "note": "claim 路径无效，标记未改动"},
                             ensure_ascii=False, indent=2))
            return 3
        st = os.stat(path)
        report(args.job, "completed", args.media_dir, args.since,
               (st.st_mtime, st.st_size, path))
        return 0

    if args.submit:
        since = args.since if args.since is not None else time.time()
        save_marker(args.job, {
            "job": args.job,
            "status": "submitted",
            "since": since,
            "submitted_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        })
        print(json.dumps({"job": args.job, "since": since}, ensure_ascii=False, indent=2))
        return 0

    if args.poll_all:
        jobs, pending = [], 0
        for fp in sorted(glob.glob(os.path.join(MARKER_DIR, "*.json"))):
            name = os.path.splitext(os.path.basename(fp))[0]
            rec, ok = load_marker(name)
            if not ok or not rec or "since" not in rec:
                # 无法确定起始时刻 —— 标 unknown，绝不扫描全量历史
                print(json.dumps({"job": name, "status": "unknown",
                                  "note": "标记缺失或损坏，无法判定；请重新登记"},
                                 ensure_ascii=False, indent=2))
                jobs.append({"job": name, "status": "unknown"})
                pending += 1
                continue
            if rec.get("status") == "completed":
                jobs.append({"job": name, "status": "completed", "file": rec.get("file")})
                continue
            hits = scan(args.media_dir, rec["since"], claimed_by_others(name))
            if hits:
                report(name, "completed", args.media_dir, rec["since"], hits[0])
                jobs.append({"job": name, "status": "completed", "file": hits[0][2]})
            else:
                pending += 1
                jobs.append({"job": name, "status": "running"})
        print(json.dumps({"jobs": jobs}, ensure_ascii=False, indent=2))
        return 3 if pending else 0

    since = resolve_since(args.job, args.since)
    exclude = claimed_by_others(args.job)

    if args.poll:
        hits = scan(args.media_dir, since, exclude)
        if hits:
            report(args.job, "completed", args.media_dir, since, hits[0])
            return 0
        report(args.job, "running", args.media_dir, since)
        return 3

    t0 = time.time()
    while True:
        hits = scan(args.media_dir, since, exclude)
        if hits:
            report(args.job, "completed", args.media_dir, since, hits[0])
            return 0
        if time.time() - t0 >= args.timeout:
            report(args.job, "timeout", args.media_dir, since)
            return 2
        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    sys.exit(main())
