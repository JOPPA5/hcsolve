# HCP1541 solver log

- 2026-10-28: Solver collaborator scoped solely to this cipher. README previously read fully. Parent supplied fresh rendered all-tab source/register inspection, immutable originals and known family key before transcription. No initial target plaintext. User override forbids watchers/reviewers; collaborator creates no marker/PDF/register/git artifact.
- Inspected both source sides and all margins. Picture upright after clockwise90-degree rotation; 19 cipher rows. Date19.VIII.1903 and AnnaTichá/Pelhřimov address are unciphered. Lower final rows overlap printed dark trees.
- Manual transcription, no OCR. Most text coherent with key transferred from earlier local AnnaTichá cards and disclosed partial public study; no key-discovery or independent-review claim. Public pc199 proposedRUDOLFINA is reference only; rareF not claimed on target.
- Early guessed PANVE and ZNAMY rejected: actual b6n5dm4/gm4r1 yields PAMETNI/KNIHY, making a reference to an Ústí deanery memorial book. P08qr6d48 is ZHATIL, not earlier mistaken KRATIL. P18qbh6f2 is ZPRAVU, no insertedK or forcedSCHUZKU.
- P09cbh6f5s gives literal SPRAVEC. Keep it; editorialSPRAVCE identified as repair. Do not silently swap glyph order.
- One distinct visible unassigned k-like glyph in P11SVA[U01]RA. Supplied key/publicgeneric assignments have noG, so do not assignG solely from expectedSVAGRA. Dedicated control retained.
- P16/P17 darkspans U02/U03 have unknown lengths. Preserve VECN[U02]TVUJ and SE[U03]NA without inserting expected endings/TESI. These spans are not counted as one glyph each.
- inventory.json:547visibleindexedunits (546known-key units+1unassignedboundedglyph), plus2unknown-length spans. All19rowcrops; whole-side/addresscontrols; focusedspravec,svagra,pametni/knihy,zpravu,tailcontrols. No canceled cipher ink identified; overprinted trees are not cancellation strokes.
- Read-onlydecode.py verifies11hashes, indexedpositions,keyapplication and realfixed-keyinverse. Unknownlabels pass through explicitly, excludedfromdeciphermentproof; no per-tokenreverse-dictionary tautology. Build-record.py is optionalmutatingbuilder, never advertised asreadonly.
- Candidate substantial but partial. No historicalidentities, fullaccentrecovery, unseenunderpaintingtext, or independentexpertvalidation claimed.

Root completed both-side/whole-region/focused source checks and reran final decoder. No new G mapping,unknowns retained. Current547positions=546known+1unassigned;553 assignedletters,7CH,2unknownlengthspans. No marker.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
U01 = k-shaped sign -> G (SVAGRA); matches single-G slots in 1554/1570.
U02 VECN[E] TVUJ, U03 [T]ESI (ESI visible). Register re-checked (357, 1541
absent). Watcher + DONE1.

## 2026-10-29 — Claude Opus 5.5 (solver), response to review 1 (REVISE)
- Re-cropped row 17 at 7x (work/review1/). Reviewer right: the stroke after
  the E-like sign is not round `c`; best match angular `s` (C), maybe `1`.
  Visible: 5 <s> 4. TESI now an editorial reading (hidden T, slip C for S);
  same kind of swapped-pair slip as TIK on hcp-1556.
- New single command work/decode_final.py + transcription-final.txt +
  key-final.json (J relabelled 7, k-shaped sign = G). Asserts the final
  transcription differs from the audited round-0 record only by the 4 relabels.
- SOLUTION.md restructured: current state on top, round-0 and completion text
  under History (superseded). Report + register entry + FINAL.
