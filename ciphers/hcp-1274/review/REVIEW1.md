ACCEPT

# Review 1 of HCP1274 (Claude Opus 5.5, reviewer, 2026-11-01)

The reading stands: I went through all 22 rows sign by sign and found no sign that changes a word or the sense. Four minor findings below are disclosure and ledger points. None blocks closure.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1274/work/decode.py` from the repo root: all four SHA-256 checks print OK. The literal rows match SOLUTION.md row for row, and the normalized text matches `work/normalized.txt`.
- **Independent decode.** `review/work/verify.py` holds my own shape-by-shape reading of all 22 rows, typed from my crops. It decodes through a map built from `../hcp-1216/work/graphic-key.json`, not through the solver's script. 21 of 22 rows match the solver's ledger exactly; the only difference is the last sign of row 19 (finding 1). Caveat: I had read the solver's text before reading the card, so this was not a blind transcription.
- **Pixels.** I made my own crops from `work/hires/*_adr.jpg` in `review/work/`: b0–b5 at 2x cover every row, and z_* at 2–8x cover the doubtful signs. Crops of the stamp box and the bottom right are `stamp.png` and `br.png`; the picture side is `pic.png`.
- **Key.** All 340 ledger tokens (338 read signs, 2 struck) fall in the family classes. Of the 24 letter classes used, none is new to this card.
  - The a/e (two against three bars), n/m, u (short plain X) against z (tail) and t/r calls hold where I checked them.
  - The stamp's rust-coloured dots at row 20 (*istEn*) sit on the ends of the bars and hide nothing; the e has its three bars.
- **Each disclosed uncertainty, on the pixels:**
  - Row 3 first sign: two tall strokes, the second clearly longer. This is the card's short+long d pattern, and *tudatnom* is sound. It is disclosed as resting on word sense.
  - Row 3 *a*: top bar plus a blot, as stated.
  - Rows 6 and 12: *hasztani* really lacks *la*; *halaszta|ni* is full. Both spellings are as written.
  - Row 8: *k e s* is really there, with three bars, so it is not *kis*. The dotted i is absent, which makes the solver's "(or *kis*)" alternative weak but harmless.
  - Row 17: *g o l j ö r a m a k i*. Every sign is clear, the two marks over the o are visible, and no *nd* is hiding.
  - Row 18: *d o g o z i k*; no l between o and g.
  - Row 18 *mikot*: the last sign has no mid-bar. Its top bar ends in a small returning hook, which could tempt a reader to F. The same hook ends the t of *boldogságot* (row 13), so t as written is right and *mikor* is an emendation, as disclosed.
  - Row 19 first sign: the overlap with the row 18 o is real, and the right-bowl reading with a lead-in stroke is sound. Row 18 o's loop is inked solid where they touch.
  - Row 16: joined n with the full stop after *a*, as stated. Rows 2 and 12: writer's own strikes, as stated.
- **Language and sense.** Continuous period Hungarian with the writer's habitual single consonants (the family's *kel*, *akor*). *rőfös kereskedő*, *berendezés*, *kénytelen*, *viszontlátás* are real words used correctly. The excuse is concrete and the addressee and signature match the plain text. There is no sign of words forced onto noise. English and Slovak match the normalized Hungarian, including the formal address.
- **Unenciphered parts.** The address reads as stated. Stamp box: *csokolom szam talan szor sirig hü Feri* confirmed under the printed circle. The printed picture-side text is confirmed, and the picture side has no handwriting (only printed series number 2802/3).
- **Sources.** No published solution appears on the portal capture. The solver discloses not reading the HistoCrypt article.

## Findings

1. **minor. Row 19 last sign is ledgered as E without comment.** At 6x (`z_kelene.png`) the sign shows a clear top bar and one lower, kinked stroke, not three separate bars as the e just before it nearly shows (its two lower bars almost touch). It is either a two-bar a (*kelena*, a slip) or a three-bar e with the lower bars run together. Fix: mark this in the ledger or the uncertainties as a call resting on word sense. Normalized *kellene* stands either way.
2. **minor. The h/p call is not disclosed.** All 5 h signs on this card (*hogy*, *hét-*, *hasztani*, *halaszta-*, *élvezhettem*) are tall+short. That is the shape the family key records as p or the h/p near-homograph (`tall-short-stroke` in HCP1216's graphic-key.json; HCP1243 gives h as two separate tall strokes). SOLUTION.md's table gives h without saying so and says p does not occur. Every instance is lexically forced (*pogy*, *pét*, *pasztani* are no words), so the reading is safe. But "applied without change" hides that h here is a word-sense call, and that the d (short+long) and h (long+short) descriptions are this card's own hand rather than the family wording. Add a line.
3. **minor. Two small marks are not accounted for, against the claim "no sign left over except the two the writer struck".**
   - Row 11, immediately after the first i (*ni*): a separate narrow pale loop, lighter than the surrounding ink, sitting low between rows 11 and 12 (`z_oval.png`). It matches no key class.
   - Row 4: the second ö of *örömeit* is heavily overwritten; the reading ö is sound, but the correction is unmentioned.
   - Neither changes the text. State them, and soften the claim. A stray dot above the row 11 n can go in the same line.
4. **minor. Small inconsistency in the uncertainties.** Item 5 calls *go[ndo]ljö[n]* "the one word not fully written", but items 3 and 6 list *ha[la]sztani* and *do[l]gozik* as also short of letters. Item 5 also cites *gondolj[ö]n* / *gondoljon* while `work/normalized.txt` prints *go[ndo]ljö[n]*. Say which form is the normalized one. Item 4's "(or *kis*)" could be dropped or qualified: the sign is e, not i.

The rule that a card with an un-understood word counts as complete only if the word is alone does not bite here. *Go[ndo]ljö[n]*, the *kes* false start and *mikot* are all accounted for, and no clause is unread.

## What I could not verify

- I did not read the HistoCrypt article, so I cannot say whether it publishes this card.
- The struck material in rows 2 and 12 cannot be read beneath the strokes.
- I did not independently confirm what the *berendezés* job was, beyond the plain sense of the sentence. The word-division choice *oldala mellé* against *oldalam mellé* stays open, as disclosed, and it does not change the translation's sense.
- Which of ö/ő is meant in *rőfös* cannot be told from the signs, as disclosed.
