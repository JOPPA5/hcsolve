ACCEPT

# Review 1 of hcp-1828 (pc_hcp_509)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. The solver was also Claude Opus 5.5, in a separate session, so this review is not from a different provider.

**Result:** the reading is correct and whole. I could not refute it. All 98 signs are on the card as transcribed, a blind climb from my own sign labels recovers the same 98 letters, and no sign needs a restoration. Five minor findings remain, all in the wording of SOLUTION.md. None changes a letter.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1828/work/decode.py` passes the hash checks and prints 98 signs, 21 distinct, none unread, no unused key entries. The output equals the plaintext in SOLUTION.md row by row.

2. **Independent transcription.** I cut my own 3x row crops from `work/hires/pc_hcp_509_adr.JPG` (`review/work/crops.py`, `crops/r1_*`…`r10_*`) and read all 98 signs, not only a sample. I typed them in my own shape labels in `review/work/own_decode.py`.
   - All ten rows have the same length as the solver's.
   - My labels map one-to-one onto the solver's 21 tokens, so there are no sign disagreements.
   - No sign lies outside the transcribed rows. The rows reach x≈33 at the left of the 1014-wide scan, and nothing in the cipher hand lies right of the spatter at R6/R7.

3. **Blind key recovery.** `review/work/own_sa4.py` runs annealing with quadgrams from the SOLUTION.md and NOTES.md of all other ciphers, with hcp-1828 excluded so its own plaintext cannot leak in. It takes only my sign labels and was run on four reading orders (`review/work/sa4.out`):

   | Reading order | Best score | Result |
   |---|---|---|
   | Turned 180 degrees (last row first, right to left) | -973.3 | exactly the claimed text |
   | Rows in place, each right to left | -975.5 | same key and letters, rows out of order: ADE FROM WITH LOVE MORE ACTRESSES… |
   | Scan order | -1067.1 | nonsense |
   | Rows reversed, left to right | -1076.9 | nonsense |

   Direction within rows is settled by score, and row order by sense. The climb fixed the hapax signs B, K and V by itself. An earlier trigram climb from a word list (not kept) was too weak to discriminate, so it counts for nothing either way.

4. **D versus T.** Sheet `review/work/crops/bars.png` shows R1, R8 and R9 D with a stem clearly below the bottom bar, and the other Ts stopping at that bar or with a tiny nub. The sheet's tile "R5 T2" is my cropping slip and shows the C of R5. The T of GET (R5, x≈134) was checked on `crops/r5_0.png` instead. The tile labelled R5 T1 is the T of CANT. The feature separates all 12 cleanly, as claimed.

5. **R versus I, including R10 (FOR).** Sheets `crops/eyes.png` and `crops/lens.png` show the lenses.
   - R10 is covered by the printed "P", so I read grey values from the original (`review/work/lens2.py`). A band across the lens at y≈1027–1035 has grey 50–110, the density of the ink strokes. Printed type on the same card reads about 160–190. The white patches above and below read about 220–240.
   - So the band is ink and R10 is an eye. The solver's claim holds.

6. **Key and language.** The key is one-to-one and covers the whole ciphertext, with J, P, Q, X and Z unused. The text is natural English of the picture-postcard craze, and actress cards as a collecting subject fit 1906. The picture side is a Tuck card of "Ye Dolphin Inn, Derby", which suits a request for castles and ruins. Dates agree: handwritten "Jan 11th", postmark JA 12 06, portal date 1906-01-12. Plain word endings fall on every row end.

7. **Translations.** The English punctuation and the Slovak translation are accurate.

8. **Restorations and completions.** SOLUTION.md has no "Completion" or "Response to review" section, and NOTES.md describes one solver session. The claim of no restorations is true. The segmentation decision (dash-crescent-dash as one sign) is disclosed. It is also supported by the U sign, which has the same dash pattern, and by the V being written as one tight group in R3.

## Findings

1. **minor: layout claim overstated.** "All rows from R3 to R10 end near the same right edge." R4 to R10 end at x≈508–520 of the 1014-wide scan, but R3 ends at x≈475. The argument still holds for R4 to R10. It should say so. Evidence: `crops/r3_1.png`, `source/address-large.jpg`.

2. **minor: "each visible feature separates the letters consistently" is too strong for R versus I.** Several R signs have a filled lens, with no pupil that can be seen separately: R2, the R of MORE in R4, and partly R7 and R9. Uncertainty 2 names R2 and R7 but not R4. There the sign is a narrow dark blob with a few white flecks. These signs differ from I by a swollen, filled belly, and that reading leans on the words as well as on the pixels. All 12 signs agree with the reading, so no letter changes, but the wording should name R4 and admit this. Evidence: `crops/lens.png` panels 1, 3 and 4 against 5 and 6.

3. **minor: one non-sign mark is not listed.** Uncertainty 7 omits the long pen flourish above R1, running from over the royal arms to about x≈340 and looping once (`crops/flourish.png`). It is in plain pen style, not one of the brush signs, and it lies next to ADE when the card is turned, so it may be a sign-off. It should be listed. Also, the note reads "Jan 11th", with a heavy diagonal stroke through it, not "Jan 11".

4. **minor: the addressee's surname is presented as a fact in the title.** The title says "Mr G. L. Serry", although Uncertainty 6 admits this is the portal's reading, not re-evaluated. The first letter (`crops/surname.png`) has a looped top and differs in form from the S of "Sussex" (`crops/sussex.png`), so "Terry" or "Jerry" cannot be excluded on this hand. I cannot decide it. The report should keep the caution.

5. **minor: context is missing from SOLUTION.md for the report.** Not stated there: the picture side (Tuck Oilette "Quaint Corners", Ye Dolphin Inn, Derby), the street (Queens Road), and the postmark, which reads 11.15 AM, JA 12, 06 from an office beginning FARN…, with the rest of the name not legible enough for me. The sender's place should be given only as far as the postmark shows it. The README requires context in the PDF.

## What I could not verify

- Whether a published solution exists elsewhere. I ran no web search. The portal status and the register check come from SOURCES.md and the orchestrator.
- The sender's identity and the full postmark name.
- The surname in the address (finding 4).
- The solver's scores in SOLUTION.md (-1017.6 and -1081.1). They were on an older sign list that is not preserved. My own run gives the same conclusion on the final signs, with different numbers.
