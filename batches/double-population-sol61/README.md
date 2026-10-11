# Double-columnar outer discovery: population and late acceptance

Unsolved calibration batch, not a target attack. Only this batch directory was written. Cipher 399, its existing controls/code/model files and all source records were read-only. No marker, watcher or reviewer was started.

## Scope and correctness

The known-outer consistent 3/4/5-gram column path from `ciphers/hcp-399/work/idp/multigram-beam-v2.cpp` was reused, beam width 16, weights .15/.4/.8. Candidate partial paths have one common column order, without independently maximizing each row. Pruning preserves the visited set and the first/last four columns relevant to future 5-grams. The objective sums within-row language windows, omitting wrap windows. `path.hpp` preserves this implementation and includes the original physical permutation/decryption helpers read-only; SHA256 provenance is recorded.

This scorer assumes a complete first rectangle. The tests use 240 letters, widths 20/17. It does not support the irregular 245-letter case. Thus even passing these tests would not satisfy the full 240/245 control requirement.

Correctness checks: 10,000 actual C++ order-crossover and mutation operations preserve permutations. Independent Python column-slicing encryption re-encrypts all reported full texts through both reported keys exactly. This checks the inverse/key conventions, not whether a false plaintext is linguistic. The known-outer diagnostic again exactly reproduces both planted inner keys and full plaintexts.

Controls were preserved from `ciphers/hcp-399/work/idp/controls.json`: an independently authored 240-letter diplomatic example and a 240-letter genuine UD test-partition excerpt. The frozen models were not modified or trained on either control.

## Landscape diagnostic

Truth is read only in the separate `landscape` invocation. All 136 single swaps in the physical outer-rank array were evaluated. Truth beats every one-swap neighbor in both cases:

| Control | Truth | Best swapped neighbor | Median neighbor |
|---|---:|---:|---:|
| Authored | -3043.50 | -3356.70 | -3550.80 |
| Held-out | -3384.56 | -3595.38 | -3802.85 |

This is evidence of a strongly separated local basin. It is not a discovery control, a seed, or proof that broad optimization can reach that basin. Diagnostic data and keys are never loaded by the blind processes.

## Algorithm 1: population/order crossover

All 40 initial physical-rank permutations are freshly random; no true keys, true plaintexts, earlier control winners, or diagnostic candidates are read. Each generation:

- Three-way tournament selection; order crossover copies one parent's contiguous interval and fills remaining positions in the other parent's cyclic order.
- Each child receives swap/reversal/contiguous segment rotation mutations; occasionally two mutations.
- 80 children, four random immigrants, and the previous population compete. Duplicate permutations are removed, top 40 survive.
- Each fourth child undergoes 24 sampled physical segment/swap refinement proposals, accepting improving moves.

40 generations; fixed seeds 619399/619400; cache counts 21,230/21,198 distinct objective evaluations. Both fail. Highest-scoring outputs match only 20/240 and 18/240 letters. Keeping top distinct individuals permits convergence to similar permutations; uniqueness alone is not a guarantee of broad population diversity.

## Algorithm 2: tabu with late acceptance

This is a different non-monotone acceptance rule, not another annealing restart. Each control starts from a fresh random outer key (seeds 619401/619402), independent of the population and diagnostic runs. At each of 30,000 proposals, a physical mutation (occasionally three combined) is accepted if its score is at least the current score OR the historical score 512 steps earlier. A 64-entry tabu queue suppresses recently accepted states, with aspiration for an improved global best. The history slot is updated to the resulting current score every step. Memoization avoids recomputing repeated proposals.

Distinct evaluations 15,596/14,280, accepted proposals 1,440/547. Both fail: 14/240 and 12/240 correct positions. The trajectories still plateaued; the finite result does not exclude better tabu/late-acceptance parameterizations.

True scores are appreciably better than all discovered false candidates. These failures therefore do not demonstrate full-language score overfit. They show that the current consistent-path objective plus two substantially different outer optimizers do not discover these keys from blind starts in the recorded budgets. No exact partial outer key was established by these false outputs.

## Reproduction

Run from repository root:

```sh
clang++ -O3 -std=c++17 batches/double-population-sol61/population.cpp -o batches/double-population-sol61/population
batches/double-population-sol61/population batches/scoring-sol61 ciphers/hcp-399/work/idp/authored-240.txt 20 17 operators
batches/double-population-sol61/population batches/scoring-sol61 ciphers/hcp-399/work/idp/authored-240.txt 20 17 landscape ciphers/hcp-399/work/idp/authored-240.outer-key.txt
batches/double-population-sol61/population batches/scoring-sol61 ciphers/hcp-399/work/idp/authored-240.txt 20 17 blind 619399 40
batches/double-population-sol61/population batches/scoring-sol61 ciphers/hcp-399/work/idp/authored-240.txt 20 17 late 619401 30000
```

For held-out substitute `heldout-240.txt` and its outer-key file, blind seed 619400 and late seed 619402. Capture output in the correspondingly named `*-landscape.log`, `*-blind.log`, `*-late.log` files, then:

```sh
python3 batches/double-population-sol61/validate.py
```

`results.json` compares every complete output against the independently planted controls and independently re-encrypts it. `landscape.json` and `provenance.json` preserve diagnostic statistics and input/model hashes. Logs retain full failed plaintexts and keys for reproducibility.

No actual 399 target run was performed because full blind controls fail. No cipher-family or width exclusion follows. A next advance would need a demonstrably better intermediate invariant/conditional objective, or a representation that handles irregular chunk boundaries and exposes a larger basin, rather than more identical optimizer runs.
