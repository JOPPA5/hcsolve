# HCP 1354 / pc_hcp_35 — Caesar (+1) postcard to W. Abbott, 5 March 1907

Status: **whole message read; review 1 verdict ACCEPT, four minor corrections made to the write-up, no letter of the reading changed.** No published solution of this card was found or used; the portal attaches none and shows Not solved.

## Origin

HC Portal cryptogram 1354 (`pc_hcp_35`). Picture side: coloured Frith's view with the faint caption "[Par]kstone From Constitution Hill", no cipher. Address side: halfpenny Edward VII stamp, postmark WIMBORNE 10 PM MR 5 07, addressed in clear to Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. The postmark agrees with the portal date (1907-03-05, a Tuesday) and with the date written on the card. Same recipient, same cipher and same signature `Mpp` as hcp-1398 (FINAL). The small circled figure at the top left of the address side is a later sorting mark, not part of the message; with POST CARD upright it is a tall stem with a closed lower loop, so probably 6 (first reported here as 5).

## Cipher and key

Monoalphabetic Caesar shift: each plaintext letter is written as the **next** letter of the alphabet; decrypt by subtracting one. The date line is in clear.

```
Cipher ABCDEFGHIJKLMNOPQRSTUVWXYZ
Plain  ZABCDEFGHIJKLMNOPQRSTUVWXY
```

## Transcription and plaintext (all ciphertext on the card)

Rotate the address side 90° counter-clockwise (`work/reading_full.png`). The message sits in the left half.

| Ciphertext | Literal plaintext |
|---|---|
| Tveefo. dibohf | SUDDEN. CHANGE |
| Jo. ifbejoh pg | IN. HEADING OF |
| mfuufs Npoebz | LETTER MONDAY |
| up. qptu dbse | TO. POST CARD |
| sfdfjwfe Tvoebz | RECEIVED SUNDAY |
| ? Gps XIZ ! Mpp. | ? FOR WHY ! LOO. |
| *(in clear)* March 5th = 07 | March 5th 1907 |

68 enciphered letters, all decoded by the one key (67 if the alternative in uncertainty 2 holds; the word does not change).

Non-letter marks in the message block, none affecting a letter: dots after `Tveefo`, `Jo`, `up` and `Mpp`; a heavy round dot just below the end of `sfdfjwfe`, directly above the I of `XIZ`, which is either another separator or a dot on that I; and a thin line from the X through the foot of the I into the foot of the Z, either the Z's foot carried back or an underline. An underline would fit the emphasis of WHY.

English (the plaintext language; the portal lists Unknown): *"Sudden change in heading of letter Monday to post card received Sunday? For WHY! Loo. March 5th 07."*

Slovak: *„Náhla zmena v oslovení listu z pondelka oproti pohľadnici prijatej v nedeľu? Prečo! Loo. 5. marca 1907."*

"Heading" most naturally means the salutation: this couple's cards vary it ("My own E. L. boy", "My own dearest"), so she seems to be asking why his Monday letter opened differently from the card she got on Sunday. That is interpretation, not on the card. "Sudden" and the capitals in WHY are hers.

## Command (from the repo root)

```sh
python3 -I ciphers/hcp-1354/work/decode.py
```

It checks the SHA-256 of all files in `source/` and `work/hires/`, decodes `work/transcription.json` and prints the table above with the letter count.

## Uncertainties

1. **`ifbejoh` = HEADING.** Read, not guessed. The first sign is a hooked minim with a dot up and to the right, the same form as the `i` of `dibohf` (`review/work/x_cmp.png`); the dot sits just below the tail of the `f` from line 1 but is separate from it. The `s` of `sfdfjwfe` is a different form, so READING (`sfbejoh`) is rejected on shape. LEADING (`mfbejoh`) is out too, because the `m` of `mfuufs` has two arches and this is a single stroke. The third sign matches the `b` of `dibohf`, the sixth and seventh match `o` and `h`. The fifth sign is a long looped descending stroke with a dot, a dotted `j`, the same form as the dotted descending `j` of `hjsm` on hcp-1398.
2. **`Tveefo` = SUDDEN: the second `e` is inferred.** After the `T` come a thick minim with a thin rising tick, then a solid black wedge with no visible eye, then one clear looped `e`, then `f` (`review/work/y_sudd.png`). I take minim plus tick as `v` and the wedge as an `e` filled by a fresh load of ink, since it is the darkest ink on the line. On the model of the two-minim `v` of `Tvoebz`, the wedge could instead be the second stroke of `v`, leaving one `e` (`Tvefo`, SUDEN, 67 letters). SUDDEN is not in doubt as the word; only whether the second D was physically written is.
3. **`qptu` = POST.** The first sign is very like the capital G of `Gps`; `q` is chosen because `gptu` gives no word.
4. **`Npoebz` = MONDAY.** A blot lies over `e` and the foot of `b`, but both are still visible. The initial N and long `p` differ clearly from `Tvoebz` two lines below, so these are two different days.
5. **`mfuufs`.** The middle minims are run together, and the first stroke of each `u` is not as tall as in `up`; LETTER is the only word that fits. A speck above them is not an i-dot.
6. **`dbse`.** The third sign is a compact hump, less clear than other `s` forms; CARD is the only word that fits.
7. **Punctuation.** The `?` stands at the left margin, before `Gps`; I attach it to the preceding sentence. It could belong with "For WHY". Dots after words are separators, as on sister cards; see also the note on non-letter marks under the table.
8. **`Mpp` = LOO**, the signature as read and accepted on hcp-1398. That it is a pet name is conjecture. The two `p` signs are close together, but each has its own stem and bowl.
9. **Date.** The sign above the "=" is read as a raised "th" with a long bar. Its bar runs under `Mpp`, which could instead be a separate underline.

Every letter was read from the scan with the one exception in uncertainty 2, where a filled sign is taken as `e`. No word is restored from context or from a sister card.

## Why it is correct

One fixed shift turns the whole message into English, including long words (RECEIVED, HEADING, SUDDEN, CHANGE, LETTER) with no free parameters. The key is the one used on accepted cards from the same correspondence (hcp-1386…1407), the signature agrees with hcp-1398, and the message reads as a coherent complaint. Tuesday 5 March 1907 suits a letter that arrived on Monday and a card that arrived on Sunday.

## Credits

Capture of sources by the orchestrator, solution by Claude Opus 5.5, 2026-10-30. No earlier work on this number.

## Response to review 1

Verdict ACCEPT. I rechecked each finding on the reviewer's crops and on the scan. All four are correct and all are fixed; the plaintext is unchanged. `python3 -I ciphers/hcp-1354/work/decode.py` was re-run afterwards: source hashes OK, same six lines, 68 letters.

1. **`Tveefo` less clean than presented (minor): fixed.** `review/work/y_sudd.png` shows what the finding says: thick minim with tick, solid wedge, one clear `e`. My "No letter is restored" overclaimed. The sign is now uncertainty 2 with the 67-letter alternative stated, and the closing sentence of Uncertainties is corrected. I keep the reading `Tveefo`, for the reason the reviewer also gives.
2. **Undisclosed dot after `sfdfjwfe` (minor): fixed.** Both the dot and the thin line through the foot of X, I and Z are visible in `review/work/x_xiz.png`. They are disclosed under the transcription table and recorded in `work/transcription.json` (`non_letter_marks`, `doubtful_signs`). `decode.py` ignores these keys, so its output is unchanged.
3. **Uncertainty 1 factually wrong (minor): fixed.** `dibohf` does have an isolated `i`, and `review/work/x_cmp.png` shows it matches the first sign of `ifbejoh`, dot included. The `j` is dotted too, and the dotted descending `j` of `hjsm` is visible in hcp-1398 `work/closing.png`, so the contrast with hcp-1386 is dropped. HEADING is now stated as read. LEADING is added to the rejected readings.
4. **Sorting mark probably 6 (minor): fixed.** `review/work/y_pen.png` shows a stem with a closed lower loop. The Origin section now says probably 6, and that the mark is not part of the message. The word "pencilled" is dropped because the medium cannot be judged from the scan.

Also corrected from the reviewer's check: the caption is now given as read, "[Par]kstone From Constitution Hill". The numbering of the later uncertainties moved up by one.
