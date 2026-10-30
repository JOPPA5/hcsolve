# Triage —2026-10-26
Same recipient and similar dense strokes/dots as1502. Morse-like appearance
is a hypothesis only: many apparent dots are short horizontal strokes and
large round marks may be separators. Need establish segmentation and code
before claiming a reading. Deferred for easy-target triage; no plaintext,
completion markers, or register entry. No watcher started.
Next known catalogue candidate1498, pc_hcp_179, subject to fresh verification.

# 2026-10-30 - Claude Opus 5.5 (solver): complete reading, Morse
- Measured the marks on the address side (R channel < 150 to suppress the red print and the red rule; see work/components.py and track.py; 33 lines).
  Four mark types: short dash, long dash, small dot, large blob. The dash widths are bimodal (about 6-11 and 16-25 px).
- Hypothesis "short = Morse dot, long = Morse dash, small dot = letter gap, blob = word gap" gives at once
  L1 `YOU CAN`, L9 `DEAR NELL`. Confirmed on all 33 lines. The automatic classification (classify.py) has errors
  (intermediate widths, marks merged with the red rule or the postmark, the red "Printed in Saxony" print), so every line was
  checked by eye on annotated 5x strips (annot.py) and 6-8x zooms (zoom.py). The manual transcription is in work/transcription.txt.
- Result: the letter (L9-33) "Dear Nell ... yours always dearest George". The P.S. (L1-8, above the date):
  "You can send me a line back if you like, it's a long week you know".
- Residual points: intermediate-length marks resolved by comparison within the line and by word context (listed in SOLUTION.md).
  Weakest: the L28 `E` of SWETHEART (16 px), and the L19 initial `E` (12 px; `T` possible). JEWIT is spelled with one T;
  "SWETHEART" and the omitted "I" before HOPE are the writer's.
- Sister card hcp-1502 (same recipient, same style) is probably the same Morse scheme. Not touched here.
- DONE1 created after writing everything. Watcher not started (disabled for this run by the orchestrator).

# 2026-10-30 - Claude Opus 5.5 (solver): review 1 addressed
- REVIEW1 verdict ACCEPT, five minor findings. Flags for L28/L19/L29 added as comment lines in work/transcription.txt, hash in decode.py updated,
  decode.py re-run: output unchanged. Edited text now "swe(e)th[e?]art" and "E. (or T.) Jewit". Report written (report/report.md, report.pdf),
  register entry written (type Morse code). FINAL created.
