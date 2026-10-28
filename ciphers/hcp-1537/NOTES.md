# HCP 1537 solver notes

2026-10-28. Solver collaboration only. Read README.md fully. User override forbids watchers and reviewers; none started. Work confined to this cipher work/, NOTES.md and SOLUTION.md. Original source bytes remain untouched.

The root inspected rendered General, Description and Attachments and the AI register. Portal status Not solved, Czech postcard pc_hcp_218 dated 1903-09-17, private collection, Anna Tichá. No attached transcription/solution. See SOURCES.md for source URLs and disclosure.

Known family substitution key transferred from earlier Anna Tichá cards and a published partial-key reference. Shallow-v/F was also available from the published pc199 comparison before this transcription. No target plaintext was supplied. This is manual transcription using an existing key, not independent key discovery or an automated OCR solve.

Both original sides and all outer margins inspected. Picture must rotate clockwise 90° (PIL rotate(-90, expand=True)); 13 message rows and unencrypted date 17/IX1903. No additional cipher writing in the floral upper field or other margins. Address is plain Czech; transcribed in SOLUTION.md. Printed publisher/series lines are not encrypted message content.

Created overlapping enlarged per-row crops from immutable picture.jpg, ordered manual-records.json, exact glyph indices in indexed-transcription.tsv and transcription-index.md, and focused same-card controls in controls.md. The visible rows are legible; no black span needs an invented unknown placeholder.

Initial quick visual readings FAMILCE and BRZY were wrong. Enlargement establishes `f6np5hs5` = VAMBERCE and FIVE glyphs `phqg1` = BRZKY. PRI and PRISTIHO have angular 4/I, not 1/Y. These corrections come from same-card shape comparison; see controls.md. The decode assertion also caught a typed t/d label error in TVUJ; corrected by the shape before finalization. These are logged because a plausible Czech paraphrase is not proof of a glyph reading.

Validation: work/decode.py is read-only by default. It verifies SHA256 of all three source files, exactly 13 ordered manual rows, 289 indexed cipher glyphs, key decode equality with manually recorded literal strings, exact tokenwise roundtrip, and exact equality of the indexed TSV with records. This establishes internal reproducibility and unchanged originals; it does not prove the visual transcription. Optional --write-derived rebuilds row crops and derived displays. Root must still visually check the rows and controls.

No marker, watcher, independent reviewer, PDF, register entry or git operation created by this collaborator. Current claim is a complete 13-row message transcription/decoding with accented editorial Czech and Slovak translation; historical identification of Vamberce and nickname identity remain unestablished.

Root completed visual/source controls, added record/reference hash guards and asserted full289-unit count/literal display consistency. All checks read-only and passed before handover. No independent provider review claimed.
