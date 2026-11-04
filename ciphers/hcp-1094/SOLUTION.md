# hcp-1094 – Solution (round 1)

Solver: Claude Opus 5.5 (2026-11-03). No earlier work on this number; no published solution found, and the portal attaches none (status Not solved).

Card: picture postcard "Fröhliche Ostern!" (R&K 4630/4), Austrian 5-Heller stamp, postmark SCHNEEGATTERN (portal file name dates it 1912-03). Addressed in plain Latin cursive:
"An Wohlg. Fräul. Fanni Rauchenschwandner / beim Wallner in / Geretsek(?) Post / Schneegattern".

## Cipher type and key

Number substitution with a place-value (Greek/Hebrew-numeral style) alphabet over the German alphabet without J:

| a | b | c | d | e | f | g | h | i/j |
|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

| k | l | m | n | o | p | q | r | s |
|---|---|---|---|---|---|---|---|---|
| 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 | 90 |

| t | u | v | w | x | y | z |
|---|---|---|---|---|---|---|
| 100 | 200 | 300 | 400 | 500 | 600 | 700 |

Only values 1, 3, 4, 5, 8, 9, 40, 50, 80, 90, 100, 200, 400 occur. Register type label: MASC.

## Transcription

Three columns of numbers on the left half of the address side, written top to bottom (card turned 90 degrees), read right to left; letters separated by dots, words by wider gaps (read from 3x hires crops of work/hires/...__adr.jpg):

1. `400.200".40.90.3.8.100.` (the `"` stands for two umlaut dots written above the 200 group)
2. `4.9.80.` `4.5.9.40.`
3. `9.50.8.1.40.40.`

## Plaintext

German: **wünscht dir dein Iohann** = "[Fröhliche Ostern] wünscht dir dein Johann" – the printed greeting "Fröhliche Ostern!" on the picture side completes the sentence.

- English: "[A happy Easter] wishes you your Johann."
- Slovak: "[Veselú Veľkú noc] ti želá tvoj Johann."

## Command

```
python3 -I ciphers/hcp-1094/work/decode.py
```
Checks the SHA-256 of the source images and the hires address scan, then prints `wünscht dir dein iohann` (the umlaut mark in the transcription is mapped to ü).

## Uncertainties

- The "1" in column 3 is a continental 1 with a lead-in stroke; read as 1 = a (pixels and word sense agree: Iohann).
- ü in "wünscht" is written as 200 with two umlaut dots above the number group (corrected after review 1; see review/work/umlaut.jpg). J of Johann is the shared i/j value 9, normal for such alphabets.
- The values 500–700 for x, y, z are the natural continuation of the scheme but do not occur, so they are not verified.
- The place name in the address is read literally as "Geretsek" (possibly Geretseck); unenciphered and irrelevant to the cipher.
- A large pencil "4" below the columns and the HCPortal collection stamp are later marks, not part of the message.
- The postage stamp is still on the card; any writing under it cannot be checked from the scans. The picture side shows no handwriting.

## Why it is correct

Every number on the card is covered by one consistent place-value key, and the result is grammatical German that forms a natural Easter greeting with the printed "Fröhliche Ostern!" and is signed with a common first name. No sign is left unread and no letter is restored.

## Response to review 1

Verdict ACCEPT, three minor findings.

1. Umlaut written (minor) – agreed and fixed. The reviewer's 4x crop (review/work/umlaut.jpg) shows two short strokes above the 200 group, i.e. the writer marked ü as 200 with umlaut dots. The Uncertainties note was wrong and is corrected; the plaintext now reads `wünscht`. work/decode.py now carries the mark in the transcription (`200"`) and maps it to ü. Re-run from the repo root: `python3 -I ciphers/hcp-1094/work/decode.py` prints `source hashes OK` and `wünscht dir dein iohann`.
2. Transcription omits the mark (minor) – fixed: column 1 is now given as `400.200".40.90.3.8.100.` with the `"` explained.
3. "Iohann" (minor) – no change needed; the i/j = 9 explanation is kept and repeated in the report.

Steganography check (prompted by a note from the human that cards of another series carry hidden messages under the stamp): the Franz Joseph 5-Heller stamp is still attached on both scans, no writing shows around its perforations, and the picture side has no handwriting at all. Nothing hidden can be found from the scans; the possibility of writing under the stamp is stated as unverifiable, and the register type stays MASC.

Reading unchanged apart from the umlaut; closing with FINAL.
