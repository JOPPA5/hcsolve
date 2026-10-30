# Solver log —2026-10-26
Fresh Not solved, all3tabs read; Morse tag confirmed by actual dot/dash text.
Standard International Morse directly reads SO GLAD YOU ARE, STUDYI and
MORSE on address side. There is an inserted --. (G) above right of STUDYI
with a curved insertion stroke, and ambiguous marks over ordinary Ramsay
signature/address. STUDYING is highly plausible but N not securely isolated;
only unambiguous excerpts are frozen in work/address-excerpts.txt.
Final separated address groups appear - .-. .--- ..-.; can also group first
two as -.-. (C) giving CJF. This segmentation/meaning is not settled; neither
TRJF nor CJF supplied as decoded signature. Need compare letter/word gaps.

Picture first line WAS THIS ONE and second-line prefix UP WITH THE FLEET
read under the same standard Morse key. Separate left/right enlarged crops
preserved. Terminal portion of line2 and all3rdline not frozen as transcript.
NE(W...) or place-name continuations tempting but do not force NEWCASTLE or
any other name from expected ship context. No historical fleet claim made.

Explicit partial, no DONE1/FINAL/register entry. Continued work should record
every remaining mark and assess spacing/possible writer errors before any
whole-message claim. Source hashes and excerpt code roundtrip are mapping
checks, not independent pixel proof. No watcher launched.

## Additional solver-subagent pass, 2026-10-26
Inspected both originals and all prior crops. Made new crops in work/ only.
The picture bottom-row first four separated groups read `-. . .-.. -.-.`
(NELC), with original-pixel mark centres recorded in agent-remaining-check.py.
This is a useful negative check against an unsupported NEWCASTLE completion:
the L group visibly has three dots and one dash, not W's one dot/two dashes.
Four additional literal positions are frozen, total 51 including the prior 47.
No semantic reading is asserted for NELC, and the rest of the row is unfrozen.
The address final run permits TRJF/CJF depending on the first grouping;
neither resolves a signature. The STUDYI correction still overlaps handwriting
and does not independently establish a clean N. No full-message candidate.
Both decoder commands passed source hashes. No sources/markers modified.

## Ten-helper pass 07 — 2026-10-26
Fresh visual examination of the original picture side, plus new native crops
and 3x/4x enlargements in work/ten-*.jpg. No additional securely segmented
letter was found. The picture bottom-row run after NELC contains six dot-like
marks, approximately x411,427,441,455,473,492 at y605, followed by a horizontal
mark around x535 and a question-like mark around x573. Thin crossing strokes
near x458 and x483 complicate interpretation: they may mark boundaries or
corrections, and are not automatically added as Morse dashes.

work/ten-boundary-check.py records these manual approximate locations and
reproduces 29 standard E/I/S/H segmentations of six dots without deletion.
The centre gaps 16,14,14,18,19 pixels do not independently pick a letter cut.
HI (and hence a contextual HIT with the later dash) is one possibility, not
a new reading. This bounded enumeration only demonstrates underdetermination;
it does not cover deletion/overwriting models or establish the writer's intent.
The existing 51 frozen letters are unchanged. Address-side correction and
terminal initials also remain unresolved. No marker, report, register entry,
source modification or watcher. Decoder commands and source hashes pass.

## Claude Opus 5.5 solver pass — 2026-10-30
Credit: all earlier passes above were by the OpenAI GPT solver (GPT-6 Astra /
GPT-6.1 Sol). This pass re-read every mark from fresh 4-10x crops of both
source scans (scratch crops, plus red-channel contrast stretch and an ASCII
intensity map of the picture line-2 tail). Full literal transcription of ALL
Morse on the card: work/claude-literal-transcript.txt; decoder (checks source
hashes): `python3 ciphers/hcp-1468/work/claude-literal-decode.py`.

Address side (confirmed): SO GLAD / YOU ARE / STUDYI? / MORSE / -.-. .--- ..-.
- After STUDYI ".." the next sign sits on the red divider under a dark smudge
  touching the handwritten "Miss"; it is not readable from the pixels. A --.
  (G) is inserted above with a curved caret stroke ending at that point. The
  intended word is surely STUDYING, but N would be a restoration of an
  obscured sign (acceptable only if disclosed).
- Final row: dash-dot-dash-dot with uniform internal gaps (~12-15 px at the
  1024 scan) -> C; large gap; .--- (J); gap ~29 px; ..-. (F). Literally C J F,
  probably sender's initials; T R J F remains a weaker grouping.
- Marks right of the stamp are the duplex postmark, not Morse.

Picture side - corrections to the earlier frozen excerpt:
- Line 1: after T only THREE dots (x~612,629,648; confirmed on red-channel
  contrast crop), then two, then three: literally T S I S. "WAS THIS ONE" is
  the obvious intent but needs a writer error (dropped dot), not a reading.
- Line 2: F L, then one dot (x912), a dash (x928-948, pale start), a dark thin
  slash (x947-957, same dark pen as the ? on line 3), a dash (x960-975) and a
  dot slightly below the line (x969,y580). Literally F L E T | T E (or N).
  The earlier "FLEET (..-. .-.. . . -)" had two E dots; only one is visible.
- Line 3: -. . .-.. -.-. (N E L C, letter gaps 40-80 px vs 12-15 inside
  letters), then four dots | one dot | one dot (two dark thin slashes between
  them), a dash, and a written question mark with dot. Literally
  NELC H E E T ?  (or with the slashes ignored, 6 dots: HI/SS/... + T).

Semantics: UP WITH THE FLE(E)T is secure in intent; the continuation
"NELC HEET?" (plus the "T E/N" after the slash on line 2) gives no English
under standard Morse. Dictionary brute force (work-free scratch, all splits of
the observed groups) yields only nonsense (NEED CHEET, TEEL CHIT, ...). Tried
and rejected: NEWCASTLE (L is .-.., not W .--), NELSON (C is not S), LEITH,
NEAR, LOCH (LCH would need an omitted O), place names near Elgin. The writer
demonstrably drops dots (THIS, FLEET), so the intended text could be a word
with lost signs, but choosing one would be forcing words onto marks.

Status: still PARTIAL. ~55 of ~60 letters read; the end of the picture-side
question (line 2 tail + line 3) is unresolved. No DONE1, no register entry.
