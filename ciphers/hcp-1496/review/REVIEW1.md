ACCEPT

# Review 1 — HCP 1496 / pc_hcp_177 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I read all nine rows of numbers from the scan myself and my transcription is identical to `work/transcription.txt` (93 numbers). Under the direct alphabet 1=A … 26=Z the whole stream reads `HELLO RICA HOW ARE YOU I WOULD LIKE TO SEE YOU I SAW SIMON AND HE ASK ME IF I HAD BEEN UP HOME THAT LOOKS BAD ANS SOON FMS`. The findings are small additions to the uncertainty list.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1496/work/decode.py` runs, hashes pass, prints the claimed plaintext and `Encrypted numeric positions: 93`. Note that the word spacing comes from the hand-written `work/words.txt`; the script asserts that it contains exactly the decoded letters in order, so it cannot alter the text.
2. **Independent reading of the scan.** `review/work/crops.sh` (sips; PIL is not installed) cuts the message into three 3.5× bands (`b1_big.png`–`b3_big.png`) and 6–20× details of the doubtful numbers (`d5`–`d8`, `n6end`, `n8end`, `n8last`). My reading, `review/work/my-transcription.txt`:

   | Row | Numbers | Letters |
   |---|---|---|
   | 1 | 8 5 12 12 15 18 | HELLOR |
   | 2 | 9 3 1 8 15 23 1 18 | ICAHOWAR |
   | 3 | 5 25 15 21 9 23 15 21 12 | EYOUIWOUL |
   | 4 | 4 12 9 11 5 20 15 19 | DLIKETOS |
   | 5 | 5 5 25 15 21 9 19 1 23 19 9 | EEYOUISAWSI |
   | 6 | 13 15 14 1 14 4 8 5 1 19 11 | MONANDHEASK |
   | 7 | 13 5 9 6 9 8 1 4 2 5 5 14 | MEIFIHADBEEN |
   | 8 | 21 16 8 15 13 5 20 8 1 20 12 15 15 11 19 | UPHOMETHATLOOKS |
   | 9 | 2 1 4 1 14 19 19 15 15 14 6 13 19 | BADANSSOONFMS |

   `diff` against the solver's file: identical.
3. **Independent decode and key check.** `python3 -I review/work/decode_review.py review/work/my-transcription.txt` (own code). 93 numbers, all in 1–26, letters used `ABCDEFHIKLMNOPRSTUWY`. A direct alphabet cannot conflict; every number on the card is used; no number is left over. Nothing else on the address side is in cipher, and the picture side carries only the printed caption "Good Bye."
4. **Plaintext.** Colloquial American English of the 1910s with typical informal spelling: "he ask me" (dropped -ed), "up home" (regional for "back home"), "Ans soon" (common postcard abbreviation of "answer soon"), initials as signature. Nothing looks forced; the letter sequence is long (93) and fully coherent under one fixed key with no adjustments. The solver keeps ASK and ANS literal and says so — correct.
5. **Context.** Addressed to `Miss Fr?derica Clark, Highland Park, Ky.` (Highland Park is a Louisville neighbourhood); `Rica` as a short form of Frederica fits. Bamforth & Co. card "Copyright 1910", U.S. 1-cent Franklin stamp (Washington–Franklin series), so the card is 1910 or later; the portal has no date.
6. **Prior solutions.** No register entry for URL 1496 / `pc_hcp_177` in `work/register-snapshot.json` (grep); not in `skip.txt`.

## Findings

1. **minor — doubtful glyphs to add to the uncertainty list.** The solver flags 15/10, 14/19 and 2/3. From my details I would add:
   - row 6, `4` of AND (`d6_big.png`): written over another digit (heavier, double outline); 4 is the final form.
   - row 6, last number `11` (`n6end_big.png`): the second `1` runs into its comma hook and at normal size looks like `13`; at 20× it is two plain strokes, i.e. 11 (K of ASK).
   - row 5, `1` of SAW (`d5_big.png`): a bare stroke squeezed between `19,` and `23` that could be taken for a comma.
   - row 8, first `15` of LOOKS (`n8end_big.png`): the 5 is a closed blob, `10` is possible graphically; the solver flagged this one. The last number of row 8 is a looped `19` (`n8last_big.png`), not `15`.
   None of these changes the reading; in each case the alternative produces a non-word.
2. **minor — the underline strokes.** Most numbers carry a long hooked comma, and several strokes run under two or three numbers (e.g. under `12 15` in row 1, under `15 23 1` in row 2). They do not coincide with word boundaries (row 1 underlines `LO` inside HELLO), so the word division in `words.txt` is editorial. `SOLUTION.md` says spacing is "separately checked against the decoded stream", which is true, but the report should state plainly that the card has no word dividers.
3. **minor — addressee spelling.** `review/work/addr_big.png`: the first name looks like `Friderica` (i after r, then a u-like `e`) rather than `Frederica`; the surname is `Clark` (portal: "Celark", a misreading of the looped capital C). The solver already keeps image and catalogue spellings apart; just do not normalise the first name silently.
4. **minor — dating.** Add the terminus post quem from the card itself (copyright 1910, 1-cent Franklin stamp). The postmark (`pm_big.png`) shows only fragments (`…AND`, `A…`, `18`) and does not give a reliable date — the solver's "not confidently read" is right.

## What I could not verify

- Who SIMON and FMS are, and where "up home" refers to; the solver makes no identity claim.
- The postmark town and date.
- Whether a decipherment has been published elsewhere; I relied on the register snapshot.
