ACCEPT

# Review 1 — HCP 1438 / pc_hcp_119 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I transcribed all 36 Pigpen signs myself from `source/address.jpg`, without using the solver's tokens or crops. My token list agrees with `work/transcription.txt` at all 36 positions. The literal reading `RLEAS` is what the ink shows. The findings are minor and concern presentation and context.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1438/work/decode.py` runs, the source hash checks pass, and the output is byte-identical to `work/plaintext-check.txt`.
2. **Independent reading of the scan.** I rotated the two margin lines 90° counter-clockwise (the orientation in which the plain `P.S.` stands upright) and cut 6×–16× windows of each line separately (`review/work/u0–u5.png` upper line, `l0–l5.png` lower line, `z-*.png` details). I recorded every sign by **the strokes I saw** (t/l/r/b) plus the dot count, and the commas and full stop as seen (`review/work/my_reading.txt`):

   ```
   tl2 lb2 tlrb1 rb1 rb3 , lrb1 tl2 tl1 tlrb2 tr1 , trb2 tr3 , lb2 tlrb1 lrb3 lrb3 tlrb1 tl2 rb3
   tlrb3 tl1 lrb3 tlr1 , tr3 tlb2 lb3 , rb3 rb1 lrb3 , tl1 tlb1 , lb3 , lb1 tlb2 trb2 tlrb1 .
   ```

3. **Independent decoder.** `python3 -I review/work/review_decode.py review/work/my_reading.txt` is my own code. It maps each stroke set to a grid cell (cell 1 = right+bottom … cell 9 = top+left), and the dot count selects the grid (A–I / J–R / S–Z). It prints `RLEAS BRING MY LETTERS` / `WITH YOU SAT IF U COME.`, 36 signs (`review/work/my_output.txt`). Converting the solver's labels (BR=rb, B=lrb, BL=lb, R=trb, C=tlrb, L=tlb, TR=tr, T=tlr, TL=tl) and comparing with mine position by position gives **0 differences out of 36**.
4. **Key consistency and coverage.** One fixed three-grid key with dots 1/2/3. No sign needs a second value, and every sign on both lines is decoded. The repeats behave correctly: the three Ts of `LETTERS`/`WITH`/`SAT` are all `⊔` with 3 dots, Y in `MY`/`YOU` is `┐` with 3 dots in both, and R in `BRING`/`LETTERS` is `┌` with 2 dots in both.
5. **The opening sign.** At 10× (`u0.png`) the first sign after `P.S.` has a vertical stroke on the **left** and a top bar running right (`┌`), with two dots. That is the same shape as the R in `BRING` and `LETTERS`, not the `┐` of Y/G/P. So the ink says `RLEAS`. The word is very probably the writer's slip for `PLEAS(E)` (a horizontally mirrored corner, with the final E dropped). The solver states this, does not repair it silently, and handles it correctly.
6. **Other text on the card.** The main message is plain cursive (`Rutland Iowa May-28-08. Recieved your card this A.M. Walter was here a few minutes yesterday. Ruth and Mabe were just here on there way to school to take exams. Ada went over to Maud's this morning so I am alone all day. Ethel Pattee`). The postmark reads `RUTLAND MAY 28 1908 IOWA`, and the address is `Ray Bartley, Laurens, Iowa`. The small mark beside "Rutland Iowa" is a printed ornament (`z-mark.png`). The picture side ("CAN YOU HEAR IT?", three cats) is printed only. I found no ciphertext that the solver missed.
7. **Context.** 1908‑05‑28 was a **Thursday**, so "SAT" is Saturday 30 May, two days later. That is a plausible "if you come" visit and fits a P.S. asking for letters to be brought along. The plain English and abbreviations (`SAT`, `U`) are natural for 1908 postcard writing.
8. **Prior solutions.** The portal status is Not solved, with no attachment. The same-day register snapshot (`hcp-1440/work/register-snapshot.json`) has no entry for 1438 / pc_hcp_119.

## Findings

1. **minor — no normalized English reading.** SOLUTION.md gives the literal text and a Slovak translation with the interpretation in brackets. The original language is English, so the normalized English reading should also be stated, clearly marked as editorial: "P.S. [Please] bring my letters with you Sat[urday] if [yo]u come." The final full stop after `COME` is on the card and could be kept in the literal text.
2. **minor — plain-text context unused.** The card is signed in plain script **Ethel Pattee**, written at **Rutland, Iowa**, and postmarked there on 28 May 1908 (a Thursday). SOLUTION.md and the metadata say "Sender: Unknown" and never mention the signature or the weekday. These belong in the context section and the report: the signature as written, without further identification, and the weekday that makes "SAT" concrete. The related card HCP 1440 (also to Ray Bartley, also postmarked Rutland) mentions "Mrs P." and "Ethel", which is consistent with this but proves nothing.

## Required for closing

Nothing blocks FINAL. Please add the normalized English line and the plain-text context (signature, place, postmark, weekday) to SOLUTION.md and the report.

## What I could not verify

- Whether the opening `┌` is a slip for `┐` (P) or something else the writer intended. Only the shape is certain.
- Dots that touch the outlines are counted as the solver counts them. At 10× each of the 36 signs gave the same count for me, but the scan is 1024 px wide and the signs are about 10 px.
- Whether a decipherment has been published outside the portal and the register snapshot. I did not search further.

## Files

`review/work/crop.sh`, `review/work/my_reading.txt`, `review/work/review_decode.py`, `review/work/my_output.txt`, and the rotated crops `review/work/u*.png`, `review/work/l*.png`, `review/work/seg*.png`, `review/work/up-*.png`, `review/work/lo-*.png`, `review/work/z-*.png`.
