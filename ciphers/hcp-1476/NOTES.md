# Solver log —2026-10-26
1477 Swedish-context symbolic margin deferred, originals saved.
1476 short Pigpen closing. Address scan rotated90degrees clockwise to read
ordinary prose and symbols. Initial quick reading confused strokes because
cursive overlaps and narrow/slanted corners; enlarged crop resolved them.
Standard interleaved Pigpen yields MYOWN / DARLING / SWEETHEART,22letters.
Key fixed by all22symbols, not a word-by-word changing substitution.

An extra terminal nonstandard mark follows finalT. Looks like two curved
upright strokes joined by horizontal bar. It is not a standard glyph in this
key. Function uncertain: flourish, personal sign or additional encoded unit
not determined. It is preserved as END_MARK with its own enlarged image,
not omitted and not called a kiss, name, zodiac symbol, or deciphered letter.
Thus all22standard Pigpen letters have a coherent reading, but entire ink
message is not unconditionally complete. No DONE1/FINAL/register entry until
scope of terminal mark is resolved or independently reviewed.

## Offline second visual pass2026-10-26
Reexamined original upright scan and terminal enlarged mark. It has two
curved uprights crossed by a continuous horizontal bar; compared with all
standard grid and wedge forms in the supplied Pigpen key, it remains outside
the key. A resemblance to an ordinary decorative/personal mark does not
prove it is decoration. No further encoded letter was established. Decoder
sourcehashes and22letter roundtrip still pass. Retain partial status and
END_MARK rather than silently remove it. No marker created.

## Dedicated helper 9 — terminal audit, 2026-10-26

Fresh full-source/upright and close-up inspection confirms the terminal mark is
separate from the final dotted wedge T. The context crop now has reproducible
coordinates: original rotated 90 degrees clockwise, then box (450,425,550,495)
in the 674x1024 upright image, enlarged tenfold for display. The two curved
uprights and horizontal bar remain visible; a dark central deposit is also
visible on the bar. It may be a dot or simply thickening/intersection ink;
its intentional status is not established. It was omitted from the earlier
verbal shape description and is explicitly retained here.

No matching glyph occurs elsewhere among the 22 decoded positions, and no
assignment follows from the existing grid/wedge key. Resemblance to an ordinary
letter or decorative symbol would not establish its function. No historical
variant or new reading is claimed, and no web source was used for such a claim.
work/terminal-audit.py runs the existing source-hash/roundtrip checks and prints
every decoded position with its line and frozen token. --crop optionally
reproduces the source-derived context image using Pillow. This inventories
manual observations; it neither recognizes pixels nor validates an undecided
symbol. All 22 letters remain unchanged; terminal mark unresolved, no DONE1.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
End mark is a -(.)- flourish, no grid outline -> decorative stop, not a
letter. Complete. Register re-checked (357, 1476 absent). Watcher + DONE1.

## 2026-10-30 — Claude Opus 5.5 (solver), after review 1 (ACCEPT)
F1-F4 accepted: malformed W of OWN and uncertain T dot disclosed; end mark
now "probably printed ornament" (reviewer's ink-density evidence); comma
after MY added to transcription; decode.py/terminal-audit.py wording updated
and re-run (22 letters, hashes and roundtrips pass). Report, register entry,
FINAL.
