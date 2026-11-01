ACCEPT

# Review 1 of HCP1271 (Claude Opus 5.5, reviewer, 2026-11-01)

The reading stands. I tried to refute it from the pixels and could not. I found one wrong token in the ledger that does not change the Hungarian, plus small disclosure points. All are minor.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1271/work/decode.py` runs. All four hashes are OK. The output matches the literal block and normalized text in SOLUTION.md (264 signs).
- **Independent decode.** `review/work/indep.py` holds my own sign-by-sign transcription, typed from my crops under my own sign names, with the key taken from the HCP1216 legend. It differs from the solver's ledger in one letter (finding 1) and one token (finding 2). My transcription was made after I had read SOLUTION.md, so it is not blind.
- **Pixels.** My crops are in `review/work/` (`rcrop.py`, from the hires original). I went through all 17 rows at 2x, then 2.5–4x for row 3, the blots in rows 12–15, row 16 and row 17. I counted bars on the a/e signs with taller crops, because neighbouring rows sit close (rows 3, 5, 6, 7, 17 checked this way). I also checked the plain insert *Gyöngyös Püspöki*, the stamp box and the postmark.
- **Key.** The table matches the HCP1216 family legend. Every sign on the card maps to a key value. No sign needs a new value.
- **Language and context.** The plaintext is real Hungarian of the period with family formulas. *Kívánom, hogy a legjobb kedvében találja soraim* is on HCP1303, and *mulatást kívánok* is on HCP1310. Gyöngyöspüspöki is a real place near Gyöngyös and within reach of Jászárokszállás, and HCP1303/1310 also tie the writer to Gyöngyös. 16 March 1912 was a Saturday. The postmark shows *2 MA* and *16*, which is compatible.
- **Portal.** Nothing in SOURCES.md or the metadata indicates a published solution. I did not re-open the portal.

## Restorations, judged on the pixels

| Place | What I see | Judgement |
|---|---|---|
| Row 1 k | Pink smudged but a recognisable section-mark outline | Sound; less damaged than `[k]` suggests |
| Row 9 c | Solid blot before the crossed z | Word sense only (*czím-* ×3); disclosed; sound |
| Row 12 j | Blotted, a wide base and a stem survive | Inverted T is compatible; sound |
| Row 12 ó | Pink smear, right arm and lower loop remnants, mark above | Rests on word sense; disclosed; sound |
| Row 13 n | Square blot | Word sense (*kívá-nok*); disclosed; sound |
| Row 14 d | Short-plus-tall shape survives under ink | Sound |
| Row 14 e | Three layers of ink (top curve, mid blob, lower bar), mark above | Three bars are visible; sound |
| Row 15 d | Heavy ink, stroke pair still visible | Sound |
| Row 16 ö | i descender of row 15 runs into the top of the loop | Dots are not provable; disclosed; sound |
| Row 17 *látásra* a's | Blurred bars | Disclosed; sound |

No reading here is forced beyond what SOLUTION.md admits.

## Findings

1. **minor: wrong token, row 3 sign 7.** `work/ledger.txt` row 3 has `6 A N` and the literal shows *kedvebantalaljaso*. The sign after the six has three bars (`review/work/t2.png`; the third bar lies low, close to row 4). It is e, not a, so the literal is *kedveben-*. The normalized *kedvében* is right, but as things stand it silently overrides the ledger and is not in the omissions list. Fix the ledger token and the literal block. The sign count is unchanged.

2. **minor: row 17 stray sign is probably not a sign.** `{s}` is read as a stray right bowl after the overwritten o. In `review/work/z17b.png` the stroke leaves the top of the dense loop and curls down, as the hooked arm of an ordinary o does (compare the next o, to its right). It is larger than usual, but it is more likely the arm of the overwritten o than a separate s. I would treat it as part of the o, which gives 263 signs and removes the "one stray sign" claim. The reading *csókolom* is unaffected. This is a judgement call, and if the solver keeps `{s}` it should note the alternative.

3. **minor: row 1 k not disclosed.** The ledger and literal mark `[k]` as restored, but Uncertainty 1 and NOTES.md do not list row 1. Add it, or drop the brackets, since the sign is legible (`review/work/a2.png`).

4. **minor: evidence missed in row 9.** Uncertainty 3 leaves *és pedig* against a name *Mises*. An accent stroke appears to stand above the e of `ese` (`review/work/c2.png`), which favours *és* over *Mises*. The sentence stays awkward, and the uncertainty should stay, but this should be noted.

5. **minor: English and Slovak commit to one side of Uncertainty 5.** Both say "going to work" and "to another workshop", while the verb is supplied and *műhelybe* may stand for *műhelyben*. The Hungarian shows `[megyek?]` but the translations do not. Mark the supplied verb in both. This is one elliptical clause; all its words are read, so it does not make the card partial.

## Could not verify

- Whether the row 16 loop carries ö dots, and whether the row 17 o had an accent: the ink hides them.
- The identity of the writer. SOLUTION.md claims none, which is right.
- The exact postmark date beyond the fragments, and the file-name date 16 March 1912 from an independent source.
- The last word of the address under the collector's stamp, beyond what is visible.
- A blind reading: this review saw the solver's text first.
