# Notes

2026-10-26: read README in full. Inspected both originals; message orientation
270-degree rotation. Root supplied HCP1407 Caesar-1 only as hypothesis.
Independent target words Mfuufs/uijt/wfsz/ojdf/J/bn/joeppst/bmm/up-Ebz/gspn/Hjsm
support a consistent -1. Last three-source-letter group Ebz resembles numeric
E/6/2 but target context and cursive support DAY. Sent this to coordinator so
another postcard's similar field can be rechecked from its own scan.

Read HCP1407 work/transcription.json and work/reading.jpg read-only for cursive
comparison. No files in its directory changed. 1406's 49 frozen alphabetic
positions are kept distinct from provisional Efbs/npsojoh/initials/last-row
opening. Earlier mental candidate poorly for body3 was rejected against pen
strokes; actual letter trace joeppst supports INDOORS. No corpus searched.

Full decipherment blocked by closing shorthand and final-row abbreviation;
no DONE1, watcher/reviewer/FINAL/register/PDF. Decoder checks source hashes.

## 2026-10-29 (Claude Opus 5.5, solver) — complete reading

Rotation: source/address.jpg rotated 90 deg CCW (PIL rotate(90)) matches
work/reading.jpg (mean diff 0.49); the earlier note "270" refers to the other
rotation convention. Crops in work/crops/ (4-6x, autocontrast).

- Greeting is `Nz. Pxo. E. L. Cpz.` = MY OWN [E. L.] BOY, identical to the
  greeting of hcp-1386. The earlier "Efbs/DEAR" candidate was wrong: the group
  is `E.` + narrow L-stroke + `Cpz` (z crossed by printed grey "O" of the
  wheel overlay; ink visible in gr3c.png).
- `npsojoh` is clearly written (b1b.png): MORNING frozen.
- Closing: `Nz. N. & L. gspn.` / `Pxo. E. L. Hjsm.` – same formulas as
  hcp-1386 (compare its crops nz1.png, nl.png, band6.png). The "Fo" was Pxo
  with a small x across the P stem; the "E/No + 1" was `E. L.`.
- Abbreviations kept literal per family convention (hcp-1386/1397/1403).
- Address: Mr. Abbott, Stokelake Farm, Chudleigh, S. Devon (not Whiteway).
  Postmark WIMBORNE 10 PM, date illegible.
- New transcript work/transcript-v2.json, decoder work/decode_v2.py
  (64 enciphered letters, hash check, asserts expected text). Old
  transcription.json/decode.py kept as the GPT record.
- SOLUTION.md rewritten; DONE1 created.
