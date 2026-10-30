# HCP 1381 / pc_hcp_62 — Caesar (+1) sweetheart postcard, 26 Sep 1907

Status: **whole message read, with disclosed weak points; review 1 (REVISE) addressed.** The pencil is very faint and the portal's watermark disc lies over it on the scan, so the confidence differs by word (see Uncertainties).

## Origin

HC Portal cryptogram 1381 (`pc_hcp_62`), portal status *Not solved*, no attached transcription or solution; language listed as Unknown (it is English). Picture side: printed view "Old Harry Rocks near Bournemouth", no cipher. Address side: halfpenny Edward VII stamp, postmark BOURNEMOUTH 4.30 PM SP 26 07 (agrees with the portal date 1907-09-26); addressed to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon (portal spelling "W. Abboú"; metadata left unchanged). 26 Sep 1907 was a Thursday, matching the plain heading. The message runs across the left half, card turned 90 degrees (`work/crops/full_rot.png`). Same couple as the Caesar cards hcp-1386…1407. No published solution of this card was found or used.

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the next letter of the alphabet; decrypt by subtracting one. The heading ("Hotel Thursday") and the date ("Sep. 26th 07") are in clear. `E. L.` (twice) and `M-L` are abbreviations kept literal, as on hcp-1382, 1383, 1386 and 1403.

## Transcription and plaintext (all ciphertext on the card)

| Line | Ciphertext | Literal plaintext |
|---|---|---|
| heading | Hotel Thursday (clear) | |
| 2 | Nz Pxo E. L. Cpz | MY OWN [E. L.] BOY |
| 3 | Kvtu Ibe b | JUST HAD A |
| 4 | gjof xbml | FINE WALK |
| 5 | mpwfmz xfbuifs | LOVELY WEATHER |
| 6 | J ipqf zpv bsf | I HOPE YOU ARE |
| 7 | xfmm M-L Gspn | WELL [M-L] FROM |
| 8 | zpvs Pxo E. L. Hjsm | YOUR OWN [E. L.] GIRL |
| foot | Sep. 26th 07 (clear) | |

67 enciphered letters; 6 abbreviation letters kept literal.

English: *My own E. L. boy, just had a fine walk. Lovely weather. I hope you are well. M-L. From your own E. L. girl.*

Slovak: *Môj vlastný E. L. chlapec, práve som sa pekne prešla. Nádherné počasie. Dúfam, že sa máš dobre. M-L. Od tvojho vlastného E. L. dievčaťa.*

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1381/work/decode.py
```

Checks the SHA-256 of the four image files, decodes every token of `work/transcription.json`, checks the inverse, prints the plaintext and letter counts.

## Uncertainties

Confidence by word (all pixels are in `work/hires/pc_hcp_62_adr.JPG`; crops in `work/crops/`):

- **Clear:** `Kvtu`, `mpwfmz`, `xfbuifs` (the best word on the card), `zpvs`, `xfmm`, `bsf`.
- **Good but faint:** `Nz Pxo` on line 2, `gspn`, `Hjsm` (H = two tall strokes with a crossbar, then long-slash j, curled s, m; a smudge follows at the card edge), `zpv`, `ipqf`, and the group `E. L.` on line 8.
- **Weak, read partly by fit with the surrounding words:**
  1. `Ibe` (line 3): the first sign is a tilted tall loop, and the middle one lies under a symbol of the overlay wheel. The b and e are visible through it. The first sign fits the writer's looped capital I (hcp-1382 `Ifsf`), so the word stands better than first thought; HAD is also the reading that makes sense. `work/crops/e1.png`.
  2. `b` (end of line 3): tall stroke with hook; its bowl lies under the overlay letter O of the wheel; only traces of it show.
  3. `gjof` (line 4): loop with descender, long slash, small loop, tall swash joined by a top bar. This matches the same writer's `GJOF` on hcp-1402 in form, but the individual letters are not certain. `work/crops/e2.png`.
  4. `xbml` (line 4): x and b are visible. **The m lies under the overlay letter R of the wheel** and only traces show; it is a restoration, since WALK is the word that fits. The final l is visible with a long tail. `work/crops/e3.png`.
  5. `Cpz` and the group `E. L.` on line 2: very faint. A low bowl favours E, the L is mostly lost near the overlay symbol, and C, p and z show as traces, so the shapes are read with the help of the couple's recurring formula. Sister cards fill this slot differently: `N. L.` (hcp-1364, 1368), `M- L` / `M. L.` (hcp-1347, 1365), `E.h` (hcp-1387). `E. L.` is preferred here only because of the low bowl and the matching legible group on line 8 of this card. The second letter of the line 8 group has a small foot and could be the h of `E.h`; L and h cannot be separated here (the same note stands on hcp-1382).
- **`M-L` on line 7:** one capital of three downstrokes, a short dash, then L; read M because of the three strokes (two-arched N is the form on hcp-1402). hcp-1382 and 1383 have the same group and read it M-L. N cannot be wholly excluded. The dash may be only a stop. Kept literal, and it remains open whether it is enciphered at all (shifted it would be L-K). No abbreviation here is expanded.
- Heading "Hotel" is read in clear and could not be proved from the pixels; sister cards have "C. H." here, and it could be another word. Not ciphertext.

## Why it is correct

One fixed shift gives continuous, natural English for a holiday card from Bournemouth, and the clearly legible words (`Kvtu`, `mpwfmz`, `xfbuifs`, `zpvs`, `xfmm`) decode directly with no fitting. The date and weekday check against the postmark. The opening and closing formula agrees with the sister cards, but this is only weak support: the `E. L.` of line 2 was itself read partly from that formula.

## Credits

Transcription, decoding and write-up by Claude Opus 5.5 as solver, 2026-10-30. Key and formulae were compared with the accepted sister cards (hcp-1382, 1383, 1386, 1402); no earlier work on this number. The line 7 correction came from the independent review by a separate Claude Opus 5.5 agent.

## Response to review 1

Verdict REVISE. All four findings are addressed; the key and all other words are unchanged.

1. **`Nz L.` on line 7 is `M-L` (major) — fixed; I agree.** I checked `review/work/z7.png`, `x78.png` and my own turned view `work/crops/full_rot.png`, where the group reads `M-L` even without enlargement. It has three downstrokes, no z foot, and the descender I took for the z is the ascender of the L below on line 8. My "Clear" label was an overclaim. `work/transcription.json`, the table, the counts (67 enciphered, 6 literal), both translations and Uncertainties are changed; the point now stands as an uncertainty. One correction to the review: it says hcp-1382 calls this form N, but `ciphers/hcp-1382/SOLUTION.md` now reads `M-L.` (changed after its own review, also for three feet), and hcp-1383 reads `M-L.` too. So M agrees with both cards from the same trip, and I transcribe M.
2. **`E. L.` alternatives (minor) — fixed.** Uncertainty 5 now covers line 2 only and names `N. L.`, `M- L` / `M. L.` and `E.h` with the cards. The line 8 group moved to "Good but faint", and its small-foot note (L or h) is stated.
3. **Capitals (minor) — fixed.** `Ibe` and `Gspn` are now capitals in the transcription and table. The plaintext is not affected.
4. **Wording (minor) — fixed.** "Printed" wheel wording is replaced by "overlay": the disc is the portal's watermark on the scan, not on the card. "Why it is correct" now states the circularity of the formula.

Reproduction re-run after the fix: `python3 -I ciphers/hcp-1381/work/decode.py` passes the hash checks and prints line 7 as `WELL [M-L] FROM`, with 67 enciphered and 6 literal letters.
