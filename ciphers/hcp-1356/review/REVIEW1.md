ACCEPT

# Review 1 of hcp-1356 (pc_hcp_37) — Claude Opus 5.5, 2026-10-30

The reading stands: Caesar −1, "My own dearest boy, many thanks for all this morning. With love from your girl." I tried to refute it and could not. Only minor disclosure points remain.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1356/work/decode.py` ran clean: all 4 hashes OK, round trip OK, 62 letters (2 restored, 60 read). Output is identical to the table in SOLUTION.md.
- **Independent decode.** `review/work/verify.py` holds my own transcription, typed from my crops and not from theirs, and uses its own shift code. It gives `MY OW? DEAREST BOY MANY THANKS FOR ALL THIS MORNING WITH LOVE FROM YO?R GIRL`, 60 letters + 2 blots. Only shift 1 of the 26 gives language. The key is one fixed shift, so it covers everything, with no exceptions.
- **Transcription against pixels.** I cropped `work/hires/pc_hcp_37_adr.JPG` myself, rotated 90° CCW, at 2x to 8x (`review/work/msg2x.png`, `l1a`…`l5b`, `mpwf`, `stu_cpz`, `nboz`, `bmm`, `hjsm`, `blot1`, `blot2`). I checked every letter of all five lines, not a sample, and every separator dot. All dots in `transcription.txt` are on the card, and I found none missing.
- **Signs checked for a reading that could change the text.**
  - `N` in `Nz` and `Nboz` has two downstrokes; `M` in `Mpwf` has a third short stroke running into the `p`. The solver's claim holds. Reading N there would give a non-word anyway.
  - `bmm` shows about six downstrokes after the `b`, which fits two three-stroke m's. There is no third m.
  - `uibolt`: a dot stands over the i, and b, o, l, t are all distinct.
  - `uijt`: both dots stand high above, on the overlay ring.
  - `npsojoh`: the dot over the j is present, and the δ-shaped `o` is as the solver describes.
- **Restorations.** I contrast-stretched both blots at 8x (`blot1.png`, `blot2.png`) and found no letter structure in either, so both are real restorations and are labelled `[x]`. Neither is forced beyond what the frame gives: OW? and YO?R each have one sensible completion here, and a one-letter gap fits both.
- **Stray marks.** The smears under `Ef` and above `Mpwf`, the blot on the `g` of `gps`, and the dot under `uibolt` are not letters. None of them adds or removes a sign.
- **Context.**
  - Python calendar: 24 Mar 1907 was a Sunday, 25 a Monday, 26 a Tuesday.
  - On the scan the postmark reads WIMBORNE 10 PM MR 25 07, and the portal date is 1907-03-25.
  - Picture side: Wick Ferry, Christchurch, J.V. 46288, no handwriting.
  - The address agrees with the Stokelake Farm cards (hcp-1380, 1386, 1387).
  - The date digit is a loose 4 with a crossing stroke. The solver's 24 stands, and the 6-like look is disclosed.
- **Language.** Natural Edwardian love-card English. "Mpwf gspn … Hjsm" and "Many thanks … for all" have parallels in hcp-1397 and hcp-1387. The elliptical "all this morning" is disclosed as such.
- **Sources.** Portal status Not solved, nothing attached. No sign of a published solution. 1356 is not in skip.txt or register-exclusions.json.

## Findings

1. **minor. `s` of `Zp[v]s` and final `m` of `Hjsm` are partly smeared and this is not disclosed.** The lower half of the `s` is a blob (`blot2.png`); only its top hook is clear. The `m` of `Hjsm` is clotted (`hjsm.png`). Both are still legible enough, and the frame YO?R and GIRL settle them, but "60 read directly" slightly overstates things and the Uncertainties section should name them.
2. **minor. The hcp-1397 parallel is normalised.** SOLUTION.md quotes "Mpwf gspn Zpvs Pxo Hjsm" as a formula. hcp-1397 has `wjfx Mpwf gspn / zpvs. Pxo. Hjsm.`, with a line break, lowercase `zpvs` and dots. This has no effect on the reading, but the quote should match the sister card.

## What I could not verify

- The letters under the two blots. No scan can show them.
- What "all" refers to, and who the writer was.
- The Wick Ferry caption is partly under the scan overlay, but it is legible enough.
