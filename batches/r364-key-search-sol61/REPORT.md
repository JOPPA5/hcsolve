# Direct known-plaintext triple-columnar heuristic: 21/19/20

Three independent65-letter controls failed blind key recovery. Best witnesses match48,48,49 positions respectively, rather than65; no target was attempted under the requested positive-control gate. This is a heuristic failure and provides no exclusion of triple21/19/20, the conditional quote, historical R, or HCP364.

The immutable scan and metadata were read. The quoted request on the cover is not established as ciphertext plaintext. Calibration uses the existing conditional64-character normalization `nelustitelnexneudalsicislopredtextomxvidbodtripokynovxuvedcislox` plus one fully known filler R/M/U in the three controls. Fully known fillers simplify calibration compared with an unknown target filler; failure even under this easier condition is a material limitation.

Keys are physical zero-based readout orders: writing by rows at widthw and emitting columns in key order. For65characters widths21,19,20 have respectively2/8/5 four-character columns, with all remaining columns three-character. This differs from the previous exact-cover/SAT model: direct coordinate assignment and joint stochastic search use only positional agreement with known plaintext/ciphertext, never language scores, cribs or truth keys.

For a chosen stage, all other stages are fixed. Independently encrypt the known text through preceding stages and decrypt the ciphertext through following stages. Its current long/short readout pattern fixes chunk boundaries. Build column-to-chunk agreement matrices separately for each height, then solve both assignments with Hungarian minimum cost. A match has weight100000, with random tie jitter<1000; at most21columns guarantees jitter cannot trade away a matched letter. One-third of coordinate proposals swap a long and short rank before assignment, changing boundaries.10% of all proposals are ordinary readout-key swaps. Annealing accepts whole-keyset agreement changes at temperature .15+1.4*(1-(iteration mod1000)/1000). Each control receives200 independently randomized starting keysets and5000proposals per start; no planted key or planted intermediate text seeds the search.

| Independent seed / known filler | Proposals | Best agreement | Seconds | Exact plaintext/keys |
|---|---:|---:|---:|---|
| 364219201 / R | 1,000,000 | 48/65 | 5.618 | No |
| 364219202 / M | 1,000,000 | 48/65 | 5.615 | No |
| 364219203 / U | 1,000,000 | 49/65 | 5.625 | No |

Complete three-key witnesses, predicted ciphertexts, inverse ciphertexts, disagreement positions, planted keys and deterministic blind seeds are retained in results.json and each control/result.json. An independent Python index-map encoder/decoder reproduces each C++ witness exactly; the witness prediction differs from the planted ciphertext in17,17,16positions, respectively. This confirms what the score means, not successful recovery.

Separate known-key checks agree with the independent encoder on all65letters and each fixed-other-stages Hungarian coordinate check retains65/65. These deliberately use truth only to check encoding and the conditional assignment step, and are not blind recovery. `assignment_check.cpp` additionally compares Hungarian with independent exhaustive permutations for300random negative/positive integer matrices of sizes2..7; all pass. Global key recovery remains failed despite these local checks.

Compile `clang++ -O3 -std=c++17 batches/r364-key-search-sol61/search.cpp -o batches/r364-key-search-sol61/search`; run/resume `python3 batches/r364-key-search-sol61/controls.py`. Search inputs contain only known plaintext and resulting ciphertext. The separate known-key file is passed only to the explicit consistency-check invocation; never to search. No SMT operation or previous search was rerun. No process remains running. All writes are inside this batch; source/cipher metadata/markers/watchers/review files unchanged.

Concrete next algorithm test: replace stochastic long/short placement for the21-column stage by enumeration of its210possible height patterns, solving Hungarian per pattern. This would find its exact best conditional single-stage update rather than local pattern flips; benchmark it blindly before any target use. The19/20 stages have75,582/15,504patterns and require a separate budget decision. Nothing in these failed controls justifies launching an equivalent target search or claiming the quote false.
