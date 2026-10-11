# Complete210-pattern stage21 refinement — failed calibration

This distinct extension enumerates every one of the210possible long/short rank patterns for the65-character21-column stage. For each pattern, Hungarian assigns columns to fixed-height output chunks. It selects the highest whole-text agreement with other stages fixed. Because every physical readout permutation belongs to exactly one such pattern and fixed-pattern assignment is optimal, this is a globally optimal conditional stage21 update; it is not a globally optimal three-stage key search.

The original stage19/20 conditional Hungarian updates and height-pattern flips remain.10% of proposals perturb a single ordinary key swap, including stage21; annealing over the complete three-key state is unchanged. The new bounded budget is60independent uniformly random starts ×1000outer proposals, temperature .15+1.4*(1-(iteration mod1000)/1000). This is a distinct algorithm/budget, not rerunning the old failed stochastic-height search. A stage21 update costs210Hungarian assignments, so outer-proposal counts cannot be equated with the old search's work.

| Control | Status | Outer proposals | Best exact-position agreement | Seconds |
|---|---|---:|---:|---:|
| original independent seed364219201 / quote+R | failed | 60,000 | 45/65 | 31.457 |
| fresh independent seed364219204 / quote+C | failed | 60,000 | 45/65 | 32.123 |

Neither control recovers the complete text or planted key triple; each best witness differs in20ciphertext positions. Complete keys, predictions, inverse texts, mismatch positions, blind seeds and planted fixtures are preserved in results.json and control directories. Independent Python index-map encryption/inversion exactly reproduces the C++ witness and its stated45/65score. Old200×5000 control runs and results remain unchanged in the parent batch.

Separate known-key encoding/current-pattern Hungarian checks give65/65at all stages for both fixtures. `check_full.cpp` checks the new complete210-pattern update with true other-stage keys, giving65/65on the fresh control. This is an encoding/local-step consistency check, emphatically not blind key recovery. No true key is supplied to a search invocation. The previously validated Hungarian implementation is preserved.

No364target was run: the requested strong positive-control gate was not met. These failures exclude neither the21/19/20model nor the conditional cover quote. The quote is still only a normalization hypothesis; fully known control filler is easier than an unknown target filler. No language model, target crib, source correction or truth-driven search adjustment was introduced.

Compile `clang++ -O3 -std=c++17 batches/r364-key-search-sol61/full-pattern/search.cpp -o batches/r364-key-search-sol61/full-pattern/search`; run/resume `python3 batches/r364-key-search-sol61/full-pattern/controls.py`. Resume skips preserved search outputs. The initial completed search process encountered a reporting-only repository-root path error; it was corrected and resumed without rerunning either search. run.log preserves that failure and resume.log the completed report. manifest.json records settings and source hashes. Only this subdirectory was written; no process remains, no source or marker changes.

A concrete remaining structural opportunity is a joint update of the19/20stages: improving only one stage while fixing the others can leave a high-agreement false basin. Exhaustively adding75,582height patterns for19 and15,504for20would be much more expensive and is not demonstrated to overcome that coupling; it was not attempted or portrayed as a recovery method.
