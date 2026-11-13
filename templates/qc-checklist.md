# QC checklist

Use this on the final file, not only on a work-in-progress preview.
Date the pass and write what you actually checked.

## File and specs

- [ ] Final path or hosted URL recorded in `STATUS.md`
- [ ] Real resolution written down (do not say 4K)
- [ ] Frame rate, duration, and audio codec checked
- [ ] Loudness and true peak measured on the finished encode
- [ ] Cover still chosen on purpose (not a random mid-film frame)

## Story and sources

- [ ] Every spoken claim is cited in `sources.md`
- [ ] Names, dates, and place names match the sources
- [ ] “First,” fortune figures, and other strong claims are qualified or cut
      if they rest on a single source or promotional wording
- [ ] Omitted facts are listed so they are not sneaked back in later

## Captions, voice, and picture

- [ ] Burned-in word-by-word captions match the finished audio
- [ ] Short words stay on screen long enough to read
- [ ] Lip sync checked if a person is on camera
- [ ] Spoken narration is present and even
- [ ] Faces are not covered by title bars; platform button safe zones are clear
- [ ] No cotton-field imagery
- [ ] No AI faces for real people; archival credits are on screen
- [ ] AI-generated narration is disclosed where the platform requires it

## Captions and packaging

- [ ] `python3 caption_check.py posts/<slug>` passes
- [ ] TikTok caption includes `#fyp` and 3–4 niche tags
- [ ] YouTube title is 100 characters or fewer
- [ ] TikTok caption is 2,200 characters or fewer
- [ ] Echo branding only

## Second pass

- [ ] A later sitting (or a second reviewer) watched and listened through
- [ ] Status is still accurate: draft, ready, or posted
