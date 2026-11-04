ACCEPT

# Review 1 – hcp-1094 (reviewer: Claude Opus 5.5, 2026-11-03)

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1094/work/decode.py` (from the repo root) prints `source hashes OK` and `wunscht dir dein iohann`, identical to the claimed plaintext.
2. **Independent decode.** `review/work/verify.py` builds the key from scratch (German alphabet without j, nine letters per decade: a–i = 1–9, k–s = 10–90, t–z = 100–700) and decodes my own transcription. Output: `wünscht dir dein iohann`. All 13 values used (1, 3, 4, 5, 8, 9, 40, 50, 80, 90, 100, 200, 400) are in the key; no value is left over.
3. **Transcription against the pixels.** I cropped each of the three vertical columns from the hires address scan `work/hires/...__adr.jpg`, rotated them 90 degrees and enlarged them 2x (`review/work/col1.jpg`, `col2.jpg`, `col3.jpg`), plus a 4x zoom of the 200 group (`review/work/umlaut.jpg`). Read sign by sign:
   - column 1 (next to the divider): `400. 200. 40. 90. 3. 8. 100.` – matches;
   - column 2: `4. 9. 80.` gap `4. 5. 9. 40.` – matches;
   - column 3: `9. 50. 8. 1. 40. 40.` – matches (the 1 is a continental 1 with a lead-in stroke; no other reading fits the shape).
   Every number is clearly written; dots separate letters and a wide gap separates "dir" from "dein". Column order right to left and reading top to bottom is the only order that gives German.
4. **Language and context.** "[Fröhliche Ostern] wünscht dir dein Johann" is idiomatic German, and the printed "Fröhliche Ostern!" on the picture side (`review/work/pic_small.jpg`) completes it exactly. Austrian 5-Heller Franz Joseph stamp and SCHNEEGATTERN postmark fit an Upper-Austrian card of c. 1912 to a Fräulein Fanni Rauchenschwandner. A cipher of this kind (Greek/Hebrew-numeral place value) is a well-known schoolbook system; nothing is forced.
5. **Stamp box and picture side.** Zoom of the stamp corner (`review/work/stamp.jpg`): the stamp is still on the card and only the postmark and printed stamp design are visible; no writing shows at its edges. Picture side: printed title, R&K 4630/4 imprint and the collection stamp only; no handwriting, nothing along the edges. (Relevant given the steganography found under stamps on other series; here it cannot be checked from the scan, and the solver disclosed this.)
6. **Sources/honesty.** Portal status Not solved, no attached solution; the solver states none was found. Not in skip.txt or register-exclusions.json.

## Findings

1. **minor – the umlaut is written, the solution says it is not.** SOLUTION.md (Uncertainties) says "ü in 'wünscht' is written as plain u (200)". The enlarged crop (`review/work/umlaut.jpg`) shows a clear two-stroke diaeresis written above the 200 group, i.e. the writer encoded ü as 200 with umlaut dots. The plaintext should read `wünscht`, and the note should say the umlaut is marked by dots over the number. decode.py likewise drops it (prints `wunscht`); either add the mark to the transcription or say in SOLUTION.md that the script ignores it. Does not change the reading.
2. **minor – transcription in SOLUTION.md omits that mark.** The transcription line for column 1 should show it, e.g. `400.200̈.40.90.3.8.100.`, so a reader can see the umlaut is in the source.
3. **minor – "Iohann".** Rendering the decoded name as `iohann` is correct for the i/j merged key; the solver already explains J = 9. No change needed beyond keeping the explanation in the report.

## What I could not verify

- Anything under the postage stamp (stamp attached; scan only).
- The postmark date (illegible on the scan); the 1912-03 date rests on the portal file name.
- The exact spelling of the place name "Geretsek" in the plain address; it is unenciphered and does not affect the solution.

Register type MASC is appropriate (a monoalphabetic number substitution; no hidden text found). Card complete: every sign read, no restorations.
