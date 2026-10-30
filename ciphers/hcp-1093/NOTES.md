# Solver notes — 2026-10-25

User requested another easy unresolved cipher. Selected English postcard
1093 from earlier rendered catalogue candidates, avoiding the crowded
German series. Fresh inspection of all three tabs: Not solved, Pigpen,
no attached solution/transcription. No local directory/markers beforehand;
not in skip list. Saved full viewer scans.

Initial 90-degree rotation left cipher upside down; 270 degrees makes it
upright. Applied interleaved Pigpen key from 1188/1187. Read DEAREST BETTY
WHAT ABOUT THIS FOR A PHOTO OF [B?]RUCE. The probable B of BRUCE has weak
dot visibility, so raw transcription leaves it unknown. Main body continues
SHALL GO TO BED EARLY TONIGHT. Initially inferred TOMORROW from a quick
view, corrected on enlarged glyph inspection to TONIGHT. Do not retain
the initial inference as a decoded reading.

Middle two words remain uncertain. Literal provisional shapes suggest
[?]A[?]LS [?]I[?]D OR SOME. Do not force THINK or invent a grammatical
bridge. Next line reads THING COLD A LITTLE, then BETTER WITH FONDEST
LOVE AND KISSES FROM YOURS EVER, followed by an unresolved short signature.
Source punctuation and word divisions are loose; normalized syntax is
not proof of the glyph readings. Particularly inspect dots and rotated
open outlines. Known output is provisional, not independently reviewed.

All source text has a corresponding provisional line, but unknown tokens
are retained and the middle is not a full coherent reading. Save as a
partial, no DONE/FINAL/register/PDF. No published target plaintext used.
Source hashes and token roundtrip check only internal consistency.
Watchers not launched, retaining prior user preference.

# 2026-10-30 — Claude Opus 5.5 (solver)

Re-collated all signs on 3-10x crops of work/upright.jpg.
- [?]RUCE: clear dot left of ⅃ -> B. BRUCE.
- Middle words: literal BL1 BR0 BR0 L1 V0 | V1 C0 TL1 BR0 B1 = FAALS TIRAD.
  ⅃ written for E three times in two adjacent words (mirror slip; E and A
  distinct everywhere else) -> FEELS TIRED. The R+⅃ pair nearly touches;
  single-box J reading rejected (top stroke stops short; no English).
- Row 8 2nd sign under ink blot -> restored E (BETTER), disclosed.
- Signature: ⅃(dot) ⊓ ⅃(dot) = BOB, underlined. First dot sits over the
  upside-down printed line; colour test shows pen ink, not print.
- Bottom row: 8 dotted < = XXXXXXXX (kisses), previously untranscribed.
Rewrote work/transcription.txt (with * and !X markup) and work/decode.py
(literal + emended output, assertion against SOLUTION.md). Handed over as DONE1.

# 2026-10-30 — Claude Opus 5.5 (solver), after REVIEWED1 (ACCEPT)
- Finding 1: re-cropped kiss row (work/kisses-row.png, 4x): 9 dotted <, not 8.
  Fixed transcription (152 signs) and decoder assertion; reran OK.
- Finding 2: "mirror slip" wording softened to a guess; literal FAALS TIRAD in report.
- Finding 3: no change. Wrote report, register entry, FINAL.
