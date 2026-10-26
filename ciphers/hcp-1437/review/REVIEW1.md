ACCEPT

# Review 1 — HCP 1437 / pc_hcp_118 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I read the whole message myself from `source/address.jpg`, sign by sign, before comparing it with `work/transcript.txt`. All 114 letter positions agree. The only difference is one full stop the solver left out. The findings below are about disclosure and context. None of them changes a letter of the plaintext.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1437/work/decode.py` runs, the SHA-256 checks of both scans and `metadata.md` pass, and the output is byte-identical to `work/plaintext-check.txt` (`diff` empty).
2. **Independent reading of the scan.** I did not use the solver's crops. I made 4× strips of every message row and 5–10× details of the doubtful places with ffmpeg (`review/work/crop.sh`, `r1-2.png` … `r7-9.png`, `z-*.png`). I wrote my own reading to `review/work/my_reading.txt`. It is identical to `work/transcript.txt` except for row 4 (finding 1). On my first pass I read the third sign of `HAVE` as `0`. A side-by-side zoom (`z-have.png`, `z-david.png`) shows that it is the same looped cursive `v` (with a flag at the top right) as in `DAVID`, and `0` does not occur anywhere else. I corrected it to `v`.
3. **Independent decoder.** `python3 -I review/work/review_decode.py review/work/my_reading.txt` (my own code, which does not import the solver's) gives the same nine lines, plus `YESTERDAY.`. Output is in `review/work/my_output.txt`.
4. **Key consistency and coverage.** 114 positions: 72 digits and 42 Latin letters. Each digit 1–9 has one value everywhere (counts 1:15, 2:13, 3:10, 4:4, 5:1, 6:6, 7:8, 8:11, 9:4). The 42 plain letters all come from `b c d f h k l m p v w y`. No plain vowel and no plain t/n/s/r appears anywhere, which is exactly what the scheme "A E I O U T N S R → 1–9, everything else plain" predicts. Every sign of the message and the signature is covered, and nothing is left over.
5. **Specific doubtful signs checked at high zoom.**
   - The overwritten first sign of `OAKLAND` (`z-oakland.png`) is a heavy `4` written over an earlier stroke. I agree with the solver.
   - The `k` in `WAKEFIELD` (`z-wakefield.png`, `z-wakefield2.png`) has a tall ascender loop with a small bowl and kicked leg. It is the same `k` as in `OAKLAND` and `SKIPP` (`z-skipp.png`). It is **not** the digit `9` (= R), which in this hand descends below the line (`y28629`). The ink therefore says W‑A‑K‑E‑F‑I‑E‑L‑D. The cramped `32` after the `f` is legible.
   - The `p` in `CASPERS` (`z-caspers.png`) has the same long descender as `p` in `PLAY` and `SKIPP`. I see no `h`.
6. **Other text on the card.** On the address side everything else is plain or printed: the address `Mrs S. J. Briggs / Canaan / Conn. / Box 275`, the postmark `MILL VA[LLEY] SEP 25 5 PM 190[8]`, the Newman Post Card Co. imprint, and the HCPortal watermark wheel. The picture side (Mills Seminary bell tower, Oakland) has no handwriting. I found no ciphertext that the solver missed.
7. **Language and context.** This is natural colloquial American English of the period. The postmark date agrees with the portal date 1908‑09‑25, a **Friday**, so "yesterday" was Thursday 24 September. Mill Valley is in Marin County, across the bay from San Francisco and Oakland, which fits "have been to Oakland once" and "was in San Francisco yesterday". The recipient `Briggs` matches the portal. On the play, see finding 2.
8. **Prior solutions.** The portal status recorded by the solver is Not solved, with no attachment. The register snapshot in `hcp-1440/work/register-snapshot.json` (same day) has no entry for 1437 / pc_hcp_118. I found no sign that a published solution was used.

## Findings

1. **minor — one full stop omitted.** Row 4 has a clear dot after `y28629d1y` (`z-row4.png`), the same kind of dot as in `W18.` and `37.`, but the transcript has `y28629d1y w36h`. The solver keeps the dots in `WAS. IN.`, so this one should be kept too (`YESTERDAY. WITH`). There may also be a small dot between `pl1y` and `6h2` (`z-play-music.png`). It is too faint for me to call ink, but it should be mentioned. Neither dot changes the meaning.
2. **minor — the strongest context is hidden.** *The Music Master* (Charles Klein, produced by Belasco in 1904) was the vehicle of **David Warfield**, who played Anton von Barwig from 1904 to 1908. A 1908 issue of the *San Francisco Dramatic Review* reports a multi-week run of "David Warfield in The Music Master" in San Francisco. I did not pin down the exact week. SOLUTION.md only says "Do not replace WAKEFIELD with a historically expected performer's name" and "not an external theatre identification". That is the right decision about the text, because the ink has `k2`, not `9` (see check 5). But the reason should be stated openly: the writer misspelled or misremembered Warfield as "Wakefield". The fact that the plaintext names the right first name and the right play, in San Francisco, in 1908, is strong independent confirmation of the decipherment and belongs in the evidence section and the report. Sources: https://en.wikipedia.org/wiki/David_Warfield , https://en.wikipedia.org/wiki/The_Music_Master_(play) , https://lantern.mediahist.org/catalog/sanfrandram1908sanf_0702
3. **minor — near-homographs not disclosed.** (a) The first `c` of `FRANCISCO` and the `c` of `MUSIC` are written as a looped, `e`-like cursive c (`z-francisco.png`, `z-music-end.png`). Because E is always the digit `2` in this system, they must be `c`, but a reader comparing with the scan will stumble on them. (b) The capital `F` of `FRANCISCO` is a 7-like capital, separated from the digit `7` (= N) only by its flat top bar, its size and the context (compare `z-san-fr.png`). Both should be listed under "Readings that need review".
4. **minor — plain-text context not recorded.** SOLUTION.md does not mention the postmark (Mill Valley, SEP 25, 1908, a Friday) or the full address (Mrs S. J. Briggs, Canaan, Conn., Box 275). Both agree with the portal metadata and with "yesterday … San Francisco", so they belong in the context section. The portal language "Unknown" should be stated as English.

## Required for closing

Nothing blocks FINAL. In the report, please: add the dot after YESTERDAY, add the Warfield / *Music Master* context explicitly (keeping the literal WAKEFIELD), note the e-shaped c and the 7-like F, and record the postmark and address.

## What I could not verify

- The last digit of the postmark year and the hour are partly under the stamp. I read `SEP 25` and `190…` and rely on the portal for 1908.
- What was written under the overwritten `4` of OAKLAND.
- The exact dates of Warfield's 1908 San Francisco engagement. My search confirmed a 1908 run, not the week.
- Who "Skipp" and "Casper" were.
- Whether a decipherment has been published outside the portal and the register snapshot. I did not do a wider search.

## Files

`review/work/crop.sh` (crop and upscale helper), `review/work/my_reading.txt`, `review/work/review_decode.py`, `review/work/my_output.txt`, and the crops `review/work/r*.png` and `review/work/z-*.png`.
