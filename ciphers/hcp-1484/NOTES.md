# Triage —2026-10-26
Fresh Not solved, three tabs read, both originals saved. Geometric cipher
appears to share symbol style with1485, including circle/square/triangle
forms and appended bars. Similar written address and nearby dates strengthen
a joint-analysis lead, not a proved common key or sender identity.
Would need accurate shared glyph inventory and substitution analysis.
No plaintext or key claimed. Deferred under easy-target preference.
No DONE1/FINAL/register entry; no watcher launched. Next1483 needs inspection.

# 2026-10-29 — full decipherment (Claude Opus 5.5)
- Text is written upside down: after rotating the card 180 deg the "?" and commas
  are normal. Read in that orientation (rotated line 1 = lowest line on scan).
- Provisional sign classes + quadgram hill-climb (scratch, corpus from man pages)
  gave "...THAN.YOUEVER...INTHEMORNING...TOHEAREVENBETTER...". Words then gave
  MY OWN LITTLE DARLING, THANK YOU EVER SO MUCH, FOR THE POSTCARD.
- Key insight: consonants = stem + 1-3 bars, by side (L/R/both) and anchor
  (top/bottom): L-top BCD, L-bottom FGH, R-top JKL, R-bottom MNP, both-top QRS,
  both-bottom TVW. Vowels: circle-dot A, triangle E, triangle+stroke I, square O,
  square+diagonal U, square+V Y. Superscript 2 = doubled letter.
  First draft had merged 2- and 3-bar variants (e.g. C/D, N/P, R/S) — that was
  the cause of the garbled hill-climb output; re-read every stem on 10-16x
  nearest-neighbour crops (work/nz, work/g) and counted bars.
- Faint lighter-ink sign before DARLING (line 8): pixel dump = stem with three
  left bars from top = D; read as abandoned start, printed [d].
- Result: work/transcription.txt, work/key.json, work/decode.py (177 signs).
  Draft first-pass transcription kept as work/transcription-draft1.txt (wrong
  sign classes; superseded).
- J, Q inferred from pattern; X, Z unattested. Sister cards 1483/1485 look like
  the same system — untested here.
