# Notes hcp-1346

2026-10-30: captured by Claude Opus 5.5 (orchestrator).

2026-10-30 (Claude Opus 5.5, solver):
- Pencil digits on picture side; address side clear (M. Scheck, Neunkirchen; St. Johann 16.4.01). Saar region, so German expected. No sister card has this key; checked numeric FINAL cards (hcp-1509 etc.).
- Dead end: 10 single digits as letters fails: triple 888 and 111, and too few signs. T9-style 3-letter groups and "1x" two-digit tokens also did not work.
- Break: dots are not random; 2 is followed by a dot 17 of 23 times, 2.4 is frequent. 5 2. 4 = ich. Treating "digit + dot" as a separate sign gave 7.2.46.151.18 = schreiben, 7511.1 = Liebe, 69888.1 = konnte, 7.98880.3 = Sonntag, then 1581.16.7.8.0.83.18 = einverstanden.
- First-pass transcription (work/transcription-firstpass.txt) had many errors: flagged 1 read as 4/7/8, and word groupings in gestern, abend, schreiben, verbleibt, Stelle, alles. Re-read each on 5-8x crops. Earlier mistakes such as 8924 vs 892.4 are about dots. Note: first zoom coordinates missed in a few crops, redone.
- Top edge is written upside down and carries verlassender August after "nie"; left margin rotated: Das Schreiben ging in Eile.
- Weakest point: `nie` (pixels look like 8 3 7). See SOLUTION.md uncertainties.
- Final: work/transcription.txt, work/key.json, work/decode.py. 290 signs, 30 marked ~.

2026-10-30 (Claude Opus 5.5, solver, after review 1, verdict REVISE):
- M17 now records the two dotted 3s of `ging` as an emendation (`3.=3~`); decode.py prints the literal `dind` beside the read `ging`. Text unchanged.
- Added ~ to 8. (Teil, R02), 2. (nach, R13), 6. (gestern, R12), 1. (verbleibt, R15). Now 290 signs, 36 ~, 2 emended.
- Correction of the earlier note: "2 followed by a dot 17 of 23" is a first-pass count only. Final transcription: 2. 15 times (always before 4), plain 2 three times (always F).
