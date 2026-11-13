# THE ARKANSAS ECHO

**Roots. Truth. Legacy.**

[![YouTube](https://img.shields.io/badge/YouTube-@thearkansasecho-b8860b?style=flat-square)](https://www.youtube.com/@thearkansasecho)
[![TikTok](https://img.shields.io/badge/TikTok-@the.arkansas.echo-b8860b?style=flat-square)](https://www.tiktok.com/@the.arkansas.echo)

Truthful, engaging Black history, Arkansas history, and genealogy — sourced, captioned, and told so families can recognize themselves in it.

This repository is the working library for the channel: post logs, captions, sources, a style guide, vetted story ideas, and small tools that help draft and check posts before they go out.

## Watch and follow

- **YouTube:** [youtube.com/@thearkansasecho](https://www.youtube.com/@thearkansasecho) — [subscribe](https://youtube.com/@thearkansasecho?sub_confirmation=1)
- **TikTok:** [@the.arkansas.echo](https://www.tiktok.com/@the.arkansas.echo)
- **Facebook:** [Wiley Jones post on the Echo page](https://www.facebook.com/1061522570385312_122122737741330451)

A public landing page for this library lives at **[thearkansasecho.github.io/buffer-scripts](https://thearkansasecho.github.io/buffer-scripts/)**.

## Featured stories

### Wiley Jones — posted

Born enslaved. Died the richest Black man in Arkansas. And the streetcars in Pine Bluff? Those were his.

- [Post folder](posts/wiley-jones/) — script, captions, sources, and cover
- [YouTube](https://www.youtube.com/watch?v=U2wFtbj-sVA) · [TikTok](https://www.tiktok.com/@the.arkansas.echo/video/7707440330441903373) · [Facebook](https://www.facebook.com/1061522570385312_122122737741330451)
- Hosted video: [Cloudinary](https://res.cloudinary.com/thyu6cse/video/upload/v1794528250/arkansas-echo/approved-videos/wiley-jones-arkansas-echo-v2.mp4)

### Charlotte Andrews Stephens — ready, not posted

She was fifteen — and made Little Rock history. In 1869 she became the city’s first Black public-school teacher.

- [Post folder](posts/charlotte-stephens/) — script, captions, sources, and archival portrait
- YouTube title: *She Was Fifteen—and Made Little Rock History*

## What’s in this repo

| Path | What it is |
| ---- | ---------- |
| [`posts/`](posts/) | One folder per story: script, per-platform captions, sources, status |
| [`ideas/STORY-IDEAS.md`](ideas/STORY-IDEAS.md) | Vetted future stories with hooks, sources, and image leads |
| [`STYLE-GUIDE.md`](STYLE-GUIDE.md) | Captions, tags, archival-image rules, QC, and organic growth |
| [`templates/`](templates/) | Story research template and QC checklist |
| [`examples/`](examples/) | Sample story file for the post generator |
| [`docs/`](docs/) | Public landing page (GitHub Pages) |
| `generate_post.py` | Build a post-folder skeleton and caption sets from a story file |
| `caption_check.py` | Lint captions for `#fyp`, length, “4K,” and cotton references |
| `schedule_helper.py` | Print a quality-first weekly plan for YouTube, TikTok, and Facebook |

## How to use the scripts

Python 3, standard library only. No extra packages.

```bash
# Build a new post folder from a story file (JSON or simple YAML)
python3 generate_post.py --story examples/florence-price.story.json --out posts/florence-price

# Lint captions and copy in one folder, or all of posts/
python3 caption_check.py posts/wiley-jones
python3 caption_check.py posts/

# Print a posting plan for the week
python3 schedule_helper.py
python3 schedule_helper.py --start 2026-11-16 --stories posts/charlotte-stephens
```

Every tool supports `--help`. After you draft captions, run `caption_check.py` and work through [`templates/qc-checklist.md`](templates/qc-checklist.md) before anything is marked ready.

The original starter in `generate_post.py` was a single printable post. It now writes a full folder (script, YouTube / TikTok / Facebook captions, sources, and status) and enforces TikTok `#fyp`, a tag cap, a 100-character YouTube title, and a 2,200-character TikTok caption. [`post_template.txt`](post_template.txt) is the plain-text checklist that matches that workflow.

## House rules, in brief

- Echo-only content. Every historical claim needs a source you have opened.
- Burned-in word-by-word captions and spoken narration on every video.
- Real archival images and real faces. No AI faces for real people. No cotton-field imagery. Never label an upscale as 4K.
- Disclose an AI voice where the platform requires it.
- Organic growth only. Quality first; hold a post rather than guess.

See [`STYLE-GUIDE.md`](STYLE-GUIDE.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full rules. Code in this repo is MIT. Original Echo writing is all rights reserved. Archival images keep their own licenses — details in [`LICENSE`](LICENSE).

---

*THE ARKANSAS ECHO — independent creator channel.*
