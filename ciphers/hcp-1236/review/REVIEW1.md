REVISE

# Review 1 of hcp-1236 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: this is a real Hungarian love message and the Jolánka key fits. One sign is misread (row 2, f for j), and the fix changes the printed plaintext, the normalization and a statement in SOLUTION.md. The remaining findings are smaller.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1236/work/decode.py` ran. All four SHA-256 checks passed, and the 18 literal rows and the normalized text match SOLUTION.md exactly.
- **Independent decode.** I read the signs from my own band crops of the hi-res address side (`review/work/crop.py`, `a1`–`a9`, `b1`–`b9`, zooms `z*.png`). I wrote my own ledger with hcp-1216 sign names (`review/work/my_ledger.txt`) and decoded it with `review/work/decode_review.py`. This was not blind, because I had read SOLUTION.md first. Result: 302 letters, 17 of 18 rows identical to the solver's, and row 2 differs (finding 1).
- **Key coverage.** Every sign on the card has a key value from the family key (`hcp-1216/work/graphic-key.json`). No extra symbol is needed, and no letter value conflicts with hcp-1216.
- **Sign-by-sign checks of the disclosed calls:**
  - Row 11 `goadol`: true horizontal two bars. Confirmed.
  - Row 17 `viszoat`: `o a t` are all there. Confirmed.
  - Row 16 `da`: short-left, long-right, the d shape. Confirmed; d for h is a slip.
  - Row 13 merged sign: a thin chevron leg, then a top bar and hooked stem. Solver's description is fair.
  - Row 8 thick a: two heavy bars joined by a stem, like an I-beam (`z8.png`). Whatever lies under it cannot be seen, but `az` is forced and no competing reading exists.
  - Row 17 heavy undotted sign: crossbar plus thick descender, i-shaped rather than o-shaped. `Isten` accepted, as disclosed.
  - Row 18: `látásra` is complete, last a slightly clipped.
  - The stroke to the right of the final F of row 14 (`dash14.png`) is only the detached top bar of that F, not an extra sign.
- **Sample of ordinary rows.** All rows were read, none disputed apart from row 2.
- **Plain parts.** Margin note `csokolja tavolba szamta lanszor Feri` and the address (`Szeretett / Toth Jolanka / kisasszonynak / Jász / Árokszállás`) are correct. The picture side has the printed verse `Sorrentói ábránd` and no handwriting.
- **Language and context.** The text is natural period Hungarian in the family's love-letter style. Recipient and town agree with the portal metadata and filename. The portal lists no solution, and I found no sign of an undisclosed one.

## Findings

1. **major: row 2 is `legjobb`, not `legfőbb`; the sign is j, not f.**
   - Evidence: `review/work/fj_compare.png`. On this card the two signs differ by where the bar sits. j (rows 1, 3, 13) has the bar near the foot with a stub below it. f (rows 4, 6) has the bar high with a long descender.
   - The row 2 sign has a low bar and a short stub, with a pale upper stem where the pen ran dry. That is the j shape.
   - In the sister cards, `grep` over `ciphers/*/SOLUTION.md` finds "legjobb kedvében" or a close variant on 24 lines and "legfőbb kedvében" only in this solution.
   - `legfőbb` also needs an ő for which the card has no marks (solver's item 11 admits it is supplied).
   - Fixes needed:
     - `work/ledger.txt` row 2: `+` becomes `J`.
     - `work/normalized.txt` and SOLUTION.md: use `legjobb`.
     - Amend the statement about accents (item 11).
     - The English and Slovak ("best", "najlepšej") already translate legjobb and stay.
     - Add the f/j distinction to the sign description; the current table does not state it.

2. **minor: row 6 word division.** `hétfőt át dolgoztam` with "the slightly loose form" (item 9) is better read as the preverb verb `hétfőt átdolgoztam`, "I worked through Monday". The signs are the same and the looseness goes away.

3. **minor: the card is not undated (item 13).**
   - The left postmark, rotated and contrast-stretched (`review/work/pm_rot.png`, `pm_read.png`), shows a year ending in 912 and a day beginning with 2. The month is not legible.
   - The portal filename `cpc_1912--22` gives 1912 and day 22. SOLUTION.md does not mention it, though sister cards use the filename as date evidence.
   - State this and say it comes from filename plus postmark.
   - Optional, as a labelled inference only: Shrove Tuesday 1912 was 20 February, and a card of Thursday 22 February would fit the carnival question and "on Tuesday". I could not read the month, so this is not established.

4. **minor: `k` without its dot is not disclosed.** The key table says the section mark has a dot below, but two k signs on the card have none: the first k of `csak` (row 14, `z14.png`) and the k of `nézhetek` (row 17, `z17a.png`). Both are forced by the word. Add them to the uncertainties, since "no unexplained sign" and "only items 1–4 needed word sense" are otherwise slightly overstated. The h/p calls in item 10 and the word-sense call in item 5 also go beyond "items 1–4".

5. **minor: punctuation is not recorded.** The card has marks the ledger leaves out, although the ledger says "one token = one written sign":
   - hyphens after `Jolán-` (row 1) and `sora-` (row 3);
   - a full stop after `soraim` (row 4, in the stain) and after `volt` (row 9);
   - a comma stroke after `farsangba` (row 5, `z5.png`).
   None changes a letter. Either record them or say the ledger omits punctuation. The row 5 stroke in particular looks like a lone sign, and it should be explained as a comma.

6. **minor: bracket in `szín[el]őadás` (item 5).** The e is on the card (literal `szineöadas`) and only the l is missing, so the form should be `színe[l]őadás`. Fix `work/normalized.txt` and the Hungarian text. The sense stands.

## What I could not verify

- The month in either postmark. The second postmark is mostly lost with the stamp.
- What lies under the re-inked a of row 8.
- Whether the row 13 sign is v+t or t alone; the reading is the same either way.
- Accent ticks between rows. I did not rule on every tick, and these do not affect the sense.
- That this Feri is the Feri of hcp-1216; the solver does not claim it.
