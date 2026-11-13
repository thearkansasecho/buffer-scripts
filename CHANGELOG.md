# Changelog

All notable changes to this repository are listed here.

## 2026-11-12

- Posted the Charlotte Andrews Stephens short to Echo YouTube, TikTok, and
  Facebook. Live links are in `posts/charlotte-stephens/STATUS.md`. Issue #11
  is marked posted and closed.

- Added a public landing page under `docs/` for GitHub Pages.
- Added a GitHub Actions workflow that runs `caption_check.py` and `tests/test_tools.py`
  on every push and pull request.
- Added issue templates (new story idea, source correction) and a pull-request
  template with the QC checklist.
- Added a “Trending Nov 2026” section at the top of `ideas/STORY-IDEAS.md`.

- Expanded the README into a real homepage for THE ARKANSAS ECHO, with the
  mission, channel links, featured stories, and how to use the tools.
- Added a post log under `posts/` for the Wiley Jones short (posted) and the
  Charlotte Andrews Stephens short (ready, not posted), including scripts,
  per-platform captions, sources, and licenses.
- Added `ideas/STORY-IDEAS.md` with vetted, sourced future stories.
- Added `STYLE-GUIDE.md` covering captions, tags, archival-image rules,
  quality control, AI-voice disclosure, and organic growth.
- Upgraded `generate_post.py` to build a post-folder skeleton and
  per-platform caption sets from a JSON (or simple YAML) story file.
  The tool now enforces `#fyp` on TikTok, a tag cap, and character limits.
- Added `caption_check.py` to lint captions and related copy.
- Added `schedule_helper.py`, which prints a quality-first posting plan for
  the week across YouTube, TikTok, and Facebook.
- Added `examples/`, `templates/`, `CONTRIBUTING.md`, and this license split
  (code MIT; original writing all rights reserved; archival images keep their
  own licenses).
- The original `post_template.txt` is kept and updated so it matches the
  current platform checklist.

## 2026-11-07 and earlier

- Starter README, `generate_post.py`, and `post_template.txt` for Buffer
  post workflows, including a YouTube subscribe call-to-action.
