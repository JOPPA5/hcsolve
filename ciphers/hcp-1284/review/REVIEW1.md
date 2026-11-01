REVISE

# Review 1 of HCP1284 (Claude Opus 5.5, reviewer, 2026-11-01)

The key, the transcription of 21 of 22 rows and the general content stand. Two concrete fixes are needed: row 17 is mis-segmented and very probably contains *nem*, and row 10 is mis-divided, which changes the sentence and its translations. Neither needs a new DONE round unless the solver's response changes more than these sentences.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1284/work/decode.py` runs; all four SHA-256 checks OK; output equals the literal block and the normalized text in SOLUTION.md. Note that the script only prints the manual ledger; it applies no key, as SOLUTION.md says.
- **Own decryption.** `review/work/my_signs.txt` is my own sign-class transcription (292 tokens; classes, not letters) from 3x to 5x crops of the hires address scan (`review/work/crop.py`, `crop2.py`, `review/work/crops/`). `cd review/work && python3 -I decode_review.py` applies the HCP1216 table to the classes and diffs against the solver's ledger. I had read the solver's ledger first, so this is not blind. Result: 18 of 22 rows identical; the differences are rows 3, 11, 13 (known word-sense calls, findings 3 and 4) and row 17 (finding 1).
- **Coverage.** Every sign in the 18 main rows and the 4 rows in the stamp box was looked at on crops; every class maps through the family key. No extra key values are needed. The key is genuinely unchanged from HCP1216.
- **Disputed spots at 5x:** row 5 and row 13 first signs, row 9 last sign, row 11 Gamma and last sign, row 13 heavy sign, row 14 start (*r a v a n*: the sign under *kocsin* is two bars, a, not e), row 15 last sign, row 17 middle, row 18 first word, the stamp block, the *Kelt* line, left postmark. Picture side viewed.
- **Language and context.** Period Hungarian, the writer's known spellings, family formulas. Gyöngyös fits HCP1244/1245/1271/1303. A place *Szentjakab* in Heves county appears in the Hungaricana urbarial listing (https://archives.hungaricana.hu/en/urberi/heves-szentjakab); I did not establish that it is this place, only that the name is not invented.
- **Sources.** No published solution; the SOLUTION.md statement on that is consistent with SOURCES.md and metadata. The key transfer is disclosed.

## Findings

1. **major. Row 17 is mis-segmented; the word before *eszünk* is very probably *nem*.** See `review/work/crops/r17mid.png`. After the dotted i the pixels show: one long stroke; a pair of strokes under a thin bar; two bars plus a separate top bar (e); then **three evenly spaced strokes, the first heavy with a small tick**; then e, s, z, ü, n, k. That last group is an ordinary m: the first stroke of m carries the same tick in row 2 (*kam*), and row 8 and row 16 have similar ticked strokes in m. The solver's ledger splits it as `{t'} n`, with no parallel, though SOLUTION.md uncertainty 1 mentions the m option in passing. Taking it as m, the pair + e + m reads **n e m**, directly before *eszünk*: the only residue is one stroke and the thin bar, and HCP1216 row 18 already has an isolated stroke of no value (its ledger class `|`). So the row reads `tanyan i | nem eszünk` (`tanyani|nemeszünk` in my decoder). The NOTES dead end "i+nem (needs a stray stroke)" was discarded too quickly, and SOLUTION.md's "*nem eszünk* would need the first signs discarded" overstates the cost. It also fits the preceding sentence: this life is not like yours; on the farm we do not eat cooked food. Fix: change the ledger to m for the last group; give *nem eszünk főtt ételt* as the main reading; disclose the unresolved i + stroke (*tanyáni*? a false start? *i[s]*?) and the unexplained bar. The alternative segmentation i, m (stroke + pair), e, m (*imem eszünk*) gives no word, so it counts against that division but cannot be excluded on pixels alone. Update the polarity statement, English and Slovak.

2. **major. Row 10 word division: *E tanya falutól*, not *E tanyafalutól*.** The letters are right, the division is not. As written the sentence has no subject (the solver supplies Szentjakab, uncertainty 10). With *E tanya falutól félórajárásnyira és Gyöngyöstől pedig 4½ órajárásra kocsin van* the subject is present and the pairing *falutól ... Gyöngyöstől pedig* is natural: "This farmstead is half an hour's walk from the village and 4½ hours by cart from Gyöngyös". Row 17 *a tanyán* continues the same subject. *Tanyafalu* occurs on no other card in this repo. SOLUTION.md also lists *tanyafalutól* among the proofs of correctness. Fix the Hungarian, English, Slovak, uncertainty 10 and the proof paragraph. The current English "half an hour's walk from this hamlet" says the reverse of the plain sense.

3. **minor. Row 3 *megkaptam*: the sign is literally d class.** On `rows01L.png`, third row, the sign is a short left tick + long right stroke, the shape of *pedig*'s d (row 13) and *edes*'s d (row 1), and not long + right tick as in *pedig*'s p or *hogy*'s h. So the literal is *megkadtam*. Uncertainty 8 files this as an ordinary h/p word-sense call. The reading *megkaptam* is safe, but the ledger token should say that the shape is d and the value is taken from word sense; a ledger which claims p here hides that.

4. **minor. Statement "This is the only restoration-type reading" (uncertainty 2) is not accurate.** Row 11 *r* (literally t), row 3 p, row 11 and row 15 final signs are also fixed by word sense, as the same list says. The row 13 sign itself, on `r13end.png`, is shaped like a retraced o (curl, heavy loop, arm to the right), which is not stated: "overwritten heavy loop with a top bar" should add that nothing of an s form is visible and the value rests wholly on *órajárásra*. Row 11 last sign is a very Z-like form; *a* is word sense. Disclosure, not reading.

5. **minor. Unrecorded side material.** The picture side bears a printed four-line verse beginning "Magácskánál mulat" and the publisher mark with 2523; SOLUTION.md says only that the side was not needed. Add one line. The left postmark shows at least *ÁSZ* and a numeral 2; "not read" is acceptable, but say it was tried. *Kelt 2 1 ?ra este* is as doubtful as the solver says; I cannot improve it (`kelt.png`).

## Confirmed without objection

Row 5 and row 13 heavy crosses as cancelled signs (their value is unprovable, but the text reads without them); row 9 *soraim*; row 9 *ro* with no l sign; row 15 *ojon* (clear o, clear second o) and *min*; row 18 *föt* with the tilted f; row 13 clear numerals; *kocsin* in Latin hand; stamp block *csokolom / szamta / lanszo / feri + r*, with the tilted F as the end of *-szor* continuing round the doodled o; address text.

## Could not verify

- The date of the card; the identity and location of Szentjakab.
- Whether the bar over the pair in row 17 has a meaning.
- Final wording of the row 17 residue i + stroke.

## Register

After findings 1 and 2 are addressed the card qualifies as complete under the run's rule: at most one small unresolved residue, the rest reads. Type label MASC, and role in the key-transfer form. No entry is permitted if the solver instead keeps a whole unread clause.
