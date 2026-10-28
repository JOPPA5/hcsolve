# HCP 905 solver notes

## 2026-10-28 — source-based Pigpen pass

Read README in full. Root supplied both immutable originals after inspecting all three rendered portal tabs and the newer AI register; no individual plaintext or transcription supplied. Standing user override means no watcher or reviewer is launched. This collaborator works on HCP 905 only, and creates no marker, PDF, FINAL or register entry.

Viewed both full source images. All identified geometric cipher writing is on the picture side, fourteen rows surrounding the printed devil/caption; address side is ordinary writing and postal marks.

Disclosed transfer of omitted-J German Pigpen convention from the read-only HCP 995 candidate and related HCP 1016. Opening yielded JA VERD.... NICHT EINMAL DIR KANN ICH'S MEHR RECHT MACHEN without fitting a new substitution. Transcribed all remaining rows manually, with indices and approximate coordinates. No full plaintext or corpus template supplied. The lower section was checked after the upper text under the same key; this is sequential internal validation, not a blinded experiment.

Small crops were required because watermark diagonals can masquerade as glyph arms or interior dots. A black-ink threshold at grayscale <100 was used only as a reading aid alongside original-color crops. It is not an enhancement that recovers missing source detail.

Corrections from the full indexed self-audit:

- Initial provisional row2 KAND resolved to KANN: final glyph has its interior dot.
- Source IM at row4, not an inferred IC.
- Gray right-arm overlay in ABGEFASSTE had first looked like W; threshold displays leave a single dark upright T. Both preceding dotted corners have real small dark interior marks. Root also inspected those crops and agreed, a solver-team check only.
- Last compound identified shape by shape as FILIAL=POSTVERHÄBTNISSE. FILIAL's fourth narrow upper-left corner is I. POSTVERHÄBTNISSE has a genuinely undotted cup, so B is retained literally and intended L explained only editorially.
- Repeated HS occurs in AUHSERDEM, MUHS, SCHLUHS, KUHS. Do not normalize these in the mechanical output. The repeated HS in typical ß contexts may reflect a writer convention, but why is unknown.
- Provisional JENE and VOR in row12 were withdrawn: the small original-color crops and masks reveal no dark interior dot for those putative N and O. Final JEDE / VER, without remapping.
- One additional geometric field after HÜBSCHE is visibly canceled. Record it as position 114 with no underlying assignment, not as an active invented letter.

Inventory: 347 positions, 346 active with key assignments and 1 canceled field. Main artifacts: transcript.json, decode.py, indexed-01..14.png; detailed limits in SOLUTION.md. This paragraph records the original pre-DONE1 state; an existing independent Review1 later returned REVISE. Current correction status is below. Final collaborator handover remains to root for source QA, with no marker creation by this collaborator.

## Review 1 correction pass — 2026-10-28

- Read full README, existing REVIEWED1/REVIEW1, solution, notes, source guard and every writing script before executing it. Scope was only SOLUTION.md, NOTES.md and work/. No watcher, reviewer, Claude, marker, source, review, PDF, register or Git action.
- Inspected both original faces afresh. Fresh raw-NN controls at source boxes pos153 `[382,366,418,402]`, pos156 `[462,366,498,402]` show dot/N versus undotted/D. Thus only position156 changes: E.→E, word GEGENGENOMMENE→GEGENGEDOMMENE. This is an original-pixel correction; grammar does not create a dot. `make-transcript.py`, transcript.json, literal/mechanical saved texts and indexed08 were reconciled. Key unchanged, 24 classes all used.
- Position114 raw box `[612,273,650,323]`: two heavy vertical cancellation strokes, remaining top/right/bottom of ⊐/□ family, no visible dot. Left boundary and letter remain unresolved. N/E suggestions remain hypotheses; still one canceled field.
- Ordinary address72 and Berlin arrival Postamte59/22.12.99 verified from originals; raw-NN crops and source boxes saved in review1-crops.json. Bonn day remains unreadable. Official Bonn page independently supports present geographic Küdinghoven/Beuel/right-bank context, not 1899 administrative status. Six period ß words and modern editorial normalization explicitly distinguished; no new historical dictionary entry audit claimed. Sources/limits in review1-context.md and SOLUTION.
- First sentence explained as elliptical comparison/apposition, possibly omitted z.B.; no missing source line assumed or words added to literal. German editorial and English bracketed bridges remain separate.
- Corrected generation scripts were inspected before running. Decoder rewritten as read-only audit: own three entries in batch source guard; seven immutable inputs (source3 + DONE1 + REVIEWED1 + existing review + its read-only decoder); 59 canonical record hashes; indexed1–14 pixels regenerated in memory; five raw-NN crops; IDs/coordinates/exact row totals; saved literal and mechanical readings; full-stream complete-key inverse. Literal-to-mechanical normalization now catches stale diplomatic base letters. No pixel-recognition claim.
- Counts unchanged: row totals 17,20,20,21,24,23,23,25,22,28,29,27,32,36; 347 positions =346 active +1 canceled; 24/24 used key classes. Exactly one literal position changed. Audit passes; root QA remains required before any closure.

- Re-ran the existing reviewer's already-written read-only `review/work/my_decode.py --diff` after inspecting its code. It reports 347 positions and **no notation differences** against the corrected inventory. This reuses existing review evidence; no reviewer agent or new independent review was launched. Its script hash is now also pinned as an immutable input.

Root review-addressed closure pass: current REVIEW1 and original-pixel controls checked; every numbered finding addressed without key/meaning change. Read-only reproduction verified. Existing review verdict remains REVISE; reviewer explicitly allows closure after corrections. Preparing corrected report and local register entry, then FINAL as final cipher-directory write. No watcher, new reviewer, external submission, commit or push.
