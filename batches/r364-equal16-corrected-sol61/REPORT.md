# Corrected HCP364 equal-width16 R triple

No target key was recovered. All16 constant shared alignments are **UNSAT** for three ordinary irregular columnar transpositions of width16, the corrected EXCUV/EXCVU ciphertext alternatives, omission of original group3, and the visible reply's64-letter four-sentence-X template with a fifthX inserted at any boundary. This is a conditional family exclusion, not a claim that historical R or HCP364 is impossible.

## Why this is a new valid check

The old `batches/constraint-sol61/sweep_aligned_equal.py` equal16 targets explicitly set group12 to **ERCUV**, and used the four-sentence-X quote with an unknown suffix filler. They did not test corrected **EXCUV/EXCVU** or a fifthX at an arbitrary boundary. The newer corrected double sweep has only two stages; the corrected primary triple runner has widths21/19/20. Exact script evidence is in `old-input-gap.md`.

At length65 and width16, physical column0 is the only five-letter column; every other column has four letters. Its common readout rank n determines the complete long/short chunk pattern in every stage. The copied exact-cover solver therefore retains only those actual chunk boundaries: rank r starts at 4r before the long column and 4r+1 afterwards. This pruning removes no valid key in the declared aligned family. The original exact rank and coverage constraints remain.

## Fresh positive controls and audit

Three independent blind controls use shared alignments1,8,16; fifthX positions0,37,64; and finite ciphertext alternatives differing by U/V exchange. No true keys or insertion positions are supplied to the solver. Alignment is the declared case condition, as in the enumerated targets. The first64-letter template is independent randomized full-alphabet text; the other two are independently encrypted source-quote-pattern fixtures.

All three are SAT in0.21,0.23,0.32s and reconstruct their exact planted65-letter plaintexts. Complete keys, selected ciphertext alternatives and insertion positions are retained in controls.json. Every witness is independently encoded by explicit physical-position gathering and inverted by column filling over all65 positions. Neither plaintext uniqueness nor original key uniqueness is assumed.

An independent finite audit enumerates every168 insertion/keyset combination for the analogous length7/width3 unique-long-column model, with common ranks1–3. All18 positive and same-inventory negative cases, including unknownX position and U/V union, agree with the pruned exact solver. This checks the stated small domain and does not constitute an exhaustive audit of65-letter instances.

## Actual conditional results

All16 target cases complete at0.06–1.33s, zero UNKNOWN and zero SAT. Both corrected source alternatives are encoded as one finite union, so each UNSAT applies to both; no UV ordering was selected by expected prose. The source originals are unchanged. The cover's reply remains a disclosed known-plaintext hypothesis, not an AI decipherment.

The source-motivated fixed-endX preparation (`...UVEDCISLOXX`) is already a subset of this free-insertion model, so the exclusion includes it without an unnecessary second run. Other widths, unequal widths21/19/20, progressive alignment, different reply preparation, indicator omission, ciphertext interpretation or another plaintext remain open.

Reproduce from repository root:

```
python3 batches/r364-equal16-corrected-sol61/audit.py
python3 batches/r364-equal16-corrected-sol61/run.py
```

The runner resumes preserved case outputs rather than restarting completed searches. Requires existing Z3 at `/private/tmp/hcsolve-z3`. Solver source credit: `batches/r364-corrected-double-sol61/exact_cover_insert.py`, with unique-long-column boundary pruning added here. Provenance retains source variants/hash. No cipher directory, source, marker, watcher or reviewer was changed.
