# Nathan Warren / first Arkansas AME Annual Conference — sources, licenses, rights

DRAFT for review. Not posted, not scheduled, not uploaded to Buffer or any platform.

Final video: `/workspace/echo-ame-1868/ame-1868-arkansas-echo-1080x1920.mp4`
Cover: `/workspace/echo-ame-1868/ame-1868-cover-1080x1920.jpg`
A/B voice file (hook only, not for posting): `/workspace/echo-ame-1868/ame-1868-voice-ab-jon-then-wade.wav` (also `.mp3`)

## Narration

- Method (final video): ElevenLabs `creative_generate_speech`, voice **“Jon — Warm, Credible, Reassuring”** (`voice_id` `zlNWXcnnZStiyXG49qLv`), model `eleven_v4`. Flow `Zm5Y2KXPR6pAlr1Rf0u6`, session `ThoxYSYPLBMeR6wciH95`, generation `w7SFGbamP14XPK9uxvNv`.
- Cost: **1,128.0 credits, 11.28 cents USD.** Estimated first at the same figure; one take generated. No plan upgrade. A prior attempt failed with a busy free-generation queue and was not charged.
- Raw speech: 79.04 s, 44.1 kHz mono (`audio/elevenlabs-jon-raw.wav` / `.mp3`).
- Final bed: 48 kHz stereo PCM, **80.59 s** (`audio/narration.wav`), two-pass loudnorm + limiter + 1.55 s pad, then a measured +1.2 dB lift. Integrated **−14.0 LUFS**, LRA 2.8 LU, true peak **−3.3 dBFS** on the bed (see QC notes for the finished MP4 measurement).
- Comparison (not used in the final video): the same script was also rendered with HeyGen `create_speech_without_player`, public voice **“Wade – Resonant & Narrative”** (`voice_id` `a3a4aa242aaf431ea8ec2c4b3bb332fa`), free turbo, model omitted, **$0.** Raw 72.636 s. A 15.25 s A/B file plays Jon’s hook first, then Wade’s, loudness-matched to about −14 LUFS. See `VOICE-AB-README.txt`.
- Word timings: faster-whisper `medium.en` on the final bed, then RMS snap and MIN_SHOW / MAX_DELAY, with spoken number expansions patched from energy bursts and prompted clip re-transcription (`ame-word-timings.json` / `.csv`, 184 display words). Display forms: **19TH**, **AME** as one on-screen word, **ONE / HUNDRED / FIFTY-EIGHT**, **THREE / HUNDRED / THIRTY-THREE**, **TWENTY-EIGHT / THOUSAND**. “Act 151” is shown as **ACT** then **151**.

## Images used on screen (source + license)

Every still is a real, public-domain archival image. No AI faces. No invented portrait of Nathan Warren. No cotton imagery. Native 1080×1920 render — not labeled 4K. A Lanczos enlargement of a real scan is still that scan; it is not called restored.

1. **Bird’s-eye view of Little Rock, 1871**, drawn by A. Ruger (`images/littlerock-1871-birds-eye.jpg`). Library of Congress, item [73693338](https://www.loc.gov/item/73693338/). U.S. work published 1871; public domain. On-screen credit: “Bird’s-eye view of Little Rock, 1871. A. Ruger. Library of Congress. Public domain.” Used for the hook, the 1819 / Crittenden beat, a dimmed ground under the Act 151 card, Bethel / Shorter College, the hometown question, the brand card, and the designed cover. The lithograph is a two-sheet fold with a binding gap at about 0.681 of the full width; the renderer keeps only the left sheet so the slit is never framed. The view is dated 1871 — after 1819 and after 1868 — and is not presented as a picture of those earlier years. The credit carries the date.

2. **Markham Street, Little Rock, looking west from Main, 1900–1910**, Detroit Publishing Company (`images/markham-st-1900s.jpg`). Library of Congress, item [2016815280](https://www.loc.gov/item/2016815280/). Public domain (Detroit Publishing / LOC). On-screen credit: “Markham St., Little Rock, looking west from Main, 1900–1910. Detroit Publishing Co., Library of Congress. Public domain.” Used when the narration turns to Warren as “Little Rock’s Confectioner” and to the ban on free Black residents. A small on-screen note reads “HIS SHOP STOOD ON THIS STREET.” The shop is not claimed to be visible in this photograph, which was taken decades later; the Capital Hotel tower in the view is a landmark on the same street, not identified as the shop itself.

3. **“Mustered out” Colored Volunteers at Little Rock**, sketched by Alfred R. Waud, published in *Harper’s Weekly*, May 19, 1866 (`images/waud-mustered-out-1866.jpg`). Library of Congress, item [2009630216](https://www.loc.gov/item/2009630216/). U.S. work published 1866; public domain. On-screen credit: ““Mustered out” Colored Volunteers at Little Rock. A. R. Waud, Harper’s Weekly, May 19, 1866. Library of Congress. Public domain.” Used for the return-as-a-minister / first congregation beat. This is a Reconstruction-era Little Rock scene, **not a portrait of Nathan Warren**, and is not captioned as one. The printed Harper’s caption is left visible in the crop.

4. **“Bishops of the A.M.E. Church,”** lithograph by J. H. Daniels, Boston, 1876 (`images/ame-bishops-1876.jpg`). Library of Congress, item [98501269](https://www.loc.gov/item/98501269/); production file from the Wikimedia Commons scan, [File:Bishops_of_the_A.M.E._Church_(19555907914).jpg](https://commons.wikimedia.org/wiki/File:Bishops_of_the_A.M.E._Church_(19555907914).jpg), cropped to the print (wooden frame removed). U.S. work published 1876; public domain. On-screen credit: ““Bishops of the A.M.E. Church,” J. H. Daniels, Boston, 1876. Library of Congress. Public domain. Not a portrait of Nathan Warren.” Used for the November 19, 1868 conference beat and the 1890 membership numbers. The printed title “BISHOPS OF THE A.M.E. CHURCH” is kept fully in frame.

5. **Bishop James A. Shorter**, oval from the same 1876 lithograph (`images/bishop-shorter-1876.jpg`). A 3.5× Lanczos crop of the Shorter oval, including the printed name “JAS A. SHORTER,” with slivers of neighboring ovals left in as honest group-lithograph context. Public domain, same source as (4). On-screen label: **“BISHOP JAMES A. SHORTER.”** On-screen credit: “Bishop James A. Shorter, from the 1876 AME bishops lithograph. Library of Congress. Public domain. Not a portrait of Nathan Warren.” Shown only while the narration names him. This is a Lanczos enlargement of a real scan, not a restoration and not 4K.

6. **Act 151 card** (designed type, not a photograph). The on-screen title “AN ACT TO REMOVE THE FREE NEGROES AND MULATTOES FROM THIS STATE” is the official title of Act 151 of 1859 as given by the Encyclopedia of Arkansas. The card is clearly designed — a dark panel over a dimmed still — and is **not a facsimile** of the original printed act. On-screen credit: “Act title from Act 151 of 1859, as given by the Encyclopedia of Arkansas. Designed card; not a facsimile of the original printed act.”

## Images researched and not used, and why

- Encyclopedia of Arkansas portrait of Nathan Warren. Credited “Courtesy of James ‘Butch’ Warren.” A courtesy photograph is not treated as cleared. Not used. No substitute face was generated.
- Frontispiece or portrait in A. W. Wayman, *Cyclopedia of African Methodism* / *Life of Rev. James A. Shorter* (1890; Internet Archive `lifeofrevjamesal00waym`, Duke PDF). The scanned volume had no usable portrait; the largest plate in the Duke PDF is the back cover. The 1876 lithograph oval was used instead.
- Library of Congress 1890 Shorter-related page scans (cover, not a portrait).
- Modern photographs of Bethel AME at 815 West 16th Street, Little Rock. The congregation moved there in 1970; the 1875 Campbell Chapel building at 9th and Broadway is not claimed to be still standing, and a modern church photograph was not used.
- Any cotton-field or plantation stock. Not used.

## Fact sources for the narration (claim by claim)

Pages were opened and re-checked on November 13, 2026 (America/Chicago). Where the Encyclopedia of Arkansas (AME entry) and the Arkansas Heritage blog conflict, the conflicting detail is omitted rather than guessed. The November 19, 1868 conference date is taken from the EOA AME entry, as assigned.

- **“They brought Nathan Warren to Arkansas enslaved.”** / **“In 1819, Robert Crittenden, the first secretary of the Arkansas Territory, brought him here enslaved.”** CALS Encyclopedia of Arkansas, “Nathan Warren,” and “African Methodist Episcopal Church”: Warren was brought to Arkansas in 1819, enslaved, with Robert Crittenden, first secretary of the Arkansas Territory. The Heritage blog agrees on 1819 and Crittenden. https://encyclopediaofarkansas.net/entries/nathan-warren-4457/ https://encyclopediaofarkansas.net/entries/african-methodist-episcopal-church-5358/ https://www.arkansasheritage.com/blog/dah/2021/12/08/african-american-branches-of-the-methodist-church-in-arkansas
- **“Warren later lived in Little Rock as a free man — known as Little Rock's Confectioner.”** Warren EOA: he lived in Little Rock as a free man and was known as “Little Rock’s Confectioner.” The voiceover does not give a year for his emancipation, or a method, because sources do not agree on the surrounding chronology (see omitted facts).
- **“Then white agitators pushed a ban on free Black residents.”** EOA, “Act 151 of 1859,” and the Warren entry: a campaign by white Arkansans produced a statutory ban on free African American residence. “Agitators” is the short’s wording for that documented campaign, not a quoted label from 1859. https://encyclopediaofarkansas.net/entries/act-151-of-1859-4430/
- **“In 1859, Act 151 ordered free African Americans out of Arkansas, or be sold into slavery for a year.”** EOA, “Act 151 of 1859”: Act 151, approved February 12, 1859 (Governor Elias N. Conway), required free African Americans to leave the state by January 1, 1860, or be subject to hire / sale into slavery for one year, with proceeds used toward relocation. The voiceover states the 1859 act, the expulsion order, and the one-year sale; it does not recite the January 1, 1860 deadline or the governor’s name, which the short did not need. Official Acts of Arkansas independently confirm the statute. The on-screen official title is taken from the EOA Act 151 entry.
- **“Warren had to leave.”** Warren EOA and the Heritage blog agree that Warren left Arkansas under this regime. The year and destination of that departure are in conflict and are omitted (see below).
- **“He returned during the Civil War as a minister, and led the state's first A.M.E. congregation.”** Warren EOA and the AME EOA: he returned during the Civil War (EOA: 1863) as a minister and led the state’s first AME congregation. The voiceover says “during the Civil War,” not a precise year, and does not pick a church founding year among the conflicting 1863 / 1866 / 1875 dates.
- **“Bethel A.M.E. in Little Rock grew from that work.”** AME EOA and the Heritage blog: Bethel AME in Little Rock grew from Warren’s early congregation. The short does not say the 1875 Campbell Chapel building is still standing, and it does not use a modern church photograph.
- **“So did Bethel Institute, the school we now call Shorter College.”** AME EOA and the Heritage blog agree that Bethel Institute, now Shorter College, grew from this AME work. Founding and first-class years conflict (1886 in EOA; first classes around 1875 in some accounts) and are omitted. The school is named; no year is given.
- **“On November 19th, 1868 — one hundred fifty-eight years ago next week — Arkansas held its first African Methodist Episcopal Annual Conference, under Bishop James A. Shorter.”** AME EOA: the first Arkansas AME Annual Conference was held on November 19, 1868, under Bishop James A. Shorter. The Heritage blog says November 1868 without a day; the assigned rule is to use EOA for this date. “One hundred fifty-eight years ago next week” is correct for a November 13, 2026 sitting: the anniversary falls on Thursday, November 19, 2026. Bishop Shorter is identified on screen by the printed “JAS A. SHORTER” on the 1876 lithograph and by the label “BISHOP JAMES A. SHORTER.” The 1876 print is not presented as an 1868 conference photograph.
- **“By 1890, the church had three hundred thirty-three congregations in this state, and nearly twenty-eight thousand members.”** AME EOA: an 1890 census counted **333** churches and **27,956** members in Arkansas. The Heritage blog’s round figure is about 28,000. The voiceover uses the exact congregation count and “nearly twenty-eight thousand members.”
- **“Does your family attend Bethel A.M.E., or an A.M.E. church anywhere in Arkansas? That's your history.”** A hometown-memory prompt, not a subscribe CTA. Bethel AME remains a living Little Rock congregation (now at 815 West 16th Street; the move itself is not in the voiceover).

## Facts researched and intentionally omitted or softened

Where sources conflict, the short omits the detail rather than choosing a side or introducing a third source as a tie-breaker.

- **Departure year and destination.** The AME EOA entry says Warren left in 1856 for Washington, D.C. The Heritage blog says 1857 and Xenia, Ohio. The dedicated Warren EOA entry places a Xenia departure after February 1859 (Act 151). All three cannot be shown as a single fact. The voiceover says only that Warren had to leave.
- **Birthplace.** The AME EOA entry has him reared in Washington, D.C. The Warren EOA entry has him born in 1812 in Versailles, Kentucky. Omitted.
- **Method of emancipation.** Not stated, because it sits inside the same unsettled pre-1859 chronology.
- **Church founding and building years** (a congregation after the 1863 return; Heritage’s 1866 Bethel and Carter’s Chapel; construction “three years later”; the 1875 dedication of Campbell Chapel). The voiceover says he led the state’s first AME congregation and that Bethel AME grew from that work, without a year.
- **Bethel Institute / Shorter College dates** (EOA 1886 founding; accounts of first classes around 1875). The school is named; the year is not.
- **“In 1868, the A.M.E. Church was organized in Arkansas under Reverend Nathan Warren”** (Heritage). The short follows EOA: the first Annual Conference on November 19, 1868, under Bishop James A. Shorter. Warren’s role is told in the earlier congregation work, not as a substitute for Shorter’s presidency of that conference.
- **Warren as an elder on November 19, 1882** (Warren EOA). That is a different November 19, fourteen years later. Not used, so it cannot be confused with 1868.
- **Scipio Jones, Daisy Bates, and members of the Little Rock Nine who had AME ties** (AME EOA). True, and already represented in this archive. Left out to keep the short on one person and one surprising fact.
- **The 1875 building at 9th and Broadway is still standing.** It is not claimed. Bethel moved to 815 West 16th Street in 1970.
- A Magnolia Reporter on-this-day item that repeats the November 19 date was labeled as ChatGPT-collected and was not treated as an independent source.

## Technical

- 1080×1920, 30 fps, H.264 High, yuv420p, CRF 17, +faststart, AAC 48 kHz stereo.
- Designed duration: **80.59 s.** Encoded file: **80.60 s** video (2,418 frames), audio 80.59 s, 1080×1920, H.264 High, yuv420p, CRF 17, +faststart, AAC 48 kHz stereo. Finished-file loudness: **−14.1 LUFS**, LRA 2.8 LU, true peak **−3.0 dBFS**. Native render — not an upscale, not 4K. See QC notes.
- Brand: THE ARKANSAS ECHO only. No mention of @coleworldera, AIRWEAR, or any personal account.
- Burned-in gold word-by-word captions at y=1288, right limit 0.85W (918), MIN_SHOW 0.24 s where the next word allows, MAX_DELAY 0.12 s. Brand at y≈165.
- Cover: designed still, 1080×1920, 1871 Ruger view, hook lines “ARKANSAS RAN HIM OUT FOR BEING FREE. / HE CAME BACK A MINISTER.” plus “NOVEMBER 19, 1868” and “ARKANSAS’S FIRST AME ANNUAL CONFERENCE.” Echo brand only. Not a mid-film frame and not 4K.
