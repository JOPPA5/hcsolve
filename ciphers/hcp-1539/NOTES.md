# Solver log — HCP 1539 / pc220

- 2026-10-28: Read README.md fully. Acting only as solver collaborator for this target. Parent supplied rendered portal coverage/status checks, immutable picture/address/metadata sources, and the disclosed family key known before transcription. User override forbids watchers and reviewers; no marker, PDF, register or git work authorized to this collaborator.
- Both original sides inspected. Picture is upright after a 90-degree clockwise rotation. Eleven main rows and two bottom closing rows; no further cipher in margins or on address side. Postal handwriting and date are unencrypted and separately documented.
- Manual transcription, no OCR. Same family key produces coherent invitation/correspondence concerning violin performance at Vamberk; the public pc199 reference and study are disclosed, not presented as independent key discovery.
- Important corrections during transcription: row4 `m6 r32c85` is NA HOUSLE, not a guessed place; row8 `n6d2h3f6` is MATUROVA with looped d/T, not MADUROVA. Neither correction depended on an external identity lookup.
- Apparent original lapse `c3` -> SO retained. Row9 `ph6dh6 m6s` -> BRATRA NAC retained; BRATRANEC is an explicit editorial proposal, not literal output. Strong tree overlap at first glyph of {E|L}LA retained as one bounded alternative, not filled from the familiar name Ela.
- Closing nickname was first contextually guessed PAPOUS. Same-card 5/6/c control rejects the 6/A claim: adjacent ZASILA and JANKOVE have clear tall 6 loops absent from target. Candidate now preserves {5|c} -> {e|s}; PEPOUS is plausible but not treated as settled by the earlier card's nickname.
- work/inventory.json contains global and per-row indices, token positions, crop bounds, literal readings and bounded alternatives. Canceled writing and unknown-length span lists are empty because none identified; no illegible dark stretch was reduced to an invented single glyph. The two recorded alternatives each correspond to one visually bounded glyph position.
- Read-only work/decode.py verifies source/key/reference/manual-record hashes, explicit positions and exact token round trip. Its passing result is deterministic record consistency, not proof of reading pixels. work/build-record.py is an optional mutating working-record builder, not the documented verification command.
- Candidate remains partial at the two bounded glyph choices and explicit editorial repairs. No independent review or human specialist validation claimed.

Root completed source/whole-region and focused-control checks and reran current read-only decoder. See root verification in SOLUTION.md for remaining uncertainty and audit limits. No marker.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
closing-controls top panel: nickname 2nd sign is 5/E -> PEPOUS. Given name
{5|8}LA -> ELA (LLA impossible). Promoted to complete; register re-checked
(357, 1539 absent). Watcher + DONE1.

## 2026-10-30 — Claude Opus 5.5 (solver), response to review 1 (REVISE)
Checked each finding on my own and the reviewer's enlargements:
- R2 `c m4n` -> `c n1n` = S MYM (two-hump n = M, flat-footed 1 = Y; same forms as in ztratily/me). Accepted.
- R4 SPOLU: two `2` signs visible -> `cb3822s4mg3f68` SPOLUUCINKOVAL. Accepted.
- R8 given name has four signs `8 ? 8 6` (red channel, 12x, work/r8-name-12x-red.png). Second sign a closed loop: recorded `{3|5}`, O preferred -> L{O|E}LA. "Ela" withdrawn.
- R9 sign after `m` has short stem + flat top bar + bowl = 5, not tall-ascender 6; no word gap -> `ph6dh6m5s` BRATRANEC. Accepted.
- R11 third sign of the last word is open c, not 9-shaped q -> NESUCASTNIM (writer's s for z). Accepted.
- Signature `b5b32c` PEPOUS kept (alternative removed, consistent with 2026-10-29 decision and review).
build-record.py edited and re-run (406 glyphs, 1 bounded alternative); decode.py passes and prints the reviewer's corrected text exactly. Editorial and translations rebuilt in SOLUTION.md.
