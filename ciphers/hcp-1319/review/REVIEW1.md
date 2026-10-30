REVISE

# Review 1 of HCP1319 (Claude Opus 5.5, reviewer, 2026-10-30)

The message stands: Feri-family Hungarian monoalphabetic substitution; departure put off a week, grape harvest, Sunday arrival. But the ledger and the printed "literal" text contain one letter that is not on the card, and that restoration is not disclosed. Sign count and coverage claims are wrong as a result. Concrete fixes are below.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1319/work/decode.py` ran: all four SHA-256 OK, output identical to the literal rows and normalized text in SOLUTION.md, 158 signs.
- **Independent decode.** I read every row from my own 2x-to-10x crops of the hires scan (`review/work/crop*.py`, `review/work/crops/`), wrote my own ledger in shape codes rather than letters (`review/work/ledger_review.txt`), and decoded and diffed it with `review/work/dec.py` (`python3 -I ciphers/hcp-1319/review/work/dec.py`). Result: 11 of 13 rows agree sign for sign. Row 3 differs by one sign (finding 1). Row 9 differs only because I keep the four strokes as one token (solver's item 5). My count is 156 tokens; solver's is 158.
- **Key.** Checked against the HCP1216 table. Every sign is in the family key; no new values. Key covers the whole cipher text, apart from the disputed signs below.
- **Word-sense calls.** Rows 3, 7, 8, 9 checked on enlarged crops. Solver's items 1 to 8 are accurate descriptions of the pixels, except as noted in findings 1 and 3.
- **Language and context.** Period Hungarian, coherent. Formula, address and formal *vele* match HCP1212/1216/1217. Family cards HCP1303 and 1304 (not yet FINAL) also mention conscription.
- **Postmark.** Rotated crops (`z_pm-105.png`, `z_pm75.png`) show 12 SEP, then a place name I could not read. Consistent with the file name 1912-09 if 12 is the year.
- **Picture side.** Print only; no handwriting or cipher.
- **Stamp field.** Line 1 is plain cursive *csókolom*. Line 2 is cursive, not family signs; I could not read it either.
- **Sources.** Portal status and absence of attachments as recorded. I saw no sign of a published solution being used.

## Findings

1. **major: row 3 has a sign that is not on the card, undisclosed.** The ledger reads `U T A Z A S`. The scan shows five signs: cross (u), gamma (t), crossed diagonal (z), two bars (a), right bowl (s). Nothing stands between gamma and z. Evidence: `review/work/crops/z_r3utazas.png` (also `r03_0.png`). The literal text is **utzason**, and *utazason* is forced from the word. The writer drops letters elsewhere (*holna*, *hetel*, *kesobre*), so *el-ut[a]zásom* is a sound normalization. The fix is not to the reading but to the record:
   - remove `A` from ledger row 3, so the literal row becomes `utzasonelhalasz`;
   - normalize as *elut[a]zásom[at]*;
   - add it to Uncertainties alongside item 6 (the same word also has n for m, so this word carries three editorial changes, not two).
   SOLUTION.md's "Long words come out letter by letter" should not be read as covering this word.

2. **minor: sign count and coverage claims.** "158 signs" in the status line, `Why it is correct` and the decode output depends on finding 1. Fixed count is 157 with row 9 counted the solver's way (n + m). State it that way, or note that row 9 has four strokes rather than five.

3. **minor: row 9 first sign has a dot; item 4 says none is visible.** A dark dab stands up and to the right of the sign, at the end of a pale smear from the v-stem of row 8 (`z_r9start.png`, top left). That is where the dots of the other i signs sit (row 10 and row 11). It very likely is the i dot, smeared. This strengthens *i*; change item 4. The third sign of the row really has a straight tail and no marks, so by shape it is i class and *idő-* rests on sense, as the solver says.

4. **minor: *sorozat* is still unconfirmed and the family evidence points the other way.** Two web searches found no attestation of *sorozat* as "recruitment muster", and item 1 says the solver did not check either. Family cards use **sorozás** (HCP1303 *sorozás lesz*; HCP1304 literal `sorozas`), and HCP1303 puts the draft in April, not September. The sign itself: the dark overwrite has a stem and top bar and no separate mid-bar, so it is gamma-shaped, with the pale z arm lying where a mid-bar would be. Only word sense makes it r. Solver's flag is honest, but add these points, check a period dictionary if possible, and keep the clause tentative in the English and Slovak.

5. **minor: "complete reading" in the status line.** With rows 7 and 9 and the omissions above, *complete in that all signs are assigned, with one word's meaning unverified* is more exact. Stamp line 2 being unread is already disclosed.

## What I could not verify

- The meaning of *sorozat* as used here; the identity of the sign under the row 7 overwrite beyond "z over gamma/F shape".
- Whether a third bar is hidden under the row 3 blot (a vs e in *halaszt-*); sense decides.
- Whether the row 5 dots are ink accents or spatter from the adjacent stain; *sz[ü/u]retre* either way.
- Stamp line 2, the sender (no *Feri* on this card) and the postmark place.
- The picture-side rotated print was not transcribed in full.
