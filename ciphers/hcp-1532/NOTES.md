# HCP 1532 working notes

2026-10-28. Solver collaborator restricted to this cipher and its batch note. Root had already rendered all three portal tabs, downloaded the two images, checked status Not solved, found no attached target transcription/solution, and supplied the existing family key before work began. The explicit user override forbids watchers/reviewers; no watcher, marker, PDF or register work is done here.

## Inputs and method

Read repository README in full. Inspected both original picture and address images. Picture has eight sloping handwritten cipher rows below the flowers, plus a tiny vertical continuation up the right edge. Upright source dimensions 1024×674. Ordinary date is 2.XI.1903. Address identifies Anna Tichá, teacher in Žirovnice near Počátky. The cipher itself signs PEPOUS; no civil sender identity inferred.

Manual known-key transcription, no OCR, automated key recovery, independent review or blind test. Initial body crop and focused native-pixel enlargements were made from the immutable original. Image resize interpolation provides visibility only; it creates no new source detail. Later `work/build-record.py` creates the indexed full image, nine readable row crops, CSV ordinal record and controls. Record coordinates are source-image row boxes, deliberately overlapping due to sloping baselines; no individual glyph coordinate precision is claimed.

## Drafts discarded after original-pixel comparison

- Initial rough shape pass confused h/b in SOBOTNI and LEPE, and n/p in BYL. Ascenders and comparison within the card resolve c3p3dm4, 85b5 and p18. Rough outputs SORODNI, LERE and MIL were drafts, not plaintext claims.
- R02 `q6t6m32` is ZADANOU and `d2t4q` is TUDIZ; the narrow forms are not inserted letters.
- R03 end was initially drafted as gt3-84 (KDO-LI), then checked for gt6-84 (KDA-LI). Close source comparison with R01 ZA, R04 ZAJISTE and R01 KTERY resolves `qt6-84` (ZDA-LI). The first shape has the q/Z bowl and hooked descender; K's g shape has a crossing loop. Third shape has the tall hooked 6/A, not round 3/O. `focused-controls.png` preserves these same-card controls. This is visual correction, not replacement from the expected question.
- R07 MUSIL was initially visually hesitant because of tightly joined strokes. Source is `n2c48`; n/M and m/N keep the transferred convention. No modern MUSel replacement.
- R08 the long word contains `m5cs4c8m5gh6d5` → NESCISLNEKRATE. The c/S, narrow s/C and following 4/I are kept as separate glyph units. No missing E is inserted to modernize to NESCISLENEKRATE. Archaic *nesčíslněkráte* is retained in editorial Czech.
- R08 CH in DUCHU is the single marked family glyph, labeled ř; source H in marginal HLAVINKU provides a same-card unmarked comparison. No rare F assignment is needed.
- The tiny margin is `r86f4mg2 84p6.` → HLAVINKU LIBA. It completes the final sentence; omitting it would leave an incomplete reading.

## Verification

Final record has R01–R08 and M01: 61,63,62,54,56,56,61,72,12 units; total 497, including 1 CH unit, yielding 498 base letters. Reproduction is read-only and standard library; source/record SHA-256 hashes, all index ordinals, claimed row text, active-unit counts and tokenwise inverse-key roundtrip pass. This checks internal consistency of the human image transcription and transferred key, not independent proof of each glyph. Original hashes are in work/manifest.json. Punctuation and editorial accents are outside the 497-unit denominator; no canceled cipher unit identified.

No target plaintext seed was supplied at commencement. Root received the solver's drafts and ambiguity descriptions during work; any later source-derived corrections or validation from root must be explicitly added to SOLUTION rather than characterized as blind or independent evidence.

Root inspected all original regions, eight body panels, full marginal continuation and ZDA-LI/NESCISLNE/CH/H controls; documented decoder, record hashes and wave manifest passed. No base-letter repairs. DONE1 is created last and freezes the directory pending review.

## Response to REVISE review1 — solver correction, 2026-10-28

Read README.md in full again, REVIEWED1 and all three numbered findings in review/REVIEW1.md, original source sides, transcription/index/key/manifest and both existing scripts. The previous final/coverage statements above describe the pre-review record and are superseded where stated here. Persistent override prohibits launching watchers/reviewers or writing markers/PDF/register/review/source files.

Inspected the original pixel regions independently of the review crops. R01 first TEPRVE's third sign has a descending p/B stroke like BYL and differs from the looped b/P in R02. Corrected R01 ordinal46 b→p, literal TEPRVE→TEBRVE. The editorial Czech alone restores teprve, and Slovak translates the intended sense. Selected b/P count17, p/B count7; fixed22-class key unchanged.

R08 OD's second sign (row ordinal27/global440) combines a closed d-like left bowl with a short t-like crossbar. Preserve t/d uncertainty; contextual D in OD is explicitly selected, with T/OT alternative recorded. No erasure, cancellation, intended correction direction or secure clean t is inferred. Added structured observation/candidates/basis to transcription.json and explicit CSV ambiguity columns plus inventory. Native and NEAREST4× original controls and exact broad source boxes are in review1-original-controls.{png,json}.

Inspected old build-record.py before running any mutator. Revised generator only writes work/, verifies existing original-source digests and fixed-key digest first, then regenerates index, literal, inventory and manifest. The revised read-only standard-library decoder validates ambiguity metadata and uses an actual whole-row inverse of printed plaintext through the fixed key (CH before C), replacing the former tokenwise identity check. All9local record hashes and3unchanged source hashes pass. Row counts61,63,62,54,56,56,61,72 plus margin12 still total497:496unambiguous and1ambiguous, oneCH→498selected baseletters. Successful checks do not resolve the ambiguous ink or prove glyph truth.

Added Response to review1 numbered1–3 and removed stale no-review/no-marker/pre-handover claims. Existing DONE1/REVIEWED1/review1 were not mutated. Root QA and protocol decision remain outstanding; this collaborator makes no ACCEPT/FINAL assertion and writes no report, register entry or marker.

Root review-addressed closure pass: current REVIEW1 and original-pixel controls checked; every numbered finding addressed without key/meaning change. Read-only reproduction verified. Existing review verdict remains REVISE; reviewer explicitly allows closure after corrections. Preparing corrected report and local register entry, then FINAL as final cipher-directory write. No watcher, new reviewer, external submission, commit or push.
