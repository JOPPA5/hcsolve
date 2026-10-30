ACCEPT

# HCP1212 – Review 1 (reviewer: Claude Opus 5.5, 2026-10-30)

Verdict: **ACCEPT**. The decipherment is correct. The key is the Feri/Jolánka graphic alphabet, the 17 main rows read as stated, and the plaintext is fluent Hungarian of 1912. There is one literal misreading in row 12 (`a földön` should be `e földön`). It does not change the meaning, and fixing it needs only a one-token ledger edit. The other findings are about documentation.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1212/work/decode.py` (from the repo root) runs. Both source hashes match. Its output is identical to the ledger output quoted in SOLUTION.md (rows 01–17, N01). Saved as `review/work/solver_out.txt`.
2. **Key.** I compared it with the accepted sister card HCP1301 (`ciphers/hcp-1301/SOLUTION.md`, key table). All 23 sign classes agree, including inverted-T = j, right bowl = s, F-like = r, corner = t, crossed diagonal = z, x = u. No sign on this card needs a value outside that key.
3. **Independent decryption.** I read every row of the main text and the N01 annotation from my own enlarged crops of `source/address.jpg` (3–8x, `review/work/*.png`, made with `review/work/crop.py`). I wrote the result into my own ledger, `review/work/my_ledger.txt`, using a separate sign-name alphabet: b2, b3, sect, rbowl, corner and so on. My own decoder `review/work/my_decode.py` turns it into text (output `review/work/my_decoded.txt`). After removing uncertainty braces, the diff against the solver's output shows only two rows:
   ```
   01  reviewer: édesjolánkámbecses       solver: édesjolankambecses   (accents only)
   12  reviewer: ésmindenn{e?}leföldön    solver: ésmindennélaföldön
   ```
   All other rows are sign-for-sign identical.
4. **Coverage.** The card has 17 cipher rows, from `Édes Jolánkám` to `… szeretetel Feri`. The ledger covers every one, and the row-17 continuation past the divider line is included. The address side has one more cipher group, N01, right of "kisasszonynak", and it is covered. The picture side (`source/picture.jpg`) is a printed image with no handwriting or cipher.
5. **Pass-6 corrections checked on pixels:**
   - Row 12: after `minden` there are two separate two-stroke n signs, then three bars and a wave. So it reads `mindennel`, not the GPT-era `mindenemél`. **Confirmed.**
   - Row 14: the sign after `kedé` is the inverted-T (j), the same shape as the j in row 1 and row 13. So it reads `kedéjes`. **Confirmed.**
   - Row 17: there are two corner+bars groups before the wave, then cross, bars, F and dotted curve. So it reads `szeretetel Feri`. **Confirmed** (`review/work/r17b.png`).
   - Row 4 `ala{t?}ti`: a small cramped tick-like mark sits between the a (two bars) and the final corner (`review/work/r4end.png`). It cannot be decided between a second t and a false start. It is disclosed correctly, and `alatti` stands in either case.
6. **Spot checks of the readings most likely to be forced:**
   - Row 6 `kivel`: the first sign is the section sign (k), not three strokes (m).
   - Row 8 `tanum, ki alkoté a nagy`: the corner+bars carries a clear accent tick (`review/work/r8.png`), and u is the plain x, different from the tailed z.
   - Row 15 `mit ad vissza`: two bars, then a tall double stroke (d), chevron, dotted curve, two right bowls, crossed diagonal, two bars.
   - Row 13 `jobban`: inverted-T with a low base, not the upright f-cross used in row 12 `földön`.
   - Row 3 `kaptam` p and rows 7/10/15 `hogy` h: the shapes match the disclosed h/p near-homography, and context settles them.
7. **Language and context.** The plaintext is grammatical early-20th-century Hungarian, with the writer's known phonetic spellings (`kösönettel`, `kedéjes`, `szeretetel`) as on the sister cards. The verse is coherent (szeretlek / szenvedek / szeretlek). Feri as signatory, Tóth Jolánka at Jászárokszállás and the postmark `1912 FEB 17` (Jászárokszállás, plus a Gyöngyös(?) stamp) all agree with the metadata and the sister cards.
8. **Honesty.** No published solution is cited or used. The portal status was *Not solved*. GPT's passes 1–5 and Claude's pass 6 are credited separately, and the transcription is declared non-blind.

## Findings

1. **Row 12 `a földön` is literally `e földön` (minor).** The sign before the upright cross (f) has three evenly spaced bars of equal length. That is e, not the two-bar a (`review/work/r12-efoldon.png`, 8x). Compare the two-bar a in row 13 `jobban` directly below. `e földön` ("on this earth") is idiomatic, and poetic Hungarian uses it often, so it fits the verse even better. Fix: change the ledger token in row 12 from `A` to `E`, then update the edition to *és mindennél e földön* and the translations to "on this earth". The meaning hardly changes.
2. **Row 12 accent on `mindennél` is not visible (minor).** The sign after the two n's is three bars of equal length (`review/work/r12b.png`). There is no separate accent tick of the kind used elsewhere, for example over `élek` and `alkoté`. Literally it reads `mindennel`, and the accent should be editorial like the others in item 4 of the uncertainties. If the solver reads the short top bar as an accent, they should say so. Otherwise it is three bars: e.
3. **N01 edition should keep its qualification (minor).** I confirm z e . e t e t e l and the hooked first stroke (`review/work/n01c.png`). Sign 1 is a single hooked diagonal with no visible bowl, and sign 4 is an M-shaped cramped sign. Neither looks like this writer's s and r anywhere in the main text. The reading `szeretet[t]el` rests on the sign-off formula and on HCP1218, whose own N01 is qualified. That is reasonable, but the edition line "Address-side annotation …: szeretet[t]el" should carry the same "probable" or "?" mark that the uncertainty section gives it.
4. **The plain-hand stamp-corner note is misread (minor, not cipher).** SOLUTION.md uncertainty 8 gives "számtalanszor csókol szerető[d] Feri". On the enlargement (`review/work/topright.png`) the five short lines read *számta / lanszor / csókol / szeretet / tel Feri*, that is, **"számtalanszor csókol szeretettel Feri"** ("kisses you countless times, with love, Feri"). This matters a little: in plain hand the writer spells *szeretettel* with tt across the line break, which supports the `szeretet[t]el` restoration in the cipher. The line above the postmark, not transcribed by the solver, appears to read *"Egy kis nefelejcsnek"* ("To a little forget-me-not"). I give it as a probable reading only. The report should either correct these readings or label them clearly as approximate.
5. **Row 1 and row 2 accents under-recorded (minor).** The two-bar signs in `Jolánkám` carry visible accent ticks (`review/work/r1a.png`, `band0.png`), but the ledger records `jolankam`. This is cosmetic. Either record the accents or keep the current note that the edition supplies them.

No blocker or major findings.

## What I could not verify

- The bottom edge of row 17 is clipped by the scan. The lower parts of a few signs (the `viszontlátásra` and `Feri` area) are cut off, and the reading relies on the upper halves plus the formula. Only the 1024 px portal image is available.
- Row 4's extra tick and N01 signs 1 and 4 cannot be resolved at this resolution.
- I did not search the literature beyond what is recorded (the portal reference article, HistoCrypt / Schrödel collection, was not read). So I cannot rule out that someone published the verse or the card. The orchestrator's AI-register check (2026-10-29) found no entry.
- `report/` already contains a draft. I did not review it, because this round reviews the solution, not the report.
