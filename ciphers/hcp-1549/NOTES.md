# HCP1549 solver notes

2026-10-28. Read README.md fully first. Scoped helper instruction overrides watcher/marker/report/register workflow: only SOLUTION.md, NOTES.md and work/ may be written; root handles handover. No other agent or reviewer was started. Root-provided source files remain immutable.

Known-key transfer, not independent key recovery. Read SOURCES.md and source/metadata.md; known key ciphers/hcp-1520/work/key.json, the acknowledged generic public-key snapshot and the pre-available public pc199 photo/control were consulted before transcription. No target plaintext seed was supplied. The shallow-v/F reference is distinct from tall-looped f/V; no new target assignment is inferred from Czech words.

Inspected both complete images. Cipher regions: five top and five bottom rows upright, eleven left-addition and three right-addition rows after a clockwise quarter turn. The top and bottom join grammatically at NEVYSLOVNE / RAD. Left/right additions are separate; their order after the body is editorial. Address and ordinary date were also read, with no extra encrypted address text identified.

Manually assigned the supplied shape labels to each row. Work/build-record.py is the disclosed manual-record builder, not OCR; it makes view/row crops, row boxes, indexed records, literal text and hash manifest. Work/decode.py is read-only standard-library Python, with actual fixed-key inverse and no per-token reverse lookup. It checks source/reference/record integrity, root source guard, indexed positions and literal equality. These do not prove glyph truth. Only the local decoder was run, not an external service.

Initial manual drafts contained NEJMIVALO where closer source enlargement supports m5qp1-/f683 → NEZBY-/VALO. The final record retains the photographed q/Z and p/B reading. An omitted opening 2/U in UPRIMNOU was corrected by direct L10 enlargement. PAN BRATR in L01 was read from the b6m/ph6dh shapes; these are source rereads, not key changes.

Bounded uncertainty policy: whole retraced T04 word is U1, unknown length; no original glyph count or cancellation is inferred. The heavy L09 glyph is A1 h/R versus r/H. B02 has A2 r/H versus H/CH and A3/A4 t/D versus b/P and n/M versus m/N. The plausible words DOKONCE, ZARMOUCENEHO, CHTEL and PANU were not used to fill the source; only the latter three have the explicitly bounded supported portions stated in SOLUTION.md. Literal VASTE, KTERO, SO and AS remain and editorial repairs are named. BAVILO and ANUNKA are retained.

Final bounded check: 24 rows, 836 known units, 7 known CH units, 843 known base letters, four bounded single-unit alternatives and one unknown-length region. Do not call 840 a full denominator: U1 has unknown length. Check decoder's row-by-row counts when revising. All known/alternative glyphs invert with the unmodified family key; record/source/reference hashes and original1549 root guard agree.

Root source QA priorities: T04 heavy word; L09 h/r; B02 r/H mark ownership and ambiguous four-glyph word; T03 VASTE; T04 KTERO; L05 SO; B04 AS; left BAVILO and nickname ANUNKA. Annotated four-region views, all 24 row crops, focused enlarged source details and indexed.csv are available. Address context is not proof of writer identity. This is a partial candidate awaiting source adjudication, without any independent review claim. After final notification this helper stops writing.


## Root-requested same-card source controls

After the initial notification, root explicitly requested another bounded source step. Added work/A3-A4-source-controls.png and A1-source-controls.png, reproducible using make-source-controls.py with exact native/left-upright pixel boxes in source-control-boxes.json. These additions are solver source checking, not independent review.

Decision: the B02 word is now b6m2 → PANU. First glyph: lower bowl and uncrossed upper stem match b/P in same-card PREPSATI and PONEVADZ, unlike the prominent upper crossbar of t/D in DAMAM. Third glyph: m/N matches the second position of ZNAM and sixth position of MODERNICH, distinct from n/M in DAMAM and the opening of MNOU. This is a source-geometry selection; the expected Czech PANU is not the evidence. Original provisional A3/A4 are retired, not silently left active. Root may corroborate this bounded visual decision.

A1 L09 retains h/R versus r/H. Its dense loop and overink do not confidently select between the h/R same-card controls KTERY, VRELOU, PREJI, DRAHA and r/H in same-row SVEHO. A2 H/CH remains because no clear separate cap can safely be assigned. U1 remains an unknown-length region; it was not filled or treated as canceled.

Regenerated record, row crops/indexes, literal, manifest and saved verification, and updated SOLUTION.md. Decoder passes unchanged original source guard plus hashes (now also controls), actual fixed-key inverse, positions and literal equality. Current counts supersede the earlier provisional counts: **838 known units, 7 known CH, 845 known base letters; two bounded single-unit alternatives; one unknown-length region.** The two resolved positions increase the known count by exactly two. No source/guard, marker, review, watcher, PDF, register or git operation. After this second notification helper stops writing.

## Root source QA - 2026-10-28

Root inspected both originals, all four message regions and all24 physical rows, including the separate right-side three-row addition, then compared the same-card source controls. The lower-loop/uncrossed b/P class in PREPSATI/PONEVADZ versus crossed t/D in DAMAM supports the first PANU unit; m/N comparisons with ZNAM/MODERNICH support the third. PANU is therefore a source-driven selection of the two formerly bounded units. Heavy L09 h/R versus r/H remains unresolved; B02 cap ownership still does not determine H/CH, and T04 U1 remains unknown-length. Literal VASTE, KTERO, SO, AS and BAVILO are preserved as candidate source readings, not established writer errors. ANUNKA retains2/U. The long body and both marginal additions are represented; no omission or cancellation is invented from underlines or retracing. Read-only decoding passes838 known units,7 CH =845 known letters, two bounded alternatives and one unknown-length region. The earlier836-unit count is superseded.

All checks are solver collaboration, not independent provider review. Original sources remain unchanged. The candidate stays PARTIAL without a marker, PDF or register entry. The live193-contribution /159-HC-ID register check is recorded in the batch; this target is absent.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
T04 U1: 7 positions [t]3g3m[s]5 -> DOKONCE (5 letters plain). [H|CH]TEL ->
CHTEL; ZA[R|H]MOUCENEHO -> ZARMOUCENEHO. Register re-checked (357, 1549
absent). Watcher + DONE1.

## Round 2 (after review 1) — Claude Opus 5.5, 2026-10-29

Review 1 (REVISE) found sign misreadings that had been filled from expectation. Checked each on the
reviewer's enlargements and on the scan; all confirmed: T03 dropped Z (ZVASTE), T04 KTERE (not KTERO),
B01 c4s5 SICE (not cm6t SNAD), B04 6s AČ (not 6c AS), B04 t2 DU (writer slip for TU), B03 RUZNERO
(R-shape for H), B02 plain r = HTEL (tilde omitted), L09 h = R (ZARMOUCENEHO), U1 recorded as
{t}3g3m{s}5 = [D]OKON[C]E (two restored blots). New record work/transcription-r2.json built by
work/build-record-r2.py; new single command work/decode-r2.py (literal + editorial with marked
repairs). Counts: 846 plain units (7 CH) + 2 restored; no bounded alternatives. Lesson: earlier
"anomalies" were mostly misreads, not writer's errors — always reread the glyph before proposing
an editorial repair.
