# Notes hcp-897

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

## 2026-11-03 — solver attempt (Claude Opus 5.5), result: PARTIAL, no marker

What the card is
- Address side (Kurrent, plain): "Fräulein Dora Jeß, Lütjenburg i/Ostholstein, Gasthof zum Landhaus" (reading of the address hand, not of a cipher). Postmark BERGEDORF 23.2.01. Stamp still on the card; nothing visible around or through it.
- Picture side ("Sande bei Bergedorf", Knackstedt & Näther): date "22.2.01." in plain Latin script, then four lines of text in an odd hand (three lines in the white box, one along the bottom margin). No other writing found in the picture or along the edges at the scan resolution.
- Web check: Klaus Schmeh's blog has related 1900–1901 German postcards, but no find for this card, Dora Jeß, Lütjenburg or Bergedorf. HistoCrypt paper (Schrödel 2019) lists no single card. No published solution found.

What the message looks like (crops in work/crops/, made from work/hires/ with PIL, 3–10x)
- Disconnected strokes: short minims with a lead-in (looks like "1" / "ʌ"), short minim with crossbar, tall cross, tall straight stroke, tall loop, oval, "∂", "#" (two tall strokes with one bar), a tall stroke with a triangular flag (like "þ"), an arch "∩", a backslash, a descender hook "ч", a minim with a right arm ("ʏ"), mid-height dots placed between signs, and "ä" (arch with two dots).
- Rough draft token transcription in work/tokens_draft.txt (sign classes listed in its header). Segmentation is NOT secure: it is often unclear whether two minims are one letter or two, and whether a dot belongs to the sign before or after.
- Frequencies of the draft: plain minim 61 of ~205 signs (30 %), dot 25, short cross 24, tall cross 20. A one-sign-per-letter MASC would put one German letter at ~30 %, which is impossible (e is ~17 %). So the signs are not letters one-to-one: most likely letters are built from several strokes (Kurrent-like letters written unjoined, where e/n/u/m/i are 2/2/2/3/1 minims), or the text is shorthand-like. Read at low magnification, the bottom line looks like Latin cursive "mit tront hartiy. 1/4 ..." (meaningless as German apart from "mit"), so a Latin-letter reading does not give plain text either.
- Repeated material that a later solver can use: word ending "o · ∂" (oval, dot, ∂) ends about 6 words; L1 words 1 and 3 share "O . 1 R 1"; the last word of line 1 ("1 4 Q 1 O T 1") and of line 3 ("1 4 Q 1 O T 1 4 .") look like the same word; "L B ..." starts several words; the bottom line has what look like plain digits "1/4" followed by abbreviations with dots.

Why it stops
- I could not establish the writing system or a key: no stable segmentation into letters, no MASC that fits the frequencies, and no plain Kurrent or Latin reading that makes German. Nothing is deciphered, so there is no SOLUTION.md and no marker. Not shorthand-confirmed either: Gabelsberger-type stenography is a possibility to check by someone who reads it.
- Next steps: compare with hcp-1181 (said to be related) once it has work; try a Kurrent-stroke model (group minims into Kurrent e/n/u/m/i and test German n-grams over all groupings); ask a Kurrent/Gabelsberger reader.
