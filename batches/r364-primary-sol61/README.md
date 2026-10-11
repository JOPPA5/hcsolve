# HCP364 conditional primary-width exact tests

Writes only this batch. Cipher directories and the earlier constraint batch are read-only. No watchers, markers, reviewer or published target answers.

The published R example independently checked in `batches/historical-context/verify-r-example.py` uses widths 21, 19 and 20 in that order. These dimensions are evidence for a historical example, not proof of the 1944 target's dimensions or keys. The original example's specific keys have already been tested elsewhere and are not repeated here. This batch instead models arbitrary column-read permutations at those three widths, with daily alignment constraining the readout rank of physical column 0. Constant n is 1..19; progressive n,n+1,n+2 is 1..18.

`exact_cover.py` is a preserved copy of the prior exact Boolean encoding. Each input column selects a possible fixed output chunk start. Every input column selects exactly one; every output position is covered exactly once. Selected chunks copy the appropriate character cells. Readout-path rank labels impose the daily alignment. Intermediate inventory bounds are redundant but aid pruning. The necessary saturated inventory pruning of raw omit3 remains intact.

Reproduce the 37 independent fixed-key encoding checks:

```
python3 batches/r364-primary-sol61/check_all_alignments.py
```

Reproduce new independent blind controls and bounded exploratory target sweep:

```
python3 batches/r364-primary-sol61/run_primary.py
```

Both scripts append JSONL; use separate fresh output paths to avoid mixing reproduction records. Fixed-key checks validate constraints and full reencryption/inverse, not blind key recovery. The fresh 65-letter control plaintexts and keys are independent of the hypothesized target quote. Blind controls each have 60 seconds; all 74 target cases each have 60 seconds, exclusive of encoding construction.

Target assumptions: the visible source quote is actual prepared plaintext; four sentence-end X characters; arbitrary last filler; omitted five-letter group 3; these widths and constant/progressive alignment convention. Raw reading permits at most three substitutions, with inventory deficits already saturating the budget. A separate explicit historical glyph variant permits zero substitutions. All are unproved hypotheses. SAT is a conditional witness requiring full independent inversion/reencryption and a blocked-keyset alternative check. UNKNOWN proves no exclusion. A bounded substitution witness is not exact equality to the literal source; differences must be disclosed.

The initial serial run completed five target cases, then was stopped only to change scheduling. One uncompleted case had no result and is not treated as a finished test. `resume_targets.py` reads all completed `(mode,n,reading)` records, skips them and runs only the remaining independent cases with four workers and unchanged 60 s per-check bounds. All completed serial records remain in the same append-only results file. Resume with:

```
python3 batches/r364-primary-sol61/resume_targets.py
python3 batches/r364-primary-sol61/summarize.py
```

`summary.json` is a snapshot, with explicit completion flag and expected 74 cases. Never present an incomplete snapshot as a full sweep.
