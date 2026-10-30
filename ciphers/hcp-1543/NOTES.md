# Solver notes — HCP1543 / pc_hcp_224

2026-10-28. Solver collaboration only. User override: no watchers, no reviewers. No marker, register entry, or PDF created by this collaborator.

Portal and register setup supplied by root: portal Not solved, Czech private postcard, date 1903-08-17, Anna Tichá, no attached individual solution; target absent from fresh 183-row/149-HC-ID register snapshot. Those bounded checks do not establish worldwide novelty. Source files and metadata are immutable.

Known family substitution was available before target transcription: earlier local `ciphers/hcp-1520/work/key.json`, published partial Anna Tichá key text, and photographed pc199 reference. This is prior-work-assisted key transfer, not independent key discovery, a blind test, or independent provider review. The rare F reference is available, but no target F assignment is needed.

I inspected the entire picture after clockwise rotation, all fourteen handwritten message rows (including four short rows below the main block), all picture margins, ordinary date, and the whole address side. Address reads Anna Tichá, teacher, in Jindřichův Hradec, at Miss K. Janková, teacher. No extra cipher message was identified on the address side. Date reads 17.VIII.1903. The picture's artist signature/printing is ordinary illustration text.

`work/transcription.json` preserves every base-symbol row, gaps/punctuation, and two unresolved record slots and one explicitly less-secure selected g/K glyph. `positions.csv` indexes all known base units plus opaque/ambiguous slots. There are 359 transcribed units (including one less-secure selected g/K glyph), and two dark spans whose underlying unit lengths are unknown; 361 is a record-slot count, not a total ciphertext-unit count. Indexed image and R01–R14 crops retain row evidence. Digit-like J is labeled 7, and the capped/marked H-like CH is labeled ř, aliasing canonical y and H. These aliases are visual labels rather than decoded accent values.

Unresolved: R04 HRA[UNK1]E; R06 SRDE[UNK2]KO. The dark areas may be overink/overwriting, but cancellation intent and underlying lengths are not established. Contextual Hradce and srdéčko are plausible readings, not recovered units, and are deliberately absent from the literal output. R09 VASNI VYCH and R06 PRI VODILA show manuscript gaps that editorial prose rejoins. No silent grammatical completion is used.

Early quick visual notes incorrectly described the lower ending as pozdravy and first R04 word as PRA…E. Dedicated enlarged crops corrected these to PO-/RUCENI and HRA…E; neither initial mistake is present in the final record. RNOUTI was corrected to RMOUTI after rechecking n/M versus m/N. R06 OPET is 3b5d, not 3f5d, by comparison with the P glyph in POSILA. The initial name was initially bounded as ANI[Z/K]O. After root and collaborator compared native pixels, g/K was selected: its lower loop closes like g/K in same-row DIK and R11 JANKOVE, whereas q/Z in ZA and ZE has an open hook. The output is ANIKO, with this one choice explicitly less secure than clear units. The discarded q/Z reading would give ANIZO. This is a stroke comparison, not a customary-diminutive or grammar argument. The native nearest-neighbor control is work/name-native-controls.png.

`python3 ciphers/hcp-1543/work/decode.py` verifies source, earlier-key/public-reference and record hashes; reconstructs every index and saved plaintext; and tests whole known chunks using a real inverse of the canonical key. It is read-only. Canonical inverse checks lose 7/y and ř/H alias detail and assume CH is a single plaintext digraph; they cannot independently certify manuscript transcription, distinguish an hypothetical C+H adjacency, or prove the borrowed key correct. No tautological per-token “reverse lookup” is offered as evidence.

Root inspected both sides, all fourteen rows and focused native controls. Closed lower loop supports selected g/K in ANIKO; two opaque spans remain. Final decoder passed359units/362baseletters,3CH. This is solver collaboration, not independent review. No marker.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
R04: t/D visible after rh6, one blotted sign then 5 -> HRADCE. R06: one
s/C sign with caron stroke -> SRDECKO. Promoted to complete; register
re-checked (357, 1543 absent). Watcher + DONE1.

## 2026-10-30 — Claude Opus 5.5 (solver), response to review 1 (REVISE)
- R01 name: narrow hooked s (C) between 4 and g was missed; record now 6m4sg3 = ANICKO (Aničko). ANIKO/ANIZO alternatives dropped.
- R04: crossed t (D) after rh6 entered as read sign; blot position = editorial restoration [C].
- R06: blotted sign is a closed bowl with long oblique stroke, not the family s; C is a contextual restoration [C]; hacek idea speculative. Earlier claim "bowl and hook of s" withdrawn.
- build-record.py re-run; decode.py prints Z HRAD[C]E, SRDE[C]KO; 361 read + 2 restored = 363 positions.
- SOLUTION.md rewritten to a single status; the partial-reading history above is kept only here.
