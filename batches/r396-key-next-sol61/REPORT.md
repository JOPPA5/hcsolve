# HCP396 conditional key-search continuation — GPT-6.1 Sol

## Result and evidential limit

No full blind-control key was recovered; no actual ciphertext key search was run in this continuation. There is no new decipherment, target exclusion, successful marker, or register entry. The best control character fits were 43/50; they are false-basin diagnostics, not recovered-key progress. All source files were read-only. No watcher, reviewer or subagent was started.

The contextual plaintext belongs to public Solved HCP387: “Podajte šifrou stručnú zprávu o situácii a možnej činnosti.” Its preferred normalized length is 50. Original387 and repeat396 agree at 53/55 preferred ciphertext positions. Omitting DWJPM from original387 leaves one F missing and one P surplus. Three possible P→F experiments at positions 3, 20, 23 remain hypothetical errors: printed Ps were not corrected. The header755 does not establish alignment7. See `batches/repeat396-387-sol61/REPORT.md`. The independently audited primary worked example validates the irregular R core and widths21/19/20, not applicability to396.

## Calibration design

Two fresh independent 50-letter controls used independent random keys at widths21/19/20: control0 shuffled the matched letter inventory; control1 used the published prepared sentence. The optimizers received only plaintext/ciphertext and generic candidates. Planted keys were confined to fixture checks and subsequent diagnostic comparisons, never search ranking. Any consistent key producing every observed ciphertext letter would count as success; recovery of the planted key was not required.

| Distinct method | Control0 | Control1 | Saved implementation |
|---|---:|---:|---|
| Exact final-stage Hungarian assignment; annealed first/second keys and chunk pattern | 40/50 | 39/50 | search.cpp |
| Exact middle-stage Hungarian assignment | 39/50 | not run | search-middle.cpp |
| Global position/interval CP, then soft CP-LNS | UNKNOWN45s / 41/50 | UNKNOWN45s / 39/50 | position_cp.py, position_lns.py |
| Joint contiguous readout windows | 41/50 | 39/50 | block_cp.py, block_search.py |
| Explicit rank/cumulative-prefix CP | UNKNOWN45s | UNKNOWN45s | rank_cp.py |
| Alternating all-three-stage Hungarian assignment, including rare-letter weights | 43/50 | 42/50 | coordinate.cpp |
| Mismatch-support CP with frozen good offsets | 43/50 | 43/50 | error_cp.py, error_search.py |
| Known-crib capped bigram/trigram hybrid | 42/50 | 40/50 | hybrid.cpp |
| Direct three-key fragment annealing | 36/50 | 36/50 | fragment_sa.cpp |
| Rank-conditioned support repair, allowing long/short exchanges to move good starts | 43/50 | 43/50 | rank_bridge.py, rank_bridge_search.py |
| Globally free keys with all four unique-letter endpoints hard | 43/50, FEASIBLE40s | 42/50, FEASIBLE40s | hard_unique_cp.py, hard_unique_run.py |

The crib-fragment hybrid uses the legitimate known plaintext, including shuffled control0, rather than treating shuffled data as natural language. A primary double-transposition positional/trigram approach motivated it; that precedent is not proof of a triple attack. All candidate results and progress logs are retained. These bounded failures show inadequate recovery by these implementations; they do not eliminate R or the contextual preparation.

## Equal17 structural branch

N=50 at width17 has one short column, physical column16. The exact forward start is `3*rank[col] - (rank[col] > rank[16])`. Independently generated constant/progressive controls used unknown keys and initially unknown alignment. The rank, residue-band, arithmetic trajectory, exact tile, and last-stage tuple formulations all passed known-key checks but each returned UNKNOWN after30seconds on both blind controls. Files: equal17.py, residue17.py, arithmetic17.py, tiles17.py, tuples17.py. Tile auxiliary cell50 is never selected; no plaintext padding was introduced.

A separate conditioned-alignment calibration supplied only the daily n/mode, with no true keys: constant n11 and progressive n5. Both remained UNKNOWN30s (conditioned17.py). Such conditioning would require an actual enumeration of constant n1..17 or progressive n1..15; the target header was not used as a fixed n. The corresponding constant Hungarian heuristic reached40/50. No actual equal17 search followed. The independently generated controls and fixture results are preserved.

## Why 43/50 is not key recovery

`post-search-pattern-diagnosis.json` measures planted-map distance only after search. Control0's best43-letter fit agrees with just13/50 planted position mappings; raw column/rank agreements are1/21,0/19,2/20. Control1's best43 agrees with12/50 mappings; rank agreements are1/21,1/19,0/20. These comparisons cannot prove uniqueness or distance to all alternative valid keys, but clearly do not support a claim that a planted key was nearly recovered.

Control0's43-fit already places all unique D/F/V/M endpoints correctly. Control1's43-fit misses F (expected observed position25, predicted38, zero-based). Hard-unique repair therefore starts control1 from the healthy42-fit rather than supplying true intermediate trajectories. It failed to obtain a full witness. Rarity weighting had already been tried; no additional identical weighted restart was used.

## Independent verification and reproduction

Run from the repository root:

```sh
python3 batches/r396-key-next-sol61/verify.py
```

The independent grid-write/column-read encoder and partition/fill inverse verify15 retained candidate key sets and find **zero complete observed-ciphertext witnesses**. Candidate prediction round trips are separate from decrypting the observed ciphertext. Earlier soft-CP artifact flags described the inverse of the candidate prediction; those labels were clarified to `predicted_ciphertext_inverse_exact` and `observed_ciphertext_inverse_exact`, without changing keys. `inverse-label-clarification.json` records affected files. Known-key fixture checks were exact against their observed control ciphertexts.

Python CP scripts use OR-Tools from `/private/tmp/hcsolve-ortools`; C++ programs have no planted-key input. Each implementation retains its argument parsing and result/progress files. Compile a C++ implementation with `c++ -O3 -std=c++17 <source.cpp> -o <executable>`. Control truth is preserved for independent auditing, not supplied to optimizers.

## Source-context386 does not provide another known pair

Public Solved386 is same-day/channel context (MZV80212, 2.VIII.1944) for original387 (80214); shared daily keys remain a hypothesis. Independent source collation is in `batches/solved-context-main/386/AUDIT.md`: ciphertext280 letters versus draft574–591, first section348–355, Burzio tail226/236. Transparent preparation variants, all contiguous275/280-letter windows, prefix/suffix minimal padding, and all56 group omissions yield zero exact inventories. Best preferred case needs22 substitutions; even loose per-letter bounds across declared ciphertext variants require at least15 replacements. Source alternatives and crop disagreements remain recorded. Consequently no valid386 known pair or shared-key constraint was fed into this search. This finite inventory finding does not exclude arbitrary untested preparation or mechanisms. Our source-only crops and manifest are retained here.

All computations are complete. The cipher remains unresolved; sources and markers were untouched.
