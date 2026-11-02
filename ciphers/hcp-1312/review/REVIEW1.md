ACCEPT

# Review 1 of hcp-1312 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. Rows 1 to 14, the end of row 15, the stamp box and the address agree with the pixels. Seven signs of row 15 are restorations from context and the family formula. They are disclosed, and they do not change the reading, because v...t + látásra leaves only viszontlátásra. All findings are minor. The card meets the completeness rule: every row reads, and the only understood-with-difficulty clause, "s az másképen is lehet", is what is written.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1312/work/decode_rev2.py` runs from the repository root. Both source hashes print OK. Its literal output equals the SOLUTION.md block.
2. **Independent decoder.** `review/work/decode_indep.py` (run from the cipher directory) has its own sign alphabet and my own transcription of all 15 rows. Result: `rows 15 signs 243 rows differing from solver ledger 0`. This check is not blind, because I had seen the ledger. For row 15, the signs i s (Isten) and i s z o n (viszont) were typed as the solver's hypothesis and only tested for compatibility. The script also aligns the literal letters against the normalized text. The only differences are c>s (soraim), s (csak), m>n (másképen) and the bracketed insertions ö, t, b, n, m, t. Each one is disclosed.
3. **Key.** All 243 signs fall in the 25 ledger classes and no per-row change is needed. The table agrees with the hcp-1216 table. The only addition is the barred left bowl, which is disclosed as the left half of cs.
4. **Pixels.** I made my own crops from `work/hires/` (`review/work/crop.py`, modes rgb, g, b-g, r-g, at 2x to 8x). I read rows 1 to 13 sign by sign at 2x, and rows 14 and 15 up to 6x.
   - Rows 1 to 11 and 13 are clean and match the ledger, including row 4 final k, which crosses the divider and looks like a stray S on the address side; ö with two dots in row 6; and four strokes in "benne" in row 10.
   - Row 9 sign 13 has its crossbar low on the stem, the same as the j of row 1 (crossbar about 80% down), so it is inverted T and not +. "Legfobb" is therefore excluded.
   - Row 8 sign 8 is an open barred bowl, not the closed 6, which agrees with "cak".
   - Row 12 *lehet*: the b-g crop `e1.png` shows the heavy stem under the blot and three bars at the right place, the lowest clean. The restoration is supported.
   - Row 12 *másképem*: three strokes, the third short and wedge-topped, as stated. "Nem" is not on the card, and the solver was right not to supply it.
   - Row 14: all 16 signs can be counted, as stated. The middle t has a stem only. The final t is firm.
   - Row 15 start and middle: e and n of Isten, chevron, wave, and the two bars of "a" (`b4.png`) are visible. s and t of Isten are compatible, and the i is weak. vele: both e are faint, so e rests on the word.
   - Row 15 end: t l a t a s r a. "látásra" is plain even in the unprocessed scan. The rise of the row is real: the Isten baseline is at y about 2070 and the látásra baseline at y about 2010.
5. **Plain parts.** Szépreményű, Tóth Jolánka and úrleánynak are clear. In the town line, the J, the sz and three accent ticks are compatible with Jász-Árokszállás, as the solver limits it. The stamp box reads as claimed, except for finding 2. The picture side has only printed text ("Sirassatok engem orgonavirágok...", "Csak egy kislányt hagyok itthon..."). I found no handwriting there.
6. **Language and context.** This is natural Hungarian of the period and fits the family formulas. "Isten vele, a viszontlátásra" occurs on hcp-1216 and 1212, and 18 family cards have "a legjobb kedvében találja soraim". The Hungarian-to-English and Slovak translations are faithful apart from finding 3.

## Findings

1. **minor: row 15 restorations are not marked apart from read signs.** In the ledger and the literal output, every row 15 sign has the same `~` or parentheses. So the solid signs (v, a, t, l a t a s r a) look the same as the restored ones. On my crops:
   - x 1115-1207 is one blob with a rising bar over a lower lobe, compatible with i.
   - x 1235-1345 is merged. s and z cannot be separated, and the long tail to x about 1420 is at least partly the lowest bar of the row 14 e above it.
   - x 1430-1473 is a bar over a lobe, assigned to o.
   - x 1490-1532 looks like a rounded, nearly closed form rather than two separate strokes, though it is assigned to n.
   Uncertainty 1 discloses this in words, and I do not dispute the word. Suggested fix: mark i s z o n and the i s of Isten as restored, for example with a separate ledger suffix, or say "v[iszon]t" in the report. Also say that "o" and "n" were not told apart as signs.
2. **minor: stamp box line 3 may be longer than "Csók".** The r-g and b-g crops (`d1.png`, `f1.png`) show traces right of the k, at the edge of the stamp mark and beyond it, compatible with "ol" (Csókol/lak). The family spells this csokolak (hcp-1206). If so, "csók[ol]lak" should be "csókol[l]ak". Not certain, because the traces are faint and overlap foxing. Say so in place of the flat "Csók".
3. **minor: "good" in "good spirits" is supplied without a note.** The card has "a kedvében", with no "legjobb" or "jó", while the family formula has "a legjobb kedvében". The translations add "good" (dobrej). Note that the word is omitted on the card, or bracket it.
4. **minor: the crossbar sign is not a textbook gamma.** The row 15 t at x about 1567 has a stem rising above the bar and a small protrusion to the left, unlike the card's other gammas. Uncertainty 3 does not say so. The t reading is still the only one that fits. It is also the only sign that might be argued to be a second t of "teremtett" in row 14, but then row 15 would lack the t of viszont, so the solver's assignment is the better one. Worth one sentence of disclosure.
5. **minor: soraim, csak and másképen are normalized without brackets**, while the other normalizations are bracketed. They are disclosed in uncertainties 4 and 5. Make the convention uniform if convenient.

## Could not verify

- The postmark. I see fragments (digits, an arc) but could not read a date, so 1912-04 rests on the file name only, as stated.
- The middle of row 15 as independent readings (see finding 1).
- The town line letter by letter. It is washed out and rests on the file name and family context.
- The portal status and the absence of a published solution. I relied on SOURCES.md and the orchestrator's register check, and did not fetch the portal.
- Sender identity. None is written, and the solver claims none.
