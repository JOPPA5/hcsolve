REVISE

# Review 1 of HCP1260 (reviewer Claude Opus 5.5, 2026-11-01)

The decipherment stands: the key is right and the message is what SOLUTION.md says it is, apart from one clause. Concrete fixes are needed: the ledger contains a sign that is not on the card, and a mark that is on the card is reported as absent. One clause also has a better reading that the solver did not offer, and that reading follows from the solver's own item 2.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1260/work/decode.py`. All 4 SHA-256 checks print OK. The output matches the literal rows and normalized text in SOLUTION.md.
- Read every main row and corner row myself on `work/hires/*_adr.jpg`, at native size (`review/work/mk.py`, `crops/band0-5.png`) and enlarged 3-5x (`mk2.py`, `mk3.py`, `crops/dh.png`, `r22.png`, `misc.png`, `r3j.png`). I also viewed the solver's corner crop. I formed the reading knowing the solver's text, so this is not a blind transcription.
- `review/work/indep.py` holds my own transcription as tokens named by shape, with its own key table (443 letter values, leaving out literal C7), and diffs it against `work/ledger.txt`. 25 of 29 compared rows are identical. The 4 differences are:
  - R5: literal h where the solver has d (he disclosed this; finding 3).
  - R18: literal d where the solver has p (disclosed).
  - R22: `ü` and no `v` (findings 1 and 2).
  - C4: `ü` where the solver has `ű` (finding 2).
- Key coverage: all signs on the card take a value from the HCP1216 key table, with nothing left over except the disclosed clear `7 het`. The address is in clear ("Szépreményű" sits beside row 6 in a different ink and hand style, the running script of the address). The picture side has only print and no handwriting (`crops/pic.png`).
- Sister cards: HCP1216 has "sírig hű kedvese Feri"; HCP1217 has "Hogy mulatott vasárnap?" and "Isten vele, édesem". The closing and sender fit the family. "Viszontlátásra" and the addressee fit too.
- Language: credible period Hungarian with the writer's normal spelling (ijen, anyira, ezel, erölirásban). This is not words forced onto noise. Long unbroken sentences decode with one key.
- Disclosed weak signs checked on the pixels: R1 sign 6 (blot, t acceptable), R5 and R18 (tick side really is as stated), R14 h (blot; word sense), R20 sign 1 and the overwritten R20 g, C5 sign 1 (foot-left stroke). All are honestly described.
- Sample of ordinary rows (2, 4, 9-13, 15-17, 19, 21): no disagreement.
- No published solution: nothing suggests one was used.

## Findings

1. **major - R22: the ledger has a chevron (v) that is not on the card.** The ledger and the literal output give `k e d v e ) e + e F i` (*kedveseferi*). The card shows S, three bars, tick + stroke, three bars, bowl, three bars, cross, three bars, F, i (`crops/r22.png`, panels b and c). That is *kedese feri*. There is no chevron between the d and the following e; the chevrons elsewhere on the card are unmistakable, and the only mark in that gap is a brown foxing spot. The literal text therefore prints a sign supplied from expectation, the very thing a sign ledger exists to exclude, and SOLUTION.md does not disclose it. It also undermines the "sírig hű kedve- ×2" repetition claim, because the two occurrences are not identical signs.
   Fix: remove the `v` token from the ledger, print literal `kedese`, normalize as `ked[v]ese` with the omitted letter bracketed, and add a disclosed item. The word itself is not in doubt, because C4 spells the v out and the family formula is firm.

2. **major - R22 and C4: the diacritic over u is misreported, in opposite directions.** Item 12 says *hu* in row 22 has "no diacritic visible". Two clear dots stand over the X in R22 (`crops/r22.png`, panel b, well above the sign, the same dots as on R11 *ügyet*). The ledger token should be `U`, literal *hü*. In C4 the same two-dot mark is encoded as `UU` and printed *hű*, while the key section says two dots on x "in the margin" give ű. That is a value depending on position, supported by nothing on the card: one mark, ü in R11. Literal should be *hü* in both places, normalized *hű*, listed as a spelling normalization.

3. **major - R8: the sign read as h in *he* is the same shape the solver reads as d in R5, and the reading *de* was not offered.** Item 2 takes the tick-right sign in R5 as *de* on word sense. R8 has the same tick-right sign followed by three bars (`crops/dh.png`, "R5" and "R8"). The solver reads R8 literally as *he* and then emends the vowel to get *ha erről nem írok*. Reading the two alike gives *de erről nem írok*, "but I do not write about this": no vowel emendation, a shape slip already present on this card in R5 and R18 (d/h-p confusion runs in both directions), and a natural lead-in to *majd szóval fogom elintézni*. Item 9 calls the two signs "distinct" but only argues about their count, and item 8 says "the practical sense is the same", which understates this: *ha* makes it a conditional, *de* a separate statement, so *hogy hogy volna jobb* then has to stand alone and is left less clear.
   Fix: present *de* (I think it preferable) and *ha* as alternatives for R8, adjust the normalized text, the English and the Slovak, and treat R5 and R8 the same way. The clause "hogy hogy volna jobb" stays uncertain and should be stated so in the translation, not smoothed into "that it would be better". This is one uncertain clause in an otherwise clear text; the sentences around it read.

4. **minor - R3: the j of *haragudjon* is the same low-cross variant as the flagged R20 sign, and is not flagged.** `crops/r3j.png` shows a stroke crossing a sloping bar with a stub below, not the inverted T of R7/R8. The ledger has plain `j`. Mark it `j?` or add it to item 5; it helps the R20 reading, since *haragudjon* is certain.

5. **minor - C4: d rests on word sense.** The sign in *ked-ve* is two nearly equal tall strokes, which is closer to n (compare C1) than to the tick-plus-long-stroke d elsewhere. *kenve* is no word, so d stands, but the brief asked for d/n calls resting on sense to be named. Add it to the uncertainties.

6. **minor - R15 normalization.** *beszélhetem [m]agával* adds a definite verb form that does not suit *magával*; *beszélhete[k] magával* is the grammatical form and needs one supplied letter just the same (or take `-e m-` as written *beszélhete(k) magával*). The meaning does not change. Mention it.

7. **minor - R20 normalization.** The card has *az egeseg*, with no final e. Normalized *egészsége* adds a letter that is not there, in addition to the z. Item 6 says so, but the normalized line shows it without brackets. Bracket it, as is done for [hogy] and [m].

8. **minor - source capture.** `source/metadata.md` says the detail page timed out and the three tabs were not read, so "attaches no transcription or solution" rests on the catalogue row. SOLUTION.md states it flatly. Say so there, or re-read the tabs.

9. **minor - stale claims after the fixes.** "Why it is correct" says "the seven `?` signs" and lists the *kedve-* repetition. Update both.

## What I could not verify

- The postmark: too faint for me as well for place or date, and I made no special attempt beyond the solver's result. The card stays undated.
- Acute accents: not reliably visible, as disclosed.
- The figure read as 7 in *7 het*: its shape suits 7 (flat top, diagonal, heavy foot); no parallel figure on this card to compare.
- The surplus *ve* in C1/C2 (item 11): signs confirmed, explanation as a false start is plausible but not provable.
- What "this matter" was.
- The portal's Attachments tab, which I did not re-open (finding 8).

## Register

After the fixes this is a complete reading in the sense of the run's rule: the single uncertain clause is short and the rest reads. HCP1260 is not listed in skip.txt or register-exclusions.json. A MASC entry with a key-transfer role is appropriate once findings 1-3 are addressed. No FINAL state is claimed here.
