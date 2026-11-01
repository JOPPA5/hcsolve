REVISE

# Review 1 of HCP1248 (Claude Opus 5.5, independent reviewer, 2026-11-01)

The decipherment stands: the key is right and the letter reads as coherent Hungarian. But the ledger has five wrong sign calls that I checked at 5x. One of them manufactured the "weakest sense point" of the solution: row 10 is not *ottan*, it is *ojjan* = *olyan*, and the supposedly broken clause is a complete sentence. The Hungarian, English and Slovak texts and the uncertainty section must be corrected before FINAL. No re-review is needed if the fixes are the ones listed here; that is the solver's call under README step 5.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1248/work/decode.py` ran. All four SHA-256 checks pass. Output equals the literal block in SOLUTION.md (32 rows, 617 tokens) and `work/normalized.txt`.
- **Independent decode.** `review/work/own_decode.py` holds my own sign-class reading of all 25 main rows and the 7 stamp rows, made from my own crops (`review/work/t00L…t09R.png`, `stamp.png`, `r2425right.png`, at 2.5x from the hires original) in a private alphabet, decoded with the HCP1216 sign table and compared per row with the solver's ledger. 28 of 32 rows are identical (accents ignored). Rows 10, 12, 18, 20 differ; see findings 1 to 4.
- **Token count.** My 611 signs + 3 literals (Okt, 5, 15) + 2 DOT tokens = 616, one fewer than the ledger because of the extra t in finding 3.
- **Key coverage.** Every written sign has a value under the unchanged family key; only the writer's blot in row 15 has none. *gy* as two signs here, against one joined sign on HCP1216, is disclosed and I confirm it.
- **Disputed signs at 5x** (`review/work/z_*.png`): see findings, plus these confirmed:
  - Row 9 *azt*: `z_r9_azt.png` shows a heavy A-like sign with a stroke crossing to the right past the blue line. z from context is a fair call and is disclosed.
  - Row 15 blot: confirmed; a solid triangular blot with a dot beside it.
  - Row 19 *is csak*: `( )` opposed bowls confirmed.
  - Row 24 k of *akarok*: upper loop above a pale abrasion; partial restoration, disclosed, fine.
  - Row 24 end *soraim* and row 25: confirmed, including `6` with a dark blot and a dot.
  - Stamp box S1 to S7: confirmed sign by sign, including the tick-right h of *hű*.
  - Row 6: final sign is two bars (`z_r6_end2.png`), so *vasutasoknak a* holds.
  - *Okt*, 5, 15 are plain.
- **Counts in "Why it is correct"**: *hogy* ×5, *mert* ×3, *mulat-* ×4, *rendező-* ×3, *nagyon* ×3 all check.
- **External.** 5 October 1913 was a Sunday (computed). Address side reads Őnagysága Tóth Jolánka úrleánynak, Jász-Árokszállás, matching the portal. `register-exclusions.json` and `skip.txt` have no entry for 1248.
- **Period language.** Formal *maga* address, *szüreti mulatság*, *rendező*, *belépnék rendezőnek*, closing formulas: all natural for the period and the family. Not noise forced into words.
- **Sources.** No published solution is used; portal attaches none. SOLUTION.md credits the key's origin correctly.

## Findings

1. **major. Row 10 is *ojjan*, not *ottan*; the "broken" clause does not exist.**
   Evidence: `review/work/z_r10_ttan.png`. The two signs after *hogy o* are both clear inverted T (⊥), the family's j, the same sign as in *jön, jó, jöt, eljön, jelenteni, gondolja, mijen*. They are not the gamma Γ used for t everywhere on this card (compare the Γ in the same crop's neighbour rows). The ledger's `O T T A N` is a misreading: it should be `O J J A N`.
   *ojjan* = *olyan* ("such"). This writer spells *ly* with j: row 13 *mijen* = milyen on this very card, and HCP1216 *ojan* = olyan.
   The text then runs without any break: *Azt előre ígérem, hogy olyan mulatságban még nem volt, és fogalma sincs róla, hogy milyen lehet egy pesti mulatság.* "This I promise you in advance: you have never been to such a ball, and you have no idea what a Pest ball can be like."
   Required: fix the ledger, literal block, normalized text, all three translations (remove "ottan…" / "there…" / "tam…"), and delete the paragraph that calls rows 10–11 the weakest sense point. Its statements "every word is read clearly" and 'with the word for "such" missing' are both wrong: the word is there. Add *ojjan* → olyan to the normalization list.

2. **minor. Row 12 first sign is three bars with a dot: *és*, not *ás*.**
   Evidence: `z_r12_first.png` shows three separate strokes, with a separate dot above them. Ledger `A:a` should be `E:a`. Uncertainty item 6 ("two bars with an accent mark", "top bar reduced to a dot") describes something not on the card. Delete the item; no normalization is needed.

3. **minor. Row 18 *it* has one t, not two.**
   Evidence: `z_r18_itt.png`: dotted i, one Γ, a grey smudge with no ink stroke at the end of its arm, then n. The ledger's `I T T N A` has an invented T. Correct to `I T N A`, 616 tokens, and add *it* → itt to the normalization list (it fits *jöt, együt, kel, ezel*).

4. **minor. Row 20 is *lennék* as written, not *lannék*.**
   Evidence: `z_r20_lann.png` shows three bars after the wave. Ledger `L A N N` should be `L E N N`, and SOLUTION's "*lannék* → lennék (two bars visible, a for e)" must go.

5. **minor (word changes, sense does not). Row 18 end: the better reading is *szabadidőt*, not a dittography *-do-dot*.**
   Evidence: `z_r18_end.png`, `z_r18_compare.png`. The faint sign the solver reads o has a flat arm to the right with no descending curl, and a dot high above it. That is the shape of the i sign (compare the i at the head of the same row), not the writer's o, whose right arm curls down, as the last sign of this word does. After the d come the o sign with two marks above it (dot and tick) and t. Literal `S Z A B A D I D Ő T`: *szabadidőt kapni*, "to get free time". This needs no dittography.
   The faint sign is overwritten-looking, so I rate i as probable, not certain. The d under the blue line I accept (short stroke leaning on the left of the long one, joined at the foot). The statement in uncertainty item 3 that "no reading gives a different word" is wrong and must be replaced. If the solver keeps *szabadot*, it should give evidence against the i.

6. **minor. Claim to correct after the fixes.** "Every word is read clearly", and the opening row list, should be reworded to fit findings 1 to 5. Update `work/normalized.txt`, `work/ledger.txt` and the token count together so that the single command still reproduces SOLUTION.md. Add a note to NOTES.md on the misread j.

## What I could not verify

- The date: the postmark on the address side is partly struck (`z_postmark.png`); the year or month cannot be confirmed from it by me. 13 Sept 1913 rests on the portal's file name, as the solver discloses. The reasoning about the 15th stays an assumption, as disclosed.
- *b[ecses]* is a conjecture (disclosed); the card has only b and a dot.
- I checked accents only where they mattered. The ledger's accent marks were not audited one by one and do not affect the reading.
- Whether the sister card of the same day ("two cards at once") survives in the collection was not searched.

## Register

After the fixes this is a complete reading of the card and qualifies for an entry; the only unread item is the blot, a writer's correction.
