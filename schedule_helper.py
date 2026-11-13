#!/usr/bin/env python3
"""Print a quality-first weekly posting plan for Echo channels.

Plans YouTube, TikTok, and Facebook only. Default is one ready story
cross-posted the same day, not a high-volume calendar. Organic growth;
quality first.

Usage:
    python3 schedule_helper.py
    python3 schedule_helper.py --start 2026-11-16 --stories posts/charlotte-stephens
    python3 schedule_helper.py --help
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

CHANNELS = ("YouTube", "TikTok", "Facebook")
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def parse_date(value: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Use YYYY-MM-DD (got {value!r})."
        ) from exc


def monday_on_or_after(day: dt.date) -> dt.date:
    return day if day.weekday() == 0 else day + dt.timedelta(days=(7 - day.weekday()))


def story_label(path: Path) -> str:
    status_file = path / "STATUS.md" if path.is_dir() else None
    status = ""
    title = path.name
    if status_file and status_file.is_file():
        text = status_file.read_text(encoding="utf-8")
        for line in text.splitlines():
            if line.lower().startswith("# status:"):
                status = line.split(":", 1)[1].strip()
            if line.lower().startswith("**youtube title:**"):
                title = line.split(":**", 1)[1].strip()
    label = f"{path.as_posix()}"
    if title and title != path.name:
        label = f"{path.name} — {title}"
    if status:
        label = f"{label} [{status}]"
    return label


def default_stories(root: Path) -> list[Path]:
    posts = root / "posts"
    if not posts.is_dir():
        return []
    found: list[Path] = []
    for child in sorted(posts.iterdir()):
        if child.is_dir() and (child / "STATUS.md").is_file():
            text = (child / "STATUS.md").read_text(encoding="utf-8").lower()
            # Prefer ready / not-yet-posted stories; skip already posted unless asked.
            if "posted" in text and "not posted" not in text and "ready, not posted" not in text:
                continue
            found.append(child)
    return found


def build_plan(
    start: dt.date,
    stories: list[Path],
    same_day: bool = True,
) -> list[str]:
    lines: list[str] = []
    lines.append("THE ARKANSAS ECHO — weekly posting plan")
    lines.append(f"Week of {start.isoformat()} (Monday start).")
    lines.append("Channels: YouTube, TikTok, Facebook. Echo only.")
    lines.append("Quality first. Organic growth only. Do not buy engagement.")
    lines.append("")
    if not stories:
        lines.append(
            "No ready stories were passed in. Use --stories with a post folder,"
        )
        lines.append("or add a STATUS.md under posts/. Hold the week rather than rush.")
        lines.append("")
        for i, name in enumerate(WEEKDAYS):
            day = start + dt.timedelta(days=i)
            lines.append(f"{name} {day.isoformat()}: no post planned.")
        return lines

    # One story per mid-week slot by default. Same-day cross-post to all three.
    # Leave Monday for QC, weekends for watching comments — not for extra volume.
    slots = [2] if len(stories) == 1 else [1, 3][: len(stories)]  # Tue / Thu
    assigned = {idx: stories[i] for i, idx in enumerate(slots)}

    for i, name in enumerate(WEEKDAYS):
        day = start + dt.timedelta(days=i)
        story = assigned.get(i)
        if not story:
            if i == 0:
                note = "QC and caption_check.py on the next piece. No post."
            elif i >= 5:
                note = "Reply to comments (genuine and specific). No extra post."
            else:
                note = "Open. Hold unless a ready story is waiting."
            lines.append(f"{name} {day.isoformat()}: {note}")
            continue
        label = story_label(story)
        if same_day:
            channels = ", ".join(CHANNELS)
            lines.append(
                f"{name} {day.isoformat()}: post “{label}” to {channels} (same-day cross-post)."
            )
        else:
            # Stagger: YouTube, then TikTok, then Facebook on following days if asked.
            lines.append(
                f"{name} {day.isoformat()}: YouTube — “{label}” "
                "(TikTok and Facebook follow the next two open days)."
            )
    lines.append("")
    lines.append("Before each post: run python3 caption_check.py on the folder,")
    lines.append("and work through templates/qc-checklist.md. If QC fails, slip the day.")
    return lines


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Print a quality-first weekly plan for THE ARKANSAS ECHO across "
            "YouTube, TikTok, and Facebook."
        )
    )
    parser.add_argument(
        "--start",
        type=parse_date,
        default=None,
        help="Week start (YYYY-MM-DD). Defaults to the coming Monday, or today if Monday.",
    )
    parser.add_argument(
        "--stories",
        type=str,
        default="",
        help="Comma-separated post folders (e.g. posts/charlotte-stephens).",
    )
    parser.add_argument(
        "--stagger",
        action="store_true",
        help="Start on YouTube and follow on TikTok and Facebook the next two days.",
    )
    args = parser.parse_args(argv)

    today = dt.date.today()
    start = args.start or monday_on_or_after(today)
    # If a mid-week date was given, snap to that week's Monday so the plan is a week.
    start = start - dt.timedelta(days=start.weekday())

    if args.stories.strip():
        stories = [Path(part.strip()) for part in args.stories.split(",") if part.strip()]
        missing = [s for s in stories if not s.exists()]
        if missing:
            print(
                "error: story path not found: " + ", ".join(str(s) for s in missing),
                file=sys.stderr,
            )
            return 2
    else:
        stories = default_stories(Path.cwd())

    lines = build_plan(start, stories, same_day=not args.stagger)
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
