# Arkansas bar exam score-tampering case — sources, licenses, rights

DRAFT for review. Not posted, not scheduled, not uploaded to Buffer or any platform.

Final video: `/workspace/echo-bar-exam/bar-exam-arkansas-echo-1080x1920.mp4`
Cover: `/workspace/echo-bar-exam/bar-exam-cover-1080x1920.jpg` (also in this folder)

This is a pending criminal case. Every allegation in the short is attributed to prosecutors, to the six justices’ joint statement, or to arresting documents as reported in the press. Nancie Givens has pleaded not guilty and is presumed innocent. A racial-motive claim that circulated on social media and in unverified X news summaries is **not** in the court statements, the prosecutor’s remarks, or the reputable print coverage we opened, and it is not in the video.

## Narration

- Method: ElevenLabs `creative_generate_speech`, voice **“Jon — Warm, Credible, Reassuring”** (`voice_id` `zlNWXcnnZStiyXG49qLv`), model `eleven_v4`. Flow `VB360C5exOR0YCWr4LZ8`, session `d1zvktJd4B6TChzWrObl`, generation `2R11IMw5KV44YMf4TarL`, node `Fy6kccA8uXM7ocJnt685`.
- Cost: **1,626.0 credits, 16.26 cents USD.** Estimated first at the same figure. A first attempt failed with a busy free-generation queue and was not charged. One take generated on retry. No plan upgrade.
- Spoken script: 274 words, about 1,631 characters (`SCRIPT-SPOKEN.txt` on the box).
- Raw speech: about 111.12 s. Final bed: 48 kHz stereo PCM, **112.12 s** (`audio/narration.wav` on the box), 1.0 s pad, two-pass loudnorm + limiter + a measured −0.7 dB lift. Integrated **−14.0 LUFS**, LRA 2.7 LU, true peak **−3.7 dBFS** on the bed. Finished MP4: **−14.0 LUFS**, LRA 2.7 LU, true peak **−3.3 dBTP**.
- Word timings: faster-whisper `medium.en` on short clips (a full-file pass collapsed after about 39 s), then a curated 267-word list with RMS snap, MIN_SHOW / MAX_DELAY (`bar-word-timings.json` / `.csv` on the box). Display forms: **65**, **270**, **64**, **11,400**, **25**, **5TH**, **FBI**, **NANCIE** (not Nancy). **ECHO** is held to 111.50 s. Some function words are shorter than 0.24 s because the next word starts immediately (same treatment as the AME short).

## Images used on screen (source + license)

See `credits.md` in this folder for the full credit list and the images held back. Summary:

1. Dsdugan, Arkansas State Capitol, Little Rock, dusk front. Wikimedia Commons, [File:21-16-009-capitol.jpg](https://commons.wikimedia.org/wiki/File:21-16-009-capitol.jpg), [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Hook, close, “11,400 files” card, cover.
2. Dsdugan, Arkansas State Capitol, side elevation. Wikimedia Commons, [File:21-16-001-capitol.jpg](https://commons.wikimedia.org/wiki/File:21-16-001-capitol.jpg), [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). Identification, 65 counts, 64 people, FBI timeline.
3. Xiquinho Silva, Capitol atrium, April 8, 2024. Wikimedia Commons, [File:Arkansas State Capitol - 54118375368.jpg](https://commons.wikimedia.org/wiki/File:Arkansas_State_Capitol_-_54118375368.jpg), [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).
4. Xiquinho Silva, Capitol dome, April 8, 2024. Wikimedia Commons, [File:Arkansas State Capitol - 54118566195.jpg](https://commons.wikimedia.org/wiki/File:Arkansas_State_Capitol_-_54118566195.jpg), [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/).

These photographs are of the **State Capitol**. They are never labeled as the Supreme Court or as the Office of Professional Programs. The Office of Professional Programs is in the Multi-Agency Complex at 501 Woodlane, just northwest of the Capitol (Arkansas Democrat-Gazette, November 11, 2026, aerial caption). The Justice Building is at 625 Marshall Street.

On-screen quote and fact cards are Echo designs. Quoted wording is from the November 5, 2026 joint press release and is credited as “exact official wording, not a facsimile of the page.”

No AI faces. No invented photograph of Givens. No cotton imagery. Native 1080×1920 — not an upscale, not 4K.

## Primary sources (opened and saved)

1. **Supreme Court of Arkansas, Joint Press Release, November 5, 2026.** “Joint Statement Regarding State Criminal Charges and Irregularities in the Supreme Court of Arkansas’s Office of Professional Programs and the Arkansas Bar Examination.” Issued jointly by Associate Justices Courtney R. Hudson, Rhonda K. Wood, Shawn A. Womack, J. Cody Hiland, and Nicholas J. Bronni, and Special Associate Justice Cory A. Cox. Chief Justice Karen R. Baker issued a separate, shorter statement and did not sign this one. Landing page: https://arcourts.gov/press-releases/arkansas-bar-examination-joint-press-release — PDF: https://arcourts.gov/sites/default/files/2026-11/Joint%20Press%20Release%20%2811-05-2026%29_0.pdf. The official PDF is a three-page scan (`docs/joint-press-release.pdf` on the box). A line-by-line transcript from those pages is at `docs/JOINT-PRESS-RELEASE-TRANSCRIPT.txt`. This is the source for: resignation in February 2026 (the court says “resigned,” not “retired”); Robert Brech’s internal review; “approximately 11,400 files were deleted or rendered unavailable” in early January 2026, including applications, profiles, and score sheets the office was required to retain for 25 years; discrepancies across “at least eight test administrations between July 2020 and July 2025”; the “harvested points” passage and elevation to “the minimum passing score of 270 or greater”; “at least one instance” in which alterations may have reduced a passing score to a failing score; “at least one instance” in which the person who should have received the top score had that score reduced; “If these allegations are true, these actions constitute an unprecedented breach of public trust”; “grave and potentially criminal abuse of power”; “The vast majority of examinees who were previously informed that they had passed … did, in fact, pass”; affected examinees “will be notified … upon definitive confirmation of their status”; criminal investigation initiated in April 2026 by the Arkansas State Police and the FBI; 65 counts of tampering with a public record under Ark. Code Ann. § 5-54-121, filed by the Prosecuting Attorney’s Office for the Sixth Judicial District; “all defendants are presumed innocent until proven guilty”; referral to the Office of Professional Conduct; new testing procedures beginning with the February 2026 exam.

2. **Supreme Court of Arkansas, Press Release issued by Chief Justice Karen R. Baker, November 5, 2026.** One-page statement (`docs/press-release-11.5.26.pdf` on the box). Confirms the internal review, the 65 counts against Nancie Givens, former Executive Director of OPP, in connection with discrepancies from July 2020 to July 2025, and declines further comment “to preserve the integrity of the active and ongoing investigation.” Does not describe the point transfers or the deleted files.

3. **Office of Professional Conduct, Order of Interim Suspension, Nancie Michelle Givens, Arkansas Bar No. 91055, CPC-2026-036, Panel B, November 5, 2026.** (`docs/opc-2026-036.pdf` on the box.) Used only for background: full name; last day February 27, 2026; OPP executive director from March 25, 2013; earlier service at the Office of Professional Conduct, 1994–March 24, 2013; a May 21, 2026 FBI interview and a home search are mentioned. This is a disciplinary order, not a criminal conviction. It is not shown on screen, and its findings are not narrated as facts of the criminal case.

4. **Ark. Code Ann. § 5-54-121**, tampering with a public record (2025). https://law.justia.com/codes/arkansas/title-5/subtitle-5/chapter-54/subchapter-1/section-5-54-121/. The offense is a Class C felony if the record is a court record, otherwise Class D. Prosecutors charged Class C. The short names the offense and does not state a maximum sentence.

## News sources (opened; used to confirm or to attribute)

5. Daniela Dehaghani, “Former Arkansas bar exam official charged with 65 felonies in alleged score tampering,” **KATV**, November 5, 2026, updated November 7, 2026. https://katv.com/news/local/former-arkansas-bar-exam-official-charged-with-65-felonies-in-alleged-score-tampering. The most detailed reporting we opened. Confirms: full name Nancie Michelle Givens; arrested November 5, 2026; 65 counts, each a Class C felony; pleaded not guilty; Sixth Judicial District Prosecuting Attorney Will Jones; at least 64 individuals with manually altered scores, attributed to an investigative affidavit / arresting documents; Nov. 4 affidavit listed 64 counts, prosecutors announced 65 on Nov. 5, and “the documents provided do not explain the discrepancy”; shared-drive file count 11,447 to 205 between nightly backups on January 4 and January 5, 2026, described as “sudden and significant”; court personnel “could not determine who carried it out”; about 8,100 files later restored “did not match the records that had been deleted”; May 21 interview with Arkansas State Police Special Investigator Joe Pickett, in which Givens said she moved files after being directed to terminate an employee and “But apparently, I didn’t put them all back”; a silver thumb drive recovered at her home; “the affidavit does not establish that she was responsible for the large-scale deletion that occurred between Jan. 4 and Jan. 5.” The short attributes the 64-person figure to “arresting documents, reported in the press,” and does **not** say Givens deleted the January 4–5 files.

6. Michael Thompson, “UPDATE: 11,400 bar exam files deleted or unavailable,” **KATV**, November 6, 2026. https://katv.com/news/local/update-11400-bar-exam-files-deleted-or-unavailable. Confirms the justices’ 11,400-file statement and the 65 counts.

7. Ella McCarthy, Brett Barrouquere, and John Lynch, “Former director of Office of Professional Programs charged in Arkansas Bar Exam tampering probe,” **Arkansas Democrat-Gazette**, November 5, 2026, updated 6:58 p.m. https://www.arkansasonline.com/news/2026/nov/05/former-director-of-office-of-professional/. Landing page and search snippets opened; the body is paywalled. Used to confirm the 65-count arrest and charge, in line with the court releases. Not used as a sole source for any number.

8. Jacie Sellars, “Altered bar exam scores could affect thousands of cases in Arkansas, experts say,” **Arkansas Democrat-Gazette**, November 11, 2026. https://www.arkansasonline.com/news/2026/nov/11/altered-bar-exam-scores-thousands-cases-arkansas/. The aerial caption places the Office of Professional Programs in the Multi-Agency Complex, “just northwest of the state Capitol.” Expert comment about possible effects on past cases is speculation and is not in the short.

9. Sam Skolnik, “Ex-Arkansas Court Official Accused of Changing Bar Exam Scores,” **Bloomberg Law**, November 6, 2026. https://news.bloomberglaw.com/litigation/ex-arkansas-court-official-accused-of-changing-bar-exam-scores. Confirms she pleaded not guilty to each count, per the Arkansas District Court docket; a seal order is in place and some documents are not public. (Coverage describes the case as filed Thursday in Arkansas District Court.)

10. Michael Hibblen, “Former Arkansas bar exam official charged with 65 counts of record tampering,” **Talk Business & Politics**, November 5, 2026. https://talkbusiness.net/2026/11/former-arkansas-bar-exam-official-charged-with-65-counts-of-record-tampering/. Reprints and attributes the joint-statement passages; useful as a second open transcription of the justices’ wording.

11. Milo Strain, “Arkansas official accused of tampering with bar exams charged with 65 felonies,” **Arkansas Times**, November 5, 2026. https://arktimes.com/arkansas-blog/2026/11/05/arkansas-official-accused-of-tampering-with-bar-exams-charged-with-65-felonies. Quotes Prosecuting Attorney Will Jones: the charges concern “the alteration of exam results and the destruction of supporting records.” Notes the investigation is ongoing.

12. Julianne Hill, “Former state official charged with tampering with bar exam results,” **ABA Journal**, November 6, 2026. https://www.abajournal.com/news/article/arkansas-official-charged-with-tampering-bar-exam-results. National confirmation of the 65 counts and the eight administrations; paraphrases the court, and in at least one sentence states the point-moving as fact rather than allegation — we stayed with the court’s “evidence exists” and “if these allegations are true.”

13. Eugene Volokh / Reason, “Arkansas Bar Official Allegedly Transferred Points Between Examinees,” November 7, 2026. https://reason.com/volokh/2026/11/07/arkansas-bar-official-allegedly-transferred-points-/. Carries a full text of the joint statement; used as a check on our scan transcript, not as a primary source.

14. Vaidehi Mehta, “Who Really Passed? Arkansas Bar Exam Case Puts Lawyers’ Results Under Scrutiny,” **FindLaw**, November 11, 2026. https://www.findlaw.com/legalblogs/greedy-associates/who-really-passed-arkansas-bar-exam-case-puts-lawyers-results-under-scrutiny/. Secondary legal-press overview. Not a source for any unique fact.

## Sources opened, then used carefully or set aside

15. **Fox 13 Memphis**, November 6, 2026. https://www.fox13memphis.com/news/former-state-supreme-court-executive-accused-of-tampering-with-bar-exam-results/article_eefd7829-469e-4415-bc1f-1b696c0bce44.html. Overstates the record: “the Arkansas Supreme Court said they discovered the scandal after Givens deleted more than 11,000 files in January.” The justices said the files were deleted or made unavailable; the affidavit, as reported by KATV, does **not** establish that Givens carried out the January 4–5 deletion. We did not use this wording.

16. Robert Steinbuch, “Backstory of state’s legal debacle,” **Northwest Arkansas Democrat-Gazette**, November 13, 2026. https://www.nwaonline.com/news/2026/nov/13/backstory-of-states-legal-debacle/. Clearly labeled **OPINION**. Mentions 65 counts, “up to 10 years” on each, and “at least 64 people.” Opinion commentary on motive, “worst scandals,” and possible effects on past cases is not used as fact.

17. 4029tv / Adam Roberts, November 6, 2026. https://www.4029tv.com/article/arkansas-bar-exam-score-tampering/74349463. Brief local pickup. No unique confirmed fact.

## Verified claims that are in the short (each with a source)

- Nancie Givens was the executive director of the Arkansas Supreme Court’s Office of Professional Programs, which administers the Arkansas Bar Examination. (Joint PR; Baker PR.)
- She resigned in February 2026. Last day, per the OPC order, February 27, 2026. The short says “resigned in February,” following the court, not “retired.” (Joint PR.)
- On November 5, 2026, she was charged with 65 felony counts of tampering with a public record, Ark. Code Ann. § 5-54-121. (Joint PR; Baker PR; KATV; Arkansas Times quoting Will Jones.)
- She has pleaded not guilty and is presumed innocent. (Bloomberg Law, from the docket; KATV; Joint PR on the presumption.)
- The alleged score changes spanned at least eight administrations, July 2020 to July 2025. The passing score is 270. (Joint PR.)
- The six justices wrote: “Evidence exists that Givens harvested points from a number of examinees’ scores and then added them to other examinees’ scores within the same test administration,” elevating some to 270 or greater. (Joint PR, exact wording on the designed card.)
- At least one examinee who otherwise would have passed may have been given a failing score; at least one rightful top scorer had the score reduced. (Joint PR.) The short attributes this to what “they say.”
- Arresting documents, as reported by KATV (and mentioned in the Steinbuch column), identified at least 64 people whose scores were altered. The Nov. 4 affidavit listed 64 counts; prosecutors announced 65 on Nov. 5. The discrepancy is unexplained. The short reports 65 as the charge count and 64 as the press-reported affidavit figure, and does not pretend they are the same number.
- About 11,400 files were deleted or made unavailable in early January 2026, including records the office had to keep for 25 years. (Joint PR.) The short does not name a person who deleted them.
- An internal review by Robert Brech found the irregularities; the FBI and Arkansas State Police opened a probe in April 2026. (Joint PR.)
- “If these allegations are true, these actions constitute an unprecedented breach of public trust.” (Joint PR, exact wording.)
- “The vast majority of examinees who were previously informed that they had passed … did, in fact, pass.” Affected examinees will be notified once their status is confirmed. (Joint PR.)

## What we could not confirm, and what we left out

- **A racial motive, or that Black test-takers were targeted.** Not in the joint statement, Baker’s statement, the prosecutor’s quoted remarks, KATV, the Arkansas Democrat-Gazette pages we could open, Bloomberg Law, Talk Business, the Arkansas Times, or the ABA Journal. It appeared in social-media posts and in unverified X news summaries. Omitted.
- **Who carried out the January 4–5 shared-drive deletion.** The justices said files were deleted or made unavailable. KATV, citing the affidavit, says court personnel could not determine who did it, and that the affidavit does not establish Givens carried out that large deletion. The short follows the justices’ wording and does not name a person.
- **A defense attorney’s name, and the next court date.** Not in the open coverage we have. Bloomberg Law reports a seal order, with some documents not public.
- **Motive.** Not established by prosecutors in the materials we opened. Steinbuch’s questions about money or friendship are opinion.
- **How many people were licensed who should not have been, or how many were wrongly told they failed, beyond “at least one” of each.** The court has not published a full count. The “thousands of cases” headline is expert speculation, not a court finding.
- **Bond amount, age, Texas law license, exact arrest hour.** Some of these appear in coverage or in the OPC order. They are not needed for the short and were left out rather than risk a thin source.
- **Maximum sentence, or “650 years.”** Each Class C count can carry a substantial term (press has said up to 10 years each). Stacking that into a headline total would be misleading. The short does not state a penalty.
- **A historical Black-lawyer angle (Scipio Africanus Jones, Wiley Branton, and others).** True as Arkansas history, and already in this archive. Left out of this short because the race-of-examinees claim is unconfirmed, and forcing that history onto this case would imply a motive the court has not stated.
- **A government-released booking photograph.** We did not find one on an official agency page. A third-party aggregator was not used. The short has no face of Givens.
- **Resigned vs. retired.** Some early news said “retired.” The court says “resigned.” We use “resigned.”
- THV11, Fox16, KARK, and Reuters pages were often blocked to our fetch tools. We did not depend on them for any unique fact.

## Legal and tone notes

- Pending criminal case: presumption of innocence throughout, including a persistent on-screen badge on the charge cards (“CHARGED · PLEADED NOT GUILTY · PRESUMED INNOCENT”) and the spoken line “She is presumed innocent.”
- The hook says “Prosecutors say she took points off some bar exams and put them on others.” The criminal charges, as described by Prosecuting Attorney Will Jones, concern “the alteration of exam results and the destruction of supporting records.” The more precise “harvested points” wording is the six justices’. The next paragraph of the short attributes that wording to them, and the on-screen card quotes them exactly.
- The joint statement’s wording on the failing-score instance is slightly more cautious (“may have reduced”). The short says “they say, someone who would have passed was told they failed,” with an on-screen badge “THE JUSTICES SAY · ALLEGATIONS, NOT A VERDICT.”
- Official document scans were not left readable under competing titles, and the 64-person card is never placed over a page that says 65.
- Brand: THE ARKANSAS ECHO only. No mention of @coleworldera, AIRWEAR, or any personal account.

## Technical

- 1080×1920, 30 fps, H.264 High, yuv420p, CRF 17, +faststart, AAC 48 kHz stereo.
- Designed duration: **112.12 s.** Encoded file: **112.13 s** (3,364 frames). Finished-file loudness: **−14.0 LUFS**, LRA 2.7 LU, true peak **−3.3 dBTP**. Native render — not an upscale, not 4K.
- Burned-in gold word-by-word captions at y=1288, right limit 0.85W, MIN_SHOW 0.24 s where the next word allows, MAX_DELAY 0.12 s. Brand at y≈165, clear of TikTok / Reels chrome.
- Cover: designed still, 1080×1920, dusk Capitol photograph, hook plus “THE ARKANSAS BAR EXAM, 2020–2025” and “PROSECUTORS SAY POINTS WERE MOVED. / SHE HAS PLEADED NOT GUILTY.” Echo brand only. Not a mid-film frame and not 4K.
- QC: frames sampled from the finished MP4 at spoken-word timestamps (including 0.20 SHE, 11.97 GUILTY, 13.40 NANCIE, 22.20 65, 26.80 INNOCENT, 37.90 270, 41.50 HARVESTED, 52.50 FAILED, 63.40 64, 68.90 11,400, 83.50 FBI, 91.00 UNPRECEDENTED, 107.60 2025, 108.80 THIS, 110.60 ECHO). Caption word matched the narration at each sample. On-screen figures 65, 270, 64, and 11,400 were checked against the joint press release and the KATV affidavit reporting. See `/workspace/echo-bar-exam/qc-final/`.
