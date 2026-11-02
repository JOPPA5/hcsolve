REVISE

# Review 1 of HCP1232 (Claude Opus 5.5, reviewer, 2026-11-02)

The cipher type, key and nearly all of the reading stand. The solver's one "unresolved word" and the odd "I await my lines" come from a single misread sign in row 22. With it corrected, the sentence is the family's standard closing formula, so the card should have no unresolved word. A clause in the translation is also wrong (munkahiány). Both need fixing before FINAL.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1232/work/decode.py` from the repo root. All four SHA-256 checks pass, and the output matches the literal rows and normalized text in SOLUTION.md.
- Wrote `review/work/mydec.py`, which maps the ledger through sign classes taken from the HCP1216 table. Its 28 rows are identical to the solver's output (`mine.txt`, `theirs.txt`, diff empty). This tests only the ledger-to-letter step. The ledger's tokens are already letters, so see finding 9.
- Read all 23 main rows and the 5 stamp rows on my own enlarged crops of the hires address side (`review/work/crop.py`; strips L0-7, R0-7 and per-sign crops in `review/work/crops/`). Row count and sign order are confirmed. I found no sign outside the key and no omitted or invented row.
- Judged each restoration on the pixels:
  - Row 3 {l}: a wave is visible under the ring, as the solver says. The solver undersells it.
  - Row 4 {p}: two smeared strokes, left broader, right fainter. Compatible with p, not provable. Disclosed.
  - Row 6: the first t of "mit tudjak" is present, a red gamma inside the postmark's Δ (`r06.png`).
  - Row 8 {t}: a gamma with an ink pool. Agreed.
  - Row 11 {s}: a right bowl with an overwritten loop on its right side. Agreed, and disclosed.
  - Row 13 {n}: a blot plus one stroke. Agreed.
  - Row 15: the blot, the barred sign and the g of `csagak` are as described (`r15b.png`, `r15c.png`).
  - Row 16: `maga` is confirmed by the a bars (`r16.png`).
  - Row 21: `fogadta` confirmed, tick + long stroke.
- Sign-class overlap: g and y are separate signs here and c and s are separate bowls, as the solver says. k appears in S and 8 forms.
- Plaintext: real colloquial Hungarian, with the family formula in the opening, and Árokszállás matching the plain address. Picture side: printed verse and "Aranyeső" only, no handwriting.
- Family search: `grep` over `ciphers/*/SOLUTION.md` for the closing formula (finding 1).

## Findings

1. **major. Row 22 is misread: the sign read as chevron v is the crossed diagonal z. The word is `zarom`, not `varom`, and the "unresolved" sentence is the family closing formula.**
   - Pixels: `review/work/crops/cmp.png`, panels left to right: row 22 disputed sign, row 21 z, row 10 z, an unused panel (row 20), row 7 v, row 9 v. The disputed sign is a long rising diagonal crossed by a descending stroke, which is the same shape as the z of `aszobaaszonyom` directly above it (`r2122.png`). The clean chevron of row 7 has no crossing. The sign is overinked, which is probably how it was missed.
   - Literal row 22 becomes `azel{b}ezaromsoraim`, read as `azel bezárom soraim`.
   - Normalized: Azzal/Ezzel bezárom soraim. Maradok imádója Feri. English: "With this I close my lines. I remain your admirer, Feri."
   - Family support: FINAL cards have the same words decoded independently, for example `ezelbezaromsoraim` in `varokezelbezaromsoraim`, and "Ez[z]el bezárom soraim". `grep -l bezarom ciphers/*/SOLUTION.md` lists hcp-1235, 1237, 1249, 1255, 1277, 1279, 1281, 1308, 1310, 1315. *ezel* for *ezzel* is a known spelling on those cards.
   - This removes uncertainties 1 and 2. The solver's b is right, and "soraim" is correct as written: "my lines" is what the formula needs, so "sorait" was never required. The heavy sign's hollow foot now has word-sense support. The first sign of the row shows two bars (a), so the literal is `azel`, one letter off the usual `ezel`; say so.
   - The solver's "no sure sense" and the English/Slovak "I await my lines" must go, in all three versions and in `work/ledger.txt` (V to Z, with {B} kept as a disclosed overinked sign) and `work/normalized.txt`.

2. **major. Mistranslation of `munkahiány` in English and Slovak.** *Munkahiány* is a lack of work, not of workers (that would be *munkáshiány*). "because there is a great shortage of labour" and "nedostatok pracovnej sily" say the opposite, and the context supports the correction: Józsi is leaving to work elsewhere because there is little work here. Use "because work is very scarce" / "lebo je veľký nedostatok práce". Keep the disclosed point that `muka` omits n.

3. **minor. Row 5 is `remelem`, not `remelen`.** A third stroke stands exactly where the postmark ring crosses the row: the purple overlap (red under black) sits at stroke height and spacing (`r05.png`). The ledger should have M, and normalization item 15's "two strokes, n for m" should go. Mark the stroke as under the ring.

4. **minor. Row 14 has an ö: dots are written over the o of `könyvet`.** Two dark dots stand directly above that sign, between it and row 13 (`r14k.png`), in the same dark ink and position as the ö dots of rows 19-20. Item 15's "no dots written" is wrong. Ledger O:, literal `kiaköny`.

5. **minor. Undisclosed damaged signs in the ledger.**
   - Row 14, sign after b (`szombaton`): a thin top bar, a heavy blob and a thin bottom bar (`r14.png`). It looks closer to three bars (e) than to a. a rests on word sense.
   - Row 9, v of `elvesztem`: a chevron with an extra crossing stroke to the left (`r09.png`), possibly a correction. v rests on word sense.
   - Stamp S1, first sign: the left bowl has an inner curl and looks like a six (`stamp.png`). c rests on word sense.
   None changes the reading, but each should be listed, and the "Why it is correct" line "apart from one blot and the restorations above" needs to cover them.

6. **minor. "The postmark date is not legible" is too strong.** The Árokszállás postmark clearly shows the number 24 (`pm120.png`, `pm270.png`), although month and year are not readable to me. Report that, without claiming it is the day. The hires filename also contains `--24`.

7. **minor. Inconsistent gloss in the `fogadta` sentence.** English gives "[it/you]", Slovak "ma/to" (me/it). Use one set. Item 11 should also mention *szépen* as an alternative to *szívesen*, since `szesen` fits neither without a spelling error.

8. **minor. Normalization item for `tiszeletetet`** should say that the writer also repeated `et`, not only that a t is lost.

9. **minor. Reproduction.** `decode.py`'s KEY only passes letter tokens through, so the ledger is effectively already plaintext, and the card's key is not really applied by the command. The ledger's {S} and {B} tokens also bypass the stated `)` and `6` convention, against its own header. Say this plainly in SOLUTION.md or name the tokens by sign.

10. **minor. After finding 1, update status and evidence.** The title line "complete reading with one unresolved word" and the "Why it is correct" section should change, and the closing formula can be added as evidence. Note that the zarom reading came from this review.

## Assessment for the register rule

With finding 1 applied, no un-understood word or clause remains, so the card is complete and eligible for an entry (type label MASC). The sentence on `szesen` and the name Józsi remain disclosed interpretations, not unread text.

## What I could not verify

- Whether p (row 4) is really what was smeared there; it is word sense plus stroke count.
- The name form Józsi and the sign under the row 15 blot.
- Which book `a könyvet` is. The work-book reading is plausible but unproved, as disclosed.
- Identity of Jáger, Móczár, and of this Feri with HCP1216's Feri.
- Month and year of the postmarks.
- Whether a published solution exists: I did not open the Histocrypt paper linked on the portal. Nothing in the files suggests one was used.
