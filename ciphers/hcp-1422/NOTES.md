# HCP 1422 notes

2026-10-26: Read README full. Root supplied fresh rendered General/Description/Attachments inspection and immutable scans. Inspected both. Address has 18 lines of custom substitution and a small final signature; picture has no further cipher observed. Reread multiple cropped/enlarged views against address original.

Repeated > O backslash gives YOU; // O backslash cup-plus gives COULD, while zigzag O backslash cup-plus gives WOULD. This distinction resolved initial mistaken guess that the double slash was W. Two-dot A, one-dot G, dot-above-stroke H and dot-below-stroke I are critical. Added consistent observed 22-class key and manually frozen transcript, without inventing unused letters.

Reading broadly concerns a cold, travel to Mt. Carmel, meeting someone, the depot and a Saturday meeting. CYNTHIANA and signature IVY are literal glyph sequences. Postal cancellation obscures two upper spans. Context suggests SATURDAY and HER, but literal transcript leaves them unresolved. Placeholder counts 8/3 are hypothesis lengths, not independent visible counts. Literal irregularities HAV and CANADISH retained. Last place/name SKELTON retained rather than normalized to SHELTON.

`python3 ciphers/hcp-1422/work/decode.py` passes source hashes and gives 363 known positions, 11 contextual placeholder slots, 22 glyph classes. It is a manual-transcript decoder, not image OCR. No full decipherment or DONE1 while upper spans remain unvalidated. No watcher/reviewer launched, per user override. No PDF/register/FINAL.

2026-10-29/30 (Claude Opus 5.5, solver): Re-examined all 18 lines on 4-8x crops of
source/address.jpg (scratch crops, not kept). Findings:
- Line 3 span under "FEB 8": pen v (over F), two dots (inside E), long cross (over
  B), comma stroke right of the "8", then + : > visible -> SAT[U]RDAY, only the U
  hidden by the stamped 8.
- Line 4 span under the postmark time line: vertical stroke, slanted hash (E),
  4-shaped comma (R), as in clear HER on line 9 -> [H]ER; H/I dot not separable.
  Dark oval at line end = full stop.
- Line 9: earlier transcript had HER {comma} CYNTHIANA; the scan shows
  "! -." (stroke with dot below, dash + comma-like dot) under its own overline ->
  HER IN CYNTHIANA. Earlier model missed IN.
- Line 6: comma after ABLE. SKELTON second glyph is the hooked K (as in KID,
  LIKE), third is pi-shaped E. CANADISH and HAV confirmed literal.
- Postmark year unreadable at this resolution.
New files: work/transcript_v2.txt, work/decode_v2.py (old ones kept for history).
`python3 -I ciphers/hcp-1422/work/decode_v2.py` -> 374 read, 2 restored. DONE1.
