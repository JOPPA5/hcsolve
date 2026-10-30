REVISE

# Review 1 of HCP1287 (Claude Opus 5.5, reviewer, 2026-10-30)

The decipherment stands: key, sign sequence and overall sense all hold up. Two points need correcting before FINAL: one sentence of the translation (finding 1) and the layout and evidence at the row 12/13 break (finding 2).

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1287/work/decode_opus.py` passes all 4 hash checks and prints exactly the literal rows and the normalized text claimed in SOLUTION.md (423 signs).
- **Independent decode.** `review/work/my_decode.py` uses its own sign codes and key, and my own row division, from my crops. My flat sequence equals the solver's in all 423 positions; I treated the h/p class and the disputed sign as classes rather than letters. Row lengths differ only at rows 12/13 (finding 2). This check is not blind, since I had read SOLUTION.md first, but every row was checked sign by sign.
- **Pixels.** I enlarged every row of the hires address side 3x (`review/work/crops.py`) and the disputed spots up to 5x (`review/work/crops2.py`), with crops in `review/work/crops/`. All 22 rows were read, not a sample.
- **Key coverage.** One class gives one letter throughout, nothing is left over, and the only unresolved sign is the row 12 dark sign. The family key matches HCP1216. The c of *szerencsésen* (a €-shape) is the sign's only occurrence and is disclosed in SOLUTION.md.
- **Restorations, on pixels.**
  - `[i]` of *viszontlátásig*: dot and long tail are visible beside the blot. Sound.
  - `[m]` of *édesem*: only a stroke on each side of the blot is visible, so the third stroke is inferred. Disclosed, and the word is secure. Sound as a restoration.
  - Row 5 final m: three strokes, the third in the postmark edge. Confirmed.
  - Row 10 `rr`, a re-inked F, and row 15 final s, a re-inked `)`: as described. Row 9's "a" has a black spot between its two bars, and two bars is the right call.
- **Language and context.** The text is real Hungarian of the period, with the writer's usual omissions. HCP1304 does mention *sztrájk* (confirmed in its SOLUTION.md). The picture side verse is confirmed. No published solution was used, as far as I can tell; the card directory holds no solution, and the provenance statements are consistent.

## Findings

1. **major: row 11 `nagybatan szol|tak`, the "my uncle" reading is forced, and a better one is not considered.** The signs are certain: n a g y b a t a n s z o l t a k. SOLUTION reads *nagybátyám szóltak*, "my uncle called [me]". This needs three repairs: y restored, final n changed to m, and a polite plural verb for one's own uncle in a love letter, plus an unwritten object. *Ahol nagy bátran szóltak*, "where they spoke quite boldly", needs only one dropped r, the kind of omission this writer makes elsewhere (*tar* for *tart*). It takes the written plural verb at face value and suits speeches at a strike camp. This is a word-sense judgment and I cannot prove it, but the solver's reading should not stand as the only one, and "my uncle" should not stand unqualified in the English and Slovak. Fix: make *nagy bát[r]an szóltak* the preferred normalization or give both readings, and update the Hungarian, English, Slovak and item 9.

2. **major: row 12/13 break is wrong in the ledger, and the evidence for the 9 is misdescribed.** On the card (`review/work/crops/r12end.png`) row 12 ends `… t a m [dark sign] o`; row 13 begins `r a i` at the left margin. The ledger, the literal block and item 1 instead put the o at the start of row 13 and call the dark sign "the end of row 12". The letters do not change, but the printed rows are not the card's rows. The "wide gap before the next sign" cited for the digit does not exist as described, since the o follows on the same row at about normal spacing. Fix the ledger and item 1.
   - Evidence the solver missed: there is a dot-like mark up and to the right of that o, consistent with an acute (*ó*, as in *óra*), which would favour 9 *órái[g]* over *korai*. This is suggestive, not proof, since it could be a stray mark.
   - The 9/k doubt itself is real. Its closed top and left-hooked foot are what the k does on this card (row 8), so keep it disclosed.

3. **minor: item 5 and the ledger header overstate the d/h ambiguity.** On this card d is a short stroke on the left then a tall one (12 cases); h/p is a tall stroke then a short one on the right (8 cases). I found no case where the two forms need word sense to separate them. Rows 5 and 18 *de* are d by form, not "from sense". Only the h/p choice rests on word sense.

4. **minor: stamp corner `leg jobban` is not what the pixels plainly show.** Line 5 reads `leg jo` followed by a tall looped letter, a small letter and `on`/`om`, more like *jobon* than *jobban* (`review/work/crops/stamp.png`). *Legjobban* is the right sense, but the literal form given should be marked as uncertain. The same applies to line 4, which reads `aval`, normalized *avval*.

5. **minor: "Why I believe it is correct" has small inaccuracies.**
   - *Jolánkám* occurs 3 times, not 2.
   - "The only signs not read straight are items 1 and 3" overlooks items 2 and 6 (`rr`, `mes`).

## What I could not verify

- Whether the second postmark is Gyöngyös. I see only partial letters, and the solver also marks this as unverified.
- The small word after *úrleánynak*: it looks like *szeretettel*, as the solver says, but it is not certain.
- The sign under the blot in row 22 beyond the inference above; and what the dark overwritten signs (rows 3, 4, 10, 11, 12, 15, 20) originally were.
- Who the sender is, or who the dead girl is.
- The 9/k sign and the finding 1 reading remain word-sense judgments; no independent evidence can settle them here.
