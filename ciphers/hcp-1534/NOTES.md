# HCP1534 solver notes — 2026-10-28

README read in full. Explicit user/root scope overrides the default watcher/reviewer steps: no watcher, reviewer, marker, PDF, register, git or submission is performed by this collaborator. Only this cipher and batch hcp-1534.md are writable task outputs.

Root captured both images and all rendered tabs before delegation. Both images were viewed by solver; address has no cipher. Picture rotated losslessly counterclockwise yields 674×1024. Cipher coverage is seven upper, thirteen right, four lower rows. All source files remain untouched.

Known key supplied before start. Family provenance/publication is disclosed in SOURCES and SOLUTION. DOUFAL's shallow-v glyph was inferred contextually before root supplied the photographed public RUDOLFINA/F comparison. That photographed comparison was then inspected and visually agrees. This is a later reference transfer, not independent discovery or review.

## Reading progress and rejected drafts

- Draft upper-row guesses based on small overall view were not retained: apparent `JISTOU` becomes visible `s4cd32` / CISTOU; `thr61` and `thr32cg2` were transcription-order/omitted-digit mistakes corrected from original close controls to `th6r1` / DRAHY and `th6r32cg2` / DRAHOUSKU.
- U07 originally looked like an incoherent short word; original-pixel controls support the special CH glyph and `cH2q4` / SCHUZI. The following word is `s5s48cg32` / CECILSKOU. This is a reading with the supplied key, not new key recovery.
- The word after TVOJE in U02 initially seemed JE MNE. The first cluster is heavily overwritten. It remains `?nm5` / [?]MNE, with no E or JE inserted; the source may contain a canceled attempt or compressed sequence. Status stays PARTIAL.
- S01 initial draft `f6cg6h4` changed from source inspection to `f6cg5h4` / VASKERI. Context strongly suggests VESKERI, but first vowel looks 6, so no 5/E repair is made.
- L01 MILAVANE is preserved from apparent `n486f6m5`. Context suggests MILOVANE; changing 6/A to 3/O would need better glyph evidence. No repair is made.
- S12 draft `c3tf6` / SODVA corrected to looped `c3df6` / SOTVA after original control. S05 draft TO TE corrected to crossed `t3` / DO TE. The key distinction is `d`=T with looped body versus `t`=D crossed stem.
- S10 AVSAK has overink at c/S. One active cipher c is read; no earlier canceled text reconstructed.

## Reproduction

`python3 ciphers/hcp-1534/work/decode.py` is read-only and stdlib-only. It checks source hashes and the manual record manifest, 564 indexed marks across all 24 rows, 563 assigned units, one unresolved cluster, three CH expansions, 566 assigned base letters and an exact tokenwise inverse-key round trip. The unresolved cluster is indexed once as an ink mark, with original component count unknown. No automatic scan-to-text, independent-review or held-out evidence claim follows from these checks.

`work/build-record.py` and `make-controls.py` are explicit record/crop generators using bundled PIL, separate from default reproduction. Crops use only the immutable original pixels and documented rotation. Indexed CSV has row coordinates plus ordinals, not false per-character pixel coordinates.

Root inspected all source regions and vowel/overink/F controls, generated all canonical row crops including S10/S12, synchronized later-reference F metadata and added two explicit reference hash checks to the decoder. Assigned text/counts unchanged. Original/record/reference checks passed. Still PARTIAL, no markers.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
U02 overink sits on the n/M of MNE (3 positions only) -> correction stroke,
no extra letter. Promoted to complete; register re-checked (357, 1534
absent). Watcher + DONE1.

## 2026-10-30 — Claude Opus 5.5 (solver), response to review 1 (REJECT)
Fresh 3x row crops of all 24 rows + 6-10x zooms (work/r2/). Confirmed the four
misreads from the scan and fixed in build-record.py (round-1 copy archived as
work/r2/build-record.round1.py): L04 qbh6f2 ZPRAVU, L02 2bh4nm1H UPRIMNYCH,
S13 t3s484n DOCILIM, L03 f5sm5 VECNE. U02 `?nm5` -> `nm5` (blob = n over an
abandoned descender sign; three positions as in clean nm5). '?' removed from key.
Counts: 564 units, all assigned, 567 letters. S01 2nd sign 6/5 ambiguous, kept 6.
Overinks at S10, L03 SLIBENOU, U04 disclosed. S08 CERTEM third sign rechecked: h.
SOLUTION.md rewritten with one status/text/translation set; DONE2.

## 2026-10-30 — Claude Opus 5.5 (solver), response to review 2 (ACCEPT)
Note on the earlier entries: the round-0 paragraphs above ("563 assigned units, one
unresolved cluster, 566 base letters", "[?]MNE", "Status stays PARTIAL") are superseded.
Current record: 564 units, all assigned, 0 unresolved, 3 CH, 567 letters; U02 reads MNE.
Review 2 findings are all minor; S01 6/5 caveat and the overink corrections are repeated
in report/report.md. Report, PDF, register entry, FINAL.
