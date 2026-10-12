# HCP369: rectangular R model and key-recovery calibration

The primary R description permits widths 16–22. HCP369's conditional payload has 110 letters after omitting WITPK; width 22 therefore gives five characters per column. Three equal 22 stages remove all long/short packing ambiguity. This is a source-motivated hypothesis, not proof that 369 used this width or system.

The direct model assigns three 22×22 one-hot column-rank matrices. Each physical column and each rank has exactly one assignment. Physical column 0 has the same unknown rank across all three stages, matching common R alignment. The solver receives no true n, planted key, hint or header-as-n assumption. Maps are `5*rank[column]+row`; composing the first two stages gives supported third-stage placements. The model has 1,452 rank Booleans and 53,240 endpoint clauses, approximately 13 times fewer clauses than the ragged 21/19/20 model.

Exactly one literal U endpoint may represent predicted N, as required by the conditional plaintext/ciphertext inventory. No source letter is changed or error endpoint selected beforehand. Other cipher letters must match exactly.

Small independent exhaustive validation enumerates all 216 width-3 key triples, retaining 24 with common alignment. Twenty-four observations are tested under eager SAT and native QF_FD: all 48 results agree with direct enumeration (**16 SAT, 32 UNSAT**). Witnesses independently re-encrypt with a separately written encoder. Records: toy-results.json.

Fresh artificial controls use independently authored plaintexts, independently generated keys with a common unknown n, and one independently chosen encrypted N observed as U. They are not held-out corpus samples. Control 0 has 102 lexical letters and 8 Xs; control 1 has 97 lexical letters and 13 Xs, versus the target preparation's 105 letters and 5 Xs. Seeds 3696122201/3696122202 are fixed independently of target ciphertext. Separate known-key checks are consistency checks only.

**Both blind controls recovered all three planted keys exactly:** control 0 at 17.63 seconds with n=7; control 1 at 34.18 seconds with n=5. Full 110-character encryption and inverse pass. verify.py independently reproduces their original ciphertexts and confirms literal key equality. No truth key or rank initialized either blind solve. Blocking the recovered full key tuple gave a 60-second UNKNOWN for control 0; this does **not** prove uniqueness. Other second-witness status records remain explicit.

A third fresh control matches the exact target plaintext/alphabet/profile: attributed published 365 plaintext, 72→SEDEMDVA, two sentence Xs and three final padding Xs, total 110 with 5 Xs. Fresh keys seed 3696122203 are generated without target ciphertext. It also recovered all three planted keys and unknown n=21 exactly, in **41.07 seconds**, independently verified over all 110 letters. This is legitimate known-plaintext calibration using an already published source, not a claim of discovering that plaintext. matched_control.py records truth separately and supplies neither keys nor n to blind search.

Second-witness checks: control 0 UNKNOWN at 60 s, control 1 UNSAT, matched control 2 UNKNOWN at 60 s. Only control 1's exact UNSAT establishes uniqueness within this particular mathematical model. The other two do not establish or refute uniqueness.

Actual 369 is gated on positive blind controls. Its fixed preparation above is compatible with primary Figure 5's padding practice, but not established as the historical preparation. WITPK omission and the N/U channel remain explicit assumptions. A target SAT would be a conditional mechanical witness: full inverse, independently verified re-encryption with its single disclosed mismatch, and a blocked-key search are required. It would not by itself establish historical key identity or uniqueness. All printed Us remain in the unchanged source.

The original 365/repeat 369 physical differences, missing UCNIO and swapped WITPK/ONDEX, are documented in batches/repeat369-365-sol61/REPORT.md. Earlier generic failures remain preserved. Solved 365 is attributed context only; no directory or marker was created for it. Only this new batch is written.

Reproduce:

- `python3 batches/r369-regular22-next-sol61/toy.py`
- `python3 batches/r369-regular22-next-sol61/run.py`
- `python3 batches/r369-regular22-next-sol61/matched_control.py`
- `python3 batches/r369-regular22-next-sol61/verify.py`

Saved JSON statuses are authoritative. Owned process IDs are saved before solving. No timeout excludes a family or plaintext hypothesis.

The actual common-alignment width22 branch returned **UNKNOWN at120seconds**; no target witness was found. This is not a general R exclusion, nor an exclusion of the fixed plaintext preparation. No target letter was modified.

A separate `progressive/` subdirectory preserves the second source-supported convention n,n+1,n+2 without overwriting common-model records. It restricts n to1..20 atwidth22, with no wrap. A new matched-profile control uses the same fixed110-letter plaintext and fresh independently generated keys seed3696122204, with no truthkey/n/hint supplied to blind search. Twenty independently enumerated width3 cases check both SAT and UNSAT before the full control. Actual progressive369 is gated on positive blind calibration. Run `python3 batches/r369-regular22-next-sol61/progressive/run.py`; its saved JSON statuses are separate from common-model records.

Completed progressive result: matched control recovered every planted key and n=6 in50.96s; blocked witness UNKNOWN60s. The actual fixed progressive22 branch is exact **UNSAT66.23s** under its declared assumptions. See `progressive/REPORT.md`. No mixed-width or general R exclusion follows. Reverse-support code is prepared but unexecuted; no duplicate progressive target run was made. The parent continues a separate native common-rank partition model; its partial results are not promoted here to a completed family result.
