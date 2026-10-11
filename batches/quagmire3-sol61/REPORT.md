# QuagmireIII / same-alphabet periodic conjugation — failed controls

The model is explicitly C_i = A^-1((A(P_i)+R[i modT]) mod26), with SAME unknown bijective26letter alphabet A on plaintext/cipher sides and unknown absolute periodic shifts R. It is a conditional generic model; no historical Budapest attribution is established. This differs from earlier Q1/Q2 standard-alphabet models, which were not rerun.

Both fresh genuine held-out150position controls failed blind recovery. No HCP334target was attempted, because the required positive-control gate was not met. These failures exclude neither QuagmireIII nor an unknown historical cipher.

A is stored as letter→position, with inverse position→letter. Decryption is A^-1(A(C_i)-R[i modT]). The only performed normalization subtracts A[a] from every alphabetposition after search; R is unchanged. R0was never fixed to0. Rotation of both sides leaves the model unchanged; reflection requires negating A and everyR. Independent100random150letter tests verify these gauges. Complete control alphabets are genuinely random; all shift classes start/search freely. Both planted R0values are nonzero (T3:1, T9:20), explicitly protecting against the erroneous absolute-shift canonicalization.

TRAIN is frozen ciphers/hcp-350/work/ring-4grams.tsv, derived from the first6786sentences of the recorded UD Slovak corpus. TESTwindows are150letters from held-out sentence offsets900and1050, with no target text supplied to scoring. Preparation matches the frozen model: accents stripped, ASCII digits spelled, PROPN wrapped inQ, sentence terminatorX. No TRAIN/control count is used as a key target. Corpus/model/source hashes and corpus split are retained in manifest.json.

Each control encrypts a complete genuine150letter plaintext using an independently random alphabet and shifts at T3orT9. Ciphertext positions70and94(zero-based) are erased. Question marks remain at those indices, preserving all later period phases. Scoring skips fourgram/fivegram windows containing an erasure; it never concatenates the separated observed letters. Full original plaintext/ciphertext and complete random planted keys are saved separately for after-search evaluation. Search reads only the erased ciphertext and TRAIN model.

Blind baseline:384random starts ×30000joint proposals.75%are alphabetposition swaps;25%replace an absolute shift class by any value0..25. Every1000moves, a chosen class is independently tested at all26shifts under its current alphabet, choosing the best language score. Annealing temperature is .2+9*(1-(iteration mod10000)/10000). Candidate selection uses only whole readable-window TRAIN4gram score.

| Control | Baseline match /148 | Selected4gram score | True erased4gram score | Seconds |
|---|---:|---:|---:|---:|
|T3|70|91.5116|215.2785|12.010|
|T9|33|−14.0398|236.4441|11.725|

One T9class has a planted shift0, meaning identity encryption in that class regardless of A.17of the33baseline matches are in this exposed class. They do not demonstrate alphabet recovery. T3has no such zero-shift class. Neither full alphabet/shift key nor complete148letter readable plaintext was recovered. True text scores exceed the selected candidates, pointing to a search failure rather than demonstrated unavoidable scorer preference.

A distinct fixed generic post-refinement uses frozen TRAIN5grams from each unchanged operative4gram winner:16starts ×50000moves, firststart unchanged and laterstarts five random alphabet swaps plus one random absolute-shift replacement. No truth-selected seed. Erasure phases and windows are preserved. It also fails: T3=69/148,5gramscore−351.8445versustrue−158.3799; T9=27/148,score−453.6517versustrue−110.0831. These weaker results are retained, not silently replaced by better baseline diagnostics.

Independent Python encoders/decoders reconstruct each selected full key pair and reproduce all148observed ciphertext letters exactly, retaining the two questionmarks. Independent whole-readable-window language scores agree with C++ float scores. This key-fit identity is algorithm consistency, not validation of incorrect plaintext. Erased plaintext/cipher positions were not inferred or claimed recovered. Complete selected alphabets, absolute shifts, candidate outputs, planted controls, per-class truth diagnostics and timings remain in results.json/results5.json and control folders.

Compile search.cpp/refine5.cpp with clang++ -O3 -std=c++17 into corresponding batch binaries; `python3 batches/quagmire3-sol61/controls.py` resumes preserved baseline searches; `python3 batches/quagmire3-sol61/post5.py` reproduces post-refinement. Gauge evidence is in gauge-check.json. All writes remain inside this batch, sourcecipher334and priorcipher/batchfiles are read-only, no markers/watchers/reviewer/solutionlookup. No process remains running. No W→Vnormalization or arbitrary omissions were introduced.

A concrete structural next approach would fit per-phase substitution maps and enforce that they commute and are powers of a common26cycle. That conjugation relation is information ignored by generic random alphabet/shift proposals and could provide a justified seed. It must pass fresh erased controls before source variants. Simply adding identical restarts to the failed objectives is not a demonstrated attack improvement. Absolute R0must stay free in such a model too; source-derived damage variants and any glyph uncertainty remain separate from key inference.
