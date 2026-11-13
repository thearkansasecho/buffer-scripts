#!/usr/bin/env python3
"""Lint Echo captions and related copy.

Flags a missing #fyp on TikTok captions, cotton references, the word "4K",
and over-long text (TikTok 2200, YouTube title 100, YouTube description 5000).

Usage:
    python3 caption_check.py posts/wiley-jones
    python3 caption_check.py posts/
    python3 caption_check.py --help
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

YOUTUBE_TITLE_MAX = 100
TIKTOK_CAPTION_MAX = 2200
YOUTUBE_DESC_MAX = 5000
FACEBOOK_CAPTION_MAX = 63206

COTTON_RE = re.compile(r"\bcotton(?:s|y|'s)?\b", re.IGNORECASE)
COTTON_PLANT_RE = re.compile(r"\bcotton\s+plant\b", re.IGNORECASE)
FOUR_K_RE = re.compile(r"\b4\s*k\b", re.IGNORECASE)
FYP_RE = re.compile(r"(?<!\w)#fyp\b", re.IGNORECASE)
TITLE_RE = re.compile(r"\*\*Title:\*\*\s*(.+)", re.IGNORECASE)
CAPTION_HEADER_RE = re.compile(r"\*\*Caption:\*\*\s*", re.IGNORECASE)
DESC_HEADER_RE = re.compile(r"\*\*Description:\*\*\s*", re.IGNORECASE)

# Markdown / structural lines to skip when scanning body copy.
SKIP_LINE_RE = re.compile(r"^\s{0,3}(#{1,6}\s|---\s*$|\*\*YouTube settings)")


class Finding:
    def __init__(self, path: Path, kind: str, message: str, line: int | None = None):
        self.path = path
        self.kind = kind  # "error" or "warning"
        self.message = message
        self.line = line

    def __str__(self) -> str:
        loc = f"{self.path}"
        if self.line is not None:
            loc = f"{self.path}:{self.line}"
        return f"{self.kind.upper()}: {loc}: {self.message}"


def _strip_md(text: str) -> str:
    return text.replace("**", "").replace("__", "").strip()


def extract_youtube_title(text: str) -> str | None:
    match = TITLE_RE.search(text)
    if match:
        return _strip_md(match.group(1))
    return None


def extract_section_after(text: str, header_re: re.Pattern[str]) -> str:
    match = header_re.search(text)
    if not match:
        return ""
    rest = text[match.end():]
    # Stop at a later markdown heading or **YouTube settings**
    stop = re.search(r"\n#{1,6}\s|\n\*\*YouTube settings", rest)
    if stop:
        rest = rest[: stop.start()]
    return rest.strip()


def is_tiktok_file(path: Path) -> bool:
    return "tiktok" in path.name.lower()


def is_youtube_file(path: Path) -> bool:
    return "youtube" in path.name.lower()


def is_facebook_file(path: Path) -> bool:
    return "facebook" in path.name.lower()


def collect_targets(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        path = raw.resolve()
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.is_file():
            files.append(path)
        else:
            raise FileNotFoundError(str(raw))
    # Lint spoken copy and platform captions. sources.md may discuss
    # omitted cotton imagery or "not labeled 4K"; those notes are not
    # treated as caption violations.
    skip_names = {"STYLE-GUIDE.md", "CHANGELOG.md", "CONTRIBUTING.md", "LICENSE", "README.md"}
    skip_dirs = {".git", "templates", "docs", ".github", "ideas", "examples"}
    out: list[Path] = []
    for f in files:
        if f.name in skip_names:
            continue
        if any(part in skip_dirs for part in f.parts):
            continue
        out.append(f)
    return out


def lint_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []
    name = path.name.lower()

    if is_tiktok_file(path):
        caption = extract_section_after(text, CAPTION_HEADER_RE) or text
        if not FYP_RE.search(caption):
            findings.append(
                Finding(path, "error", "TikTok caption is missing #fyp.")
            )
        length = len(caption)
        if length > TIKTOK_CAPTION_MAX:
            findings.append(
                Finding(
                    path,
                    "error",
                    f"TikTok caption is {length} characters (max {TIKTOK_CAPTION_MAX}).",
                )
            )

    if is_youtube_file(path):
        title = extract_youtube_title(text)
        if title is not None and len(title) > YOUTUBE_TITLE_MAX:
            findings.append(
                Finding(
                    path,
                    "error",
                    f"YouTube title is {len(title)} characters (max {YOUTUBE_TITLE_MAX}): {title!r}",
                )
            )
        desc = extract_section_after(text, DESC_HEADER_RE)
        if desc and len(desc) > YOUTUBE_DESC_MAX:
            findings.append(
                Finding(
                    path,
                    "error",
                    f"YouTube description is {len(desc)} characters (max {YOUTUBE_DESC_MAX}).",
                )
            )

    if is_facebook_file(path):
        # Body is the file minus the heading.
        body = re.sub(r"^#.*\n", "", text, count=1).strip()
        if len(body) > FACEBOOK_CAPTION_MAX:
            findings.append(
                Finding(
                    path,
                    "error",
                    f"Facebook caption is {len(body)} characters (max {FACEBOOK_CAPTION_MAX}).",
                )
            )

    # 4K and cotton rules apply to captions and spoken script, not to
    # source notes that record what was omitted or forbidden.
    apply_banned_words = (
        is_tiktok_file(path)
        or is_youtube_file(path)
        or is_facebook_file(path)
        or path.name.lower() == "script.md"
    )

    if not apply_banned_words:
        return findings

    for lineno, line in enumerate(text.splitlines(), 1):
        if SKIP_LINE_RE.match(line) and not FOUR_K_RE.search(line) and not COTTON_RE.search(line):
            continue
        if FOUR_K_RE.search(line):
            findings.append(
                Finding(
                    path,
                    "error",
                    "Contains '4K'. Never label an upscale (or anything else) as 4K.",
                    lineno,
                )
            )
        for match in COTTON_RE.finditer(line):
            # Allow the place name "Cotton Plant"
            window_start = max(0, match.start() - 0)
            window = line[window_start:]
            # If this "cotton" is the start of "Cotton Plant", note it only.
            tail = line[match.start():]
            if COTTON_PLANT_RE.match(tail):
                findings.append(
                    Finding(
                        path,
                        "warning",
                        "Contains 'Cotton Plant' (place name). Allowed, but do not use cotton-field imagery.",
                        lineno,
                    )
                )
            else:
                findings.append(
                    Finding(
                        path,
                        "error",
                        "Cotton reference. No cotton-field imagery; check whether this wording should be cut.",
                        lineno,
                    )
                )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Lint THE ARKANSAS ECHO captions for a missing #fyp on TikTok, "
            "cotton references, the word 4K, and over-long text."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Caption files or folders (default: posts/).",
    )
    args = parser.parse_args(argv)
    targets = args.paths or [Path("posts")]
    try:
        files = collect_targets(targets)
    except FileNotFoundError as exc:
        print(f"error: path not found: {exc}", file=sys.stderr)
        return 2
    if not files:
        print("error: no markdown files to check.", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    for path in files:
        findings.extend(lint_file(path))

    errors = [f for f in findings if f.kind == "error"]
    warnings = [f for f in findings if f.kind == "warning"]
    for item in findings:
        print(item)
    print(
        f"Checked {len(files)} file(s): {len(errors)} error(s), {len(warnings)} warning(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
