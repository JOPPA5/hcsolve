REVISE

# Review 1 of HCP1316 (Feri to Jolánka Tóth), Claude Opus 5.5, 2026-10-30

The key, the identification as Hungarian, and almost all of the reading stand. One sign that changes a word in the tentative clause (row 17) was misdescribed, and a few alternatives need to be disclosed. No finding is a blocker.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1316/work/decode.py` ran from the repository root. All four SHA-256 checks print OK. The output has 337 ledger tokens, and every row matches the "Literal decipherment" block in SOLUTION.md.
- **Independent decode.** I read the signs myself into glyph classes (`review/work/reading.txt`) from my own 2x row crops and 4-7x detail crops (`review/work/crops/`, made by `rows.py`, `z.py`, `z2.py`, `z3.py` from the hires address side). `review/work/decode_review.py` uses its own class-to-letter table, taken from HCP1216 `work/graphic-key.json`, and compares with the ledger. Result on 336 decoded signs: no conflict in a clearly read sign. Three flagged positions:
  - row 16, sign 5, and row 18, sign 8: I left these as doubtful (see findings 2 and 6).
  - S4, sign 2 (ü against ű): this is an artefact of my class name, because the sign shows two marks and the ledger's double-acute is acceptable.
  - Row 15, sign 2 and row 17, sign 1 are doubtful in both readings.
- **Transcription against pixels.** I checked all 19 rows and all 5 stamp rows sign by sign. Rows 1-3, 5-7, 9, 10, 12-14 and 19 are correct. In rows 2, 7, 10, 13 and 14 g and y are separate signs here, as SOLUTION.md says.
- **Key coverage.** Every sign outside the struck-out passage maps to a family class. The cancelled sign in row 11 is treated correctly as having no value.
- **Restorations.**
  - *csókolom*: only an arc of k and the arch and crossing of o survive in the stain. They fit, but the word is restored from its formula. SOLUTION.md item 11 discloses this properly.
  - *számta*: the a is stained, and its lower bar is clear. The third stroke of m is pink but visible at 7x, so S2 holds.
  - Row 19 *ve a*: three bars then two bars, as stated. The bracketed [le] is an honest omission note.
  - Row 11 *semit*, row 4 overwritten m and row 8 Latin-looking m are all described accurately.
- **Language and context.** The text is natural Hungarian of the period and the card's formulas match the family. The address is in clear and reads Szépreményű Tóth Jolanka úrleánynak, Jász Árokszállás, consistent with the portal. Sender Feri matches HCP1212, 1213, 1216.
- **Sources.** The portal metadata shows no attached solution. SOLUTION.md credits the family key correctly.

## Findings

1. **Major: row 17, first sign is misdescribed, and *be-* is not considered.** SOLUTION.md item 8 calls it "a large blot with a stroke rising to the right" and reads d, so *de bizonyíthatnak*. At 6x with the green channel stretched (`review/work/crops/r17_blob.png`) the blot is not formless. Under the ink halo there is a tall curved stem and a closed bowl, whose thin lower arc reaches the foot of the stroke on the right. That is the shape of the six (b), compare the clean b two signs later. The family d is a short and a long stroke with no bowl. The right-hand stroke stays unexplained under b, and the bowl stays unexplained under d, so the pixels do not settle it, but they lean to b. That gives *bebizonyíthatnak/-nák*, one word, from the standard verb *bebizonyít* "to prove", and it removes the *de* that makes the clause read badly. A counterpoint: HCP1212 has bare *bizonyítsam*, and HCP1216 has *de*. **Fix:** mark the sign b or d in the ledger, describe the bowl, give both readings with translations, and update the Slovak and English. Do not present *de* as the main reading without saying why.
2. **Minor: row 18, sign 8, is not a clean e.** Item 9 says all signs are "legible as b e z e t o m". In `review/work/crops/r18_end.png` this sign has two full bars and only a tiny speck under the left of the top bar, where the e needs a middle bar. This writer's e can have a reduced middle bar (row 7, sign 2), so e stays possible, but a or á is also possible. With a, the slip against *bezárom* is one letter (t for r), not two. The following sign is plain gamma, with no r crossbar. **Fix:** mark it doubtful (a/e) and restate the correction.
3. **Minor: row 5 word division is an undisclosed choice.** The letters are *…iskola is voltam*. SOLUTION.md splits them as *volt ám* without noting the alternative *voltam* "I was", which would need a missing case ending (*tánciskolá[ban]*). Both are possible. The first-person run of the card (*megérkeztem*, *kerültem*) makes *voltam* worth stating. **Fix:** add it to the uncertainties.
4. **Minor: *-nak* or *-nák*.** Acutes are mostly unwritten, so row 17's ending may be conditional *-nák* ("they could prove"). Two bars are certain, so *-nék* is excluded. The speck under the row 17 k belongs to the i of *soraim*. **Fix:** give the option. It suits the *bár* clause, and it changes the translation.
5. **Minor: row 15, first sign is retouched but unmarked.** The ledger has a plain M. The sign is thick and shows three strokes plus a branched extra ink stroke (`review/work/crops/r15_start.png`), so it looks like four. m fits *magát*, but it should carry the same doubt as the blotted vowel beside it. **Fix:** mark it M? or add it to item 7.
6. **Minor: row 16, description of the sign and the struck passage.**
   - The zigzag sign is correctly flagged as *context*. I cannot confirm m from the pixels, and I recorded it as unknown.
   - The strike-through does not end at the column rule. Its lines run past the rule to the right.
   - Above the struck line there is a second, raised 6 and a dotted sign, and below the blot a large loop. Item 3 does not mention these, and they suggest overwriting in layers. **Fix:** correct the description. The passage stays undecoded, and I could not decode it either.
7. **Minor: status line.** After finding 1 the header's "read letter by letter" for rows 15-17 is too strong. Reword it. *Why it is correct* may stay.

## What I could not verify

- The sense of rows 15-17 under either reading. It stays tentative.
- The decoding of the struck-out passage in row 16.
- The postmark beyond the day 30, which is clearly visible. The month numeral and the year are not readable with confidence, so the portal's 1912-06-30 is only partly confirmed.
- Whether a published solution exists elsewhere. I relied on the portal metadata and the orchestrator's register check, and did no web search.
- The crops are from a scan. Pixel inspection cannot show stroke order in the overwritten signs.
