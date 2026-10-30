REVISE

# HCP 899 – Review round 1 (reviewer: Claude Opus 5.5, 2026-10-30)

## Summary

The cipher type, the 27-letter three-per-cell Pigpen key and the overall reading (upper love note signed Hermann; lower poem adapted from Heine's "Mädchen mit dem roten Mündchen") are correct. I could not refute the key or the poem as a whole. However, one word in poem row L4 is wrong, and that error matters: the third word of L4 has **6 signs, not 8**. It reads **LIEBES**, not LIEBCHEN. The card therefore reads "Du mein liebes, süßes Mädchen", which is closer to Heine ("Du mein liebes, kleines Mädchen") than the solution claims. The solution presents "Liebchen" as one of six card variants "all read from the cipher signs". For this word the claim is false, and the token string in the transcript is a verbatim copy of L1 word 1. The glyph counts, plaintext, translations and variant list must be corrected. The reading stands, so the verdict is REVISE rather than REJECT.

## What I verified and how

1. **Solver's command.** `python3 ciphers/hcp-899/work/decode_v2.py` (from the repo root). The source hashes check out, and the output matches the claimed plaintext exactly. It reports 75 + 190 = 265 glyphs and 26 obscured.
2. **Independent decoder.** `review/work/indep_decode.py` rebuilds the key from the stated rule alone: 9 shapes in the order br, lbr, bl, tbr, box, tbl, tr, tlr, tl, three letters each, A–Z with J plus ß. It does not use the solver's key dict. Its output is identical to the solver's for all rows. The key is a bijection, and every token in `transcript_v2.json` is covered.
3. **Scan checks.** I made my own crops at 5–14× (`review/work/crop.py`, PIL Lanczos with a contrast boost; crops are in `review/work/*.png`). Note that the poem rows slope down to the right by roughly one row-height across the block. Crops taken at a fixed y pick up the neighbouring row on the right side. I fixed this with tall crops (`RR1.png`, `RR2.png`) and assigned the rows from those.
   - Upper message, sample: ICH HABE (`u1a.png`), GRÄßLICHE (`u1b.png`), KÜSSE / DEIN / HERMANN (`up3.png`). Shapes and tick counts agree with the transcript.
   - L1 LIEBCHEN MIT DEM (`L1l.png`): 8 + 3 + 3 signs, agrees. ROTEN (`L1roten2.png`): ⊏3, □3 and the final □2 are visible. Two signs lie under watermark "GPO", and their ticks cannot be seen. The restoration is disclosed and is space-consistent (two sign widths).
   - L2 MÜNDCHEN (`L2m.png`): □1, ┐3 with umlaut, □ and ⊔ under the watermark, then ┘3 └2 ⊔2 □2. Agrees, 8 signs.
   - L3 MIT DEN ÄUGLEIN (`L3a.png`), the end of ÄUGLEIN and the first sign of LIEB = ⊐3 (`L3lieb.png`), UND KLAR (`R1.png`, `L4c.png`). Agrees. The first sign of LIEB is clearly ⊐ (L), so Heine's "süß" is excluded.
   - **L4** (`L4l.png`, `L4w3.png`, `L4n.png`, `L4s.png`, `L4m.png`): DU, MEIN, SÜSSES (┐1 ┐3̈ ┐1 ┐[obscured] ⊔2 ┐1) and MÄDCHEN (□1 ┘1̈ ⊔1 ┘3 └2 ⊔2 □2) agree. Word 3 does not (Finding 1).
   - L5 DEINER DENK ICH (`L5l.png`, `L5m.png`) and IMMERDAR (`L6w3.png`, `L6w4.png` bottom row; └3 □1 □1 ⊔2 ⊏3 ⊔1 ┘1 ⊏3). Agrees. The DEINER first sign is ⊔ with a heavy stroke, and D is the reasonable reading.
   - L6 KALT IST HEUT (`L6l.png`) agrees. DER WINTERABEND (`L6win.png`, `L6abend.png`): ⊔1 ⊔2 ⊏3 / ⊓, then signs under watermark "S/3", then ┐2 ⊔2 ⊏3 ┘1 ┘2 ⊔2, □ and ⊔ under "P/D". Consistent, with a partly obscured start and end, as disclosed.
   - L7 MÖCHTE GERNE (`L7l.png`) and BEI DIR SEIN (`L7sein.png`). Agrees.
   - L8 BEI DIR SIT(Z)EN (`L8l.png`): ┌2 = Z is visible. KOSEN (`L8kosen.png`): ⊐, □3 visible; the third sign is under watermark "T" (restoration disclosed); ⊔ and □2 follow. Consistent.
   - L9 IM VERTRAUTEN (`L9l.png`): the first sign has a left wall, a top and a right wall (⊓) with one tick, so V. Agrees. The end of KÄMMERLEIN (`L9kam.png`) is consistent.
4. **Language and context.** The text is fluent German of c. 1900. The rhyme pairs are Mündchen/Mädchen, klar/immerdar and sein/Kämmerlein. The date, the winter evening, Bodenwerder → Hameln (both on the Weser) and "Fräulein Johanne Stiebe" on the address side (checked on `source/address.jpg`) all fit.
5. **Sources.** The Heine source is disclosed in SOLUTION.md and SOURCES.md as a literary source, not as a decipherment. The portal lists no solution, and earlier GPT work is credited.

## Findings

1. **[major] L4 word 3 is LIEBES (6 signs), not LIEBCHEN (8 signs).** At 9× (`review/work/L4w3.png`, x 505–670, y 458–488 of `source/picture.jpg`) there are exactly six signs between the slash after MEIN and the slash before SÜSSES: ⊐3 └3 ⊔2 ┘2 ⊔2 ┐1. The last sign is clearly a ┐ (top bar plus right wall, no bottom) with one tick. It is not a □2, and no ┘3/└2 (C, H) signs are present. In `build_transcript_v2.py` this word is `tbr3 bl3 lbr2 br2 br3 bl2 lbr2 box2`, character for character the same as L1 word 1, so it was apparently copied, not read. The error goes back to the 2026-10-28 GPT notes ("DU MEIN LIEBCHEN" listed as a clear fragment) and was carried into v2. Consequences that must be fixed:
   - the plaintext ("du mein liebes, süßes Mädchen") and the English and Slovak translations
   - the glyph totals: lower 188, total 263 (if nothing else changes)
   - the "six variants all read from the signs" paragraph: the card agrees with Heine's "liebes" here, and only "süßes" replaces "kleines"
   - the "Why this is correct" bullet, which cites "süßes Mädchen" variants
   - NOTES.md
2. **[minor] The over-strong claim "every variant was read from the signs, Heine used only as a cross-check" is undermined by Finding 1.** Since one word was evidently filled in from L1 rather than read, the solver should re-confirm the remaining Heine-divergent words against the scan and say so explicitly. I checked them and they hold: LIEB (first sign ⊐3), KALT (⊐2 ┘1 ⊐3 ┐2), MÖCHTE GERNE, KOSEN (K, O, E, N visible; S restored) and SÜSSES. The solver should also re-check every other word whose token string duplicates another word's (e.g. MIT, BEI, DIR, DEN/DEIN) against its own crop, not by copying.
3. **[minor] The restorations are disclosed, but their basis is partly linguistic.** ROTEN T/E and KOSEN S are filled by the only fitting word, with the Heine text in the background. That is acceptable and disclosed, but the report should state plainly that these three letters are not visible on the scan and that the poem was known when they were restored.
4. **[minor] Reproducibility of the crops.** NOTES.md says the solver's crops are in the session scratchpad and not in `work/`. A reader cannot see the evidence for the 26 obscured-sign decisions. The key crops (at least the four restorations and the corrected L4 word) should be saved in `work/`.

## What I could not verify

- The tick counts of signs fully under the watermark (ROTEN T/E, KOSEN S, the first signs of WINTERABEND, KÄMMERLEIN M-E-R). I can see only that the shapes and spacing are consistent with them. The scan is 1024 × 680, and no higher-resolution image is available.
- Every tick of every upper-message sign. I checked a sample, and the decoded text is fully fluent, so a residual error there is unlikely.
- Whether "kosen" / "Kalt" / "süßes" reflect a printed popular variant of the Heine text or the writer's own changes. This does not affect the decipherment.
- The left-margin cursive and "Frau von Blum(?)" on the address side are plain text and outside the cipher. I did not review them.
