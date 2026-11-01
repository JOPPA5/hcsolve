REVISE

# Review 1 of HCP1253, Claude Opus 5.5 (reviewer), 2026-11-01

The reading stands: this is the Jolánka family MASC and the letter body is correct. Two concrete ledger fixes are needed. One written sign was missed at the end of row 2, and one sign in the stamp box was misread, which turns *Imádja* into *Imádója*. The Hungarian closing and its translations change. Neither fix alters the sense of the letter body.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1253/work/decode.py` ran. All four SHA-256 checks print OK and match SOURCES.md. The output matches the literal text and the normalized Hungarian in SOLUTION.md.
- **Independent decode.** `python3 -I ciphers/hcp-1253/review/work/decode_review.py` holds my own transcription, in my own sign names, and my own key. It compares base letters with the solver's ledger and reports two differences only: row 02 and S4 (findings 1 and 2). All other rows agree. Caveat: I had read the solver's text before transcribing, so this is a check against the pixels, not a blind transcription.
- **Pixels.** Using my own crops in `review/work/crops/` from the hires address scan, I read all 20 rows and all 7 box rows at 1.35x (`b0`–`b6`, `low`, `box`). The contested places were read at 2–6x: `eg1`, `e1`–`e3` (all row ends past the divider), `r13`, `r11`, `r16`, `r19e`, `r19f`, `r19s`, `r20`, `r20b`, `s1`, `s3s5`, `s7`.
- **Disclosed calls, checked on the pixels.**
  - S1 blot: only one heavy stroke survives, and the space to its left lies in the stamp stain, so a left bowl would fit. It is a fair restoration and is disclosed as one.
  - Row 13 `#`: two strokes crossed by two bars, overwritten; n rests on sense, as disclosed.
  - Row 13 t: overwritten, with a thin extra stroke, as disclosed.
  - Row 19 final sign: heavy retouched right bowl, as disclosed.
  - Row 19 cs: the "6 + stroke" shape, as disclosed.
  - Row 20 *v e é d e s e m*: no hidden *le*. The omission is real.
  - Left bowl where s is needed in rows 1, 12 and 15: confirmed.
  - S4 first sign: h/p shape, as disclosed.
  - S6 d as two strokes: as disclosed.
  - S7 f: a cross, crossing near the middle, unlike the j base bar on this card.
- **Key coverage.** Every token decodes. No value of the key is contradicted anywhere on the card apart from the disclosed left bowl.
- **Language.** The text is period Hungarian in the family's register. *Tóth Jolánka, Jászárokszállás* is visible in the address, and the postmark *22* fits the file date.
- **Picture side.** The couple photograph has no handwriting, only the print number, as stated.
- **Sources.** Portal metadata: no solution attached. I saw no sign of a published solution being used.

## Findings

1. **major: a written sign is missing from the ledger at the end of row 2.** After *e s z e*, past the printed divider, there is one more black-ink sign, an open loop with descender: g. It is in the same ink and hand as the rest. It is not the grey postmark ring it overlaps, and it matches the g earlier in the same row. See `review/work/crops/eg1.png` and `e1.png`. Row 2 therefore ends *joegeszeg*, and row 3 begins *ben*: *egész[s]ég|ben*. A tick also stands above the last e of the row, so that e is probably é.
   - SOLUTION item 9 says "*sé-g* are not written", and that is false for the g and the é. Only one s is missing, and the writer's form is *egészég-ben*.
   - The "Why it is correct" claim that the ledger gives the card sign for sign does not hold until this is fixed.
   - Fix: add `G`, and `E:acute` if the solver agrees, to ledger row 02; correct the literal block; rewrite item 9. The normalized word stays *egészségben*.

2. **major: S4 is *imádója*, not *imádja*.** The second sign of S4 is read as "an i loop without a visible dot, which the normalization drops". On this card, in the box, the undotted loop with a crossing tail is exactly the o: compare S1's o signs (`s1.png`) with S4 (`s3s5.png`). The i of S3, in the same box, has its dot. The literal signs are therefore *d o j a* (with the disclosed h/p-shaped d and the overwritten j).
   - This needs no dropped sign. *Imádója* is also the closing word used across the family (HCP1250, 1258, 1265, 1267, 1275).
   - It also fixes the grammar. A verb *imádja* cannot be coordinated with *és sírig hű kedvese*; *imádója és sírig hű kedvese* is a proper pair of nouns.
   - SOLUTION item 3's claims that "*imádja* is the only sense" and "Sister closings have *Imádja Feri*" are not supported by the sister cards I searched. HCP1254 does have *imádja*, but in the body of that card.
   - Fix: ledger `I` → `O` in S4; literal *{d}o{j|t}aés*; normalized and ledger text *Imádója és sírig hű kedvese, Feri*; English roughly "Your adorer and sweetheart faithful unto the grave, Feri"; Slovak roughly "Váš zbožňovateľ a do hrobu verný milý, Feri"; rewrite item 3.

3. **minor: S7 and o/i.** Finding 2 means that undotted o and i are the same shape in the box. The solver's item 6 note about the final sign of S7 should say so. *Feri* rests on the undotted loop being i by word sense and family; it would literally be o.

4. **minor: stray mark in row 11 not disclosed.** There is a heavy tick between the m and the i of *mit* (`r11.png`). It is most likely that i's dot, displaced to the left. It does not affect the reading, but it should be noted.

5. **minor: "Only item 8 extends the key".** The table also carries *left bowl + stroke = cs*, a form not in HCP1216's table, used here in rows 11 and 19. Say which sister card gives it or list it as a second variant. The same applies to the h/p-shaped d in S4, which the table does not list.

6. **minor: *ugyanéz is régi*.** The English "even this is old" is one option. *Ugyan ez is régi* ("though this too is old") is another. Add it to the interpretation list.

## What I could not verify

- Rows 5–8 punctuation and the place meant by *le*/*lent*/*bejön*: the solver's alternatives are fair, and the card does not settle them.
- Faint acute marks: I did not audit every tick, only the ones in the crops above. They do not affect base letters.
- Sister-card evidence for left bowl = s: a text search hits other Jolánka cards, but I did not check those scans.
- First address word *Szépreményű*: it is overlapped by postmarks. It looks plausible, but I did not read it letter by letter.
- The cancellation place and full date: only *GY…*, *913 F…* and *22* are clearly legible. The year and month come from the file name, as disclosed.
