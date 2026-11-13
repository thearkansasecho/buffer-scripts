#!/usr/bin/env python3
"""Local tests for generate_post.py, caption_check.py, and schedule_helper.py.

Run from the repository root:

    python3 tests/test_tools.py
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import caption_check  # noqa: E402
import generate_post  # noqa: E402
import schedule_helper  # noqa: E402


def _story(**overrides):
    data = {
        "subject": "Test Subject",
        "youtube_title": "A Tight, Sourced Hook Under One Hundred Characters",
        "hook": "A specific Arkansas fact.",
        "body": "A second sentence with a place and a date.",
        "cta": "Did your history class mention this?",
        "signoff": "This is The Arkansas Echo.",
        "tags": ["ArkansasHistory", "BlackHistory", "LittleRock"],
        "ai_voice_disclosure": True,
        "sources": [
            {"title": "Encyclopedia of Arkansas", "url": "https://encyclopediaofarkansas.net/"}
        ],
        "status": "draft",
    }
    data.update(overrides)
    return data


class GeneratePostTests(unittest.TestCase):
    def test_example_story_builds_and_enforces_fyp(self):
        path = ROOT / "examples" / "florence-price.story.json"
        story = generate_post.load_story(path)
        files = generate_post.build_texts(story)
        self.assertIn("#fyp", files["captions-tiktok.md"].lower())
        title_line = [
            line for line in files["captions-youtube.md"].splitlines() if line.startswith("**Title:**")
        ][0]
        title = title_line.split(":**", 1)[1].strip()
        self.assertLessEqual(len(title), generate_post.YOUTUBE_TITLE_MAX)

    def test_rejects_long_youtube_title(self):
        story = _story(youtube_title="X" * 101)
        with self.assertRaises(generate_post.StoryError) as ctx:
            generate_post.build_texts(story)
        self.assertIn("YouTube title", str(ctx.exception))

    def test_rejects_long_tiktok_caption(self):
        story = _story(body="Y" * 2300)
        with self.assertRaises(generate_post.StoryError) as ctx:
            generate_post.build_texts(story)
        self.assertIn("TikTok caption", str(ctx.exception))

    def test_adds_fyp_when_missing_from_tags(self):
        story = _story(tags=["ArkansasHistory", "BlackHistory", "PineBluff", "Genealogy"])
        files = generate_post.build_texts(story)
        self.assertIn("#fyp", files["captions-tiktok.md"].lower())
        caption = files["captions-tiktok.md"].split("**Caption:**", 1)[1]
        tags = [t for t in caption.split() if t.startswith("#")]
        self.assertLessEqual(len(tags), generate_post.TIKTOK_TAG_CAP)
        self.assertIn("#fyp", " ".join(tags).lower())

    def test_yaml_round_trip_subset(self):
        text = (
            "subject: YAML Subject\n"
            "youtube_title: YAML Title Is Short\n"
            "hook: A hook.\n"
            "body: A body.\n"
            "tags:\n"
            "  - ArkansasHistory\n"
            "  - BlackHistory\n"
            "  - LittleRock\n"
            "sources:\n"
            "  - title: EOA\n"
            "    url: https://encyclopediaofarkansas.net/\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "story.yml"
            path.write_text(text, encoding="utf-8")
            story = generate_post.load_story(path)
            files = generate_post.build_texts(story)
            self.assertIn("YAML Subject", files["script.md"])
            self.assertIn("#fyp", files["captions-tiktok.md"].lower())

    def test_write_and_lint_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "post"
            files = generate_post.build_texts(_story())
            generate_post.write_post(out, files)
            findings = []
            for path in out.glob("*.md"):
                findings.extend(caption_check.lint_file(path))
            errors = [f for f in findings if f.kind == "error"]
            self.assertEqual(errors, [], errors)


class CaptionCheckTests(unittest.TestCase):
    def _write(self, tmp: Path, name: str, text: str) -> Path:
        path = tmp / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_flags_missing_fyp(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(
                Path(tmp),
                "captions-tiktok.md",
                "# TikTok\n\n**Caption:**\n\nA caption.\n\n#ArkansasHistory\n",
            )
            findings = caption_check.lint_file(path)
            self.assertTrue(any("missing #fyp" in f.message for f in findings))

    def test_flags_4k(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write(Path(tmp), "script.md", "This render is 4K.\n")
            findings = caption_check.lint_file(path)
            self.assertTrue(any("4K" in f.message for f in findings if f.kind == "error"))

    def test_flags_cotton_but_warns_on_place_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = self._write(Path(tmp), "captions-facebook.md", "A cotton field at dusk.\n")
            ok = self._write(
                Path(tmp),
                "captions-tiktok.md",
                "# TikTok\n\n**Caption:**\n\nBorn in Cotton Plant, Arkansas.\n\n#fyp\n",
            )
            bad_findings = caption_check.lint_file(bad)
            ok_findings = caption_check.lint_file(ok)
            self.assertTrue(any(f.kind == "error" and "Cotton" in f.message for f in bad_findings))
            self.assertFalse(any(f.kind == "error" for f in ok_findings))
            self.assertTrue(any(f.kind == "warning" and "Cotton Plant" in f.message for f in ok_findings))

    def test_existing_posts_pass(self):
        posts = ROOT / "posts"
        files = caption_check.collect_targets([posts])
        findings = []
        for path in files:
            findings.extend(caption_check.lint_file(path))
        errors = [str(f) for f in findings if f.kind == "error"]
        self.assertEqual(errors, [], errors)


class ScheduleHelperTests(unittest.TestCase):
    def test_prints_week_and_channels(self):
        import datetime as dt

        start = dt.date(2026, 11, 16)
        lines = schedule_helper.build_plan(start, [])
        text = "\n".join(lines)
        self.assertIn("2026-11-16", text)
        self.assertIn("YouTube", text)
        self.assertIn("TikTok", text)
        self.assertIn("Facebook", text)
        self.assertIn("Monday", text)
        self.assertIn("Sunday", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
