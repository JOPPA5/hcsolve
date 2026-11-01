REVISE

# Review 1 of HCP1261 (Claude Opus 5.5, reviewer, 2026-11-01)

The decipherment stands: family key, reading order and nearly every word are confirmed from the pixels. One segmentation in row 13 should change, because it alters the normalized text and all translations. Three small corrections to the ledger and disclosures are also needed.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1261/work/decode_opus.py` ran; all four SHA-256 checks passed. Output matches the literal block and the normalized text in SOLUTION.md. It reports 444 signs.
- **Independent reading.** I cut my own crops of the hi-res address side (`review/work/crop.py`, `review/work/crops/`, 2x to 5x) and read every row, the edge, the bottom row and the stamp box into `review/work/my_reading.txt`, using graphic class names. `review/work/my_decode.py` decodes it with its own key table and diffs it against the ledger.
- **Result.** 440 of 444 ledger signs agree (h/p counted as one sign). The only differences are the blot signs the solver flags: row 8 (two positions, finding 2), row 13 v, row 18 s. On S2's first sign I marked a blot and the solver reads a; he discloses it. I found no undisclosed misreading.
- **Key.** Compared with the HCP1216 legend. Every sign falls in a family class except the plain M (finding 3). No value was invented.
- **Reading order.** The left edge, rotated 90°, reads downward *b. sorait*; the bottom row reads *várva … feri*; the stamp box runs on through *számtalanszor*. The sentence continues through the corner. Confirmed.
- **Flagged points on the pixels.**
  - Row 3 `= gy`: two bars, clear. The slip for *úgy* is an interpretation and is disclosed.
  - Row 10 *képzel a i*: two clear horizontal bars, as stated.
  - Row 11 *még megka-*: clear.
  - Row 13 blot: a v-like right arm is visible; v is reasonable.
  - Row 18 blot: an overwritten mass; the sign before and the *z* after are clear, so s rests on sense, as disclosed.
  - Row 19 *pediglen*: the p is the same stroke pair as the following d, as disclosed.
  - Bottom *mara maradok*: the first three-stroke sign is unevenly spaced, followed by a F a, as stated.
  - Stamp S2 and S5: Γ followed by two bars (a), confirmed. S4's heavy inverted T: accepted.
  - Plain *egy igaz* / *sziv*: readable, last letter uncertain as stated.
- **Language and context.** The text is natural period Hungarian in the family's register (formal Ön, *rabszolgája*, *számtalanszor*, signature Feri). The maxim and *pediglen* fit a 1912 writer. Addressee and town match the address side and the portal.
- **Postmarks.** The left one shows 912, MAR and a 7, agreeing with the file name. The right one shows 912 and a partly lost Roman month. Picture side: the printed verse is as quoted, under the collection stamp in part.
- **Sources.** Portal status and attachments are as SOURCES.md says. Neither `skip.txt` nor `register-exclusions.json` lists 1261. I found no sign of a published solution.

## Findings

1. **Major: row 13 is better divided *a levele, repülőgépet*, not *a levél: e repülőgépet*.** The signs are l e v e l e r e p ü l ö (crop `r13.png`: blot, three bars, wave, three bars, F). The solver's *e* "this" needs a demonstrative pointing at an aeroplane, and the picture side shows a couple by moonlight, with none. His alternative *er[r]e* needs an added sign. *Levele* ("your letter", possessive) needs no change to the signs, and it agrees with *sorait*, *becses lapjai* and the formal address throughout. It gives *Úgy szeretném, ha repülne a levele; repülőgépet szerzek be, hogy gyorsabban jönne becses lapjai*: "How I wish your letter could fly; I will get an aeroplane so that your esteemed cards come faster." Fix: change the normalized text, English, Slovak and uncertainty 4, and keep the old division only as a rejected alternative. The title may stay. The ledger needs no change.

2. **Minor: the row 8 ledger drops a written sign.** I read ö, blot, two strokes, stroke pair with longer second stroke, e, k, which is six signs, and uncertainty 2 describes the same six. The ledger has five (`O:d N! N? E K`), though its header says one token per written sign. The true count is therefore 445, not 444, and the literal `ön*n*ek` has one sign fewer than the card. Fix: add a token for the extra sign or state that one sign was dropped as a false start, then update the count. The reading *önnek* stands, on word sense.

3. **Minor: the first sign of row 16 is a plain Latin cursive capital M, not the three-stroke cipher sign.** See crop `a5.png`, last row. The ledger records it as ordinary `M`, and the text says the whole message uses the key, with plain writing mentioned only in the stamp box and the address. The value is not in doubt. Fix: mark it as a plain letter in the ledger or a note, and disclose it.

4. **Minor: the dot token is handled inconsistently.** S2 ends `6 .` in the middle of the word *távol-b.-ól*, where the dot cannot be an abbreviation mark; the word simply continues in S3. The edge *b.* is expanded as an abbreviation for *becses* because of a similar dot. The expansion is still the best reading, but the S2 dot should be mentioned, since it shows this writer's dot after 6 need not mean abbreviation. Fix: one sentence in the uncertainties (10 or 11).

5. **Minor: small translation point.** English row 9 says "as if I were talking with you", while the Hungarian has only *beszélgetnék*. The Slovak is correct. Bracket "[with you]" or drop it.

## What I could not verify

- The blotted signs in rows 8, 13, 18 and the first sign of S2 can only be judged by sense; the original underwritten strokes are not recoverable from the scan.
- The short plain line under *úrleánynak* is unread by me too. It begins roughly *sz r t*, followed by spaced letters, among them *e e e t*, and a heavy blot, and it is partly under the collection stamp. The solver's disclosure is fair; it does not affect the message.
- The right-hand postmark's place and month.
- Sender's identity beyond "Feri".
- Register entry: none exists yet. After the fixes above the card qualifies as a complete reading.
