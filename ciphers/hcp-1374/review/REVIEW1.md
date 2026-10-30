REVISE

# Review 1 of hcp-1374 / pc_hcp_55 (Claude Opus 5.5, reviewer, 2026-10-30)

The key, the letter sequence and the reading of the card stand. I tried to break them and could not. Two concrete changes are needed: the English and Slovak sentence should be re-punctuated (finding 1), and the z of `Wfsz` should be marked as an emendation (finding 2). No re-review is needed if only these are changed.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1374/work/decode.py` ran, the hashes passed, and the output equals the table in SOLUTION.md (39 enciphered and 6 abbreviation letters).
- **Independent decode.** `review/work/indep_decode.py` uses its own transcription, typed from my crops, and plain ord arithmetic. It gives the same text: MY OWN / BOY / VERY IDLE STORM / TO DAY / MY / YOUR OWN / GIRL, 39 letters. 18 Oct 1907 was a Friday.
- **Transcription against pixels.** I rotated `work/hires/pc_hcp_55_adr.JPG` 90 degrees CCW and made my own crops at 2x to 10x, some with autocontrast (`review/work/l1…l5.png`, `s4`, `jemf`, `tail`, `hjsm_m`, `p2`). I went through every row.
  - Clean: `Nz`, `Pxo` (twice; on line 4 the x overlaps the bow of the P, see `p2.png`), `Cpz`, `jemf`, `up`, `Ebz` (b is 6-shaped, z is 2-shaped), `zpvs`, `Hjsm`.
  - `N & L.` has the same three forms as hcp-1386 (`work/crops/nl.png` there). The card has no dot after the N, and the solver records none.
- **Disputed signs.**
  - `tail.png` against `hjsm_m.png`: the last sign of `tupsn` has two minims joined low and rising. That is the ductus of this writer's m (three minims joined the same way in `Hjsm`, and in `jemf`). So n is as good as u, and the solver's claim that n and u are not separable holds. STORM is chosen by the word but is well supported: the sign is not 2-shaped, so `tupsz` is excluded, and `tu`, p and s are clean.
  - `jemf`: the first sign is a long stroke with a hooked foot. It is drawn like the j of `Hjsm` and like the stem of `Pxo`, but there is no bow over the word, so P is out. The second sign is a looped e with an open eye. The third is a three-minim m. The fourth is an f with a closed lower loop. Among ?-L-E words only IDLE fits a d in second place, so no competing word exists.
  - `tupsn` begins with t (tall, round-footed stroke, long bar), then a low u. The tall stroke is not the first stroke of a single `u`: a separate two-minim u follows it.
- **Key coverage.** One Caesar shift covers every enciphered sign. No per-word adjustment is used.
- **Context.** I checked these on the scans: picture "Royal Pump Room and Baths. Leamington" with no cipher; postmark WIMBORNE, 10 PM, OC 18 07; address Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon; plain heading Friday; plain date Oct. 18th 1907. The formulas match hcp-1386, 1405 and 1368.
- **Published solution.** None is attached in the capture. The target is not in register-exclusions.json. The orchestrator's AI-register check covered the register; I did not re-fetch it.

## Findings

1. **major: the English and Slovak sentence is probably misparsed, and the doubt about IDLE is misplaced.**
   - SOLUTION.md gives "Very idle storm to-day", calls it odd English, and suggests a writer's slip and VILE or WILD.
   - The card has a real, separate dot after `jemf` (`jemf.png`). The same couple writes this pattern elsewhere: hcp-1405 has "I have been very busy to-day" (`wfsz. cvtz.` / `up-Ebz.`).
   - "Very idle. Storm to-day." is natural English, and "idle" is the plain opposite of the "very busy" of that card. It may describe the writer or her day, which the card does not say.
   - Caveat: this writer's dots are not firm word-boundary marks (`up. Ebz.`), so this is the preferred punctuation, not a proved one.
   - Fix: give "Very idle. Storm to-day." as the main English and Slovak rendering, with the unpunctuated form as the alternative. Rewrite Uncertainty 1 and the last line of "Why this is believed correct" accordingly, and drop the slip suggestion. The letters do not change.

2. **minor: the fourth sign of `Wfsz` is s-shaped, and the table prints it as a plain z.**
   - In `s4.png` the pale top and then the stroke descend to the right into a dark foot with a beak pointing left. That is the same construction as the s immediately before it.
   - The writer's z (`Cpz`, `Ebz`, and `wfsz` on hcp-1386, `work/crops/wfsz.png` there) descends to the left and its foot runs to the right.
   - So the literal sign is s (VERR), and z is an emendation from the word. VERY is secure, because the word recurs on many cards of this correspondence, but this is not a reading of the pixels.
   - Uncertainty 2 discloses the weakness honestly but softly ("looks closer").
   - Fix: mark the sign in the table (`Wfs[z]`, literal s) and say "38 letters read, 1 emended by the word" in the status line. "Every enciphered word" decoding into English holds only with that emendation.

3. **minor: the dot after `Wfsz` is not on the card.** There is no separate dot between the fourth sign and the j (`s4.png`). Only the beak of the sign's own foot is there. Remove it from the table and from `transcription.json`, or say it is an assumption.

4. **minor: the underline is not recorded.** A single long stroke runs under `L. Hjsm` on the last line (`l5.png`). Mention it. The sense is unaffected.

## What I could not verify

- Whether the paleness at the top of `Wf`, the s and the fourth sign is pen run-out or partly comes from the portal watermark band crossing that spot. No clean scan exists.
- What `E. L.` and `N & L.` stand for, and who or what was "idle". Both are correctly left open.
- Whether hcp-1394's doubtful `tupsn` is the same word. I agree with the solver that it gives this card no support.
