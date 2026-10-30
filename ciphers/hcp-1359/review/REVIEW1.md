ACCEPT

# Review 1 of hcp-1359 (pc_hcp_40), Claude Opus 5.5, reviewer, 2026-10-30

The reading stands: "My own dearest, I am about the end of this stock. N. & L. [t] From your own girl." Caesar -1, English, 9 May 1907. I tried to break it through the weakest letter, the capital of `Foe`, and found it better supported than the solver claims. The findings below are all minor.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1359/work/decode.py` ran. Source hashes OK, 52 cipher letters, 3 literal, round trip OK. Its output matches the table in SOLUTION.md row by row.
2. **Independent decode.** `review/work/mydecode.py` has its own shift and my own token list, and does not read the solver's JSON. It gave the same six rows and 52 letters. The count of 52 in SOLUTION.md is correct.
3. **Key coverage.** One key covers all 52 cipher letters with no per-word adjustment. The only tokens outside it are the literal `N. & L.` and `t`, which are disclosed.
4. **Transcription against the scan.** I rotated `work/hires/pc_hcp_40_adr.JPG` myself and made my own enlarged crops (`review/work/r1.png`…`r5.png`, `cap.png`, `Lt.png`, `tail.png`, `z_*.png`) and read every word sign by sign.
   - `Nz`, `Pxo` (both forms of P), `Efbsftu`, `J`, `bn`, `uif`, `pg`, `tupdl`, `Zpvs`, `Pxo`, `Hjsm`: all as transcribed. The E-f-b-s of `Efbsftu` has the same construction as `Efbsftu` on hcp-1351 and hcp-1355.
   - `bcpvu`: b, flagged c, long-stem p with its bowl running into v, then u. The letters are crowded but the five signs are there; the solver's warning about the misreading `befpvu` is fair.
   - `uijt`: u, i, j, then an uncrossed t. It reads literally like `uijl`; see finding 3.
   - `Gspn`: G, s, p, n, clear.
   - `Foe`: see finding 1.
5. **Plaintext.** Period English. The sentence is not one of the couple's formulae and its words were not forced: ABOUT, THE, OF, THIS and STOCK are independent of the frame. The sense (nearly out of this stock of cards) is correctly labelled an inference.
6. **Context.** 9 May 1907 was a Thursday (computed). hcp-1392 (FINAL) has the same heading "G. H. Thursday." and the same plain date. The address, the E.S. London No. 468 imprint and the picture caption "The Promenade and Beach. Morecambe" are as stated; the picture side has no handwriting. The stamp shows "…ORNE", 10 PM and 9, as the solver says.
7. **Sources.** The portal metadata records no solution or transcription. Nothing in the directory suggests an undisclosed published solution. Neither the number nor the name is in skip.txt or register-exclusions.json.

## Findings

1. **Minor. A sister capital F does exist, and it supports the reading.** SOLUTION.md uncertainty 1 says "no enciphered capital F survives on a sister card to compare". It does: `Fbsmz` = EARLY on hcp-1355 (row 4). See `review/work/cmp_F_1355_vs_1359.png`, hcp-1355 left, this card right. Both signs have the same construction: a left curl, an arch over into a stem running down-left to a foot, and a long straight stroke rising up-right. The only difference is that the rising stroke leaves the stem higher on hcp-1355 and lower here, which makes this one look V-like. It is unlike the V of `Vtvbm` on hcp-1373 and `Vq` on hcp-1351, which have no such left curl. So F rests on form as well as on sense, and uncertainty 1 can be downgraded. Caveat: hcp-1355 is itself only at DONE1, so cite it as a parallel, not as accepted. Its own sentence "No sister card gives a capital cipher F" now has this card as a counter-example.
   Fix: correct uncertainty 1, and update "51 of the 52 letters … no judgement about form" to match.
2. **Minor. "accepted sister cards" is loose for two parallels.** The trailing `t` is justified by hcp-1368 and hcp-1366. Neither is FINAL (both stop at REVIEWED1). hcp-1392 is FINAL and supports the frame and the date, but it has `N & L!` with no t. The parallel is real: the same c-like stroke with a short dash at top right is at `Lt..` on hcp-1366, and I see the same shape here (`Lt.png`). But say that the t parallel comes from cards not yet closed.
3. **Minor. The third dot near `uijt` is not in a period's position.** Uncertainty 5 takes it as a period. Every clear period on this card sits low, near the baseline; this mark sits level with the top of the t, to its right (`z_uijt.png`). Its position matches the detached dash at the top right of the trailing `t` (`Lt.png`), so it may be the detached crossbar of this t. That would support reading t. It is a little rounder than that dash, so this is not certain. No change to the plaintext; adjust the note.
4. **Minor. The postmark can be completed by parallel.** "…ORNE" with hcp-1392's `[WI]MBORNE 10 PM MY 9 07` gives WIMBORNE on the same day. SOLUTION.md leaves the name partial. If added, label it as taken from the sister card, since the month and year are not readable here.

The other disclosures (third letter of `Foe`, `N`/M of `N. & L.`, the pale curve before `Hjsm`, the missing "at") hold up. I looked at each and have nothing to add. For the `N.` of `N. & L.`: hook, stem, then one arch and a short foot (`z_caps_N2.png`). M is indeed not excluded.

## What I could not verify

- The meaning of `N. & L.` and of the trailing t.
- What the "stock" is.
- The identity of G. H.
- Month and year on the postmark from this scan alone.
- Whether a lost abbreviation stood at the pale curve before `Hjsm`. Nothing legible is there.
- I did not make a separate web search for a published solution. I relied on the portal record, the solver's statement and the orchestrator's register check.
