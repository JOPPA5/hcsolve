REVISE

# Review 1 of HCP1258 (Claude Opus 5.5, 2026-11-01)

Summary: the decipherment stands. The family key gives running, period Hungarian across the whole card, and I found no forced reading in rows 1-27 or the box. Two things need fixing: row 28 has a written sign that the ledger leaves out, and the closing of row 29 is under-read. Neither changes the sense of the message body.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1258/work/decode_opus.py` ran. All 4 hashes printed OK. The output matches the rows and the normalized text claimed in SOLUTION.md.
- **Ledger counts.** `review/work/check.py` gives 36 rows, 785 tokens, 792 letters, which matches the claim. The same script diffs the literal text against the normalization with accents removed. Every difference is in Uncertainties 4 and 5 or is ordinary gemination (the -kk-, -ss-, -mm- type), and the row 29 tail is cut from the comparison. The diff cannot see finding 1, because the ledger and the normalization both lack the sign.
- **Pixels.** I made my own crops of the hi-res original with `review/work/crop.py` (`review/work/c/`). L1-L5 and R1-R5 cover rows 1-25, foot1-3 cover rows 26-29, and box, box_r and box3 cover the stamp box. I read rows 1-29 and s1-s7 sign by sign against the ledger and the key in `ciphers/hcp-1216/SOLUTION.md`. Every row agrees except row 28 (finding 1) and the closing (finding 2).
- **Restorations.** Rows 26, 28 and 29 at the tear:
  - *feleség[e][m]é*: a fragment and the last m stroke are visible.
  - *éve[t]*: the end of the bar is visible.
  - s3 *marad[o][k]*: a wedge and a vertical trace are visible.
  - All are disclosed as restorations. I find them honest and the context supports them.
- **Word-sense calls.** I checked these on the pixels: *högtön* (h/p sign, clear, then ö), heavy f blot in row 13, *át*+blot+*alszom* in row 14, wiped *az eső és* in row 12, *irntam*, g-like k in *-ságunkat*. Each is as described. Row 12 is legible only as ghosts, as the solution says.
- **Repeated words.** *édesem* ×7 and *hogy* ×7 (ledger count) are correct.
- **Language and content.** The text is coherent, period colloquial Hungarian in the Feri/Jolánka hand and formulae. The English and Slovak follow the Hungarian. Numerals 2 and 1 fit. I saw no sign of an outside solution.

## Findings

1. **major: row 28 omits a written sign.** After *fiatal* the card shows a separate two-bar sign before *hogy*. The sequence on the card is i, a, t, a, l, **a**, h, o, gy (`review/work/c/foot3.png`, row 3; `review/work/c/r28end.png`; `review/work/c/r28aa.png`).
   - The ledger has `F I A T A L H O GY`, so the ledger, the literal row 28 and the 792-letter count are all wrong by one sign.
   - The claim that the comparison "shows only the disclosed changes" holds only because the sign was never transcribed.
   - Add the token, recount, and normalize it openly (*fiatal, a hogy* or *ahogy*, or a slip). The translation may need a small adjustment. The sense of the sentence stands.
2. **major: the end of row 29 is under-read, which decides how complete the card is.**
   - *First word.* Uncertainty 1 says the signs do not show *csókolja*. On `review/work/c/r29blot.png` both middle signs have the loop-with-tail shape of the hurried o, as in *hogy* at the end of row 28 (`review/work/c/r28aa.png`). The second is overinked and may hide a sign. So cs-o-(k?)-o-l-j-a is much better supported than the solution says, with the k omitted or lost under the blot. This writer omits letters often. Re-examine and state it.
   - *Second word.* `kedves` + `se` is printed as *kedves[e?]*, but the following signs are plain ")" for s, then a ")" with a hooked top, not a clear second s (`review/work/c/r29end.png`). Test whether that hooked sign is a variant of k.
   - *Tail.* Test whether ?X is z. The dot beside it may be stray, and the cross-with-tail is close to z and f. Then the tail could read *kedves kezé[t]* ("kisses your dear hand"), with the final t dropped or lost at the corner, in line with this writer's dropped endings. **This is my hypothesis, not a confirmed reading.** The hooked sign is not a normal k.
   - Either adopt a reading with its doubts or keep the signs literal, and do not print a doubled-s *kedves[e?]* without saying why. If at most one word stays unread and the rest reads, the card can count as complete. If not, it is partial and gets no register entry.
3. **minor: the command does not really decode.** The ledger tokens are already plaintext letters, so `dec()` only lowercases them, and the normalized text is a hand-typed file. SOLUTION.md says "decodes" and gives no key table, only a pointer to HCP1216. Copy the key table into SOLUTION.md and say plainly that the ledger records letter values read through the key. Sign-class tokens would be better.
4. **minor: ledger and disclosure gaps.**
   - Uncertainty 2 says the g of row 28 *hogy* is in the tear, but the ledger gives `GY` unbracketed.
   - The n of row 17 *van* is a faded, smudged shape and is not mentioned (`review/work/c/R4.png`, row 1).
   - The é in row 18 and the blotted o-n in row 22 *halgason* are heavy or smudged and also not listed.
   - None of these changes the reading.
5. **minor: possible support for s3.** The wedge after *marad* resembles the wedge-shaped ó the solution itself reports in s6 *imádója* (`review/work/c/box3.png`). This supports *marad[o][k]* and could be cited. Literal text remains *marad*.

## What I could not verify

- The portal detail tabs: the capture timed out, and the solution discloses this. "No attached solution or transcription" rests on the catalogue row and on sister cards only. I did not fetch the portal.
- The address first line and the postmark date: not read, not part of the cipher.
- Row 14 blot content, and whether a sign lies under it.
- My sign-by-sign pass was not blind, because I had the ledger and key to hand. I did not re-derive the family key.
