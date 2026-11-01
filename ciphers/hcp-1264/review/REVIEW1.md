REVISE

# Review 1 of HCP1264 (Feri to Jolánka Tóth)

Reviewer: Claude Opus 5.5, 2026-11-01. The reading stands and I could not refute it. The fixes needed are to the record: one sign in the ledger is not what the card shows and the supporting claims are overstated. No word of the normalized text has to change.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1264/work/decode_opus.py` passes all four SHA-256 checks. Its output matches the literal table in SOLUTION.md row for row, and it prints the normalized text.
- **Independent decode.** `review/work/decode_review.py` holds my own sign table, built from the HCP1216 legend, and my own row transcription from my own crops (`review/work/crops/`, made by `review/work/crops.py` and `z.py`). Output: 423 signs and 28 of 29 rows identical to the ledger. The only difference is stamp row 6. This pass was not blind: I had read the ledger first. I went through every main row and every stamp row on 2x tiles, and through all disputed signs at 3.5x to 10x.
- **Key coverage.** Every sign falls in the HCP1216 classes. The exceptions are the struck sign (row 12), the two blots (rows 6, 7) and the extra tick (row 16), and all of these are disclosed. No key element is new. The key was not forced: letter counts look like Hungarian, and the text is continuous.
- **Language.** This is running, informal Hungarian of the period with the family's habits (*ijen*, *hejzetbe*, dropped letters) and formulas. Grammar and sense hold through all 23 rows and the stamp box. The English and Slovak follow the Hungarian.
- **Address and picture side.** Szépreményü / Tóth Jolánka / úrleánynak / Jász Árokszállás is confirmed on the hires scan. The picture-side printed verse, vertical words *beszél suttogva* and *hulló falevél*, and number 2203 are confirmed, and that side has no cipher.
- **Sources.** The portal shows Not solved with no attached solution, the directory holds no external plaintext, and the number is not in skip.txt or register-exclusions.json.

### Disputed signs, judged on the pixels

| Place | Finding |
|---|---|
| Row 6 `r[a]m` | Curved top bar with a solid blot below. Correctly disclosed; the restoration is by sense. |
| Row 7 `tud[a]tom` | Same. Correctly disclosed. |
| Row 15 `<vagy>` | Small caret v and two-bar a are clear. The third mark is only a forked mark on the top of the n stroke, so g is sense alone. The fourth mark, with arm and loop, is a reasonable small y. See finding 2 for what follows it. |
| Row 12 struck sign | Vertical stroke through three bars. Agrees with a deleted e. |
| Row 16 `D'` | Tick, long stroke, thick tick. Agrees with the solver's description; only *de* gives sense. |
| Row 17 `rólam` | Short thick third stroke, as disclosed. |
| Stamp 1 | The sign before m is a bold gamma, not o. The solver's `{t?}` is right, and normalizing to *Csókolom* is honestly labelled. |
| Stamp 4 `sirihü` | No g on the card. Dot left and tick right over x. Agrees. |
| Stamp 5 `kedvesse` | Two hooks and a stained final sign. Agrees. |

## Findings

1. **Major: stamp row 6, the first sign of the signature is misrecorded, undisclosed, and used as evidence.** The ledger has `+` (f). The card shows a symmetric X of two 45-degree diagonals, the same shape as the plain x = u signs on this card (compare row 17 *ü* crops, stamp row 4). It is not the upright cross of row 13, row 16 or row 23, whose stem is near-vertical with a horizontal arm. See `review/work/crops/feri_stamp.png`, `feri_r23.png`, `f_r13.png`. The HCP1216 stamp signature has a slanted f, so a careless f is the likely explanation, and *Feri* is surely the sense. However, the literal output `feri` is not what is written (`ueri`), the uncertainty list says nothing about it, and "Why it is correct" counts *Feri* ×2 as identically decoded proof. **Fix:** give the sign its own ledger token (e.g. `X?`), print it as literal `{u/f}`, keep *Feri* in normalization as a call on word sense, list it under uncertainties, and drop it from the repeated-words evidence.

2. **Minor: an ink mark after the row 15 insertion is not reported.** Directly after the small y, on the same interlinear level, stands a double blot with a small loop at its left end, touching the foot of the h of row 14 (`review/work/crops/blob.png`, `ins.png`). It may be a plain blot. It also sits exactly where *-ok* would go, and the solver's first-person reading depends on *vagy[ok]* being truncated. I cannot read it as letters. **Fix:** mention it in item 3 as possible but unreadable.

3. **Minor: the row 21 *i* of *csütörtökig* rests on sense and is not disclosed.** The sign is heavily blotted or overwritten in its upper half and no dot is visible. Loop, crossing and right arm allow i but also o (`review/work/crops/k21b.png`). The k before it is a small closed 8, unlike the open S of the other k signs. The heading "Restorations (the only signs hidden on the card)" is therefore too strong. **Fix:** add both to the uncertainties and soften the heading.

4. **Minor: the numbers in the support section are wrong.** The ledger gives *hogy* ×5, not ×6, and *édesem* ×4 (plus *édes* once), not ×5. There are 423 written signs: the 426 tokens include the `<`, `>` and `-` marks, so "426 tokens" and "all 426 tokens" should read 423 signs.

5. **Minor: the date evidence is under-reported.** SOLUTION.md mentions only GYÖN… and "I do not claim a date". A second, faint postmark at upper left, rotated, shows **FEB** with a numeral 1 before it (`review/work/crops/pmA.png`). The day and year are not legible enough to me either. **Fix:** record the month as visible, still without a full date.

## Could not verify

- The small g of `<vagy>`, the letter content of the blot in finding 2, and the true value of the blotted signs in rows 6, 7, 21 are beyond what the scan shows; those calls are from sense.
- Whether *vagy* is first person is unsettled. The solver's sense argument is reasonable and disclosed.
- The full postmark date.
- The dots on every ö/ü were not audited one by one. Accents do not change any word here.
- "Thursday" and the party cannot be tied to any outside record.
