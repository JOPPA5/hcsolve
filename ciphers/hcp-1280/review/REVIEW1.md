REVISE

# Review 1 of HCP1280 (Claude Opus 5.5, reviewer, 2026-11-01)

The decipherment of the 15 enciphered rows stands. I found no misread word. Four concrete corrections are needed in the solver's text and ledger, and one decision is needed on how the card is labelled, because a clause of the plain stamp-box note is unread (finding 1).

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1280/work/decode.py` passes all four SHA-256 checks. Its output matches the literal block and the normalized text in SOLUTION.md exactly. The script only prints the ledger and `normalized.txt`, so the real test is ledger against pixels.
- **Independent decode.** `review/work/indep.py` holds my own row-by-row sign-class transcription from my crops, with the HCP1216 key typed separately. It covers 213 signs. Fourteen rows agree letter for letter. Row 12 differs by one mark (finding 3). Caveat: I had read the solver's text before transcribing, so this is a check against the pixels, not a blind reading.
- **Scan check.** All 15 rows were checked sign by sign on 2x crops of the hires address scan (`review/work/crops/a1 … e2`, made with `review/work/crop.py`). The disputed signs were checked at 4–7x: `r2x2`, `r3ly2`, `r6s2`, `r8l2`, `r13s2`, `r12o2`, `r4o`. I also checked the critical pairs:
  - k against s: the dot or tail below is present on every k, absent on every s.
  - d against n: in rows 5, 8 and 9 the left stroke is clearly the shorter one.
  - a against e: bars counted, including row 7 *re*, whose bars straddle two crops.
  - ő and ö ticks in rows 4, 6 and 9 are present; row 12 is the exception (finding 3).
- **Stray dots.** The two dots at the end of row 1 are the k's dot and the dot of the i in row 2. The tick under the m at the start of row 9 is the dot of the i in row 10. Neither is a missed sign.
- **Key.** Every sign takes a value from the family table. The fullest table, HCP1216, was checked. *Ly* is wave + y, that is l + y, so no new value is needed. Note that HCP1212 records this writer family as spelling ly with j (and HCP1216 has *ojan*). This card's written ly is a spelling difference, which adds a little to the open question of the writer but does not affect the key.
- **Language.** The text is natural early-20th-century Hungarian love-letter prose. *Várva várt sorait*, *Isten vele, a viszontlátásra* and *tiszta szívéből* are all period idiom. *Melyre* and singular *mely* after plural *sorai* are loose but real usage. The English and Slovak translations are faithful, apart from finding 2.
- **Picture side.** It carries only a printed Hungarian verse and a series number, with no handwriting or cipher.
- **Sources.** The portal metadata records no solution. I found no use of a published solution and no undisclosed copying from sister cards.

## Findings

1. **major: the status must face the unread stamp-box clause.** Rows 2–3 of the plain note are unread. That is a whole clause of the note (`nem is … … … hogy szeretlek`), and "that I love you" depends on it. I confirm the rows cannot be read: my own ink separation (`review/work/sep.py`, `crops/sep2.png`) recovers no more than the solver's attempts, only `v a k e…` and `l e…`. The solver is honest here and rightly offers no reconstruction. The header's split between "enciphered message complete" and "note partly read" is accurate. However, the run's rule says a whole unread clause makes a card partial, with no register entry. The rule does not say whether that covers unenciphered text. The solver should state its position in the Response section. My view: the cipher is fully solved, so the entry may proceed only if the orchestrator or human accepts that the rule covers enciphered text; if that is not settled, treat the card as partial and write no entry.

2. **major: wrong normalized word, *álva*.** The ledger row 14 has plain `A L V A`, and no accent is visible. The normalized text writes *Akár álva*, and Uncertainty 9 says "*Álva* is the literal *alva* (asleep), not an error". Hungarian for "asleep" is *alva*. *Álva* is not that word, and the accent is the solver's own addition. Translations are correct. Fix `normalized.txt`, the SOLUTION.md text and item 9 to *Akár alva, akár ébren*.

3. **minor: row 12 ledger claims a mark that is not on the card.** The ledger token `O:dd` ("double tick seen") and the literal `-bő-` of *szívéből* are unsupported. At 6x (`crops/r12o2.png`) the pale o has no ticks. The only nearby mark is the dot below the k of row 11. Compare the clear ticks and dots in rows 4 (`crops/r4o.png`), 6 and 9. The literal should be `-bo-`, with ő supplied in normalization and disclosed beside the first o of *köszönet*.

4. **minor: "no leftover sign except the possible hyphen" is false.** A clear short mark follows the final i of row 13 (`crops/r13s2.png`, also `d2.png`), low and to the right. It is punctuation at the sentence end after *szereti*, not a letter. It should be disclosed in the ledger or uncertainties, and it supports the sentence break.

5. **minor: descriptions of overwritten signs are firmer than the pixels.** Each value is still the only one that gives a word, and each is disclosed as resting on word sense, so the reading stands.
   - Row 6 (`r6s2.png`) is a wide top hook over a closed loop, with a side tick and a foot.
   - Row 13 (`r13s2.png`) is a thick stem with a foot bar.
   Neither is seen as a "right bowl"; both look like something else overwritten. Say "overwritten, form not a clean right bowl". Row 2 (`r2x2.png`) does show F and chevron superimposed, but the order of the strokes (v corrected to r) cannot be proved from the scan, so say so.

6. **minor: address side understated.**
   - The second postmark is called "not read", but it shows `912-` clearly (`crops/pm1.png`). That confirms the year behind the solver's `91[2]`. Its place name begins with G (`crops/pm3.png`) and is not otherwise legible. Since the first postmark is the addressee's own town, this may be another office on the route or the sending office; that is worth one line, without guessing the town.
   - The first address word is better than "only `Sz…e…y…`": before the blot `Széprem/ne` is visible, with `yű` after it (`crops/addr1.png`). *Szépreményű* is therefore supported by the card, not only by the family form.

7. **minor: imprint spelling.** The vertical imprint reads closer to "Bromüra" than to "Brömaüra" (`crops/c1.png`). The solver already marked it unverified.

## What I could not verify

- Stamp-box rows 2–3 (see finding 1) and the last word of row 1.
- The place name on the second postmark.
- The sender: the card is unsigned, and the solver rightly claims no identification.
- Accents overall: absence of a mark on the scan could in principle be fading, as the pale ink of row 12 shows. Row 12's ticks are nonetheless not visible at the resolution available.
