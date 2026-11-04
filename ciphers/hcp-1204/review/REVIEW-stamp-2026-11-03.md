CORRECTIONS

# HCP1204 stamp-box review, 2026-11-03 (Claude Opus 5.5, independent reviewer)

Subject: SOLUTION.md section "## Stamp-box message (2026-11-03)" and the type note "MASC + Steganography".

## What I checked and how

- Original: `work/hires/cpc_--_HU__HU_Rakos-Palota-Ujfalu_jolanka-59_adr.jpg` (3671x2445). `work/decode.py` was re-run. All three hashes are OK, and rows S1-S9 print as the ledger says.
- My own crops are in `review/work/stamp-2026-11-03/`, all from the original. They are: `overview.png`; `box_1x.png` / `box_2x.png` (stamp frame, original x 2740-3280, y 320-880); `row1_3x.png` … `row9_3x.png`; row-edge crops at 6x (`row2_start_6x`, `row3_start_6x`, `row4_start_6x`, `row7_start_6x`); `rows34_right_5x.png`; `row8_bol_5x.png`; and the S1 crops `row1_start_6x`, `row1_mid_5x`, `row1_0/1_red5x`, `row1_inkB-R_3x` (blue minus red ink separation), `row1_s2s3_inkB-R_6x`, `row1_gap_color6x`, `row1_gap_G6x`, `row1_gap_R6x`. I also made a column ink profile of row 1.
- I read the box sign by sign before I compared it with the ledger.

## Type change: justified

The stamp is gone. Old gum and a violet smear remain at the left edge and a grey postmark arc remains at the top. Inside the red dashed stamp frame are nine rows in the card's cipher signs. None of it is plain Hungarian, and the end of rows 3-4 runs past the frame line. So there is writing hidden under the stamp, and **MASC + Steganography** is correct. The card stays PARTIAL with no register entry, which is consistent.

## Rows S2-S9: confirmed

My own reading matches the ledger for every visible sign.

- S2: right bowl s, a smeared three-bar e (one bar clear, two more faintly visible, so the restoration is fine), three strokes m, then F r, ≡' é, bowl+cross sz, ≡ e, three strokes m. This gives *s{e}m részem*.
- S3: a violet smear, then a loop with two dots ő, wave l, two bars a, 6 b, loop o, wave l, long+short d, dotted i, and a left bowl g that runs past the frame. This gives *{r}ől a boldig*.
- S4: a smear, then dotted í, sz, o, n, gamma t, l, =' á, t, =' á, right bowl s (at and past the frame). This gives *{v}íszontlátás*.
- S5: F r, = a, sz, ≡ e, F r, ≡ e, Γ t, loop with two dots ő. This gives *ra szerető*.
- S6: faint traces, then a cross with two dots, hook k, e, d, "1"-hook v, e, s, e. This gives *{h}ű kedvese*.
- S7: a smeared crossed sign is visible (only its dots are lost), then d, v, ö, z (cross), wave l, dotted i, = a. This gives *{ü}dvözli a*.
- S8: Γ t, =' á, v, o, l, 6 b, then a loop with dot(s), then l. This gives *távolb?l*.
- S9: low-bar cross j, o, l, á, n, k, a. This gives *Jolánka*.

The restorations of e (S2), r (S3), v (S4), h (S6) and ü (S7) are each at a genuinely smeared left edge, each is the only letter that makes the word, and each is disclosed. I accept them.

## Differences (corrections)

1. **S1 "é" of *éde* is not read from the pixels (minor-major).** It is presented as read. In `row1_gap_color6x.png` / `row1_gap_G6x.png` (original x ≈ 3060-3210), the sign before *d e* is a dense two-blob smear with a dot above it. Its bars cannot be counted, and the dot could just as well be an accent on a two-bar á. The *é* comes from the word *édesem*, not from the ink. It must be marked as restored or uncertain (e.g. {é} or é?), in both the ledger and the stamp section.

2. **S1 gap: wrong size, and "válasz would fit" is not supported (minor).** From the ink profile and crops, the space between the end of the wave *l* (box x ≈ 330) and the é-blob (≈ 370) holds about one sign, at most two. The one sign that shows is three short stacked bars (an e-type sign, box x ≈ 347-368). I see no right bowl and no crossed sign there, so the *sz* of *válasz* has no support. Change "two to four signs" to "one or two signs, one showing three stacked bars". Drop the "*válasz* would fit" remark, or say the visible trace argues against it.

3. **S1 "á" of *vál* is ambiguous with e (minor).** At `row1_mid_5x.png` (box x ≈ 253-273) the sign after the "1"-hook has three short marks. The top one may be an accent (á) or a third bar (e). Either way S1 is the open word, but *vál* should be given as "v á/e l", not as a firm prefix.

4. **S1 "r t" are not individually legible (minor).** In `row1_start_6x.png` and `row1_s2s3_inkB-R_6x.png`, the restored í and the next two signs form one smeared mass. A gamma-like top hook (t) can be seen, but the F of r cannot be separated. *írtem* is consistent with the mass, and the e and m after it are clear. Still, r (and arguably t) should be disclosed as weakly read, not counted as read cleanly.

5. **Ledger and section disagree on S7 (minor).** The ledger has `{Xu'}`, and decode.py prints `{u'}dvo:zlia` (ú). SOLUTION.md says {ü}, and *üdvözli* needs ü. The token should be `{Xu"}`.

6. **S8 normalization (minor, disclosure).** The literal reads *távolböl/-ből* (loop with dots; `row8_bol_5x.png` shows dot marks, no acute), and the text normalizes it to *távolból*. That is acceptable editorially, but it should go into the "writer's forms" note next to *írtem, boldig, víszontlátás*.

## Not verified

- The exact number of signs lost in the S1 gap.
- Whether a further dot or accent is lost under the gum on the S2-S7 left-edge signs.
- The postmark date, which I cannot read either.

The link between the stamp text and main-text row 25 (*olyan idegen levelet*) I took from SOLUTION.md and did not re-read.
