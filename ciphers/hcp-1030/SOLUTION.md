# HCP 1030 — German love postcard to August Dederding, Neunkirchen, 26 March 1903 — PARTIAL

Status: **partial**. Not a complete decipherment; no DONE marker. Portal status at capture: Not solved, no transcription or solution attached. No published solution found or used. All work here by Claude Opus 5.5, 2026-11-03.

## Cipher type and key

Monoalphabetic substitution with digits; each digit is a different letter plain or with a comma-like mark, plus a stroke-above mark for W and Z. It is the key of the sister card hcp-1346 (FINAL; 1901, signed "August", to Neunkirchen), with the dot written here as a comma. `work/key.json`:

| digit | plain | with comma | with stroke above |
|---|---|---|---|
| 0 | M | A | |
| 1 | E | B | |
| 2 | F | C | W |
| 3 | G | D | |
| 4 | H | P | |
| 5 | I | (Z on 1346) | Z |
| 6 | K | R | |
| 7 | L | S | |
| 8 | N | T | |
| 9 | O | U/Ü | |

## Reproduce the partial reading (from the repo root)

```
python3 -I ciphers/hcp-1030/work/decode.py
```

Checks the four source hashes and decodes `work/transcription-partial.txt` (block B, lines 1-4 only).

## Partial plaintext (block B lines 1-4)

Mein über alles innig geliebter guter Herzensaug[ust]! Ich bin so glücklich, das(s) ich dir, mein Liebling, schreiben kann, das(s) alles gut gelangen [sic, for gelungen?] ist mir. Geht es den[n] um … nach … ? Wie geht es? Wir …

English: My beloved, dear darling August, loved above all! I am so happy that I can write to you, my darling, that everything has turned out well for me. … How are you? We …

Slovensky: Môj nadovšetko vrúcne milovaný, dobrý, najdrahší August! Som taká šťastná, že ti, môj miláčik, môžem písať, že sa mi všetko podarilo. … Ako sa máš? My …

## What is missing / uncertain

- Not transcribed: block B lines 5-8, the left column (about 20 lines, partly under the portal watermark), the vertical and curved lines round the column and flowers, the corner lines. This is most of the card.
- B4: the words after "um" and after "nach" are not read.
- 5' in "innig": Z-mark or i-dot.
- 9/4/7 look alike in this hand; several calls rest on the word.

See NOTES.md (2026-11-03) for details and the plan to continue.
