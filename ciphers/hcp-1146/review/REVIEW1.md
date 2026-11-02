REVISE

# Review 1 of hcp-1146 (reviewer: Claude Opus 5.5, 2026-11-02)

The key and nearly all of the reading stand. Two concrete errors must be fixed. One enciphered word is misread, and the card's written place and date line is missing, with SOLUTION.md stating that no such date exists. Neither changes the key type or the sense of the rest.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1146/work/decode.py`: exit 0, all four hashes OK, 311 signs, output equals the SOLUTION.md plaintext.
- Wrote an independent decoder, `review/work/indep.py`, with its own hand-written key and my correction from finding 1. Run: `python3 -I ciphers/hcp-1146/review/work/indep.py`. All 311 signs decode; 30 distinct signs, none unused. Apart from `városban` the output agrees word for word with the solver (accents folded).
- The base key agrees with the hcp-1174 table. The added signs (`.1`, `6`, `6.`, `4.`, `8.`, `4`) are each consistent across their occurrences on this card, though `6.`, `8.` and `4` occur once each.
- Checked the transcription against `work/hires/...adr.jpg` with my own 2x to 5x crops (`review/work/crop.py`; `review/work/*.png`). I covered every cipher row, not a sample, reading the words below against their crops: greeting (`t0`), rows 1 to 7 (`a1 a2 b1 b2 c1 c2`), verses (`d1 d2 e1 e2 f1 f2 g1 g2 h1 h2`), closing (`udv hu date`), and the restorations (`varos small1 small2 megis`).
- Dating logic: 14 April 1916 was a Friday, nine days before Western Easter (23 April), so "not coming on Sunday, only at Easter" fits exactly.
- `register-exclusions.json` and `skip.txt` do not list 1146.

## Findings

1. **major: `városian` is a misreading; the card has `városban`.** In the first verse line the sign before `1. 6,` is `1,`, not `1`: a separate, full comma stroke stands under the 1, the same shape and size as the comma of the `6,` beside it (`review/work/varos.png`, 5x). `work/transcription.txt` line V1 should be `3. 1' 3, 0 7, 1, 1. 6,`, which decodes by the table to `városban`. The line is then `Itt e városban járok` ("Here in this town I walk"), which matches `e városban` in the next stanza's open text and replaces an invented sense. Required: fix the transcription and plaintext, change the English ("Here I go about in town fashion") and Slovak ("Tu chodím po mestsky") lines, delete Uncertainty 6, which says outright that `városban` "is not what the signs give". The word adds a further `1,` to the table count, so recount the sign statistics if any change.

2. **major: the card's written place and date are omitted, and SOLUTION.md denies them.** The last line of the message, below the signature, reads in open script `Mezőkövesd. 1916.` followed by `IV/14`, in the same blue (`review/work/date.png`, `date2.png`; also visible in `review/work/adr_full.png`). SOLUTION.md says "The card itself carries no written date" and "The date 1916-04-14 comes only from the collection file name". Both are false. Required: add the line to the plaintext and to both translations, add it to the hard-coded print lines in `decode.py`, and correct the Card section. This also adds direct evidence for the "Why I believe" section, and it gives the place the family's other cards carry. The solver is right that the postmark date is illegible; I could not read it either (`review/work/postmark.png`).

3. **minor: address spelling.** The card has `Szépreményü` with two dots; the solver prints `Szépreményű`. Print as written or say the double accent is normalised.

4. **minor: count of sense readings understates the `mulattatlak` dependence.** Disclosed, but the headline "308 of 311 decode by the table" counts the two signs of Uncertainty 4 (`1.`, `7`) as table readings although they rest on assigning strokes to the row above. I agree with that assignment: the upper strokes line up with the descending commas of the row above (`small1.png`, `small2.png`). The headline should say so, for example 306 clean plus 5 sense or overlap readings.

## Restorations judged on the pixels

- `hála`: no comma under the second 5, confirmed (`b2`). Sense certain. Disclosed.
- `mulattatlak` sixth sign, and `1.`, `7` near the end: overlap with commas from the row above. Reading sound, disclosed.
- `mégis` last sign: a blotted, overwritten loop with a comma stroke after it (`megis.png`). It is not a clean 7. By sense only, disclosed; the verse needs it.
- `Ezer` E, `Vagy` V: over printed text, disclosed.
- `üdvözöl`: three strokes after `9` look like an extra sign, but they are the long tail of the 9, its comma, and the comma of `0,`; the reading stands (`udv.png`).
- `Margitkám!`: the low dot after the final 8 is the dot of the exclamation mark, not `8.` (`t0.png`).
- `hogy`: the mark after the 4 is a short dash, as disclosed (`a2.png`).

## Judgement of the text

Apart from finding 1 the plaintext is natural Hungarian of the period: three rhymed stanzas with a plain frame, and the open words join the enciphered ones grammatically. Names, recipient and place fit the correspondence. No published solution was used, as far as anything here shows. The solver's Uncertainties 7 to 10 are fair.

## Could not verify

- Whether the HistoCrypt article the portal links discusses this card. The solver did not check it and neither did I.
- The postmark date.
- Whether the short strokes in the right margin near rows 9 to 12 mean anything; they look like stray punctuation. They do not form a clause, so they do not affect completeness.

## After the fixes

No new review round is needed for findings 1 to 4 if they are applied as stated: finding 1 changes one sign and one word, finding 2 adds an open line. The card would then read in full and qualifies as complete.
