# HCP 1348 / pc_hcp_29 — Caesar −1 love postcard, 8 Feb 1907, signed "Loo"

> **With love and [k]isses from [y]ours. Loo. Feb 8th 1907.**

Status: every sign on the card is read and decoded by one fixed key (28 letters). Two words carry a one-letter defect in the literal decode (disclosed below, not silently repaired). Not a published solution: portal status Not solved, nothing attached; no published solution was found in this repo's sources. I did not run a separate web search. Revised after review 1; see the last section.

## Origin

HC Portal 1348, `pc_hcp_29`. Picture side: printed "Rowlands Hill, Wimborne", no handwriting. Address side, ordinary writing: Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon (the portal's "W. Abboú" is a misreading). Postmark WIMBORNE, 10 PM, FE 8, no year struck; ½d Edward VII stamp. The handwritten date reads "Feb 8th 1907" (uncertainty 4). 8 Feb 1907 was a Friday, the day after hcp-1353 (Feb. 7th 1907, WIMBORNE 10 PM FE 7 07, same address). The portal's catalogue date 1904-02-08 is taken to be a misreading of this writer's 7. Message is on the left half; read after rotating the scan 90° counter-clockwise. Language: English.

## Cipher and key

Caesar shift: each plaintext letter is written as the next letter of the alphabet; decrypt by subtracting one (A→Z). Key taken from sister cards (hcp-1355, 1356, 1362, 1386…1407) and tested here.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext

| Ciphertext | Literal | Reading |
|---|---|---|
| Xjui Mpwf. boe. | WITH LOVE. AND. | With love and |
| jttft gspn x pvst | ISSES FROM W OURS | [k]isses from [y]ours |
| M.p.p. | L.O.O. | Loo |

English: "With love and kisses from yours. Loo. Feb 8th 1907."

Slovak: „S láskou a bozkami od tvojej. Loo. 8. februára 1907."

(The feminine "tvojej" follows the sister cards signed "your loving girl, Loo"; this card does not state the writer's sex.)

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1348/work/decode.py
```

Checks the SHA-256 of the source and hires files, decodes every token of `work/transcription.json`, checks the round trip, and prints the literal text and the reading.

## Uncertainties

1. **`jttft` = [K]ISSES.** The tail is secure: two stems with two overlapping bars (tt), looped f, a final stem with a detached bar (t), the same outline as `Ljttft` on hcp-1362. There is no separate L. The first sign is one oval-headed looped sign (`work/crops/kisses.png`, `cmp_gj.png`, `review/work/r_kiss.png`). Its wide oval and returning tail are closer to the g of `gspn` than to the narrow j of `Xjui`, and literal g would give FSSES. So the literal ISSES is itself an interpretation of that sign: j or g, with a K omitted or an L and j run together. I cannot show which. [K]ISSES is an editorial restoration resting on the tail and on `Ljttft`, not a physically visible K.
2. **`x pvst` = [Y]OURS.** The × is a plain cross, the same sign as the X of `Xjui` (and the x of `pxo` on hcp-1362), not this writer's zigzag z (`ciphers/hcp-1358/work/crops/z_my.png`), and it is written close before `pvst`. Literal W, so WOURS is not a word. Three explanations stay open: a writer's slip for z (`Zpvst` occurs on hcp-1358 and 1400), a shift in the wrong direction (Y−1 = X), or a kiss cross followed by OURS. The word boundary and the sense "from yours" are probable, not proved.
3. **`M.p.p.` = LOO.** The capital has a looped first stroke and two further downstrokes, three in all, the construction of the capital of `Mpp` on hcp-1351 (`ciphers/hcp-1351/work/crops/signature_Mpp.png`, where M has three strokes against two in `Nz`). The sender signs `Mpp` on hcp-1350, 1351, 1353 and 1398 (hcp-1352 has the same dotted form). The expansion rests on the capital plus that signature; on this card alone a two-hump N (giving M.O.O.) is not fully excluded. "Loo" as a pet name is conjecture.
4. **Year 1907.** The last digit has a left hook, a rising right arm and a long descender. Taken alone it looks like a 4, but it is the same form as the 7 in "Feb. 7th 1907" on hcp-1353, whose postmark independently gives 07 (`review/work/cmp_seven.png`). This card's postmark has no year, so 1907 rests on the handwriting and the correspondence. It disagrees with the portal's 1904.
5. **v of `pvst`.** Small knotted sign, r-like at this size (`work/crops/ours.png`), not the s of this hand. v rests on the word; literal r would give no word.
6. **w of `Mpwf`** looks like several letters, but it has the same outline as `Mpwf` on hcp-1362 (`work/crops/l1b.png`).
7. **Punctuation and small marks.** Dots after `Mpwf` and `boe`, after `M` and after each `p` (the middle one lies on the watermark S; the last is faint). They do not affect the reading. The bar after `jttft` is read as the detached bar of the final t, not a hyphen. A small dark tick above `ui` (`review/work/r_l1a.png`) is most simply the dot of the final i, but this is not established.

## Why I believe it is correct

One fixed shift, not tuned to this card, gives WITH LOVE AND … FROM … LOO: the same phrase as `Xjui Mpwf. Gspn` on hcp-1355 and 1356 and `Mpwf boe Ljttft` on hcp-1362, in the same hand (`Mpwf` and `gspn` compare closely), closed by this writer's usual signature. The two defects are limited to single letters and the card is short, so the text is confirmed by its formula rather than by length.

## Credits

All work on this number by Claude Opus 5.5 as solver, 2026-10-30. Key and comparison material come from the sister cards in this repo, some begun by the OpenAI GPT solver.

## Response to review 1

1. **Closing is `Mpp` = LOO (major): fixed.** I enlarged `review/work/r_ini.png` and compared `ciphers/hcp-1351/work/crops/signature_Mpp.png`: looped first stroke, two further downstrokes, the same capital. My N. P. P. was wrong. The transcription is now `M.p.p.`, the plaintext LOO, and `decode.py` prints it. The residual N is stated in uncertainty 3.
2. **Year is 1907 (major): fixed.** I compared the digit in `review/work/cmp_seven.png`: the same form as in "1907" on hcp-1353, whose postmark reads 07. My "clear final 4" followed the portal and ignored the writer's form. Corrected in the title, origin, translations, `work/transcription.json` and `NOTES.md`. The disagreement with the portal and the lack of a year in the postmark are stated (uncertainty 4). Confirmed that 8 Feb 1907 was a Friday.
3. **First sign of `jttft` (minor): fixed.** I agree that the oval is closer to g than to the j of `Xjui`. Uncertainty 1 now says that ISSES is an interpretation and gives FSSES. [K]ISSES stays a disclosed restoration. I removed my former separate j/g uncertainty, which claimed all three signs have the same shape.
4. **`x` (minor): fixed.** Uncertainty 2 now says that it cannot be a misread z and adds the wrong-direction shift Y−1 = X.
5. **Punctuation (minor): fixed.** Dots after `Mpwf` and `boe` and in the closing are in the transcription and uncertainty 7. The tick above `ui` is disclosed with its likeliest explanation. Reviewer's not-verified item: I opened the picture side; it carries only the printed title.

Re-run: `python3 -I ciphers/hcp-1348/work/decode.py` prints source hashes OK, 28 cipher letters, `M.p.p.` → `L.O.O.`, and date Feb 8th 1907. Key and all decoded letters of lines 1–2 are unchanged.
