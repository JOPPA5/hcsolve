REVISE

# hcp-1179 review, round 1 (reviewer: Claude Opus 5.5, 2026-11-01)

The decipherment stands: the card carries a Hungarian rhymed couplet in the Mezőkövesd family digit cipher. Fixes are needed in one word's treatment (`kar?im`), in two transcription details, and in some key and sister claims. I found no sign that a published solution was used.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1179/work/decode.py` from the repo root. Hashes are OK, and the output matches the claimed plaintext (`mindent megtennéK én érted alegszeb karj?im küldöm néked`).
- Read all signs on my own crops of the hires address side: `review/work/crop.py`, `crop2.py`, `crop3.py` (r1 to r4, up, z_*, y_*; 3x to 10x, plus a green-channel stretch of the blot, `y_blot_g.png`).
- Sign by sign, I confirm every token in `work/transcription.txt` except the mark after the second-word blot (finding 2) and the mark on `2` in néked (finding 3). Crossed 7 and flagged 1 are kept apart consistently; every 7 on this card is crossed.
- Independent decode: `review/work/indep.py`, with my own sign list typed from the crops and values taken only from the hcp-1174 table. Output:
  `mindent / megtenné[blot] / én / érted / a[5.]egszeb / kar[8.]im / küldöm / ncsked`
  So the only places not read by key alone are 5., 8., the blot and the `2,`-like mark.
- Key coverage: all other tokens decode. `:1` = ü and 1, = b have outside support (`:1` in hcp-1174 üdvözöllek; 1, in hcp-1175 `4 0, 1, 5, 0, 3. 0, 8 8 1. 4, 1. 8` = főb lövöm magam, which agrees with that card's transcription file).
- Language: real Hungarian. The two clauses rhyme (érted / néked), which the solver did not note. That supports both the row order and the form néked. Bottom row first is also where the rhyme word falls at the end. The open verse (Poéta én sohasem voltam ...) reads as the solver gives it where I checked it.
- Dot after the upper-row final 3: present (`z_ned.png`), so the row-end period is real.

## Findings

1. **major: "karj?im" is the wrong lead reading of `8.`; `8.` is most likely 8, = t, giving `kartim`, a card word.**
   - The mark on 8 is a round dot, clear (`y_8dot.png`). The sign exists as the solver says.
   - This writer has a confirmed dot-for-comma variant in this very passage: `5.` = `5,` = l (`a legszeb`), and the hcp-1178 review settled the same point. So the first hypothesis for `8.` is the known sign `8,` = t, not a new letter. The solver lists 5. as a variant of l but does not apply that to 8.
   - j has no support: no sign for j is attested in the family (hcp-1178's `5.` = j was rejected in review), and the solver admits that karjaim would need a missing a and the wrong case. "I send you my finest arms" also makes poor sense.
   - The open text on this very card is about sending cards: "Második lapot küldöm ... Küldök még én százat is". `kartim` points to kártya, "card" (kártyám / kártyáim, "my card(s)"), with a loose or dialect spelling. That reading is not clean either: y and an a are not written, and the 1 is unexplained. I do not claim it as proven.
   - Fix: report the word as `kar[8.]im`, literal `kartim` if 8. = 8,; give kártyám/kártyáim as the leading sense and karjaim as a weak alternative. Change key.json (`8.` should not be "j?"), both translations, and uncertainty 1. The word remains not fully understood, and must be labelled so. The rest of the text reads, so under this run's rule it stands as a single uncertain word, not a partial.

2. **major: the blot is under-described and the `[7]` restoration ignores a visible mark.**
   - The blot and its surrounding smear span about 157 px of the hires scan (`y_blot.png`), which is room for 2 to 3 signs with marks, not one, and the solver's own "about two sign widths" does not fit the single `[7]` in the transcription.
   - Immediately right of the blot, before the `2.` of én, stands a comma-shaped mark with an arched head, of the same form as the comma after 6 earlier in this word (`z_blot.png`, `y_blot.png`, `y_blot_g.png`). SOLUTION does not mention it. If it belongs to the last hidden sign, that sign is not plain 7.
   - The enhanced crop shows a left lobe, a long diagonal stem with a low horizontal, and a heavy mass. I cannot read any of them as a certain digit. It may be a correction.
   - megtennék is still the best sense, because the first-person form fits "én", and it remains a restoration by sense. Fix: state the width, the comma and that the hidden signs are unknown in number; keep [k] as a sense restoration; change the comment in transcription.txt.

3. **minor: the `2.` of néked is not what the pixels show.** There is no separate dot after this 2. The one candidate mark is a hook at the height of the 2's middle with a tail running down-left into the row below (`y_hook.png`, `z_ned.png`). It has the shape and tail length of this row's commas (see `0,` in `z_ku.png`), though it merges with the lower-row 1 and may partly be that stem. So the pixels favour `2,` or nothing, and key alone gives ncsked. néked rests entirely on word sense and on the rhyme with érted. Uncertainty 4 discloses a doubt but presents the dot as the reading, and transcription.txt writes `2.` with no flag. Fix: flag the token as read by sense, and add the rhyme as the evidence.

4. **minor: false or inconsistent statements about the key and sisters.**
   - The key table and uncertainty 7 say plain 5 = l "here and on the sisters". No plain 5 occurs on this card, and hcp-1174's table has 5 = h. Remove `5` from the l row in the table and key.json.
   - Uncertainty 3 calls `:1` "attested once" and the table says "one use". hcp-1174 has `:1` = ü in üdvözöllek. This improves the claim; it does not rest on this card's sense alone.
   - The sister strings quoted under "Key recovery" differ from hcp-1174's filed reading: the heading ends `7 1' 8` there (high dot, á), not `7 1. 8`; éled has `5, 1: 3` there, not `5 1: 3`. I did not re-read the hcp-1174 pixels, but the two solvers disagree and SOLUTION should say so or conform. The word "all 13 signs of the heading" depends on this.
   - The solver wrote that "those cards are unfinished", which is correct for hcp-1175, but the comparison with hcp-1174 and hcp-1178 should now cite their filed readings.

5. **minor: attribution of the signature.** "Sz. A. (can also be read Sz. K.)" is fair for the pixels, but hcp-1174 is signed Árpád in cipher and hcp-1175 reads Sz. A., which favours A. Say so.

6. **minor: the plaintext output of the single command** prints `alegszeb` without a word break and the capital K marker unexplained. Split the article, or document that the output is a raw form. No effect on the reading.

## What I could not verify

- What lies under the blot (finding 2).
- The kártya sense of `kartim`; it is a proposal, not established.
- The tick at the extreme upper right of the card corner: a short dark dash running off the edge (`y_end.png`). It may be a mark for another sign, or a stray; undetermined. hcp-1174 has a high-dot sign 1', but I have no evidence of a high mark on 8.
- Whether the mark after 2 in néked was a comma as written or a merger with the row below.
- The struck-through open text in full; I checked only the parts used here.
- The HistoCrypt article linked from the portal was not consulted by me.
