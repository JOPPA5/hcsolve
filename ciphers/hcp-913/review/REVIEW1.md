ACCEPT

# Review 1 – hcp-913 (Fritz Lehmann card, Reichenbach i. Schl.)

Reviewer: Claude Opus 5.5, 2026-11-03.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-913/work/decode.py` (repo root): all four SHA-256 checks print OK, and the output
   matches the "Literal decode" in SOLUTION.md line for line (LIBER FRITZ ! … DEINNER EMMA).
2. **Independent decode.** I wrote `review/work/decode_review.py` (my own parser, alphabet A–Z without J numbered from 2). Run as
   `python3 -I ciphers/hcp-913/review/work/decode_review.py ciphers/hcp-913/work/transcription.txt`, it gives exactly the same 18
   lines. Every number in the transcription falls in 2–26, so the key covers the whole ciphertext. Nothing is left over and no
   number is skipped.
3. **Key provenance.** The same table appears in SOLUTION.md of hcp-1113, 1134, 1044 and 1045, and each of those has REVIEW1 =
   ACCEPT. Note that those sister cards are REVIEWED1, not FINAL (see finding 3). On this card the key has independent support:
   it gives 18 lines of coherent German with no help from the sister cards.
4. **Transcription against the pixels.** I rotated the hi-res original in work/hires/ by 180 degrees and cut eight full-resolution
   strips that cover all 18 lines (`review/work/s0.png` … `s7.png`). I read every line against work/transcription.txt and found no
   discrepancy. I also made 3x enlargements of the disputed spots:
   - `z_gruesse.png`: "8.13.10".19" is clearly 8, 13, and 10 with two ticks above it. The 13 is a plain 13 and cannot be read as
     18. So the "GMI"SZE for GRÜSZE" slip is real, and the solver disclosed it.
   - `z_line2end.png` / s0: "21.15" (UO) at the end of line 2 and "8.15.20" (GOT) at the start of line 3 are clearly written.
     The slips are real and disclosed.
   - s3: "5.15" (DO) in line 8 is clear. The ringed top of 5 is the writer's normal 5 (it also appears in 5.10.6 DIE, 15.3 OB and
     5.15.4.9 DOCH). I agree with the solver here.
   - s3, line 9: the third number of KOMMST (13) and the 2 of 21 (WURDE) are ink-blotted but readable. The solver disclosed both.
   - `z_wenns.png`: in line 15 the second 14 of 23.6.14.14.19 is overwritten (the 1 is reworked into a 4-like shape). The solver
     disclosed that reading it as 14 (WENNS) partly rests on word sense.
   - `z_line1strike.png`: in line 1 a struck-out number (2x, probably 26) has a 7 written above it, followed by 18. The reading
     7.18.10.20.26 = FRITZ is correct, and the solver disclosed the struck number.
5. **Other surfaces.** On the picture side (`review/work/pic.png`) I found only the printed caption and the publisher line, with no
   handwriting. On the address side the stamp is still affixed (`stamp_pm.png`), so nothing under it can be checked; the solver
   disclosed this. The plain-script address (Herrn Fritz Lehmann, Schweidnitz) agrees with the portal recipient.
6. **Language and sense.** The text is natural, informal German of the period: an invitation to go cherry picking on Sunday, with
   a request for an answer and the signature "Emma". All the irregularities (LIBER, DEINNER, WEIST, "kommen kommst", the missing
   umlaut in WURDE) are the kind of spelling slips a private writer makes. None of them depends on a forced reading. The
   translations into English and Slovak are faithful.
7. **Honesty.** The portal shows Not solved, with no transcription or solution attached. The solver says no web search was made
   and credits the key to the sister cards. The earlier-work statement is consistent: this directory had no earlier GPT work.

## Findings

1. **minor – geography of Hohenposeritz.** SOLUTION.md says that Hohenposeritz (Pożarzysko) lies "between Reichenbach and
   Schweidnitz". To my knowledge Pożarzysko lies north-east of Schweidnitz, near the Zobten (Ślęża) massif, and not on the way
   between Reichenbach and Schweidnitz, because Reichenbach is south of Schweidnitz. It is still a nearby Silesian village, so the
   argument from context still holds. I did not check this against a map. Please re-word it as "a village near Schweidnitz", or
   verify the location, before it goes into the report.
2. **minor – date.** The postmark date is illegible in my crops as well, so the year cannot be read. Keep the date as uncertain
   in the report. The portal file name "-03-26" disagrees with the solver's month reading of 6, and the report should mention this
   disagreement once. The solver already does so in SOLUTION.md.
3. **minor – sister-card status.** SOLUTION.md calls hcp-1113, 1134, 1044 and 1045 "finished". They carry REVIEWED1 with an ACCEPT
   verdict, but they have no FINAL marker yet. Describe them as "reviewed (accepted) sister cards" rather than as finished.
4. **minor – the "+" marks.** Rendering the cross as "!" is an editorial choice. It is harmless, but the report should say it is a
   sentence-end cross on the card and not an encoded sign. SOLUTION.md already says this.

There are no blocker or major findings. Every claimed slip is visible in the pixels, and none of them was smoothed over.

## Register type

Plain number substitution of a 25-letter alphabet, so the register label is `MASC`. I found no steganographic or hidden part.
The stamp is still affixed, and that cannot be checked.

## What I could not verify

- Whether anything is written under the affixed stamp.
- The postmark year, and therefore the exact date.
- The identity of "Emma", and the exact location of Hohenposeritz (I did not consult a map; see finding 1).
- I made no web search for a published solution of this card.
