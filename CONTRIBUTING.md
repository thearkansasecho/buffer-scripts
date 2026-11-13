# Contributing to this repository

This repo is for **THE ARKANSAS ECHO** only: truthful, engaging Black history,
Arkansas history, and genealogy. Personal projects and other brands do not
belong here.

## Before you add a story

1. Start from `templates/story-research-template.md`.
2. Every historical claim needs a source you have actually opened. Prefer
   primary documents and the [Encyclopedia of Arkansas](https://encyclopediaofarkansas.net/).
   Put full citations and URLs in `sources.md`. Do not invent facts, dates,
   quotes, or image credits.
3. Follow `STYLE-GUIDE.md`. Run `templates/qc-checklist.md` before you call
   anything ready.
4. Use the tools:

   ```bash
   python3 generate_post.py --story examples/florence-price.story.json --out posts/florence-price
   python3 caption_check.py posts/florence-price
   python3 schedule_helper.py --help
   ```

5. Keep captions in the post folder, one file per platform
   (`captions-youtube.md`, `captions-tiktok.md`, `captions-facebook.md`).

## What not to commit

- Secrets, tokens, API keys, `.env` files, or login credentials.
- Large media (MP4, WAV, and other audio/video). Host the file and link to it
  from `STATUS.md`. Small archival stills or covers under 1 MB are fine when
  you have the rights and a credit in `sources.md`.
- Content for any other account or brand.

## Pull requests and commits

Write a clear commit message that names the story or tool you changed. If a
claim cannot be sourced, leave it out rather than guessing.
