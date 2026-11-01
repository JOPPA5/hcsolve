REVISE

# Review 1 of HCP1259 (Claude Opus 5.5, reviewer, 2026-11-01)

The reading stands: Feri to Jolánka Tóth, Hungarian, Jolánka family key, 18 cipher rows that read through. I tried to refute it and could not. No finding changes the sense of the card. The fixes below are concrete, though: two editorial readings should change or be opened, and several calls that rest on word sense are not marked. The orchestrator's brief asks for those calls to be stated.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1259/work/decode.py` ran cleanly. All four SHA-256 values match, also by a separate `shasum`. Its output matches every row of "Literal decipherment" and the normalized text in SOLUTION.md.
- **Independent decode.** `review/work/my_decode.py` holds my own 18-row transcription in my own notation, made from my own enlarged crops, with its own sign table. It compares row by row with the solver's ledger. Result: 267 letters, row lengths equal, **one hard difference** (row 11, see finding 3). 12 further signs, all in blots or stains, I could place only by word sense (see finding 4).
- **Key coverage.** Every ledger token is in the key. Sign counts are spread like Hungarian (e 36, a 34, o 20, s 18, n 18, l 17). No sign is left over. c and f do not occur.
- **Pixels.** I read all rows on work/hires crops at 1.8x (`b1l`…`b5r`), and the disputed spots at 3–4x (`r6gap`, `r8`, `r9blot`, `r11`, `r15`, `r16g`, `r17`). The stamp box is levelled in `stamp33.png`, and `stamp-top-red.png` is a red-channel map of it. The address is in `addr1.png`, the postmark in `pm2.png`, the picture side in `pic.png`.
- **Restorations checked against pixels.**
  - Row 5 strike-through and rows 5–6 *ilo|na ylona*: as stated.
  - Row 6 pale pair: as stated. No t is visible, and the n/d call is disclosed.
  - Row 13–14 *tépni*: acceptable; first sign of row 14 is a blot.
  - Row 14 *ír{j}on*: wide foot visible, acceptable.
  - Row 17 e of *nyelvek*: one bar plus a wedge under the g tail of row 16; disclosed, and sense decides it.
- **Language and context.** The Hungarian is natural for 1912 and the formulas match sister cards. *Kedves*, *édesem* ×3 and *zavaros írás* ×2 recur independently. *Ojan* is on HCP1216 as stated, and *Ilonka* on HCP1263. Recipient and signature fit the family. I found no sign of a published solution, and the portal capture records none.

## Findings

1. **minor (fix needed). Row 17 end: *vela* is better read as *vel[e] a*, with no bar-count emendation.** The last sign is two clean bars (`b5r`), literally a. SOLUTION.md (Uncertainties 7, normalized text) forces it to e. But the family's closing formula is *Isten vele, a viszontlátásra*, literally *istenveleaviszontlatasra* on HCP1216 row 22, and *Isten vele! A viszontlátásra* on HCP1212. So the final a is probably the article, and this writer, who drops letters elsewhere, left out the e of *vele*. That keeps every sign as written. The normalized text should read *Isten vel[e], a viszontlátásra* (translations unchanged), or both options should be given. The line in "Why it is correct" about one sign needing a bar count should go.

2. **minor (fix needed). Row 9, first sign: *ily* is an open alternative, and "required" overstates *oly*.** `r9blot.png` shows the blot with a right spur. Directly above it stands a separate red dot that SOLUTION.md does not mention. Elsewhere on this card, marks between rows belong to the row below: the i dots, and the accents of *órái* and *írás*. A dot here points to the dotted i, and the right spur fits i's arm as well as o's. *Ily zavaros írás, mint itt van* is as good Hungarian as *oly*, and the sense is the same. *Ej* is not the rival; *ily* is. I cannot prove i, because the sign is hidden. The ledger and normalized text should show the first letter as unresolved i/o, or argue for one, and should mention the dot. Literal `{o}j` and normalized `[O]ly` assert more than the pixels show.

3. **minor (fix needed). Row 11, *lát-h-at*: the sign has the d shape, not the h shape, and this is undisclosed.** In `r11.png` the sign is a short stroke at upper left against a long stroke, the same form as d in rows 1, 4 and 8 (*kedves*, *édesem*). The h/p form in row 2 and at the end of row 13 is a long stroke with the tick on the right. The ledger writes `th` with no flag. *Láthat* is certainly the word (*ládat* gives nothing), so the reading stands, but this is a shape call on word sense. It must be listed. It also contradicts "only one sign (row 5–6 y) needs an emendation of shape". Row 8's first sign, a long stroke with a low short stroke, is also not a clean h and is worth a line.

4. **minor (fix needed). The ledger's `?` flag is not applied consistently.** Only three signs carry `?` (rows 9, 14, 17), although the header defines `?` as a blotted sign whose value rests on word sense. Heavily blotted signs without the flag: row 10 m (not mentioned anywhere), row 13 m, row 14 n, row 15 both h, row 16 r, a and g, row 17 n (not mentioned anywhere). The row 6 pale pair is also unflagged. Row 16's g is an ink blob with a long tail (`r16g.png`); it could be k by shape and is not named in Uncertainties. Row 16 rests on *rágódnak*, so that word is less secure than it appears. Flag these signs and add rows 10, 16 g and 17 n to Uncertainties 5. All of them read acceptably in the word.

5. **minor. Accents and dots are misdescribed.** Uncertainties 10 calls the small marks stray and says only the é of *remélem* and two á show. In fact the marks between rows are mostly real accents of the row below: ó and á of *órái* (row 3), é of *elég* (row 2), á of *írás* (row 9), and the stroke over the first e of *nézésel* (row 5). The solver's "supplied" accents are thus partly written ones. The dot beneath k (rows 1, 3, 13) also looks like part of that sign, so the "full stop" after *nyelvek* (row 17, k then dot) is not secure. It changes nothing in the text, but the statement and the key table should be corrected.

6. **minor. Address: *Szépreményű* is an undisclosed restoration.** `addr1.png`: the word ends at y, and paper damage begins at once. No ű is visible. HCP1250 prints *Szépremény[ű]* in the same situation. Write it that way here.

7. **minor. Postmark statement.** SOLUTION.md says the Jászárokszállás postmark reads 912 ÁPR 4. `pm2.png` shows …ÁROKSZÁ… with "91 ÁPR 4": no 2 is printed. The "912 ÁP" is on the second cancel, over the stamp box, whose place name is illegible except a final S. The date is right (with the portal file name) but the attribution should be corrected.

8. **minor. Stamp box top line.** I confirm it is about one word long, partly outside the box, with one loop visible at left, and I cannot read it either (`stamp-top-red.png`). Whether it is a deliberate deletion is not shown: the pink mass looks at least as much like a smear. The title line and translations say "scribbled-over" as fact, while Uncertainties 8 says "scribbled over or smeared". Use "illegible" throughout. One lost word at the margin does not make the card partial under the brief's rule, since the rest reads.

9. **minor. "Used unchanged".** The family legend (HCP1212, 1213, 1216) gives y as "low descender", whereas this card's y in *nyelvek* and *ylona* is the undotted crossed curve. That is well supported here, but it is a local variant, or an i without a dot, not an unchanged key entry. Say so. Also note that the picture side (printed verse *Szerenád. Ábránd.*, series number 2317) has no cipher; SOLUTION.md is silent on it.

## Could not verify

- Row 9 first letter, row 6 pale pair, top stamp line: signs hidden; see findings 2 and 8.
- Row 5–6 *ilo|na ylona*: the repeat as *Ilona* is the best parse, and the signs are as stated, but I cannot prove the writer's intent. *Írna* for *irán[t]* is also left open; disclosed.
- General, Description and Attachments tabs: `source/metadata.md` says the detail page timed out, so the statement that nothing is attached rests on the catalogue row. I did not re-open the portal. The solver disclosed this, but the capture should be retried if possible.

## Register

After the fixes this qualifies as a complete solution (no unread clause; one illegible word at the box top). Type MASC; not in register-exclusions.json or skip.txt.
