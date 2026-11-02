REVISE

# Review 1 of HCP1224 (Claude Opus 5.5, reviewer, 2026-11-02)

**Summary.** The key is right and the card reads as coherent Hungarian from start to finish, so the reading stands. But the ledger is not a true record of the signs. In row 26 it contains signs that are not on the card and it silently corrects others to the expected word. SOLUTION.md presents these as literal text and in one case describes them wrongly. The ledger and the uncertainty list must be fixed before FINAL. No translation changes beyond small points.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1224/work/decode.py`. All four hashes OK. Output matches the "Literal decipherment" block in SOLUTION.md and the normalized text, 574 tokens.
- Compared the key with HCP1216 SOLUTION.md (table and decode_opus.py): same classes, same values. The HCP1224 table merges nothing into a new sign. "d" written as tall + short is an extension of the disclosed h/p homograph (see finding 8).
- Own transcription by sign class in `review/work/mine.txt`, own key and diff against the ledger in `review/work/verify.py`:
  `python3 -I ciphers/hcp-1224/review/work/verify.py`.
  This pass was not blind, since I had read the solver's text first; I read the signs from the scan, not from the ledger. Five differences result: rows 3, 21 and three in row 26 (findings 1 to 5).
- Pixels: read all rows on the hires address scan at 1:1 and again at 2x (`review/work/t1-3.png`, `a1-6.png`). Enlarged 3x to 6x: rows 2, 3 end, 4, 15, 19, 20, 21, 22, 24, 25, whole of row 26, all stamp rows (`z*.png`, `y*.png`, `r*.png`, `stamp.png`).
- Picture side viewed (`review/work/pic.png`, `picmarks.png`, `picred.png`): a photograph. No writing. A row of about a dozen small dark dots across the woman's garment and two red streaks are part of the tinted image or staining, not script, as far as I can tell.
- Address side in clear: Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás. Confirmed.
- Blots checked: row 2 a, row 4 a, row 12 n, row 15 j, row 24 h, row 24 k; these are honest calls by word sense as stated. Row 3 end: the final sign is the crossed curve with no dot, and "kami / am" is as disclosed. Row 8 two k signs and row 20 extra t + o are real and disclosed. Stamp row 2 sign 6: a gamma with the two a bars beside it, so t + a is well supported and better than the solver's own caution suggests.
- Language and context: period Hungarian, informal spelling of one writer, consistent with HCP1216 (*ojan*, *egesseges*). Names and places fit the family. No published solution found or used; the portal attaches none.

## Findings

1. **major. Row 26, "egészséget": the ledger holds a sign that is not on the card, and the disclosure is false.** Ledger: `J O E G E Z S E G E T`. On the card (`review/work/z26j.png`, `cmp.png`) the sequence is: loop (o), three bars (e), g, one curved sign, right bowl (s), three bars, g, three bars, gamma. There is no e between g and the curved sign, so there are 8 signs after the o, not 9. The curved sign is also not the z of this card (compare the crossed diagonal in rows 3, 7, 22, 23): it has a closed lower loop and a hooked right end, like the undotted o or i, and no dot. Uncertainty 8 says the row "has z s rather than sz: literal *egezseget*"; that literal does not exist. Fix: ledger `J O E G {o|i?} S E G E T`, literal *eg?seget*, normalized *egészséget* as a word-sense call from the set phrase *jó egészséget kívánok* (HCP1216 spells *egesseges*). The word itself is safe.

2. **major. Row 26, "valakinek": the ledger adds an a.** Ledger `V A L A K I N E K`. On the card (`review/work/r26a.png`): chevron, two bars, wave, section sign, dotted i, two strokes, three bars, s-shape. Nothing stands between the wave and the k. Literal *valkinek*, a real colloquial contraction. Keep the normalization but correct the ledger and list it among the writer's spellings.

3. **major. Row 26, "vele": the literal is v-a-l-e.** Ledger `V E L E`. The sign after the chevron has exactly two bars, with clear card above and below (`review/work/y26v.png`); compare the three-bar e signs just after it (`z26v.png`). Literal *valeedesem*, normalized *vele édesem* as a slip for e. Correct the ledger and disclose it. Items 1 to 3 together mean the literal row 26 printed in SOLUTION.md is partly the expected text, not what is written, and "574 tokens" is wrong: the ledger should have 572.

4. **minor (resolves an uncertainty). Row 21: the sign after the struck one has three bars, so the literal is {#}-e-m, not {#}-a-m.** `review/work/y21.png` shows three bars in one column after `#`. The solver counted two, apparently taking the lowest for row 22, but the row 22 a has its own two bars, lower and to the right. Uncertainty 4 ("the bar count disagrees with *nem*") should go: the word is plainly a corrected *nem*. The bars are slightly more widely spaced than usual, and I would still mark the struck n as a sense call.

5. **minor. Row 3, *köszönök*: the first o after z has two dots.** `review/work/r3end.png`. Ledger `O N O:` should be `O: N O:`. The literal in SOLUTION.md (*köszonök*) is wrong by a dot. Row 22 *köszonom* has no dots at that place in my crops and stands.

6. **minor. Counts in "Why it is correct".** "hogy ×8": the row-contiguous count is 7, *valahogy* included (`verify.py`). Update it. "574 tokens" per finding 3.

7. **minor. Row 24: a real full stop after *öne*.** There is a clear dot after the *öne* e (`review/work/a5.png`). This favours "a szívem már rég az öné. Édesem, hogy gondolhat olyat, ..." over the solver's "az öné, édesem. Hogy gondolhat...". Change the normalization and all three translations, or say why not. A comma-like mark between the two a of row 23 (*írta, a szívem*) agrees with the punctuation as normalized. Say that the writer sometimes punctuates.

8. **minor. Incomplete disclosures.** (a) Row 18 k of *harmadik* is a heavy blot on a section sign, not listed; it is read by word sense. (b) Ledger class D is used in rows 24 (*gondol*) and stamp rows 1, 4, 7, where the sign looks like tall + short rather than the joined 4-like d of rows 1, 5, 8, 16; item 7 lists only rows 13 and 18 as h/p/d calls. Mark them `H:d` or say that they rest on word sense. (c) Stamp row 7 has an acute tick over the first o of *dód*: this confirms ó and could be recorded.

9. **minor. Context left out.** The large postmark reads Budapest (BUDAPE..., 912 OK), so "itt" (here) is apparently Budapest, which suits a workman comparing wages with Gyöngyös. Add it to the context, with the caveat that a postmark gives the posting place only. The day of the month is not legible to me, so 1912-10-12 remains the portal's date.

## Register entry

The card meets the completeness rule once the above is fixed: only *a mi ám* (one phrase, disclosed) is an editorial division, and the rest reads. Type label MASC. Report must describe the corrected row 26.

## What I could not verify

- The sense of rows 3 to 4 (*a mi ám jóban lettünk*): I found no better division, and the phrase remains awkward.
- The class of the curved sign in finding 1 (o or undotted i): no sign shape settles it.
- Whether the Feri of this card is the same man as on other family cards.
- Acute accents, which are too faint to audit in full; ledger leaves them out by design.
- The row of dots on the picture side under magnification beyond the scan's resolution; I treat it as non-script without proof.
