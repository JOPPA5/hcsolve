ACCEPT

# Review 1 of hcp-1362 (pc_hcp_43), Claude Opus 5.5, reviewer, 2026-10-30

The reading stands: Caesar −1, 53 enciphered letters, "My dearest, I have one like this. Love and kisses from your own girl." followed by the plain "G. H. April 10th". I tried to break it and could not. The findings below are minor and change no word of the plaintext.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1362/work/decode.py` prints "source hashes OK", the five plaintext lines and "53 enciphered letters decoded by one key". The output matches the table in `SOLUTION.md`.
2. **Independent decoder.** `review/work/indep.py` holds my own transcription, typed from my crops and not read from `work/transcription.json`. It decodes to the same text: 53 letters, 19 distinct cipher letters, no sign left outside the key. Of all 26 shifts, only −1 gives English (printed by the script).
3. **Transcription against the scan.** I rotated `work/hires/pc_hcp_43_adr.JPG` with my own script (`review/work/crops.py`, `crops2.py`, `crops3.py`) and read every word at 3x to 10x. The crops are in `review/work/` (`r_l1a` to `r_l5`, `z_*`). No other handwriting is on either side; the picture side has only the printed caption "Raglan Castle".
4. **Sign by sign on the disclosed points.**
   - `Efbsftu` (`z_blot.png`): the 4th sign is a blot, but its top curl to the right is the writer's s. It is a restoration and is disclosed as one. The other six signs are clear, and the crossbar of t runs far to the right as `SOLUTION.md` implies.
   - `Mjlf` (`z_mjlf.png`, `z_M1.png`): see finding 1. The dot above j, the long j, the stem with foot (`l`) and the looped f are all ink. The loop near the third sign is the grey watermark, not ink.
   - `uijt` (`z_uijt.png`): two dots stand over the i and j positions, followed by the looped j and a tall t. The black "2"-headed stroke with its bar to the card edge attaches at the head of the t. No plausible reading of it as a further letter gives a word.
   - `boe` (`z_boe.png`): the last sign is c-shaped with a heavy ink-filled top, as disclosed. hcp-1363 does record a c-shaped e for this hand.
   - `Ljttft` (`r_l3b.png`): two stems under one bar, a pale f, then a pale double-track t with its bar shifted right, then a dot. All are legible.
5. **Ordinary rows.** `Nz`, `J`, `ibwf`, `pof`, `Mpwf`, `gspn`, `Zpvs`, `pxo`, `Hjsm` are clear on the pixels. `Mpwf` matches `hcp-1366/work/crops/love.png` in outline.
6. **Context.**
   - The address is as stated: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon.
   - The postmark upright (`z_pm.png`) shows BORNE / 10 PM / 10, then further marks (finding 2).
   - 10 April 1907 was a Wednesday (`indep.py`).
   - The sentence is period-normal postcard English. "Efbsftu" recurs on hcp-1356 and hcp-1397.
7. **Sources.** The portal metadata records no solution or transcription, and the card is not in `skip.txt`. Nothing suggests a published solution was used. The sister cards are named as the source of the key.

## Findings

1. **minor: the `Mjlf` capital is better supported than `SOLUTION.md` says.** At 10x (`z_M1.png`) there is a hook, an arch and a diagonal, then a second arched stroke falling to a foot, then a separate third dab just right of it, crossed by a watermark line. That makes three elements. The `Nz` capital (`z_N.png`) has two. So the shape leans to M, not merely to context. The solver may keep the doubt, since the third element is faint, but uncertainty 1 understates the shape evidence. This is not a forced reading.
2. **minor: the postmark month is partly visible, and the "Month is from the handwriting only" statement is too strong.** On the upright crop (`z_pm.png`, `z_pm2.png`) a faint triangular A stands left of the stamp edge and a bowl stands at the perforation, level with the day "10", in the position of AP. Below that are a faint 0 and a plain 7. This supports AP 10 / 07 independently of the handwriting, and the 7 is more legible than "faint" suggests. `SOLUTION.md` and `NOTES.md` say the month is not visible.
3. **minor: the same-day companion card was not used.** FINAL card hcp-1397 is dated in clear "April 10th 1907", agrees with its portal date 1907-04-10, and opens with the same `Nz. Efbsftu`. This is direct evidence for the year on this card, stronger than "07 fits the correspondence". It is context only and does not touch the reading.
4. **minor: the status line says "Three sign points" but Uncertainties lists five sign points** (items 1 to 5). The Uncertainties section itself is complete. Only the summary count is off.

## Could not verify

- What "one like this" refers to. The solver's "another card of the same view" is labelled as a presumption, which is right.
- The expansion of G. H., and whether the initial is G or C. On this card the second stroke at the foot of the capital (`z_G.png`) favours G.
- I did not search outside the repo for a published solution, because the orchestrator's register check covers this run.
