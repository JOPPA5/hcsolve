# HCP 1538 / pc_hcp_219 — solver notes

2026-10-28. Assigned solver collaboration limited to this card. Root captured the rendered General, Description and Attachments: Not solved, Czech, Substitution, private postcard to Anna Tichá, 1903-09-22, no individual solution/transcription attached. Root checked the fresh 173-row/139-HCP-ID register snapshot; target absent. This bounded register check does not prove worldwide novelty. No watcher, reviewer, markers, PDF, register entry or git operation was launched by this collaborator, following the explicit user override and assignment.

Both original images were visually inspected in full, including edges, the date, address side, main picture-side text and upper inverted margin block. Address: Velectěná Slečna / slečna Anna Tichá / učitelka v / Žirovnici / u Počátek. Picture date: 22./IX.1903. No encrypted address-side message observed.

Method: manual glyph transcription with the pre-existing Anna Tichá family substitution key from hcp-1520 and the already disclosed public partial study and generic key. The pc199 photograph/provenance was available as an external visual F reference from the start; it is hashed, but this target needs no newly discovered F mapping. This is known-key transfer informed by prior public partial work, not independent key discovery or a blind target test. No initial target plaintext was supplied. No OCR was used.

The picture is rotated clockwise 90 degrees for main rows M01–M11. Original upper band is rotated 180 degrees for S01–S04. `work/row-index.json` gives exact crop coordinates and `work/rows/` contains all 15 physical row crops. Additional enlargements retain context at difficult spots. Rows retain physical boundaries, original spellings and visible word spacing; gaps across stems are not filled from grammar.

Several central spans are too dark to transcribe securely. G01–G09 denote unknown-length spans near stems in the nine upper main rows; G10 is the flower-overlapped margin span. U01 is one visible but ambiguous m/n cipher glyph before G10. Counts do not assume that a dark span is one cipher unit, or infer its length from plausible Czech.

Initial shorthand suspected the dense M08 word was a canceled `projekt`; closer source inspection refuted that reading. Readable `bh3` and `q5d4` yield `pro…zeti`; possible middle `r84` would yield `hli`, making `prohlizeti`. Root independently inspected the crop and correctly noted that horizontal/overwritten ink does not prove intentional cancellation. Final C01 is an uncertain overink span, with its middle neither counted nor silently completed. Seven surrounding readable glyphs are provisionally treated as active. No definite canceled segment has been established.

Current honest result: partial. The 494 visible indexed units comprise 493 mapped units and one ambiguous U01. The mapped output has 494 base letters because one CH glyph expands to two letters. There are ten unknown-length dark spans and one additional uncertain overink span. Unknown span lengths make full-message coverage and total active-symbol count unknown. Native-pixel and nearest-neighbour control inspection corrected the initial duplicated b in `bb6d5g`: source reads `b6d5g` = patek. The 6/A ascender had been mistaken for an extra b/P. Same-card b3/d3p5 and 6m4sg3 controls are saved with exact coordinates in control-index.json. `Pus` in “tisic uprimnych pus” is correct Czech genitive plural, not a typo.

`work/decode.py` is read-only by default. It verifies SHA-256 of the immutable original images, original metadata/SOURCES, manual transcript/key/row index, all row crops, generic public key and pc199 photo/provenance. It checks all local/global unit indices, each mapped glyph, and exact token-wise roundtrip of the stored manual record. The whole-key inverse independently recovers 479 singleton-class units; 14 alias-class units require their saved glyph labels because j=y/7 and ch=H/ř are noninjective. Unknown placeholders retain placeholders. Default verification also asserts exact equality of saved decoded-literal.txt and indexed-units.tsv against current output; --emit-only skips those saved-output comparisons only during authoring. This proves internal reproducibility, not that pixels were automatically decoded or that every manual reading is correct. Full verification currently passes for 30 hashed files and all 494 indexed units.

Root reviewed nativePATEK/source controls and all regions,required correction of duplicateP and unsupported cancellation classification,then reran corrected decoder. Currentcounts494positions,493mapped/1ambiguous;10dark+1overink unknownlength spans. No marker.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
Stem printed first; writer skipped it, so G01-G05, G08, G09 hide nothing.
G06 [O], G07 [OS], G10 [A] restored at edges. M03 m5 -> n5 (ME) proposed
correction. C01 = PROHLIZETI. Register re-checked (357, 1538 absent).
Watcher + DONE1.

## 2026-10-29 — Claude Opus 5.5 (solver), response to review 1 (REVISE)
New record work/transcript-final.txt + work/decode_final.py (503 signs: 498 read, 1 partial, 4 restored).
M04 `c4s` added (reviewer crop m04a.png confirms raised s), M03 n5, M08 r84, S01 m[6], stems as blank.
SOLUTION.md header/uncertainties rewritten; response section added; report + register entry; FINAL.
