# Notes hcp-1075

2026-11-03: captured by Claude Opus 5.5 (orchestrator).

2026-11-03 (Claude Opus 5.5, solver round 1):
- Address side has 8 rows of dots/dashes with commas as word separators; spaced-dot letters
  (. .. R, .. . C, . . O, .. .. Y) and a long dash L show American landline Morse, as on FINAL
  sister hcp-1453. International Morse fails on the first word.
- Read every mark from 3-5x crops of work/hires/*_adr.jpg (crops not kept). Transcript in
  work/transcript.json, decoder work/decode.py (hash checks). Result:
  RECD YOUR CARD THIS AM I WILL WRITE SOON MY ADDRESS IS 457 CARROLL ST AKRON OHIO.
- OHIO lies under the grey collector stamp: sampled darkness, all 10 dots are ink (~60-130 vs
  stamp ~157).
- Word-sense points: I (gap between I and O), WILL (middle-length dashes), second O of SOON
  (tight, I-like), Y of MY (wide first pair). Second D of ADDRESS is a caret insertion.
- Picture side, plain: "No 547 Carroll St akron ohio", "I have not forgot the code but do Not
  remember the Noo on the Bx card", corner "547 Carroll St", initials "J. N. S.". Morse 457 vs
  plain 547 disagree; reported, not resolved. "Bx" unexplained.
- Stamp box: printed Tuck trademark only, no stamp, nothing hidden. No published solution
  looked up beyond the portal (Not solved, no attachments besides scans).
- work/measure_marks.py is a rough mark detector (row windows approximate; misses light dots).
