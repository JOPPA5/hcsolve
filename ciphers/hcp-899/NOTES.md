# HCP 899 — working log

## 2026-10-28: source and first pass

Root freshly inspected all three rendered HC Portal tabs and the newer AI register before delegation. The target is Not solved and absent from the bounded 158-entry register inspection. Both original scans were inspected by this solver collaborator. The address side has ordinary address and postal marks, no identified geometric cipher. The picture has two separate geometric regions: a personal upper-right message and a longer lower poem. The ordinary left-margin cursive and printed greeting are separate from the cipher.

The source image is 1024 × 680 pixels. Working crops and contrast aids enlarge existing pixels; they add no source information. The HC Portal watermark overlaps several lower glyphs and interior ticks. No higher-resolution link was observed by root; no guessed media URL or cryptogram API was used.

## Discovery and correction of hypotheses

The repeated corner shapes suggested a three-state lattice. The first proposed ICH / HABE was initially insufficient: counting tiny cellwalls as interior ticks produced nonlanguage immediately afterward. The pair-filled and simple dotted/undotted keys of HCP 962 and 995 were read as possible conventions, but neither was simply imposed here. Their frozen directories were not changed.

The successful key uses three successive letters per cell, with one, two or three interior short strokes. It retains J and adds ß as the 27th letter: ABC / DEF / GHI; JKL / MNO / PQR; STU / VWX / YZß. Distinguishing the faint left wall of U-shaped cells from interior ticks is essential. The initially anomalous upper glyph is the third-mark final cell = ß, while two extra strokes above the A are an umlaut. This produces GRÄßLICHE and a continuous personal message.

**Retired hypothesis:** an early message to root suggested SCHNUPFEN. The actual fixed-key glyph sequence is SEHNSUCHT, followed NACH DIR. SCHNUPFEN was a mistaken provisional word guess and is not retained in the transcript or decoder.

Upper personal message: ICH HABE GRÄßLICHE / SEHNSUCHT NACH DIR. / SCHREIBST DU / MIR AUCH / RECHT BALD? / 1000 KÜSSE / DEIN / HERMANN. The key was established from this region before reading the lower poem in detail. The lower source had already been visually seen during inventory and its first possible LIEBCHEN noticed, so this is a sequential check, **not a blind held-out experiment**.

## Lower block and stopping scope

The unchanged key gives clear lower fragments including LIEBCHEN, MIT DEM, ÄUGLEIN, DU MEIN LIEBCHEN, DEINER, ICH, MÖCHTE GERNE and IM TRAUTESTEN. MÜNDCHEN, MÄGDELEIN, IMMERDAR, AUF DER and KÄMMERLEIN are only provisional because some source shapes remain obscured. Other groups remain untranscribed where the watermark or faint walls obscure exact counts. No poem search, known-plaintext seed or rhyme completion was used. Root separately inspected b1-2 and b2-2 and agreed that overlapping watermark strokes prevent a reliable count there at this resolution.

The transcript records reliable words explicitly, brackets 41 provisional positions and marks the remaining seven row spans as UNTRANSCRIBED. There are 75 confirmed upper positions and 73 confirmed lower positions; there is no exact denominator for the whole source. It does not claim the unknown spans' exact glyph counts, and it does not claim complete lower-source coverage. Some word bounding boxes are approximate row ranges rather than exact glyph segmentation; the upper glyph coordinates are individually indexed.

No DONE, watcher, reviewer, PDF, FINAL or register entry was created by this collaborator. The result is partial, despite a coherent full upper message and a transferable lower key.

## 2026-10-30: lower poem completed (Claude Opus 5.5)

I re-read the whole picture side from enlarged crops (5–18×, PIL Lanczos with a contrast boost) and added a colour-weighted view, because the cipher ink is bluer than the grey watermark. The upper message was re-checked and confirmed as ICH HABE GRÄßLICHE SEHNSUCHT NACH DIR … HERMANN. The lower poem has 9 rows and 190 signs (188 after the review-1 correction, see below), and all of them are now transcribed in `work/transcript_v2.json`. `work/decode_v2.py` decodes them and checks the source hashes.

Poem as read (L4 corrected after review 1): LIEBCHEN MIT DEM ROTEN / MÜNDCHEN / MIT DEN ÄUGLEIN LIEB UND KLAR / DU MEIN LIEBES SÜSSES MÄDCHEN / DEINER DENK ICH IMMERDAR / KALT IST HEUT DER WINTERABEND / MÖCHTE GERNE BEI DIR SEIN / BEI DIR SITZEN MIT DIR KOSEN / IM VERTRAUTEN KÄMMERLEIN.

Corrections to the 2026-10-28 provisional words:
- MÄGDELEIN → MÄDCHEN. There are only five signs between Ä and the final N: ⊔1 ┘3 └2 ⊔2 □2.
- AUF DER → BEI DIR, read at 14×: ┘2 ⊔2 └3 / ⊔1 └3 ⊏3.
- IM TRAUTESTEN → IM VERTRAUTEN. The first sign is ⊓1 = V, with a clear left wall and one tick.

After rows L1–L4 had been read, I recognised the text as an adaptation of Heine's "Mädchen mit dem roten Mündchen" (Buch der Lieder, Die Heimkehr). From then on I used the poem only as a cross-check. The six places where the card differs from Heine (Liebchen, lieb, Liebchen süßes Mädchen, Kalt, möchte gerne, kosen) were all read from the signs.

The watermark covers parts of 26 signs. For most of them, the visible walls and ticks agree with the reading. Tick counts were restored by word in four cases: ROTEN t and e, KOSEN s, and DEINER d. All of these are listed in SOLUTION.md.

The 2026-10-30 scratch crops were in the session scratchpad. After review 1 the key evidence crops were regenerated reproducibly into `work/crops/` by `work/crop_evidence.py`. The left-margin cursive is not cipher and was not transcribed.

## 2026-10-30 – after review 1 (Claude Opus 5.5, solver)

- Review 1: REVISE. Finding 1 is confirmed. L4 word 3 has six signs, ⊐3 └3 ⊔2 ┘2 ⊔2 ┐1 = LIEBES (`work/crops/L4_word3_LIEBES.png`, source box x 500–675, y 455–492, 8×). The earlier token string was a copy of L1 word 1 (LIEBCHEN). That error came from the 2026-10-28 fragment list and was carried into v2 without a fresh look. `work/build_transcript_v2.py` has been fixed and `transcript_v2.json` regenerated. The decoder now reports 75 + 188 = 263 glyphs, with 26 obscured.
- Re-check against each word's own crop: L1 LIEBCHEN, 8 signs (`L1_left.png`); L3 MIT, DEN (`L3_left.png`); L8 BEI DIR SITZEN MIT (`L8_left.png`); L7 MÖCHTE GERNE (`L7_left.png`); L7/L8 right halves (`L7_right.png`, `L8_right.png`). All agree with the transcript. The restorations ROTEN T, E (`L1_ROTEN.png`) and KOSEN S (`L8_KOSEN.png`) are saved as crops. Their ticks are not visible.
