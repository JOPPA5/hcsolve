# HCP1548 solver collaborator log — 2026-10-28

- Read README.md fully. Role: solver collaborator. Root supplies rendered three-tab portal/status/register inspection and immutable source acquisition. User override forbids watchers/reviewers; this collaborator creates no marker, PDF, register entry or git action.
- Prior knowledge: public partial Anna Tichá study and family key already known before target transcription; photographic pc199/F reference available, although this target needs no F. No target plaintext supplied. Known-key transfer, not blind recovery or independent discovery.
- Viewed both originals including all margins. Upright picture is a lossless ROTATE_270 of source/picture.jpg. Nine handwritten cipher rows at bottom; address in ordinary Czech to Anna Tichá in Žirovnice u Počátek. Ordinary date 6.VII.1903.
- Manually read all nine rows, saved individual row crops, indexed picture, tokens and glyph positions. Printing under green stem reduces contrast. R01 DRAHE, R03 SLAVNOSTI and R04 NAVSTEVY were read from distinguishable ink. R02 keeps U1 as an unknown-length span after N and before STALE; No grammatical completion of U1 is supplied in the deliverable.
- A preliminary R02 shape label g produced JIK. Comparing looped g/K in R01 DIK and R07 KOMISARE against unlooped q/Z in R01 ZA, R02 JIZ and R08 Z corrected the label to q and the output to JIZ. The actual contrast crops are work/q-g-controls.png; this is a documented image-based correction, not a retained ambiguous K/Z alias.
- R08 terminal glyphs after VRELY and DLOUHY are unmarked r/H in this scan; R09 is manually read as a separately capped r/CH; these H/CH readings have not been independently confirmed. Saved work/h-ch-initial-controls.png. Literal output retains VRELYH, DLOUHYH; editorial Czech/Slovak may supply CH with explicit labels.
- Underlined final tall-loop glyph after TVUJ is tentatively b-class/P, followed by dot then ordinary date 6.VII.1903. Sender remains unknown; no name expansion.
- Read-only decode.py checks original batch hashes, 5 record hashes, external reference hashes, all 9 rows, exact indexed known positions and saved literal/ciphertext equality. Whole-row fixed-key inverse (CH before singleton letters) reproduces ciphertext. Current result: 294 mapped units -> 295 base letters (including the tentative final b/P assignment) and U1 of unknown length; exact total length/coverage unknown. Command passed.
- This is substantial partial plaintext, not an exact full solution. No external review claimed. Root should inspect every row/control before any further decision.

- Final self-consistency pass: reread current README; matched the nine SOLUTION literal rows byte-for-byte to work/literal.txt and checked token/table/decoder counts. Removed the former contextual completion of U1 from editorial Czech, Slovak and record notes. Explicitly labelled final b/P tentative and H/CH as solver image readings without independent confirmation. Decoder remains read-only and preserves the original literal output. Root performs image QA; no further file changes after handoff.

## Root source QA and register refresh - 2026-10-28

Root inspected both original sides, all nine rows and complete margins, the stem intersection, q/g controls, H/CH controls and the terminal initial/date. DRAHE, SLAVNOSTI and NAVSTEVY retain discernible individual strokes at the stem; this does not justify filling U1. JIZ follows the q/Z class, contrasted with looped g/K. R08 VRELYH and DLOUHYH retain unmarked r/H; the separate R09 cap supports the tentative CH reading. The final looped b-class/P remains a qualified shape assignment, not a sender identification. The result remains partial with one unknown-length span.

Fresh rendered register check now has 193 contributions and 159 distinct HC Portal source IDs; this target is still absent. Ten new pc420–429 registrations are excluded in skip.txt. The current snapshot is batches/easy-2026-10-28/register-snapshot-193.json. This supersedes only the earlier register count, not source metadata or a global novelty claim. Root/helper checks are solver collaboration, not independent provider review. Hashes and inverse checks test record consistency, not automatic handwriting accuracy. No watcher or reviewer was launched.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
U1: visible 2/U inside the stem before cd685, one-sign gap after m ->
NEUSTALE (work/claude/neustale.png). Promoted to complete; register
re-checked (357, 1548 absent). Watcher + DONE1.

## 2026-10-29 — Claude Opus 5.5 (solver), response to review 1 (REVISE)
Supersedes the "partial / U1 unknown length" lines above. The records now encode
R02 as m52cd685, with positions 18-19 flagged "restored" in transcription.json.
build-record.py was re-run, and decode.py now asserts 296 units and the two
restored units, and prints NEUSTALE. SOLUTION.md was rewritten as one current
statement, with P[epouš?] marked as a family inference and the E described as
partly visible (from the reviewer's red-channel crop). The reading did not change.
I wrote the report and register entry, then created FINAL.
