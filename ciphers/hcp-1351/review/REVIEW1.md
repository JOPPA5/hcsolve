ACCEPT

# Review 1 of hcp-1351 / pc_hcp_32 (reviewer: Claude Opus 5.5, 2026-10-30)

The reading stands. I tried to break it and could not. The only soft point is one sign, the second letter of `Xjmm`, and the solver disclosed it. The findings below are minor.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1351/work/decode.py` prints "source hashes OK", the six lines claimed in `SOLUTION.md`, and "70 cipher letters". The output matches the claimed plaintext.
2. **Independent transcription and decryption.** I read the card from my own crops of `work/hires/pc_hcp_32_adr.JPG` rotated 90 degrees anticlockwise (`review/work/adr_rot.png`, `msg.png`, `a_*.png`, enlarged 4-8x, some with contrast stretch). I then typed that reading into `review/work/independent_decode.py`, which uses its own translate table. Its output: 70 letters, identical to the solver's transcription once word-final dots are removed, and the same plaintext. Shifts 0 and 2 give nothing readable.
3. **Sign-by-sign check of every word**, looked at directly:
   - `Nz` has two downstrokes in the capital, then a clear z.
   - `Efbsftu`, `Cpz`, `uxfmwf`, `up`, `ebz`, `Cf`, `Vq`, `Gspn`, `Zpvs`, `Mpwjoh`, `Hjsm`: all clear. The j dots of `Mpwjoh` and `Hjsm` are visible, and both dots of `uijoht` are visible.
   - `Xfflt` and `uijoht`: the t crossbars are present. The bar of `uijoht` lies where the tail of the last f of `uxfmwf` ends, but it is the same heavy bar as in `Xfflt`.
4. **`Mppljoh` and `Mpp`** (`a_looking_zoom.png`, `a_loo_zoom.png`). The capital has three downstrokes, like `Mpwjoh`, so it is M rather than the two-stroke N of `Nz`. Both p's have the bowl to the right of the stem. The f of `Efbsftu` and `Xfflt` has its eye to the left. The solver's claim holds. LOOKING also needs pp as a checked word, and it is the same pair of signs as the signature.
5. **`Xjmm`, second sign** (`a_will_context.png`, `a_will_zoom.png`, and the solver's `will_second_sign.png`). See finding 1. The solver's account is accurate and not forced.
6. **Key coverage.** One shift covers all 70 letters, with no leftover signs and no extra enciphered text. The picture side has only the printed caption "Wimborne Minster, Nave East". The address side has otherwise only the plain heading, the address, the print, the postmark and the pencil "3".
7. **Language and context.** This is natural English of the period and uses the same formula as the sister cards. I recomputed 16 Feb 1907 = Saturday and +12 weeks = Saturday 11 May 1907. The postmark reads 1 PM, FE 16, 07, and WIMBORNE is legible around the stamp. The recipient is the Abbott of the sister cards. hcp-1352 has the same plain heading form, "G. H. Friday". `Mpp` = LOO appears on the FINAL card hcp-1398.
8. **Sources.** `SOURCES.md` and `metadata.md` record no attached solution, and the solver says it found no published one. Nothing in the directory contradicts that.

## Findings

1. **Minor: `Xjmm` is the one sign that does not read on pixels alone, and "Why it is correct" slightly overstates this.** The evidence is as follows.
   - A horizontal link leaves X and reaches a dark junction. From that junction a loop drops to the C-shaped hook above `Mppljoh` and closes against a diagonal stroke. This fits a looped j descender, and the solver's "descender" claim is real.
   - The tails of `Xfflt` run into the junction from above, and the diagonal runs on collinear with the j of `Mppljoh` below, so the strokes cannot be fully separated.
   - No dot of its own is visible. The blotchy dot inside the loop (`a_will_context.png`, about 555,680) lies directly over the stem of the `Mppljoh` j, so it most likely belongs to that j and cannot serve as the dot of `Xjmm`. The solver does not claim it.
   - WILL is the only sensible reading. WELL gives no sentence and the other vowels (WALL, WOLL) are not supported.
   - The disclosure in Uncertainties 1 is correct. But "holds on every word here" and "with no adjustment" should carry the exception that this one sign rests on context plus form. Suggested fix in the report: say "69 letters read on form, 1 on form plus context".
2. **Minor: `Mpp` capital argument is missing.** Uncertainties 3 argues p against f but does not address M against N. On this card the three-stroke capital against `Nz` settles it, and sister hcp-1350 discloses the same question. One sentence would close this.
3. **Minor: Slovak vocative.** "Môj najdrahší chlapec" should be "chlapče" in address, as on hcp-1350. This affects the translation only.
4. **Minor: "G. H." is called plain but is not separately tested.** It stands in the same plain line as "Saturday", and under Caesar -1 it would give F. G., which means nothing. The plain status is reasonable and the sister heading on hcp-1352 supports it. The report should say it is an inference.

## Could not verify

- What "twelve weeks to-day" refers to. The future reading (11 May 1907) is the natural one, but the event is unknown, and the solver says so.
- The meaning of G. H., and whether Loo is a pet name. Both are disclosed as open.
- That no published solution exists anywhere. I ran no web search; I relied on the portal capture recorded in `SOURCES.md`.
