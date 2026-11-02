REVISE

# Review 2 of HCP1226 (Claude Opus 5.5, reviewer, 2026-11-02)

The key, the type, the whole transcription and the reading of the card stand. The closing corrected after review 1 is right. One concrete fix remains: the new division of row 27 breaks the plain verb *lesznek* and adopts a sense that the Hungarian does not give. The sentence is better read as *modorom[mal] meg lesznek elége[dve] talán*. This changes one clause and not the drift, so another review round is not needed if the solver makes only this fix.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1226/work/decode.py`: all four SHA-256 hashes OK. A scripted comparison of the output with the literal block in SOLUTION.md gives 28 of 28 main rows equal; the stamp rows and the normalized text also match by eye.
- **Independent decode.** `review/work/verify2.py` has its own sign map over the ledger, and compares 17 rows against my own transcription from the new crops (rows 1, 2, 13, 18, 20, 21, 26, 27, 28, edge, S1 to S7). 724 tokens, no differences. Row 18 was compared with e in the scribble position, by sense as the solver states. The ledger was in view, so this is independent in code and pixels, not blind.
- **Normalized text against literal letters.** `verify2.py` also aligns `work/normalized.txt` with the literal letters and lists every letter added, dropped or changed. 19 differences; all but one are disclosed (finding 3).
- **Pixels.** New crops in `review/work/r2/`, 1.2x for all rows (`l1.png` to `l5.png`), 2x for rows 26 to 28 following the card's slope (`m2627.png`, `m28.png`, `r27a.png` to `r27d.png`), 4.4x to 5x on row 27 (`z1.png`, `z2.png`), 4x on the stamp (`st.png`), plus the green-suppressed `review/work/s4i.png`.
- **Published solution.** None named and no sign of one; the key transfer is disclosed. The family formula is cited as support, not as source.

## Findings

1. **major: row 27, the adopted division and sense do not hold; adopt *modorom[mal] meg lesznek elége[dve] talán*.**
   - The signs are as the solver says. `m2627.png`, `r27b.png`, `r27c.png`: `...m o d o r o m | m e g | l e s z n e k | e l e g e | t a l a n | a m u g y i s...`. The two sets of three strokes at x about 907 to 954 and 1016 to 1078 are one m each (`z1.png`), with nothing between them and no insertion above the row. The correction to *talán* is sound, and it is a real gain on both earlier readings.
   - The adopted reading (a) *modorom meg lesz nek[ik] elege talán*, "my manners will perhaps be enough for them", is not what those words give. "Enough for them" would be *elég lesz nekik*. *Elege* is the possessed form, found in *elege van/lesz* "is fed up", which is reading (c). So (a) silently equates *elege* with *elég*, which item 1 does not count as a change.
   - (a) also splits a complete word: *lesznek* "they will be" is on the card, and its plural fits the relatives as subject. Reading (a) has to break it and supply *-ik*, and then *meg* has no job except a weak contrast.
   - In (b) every word has its function. *meg* stands exactly where the resultative needs it (*meg lesznek elégedve*, "they will be satisfied"), the plural is the relatives, the instrumental is the regular government of *megelégszik/elégedett*, and *talán* closes it. Same construction in the family: *meg lesz örökítve* on HCP1275 row 25.
   - The two omissions in (b) fit this writer, who drops letters and syllables often: *szetném*, *ija*, *foglakozást*, *rokonin[ak]*, *legjob*. *Modorom[mal]* before *meg* is a natural skip (m... m...). Item 1 rejects (b) only for its count of additions, but (a) has a comparable count once its hidden change is included.
   - Fix: normalize as *Ami a rokonait illeti, modorom[mal] meg lesznek elége[dve] talán*, "As for your relatives, they will perhaps be satisfied with my manners", in all versions (normalized.txt, Hungarian, English, Slovak). Keep the brackets. Keep (c) as a stated alternative in item 1, and say that *-mal* and *-dve* are supplied. Status line: the clause rests on two supplied endings; every sign is clear. This is my reading of the sense, not something shown on the card, so the disclosure must stay.
   - Under the batch rule this is one soft word in a clause whose other words read, so I would count the card as complete after this fix.

2. **minor: Item 1's "I found no parallel" should be narrowed.** It is true for *modor* and *elégedve* (my grep over `ciphers/hcp-*/SOLUTION.md` found none), but the construction has the parallel in finding 1.

3. **minor: *kell* is not in the spelling list.** Row 4 has `kelki`, a single l. Item 7 lists the other normalized spellings but not *kel* → *kell*. Add it. The other 18 differences from `verify2.py` are disclosed in items 5 and 7 or are the row 27 supply of finding 1.

## What held up under attack

- **S3 and S4, the response to review 1.** `st.png` and `s4i.png` show in S3 three strokes for m (one crossing the triangle's left edge, one inside), the two a dashes, the stem of the six on the right edge, then o and the wave. In S4 the tick + long stroke, a partial arc, the g with its descender, an apex with two arms for v, and the dotted curve. *a boldog viszontlátásra* holds; the word sense helps on the o and, less so, on the v, and item 2 discloses the o. *Isten vele, édesem, a boldog viszontlátásra* is on HCP1248 and HCP1251 as claimed.
- **Row 27 end.** *amúgy is még azt írja* is clear, including the part under the postmark (`r27d.png`).
- **Row 26.** *eljö az az idö mit alig-alig várok amit a rokonait il|leti* is sign for sign as in the ledger. *amit* for *ami* is disclosed.
- **Row 28 and edge.** As in the ledger; *rokon[a]in|ak* accepted.
- **Row 18.** Blob with bar structure, disclosed; *eléjébe* accepted.
- **Rows 1 to 25, sample.** Rows 1, 2, 13, 20, 21 sign by sign, the rest read through on `l1.png` to `l5.png`, with no disagreement. Rows 15 (*sa+nos*) and 16 (*tehetem*, no *nem*) are as disclosed; the translation of row 16 keeps the sense honest.
- **Key and coverage.** All 724 tokens have a value; only the scribble is by sense without a sign. Nothing is fitted on this card.
- **Language and context.** Period Hungarian, formal *maga*, the family's formulas, addressee and signature fit. Repeated-word counts in "Why it is correct" check out (*édesem* ×5 with *édes|sem*).

## What I could not verify

- The tone of row 27 can only be argued from grammar and context; (c) cannot be excluded from the card alone.
- The o of S4 is partial, and its lower loop is lost.
- Postmark date and year, as in review 1. Accents are not in the ledger, so I did not check them sign by sign.
- Whose occupation row 28 means: the English keeps this open, which is right.
