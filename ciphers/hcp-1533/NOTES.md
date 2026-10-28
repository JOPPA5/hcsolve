# Solver notes — HCP1533 / pc_hcp_214

## Scope and provenance

2026-10-28 UTC: read repository README in full before work. Work is limited to this cipher and its batch note. User/root override: no watchers or reviewers; collaborator does not create markers, PDF, register entry, submission or git changes. Root captured rendered General, Description and Attachments, both immutable original images and the bounded register/public-family provenance before work. Existing HCP1520–1527 key explicitly supplied; copied HCP1527 key. No independent recovery or blind test claimed. A memory-registry search for Anna/1533/1520/1527 returned no relevant hit and supplied no facts.

## Image reading

Original picture 1024×674 becomes upright 674×1024 after lossless 90° clockwise transpose. An initial counterclockwise working preview was upside down; overwritten working upright copy after inspection, source untouched. All writing is in two lower side blocks: nineteen rows total, left A01–A11 then right B01–B08, as indicated by arrow after A11. Address side contains ordinary postal cursive and stamps, no further identified cipher units.

Manual shape transcription and row boxes are in work/transcription.json. Global and row ordinals (236 positions) are in work/positions.csv; source hashes in source-sha256.json. The original-pixel controls are native crops and exact nearest-neighbor enlargements, no OCR, sharpening, generative restoration or contrast modification. Supplemental broad crops A1-4.png/A5-8.png/A9-11.png/B1-4.png/B5-8.png were early working views; C01–C10 and per-row crops are the precise final controls.

## Discarded rough drafts and decisions

- Rough A02 visual draft `72cy6g3` gave nonsense “JUSJAKO”. Focused source read `t2c4sg3` → DUSICKO, with ordinary D/I/C glyph classes; draft discarded.
- Rough A03 omitted the R-shaped `h` in ZARMUTKU; original clearly has `q6hn2dg2`. Not a missing base letter supplied from semantics.
- A06 after K is E-shaped `5`, not A-shaped `6`; final SRDECKEM, rough SRDECKAM discarded after original comparison.
- A07 is `6m2mg3` → ANUNKO. Third shape is same 2/U form as nearby BUD. Familiar ANINKO/ANICKO would require different source units and is not adopted.
- A08 is `fqt4d` → VZDIT. Do not silently replace I with Y to modernize “vždyť”. Editorial “vždiť” is explicitly base-preserving.
- Four special CH glyphs are complete units including their caron-like top: CHOROBU, VRELYCH, UPRIMNYCH, KACH.
- Dark stroke in the first M-class `n` of B06 MYSLEN is documented C09; no unsupported prior canceled glyph is reconstructed.
- Arrow after A11 is continuation into B01, no extra cipher unit. Three line-end splits ZA-/JISTE, ZI-/ROVNICE, MYSLEN-/KACH retained literally and joined editorially.

## Verification

Read-only stdlib command `python3 ciphers/hcp-1533/work/decode.py` passed: three immutable source hashes, three record hashes, nineteen expected row IDs, 236 ordinals, four CH units, 240 base letters, exact tokenwise cipher→plain→cipher roundtrip including separators. This verifies record consistency rather than independently proving manual glyph readings. Both original images and the focused crops were visually inspected by this solver collaborator. No external target solution was used. Root source-derived comparison feedback, if subsequently supplied, must be separately acknowledged in the final solution.

Root inspected both originals, all row panels and focused ANUNKO/VZDIT/MYSLEN controls. Read-only decoder, record hashes and wave source manifest passed. Translation clarified sympathy in the brother-illness context. DONE1 is created last and freezes the directory pending review.
