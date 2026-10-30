# Triage —2026-10-26
Fresh Not solved, three tabs read, both originals saved. Faint Pigpen-like
symbols on picture side; transcript not reliable. No plaintext or specific
alphabet claimed. Deferred under user's easy-target preference; originals
preserved for clearer-source/image work. No DONE1/FINAL/register entry.
No watcher launched. Next1492 needs fresh inspection.

# 2026-10-30 — Claude Opus 5.5 (solver): serious attempt, stops at PARTIAL
Earlier work (2026-10-26, OpenAI GPT solver) was triage only: metadata and
both scans captured, no transcription. Nothing from it is contradicted here.

Source hashes (SHA-256): source/picture-large.jpg
240b763740dfbf7725e3f848c10c9d9cf45a31f539471cdd7c61c2a43d78297b;
source/address-large.jpg
74e99d6463e6acccb956772d7d2a69c19e5539a92adaefe9a8f75173c914300a.
Downloaded the original-resolution picture scan (work/hires/pic-original.jpg,
1785x1175; see SOURCES.md). Enhancement scripts: work/crop.py (autocontrast +
enlarge), work/norm.py (divide by local max-filter background, which lightens
the grey watermark band so pencil inside it shows); outputs in work/enhanced/.
Run them with the codex runtime python3 -I <script> <img> <out> x0 y0 x1 y1 scale.

What the card shows
- Ciphertext is pencil, on the PICTURE side, written across the whole card
  over the printed illustration ("Gruss aus Kiautschau"). Orientation: as the
  picture stands (not rotated). Evidence: commas/full stops sit low at the
  right end of lines 1, 3, 5; two dots ABOVE a V-shaped sign (line 2, x~800)
  and dots above other signs; ragged right margin. Read left to right, word
  gaps are visible.
- About 9-10 lines, baselines at original-scan y ~350, 435, 520, 605, 685,
  765, 850, 930, 1010 (+ faint traces near y 1080).
- Only the right part of each line (x ~830/1000 to 1720) is readable. Faint
  pencil marks also appear at the far LEFT margin (x 40-120, work/enhanced/
  left-normalized.png), so the lines start at the left edge and run under
  the sailor, boat, women and umbrella, where the dense print hides the
  pencil completely. Estimated 40-50 % of the ciphertext is invisible.
- The portal's watermark (cipher wheel) adds opaque printed letters E F G H I
  J K L M N O P and an inner ring of symbols (F, ©, /, ǂ ...) plus a logo
  caption "ɢ⊕ϴπF♀"-like string under the temple logo. Comparison with the
  address side (work/enhanced/address-watermark-compare.png) shows the logo
  caption is watermark, NOT cipher; earlier eyeballing could mistake it for
  ciphertext. Each opaque wheel letter also hides 1-2 pencil signs per line.
- Sign inventory seen (provisional names): diamond ◇, +, Λ (wedge), V, o,
  c / ʟ (c with foot), ɔ, κ/ʞ (k-like), ɑ (o with tail), ⊥⊥ / ш with base
  bar, Ш (three stems on a bar), S/2, μ-like hooked stroke, ı, ⌐/T, ◊ with
  dot. This is a symbol MASC-type script, not Pigpen (standard or dot-count
  variants from hcp-1131/1189/1190/1476 do not fit: no grids/dots system,
  round letters present), and not a script of any finished family in the
  repo (Tichá/Pepouš, Caesar-1 English, Jolanka) as far as I could compare.
- Structure noted: line 1 ends "+ ◇ ʟoκɑ ," and line 4 ends "Λ + ◇ ʟoκɑ"
  (same 3-word tail twice); lines 2 and 3 end in 3-sign words sharing the
  last two signs ("Sɔμ", "ıɔμ"). Too little visible text to fix a key;
  language unknown (address in German; recipient Wojnović jun., Indjija,
  Syrmia, Slavonia, so Serbian/Croatian or German plausible). I tried
  nothing beyond pattern notes because any key fitted to ~half the text
  with the line starts missing would be guesswork.

Why it stops
- A complete reading is physically impossible from the available scans:
  roughly half of every line is under the opaque illustration, plus signs
  under the portal watermark letters. Better material (an unwatermarked,
  high-resolution or raking-light/infrared photo of the original card)
  would be needed. No DONE marker, no SOLUTION.md, no register entry.
