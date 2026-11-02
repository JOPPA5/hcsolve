REVISE

# Review 1 of hcp-1144 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands: this is a monoalphabetic digit-plus-mark text in Hungarian, signed Árpád, and it is not forced. But two signs in `work/transcription.txt` are misread, both in plain sight and neither disclosed. One changes a person's name (Jani, not Nani) and with it the "her" of both translations. The second changes így to úgy. Both are small edits. The one unread word stands alone, so the card can count as complete under the run's rule.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1144/work/decode.py` from the repo root: 4 hashes OK, "all 25 rows match; 456 cipher signs, 450 by the table, 6 by sense or doubtful", exit 0. Its output equals the plaintext in SOLUTION.md. The script prints a held clean text and only asserts the rows, as SOLUTION.md says.
- Wrote `review/work/mydecode.py`, with my own key typed independently and using the literal drawn sign, ignoring the solver's `~x` overrides. All 456 tokens are keyed. Its output differs from the claimed text only at the disclosed spots: `csjkol`, `udvözöl`, `lásni`.
- Compared the key with hcp-1174/work/decode.py and SOLUTION.md of hcp-1178, 1179: consistent. Árpád `1' 3, 9 1' 3` and csókol are the same as on hcp-1174. `.1` = u was removed from the reviewed key on hcp-1178, so here it rests only on this card (szervusz, and úgy, finding 2).
- Crops from the hires address side with `review/work/mycrop.py`, stored in `review/work/crops/`: all cipher rows in 2x tiles, including the part right of the green line and under the postmark. At 3 to 6x: the blot word, the row of Janinak, így/úgy, the postmark, jöjetek, pünkösdre, szervusz, the bottom-right block, the last row, menyországban. Corrected rows are in `review/work/transcription-reviewer.txt`, which decodes to `mert ugy is soká lesz kész` and `lesz meg janinak még most`.
- Claimed doubtful signs, judged on the pixels:
  - értesíteni: the sign under the postmark has a visible crossbar and tail, so 7, is fine.
  - szervusz: only the upper dot of the blotted 1: shows, as disclosed.
  - menyországban: as disclosed.
  - csókol: the second sign is a tall 6 as disclosed; a slip by the writer.
  - üdvözöl: one dot left, as disclosed, so udvözöl literally.
  - hű: two dots left of a 1 whose top joins the 5's flag; I accept it.
  - jöjetek: 1: both times, confirmed.
- Row order: the curve at bottom right does route as claimed; rows right of it read as the closing formula.
- Open heading and address agree with the scan. The picture side is a park pond with a small house and bridge, and has no writing.
- Context: 19 May 1916 is before Whitsun (11 June 1916). The verse rhymes and the prose is connected, ordinary Hungarian with period colloquial forms (montad, jöjetek). This is real language, not forced words.
- No published solution is attached on the portal record; none used.

## Findings

1. **major: the name is Jani, not Nani.** In `work/transcription.txt` row 10 the first sign after `)` is transcribed `6,`. Enlarged 6x (`crops/nan2.png`, also `crops/nani.png`, and the top of `crops/L4.png`), it is a plain 6 with empty paper below it, whereas the next 6 in the same word has a long tail, and all other 6, on the card show theirs. The word is `6 1. 6, 1 6, 1. 7` = **janinak**, "to Jani", an ordinary male pet name (János). The solver's own key gives this. Fix the transcription, the READ list and held text in decode.py, plaintext, both translations, NOTES.

   Consequence: "her address" and Slovak "jej adresu" and "Nani som" are unsupported. Hungarian has no gender, and Jani is a man's name, so use "his address", "jeho adresu", "Janimu som". Uncertainty 1 and the note "Naninól" need rework too. Also add Jani to the attestations of 6 = j.

2. **major: így should be úgy.** Row 8: the sign is transcribed `1`, but there is a clear round dot left of the 1, under its flag (`crops/igy.png`, 4x), the same mark as the `.1` of szervusz, which the key reads as u. So `.1 4.` = **úgy**: "mert úgy is soká lesz kész", "because it will take long anyway". The sense is as good or better, and the translation hardly changes (Slovak aj tak fits). Fix the transcription, decode.py, plaintext, and the key list that cites így for gy. `.1` then has three attestations, counting the udvözöl sign.

3. **minor: the counts overstate clean signs.** "450 by the table" includes the two 9-shaped ö of üdvözöl, which SOLUTION.md itself says are not table shapes, and `.1~ü` differs from the key. Mark them `~` so the count is honest.

4. **minor: two soft calls are not listed.** In pünkösdre the mark on the 7 is a short oval (`crops/punk.png`), between the long tail of `7,` and the dot of `7.`; only s makes the word. In the same word the `:1` left marks merge into one blob with the 1's foot. List both as read by sense. Also the mark on the first 2 in fényképészhez is short and slanted; é is sound, but say so if the list is meant to be complete.

5. **minor: the unread word is correctly left open, but the description can be tighter.** I confirm `5, 1' ? 6, 1 | 6, 0 5,`. The dot on the second sign is a single high one, so á stands; the 6, and 5, of "nol" are clear, so this is not a misread "hol". The blot has a flat top and a notch at right with a separate tail: `3,` is as likely as `7,`, and `8,` (t) is not excluded, which would give "lát-ni" and, with a slip, "nem látni, hol". That is only a hypothesis, and címét would be the wrong case for it. Keep it unforced, but state the other candidates, and say it may be two words. With Jani (finding 1) the "reason concerning her address" wording must become "his". Under the run's rule this one spot does not make the card partial, because it is alone and the rest reads; I would not stretch that further.

6. **minor: the exclamation mark.** A stroke and a low dot follow Margitkám in row 1. The solver printed "!" but the transcription omits it and the plaintext note calls punctuation editorial. Say this one is on the card and is not a cipher sign. The same applies to the hyphens at line ends (for example after értesíte).

## What I could not verify

- The HistoCrypt article linked from the portal was not read by the solver or me, so I cannot say whether it treats this card.
- Whether the verse has a printed source.
- What ángyika means exactly here, and who Jani is. No other card checked in the hcp-11xx SOLUTION.md files mentions Jani or Nani.
- I read every row at 2x and doubtful spots at 3 to 6x, not every one of the 456 signs at 3x or more. Two errors in about 456 suggests a few more single-mark slips are possible; I found none in the rows compared.
