# Portal 1825 / pc_hcp_506 — reading corrected after review 1

This is portal record **1825**, named **pc_hcp_506**, not portal record 506.
The independent reviewer returned REVISE and explicitly found that the
following transcription corrections need no further review round. The key
is unchanged; the complete reading contains **95 letter signs**.

## Literal decoded text

```text
I HOPE YOU ARE
A GOOD DEAL BETTER.
WHAT KIND OF
WEATHER ARE YOW
GETTING? VERY
WET HERE ANY
MORE MARRIAGES?
KIND LIVE MARY.
```

The unencrypted opening **Both puzzles correct** is source cleartext, not
claimed as deciphered. Source comma marks separating words are rendered
as spaces. The full stops after BETTER and MARY and the question marks
after GETTING and MARRIAGES are present in the handwriting.

## Normalized reading and Slovak translation

“I hope you are a good deal better. What kind of weather are you getting?
Very wet here. Any more marriages? Kind love, Mary.”

„Dúfam, že sa máš oveľa lepšie. Aké máte počasie? Tu je veľmi mokro.
Nejaké ďalšie sobáše? So srdečnou láskou, Mary.“

This normalizes exactly two literal anomalies: **YOW → YOU** and
**LIVE → LOVE**, one glyph each. In the literal original, YOW is the
spelling in the second YOU position and LIVE the closing word. Those
substitutions are the writer's apparent slips, not changes to the key.
The translation conveys their likely intended meaning. Mary is the
signature read from the cipher; her historical identity is unknown.
The cleartext opening means „Obe hádanky sú správne.“

## Key

Pigpen with alternating undotted/dotted letters, transferred unchanged
from the earlier HCP1188/HCP1187 work. The portal already labels the
cipher family. Short internal dashes serve as the writer's dots.

| Visible outline | Token | Undotted | Dotted |
|---|---|---|---|
| bottom/right | BR | A | B |
| bottom/left/right | B | C | D |
| bottom/left | BL | E | F |
| top/bottom/right | R | G | H |
| four sides | C | I | J |
| top/bottom/left | L | K | L |
| top/right | TR | M | N |
| top/left/right | T | O | P |
| top/left | TL | Q | R |
| downward V | V | S | T |
| right-pointing wedge | > | U | V |
| left-pointing wedge | < | W | X |
| upward wedge | ^ | Y | Z |

Transcription tokens append 0 for undotted and 1 for dotted. The complete
95-sign transcript uses 21 distinct signs; no sign requires two values.

## Reproduce

From repository root:

```sh
python3 -I ciphers/hcp-1825/work/decode.py
```

The command checks preserved source hashes and decodes the manual
outline/dot transcription in work/. The portal supplied no transcription.
It does not OCR the scan; exact token roundtrip checks internal
consistency, not independent pixel verification. The independent review
collated all signs against the scan and decoded them using a separate
implementation in review/work/review_decode.py. After the corrections,
the two complete 95-sign readings agree.

## Evidence and limits

One unchanged alphabet yields coherent English across all eight lines.
The signature's touching M and A have the same separate outlines as MA in
MARRIAGES. The second word YOU has a left-pointing final wedge, unlike
the right-pointing wedge in the first YOU. The closing V has an internal
dash-dot, while its I is a genuinely closed box; hence literal YOW and
LIVE remain in the decoder output. The likely YOU and LOVE are explicit
interpretations. A dot at the baseline between M and O in MORE is outside
the M outline and is treated as a pen touch, rather than an internal dot
that would give NORE. These are disclosed source features, not word-wise
key exceptions.

The source date is unreadable and the catalogue gives none. The address
reads Miss Stirling, Islay House Square, Bridgend, Islay; the catalogue
spelling is Stioling. The identities of Mary and Miss Stirling and whether
they regularly exchanged puzzles are unestablished. Both scans have a
large watermark. The 110-record register snapshot has no matching URL or
name; that does not prove historical priority. No published target
plaintext was used. PDF generation and final closure are separate steps.

## Response to review 1

1. **Signature (major): corrected CRY to MARY.** The first apparent
   closed-bottom outline is actually two touching signs, TR0 BR0. The
   top bar projects left of the first upright, as in the MA of MARRIAGES
   (review crops z8-mary.png and z7-ma.png). Updated transcript, literal
   text, translation, signature discussion and count from 94 to 95.
2. **Closing V (major transcription): corrected LIUE to LIVE.** The
   rightward wedge contains a clear dash-dot (z8-love.png), matching V
   in VERY. The closed box remains I. Intended LOVE therefore requires
   one source-sign correction, not two. Removed the obsolete argument.
3. **Second YOU (major transcription): corrected to literal YOW.** Its
   last wedge points left (z4-you.png), matching the W that opens WEATHER;
   the earlier YOU ends with a right wedge (z1-you.png). Normalized YOU
   is now explicitly separate from the literal output.
4. **Punctuation after GETTING (minor): retained source question mark.**
   The heavy hook and lower dash match the mark after MARRIAGES
   (z5-q.png). Replaced the earlier unresolved-overwriting account.
5. **Mark after M in MORE (minor): disclosed baseline pen touch.** It
   sits outside the TR outline and near O's foot, unlike internal
   mid-height dots (z7-more.png). M is retained; interpreting it as N
   would give NORE. The visual basis is primary; English is supporting.
6. **Record keeping and punctuation (minor): corrected the address to
   Islay House Square in SOURCES.md without editing immutable metadata.**
   Also restored the source full stop after BETTER; the closing stop and
   both question marks are literal. Word-separator commas are explicitly
   rendered as spaces; normalized sentence punctuation is distinguished.

All six findings are addressed. Corrections concern transcription and
source record keeping; the key and method have not changed. The reviewer
explicitly stated that these corrections do not require another round.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
