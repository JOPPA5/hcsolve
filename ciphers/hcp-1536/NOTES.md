# HCP 1536 — solver collaboration log

2026-10-28. Read README in full. Assigned this target only. Explicit session override: no watcher, reviewer, marker, PDF, register entry, or git operation. Source acquisition and rendered portal checks were performed by the root solver and recorded in SOURCES.md. Originals were not edited.

The key was supplied before target transcription from the related Anna Tichá cards (hcp-1520/1527). The public partial study and photographic pc199 reference were already known. This is transfer of a known family key, not independent discovery of the key or a claim of worldwide novelty. No target plaintext was provided to this helper. Collaboration is solver work, not independent review.

Inspected the entire picture and address images, including all margins. Picture rotated clockwise 90 degrees has nine main rows B01–B09. A separate 180-degree orientation makes the two margin rows M01–M02 upright. Date is unencrypted. Address side has no cipher body; the recipient/address and printed/postal matter are recorded in SOLUTION.md.

Manual transcription: digits and lowercase Latin shape labels follow the transferred key. `H` names one handwritten sign resembling r with a caron and maps to CH. `y` names the 7-shaped J sign. This is not OCR. `transcription.json` preserves every indexed sign, punctuation/space token, and an unknown-length span. `panel-*.png` combines each row with its position legend. The row rectangles are navigation crops, not automatic character bounding boxes; overlaps preserve ascenders/descenders.

First pass incorrectly labelled the sign inside B03's last word as y/J. Compared the source shape with B04 q5/ZE and B07 y4q/JIZ: the loop and hooked descending tail agree with q/Z, whereas y/J is the angular 7-shaped sign. Corrected to `3t83q4d4`, ODLOZITI; see `q-vs-y-same-card.png`. Both transcript hashes were regenerated. No correction was made from grammar alone.

B01: after clear `n3` (MO), ink on the dark cherry cannot be segmented confidently. It is U01, an unknown-length span. MOJE is a plausible contextual completion, excluded from all claimed plaintext and counts. The following q6/ZA is legible. Brightened/channel views did not warrant forcing the gap to one or two glyphs.

Preserved unusual literal forms ODSILAM, ODOJETI, and KOMISSI. Editorial diacritics are kept separate; they are not encoded by the simple base-letter key. The small VACLAVA/ST.VACLAV passage and route names fit Czech but are coherence checks, not substitutes for source reading.

Validation: read-only `decode.py` verifies all source-file hashes, key and manual-record hashes, sequential token positions, exact transcript reconstruction, and exact tokenwise encryption/decryption roundtrip. A full image-to-text OCR check is not claimed. Current record: 390 assigned cipher signs, including 2 CH signs and 388 other signs, emitting 392 base letters, plus U01 of unknown length. Consequently no total coverage percentage is meaningful. No review or completion marker was created.

Root viewed both originals, full main/margin regions, U01 controls and ODLOZITI q/J comparison, checked final source/record hashes and390/392counts. No context-driven completion of U01. Editorial PSANKO discrepancy corrected before final state. No marker.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
U01 under the cherry: lower strokes of y/J (descender) and 5/E bowl visible,
then a comma -> MOJE (work/claude/moje.png). Promoted to complete; register
re-checked (357 records, 1536 absent). Watcher + DONE1.

## 2026-10-29 — Claude Opus 5.5 (solver), response to review 1
Status note: the statements above that "no marker / review / PDF" exists and that U01 is
excluded describe the state on 2026-10-28 only; they are superseded.
Fixes: (1) M01 first word is `3t5c486n` ODESILAM — the earlier `3tc486n` ODSILAM was a
misreading (a 5 touches the t; review/work/m01_head_x9.png), not an unusual spelling.
(2) U01 recorded as glyphs `y5,` (B01 pos 25-27, partly obscured, comma probable);
decode.py flags it as MO[J][E][,]. (3) R of PRAHY not visible -> U02 (M01 pos 26,
restored from context and PRAHA 7 postmark). (4) Postmarks PRAHA 7 and ŽIROVNICE 27 ? 03
added as evidence. Counts now 393 keyed signs / 395 letters. Reviewer's my_decode.py agrees.
