REVISE

# Review 1 of HCP1211 (Claude Opus 5.5, reviewer, 2026-11-02)

The decipherment stands: Hungarian, Jolánka family key, 17 rows, connected text. Two concrete errors must be fixed. The normalized text contains a word that is not on the card, and one ledger token is wrong. Neither changes the sense of the card, and the first one in fact improves it.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1211/work/decode.py` prints four OK hash lines and 322 signs. All 17 printed rows match the literal block in SOLUTION.md (checked by script).
- **Independent decoder.** `review/work/indep.py` has its own key table and parser. All 322 ledger tokens have a value (0 unknown). It also aligns the literal string against the normalized Hungarian letter by letter. Every difference between them is listed in findings 1, 2 and 4 and was checked against the pixels. Output of the alignment:
  ```
  [h]->[p] kaptam | [a]->[n] időn | []->[t] érkezett | [a]->[n] válaszolni | [h]->[p] szép
  []->[s] sors | []->[ha] mostoha | [e]->[a] Jolánkámat | []->[nt] viszontlátásra
  ```
- **Transcription against the scan.** I read all 17 rows sign by sign on my own 2x crops of `work/hires/*_adr.jpg` (6.7 times the source-large scale; `review/work/crop.py`, `r*_*.jpg`), and made stronger zooms of the critical places (`z.py`, `z2.py`, `z_*.jpg`). Apart from the findings below, the ledger agrees with what I see, including the blotted signs of rows 6, 7, 11 and 16, the Latin "is" in row 11, and the cs signs.
- **Language and context.** The text is real early-20th-century Hungarian in the family's register, with formal address. The verse-like close (soha / mostoha / soha) rhymes. Feri, Tóth Jolánka and Jászárokszállás fit the family. Rows 3 to 4, 12 to 13 and 14 to 15 divide words correctly.
- **Plain writing.** I read the stamp note and the address on `stamp.jpg`, `addr.jpg` and `z_pm.jpg`. The reading is right apart from finding 5.
- **The g value.** The C-shape as g holds independently of Hungarian guesswork: *meg* three times, *alig*, *boldogság*, *leg-*, *virága*, and joined gy. The left-bowl value c of the sister tables would give no words. This is a card-level variant of the sister cards' open-loop g (which HCP1225 keeps, with the same "cy" joined gy).

## Findings

1. **major: the normalized text inserts a *ha* that is not on the card.** Row 14 ends *mosto* and a hyphen stroke follows it (`z_row14end.jpg`). Row 15 begins P = = Z E II, that is *ha az én* (`z_row15start.jpg`). There is one *ha* only, and it is the end of *mosto-ha*. SOLUTION.md uses the same two signs twice: it counts *mosto-ha* as a word run across a row break ("Why it is correct") and also keeps a separate word *ha* in "bár mily mostoha, ha az én édes Jolánkámat". The independent alignment shows this as an insertion of two letters. Uncertainty 3 ("the grammar of *ha az én … nem bírnám* is loose") is therefore a false problem made by the error. Without the extra word the sentence is clean and rhymes: *legyen a sor[s] bár mily mostoha, az én édes Jolánkámat elfeledni nem bírnám soha.*
   Fix: correct `work/normalized.txt` and the Hungarian block; delete uncertainty 3; drop "since" in the English and "lebo" in the Slovak ("however cruel fate may be, I could never forget my sweet Jolánka").

2. **minor: ledger error in row 15, *Jolánkámat*.** The sign after III is two bars, a, not three bars. On `z_row15end.jpg` only two bars stand between the m and the t, crossed by the printed divider, and there is no third bar below them. The ledger has `E`, so the literal block prints *jolánkamet*, while the normalization silently gives *Jolánkámat*. The card simply has the a.
   Fix: change that token to `=` and regenerate the literal block (row 15 becomes *haazenedesjolánkamat*).

3. **minor: row 7, last sign wrongly described.** Uncertainty 1 and the ledger token `I_` say the last sign of row 7 shows no dot. It has one: a clear round dot stands above and to the right of the sign, the same placement as the other i of this hand, and a separate full stop follows at mid-height (`z_r7end.jpg`). The i is better supported than stated.
   Fix: change the token to `I` and the sentence.

4. **minor: Row 12 is described inexactly.** The brackets of *[Ö]n* suggest the letter is restored, but the cursive o is plainly there (`z_blot12.jpg`). What is supplied is only its dots, and they are absent, not hidden. The blot stands in the first-sign position of the row, to the left of the o and not over it, so the question is a different one: does the blot cover a letter in front of *on*? SOLUTION.md does raise this, and it is correctly called the weakest point. I cannot resolve it from the pixels either. I accept *Ön* as the best reading, one uncertain word in an otherwise clear card. It should be written *Ön* with a note that the dots are supplied, or *{blot} [Ö]n* in a form that says so.

5. **minor: address abbreviation.** The abbreviation after *kisasszonynak* looks like *sz. r. t.*, with an sz, not *s. r. t.* (`addr.jpg`). The writer also seems to have written *kisaszonynak* with one s, which the plain-hand line should mention. The abbreviation stays unexpanded, as the solver reports, and it does not touch the cipher.

6. **minor: u against z is not disclosed.** On this card the signs for u and z are hard to tell apart by shape: both are a crossing diagonal with a tail (compare *rózsa* in `z_r10start.jpg` with *virul* in row 11, `r6_2.jpg`). There are only two u tokens, *tudok* and *virul*, and both rest on word sense. Item 5 mentions over-inking in *tudok* only. Add this to the word-sense calls.

7. **minor: the date note can say more.** The Jászárokszállás mark shows the date with 10 (`z_pm.jpg`), consistent with the portal file name 1912-02-10. The second mark begins GYÖN…, possibly Gyöngyös, which remains a guess. No change to the reading.

## Checked and accepted

- Row 4 and row 7 *a* for *n*: the two bars are clear and horizontal in both places, so the two emendations are correctly disclosed as emendations. The sense supports them, and I found no reading that keeps the bars.
- Row 17 *viszolátásra*: there is a blank gap between the o and the small wave and no hidden sign (`z_r17viszo.jpg`), so *[ont]* is rightly bracketed.
- Row 14 *sor*: no right bowl follows the r before the six.
- Row 9 filled ring: an over-inked ring, left out and disclosed.
- Row 16 *elfeledni* under the printed "Série 2285": the star-shaped f and the double-started l are as described; the word holds by sense.
- Only words the writer actually put in cipher are claimed: nothing else remains undeciphered, and the card has no second unenciphered clause apart from the stamp note and the address.

## What I could not verify

- What lies under the row 12 blot.
- The full postmark text; only fragments are legible.
- *Alszög* as a part of Jászárokszállás, and the meaning of the address abbreviation.
- Accents: many are absent or ambiguous at any scale, and I did not audit each ledger accent mark.
- The HistoCrypt article linked on the portal: I did not read it. SOLUTION.md says no published solution was found, and the portal attaches none; the orchestrator's register check found no record.
