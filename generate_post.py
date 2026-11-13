#!/usr/bin/env python3
"""Build an Echo post-folder skeleton from a JSON or simple YAML story file.

Usage:
    python3 generate_post.py --story examples/florence-price.story.json --out posts/florence-price
    python3 generate_post.py --help

The tool writes script.md, captions-youtube.md, captions-tiktok.md,
captions-facebook.md, sources.md, and STATUS.md. It enforces #fyp on
TikTok, a tag cap, a 100-character YouTube title, and a 2,200-character
TikTok caption.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

YOUTUBE_TITLE_MAX = 100
TIKTOK_CAPTION_MAX = 2200
YOUTUBE_DESC_MAX = 5000
TIKTOK_TAG_CAP = 5  # #fyp + 3-4 niche tags
DEFAULT_TAG_CAP = 5
SIGNOFF = "This is The Arkansas Echo."


class StoryError(ValueError):
    """Invalid story file or limit violation."""


def _strip_hash(tag: str) -> str:
    return tag.strip().lstrip("#").strip()


def _format_tags(tags: list[str], *, require_fyp: bool = False, cap: int = DEFAULT_TAG_CAP) -> list[str]:
    seen: list[str] = []
    for raw in tags:
        name = _strip_hash(str(raw))
        if not name:
            continue
        key = name.lower()
        if any(s.lower() == key for s in seen):
            continue
        seen.append(name)
    if require_fyp and not any(s.lower() == "fyp" for s in seen):
        seen.append("fyp")
    if require_fyp:
        # Keep #fyp, then the remaining slots for niche tags.
        fyp = [t for t in seen if t.lower() == "fyp"]
        others = [t for t in seen if t.lower() != "fyp"]
        seen = others[: max(0, cap - 1)] + fyp[:1]
    elif len(seen) > cap:
        seen = seen[:cap]
    return [f"#{t}" for t in seen]


def _load_simple_yaml(text: str) -> Any:
    """Minimal YAML subset: mappings, lists, quoted/literal strings, scalars.

    Good enough for the story files this tool expects. Use JSON if you need
    the full language.
    """

    def parse_scalar(raw: str) -> Any:
        raw = raw.strip()
        if raw in {"", "~", "null", "Null", "NULL"}:
            return None
        if raw in {"true", "True", "TRUE"}:
            return True
        if raw in {"false", "False", "FALSE"}:
            return False
        if re.fullmatch(r"-?\d+", raw):
            return int(raw)
        if re.fullmatch(r"-?\d+\.\d+", raw):
            return float(raw)
        if (raw.startswith('"') and raw.endswith('"')) or (
            raw.startswith("'") and raw.endswith("'")
        ):
            return raw[1:-1]
        if raw.startswith("|") or raw.startswith(">"):
            return raw  # handled by block reader
        return raw

    lines: list[tuple[int, str]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        lines.append((indent, line.strip()))

    def parse_block(idx: int, min_indent: int) -> tuple[Any, int]:
        if idx >= len(lines):
            return {}, idx
        indent, content = lines[idx]
        if indent < min_indent:
            return {}, idx
        if content.startswith("- "):
            items: list[Any] = []
            while idx < len(lines) and lines[idx][0] == indent and lines[idx][1].startswith("- "):
                item_raw = lines[idx][1][2:].strip()
                idx += 1
                if item_raw and (item_raw.endswith(":") or ": " in item_raw):
                    # inline mapping on a list item, plus following indented keys
                    first: dict[str, Any] = {}
                    if item_raw.endswith(":"):
                        key = item_raw[:-1].strip()
                        if idx < len(lines) and lines[idx][0] > indent:
                            val, idx = parse_block(idx, lines[idx][0])
                            first[key] = val
                        else:
                            first[key] = None
                    else:
                        k, v = item_raw.split(":", 1)
                        first[k.strip()] = parse_scalar(v)
                    while idx < len(lines) and lines[idx][0] > indent and not lines[idx][1].startswith("- "):
                        nested, idx = parse_mapping_segment(idx, lines[idx][0], first)
                        first = nested
                    items.append(first)
                elif item_raw:
                    items.append(parse_scalar(item_raw))
                else:
                    if idx < len(lines) and lines[idx][0] > indent:
                        val, idx = parse_block(idx, lines[idx][0])
                        items.append(val)
                    else:
                        items.append(None)
            return items, idx
        return parse_mapping_segment(idx, indent, {})

    def parse_mapping_segment(idx: int, indent: int, acc: dict[str, Any]) -> tuple[dict[str, Any], int]:
        while idx < len(lines) and lines[idx][0] == indent and not lines[idx][1].startswith("- "):
            content = lines[idx][1]
            if ":" not in content:
                raise StoryError(f"YAML line not a key: {content}")
            key, rest = content.split(":", 1)
            key = key.strip()
            rest = rest.strip()
            idx += 1
            if rest in {"|", ">"}:
                block_lines: list[str] = []
                while idx < len(lines) and lines[idx][0] > indent:
                    # restore a conservative indent
                    block_lines.append(lines[idx][1])
                    idx += 1
                acc[key] = "\n".join(block_lines)
            elif rest:
                acc[key] = parse_scalar(rest)
            else:
                if idx < len(lines) and lines[idx][0] > indent:
                    val, idx = parse_block(idx, lines[idx][0])
                    acc[key] = val
                else:
                    acc[key] = None
        return acc, idx

    if not lines:
        return {}
    value, end = parse_block(0, lines[0][0])
    if end != len(lines) and not isinstance(value, dict):
        # top-level mapping may have been parsed as a first segment
        pass
    if isinstance(value, dict):
        # If parse_block started a mapping, consume remaining top-level keys
        acc = value
        idx = end
        while idx < len(lines):
            acc, idx = parse_mapping_segment(idx, lines[0][0], acc)
        return acc
    return value


def load_story(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix in {".yaml", ".yml"}:
        data = _load_simple_yaml(text)
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise StoryError("Story file must be a mapping / JSON object.")
    return data


def _as_source_lines(sources: Any) -> list[str]:
    lines: list[str] = []
    if not sources:
        return lines
    for item in sources:
        if isinstance(item, str):
            lines.append(f"- {item}")
        elif isinstance(item, dict):
            title = str(item.get("title") or item.get("name") or "").strip()
            url = str(item.get("url") or "").strip()
            if title and url:
                lines.append(f"- {title}. {url}")
            elif url:
                lines.append(f"- {url}")
            elif title:
                lines.append(f"- {title}")
    return lines


def build_texts(story: dict[str, Any]) -> dict[str, str]:
    subject = str(story.get("subject") or story.get("slug") or "Untitled").strip()
    hook = str(story.get("hook") or "").strip()
    body = str(story.get("body") or "").strip()
    script = str(story.get("script") or "").strip()
    cta = str(story.get("cta") or "").strip()
    signoff = str(story.get("signoff") or SIGNOFF).strip()
    youtube_title = str(story.get("youtube_title") or hook or subject).strip()
    image_credit = str(story.get("image_credit") or story.get("image_credits") or "").strip()
    disclose = bool(story.get("ai_voice_disclosure", True))
    status = str(story.get("status") or "draft").strip()
    tags = story.get("tags") or []
    if not isinstance(tags, list):
        raise StoryError("'tags' must be a list.")

    errors: list[str] = []
    if len(youtube_title) > YOUTUBE_TITLE_MAX:
        errors.append(
            f"YouTube title is {len(youtube_title)} characters (max {YOUTUBE_TITLE_MAX})."
        )

    yt_tags = _format_tags(list(tags) + ["Shorts"], require_fyp=False, cap=DEFAULT_TAG_CAP)
    # Prefer niche tags, then #Shorts, cap at 5. If Shorts got dropped, swap last.
    if not any(t.lower() == "#shorts" for t in yt_tags):
        if len(yt_tags) >= DEFAULT_TAG_CAP:
            yt_tags = yt_tags[:-1] + ["#Shorts"]
        else:
            yt_tags.append("#Shorts")
    tt_tags = _format_tags(list(tags), require_fyp=True, cap=TIKTOK_TAG_CAP)
    fb_tags = _format_tags(list(tags), require_fyp=False, cap=DEFAULT_TAG_CAP)

    paragraphs = [p for p in (hook, body, cta, signoff) if p]
    common = "\n\n".join(paragraphs)

    source_lines = _as_source_lines(story.get("sources"))
    source_block = ""
    if source_lines:
        source_block = "Sources:\n" + "\n".join(source_lines)

    disclosure = ""
    if disclose:
        disclosure = (
            "Narration is an AI-generated voice. Photographs and engravings "
            "are authentic archival images, not AI-generated."
        )

    yt_desc_parts = [common]
    if source_block:
        yt_desc_parts.append(source_block)
    if image_credit:
        yt_desc_parts.append(image_credit)
    if disclosure:
        yt_desc_parts.append(disclosure)
    yt_desc_parts.append(" ".join(yt_tags))
    youtube_description = "\n\n".join(yt_desc_parts)
    if len(youtube_description) > YOUTUBE_DESC_MAX:
        errors.append(
            f"YouTube description is {len(youtube_description)} characters "
            f"(max {YOUTUBE_DESC_MAX})."
        )

    tiktok_caption = common + "\n\n" + " ".join(tt_tags)
    if len(tiktok_caption) > TIKTOK_CAPTION_MAX:
        errors.append(
            f"TikTok caption is {len(tiktok_caption)} characters "
            f"(max {TIKTOK_CAPTION_MAX})."
        )
    if "#fyp" not in tiktok_caption.lower():
        errors.append("TikTok caption is missing #fyp.")

    if errors:
        raise StoryError(" ".join(errors))

    if not script:
        script = common

    fb_parts = [common]
    if image_credit:
        fb_parts.append(image_credit)
    fb_parts.append(" ".join(fb_tags))
    facebook = "\n\n".join(fb_parts)

    sources_md_lines = [f"# {subject} — sources", ""]
    if source_lines:
        sources_md_lines.extend(source_lines)
    else:
        sources_md_lines.append(
            "Add full citations and URLs here before this story is marked ready."
        )
    if image_credit:
        sources_md_lines.extend(["", image_credit])

    status_md = (
        f"# Status: {status}\n\n"
        f"**Story:** {subject}\n"
        f"**YouTube title:** {youtube_title}\n\n"
        "Update this file when the piece moves from idea to script to ready "
        "to posted. Add live URLs only after they exist.\n"
    )

    return {
        "script.md": f"# {subject} — narration script\n\n{script}\n",
        "captions-youtube.md": (
            f"# YouTube Shorts\n\n"
            f"**Title:** {youtube_title}\n\n"
            f"**Description:**\n\n{youtube_description}\n"
        ),
        "captions-tiktok.md": f"# TikTok\n\n**Caption:**\n\n{tiktok_caption}\n",
        "captions-facebook.md": f"# Facebook\n\n{facebook}\n",
        "sources.md": "\n".join(sources_md_lines) + "\n",
        "STATUS.md": status_md,
    }


def write_post(out_dir: Path, files: dict[str, str], force: bool = False) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for name, content in files.items():
        dest = out_dir / name
        if dest.exists() and not force:
            raise StoryError(
                f"{dest} already exists. Pass --force to overwrite generated files."
            )
        dest.write_text(content, encoding="utf-8")
        written.append(dest)
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Build a THE ARKANSAS ECHO post folder (script, per-platform "
            "captions, sources, status) from a JSON or simple YAML story file."
        )
    )
    parser.add_argument(
        "--story",
        type=Path,
        help="Path to a story file (.json, .yaml, or .yml).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        help="Output folder, for example posts/florence-price.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite generated markdown files if they already exist.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and print the files without writing them.",
    )
    args = parser.parse_args(argv)

    if not args.story or not args.out:
        parser.print_help()
        return 2 if (args.story or args.out) else 0

    try:
        story = load_story(args.story)
        files = build_texts(story)
        if args.dry_run:
            for name, content in files.items():
                print(f"===== {name} =====")
                print(content)
            return 0
        written = write_post(args.out, files, force=args.force)
        print(f"Wrote {len(written)} files to {args.out}")
        for path in written:
            print(f"  {path}")
        return 0
    except (OSError, json.JSONDecodeError, StoryError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
