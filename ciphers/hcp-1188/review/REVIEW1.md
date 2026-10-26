REVISE

# Review 1 — HCP 1188 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct**. The key is a real one-to-one interleaved Pigpen key, it covers all 114 signs, and the message is coherent 1913 American English. The verdict is REVISE rather than ACCEPT because the literal transcription disagrees with the card in two places. The more important one is the signature: the disputed second TL sign carries a small dot, so the card itself reads **DARROW**. Literal DARQOW should not be the headline reading. Neither difference changes the meaning of the message.

## What I verified and how

1. **The documented command.** `python3 ciphers/hcp-1188/work/decode.py` runs. The hashes match `shasum -a 256 source/*.jpg`, and the output is identical to the `text` block in `SOLUTION.md` (114 glyphs, 22 distinct).
2. **Independent decoder.** I wrote `review/work/review_decode.py` from scratch, without importing the solver's code. The #-grid is filled in (undotted, dotted) pairs per cell: A/B in the bottom-right cell, then C/D, and so on. The four X-wedges carry S–Z. The decoder asserts 26 distinct tokens for 26 letters.
   - `python3 -I review/work/review_decode.py work/transcription.txt review/work/claimed.txt` gives `MATCHES CLAIMED`.
   - Repeated signs keep their values throughout: E (BL0) ×13, the TL1 = R in DEAR, FRIEND, PLEASURE, WRITING, RESPFULLY, YOURS, DARROW, and the wedges S/U/W/Y. No sign needs two values.
3. **Independent reading of the scan.** I made half-line crops at 5× of all eight lines (`review/work/L1a.png` … `L8b.png`), 10–18× details (`z-*.png`) and contrast-enhanced versions (`zc-*.png`, ffmpeg, `zoomc.sh`). I read every sign before comparing with `work/transcription.txt`. My reading is `review/work/reviewer-reading.txt`:

   ```
   $ python3 -I review/work/review_decode.py review/work/reviewer-reading.txt review/work/claimed.txt
   DEAR FRIEND AS I
   NOW TAKE TIME AND
   PLEASURE OF WRITINH
   TOYOU IF NOT TO
   STORMY WILL BE UP
   WEDNESDAY EVENING
   RESPFULLY YOURS
   JESSE DARrOW ANS
   DIFFERS FROM CLAIMED  (line 3, line 8)
   ```

   Lines 1, 2 and 4–7 agree sign for sign with the solver, dots included. The literal spellings TO (for too) and RESPFULLY are really on the card, and the solver was right not to normalize them.

4. **Language and context.** The message is plain, slightly ungrammatical rural American English, typical of a courting postcard. The picture side is captioned "The Kind We Raise in Gray, N. Y.". The postmark reads "G… / N.Y." with "2" and "191[3]" visible, which is consistent with the catalogue date of 1913-04-02. That date was a **Wednesday**, so "will be up Wednesday evening" naturally means the following Wednesday. The address looks like "Miss El(z)ora(?) Houghtaling(?), Cold Brook(?), N.Y., R.D. No. 1" (`review/work/address.png`). If "Cold Brook" is right, it is the neighbouring hamlet to Gray in Herkimer County, which fits a short trip "up". I treat that as unverified.
5. **Prior solutions.** I found nothing indicating a published solution was used.

## Findings

1. **major (transcription) / minor (meaning): the surname reads DARROW on the card, not DARQOW.** Details: `review/work/z-L8-RQ.png`, `zc-L8-RR.png`, `z-L8-RR-wide.png`. Both TL signs after DA have a dot:
   - the first TL has its dot well inside the corner;
   - the second TL has a smaller dot pressed against the inner side of its stem, low down.

   The ink stain is to the **right** of the second TL. It affects the following `⊓` (O), whose left stem is lost in it, not the TL itself. So the claim "visible undotted TL0" does not hold. `work/transcription.txt` and the literal reading should give `TL1` = R, flagged as a small dot. "Jesse Darrow" then needs no restoration. I also see a dark speck inside the stain, left of the `⊓`. I read it as a stain particle, not as a dot of the O.

2. **minor: the last sign of WRITING has a dot (H), not R0 (G).** Details: `review/work/z-L3-ING.png`, `zc-L3-NG.png`. The `⊐` after the dotted `7` (N) has a clear dot inside it. That dot is as strong as the N's own dot and sits well away from the N. The literal is therefore **WRITINH**, a writer's slip; compare the undotted `⊐` (G) at the end of EVENING, `z-L6-evening.png`. The solver's notes say "No spelling corrections are applied here" for the literal reading, so this G is a silent correction. Record `R1` in the transcription and list G as an editorial correction.

3. **minor: interpretive points that should stay labelled as such.**
   - ANS is three clear signs after the signature (`┘ 7· V`). The solver's "may request an answer" is a reasonable gloss, and it is labelled as one.
   - "[I] will be up" and "too" for TO are editorial, and they are labelled correctly.

4. **minor: the reproduction command only round-trips a manual token list.** The solver discloses this. The token list is a genuine as-seen transcription, not one derived from the plaintext; I checked it against the scan. The `exact token roundtrip` assertion is tautological and should not be offered as evidence.

## Required for closing

- Change the second TL of DARROW to `TL1` and present **Jesse Darrow** as the reading, noting the small dot. Correct the line-3 final sign to `R1`, with WRITING as an editorial correction.
- Update the literal reading, the interpreted English, the translation and the uncertainty section accordingly.

These are corrections of the record, not of the solution. I see no need for another review round.

## What I could not verify

- The recipient's name and place in the cursive address (my reading above is tentative), and the exact postmark text.
- Whether a decipherment has been published elsewhere.
