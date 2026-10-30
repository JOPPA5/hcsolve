REVISE

# Review 1 of hcp-1348 / pc_hcp_29 (reviewer: Claude Opus 5.5, 2026-10-30)

The key and the words WITH LOVE AND … FROM … stand. Two claims are wrong and must be corrected: the closing is the signature `Mpp` = LOO, not unexpanded initials N. P. P., and the year is 1907, not 1904. The text should read: "With love and [k]isses from [y]ours. Loo. Feb 8th 1907."

## What I verified and how

- **Solver's command:** `python3 -I ciphers/hcp-1348/work/decode.py` runs, the hashes pass, 28 letters, and the output matches SOLUTION.md.
- **Independent decode:** `review/work/indep.py` uses my own transcription from the hires scan. Of the 26 shifts, only k=1 gives English. It yields `with love and / isses from w ours / l o o` when the capital is read M.
- **Key coverage:** all 28 letters are covered by one fixed shift, with no exceptions.
- **Crops:** from `work/hires/pc_hcp_29_adr.JPG`, 4–5x, every word: `review/work/r_l1a`, `r_l1b`, `r_l1c`, `r_kiss`, `r_from`, `r_ours`, `r_ini`, `r_year`, `r_postmark`.
- **Year comparison:** `review/work/cmp_seven.png` sets this date beside the date on hcp-1353.
- **Sign reading:** Xjui, Mpwf, boe, gspn and pvst agree with the solver's reading of the signs. The tail `ttft` of `jttft` also agrees (shared bar on two stems, looped f, final stem, detached bar).
- **Address:** Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon confirmed.
- **Postmark:** WIMBORNE 10 PM FE 8. I see no year struck, which agrees with the solver.
- **Plaintext:** real period English, the same formula as sister cards.
- **Published solutions:** the portal attachment state rests on the solver's capture (SOURCES.md). I did not re-render the portal. I found no sign of borrowed text.

## Findings

1. **major: the closing is the writer's signature `Mpp` = LOO, not unexplained initials.**
   - Evidence: SOLUTION.md uncertainty 4 reads N. P. P., decodes M. O. O. and offers no expansion. The solver lists M as "not excluded" but never tries it. With M, the same shift gives L. O. O.
   - The sender signs exactly `Mpp` on hcp-1350, 1351, 1353, 1354 and 1398.
   - hcp-1352 has the same problem in the same dotted form: `N.p.p.`, a compressed capital read as M (its uncertainty 7).
   - On the pixels (`r_ini.png`) the capital has a loop lead-in and two further downstrokes, the same construction as the capital of `Mpp` in `ciphers/hcp-1351/work/crops/signature_Mpp.png`. Its two signs after that are this writer's p.
   - The solver's comparison with `N. & L.` is not the right parallel.
   - Fix: transcribe `M.p.p.` (or `N.p.p.`, read as `Mpp`, disclosing the two-hump capital as hcp-1352 does) and give the reading LOO in the plaintext and in decode.py's output. "Loo" as a pet name stays conjecture, as on the sisters. Say that the expansion rests on the shape of the capital plus the signature; a two-hump N is not fully excluded by this card alone.

2. **major: the year is 1907, not 1904.**
   - Evidence: SOLUTION.md calls the last digit "a clear final 4" and builds on it ("about three years earlier than the bulk"). `review/work/cmp_seven.png` shows it is this writer's 7: left hook, rising right arm, long descender.
   - On hcp-1353 the same form occurs twice in "Feb. 7th 1907", and the postmark there reads FE 7 07. It also appears in "March 5th 07" on hcp-1354 (`ciphers/hcp-1354/work/crops/l7.png`).
   - The solver's 4 reading follows the portal's catalogue date 1904-02-08, which appears to be a misreading of this digit form.
   - Consequences: the card is dated 8 Feb 1907, a Friday, the day after hcp-1353, in the same Wimborne 10 PM series and with the same address. It is not an outlier. This is ordinary writing, but it is a wrong historical claim in the header, status, translations and the transcription JSON (`ordinary.date`).
   - Fix these, and note the disagreement with the portal's date in SOLUTION.md and the report. The postmark has no year, so 1907 rests on the handwriting and the correspondence.

3. **minor: the first sign of `jttft` is closer to g than the table implies.**
   - In `r_kiss.png` and `r_from.png` its wide oval and returning tail match the g of `gspn` better than the narrow j of `Xjui` (`r_l1a.png`). Literal g would give FSSES.
   - Uncertainty 3 calls them the same shape. The literal ISSES is therefore already an interpretation of the sign.
   - The K supply stays reasonable: `Ljttft` is on hcp-1362, and no other word of the form fits (`indep.py` finds only classes/glasses/Ulysses in the system list, none fitting here).
   - Fix: state this. [K]ISSES remains disclosed as a restoration.

4. **minor: `x` needs one more disclosed explanation.**
   - The sign is a plain cross, identical to the X of `Xjui` (`r_ours.png`), and not this writer's zigzag z (`ciphers/hcp-1358/work/crops/z_my.png`).
   - So "a slip for z" is not a misread sign. If it stands for Y, the likely slip is a shift in the wrong direction (Y−1 = X).
   - Either way [Y]OURS remains a restoration, correctly bracketed. Add this alternative.

5. **minor: punctuation incomplete.**
   - Uncertainty 7 and the transcription omit an ink dot after `Mpwf` (`r_l1c.png`, left edge). The dots of the closing are shown in the table but lost for the middle one, which lies on the watermark S (`r_ini.png`).
   - No effect on the reading.
   - The dark spot above `ui` in `r_l1a.png` is unexplained, possibly an ink mark.

## Not verified

- Whether the sender of this card is the same person beyond the hand and signature comparison; I did not compare the whole hand statistically.
- The picture side beyond the solver's statement that it has no handwriting; I did not open it.
- No external search for a published solution was run by me. The AI-register check is the orchestrator's.
