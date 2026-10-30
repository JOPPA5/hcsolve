ACCEPT

# Review 1 of hcp-1382 (pc_hcp_63) — Claude Opus 5.5, reviewer, 2026-10-30

The reading stands: Caesar −1, 40 enciphered letters, one key, all seen on the pixels. "only. Wish you. Were Here as. Well." and "From Your Own … Girl" are correct. I tried to break it and could not. Five minor findings remain. Finding 1 changes one literal sign and should be fixed before FINAL. None changes a deciphered letter.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1382/work/decode.py` ran. Hashes OK (also recomputed with `shasum -a 256`, all four match SOURCES.md). Output equals the table in SOLUTION.md. 40 enciphered letters, a count I confirmed independently. 24 Sep 1907 was a Tuesday.
- **Independent decode.** `review/work/own_decode.py`, own mapping table, typed from my own reading of the scan. Output: ONLY. WISH YOU. / WERE HERE. AS. / WELL. [M-L.] FROM / YOUR OWN [E.L.] GIRL. 40 letters. It differs from the solver only in findings 1 and 2.
- **Transcription.** Rotated `work/hires/pc_hcp_63_adr.JPG` 90° CCW and flattened the overlay with my own filter (`review/work/crops.py`, `norm.png`), then 3–7x crops (`crops3.py`, `crops4.py`). All eight rows were read sign by sign.
  - Clear with no doubt: `pomz.` (the long slash is the p stem, as the solver says; no letter precedes it), `Xfsf`, `Ifsf`, `bt.` (b looped, t with detached bar, dot), `Xfmm.` (six minims after f), `Gspn`, `Zpvs`, `Pxo` (P with the arc, same form as hcp-1383), `Hjsm`, `24th Sep 07`, `Tues. Morning`, `I am enjoying`, `myself`.
  - `Xjti`: X, long slash j, stem t curving into the low i. The t bar stands well to the right of its stem, as the bar of `bt.` does. The small heavy mark above the i is in the right place for its dot (`z_ijti.png`). Good.
  - `zpv.`: z under the printed R is a real z form with the two strokes of its top and foot visible; p long stem and bowl, v, dot (`z_zpv.png`). Good.
  - X is a capital in all three places; no kiss marks.
  - `G. H.` (row 1): oval and stem, then two faint stems (`r1end.png`). Acceptable; the disclosed "flourished" wording is fair. G or C cannot be separated here, as on the sisters.
- **"Dear" (row 3).** Raw and flattened crops (`z_dear_raw.png`, `r3end.png`). Large faint initial, about three low letters, a tail. No ascender. D-e-a-r fits and nothing excludes it, but the pixels alone do not prove it. It is correctly labelled probable and is marked `[?]`. I could not find a better reading.
- **Restorations.** No completion section; nothing is restored. `Dear` is the only word helped by sense, and it is disclosed.
- **Key coverage.** One shift, no exceptions. Only the two abbreviations (4 letters) stay outside it, and both are disclosed.
- **Language and context.** Natural period English. Plain opening runs into the cipher as one sentence. Postmark BOURNEMOUTH SP 24 07 confirmed; the hour is consistent with 12.45 PM (the middle sign is cross-like, `z_pm2.png`). Halfpenny Edward VII stamp, printed title "Christchurch Priory. Norman Turret.", no. 23241 confirmed. Sister groups checked in their SOLUTION.md: `pomz` on hcp-1383, `Zpvs Pxo … Hjsm` on hcp-1381 and hcp-1386, `E.h` on hcp-1387, `N-L` on hcp-1402.
- **Sources.** Portal status Not solved and no attachment, per metadata.md. No sign of a published solution being used. The number is not in skip.txt or register-exclusions.json.

## Findings

1. **minor — the first sign of `N-L.` (row 6) is the M form, not N.** In `z_N.png` it has three feet: a long diagonal up into an arch, down to a second foot, then a separate short third stroke. This is the shape read `M-L.` on hcp-1383, written the day before from the same town (`hcp-1383/review/work/z_ml.png`). The N of `Nz` there has two feet (`z_nz.png`). The same three-downstroke rule gives M on hcp-1347, 1361 and 1365. Part of the top is tangled with the descender loop of the f of `Ifsf`, so N is not wholly excluded, but the feet are clear of it. Fix: transcribe `M-L.`, change decode.py, the table, the English and Slovak lines, and uncertainty 2 (its appeal to hcp-1402 no longer serves; that card's own note says M is not excluded). I did not re-examine the 1402 pixels. No sense changes, because the group is unexplained.
2. **minor — a dot is missing in row 5.** There is a clear dot after `Ifsf`, on the line, before `bt.` (`r5b.png`, also visible in the solver's own `rot2x.jpg`). SOLUTION.md uncertainty 5 says dots are "transcribed as seen". Fix: `Xfsf Ifsf. bt.` in the table, decode.py and the plaintext.
3. **minor — the address omits "S."** The large stroke before `Devon` is an `S`, as on hcp-1387 ("S. Devon"). Plain field; no effect on the reading.
4. **minor — "no handwriting" on the picture side needs a word.** There is a small dark mark in the sky at the lower left, a blob, two rings and short strokes (`z_picmark.png`). It looks like set-off from a postmark, not writing, and holds no message text that I can see. State that it was seen and set aside.
5. **minor — wording under "Why it is correct".** "with no exceptions and no word forced" sits beside a claim that `zpv` "needs that letter". This is harmless, since the shape does support z. But "you" being needed is a sense argument and should be kept apart from the shape evidence. Also, "E.L." shifted gives "D.K" and the sister `E.h` gives "D.g"; it remains open whether the group is enciphered at all, which uncertainty 2 already says in part.

## What I could not verify

- The meaning of `M-L.` and `E.L.`, and whether either is enciphered. The second sign of `E.L.` is an L or h: it has the same small foot as the sign on hcp-1383 (`z_EL.png`, `z_el_end.png`), and I cannot decide it. The solver discloses this.
- "Dear" beyond "probable".
- G against C in the heading.
- The postmark minute beyond "consistent with 45".
- The picture-side mark's origin.
