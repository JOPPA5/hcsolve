REVISE

# Review 1 of HCP1228 (Feri to Tóth Jolánka) — Claude Opus 5.5, 2026-11-02

The key, the cipher type and the sense of the card stand. One word group in row 15 is misread, which changes a clause of the translation, and the ledger is not the sign-for-sign record it claims to be in three places. All are concrete fixes. No published solution was met, and I found no sign that one was used.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1228/work/decode.py`. All four SHA-256 checks print OK, and the literal text and normalized text match SOLUTION.md row for row.
- Read every row, and the six stamp rows, on my own 2.4x crops of the un-converted `work/hires/*_adr.jpg` (`review/work/p1a…p7b.png`, `stamp.png`), then used 3.5–7x crops at disputed places (`z*.png`). The crop tool is `review/work/crop_rv.py`.
- Wrote my own sign transcription with shape-named tokens (`review/work/my_transcription.txt`) and my own decoder (`review/work/my_decode.py`), which takes the letters from `hcp-1216/work/graphic-key.json`, not from the solver's key. Output is in `review/work/my_decode.out`. This reading is independent of the ledger file but not blind, because I had read the solver's text first.
- Result: 666 letters compared; 21 of 27 main rows and all 6 stamp rows agree with the solver, with damaged signs counted as restorations. Six rows differ. Rows 5, 7 and 21 include the disclosed h/p/d sense calls (my decoder prints the tall+tick sign as h by design). The real differences are in rows 5, 14, 15 and 22.
- Key coverage: every sign on the card falls in a family class and no new value is needed. The family key is applied unchanged, apart from the h/p/d sense calls the solver discloses.
- Language: real period Hungarian with plausible unschooled spelling. Formal third-person address, *sírig hű kedvese* and the Feri signature fit the family. Nothing reads as words forced onto noise.
- Row 4 `t`: the sign has a stem, a long curved top arm and only a stub at mid height. It is closer to a gamma than the SOLUTION suggests, so t is well supported.
- Row 8 `elmetem`: no n is present. Row 10: the strike covers the word. I could not recover it either, and the final chevron-like sign is struck too.
- Row 15 first `var[o]k`: blot over the sign, stub, hook and tail visible as described. The restoration is fair and disclosed.

## Findings

1. **major — row 15 is `hát én is`, not `héten is`.** Crop `review/work/z15a.png`. The second sign has two bars, not three, with a pale accent tick above it, slanting up to the right like the card's other accents; there is no third bar below. So it is a with accent (á), not é. The ledger token `E'` there is wrong. The fourth sign, three bars with a clear accent, is é, while the ledger has plain `E`. The signs are h á t é n i s: **Hát én is várok, várok...** ("Well, I too wait, I wait..."). This follows directly on the saying about those who endure and suffer, and is idiomatic, whereas `héten is` needed the free rendering "All week", and SOLUTION uncertainty 6 hedges exactly there. Fix the ledger, literal text, normalized text, English, Slovak and uncertainty 6. The tick is pale, so state that the accent on a is faint. The two-bar count does not depend on it.

2. **major — the ledger has signs that are not on the card: `annyit` and `annyi`.** Crops `review/work/z05any.png` (row 5) and `z22any.png` (row 22). Both show two bars, one pair of strokes, the low descender, i. That is a n y i (t) with one n only; the ledger writes `A N N Y`, so one sign was supplied from the expected word. The literal text must be `anyit` and `anyi`, and both go into the list of writer spellings at uncertainty 11. The reading itself is unchanged, but the ledger is described as one token per written sign, and this is the same spelling habit as *menyek-* in row 14.

3. **minor — row 14 is `menyeknek`, not `menyegnek`.** Crop `review/work/gk.png` compares 8 g signs and 8 k signs from this card. g ends in a straight tail; k ends in a hook curling left. The disputed sign has the hook, so it is k. SOLUTION uncertainty 5 ("the g for k is the writer's") is therefore wrong, and the word needs only the usual doubled-consonant normalization to *mennyeknek*.

4. **minor — restorations not disclosed as such.**
   - Row 17 `mentem`: uncertainty 7 says "the signs are clear", but the n and t lie under the wet blot (`z17.png`). The first stroke of n is firm, the second is ghostly, and of t only the top arm is firm. Both fit, but they should be listed like the row 15 blot.
   - Stamp row 4 (`zs4.png`): the disclosure is the wrong way round. The F arms and a pale stem are visible outside the triangle's right side, while the o lies on the printed monogram and only a loop-like bowl can be made out, yet the ledger marks only F as restored. Mark `O?` too and correct the wording of item 9.

5. **minor — written dots are omitted from the ledger.** Its header says `.` records a written dot, but small dots stand after `türöké` in row 13 and after the third sign in row 11 (`lo` + `l`, near x 300, y 855 of the hires scan), and neither appears. Record them or say they are treated as strays.

6. **minor — wrong counts in "Why it is correct".** The text says *mert* ×4 and *hogy* ×4. The solver's own output has mert 3 and hogy 5.

7. **minor — Slovak wording.** *zo zhľadania* is not idiomatic; use *z opätovného stretnutia*. Redo the sentence anyway for finding 1, for example: *Veď aj ja čakám, čakám, kým si budem môcť vychutnať radosti opätovného stretnutia.*

## What I could not verify

- The date and place of posting. The postmark is too faint to read on the hires scan, so 1913-09-07 rests on the file name, as the SOLUTION says.
- The struck word in row 10.
- `hana` in row 17. The signs h a n a are firm, but the assumption that it means *hanem*, and the supplied e of *[e]lmentem*, rest on sense. This is disclosed as the weakest point. It is a single word in a sentence that otherwise reads, so it does not make the card partial.
- Whether the two bars in the stamp disc (row S5, the a of *imádója*) are the writer's or part of the printed design. They look like pen strokes; if they are printed, that a is supplied too. The word is fixed by rows 26–27 either way.
- Whether a published solution exists outside the portal. I ran no web search and rely on the portal capture and the orchestrator's register check.

## Assessment for the solver

The fixes are local and the reading stands. Once findings 1 to 7 are addressed, the card counts as complete, because the only unread items are the writer's own cancelled word and the single doubtful `hana`. Finding 1 changes the literal text and translation of one clause, which the solver should weigh when choosing between `FINAL` and `DONE2`.
