REVISE

# Review 1 of HCP1270 (Claude Opus 5.5, reviewer, 2026-11-01)

**Summary.** The key, the transcription and the reading of rows 1 to 29 and of row 30 up to *ruhám* stand. I found no misread sign that changes a word. The one thing that blocks completion is the last clause of row 30. It is not read, so by the project's rule the card is partial and gets no register entry unless the clause is solved. The other findings are minor disclosure and normalization points.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1270/work/decode.py` passes all four SHA-256 checks and prints 848 tokens. `review/work/cmp.py` compares its 30 main rows with the literal block in SOLUTION.md: no differences. The stamp rows match by eye.
- **Independent decoder.** `review/work/indep_decode.py` has its own token map and reproduces the same rows. Token counts: 3 `#` and 1 `|` have no letter value, 8 tokens are bracketed. No unknown token. Letter frequencies look Hungarian (e 112, a 99).
- **Key against the pixels.** I did not rely on the ledger's sign names. On my own crops of the hires address image (`review/work/crops/`, 2x to 4x), I read every row 1 to 30 sign by sign against the ledger: sheets L0a to L5b, B0 to B4, r30a to r30d, z30a to z30e, zferfi, zr21, stamp, zs12. Signs match the HCP1216 table. *gy* and *ny* are written as two signs here (for example row 5, row 27), as claimed.
- **Restorations seen on the pixels.**
  - Row 18 `ba[n]`, overinked strokes: acceptable, disclosed.
  - Row 21 `eltünö[k]`, one blot with a hook to the right and dots. The ledger gives it two tokens (ö + k), which is an interpretation of a merged blot. Disclosed; the word is the only option.
  - Row 23 `ba[l]`: a blot with no readable form; *balsors* comes from sense. Disclosed.
  - Row 27 `fe[l]ejt`: heavy blot. Disclosed.
  - Row 28 `a[m]enetelemet`: three overinked strokes are visible, so m is supported by the pixels.
  - Rows 7, 9 and 29 are as described in Uncertainties 3, 8 and 9.
- **Row 26 *férfi*.** zferfi and the wider sheet show the sign is a small cross; `+` is acceptable.
- **Row 30.** Enlarged sign by sign: `s o h/p a m o s t v a z a z o l t o n y a m i t m a 6 i s t u d`. The ledger is right. The sign after `6` has a single dot, so i (not ö) is defensible. The final sign is long stroke with short tick, read d.
- **Language and content.** Rows 1 to 29 are natural period Hungarian with a coherent argument. Period-appropriate spelling simplifications. No sibling card mentions *felülvizsgálat*, so the WWI link remains the solver's inference, as disclosed.
- **Picture side.** Printed violinist card with a printed caption in plain Hungarian and no cipher.
- **Sources.** SOURCES.md and metadata agree: portal status Not solved, no attached solution. HCP1270 is not in `register-exclusions.json`; the orchestrator's note covers the register check. I found no sign of an outside plaintext.

## Findings

1. **major: the last clause of row 30 is unread, and the card must be labelled partial.** Literal: `sohamostvazazoltonyamitmabistud`. The solver's text *soha most va[n?] az öltöny, amit ma[ga?] is tud[ja?]* needs three emendations in nine words: `z` to n against the sign, `6` to *ga* against the sign, and an added *-ja*. Even then *soha most* gives no syntax, and the translation is admitted to be a guess. Only *most, az öltöny, amit* are firm. That is not one lone word: no clause is recovered, so the rule "a whole unread clause is partial and gets no entry" applies. Solver's Uncertainty 1 left this call to me, and this is my ruling. **Fix:** change the header from "all signs read, handed over" to partial, or solve the clause; give the clause as literal text with no continuous translation in English and Slovak (keep the word fragments only); write no `register-entry.txt` unless it is actually read. Untested segmentations to try: `v azaz` (*azaz* = "that is"), `sopa` with h/p read p, and `tun` with d/n read n.

2. **minor: `Mer[t]` hides an emendation against a clear sign.** Row 26 opens with a clear wave, `mel`. The bracket shows only a supplied t, but the r is also not on the card. The same writer spells `mert` correctly twice (rows 22 and 26), so a slip is not the obvious explanation. The attachment of *biztató szavam!* to the previous sentence, rendered "as my word of comfort", is also forced. *Biztató szavam: ...* ("my word of comfort is: you can still be happy with another man") would fit better and might not need *mert* at all. **Fix:** show `mel` as unresolved in the normalized text, and list the alternative punctuation.

3. **minor: undisclosed normalization in row 3.** Literal `amisorailetoen` has one i and no t between *sora* and *let*. The normalized *sorait illetően* adds a t and an i that are not on the card, and *ami ... illetően* is itself a mix of two constructions. Uncertainty 11 mentions only the double consonant in *ilet-*. **Fix:** disclose it.

4. **minor: `napig` translated "for days".** Literal `nahig` = *napig* means "for a day / until the day". "for days" needs *napokig*. The h/p reading is sense-based and the English and Slovak overstate it. **Fix:** note the difference; "for [some] days" as an interpretation, or mark that a number may be understood.

5. **minor: k/g near-homography not disclosed.** The h/p and d/n calls are disclosed, but k (closed S) and g (open with descender) also run together on this card: row 24 *enekem* and row 16 *sikerül* have a k written close to the g shape. No word changes. **Fix:** one line in the uncertainties.

6. **minor: the stamp rows are presented more firmly than the pixels allow.** S2 is `[j]a # s[z][a]m`, with most signs restored, as disclosed in Uncertainty 10. However, S1 has further faint residue at its right end (crop `zs12.png`) that the ledger does not account for, and the first sign of S2 is only a broken angle. The family has both *Csókolja* and *Csókolom*. *Csókolja* is the better fit, but the normalized and translated closing should show the restoration by brackets. **Fix:** bracket the restored letters in the normalized line and mention the residue.

7. **minor: "Why it is correct" has wrong counts.** The literal text has *hogy* 6 times, not 7. *ilet-* occurs 3 times, but that is *illeti* twice and *illetően* once, not *illeti* ×3. "from start to the last clause" should stop before the last clause. **Fix:** correct them.

## What I could not verify

- The sense of the row 30 clause, the core of finding 1. I offer no reading of my own.
- Blotted signs in rows 21, 23 and 27 and the damaged stamp signs cannot be confirmed from pixels. They rest on word sense, as disclosed.
- The date and the writer's identity beyond the name Feri. No readable date is on the card.
- Absence of a publication elsewhere: I did no independent web search.
