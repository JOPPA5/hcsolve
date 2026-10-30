# In progress —2026-10-26
Fresh Not solved, all tabs inspected, originals preserved.
Own printed-letter transcription150 positions over7 source lines. Fourth
line includes an actual2-shaped symbol; initial Z normalization was undone.
Reading of O/0, B/8 and some overwritten letters remains provisional.
Cursive Jack excluded; printed LET after it included in final line. Corner
triangles observed, not assumed to be a key. No plaintext claim.
Script tests bounded rail fence2..25 rails/all offsets/both rail directions,
grid row/column/snakes/spiral routes for divisors of150 with flips, and
coprime modular skips/offsets. English word/trigram heuristic is deliberately
simple and not a probability model. Top candidates are not coherent reading.
No broad impossibility conclusion: transcription may be inaccurate, method
may be substitution or composite, and search does not cover all ciphers.
Letter IC about0.054 on provisional normalized transcription, not diagnostic.
Other available repo quadgrams inspected are Slovak, not used to label target
English candidates as failures. No target plaintext or external corpus used.
Rerunnable try_routes.py and route-results.json retain attempts.
No DONE1/FINAL/register entry; no watcher launched.
Next1488 needs fresh inspection.

# 2026-10-30 — Claude Opus 5.5 (solver)
- Re-read every line from 5x rotated crops of source/address-large.jpg. The two leading "I" of the
  GPT transcription are the sideways L and H of the HULL postmark; dropped. Line 4: O (not Q) at
  sign 4, overwritten R (not Q) at sign 13. New file work/transcription-v2.json (144 signs).
- Monoalphabetic hill-climb with English quadgrams (built from a local Gutenberg sample, outside the
  repo, scratch only): no English. Ruled out substitution.
- Noticed plain English fragments (THUS, BEST, AND, WI..SH..ES). Hypothesis: null cipher, plaintext
  letters in order with inserted nulls. Found WITH LOVE AND BEST WISHES FOR YOUR BIRTHDAY as an
  ordered subsequence in 73 signs (0/2000 random reorderings), FROM YOUR in 23 signs (0/2000),
  DEAR at the start, NAN after it (weak alone, contextual: Miss A. Stainforth).
- Tail OSPIOUTWTOFE WRIORBBKIR + LET.: word search (top-3000 English words) found nothing coherent;
  treated as nulls/decoys. Signature cursive "Jick" (maybe Dick).
- Result: "Dear Nan, with love and best wishes for your birthday, from your Jick."
  Key work/key.json, command `python3 -I ciphers/hcp-1489/work/decode.py`. DONE1 created.

# 2026-10-30 — Claude Opus 5.5 (solver), after REVIEWED1 (REVISE)
- Review finding 1: DEAREST (line 1, 15 signs) is a real alternative to DEAR NAN. Added DEAREST to the
  decode.py chance test (0/2000) and wrote work/salutation_test.py (DEAR fixed, 9 signs after it,
  20000 trials: EST in order 1.0 %, NAN adjacent 0.04 %). Keep NAN (own visible group, addressee);
  DEAREST disclosed in SOLUTION.md as the alternative.
- The GPT transcription also had a leading I in line 3 (underline of the printed "Carte Postale"); dropped
  like those in lines 1-2.
- Signature: portal/GPT "Jack" rejected for "Jick" (dotted i); recorded. Tail after FROM YOUR is 22
  letters (not 25); closing words declared not established.
