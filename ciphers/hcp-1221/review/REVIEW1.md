REVISE

# Review 1 of HCP1221 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: the Jolánka key turns the whole card into coherent Hungarian, and I found no forced passage. Three concrete corrections are needed. The main one is that rows 7-8 are not an unread word. They read `mert ahol dolgozok sürgős a munka`, which removes the solver's false start, invented accent and broken syntax.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1221/work/decode.py` ran. All four hashes are OK, and its output matches the literal block and normalized text in SOLUTION.md.
- **Independent transcription.** I read all 20 left rows and 7 stamp rows from my own crops of the hires scan (`review/work/crop.py`; bands a1-a5, st, b1; zooms z7, z8, z10, z13, z16, z16b, z17, z18, z18a, z19, z6, sender). `review/work/independent_decode.py` compares my reading with the ledger, decoded by my own table. Result: 27 rows, 337 tokens, **one row differs**, row 16 (finding 2). I had seen the solver's text before transcribing, so this is a check, not a blind reading.
- **Key.** Ledger tokens are all in the HCP1216 classes (compared with `hcp-1216/work/decode_opus.py` and the table in its SOLUTION.md). No new value, and no sign is left without a class except the blot in row 10 and the digit 8 in row 6, both disclosed.
- **Restorations judged on pixels.** Row 13 `[o]`: a bold X body with two horns; no o shape is visible, so this is a true restoration from word sense, disclosed. Row 18 `[na]`: the blot shows two strokes crossed by two bars, a good fit for overwritten n + a. Row 10 blot: bars stick out at top and bottom, so a hidden letter (a) is possible; both options are disclosed. Row 6: a looped 8 with a long tail, sense reading, disclosed.
- **Clear text.** Szépreményű / Tóth Jolánka / úrleánynak / Jász Árokszállás read as claimed. The postmark at lower right shows only C 12; the partial postmark at top centre shows no text. No date is legible. The picture side is a printed photo with publisher number 1012 and no writing.
- **Sister-card claims.** HCP1216 has *de* with a right-tick stroke, read as d from context (its Uncertainty 3). HCP1216 row 4 omits the g of *még* (its Uncertainty 1). HCP1296 has *Jolankaek*. HCP1309 has Holes Feri, left Szentmihály for Rákospalota. All confirmed in those files. The Hungarian *ahol* occurs on sister cards (hcp-1227, 1236, 1249 and others).
- **Published solution.** None is used or claimed; the portal attaches none. I did not search further.

## Findings

1. **major: rows 7-8 are `ahol dolgozok`, not `[dol-] dolgozók [?]`.** Crop z7 shows a, stroke + right tick, o, l, stroke + right tick, o, l, g, o, then row 8 z, o, k. Dividing `a-h-o-l | d-o-l-g-o-z-o-k` gives `mert ahol dolgozok sürgős a munka` ("because where I work the job is urgent"). This is plain grammar.
   - The first right-tick sign is the ordinary h. Only the second needs d with the tick on the wrong side, the same anomaly already accepted on HCP1216 (*de*).
   - The solver's reading needs that anomaly twice, plus a false start, plus an accent, and it still has no syntax.
   - Fix the normalized text, English, Slovak, Uncertainty 1 and `work/normalized.txt`. The word stays a word-sense call for one sign and should be disclosed as such, but it is no longer an uncertain word.
   - Corrected translation, Slovak: `lebo tam, kde pracujem, je práca súrna`.

2. **major: row 16 is `mesterrel`, not `mesterral`.** The sign after r r has **three** bars (z16, z16c). A red-pixel profile (`review/work/profile.py`) on x 945-1025 gives three separate bands at about y 1634-1646, 1655-1667 and 1682-1691. The a of `hat` in the same row gives two. The third bar is not an accent of row 17: that row's é has its tick further left, at about x 755, y 1672, under the first r of row 16. So the claimed writer's slip does not exist. Change the ledger token to E, drop the "-ral is a slip" part of Uncertainty 9, and fix the literal block, including NOTES.md if it is kept as history.

3. **minor: false accent claim in rows 7-8.** Uncertainty 1 lists the signs as `z, ó, k` and the normalized text prints *dolgozók*, but the ledger and literal output have `zok`. The only tick nearby (z8) lies below the k and is the acute of row 9 `é`. There is no accent. Finding 1 resolves this.

4. **minor: row 18 `sag` lacks a visible acute.** z18a shows a tick above the two bars, so the sign is á (`ság`). Add `:acute` to the ledger. No effect on the text. The same word in row 17-18 is therefore fully written with its accent, unlike row 14.

5. **minor: miscount.** Uncertainty 1 says "all four unquestioned d ... (rows 2, 6, 9, 13)". Row 1 *édes* has one as well, so there are five, all with the tick left. The ledger has five D tokens.

6. **minor: sender line.** I see the same thing as the solver: `Emocn` (E-m-o-c-n/u), then an overwritten word best fitting `Telep`, then Bocskai utcza 3. Neither word could be resolved by me. It may be a locality or a person ("c/o") and SOLUTION.md should not imply either. It is disclosed and sits in an address, so I do not count it as an unread clause.

7. **minor: `mely bár soká lesz`.** The signs are clear, but *bár* alone leaves the sentence hanging, as the solver notes. A wish sense of *bár* (or a dropped *nem*: "which I wish would not be long") is possible. Mention the alternative beside "though that will be long".

## What I could not verify

- The date and origin of the card: no legible date.
- That the writer is Feri: there is no signature here; it rests on hand, key and HCP1309, and the title's "(?)" is right.
- What lies under the row 10 blot and the row 13 overwrite.
- The sender line words in finding 6.
- The hidden letter count of the row 18 blot beyond the shape fit; `vasárnap` makes it safe.
