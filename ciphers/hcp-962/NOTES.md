# HCP 962 solver notes

## 2026-10-28 — source inspection and solution

- Read the full repository README. This is solver collaboration, not independent review. User override forbids watchers and reviewer launches; none was started. Root owns any DONE marker after checking the candidate.
- Root supplied fresh browser capture of General, Description, Attachments and a bounded AI-register check. Source files were read only. Both scans were visually inspected; all cipher writing is on the picture side. No new individual published solution was used.
- Created enlarged working crops `top.png`, `bottom.png`, `detail.png`, `b1.png`, `b2.png`, `b3.png`, `row3.png`, and `row4.png`. `coord.png`, `r5-coord.png`, `r6-coord.png`, and `coords-first.png` are location aids with red grid lines, never source replacements.
- Initial attempts to apply a one-letter-per-cell German Pigpen table did not fit. A monoalphabetic reading of recurring groups instead revealed the regular paired alphabet AB / CD / EF / GH / IK / LM / NO / PQ / RS, followed by angled signs. J is absent. This yields connected German across all six rows with one source anomaly.
- Shared only the established shape key with the HCP 949 collaborator to test a related family; no HCP 949 files were changed.
- The anomalous third-row word begins with a clear dotted bracket open left (`tbr.` = H), not the open-right dotted bracket M. The two M controls in preceding KOMME visibly differ. Root also inspected `row3.png` and agreed. Literal **HORGEN**, likely intended **MORGEN**, retained.
- Explicit three-dot U in ZURÜCK is represented as the regular dotted U plus two umlaut dots. No extra dot is supplied to other words, e.g. GRUSS/KUSS remain SS spellings.
- Full manual inventory: row counts 11 + 13 + 11 + 13 + 39 + 30 = **117** alphabetic glyphs. No unread glyphs. Standard punctuation and the SONN= / TAG line split are separate.
- `python3 ciphers/hcp-962/work/decode.py --write-transcript` passed: all 117 decoded and re-encoded, all source hashes matched. `transcript.json` records row and glyph position; row boxes use the original 1024×678 picture coordinate system. This is a manual transcript, not OCR.
- No blind held-out test was performed: lower rows were visible during discovery. Full fixed-key reread and repeated-symbol consistency support the claim, but are not independent-provider review.
- Pending: root verification, then any marker handover authorized by root. No marker, report, or register entry written by this collaborator.
