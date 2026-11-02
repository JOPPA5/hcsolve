ACCEPT

# Review 1 of HCP1302 (Claude Opus 5.5, 2026-11-02)

Reviewer's result: the reading stands, including the rows and stamp lines added in the 2026-11-02 revision. All findings are minor. Finding 1 should still be fixed before the report is written, because it concerns writing on the card that SOLUTION.md leaves out.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1302/work/decode_rev2.py` ran from the repo root. All four hashes are OK. The output matches the ledger and normalized text in SOLUTION.md. The script only prints a hand ledger, as SOLUTION.md says; it does no decoding from signs.
2. **Independent decode.** `review/work/rows.txt` is my own reading of all 19 rows and the stamp from my crops, written as shape-class tokens rather than letters. `review/work/indep_decode.py` applies the key table in `ciphers/hcp-1216/SOLUTION.md` and compares base letters with the ledger (accents stripped). Result: 381 letters, 11 differing, and every difference is a point the solver already discloses:
   - row 3 h for p (the h/p near-homograph, *vasárnap*);
   - row 11 b for the solver's literal 6 (same sign; *hatkor*);
   - row 17 r for t (the last sign of *cselédeket*);
   - row 19 *né?h?ég* against *népség*;
   - stamp l, m, s+z, g+h, which I left unvalued because the signs are not legible.
   No undisclosed difference remains, and the key needed no new value.
3. **Pixels.** I looked at every row at native hires scale and at 3 to 5 times enlargement for each claimed restoration: `review/work/r0103.png` to `r19b.png`, `z18num.png`, `z18ot.png`, `z19lesz.png`, `z19blot.png`, `blot_g.png`, `z19end.png`, `z19e2.png`, `r14e.png`, `r1s.png`, `st.png`, `st_pink.png` (my own pink-excess map).
4. **Disputed points, judged on the pixels.**
   - Row 18 *20-ikán*: a 2 with crossed foot, a large 0, then a dotted curve, a 5-shaped k tangled with it, bars, tick, two strokes. Accepted. The numeral is really there. *-ikán* with a numeral occurs on hcp-1298.
   - Row 18 *ot majd nem*: o, gamma, three strokes, two bars and an inverted T under the portal seal lettering, tall stroke with tick, two strokes, three bars, three strokes. All seen. Accepted.
   - Row 19 *lesz*: the sign before z is a closed-headed 9 shape, not the usual open bowl. It has no y stroke; the z after it is clear. Accepted as disclosed: shape plus sense.
   - Row 19 *né[p][s]ég*: n, é, a blot, a tall stroke with a foot, a short stroke, an inked-over mass, then three bars and g. I confirm the solver's description. The s is not visible; the word is a restoration from sense, and it is disclosed as such. *Kevert népség* is good Hungarian and answers the complaint about the servants. I found no better word. The word stands alone and the sentence reads without it, so under the run's rule it does not make the card partial.
   - Row 19 end *viszontlátásra*: a single right bowl, F, two bars. Clear to the card's corner. The first ledger's *-cs-* is correctly removed.
   - Rows 1 to 17: I confirm the ledger as read. In row 14 the a after the second t looks like three bars, but the top one is that t's detached crossbar, so *mulathattam* stands (`review/work/r14e.png`).
   - Stamp: right way up, S1 *csókolom*, S2 *számta*, S5 *imádó*, S6 *ja Feri* are read. S3 *lan[s]zor* and S4 *sírig [h]ű* rest on the formula, as disclosed (see finding 3). The closing formula is on hcp-1216 as the solver says.
5. **Language and context.** Period Hungarian, with this writer's habits (dropped double letters, *se* for *sem*). The mention of Árokszállás agrees with the address. Sender Feri and the closing agree with the family.
6. **Sources.** `source/metadata.md` shows no attached solution. SOLUTION.md credits the sister-card parallels. I found no sign of an unattributed published solution.

## Findings

1. **minor. Plain-hand word on the address side is missing from SOLUTION.md.** Above the postmark, in the same pink hand, stands *Szépremény[ű]*: visible through the y, with the end under the cancel (`review/work/plain.png`). It is the family's address formula (hcp-1220, 1223, 1224 and others). SOLUTION.md gives the address as "Tóth Jolán[ka] úrleány[nak], Jász-Árokszállás", which also brackets letters that are plainly written (*Tóth Jolánka úrleánynak*; only the end of Jász-Árokszállás runs under the portal seal). The run's completeness rule covers unenciphered matter, so state the full address as read: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás, with the ű noted as under the cancel. This does not change the reading.
2. **minor. "The date is not read; the cancellation is faint" understates the cancel.** Turned 180 degrees, the date block of the upper round cancel shows "…3-N-16", with rim letters around S-O (`review/work/pmk2.png`). A second, weak cancel below shows a number that looks like 28, upside down (`review/work/cancel2.png`). Record what is visible. I could not settle the format or year, and any interpretation should be labelled. A day of 13 or 16 would suit an invitation for the 20th, but that is only compatibility, not proof of *20-ikán*.
3. **minor. The ledger is less cautious than the text in S3 and S4.** SOLUTION.md item 7 says only the arms of z and the top of o survive, yet the ledger has them unbracketed: `l a n [s] z o r`. On my crops the sign after the blot looks more like a stem with a top bar than a z, and I would not read it without the formula. The first sign of S4 is also a solid blot with a stem and its shape is hard to confirm; the ledger has it plain. Write `[z] [o]` in S3 and `[s]` in S4. The words are not in doubt.
4. **minor, favourable. The accent on the last vowel of *népség* is missing from the ledger.** There is a tick above the three bars before g (`review/work/z19blot.png`). If it is an accent and not a stray stroke, the ledger's `e g` should be `é g`. That is the spelling *-ség* needs, so it gives the restored word some support from the pixels. Separately, the ledger marks `(?) [p] [s]`, so the p is correctly flagged as resting on sense: read literally it is the h/p sign.
5. **minor. Translations flatten the name.** *Jolánkám* is "my Jolánka" (compare the wording on hcp-1216); the English and Slovak give "Jolán" twice, dropping the diminutive and at the opening the possessive. Also, *kis angyalka* may be a person: *Kis Angyalka* could be a surname plus a pet name, as well as "a little angel". SOLUTION.md notes that it may be a nickname or person, but the translations should carry the same hedge in the report.

## What I could not verify

- The value of the blotted signs in row 19. No channel, including the green-channel stretch `review/work/blot_g.png`, shows the s. Below the mass's top bar a loop can be seen, closer to an overwritten S-shape than to a bowl, but I cannot give it a value.
- The postmark's place, format and year; hence no calendar check of "vasárnap" or the 20th.
- The identity of Feri and of the person at the party.
- Whether the first sign of row 1 is a struck false start; I agree it has no value.
