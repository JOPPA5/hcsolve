REVISE

# Review 1 of HCP1272 (Feri to Jolánka Tóth) — Claude Opus 5.5, reviewer, 2026-11-01

The reading of the ciphertext stands. Nothing I tried refuted it. Revision is needed because the plain-hand note under the stamp has an unread stretch of at least a line, which affects completeness, and because two unusual signs are recorded more confidently or less fully than the pixels allow.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1272/work/decode.py` ran. All four SHA-256 checks print OK, and the literal text is identical to the block in SOLUTION.md. It also matches the printed normalized text.
- **Independent decoder.** `review/work/indep.py` uses my own transcription of 18 rows, made from my crops, in its own sign codes. Its key is read from `ciphers/hcp-1216/work/graphic-key.json`, not from the solver's table. On base letters (306 signs, accents ignored) all 18 rows equal the ledger. The transcription was not blind, because I had read the solver's text first, so this is a check of the ledger, not an independent discovery.
- **Key coverage.** Every sign falls in a family class, and the only exception is the row 17 sign. No f occurs in the cipher (the name *Feri* is cursive). The family key needed no change, and the card uses no new sign class.
- **Scan check.** I checked all 17 rows and the address line on crops of `work/hires/*_adr.jpg` (`review/work/crop.py`, `review/work/crops/a1-a4, row17a/b, addr`), with 2–4x zooms of each disputed place: row 2 (`ly`), row 4 (`r4`, `r4e`), row 5 (`r5m`), row 9 (`r9`), row 11 (`blot`), row 12 (`at`), row 17 (`hump`, `end`), and the stamp note (`stamp`, `s_G`, `s_B`, `s_l6_7`).
- **Checks that agree with the solution.**
  - The six strokes in row 4 are 3+3.
  - Row 5 m is cramped, but three strokes are present.
  - Row 8 is m m e m as stated.
  - Row 9 *ha* is tall+short, then two bars.
  - Row 11 á is two bars, heavily blotted over something, and *Jász* is forced by the word.
  - The address line *szeretetel* is clear apart from a pink wash.
  - Row 17 *Feri* is cursive.
  - The picture side (`source/picture-large.jpg`) has only the printed verse, a printed caption and a postmark, with no handwriting.
- **Language and context.** The text is continuous, ordinary Hungarian. The formulas match the family (*Isten vele*, *sorait várva*, Feri, the formal address). Jászberény is plausible beside the Jász-Árokszállás address, and the file name and postmark give 30 April (1912 by file name). I found no sign of a published solution; the portal lists none.

## Findings

1. **major — The stamp note leaves more than a word unread, and SOLUTION.md does not state the consequence.** Crops `s_G`, `s_l6_7`. After *számtalan/szor* comes "a m…g" with a long descender, then a line of about a dozen letters ("r/so." then a word beginning t-e-m/n and ending with several joined letters), then *hű* and an unclear word. That is about a whole clause. The status line says the ciphertext is fully read, which is true, but the run's rule says a whole unread clause is partial and gets no register entry. The solver must state explicitly which applies: either complete for the ciphertext with the unenciphered note excepted, or partial. The rule does not clearly say whether it covers plain text, so the human or orchestrator may have to settle this. Until then, no `register-entry.txt` should be treated as automatic. The solver also has a useful parallel it does not cite: HCP1216's stamp note reads *csókolom számtalanszor sírig hű kedvese feri*, so the unread stretch may be a "faithful unto…" phrase. I could not confirm that on the pixels, and it must not be written in as a reading. Likewise *a mag…* is itself unsure, and *kedvese* should stay marked (?) because the last word's letters are not legible; it may be supported only by that parallel, and if so that should be said.

2. **minor — Row 17 token `{lm}` asserts more than is visible.** Crop `hump`. The sign has three arches and a closing tail, with no wave element. It matches the writer's own cursive *m* in *Szépreményű* (crop `szm`). The simpler description is a slip into cursive *m*, as in *lev|la* and *Feri*, with the l of *részéről* not written. SOLUTION item 2 calls it "two or three humps" and "l and m run together". The plaintext is the same either way, but the l is then a supplied letter: *részérő[l] más[ik] lapon*. Record the alternative in item 2.

3. **minor — Row 2 sign is transcribed as plain `L Y`, and the extra stroke is undisclosed.** Crop `ly`. Between *e* and the descender stands a wave followed by a further n-like arch with a short stem, then the *y*: not a plain one-hump wave. *melyet* is certainly the word, but the ledger omits the shape. This contradicts "only the sign in item 2 needs a special reading". Add it to the uncertainties. It also weakens "unlike the one-hump wave l" as an argument in item 2, since this writer's wave is not always one-humped.

4. **minor — Row 4 end: the F-shape alternative is not stated.** Crop `r4e`. The sign can also be seen as a single F (r) with a long top bar, not a gamma plus overlapping bars. Item 3 gives "double hyphen" as the explanation, yet no other row break on this card carries a hyphen, and it rejects only the letter a. *vet|tem* is right by sense, but *t* here rests on word sense, not the shape. State that.

5. **minor — Normalization of the opening is a choice not flagged.** *Levlapját* in the printed text is a verbless fragment, followed by "Igazán örömmel vettem tudomásul". The accusative may instead be the object of *vettem*: "Your card, for which many thanks, I truly received with joy; and noted that…". The sense barely changes, but the punctuation is editorial and the English and Slovak follow only one option. Note it, or re-punctuate.

6. **minor — Row 17 sense.** *más[ik] lapon* needs a missing k, has no verb, and its meaning ("on another card") is the solver's inference. Item 2 discloses all this, and the surrounding signs are clear. It remains the weakest part of the cipher. I found no better parse: the h value gives *lahon*, not a word. This stays a single uncertain phrase, not an unread clause.

## Could not verify

- The unread part of the stamp note, or *kedvese*, even with green and blue channel contrast.
- The year from the postmark alone; only "ÁPR 30" is legible to me, and 1912 comes from the portal file name.
- Accent marks sign by sign. My comparison was on base letters only, and accents are editorial in any case.
- That the family key is right beyond its fit on this card; I relied on HCP1216's accepted review.
