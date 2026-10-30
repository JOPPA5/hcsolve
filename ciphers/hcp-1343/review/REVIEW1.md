REVISE

# Review 1 of HCP1343 / pc_hcp_24 (Claude Opus 5.5, reviewer, 2026-10-30)

The cipher, key and reading stand, except for one word in B15. "fool" is not supported by the pixels and changes the sense of that sentence. It must be reopened before FINAL.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1343/work/decode.py` passes the hash check for 4 files and prints the claimed plaintext. Its output matches `work/decoded.txt` and the SOLUTION.md text. STATS: 24 lines, 174 words, 699 tokens (697 letter and apostrophe signs plus the 2 brackets), 0 unknown.
- **Independent decoder.** `review/work/mydecode.py` has its own key table and tokenizer. Line by line it is identical to the solver's output once case and brackets are normalised.
- **Key coverage.** All 24 sign types in the transcription are mapped. Letter frequencies look like English (e, n/w, o, a, t lead). q and j each occur once; x and z do not occur.
- **Transcription against pixels.** I read every line of the card from `work/hires/pc_hcp_24_adr.JPG` (not from the solver's crops):
  - left panel, deslanted and enlarged (`review/work/strips.py`, P0–P7 L/R)
  - top margin, T0–T2 L/R and zT5, zT5R
  - divider line rotated, zS0, zS1
  - close-ups: zF, zF2, zNO, zH, zCARD
  - The review was done sign by sign, including dot count and slant on e, g, h, i. Every line agrees with `work/transcription.txt` except the third sign of the B15 word (finding 1).
  - Restorations and weak spots judged individually:
    - *darling*, arch where r is expected: seen; disclosed.
    - *dredful* × 3, caret: seen.
    - *dining*, final g: acceptable.
    - *harold*, blotted o, box and ) touching the divider: acceptable.
    - *news*, heavy caret: acceptable from context.
    - *movey*, m-o-v-e-y: clear, including the plain bar. The solver is right not to emend it.
    - *no* in B15, caret plus blotted circle with a smear below: acceptable, disclosed.
- **Sister card.** `hcp-1469/work/transcription.txt` writes *dredful* with the same caret (`) V=r? . ) F U L`, B05 and T5), so that spelling claim is true. Hand, recipient and layout agree. The body-then-top reading order is confirmed by the sentence running across "as ever / he did of Brownie".
- **Language and context.** This is natural Edwardian private English, in a consistent voice (third-person "Reg", underlined *dredful*). No forced word was found outside finding 1. Recipient and address are as stated.
- **Published solutions.** Portal capture shows none attached. The orchestrator's register check found no record. I found no sign of one being used.

## Findings

1. **major – "fool" (B15) is forced; the third sign is not a box.** Crops: `review/work/zF.png`, `zF2.png`.
   - The word has three signs, not the four the transcription gives (`F Q Q L`).
   - Sign 1 is a clear gamma.
   - Sign 2 is a round circle with a heavy vertical stroke at its right side. It is not the barred θ of o: every o on the card has a horizontal bar, or the blotted equivalent.
   - Sign 3 is not "a heavy box with an oval inside". It has a top stroke that overshoots to the left and a straight right stem that descends below the base line, which is the construction of the seven-shape r (compare `zH.png`, *harold*). A small round O sits inside it. Every box on the card (`zH.png`, *well*, *blinds*) is closed and has no descender. So this is r overstruck with, or corrected from, a circle.
   - The evidence therefore points to F + round sign + 7, not F-o-o-l. No l is visible.
   - **fear** is clearly the better reading: "she has no need to fear. Reg thinks just the same as ever he did of Brownie". It removes the solver's inserted "[he]" before *thinks*, because *Reg* becomes the subject, and it fits the reassuring run of the passage ("not to worry about it"). This writer also spells *dreadful* without its a. The e dot is not visible, so "fear" is also not fully literal; it needs an e absent or lost in the correction.
   - Required fix: stop asserting f-o-o-l. Change the transcription to record the signs actually seen (for example `F ?overstruck 7`), print the word as uncertain in the plaintext, for example `f[ea]r?`, and update the English and Slovak ("Nemá dôvod Rega klamať" and "She has no need to fool Reg"). The solver's disclosure (uncertainty 4) does not cure this, because its sign description is wrong and it dismisses the structural evidence. Plaintext line B15 prints "fool" unmarked, and decode.py does not count it as contextual.

2. **minor – "without any adjustment" is overstated.** "Why I believe it is correct" says the key gave the text "without any adjustment". The same file says m is new on this card, and HCP1469 has m as a left bowl/bar, while j, k, p and q are "attested with better resolution". Further, 4 r-places need special handling. State plainly: the HCP1469 key, plus the plain bar for m. "0 unknown" also counts the contextual r-places as known.

3. **minor – the caret in *dredful* is the n/w sign; the alternative is undisclosed.** Solver's "R" treats it as a stray r sign. As the sign is also w, the reading "dwedful" (baby-talk r→w, in keeping with third-person "Reg", "Brownie's own Reggie boy") explains it better than a substitution slip. Say so as a hypothesis, even if the normalised sense is unchanged. It does not apply to *dacling* (arch), which stays a one-off.

4. **minor – postmark and printed area.** The date line reads "… 5 07" as stated; the month strokes are unresolved. Faint marks over the printed C-A-R-D (`zCARD.png`: a large B-like shape, a bow right of A, a dashed vertical, a mark right of D) were not mentioned in SOLUTION.md. They match the postmark's broken print, not the pen signs, so I take them as the postmark's town line and not as omitted cipher, but they should be recorded. If the date is the 5th, then 5 June 1907 was a Wednesday and 5 July a Friday. That is odd for a card written at the end of a weekend; 5 August was a Monday. Do not infer a date beyond "1907" unless the month is resolved.

## What I could not verify

- The meaning of *movey* and the identity of Ethel, Harold and "her".
- The postmark month and town.
- That "fear" is the intended word: the overstruck word is a best reading, not a certainty.
- The English nuance of "she" in B14, which fits Brownie in the third person but is not proven.
