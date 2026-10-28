# Solver notes — HCP 1527

2026-10-28. Scoped solver collaborator, HCP 1527 only. README read fully. Standing human instruction overrides watcher requirement: no watcher/reviewer/marker started. Root had already inspected all rendered tabs and supplied immutable originals, metadata and key-transfer provenance. No additional portal/API retrieval performed by collaborator.

1. Viewed both original sides. Lossless counterclockwise transpose gives 674×1024 picture with twelve cipher rows, ordinary date below. No additional picture-margin cipher or address-side cipher found.
2. Applied existing Anna Tichá family key from HCP 1520–1525. Published generic key provenance acknowledged from the outset. No statistical search, target corpus lookup, claimed independent key recovery or external decipherment service used.
3. Read every row visually. Initial draft had clerical transcription-label errors while reading the small image; these were corrected against enlarged rows before candidate creation. In particular R08 was initially mistyped sdfrd (CTVHT), then corrected to source sdfhd (CTVRT); this was a label typo, not an inferred replacement of a hidden glyph. R04 NENALEZIM and R01 PSANKO checked using source controls. The unusual PRED CTVRT ROKEM is retained, not repaired to a conventional phrase.
4. Recorded twelve source row boxes and every active glyph position in transcription.json and positions.csv. Generated indexed whole image and full row crops. Focused control crop coordinates and transforms are preserved in focused-controls.json/make-controls.py. Display enlargements use nearest-neighbor and introduce no new image evidence.
5. Created standard-library read-only default decode.py. Initially it checked three source hashes and three record hashes; after Review 1 it checks38 record/crop/code hashes, two reference hashes, all rows/counts/positions, saved/SOLUTION literal equality and actual whole-row inverse as well as tokenwise round trip. This checks record consistency; image truth still requires visual checking and independent review.
6. Pre-review count was 414 active glyph units, 2 CH digraph units, 416 base letters; the correction below supersedes it with 415/2/417. No canceled cipher unit identified. Ordinary date/address, underline, punctuation, whitespace and diacritics are excluded from base-unit counts. Separate accent restoration and translation supplied in SOLUTION.

No DONE/FINAL, reviewer files, PDF, register entry or git operation. Root owns the final visual check and marker decision.

Pre-review handover: root inspected both originals, full twelve-row body and focused controls; documented decoder and original/record hash checks passed. DONE1 was then created by root. REVIEWED1 now returns the card for correction; the earlier 414-unit count and some visual assignments are superseded below.


## Solver correction after Review 1

2026-10-28. Read README fully again, then REVIEWED1/review1, full SOLUTION/NOTES, records, source scans and both authoring scripts/decoder before mutation. Scoped writes remain only this card's SOLUTION.md, NOTES.md and work/. No watcher/reviewer/Claude launch, source/review/marker/PDF/register/git write. This card was not excluded by the explicit register-overlap constraints. Review 1 remains REVISE; this correction does not assert accepted/FINAL.

Re-read both original sides and all disputed rows. New `make-review1-controls.py` was inspected before execution; its source-derived nine-panel sheet is `review1-controls.png`, individual panels `review1-R*.png`, native boxes/transforms in `review1-controls.json`. The original pixels confirm all requested changes:

1. R02 has terminal angular s/C in `c5t86s-`, so SEDLAC-/KOVA and editorial Sedláčková, not Sedláková. Added R02 unit38/global73.
2. R10 fourth POSILA sign is 4/I, not1/Y. Updated `b3c186`→`b3c486`, removed posýlá claim, editorial posílá.
3. R03 final glyph order is `mn5` = NME, opposite same-row `nm` in MNOHO. Literal slip retained, editorial mně.
4. R02 initial `s85sm6` gives CLECNA; R11 initial `sht5sg2` gives CRDECKU. Both are angular C forms, not round S. R07 SRDECKA/JSEM/CASTECNE supply local contrasts. These repeated C-for-S slips are recorded; the fixed key was not altered to hide them.
5. R06 JINYMI fourth sign remains preferred1/Y (height/foot), with retraced closed 2-like loop and bounded2/U alternative. Added indexed uncertainty, global187/row4; literal preferred JINYMI, alternative JINUMI, no added or unassigned position.
6. Confirmed agreed PSANKO, NENALEZIM TEZ q/Z, K TEM/KDOZ g/K, CTVRT ROKEM, underlined PRED, CH mark VRELYCH. Meaning of PRED CTVRT ROKEM stays unresolved.

Counts now12rows,415activeunits,2CH,417baseletters,22observedclasses,0unassignedunits;1assignedsign explicitly uncertain. I/4 23→24,Y/1 10→9,C/s10→13,S/c32→30; m/n totals unchanged. Added counts/writer_slips/uncertain_positions to transcription.json, regenerated positions.csv and saved transcription.txt/literal.txt. Source/key bytes unchanged. Inspected modified build-record.py before running; it regenerates only work records/crops. Record manifest now covers records, crops, controls and code; references have separate hashes. Decoder gained actual full-row inverse and exact position/count/saved/SOLUTION equality. Its documented portable command remains `python3 ciphers/hcp-1527/work/decode.py`, read-only. Root handles QA and closure.

Root closure QA: every numbered Review1 finding checked against native/same-card source controls; review-addressed closure explicitly allowed by reviewer, with existing REVISE verdict preserved. Latest337/303register has target absent; six explicit exclusions remain honored. Preparing corrected report/local entry before FINAL as final cipher-directory write. No new reviewer/watcher/external submission/Git action.
