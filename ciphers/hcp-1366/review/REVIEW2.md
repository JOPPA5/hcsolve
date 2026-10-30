ACCEPT

# Review 2 of hcp-1366 (pc_hcp_47)

Reviewer: Claude Opus 5.5, 2026-10-30. No watcher, per this run's orchestration rules.

## Summary

The reading stands: Caesar (cipher = plain + 1), **MY OWN LOVING BOY / NO TIME TO / SEND LETTER / LOVE & [Lt..] / FROM YOUR OWN / [M. h.] GIRL**. I tried to break the new word `Mpwjoh`, which is the main point of this round, and could not. It replaces my own round 1 proposal `Mpwfs`, and that proposal was wrong. All remaining findings are minor disclosure points. None changes a word.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1366/work/decode.py` ran. Hashes passed and the output equals the SOLUTION.md table, with 51 enciphered + 4 literal letters. I recounted 51 by hand.
2. **Independent decode.** `review/work/my_decode2.py` uses my own arithmetic and my own transcription of the six rows. Shift 1 gives the claimed text. The neighbouring shifts printed (0, 2, 3) give no English. 51 letters.
3. **Transcription against pixels.** I rotated `work/hires/pc_hcp_47_adr.JPG` (the un-converted original) 90 degrees anticlockwise and made new 3-7x crops, some with raised contrast (`review/work/r2/a_*.png`). I checked every word on the card except `Mpwf` of line 4, where I used the solver's crop in `cmp_mpwjoh.png` and my `a_feet.png`.
4. **`Mpwjoh`, sign by sign** (`a_wjoh.png`, `a_wjoh_c.png`, `a_feet.png`).
   - After `Mpw` the next sign starts at a dark left-hand foot below the line, runs through the bottom of a hook and rises right. That is one continuous pen stroke: j.
   - It is not f. On this card f has a closed loop at the foot in both `Mpwf` and `ujnf`, while the j of `ujnf` and of `Hjsm` has exactly this open hook (`a_feet.png`, panels 2 to 5). The `ujnf` j is stronger evidence than the `Hjsm` the solver cites, because it stands beside an f in the same word.
   - A closed lens with a clear counter follows on the baseline: o.
   - Its exit runs up right to a sharp apex, falls straight, and ends beside a dark blob: h. The shape matches the same word on hcp-1361 and hcp-1367 (`work/crops/cmp_mpwjoh.png`, rows 1 to 3).
   - Against LOVER and LOVED: both need f at the hook, which the foot excludes, and then cannot place the lens and apex as one letter.
   - Each sign is seen on the pixels. The word is not forced from the parallel.
5. **Other restorations.**
   - `Cpz` (`a_cpz.png`): looped C with inward hook, long p stem with a bowl, z pale with a dark foot dash, two dots.
   - `Mfuufs` (`a_letter_c.png`, `a_ff.png`): M, f, then the fading uu. There is a pale curl, three blots and a pale double stem at the second f. The pale ink is real ink, and it is not the printed overlay.
   - `Lt..` (`a_lt.png`): looped L, c-like stroke, a short dash at its top right, two dots above and to the right. This agrees with Uncertainty 3.
   - `M. h.` (`a_ml.png`): three downstrokes after a pale lead-in; second sign has a stem with a short foot. Agrees with Uncertainty 4. The p tail of `Zpvs` stops above the h stem, so the stem is not borrowed from it.
6. **Ordinary rows.** `Nz Pxo` (`a_l1a.png`), `Op ujnf up` (`a_l2.png`, the j with its dot), `Tfoe` (`a_send.png`), `Gspn Zpvs Pxo` (`a_l5.png`, `a_zpvs.png`), `Hjsm` (`a_hjsm.png`) and the plain heading (`a_top.png`) all fit, apart from finding 1.
7. **Coverage and key.** No writing on the address side's message half is left outside the table. One fixed shift covers everything except the two groups kept literal, and those are declared.
8. **Language and context.** Period English; "no time to send letter" is telegraphic but natural. 19 July 1907 was a Friday (checked in Python). hcp-1363 confirms the same date and postmark time and "No. 2.".
9. **Citations.**
   - hcp-1363's review does reject s, on the ground that the fall and blob have no counterpart in any s.
   - hcp-1360's review does read `Mpwjoh`.
   - `Mpwfs`/LOVER otherwise survives only in the withdrawn text of hcp-1363 and this card, so that claim holds.
   - `compare.py`'s input crops exist. I did not run it, because it would overwrite a solver file.
10. **Sources.** No published solution is used, and the search limits are disclosed honestly. The user's list of externally published ciphers does not include this number.

## Findings

1. **minor: `Zpvs` final sign is not disclosed.** In `a_zpvs.png` the last sign is a small c- or r-shaped hook, unlike the large angular s of `Mfuufs` and `Hjsm` and closer to the e of `Tfoe`. Only YOUR makes sense, so the reading stands, but here context decides it, as for `up` (Uncertainty 8). Add one line to the uncertainties.
2. **minor: the missing j dot is not disclosed.** The j of `ujnf` has its dot. The j of `Mpwjoh` has none on this card: the dark stroke above it is the foot of the p of `Cpz`, not a dot. `Hjsm` has no dot either, so this is a habit and not an objection, but Uncertainty 1 should say so.
3. **minor: the comparison with hcp-1367 is slightly misdescribed.** Uncertainty 1 says the two sisters have "a straight tail". hcp-1367's SOLUTION.md (Uncertainty 3) describes "the j's hooked foot" there, and its crop shows the stroke curling at the top of the C below. So the difference from that sister is smaller than stated, which favours the reading. Correct the sentence, and cite the j of `ujnf` beside `Hjsm`.
4. **minor: the pale forms at the second f of `Mfuufs` are slightly under-described.** `a_ff.png` shows two pale forms, a closed arch near the second u and a separate c-like curl, as well as the stem. Uncertainty 5 mentions one curl. Six letters remain the best count, and "letter" fits the sign order. The doubt is already flagged in general terms, so a clause is enough.

No blocker or major finding. These can be fixed when the report is written, without another review round.

## Could not verify

- Whether `Lt..` and `M. h.` are enciphered or literal, what they mean, and the identity of t (against c or r) and h (against L). The solver rightly leaves these open and keeps "Ks" as a hypothesis.
- The postmark town beyond WIM...; I relied on round 1's `z_stamp.png` and did not re-crop it. The same goes for the address and picture side, which I did not re-read.
- Whether a published solution exists outside this repo: I made no web search, and the register check is the orchestrator's.
