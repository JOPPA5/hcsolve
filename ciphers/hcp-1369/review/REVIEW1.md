REVISE

# Review 1 of hcp-1369 (pc_hcp_50), Claude Opus 5.5 as reviewer, 2026-10-30

The Caesar −1 reading of all 41 claimed letters stands: I could not refute any of them. The one needed fix is that the marks after `L` in line 4 are not ornament. They are the recurring `t..` of this correspondence, and the solution leaves them out of its "all ciphertext" table.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1369/work/decode.py` ran, the hashes passed, and the output equals the claimed plaintext (41 letters, 6 literal). The "0 restored" in its last line is a fixed string, not computed. The claim itself holds: I found no restoration.
- **Independent decode.** `review/work/independent.py` uses arithmetic mod 26 on tokens I keyed from my own crops, and gives: my own boy / school treat / in park to / day / your own / girl (41 letters). Letter count by hand also gives 41.
- **Key coverage.** One shift covers every enciphered token, with no exceptions and no per-word adjustment.
- **Transcription against pixels.** `review/work/crops.py` makes greyscale 4x crops (`a_*.png`) and 8x crops (`b_*.png`) from the un-converted `work/hires/pc_hcp_50_adr.JPG`. I read every token sign by sign:
  - Clear on my crops: `Nz`, `Pxo` (twice), `Cpz`, `usfbu`, `Jo`, `up`, `Ebz`.
  - `Tdippm`: the third sign is one downstroke with no dot, so i. Both p are the looped-stem form with a bowl. The m has humps and is pale. u would give no word.
  - `Qbsl`: the bowl and tail of Q run on into the ascender of b, and that ascender stands above the bowl, so it is b and not o. The l is pale and looped.
  - `zpvs`: the first sign is the z of `Nz`; the p is the same looped-stem form as in `Tdippm`; v and s are pale but readable.
  - `Hjsm`: H is two crossed strokes. The long j has the same construction as the J of `Jo`, ending in a hook up to the left. s is clear. m is flattened, with three low humps and a terminal blot (`b_sm.png`).
- **Language and context.** "School treat" is a sound period term, and the sentence is natural English. 26 July 1907 was a Friday (computed), matching the heading. On the scan I read the WIMBORNE postmark with JY 26 / 07, and the address Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The postmark date agrees with the plain date on the card.
- **Reading order.** `Hjsm` after the date is supported by the same-day card hcp-1368, which closes `zpvs. Pxo. N. L. / Hjsm.`.
- **Sources.** The solution claims no published solution, and I saw no sign of one being used. The orchestrator's register check covers this number.

## Findings

1. **major: the marks after `L` are the recurring `t..`, and the table of "all ciphertext" omits them.**
   Uncertainty 3 treats them as "punctuation or ornament" and says the curved stroke "gives no word". My crop `a_l4b.png` shows a curved stem, a short dash detached at its upper right, a dot below the dash, and two dots near the end of the row above.
   - The same slot on the same-day card hcp-1368 holds `N. & L. t` (`hcp-1368/work/crops/z_dot_t.png`), with the same curved stem and a bar at top right, there attached.
   - hcp-1359 reports "a curved stroke with a detached short dash at its top right" after `N. & L.`, which is this construction.
   - hcp-1361 gives `M & L. t..`, and hcp-1363 gives "`& L t..`" with the "same c-like stroke with a dash at its top right and two dots".
   - Those four solutions are still at DONE1, not FINAL, so this is a recurring pattern, not an accepted reading. The solver's own Uncertainty 2 compares this group with sister cards but does not make this comparison.

   Required fix: list the sign in the transcription as a kept-literal or uncertain `t..` (shifted S), not as ornament. Cite the parallels and state the doubt (c is not fully excluded, and the bar here is detached). Then amend "All ciphertext on the card", the count, and "whole message read". The English gains only an unexpanded tail, and no other word changes.

2. **minor: the sister list for `M-h` leaves out the closest evidence.**
   Uncertainty 1 lists `N-L`, `M-L`, `M[h]` and `N.-1`. It omits the forms with an h-like second letter: `N-h.` on hcp-1349, `N. h.` on hcp-1360 and 1371, `M-h.` on hcp-1361. It also omits the same-day hcp-1368, which reports `N. L.`. In `hcp-1368/work/crops/cmp_N.png` that group has the same pen forms as here, so the two cards should not differ by accident. Please cite them, and state that the M versus N and h versus L calls on 1368 and 1369 disagree although the shapes match. My crops confirm the solver's counts on this card: three downstrokes against two in `Nz`, and a second letter unlike the capital L.

3. **minor: Uncertainty 7 can be closed.**
   The solver did not compare the capital Q with a sister. The lower-case q of `qptu` on hcp-1368 (`hcp-1368/work/crops/r_l3a.png`) is the same 9-shaped form as the sign here: closed bowl, long tail, loop. This supports Q on shape, not only on sense. Note that hcp-1349 reads a different, 2-shaped capital as Q, so this form is not the only one claimed in the series.

4. **minor: Uncertainty 6 has a small error.**
   It reports "a small gap before the m". `b_ppm.png` and `a_l2b.png` show a fine hairline running from the second p across to the first hump of the m, so the word is joined. This strengthens the single-word reading.

5. **minor: same-day card not mentioned.**
   hcp-1368 has the same plain heading "G. H. Friday", the same date and the same postmark time. It supports the reading order (Uncertainty 4) and the structure, so it belongs under "Why it is correct". Replace "nothing else proves it" in Uncertainty 4 accordingly.

## What I could not verify

- The meaning of `M-h` and `M. & L. t..`. Whether either is enciphered remains open.
- Whether `t..` here is truly t: the detached bar makes this a strong parallel, not a proof.
- The portal status and absence of a published solution: I did not re-render the portal, and relied on `SOURCES.md` and the orchestrator's check.
- The reference to "the same hand" on other cards: I compared forms on hcp-1368 and sign crops from hcp-1349 and 1359 only, not the whole series.
