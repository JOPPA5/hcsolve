ACCEPT

# Review 1 — HCP 1440 / pc_hcp_121 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I transcribed the two header rows myself from `source/address.jpg`, and my 19 tokens agree with `work/transcription.txt` at every position. Two signs carry dot marks that the solver did not describe (findings 1 and 2). Context resolves both readings, but they should be disclosed.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1440/work/decode.py` runs, the hash checks pass, and the output is byte-identical to `work/plaintext-check.txt`.
2. **Independent reading of the scan.** I made 9× crops of each row (`review/work/r1a.png`, `r1b.png`, `r2a.png`, `r2b.png`, `r2-tall.png`) and 12–18× details (`z-N.png`, `z-wish.png`, `z-you1.png`, `z-you2-c.png`, `z-ou2.png`, `z-LD.png`). I recorded strokes seen plus dot count (`review/work/my_reading.txt`):

   ```
   trb1 tlb2 tlrb2 lrb3 , tr3 tlb2 lb3 , tlrb3 tl1 rb3 tlr1
   tr3 tlb2 lb3 , lb1 tlb2 lb3 lb2 trb1
   ```

3. **Independent decoder.** `python3 -I review/work/review_decode.py review/work/my_reading.txt` (my own stroke-set → cell, dots → grid code) prints `DONT YOU WISH` / `YOU COULD`, 19 signs (`review/work/my_output.txt`). Compared with the solver's tokens after converting labels: **0 differences out of 19**.
4. **Key consistency and coverage.** One three-grid Pigpen key, the same as on HCP 1438 (also to Ray Bartley). `YOU` is written twice with identical signs (`┐`3, `[`2, `└`3). O (`[`2) and U (`└`3) recur in `COULD`. Every sign in both rows is decoded and nothing is left over.
5. **Other text on the card.** Everything else on the address side is plain: the date `4-17-08`, `Ha Ha.` immediately after the cipher, a long cursive letter signed `R.E.B.`, the address `Mr Ray Bartley, Laurens, Iowa`, and the postmark `RUT[LAND] APR 1? … PM 1908 IOWA`. The picture side ("Easter Greetings", lambs, egg) is printed only. I found no ciphertext that the solver missed.
6. **Context.** 1908‑04‑17 was **Good Friday** (Easter Sunday was 19 April 1908), which matches the Easter Greetings picture. The plain letter tells of going to Lodge and dancing although someone "didn't want us to dance but we did it anyway", sitting up all night, and wanting to go to a play in Humboldt. A teasing "Don't you wish you could? Ha Ha." fits it naturally. The solver's decision not to supply an object for "could" is right.
7. **Prior solutions.** The portal status is Not solved, with no attachment. The solver's register snapshot (`work/register-snapshot.json`) has no entry for 1440 / pc_hcp_121, which I checked with grep. I saw no sign of an undisclosed published solution.

## Findings

1. **minor — the N of DONT is a one-dot box plus an edge blob.** In `z-N.png` the box has one clear dot inside at the left. The second "dot" is a dark mark merged into the right-hand side of the box. Read strictly as one dot, the sign is E (`DOET`). The two-dot reading (N) is forced by context and is surely right, but SOLUTION.md lists only the W and U dots as touching outlines. This sign should be listed by name.
2. **minor — two specks above the D of COULD are not mentioned.** In `z-LD.png` the final sign (`]`, one dot inside) has two small specks just above its top stroke, *outside* the outline. If they counted as dots the sign would be three-dot `]` = V (`COULV`). Every other dot in both rows sits inside its outline, and these specks are smaller than real dots, so not counting them is right. But it is an uncertainty, and SOLUTION.md should state it.
3. **minor — the I of WISH.** In `z-wish.png` the left stroke of the `┌` (I) runs down into the printed caption "This Space for Writing Messages". I see no bottom stroke, so it is not `[` (= F, `WFSH`), and the solver's reading stands. The overlap with the printed caption is worth one line among the uncertainties.
4. **minor — context left out.** The Good Friday date and Easter card, the "Ha Ha." and the dancing story in the plain letter, the Rutland postmark, and the plain initials `R.E.B.` are not used, or are only alluded to. They strengthen the reading and belong in the report. No identification of the writer beyond the initials is needed.

## Required for closing

Nothing blocks FINAL. Please add findings 1–3 to the uncertainty section and finding 4 to the context in the report.

## What I could not verify

- The day digit of the postmark (`APR 1?`) and the hour. They are overprinted by the "POST CARD" ornament.
- Whether the two specks over the final D are ink dots made by the writer or paper defects.
- Whether a decipherment has been published outside the portal and the register snapshot. I did not search further.

## Files

`review/work/crop.sh`, `review/work/my_reading.txt`, `review/work/review_decode.py` (identical to my HCP 1438 reviewer decoder), `review/work/my_output.txt`, `review/work/alt.txt` (the strict alternatives `DOET` / `…LV` decoded for findings 1–2), and the crops `review/work/r*.png`, `review/work/hdr*.png`, `review/work/z-*.png`.
