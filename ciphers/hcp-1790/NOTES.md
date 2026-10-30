# Notes — 2026-10-26

Initial visual triage only. Dense multi-dot Pigpen-like symbols under large
watermark. Both scans captured, working rotation made. No stable complete
transcription or plaintext claimed. Deferred for a cleaner easy target.
No DONE/FINAL/register entry. No published plaintext consulted.

# Notes — 2026-10-30 (Claude Opus 5.5, solver) — PARTIAL, no marker

## What was established
- Higher-resolution scan obtained (see SOURCES.md): work/hires/pc_hcp_471_adr.JPG.
  The cipher is written upside down relative to the address; reading copy is
  work/hires/flip_color.png (rotate -90, deskew 3.5 deg, rotate 180).
  Line centres (y in flip_color.png): 1020 1080 1135 1190 1250 1305 1362 1416
  1470 1524 1568 1618 1665 1718 (14 lines; lines 12-14 start at x~60).
- Cipher: the dotted-outline Pigpen variant already solved in this repo
  (HCP 1131/1189/1190): nine cell outlines A-I, the number of dots (1/2/3)
  selects A-I, J-R, S-Z. No new key was needed; every glyph checked so far fits.
- Working plaintext (English), read glyph by glyph from 6-14x crops
  (work/crops/H??_*.png, K*.png); line breaks as on the card:

   1  L? TOMMY I WAITED            (first sign partly under the postmark; may be
                                    a salutation letter or initial, unresolved)
   2  FOR YOU TO COME DOWN
   3  YESTERDAY AND WHEN YOU
   4  DIDNT COME, I WAS SURELY
   5  LONESOME FOR YOU, DARL-
   6  ING. JOE M?RNEY AND ARTHUR   (2nd letter of the surname not settled)
   7  KENNEY WERE OVER IN
   8  THE EVENING. IT WILL
   9  INTEREST YOU TO KNOW
  10  THAT PRINCE OBER DIED
  11  SATURDAY ... BRIGHT'S D-     (middle of line 11 not yet transcribed;
                                    last sign at the card edge is crowded)
  12  ISEASE. I AM MAKING ANOTHER KIN-?  (end of line: a heavily inked cell,
                                    reading not settled)
  13  ?A ... (W)RITE ...           (not yet transcribed sign by sign)
  14  ...                          (not yet transcribed)

## Why it stops here
- Lines 11 (middle), 12 (end), 13 and 14 still need a sign-by-sign token
  transcription; several cells at the right edge of lines 11-12 are crowded
  or overinked, and the first sign of line 1 lies under the postmark.
- No token transcription file / decode script has been written yet, so the
  README step 4 "single command" does not exist. No SOLUTION.md, no DONE1.
- No published plaintext was found or used.

## Next steps
1. Write work/transcription.txt in outline+dot tokens (as hcp-1131) for all
   14 lines, using the crop tools work/hcwin.py / work/hc.py (args documented
   in the files).
2. Settle: line-1 first sign; M?RNEY; line 11 middle; end of line 12; lines 13-14.
3. Write work/decode.py (hash check of source/ + hires file, decode, roundtrip),
   SOLUTION.md, then DONE1.
