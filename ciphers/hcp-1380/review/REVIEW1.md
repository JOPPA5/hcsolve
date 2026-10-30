ACCEPT

# Review 1 of hcp-1380 (pc_hcp_61)

Reviewer: Claude Opus 5.5, 2026-10-30. The reading stands. The four findings below are all minor. They concern how individual signs are described, not the words read.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1380/work/decode.py` ran clean. All 4 hashes passed, 97 letters decoded, and the output matches the SOLUTION.md table line by line.
2. **Hashes against SOURCES.md.** decode.py asserts the same four SHA-256 values listed in SOURCES.md.
3. **Independent decryption.** `review/work/indep.py` holds my own transcription, typed from my own crops, and its own shift code. It gives 97 letters and 25 tokens. The only token that differs from the solver's is `bcpvu` against `bepvu` (finding 1). Plaintext: MY DEAREST I AM VERY SORRY ABOUT NEWS IN CODE & HOPE YOU WILL TAKE GREAT CARE BY VERY SPECIAL REQUEST YOUR OWN LOVING GIRL.
4. **Removing the wheel watermark.** The wheel is the portal's overlay and sits at the same pixels on every scan. `review/work/wm.py` takes the pixel median of 25 other address sides of the same size. `review/work/flat.py` divides this card by that median, giving `review/work/flat.png` and `flat2x.png`. The solver did not have this view. It makes the pale letters much easier to separate from the wheel.
5. **Sign-by-sign check** on `flat.png` and the raw hires (crops in `review/work/`, 4–8×). I checked every word of the card, with close zooms on `Efbsftu`, `bn`, `wfsz`, `Tpss.z`, `bepvu`, `Jo`, `dpef`, the `&`, `ipqf`, `xjmm`, `Zpvs`, `pxo`, `mpwjoh` and `Hjsm`, and whole-line views of lines 5–7. Each letter is present in the ink, apart from findings 1–3.
   - `Tpss` starts with the barred T form seen in `ofxt` and `tqfdjbm`.
   - `xjmm` shows about six minims.
   - The tall sign in `ublf` is the looped `l`.
   - `Jo` has the J hook and a pale `o` with a dark top.
   - No letter in this card is restored from context. The solver's statement to that effect holds, apart from the shape issues in findings 1 and 3.
6. **The sign after `dpef` (the solver's uncertainty 5).** I tested whether it could be a wheel symbol. The median shows only the wheel's `Q` and ring in that area, with no loop or stem (`review/work/amp_vs_wm.png`). So the sign is ink on this card. Its structure (loop, crossing stem, horizontal tail) matches the `&` on sister card hcp-1373 (`ciphers/hcp-1373/work/crops/w_and.png`). The doubt in uncertainty 5 can be closed.
7. **Key coverage.** All 97 letters use the one shift, and 21 letters of the cipher alphabet occur. The key is the same Caesar −1 as the accepted sister cards. It was checked on this card, not assumed.
8. **Context.**
   - Postmark enlarged (`review/work/pm2.png`): WIM…, 10 PM, AP 6, 07. The 6 and 07 fall on the stamp but are legible.
   - 6 April 1907 was a Saturday, matching the plain heading "Sat: afternoon" and the portal date.
   - The address reads Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.
   - Same hand and correspondence as hcp-1379 (Wimborne, 9 April 1907), three days later.
   - "My dearest" and "your own loving girl" are the couple's usual formula. The language is period English with no forced words.
9. **Disclosure.** The sense of "news in code" is marked as interpretation. The ampersand is marked literal. The bepvu residual is disclosed. The portal has no solution or transcription attached.

## Findings

1. **minor. The second sign of `bepvu` is most likely this writer's `c`, so "ADOUT" overstates the problem.**
   - Evidence: the upper lobe of the sign is a solid ink wedge with no visible counter (`review/work/raw_be2.png`). The "closed loop" SOLUTION.md describes is not visible. The same word on sister hcp-1359 (`ciphers/hcp-1359/work/crops/z_about.png`) has a very similar `c` with a heavy top flag, which that card reads as `bcpvu`.
   - SOLUTION.md says there is no other lowercase c on the card, which is true, but it did not compare the sister cards.
   - Suggested fix: transcribe `bcpvu` with a note that the sign looks close to the card's `e`, or keep `bepvu` and cite hcp-1359. Either way, drop the claim that this may be a writer's slip unless it can be supported. The word ABOUT is not in doubt.
2. **minor. The "separator dot inside the word" in `Tpss.z` is probably the foot of the second `s`.**
   - Evidence: in `review/work/t_sorry.png` the first `s` ends in a dark pooled foot at lower left. The second, faint `s` has a dark blob in the same position, and the faint arc runs into it.
   - The same thing is seen under the faint `s` of `Zpvs` (`review/work/t_own.png`), which the transcription counts as a following dot.
   - Dots are also recorded unevenly: `xjmm` has a faint trailing dot that is not transcribed (`review/work/t_xjmm.png`), and `pxo` has a small mark between `x` and `o` that is not mentioned.
   - Suggested fix: write `Tpssz` / SORRY, and say the separators are approximate. This affects no words.
3. **minor. The `n` of `bn` is under-described.** Uncertainty 6 calls it readable but thin. In fact it is angular, close to an `x` or `z` shape (`review/work/raw_bn.png`), and it is the only lowercase `n` on the card, so nothing on the card confirms it. AM is certain from context and from `J. bn` on many sister cards, but the note should say that the reading rests on that and not on the shape.
4. **minor. Wrong pointer in uncertainty 5.** It cites `work/crops/y_amp.png` as the comparison with hcp-1403, but that crop shows this card only. Cite the sister crop, for example hcp-1373's `w_and.png`, and add the median result from point 6 above.

## What I could not verify

- The meaning of "news in code" and of the quoted "by very special request". Neither can be tested from this card alone.
- The solver's statement that no published solution exists. I did no web search of my own; the task records today's register check as clean.
- Whether the mark on the stem of `wfsz` (line 2) and similar blobs are separators or ink pools. The scan's fading pattern does not settle it, and no word depends on it.
