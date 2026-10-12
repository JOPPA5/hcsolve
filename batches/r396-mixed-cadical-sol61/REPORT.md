# 396 mixed widths 21/19/20: exact prefix-path CNF

No full blind-control witness was recovered in this generic irregular-width continuation, so no actual mixed-width target search was run. This is a calibration limit, not an exclusion of the historical cipher or the quoted plaintext. The preceding equal-17 experiment and all earlier reports/timeouts remain unchanged.

The model adapts `batches/r369-mixed-bidirectional-sol61/engine.py` to the 50-letter published 387 quote and an expected-F/literal-P error. Boolean choices enumerate every feasible contiguous readout start for each physical column. Exact-one column choices and occupied-cell covers select a partition. A prefix path tracks preceding columns and preceding long columns, connecting chosen chunks to consecutive states. Forward and backward full-letter endpoint supports join three independent transpositions. An exact-one error selector searches all raw P positions. No key, short-column location, intermediate trajectory, or error position is supplied.

Before full-size search, the width-3/4/3 analogue exhausts all 56 PPPAAAAA-inventory ciphertext permutations, all three common alignments and the one legal progressive alignment. All 448 CaDiCaL195/300 outcomes agree with independent full-key Cartesian enumeration; a separate 224-case Glucose42 audit also agrees. Every SAT model passes independent expected-ciphertext encoding/inverse and raw-literal inverse/re-encoding, with exactly one P/F plaintext mismatch. A separate full-size known-key fixture is SAT and verifies all 50 observed letters. Its true-key assumptions are confined to `fixture.py`; it is not blind recovery and does not open the actual-search gate.

The fresh 50-letter control uses the exact public quote, random independent width-21/19/20 keys, and an expected-F→literal-P injection. Only daily n=19 is supplied in explicitly conditioned calibration. Keys and the error location remain unknown. A successful control would license actual enumeration of common n=1..19 and progressive n=1..18, rather than supplying a historical daily n.

The full control CNF has 382,904 clauses and 4,257 variables, including 2,790 start choices and 351 prefix-path state bits. Construction takes 6.41 seconds and CNF conversion 0.71 seconds. Results are preserved separately:

- CaDiCaL195: UNKNOWN at 500,000 conflicts, 25.88 seconds.
- CaDiCaL300: UNKNOWN at 500,000 conflicts, 28.06 seconds.
- Glucose42: UNKNOWN at its 45.01-second interrupt, approximately 730,583 conflicts; the requested conflict budget was 2,000,000.
- Deeper CaDiCaL195: UNKNOWN at the 90-second worker wall cap, with a requested 2,000,000-conflict budget. The process was terminated, so no completed-call conflict count is claimed.

The deeper run keeps the identical frozen plaintext, ciphertext, n, and model. It changes no seed or hint and does not overwrite earlier outputs. No partial fit counts as recovery. Actual source-union search remains gated on a complete blind-control witness with independent verification of every observed letter.

Evidence includes `exhaustive-audit.json`, `glucose-exhaustive-audit.json`, control input/truth, `control.cnf`, `control-names.json`, `cnf-summary.json`, all backend results/logs, `known-key-fixture.json`, `summary.json`, and `provenance.json`. The [official PySAT API](https://pysathq.github.io/docs/html/api/solvers.html) documents limited-call UNKNOWN and interrupt behavior; no CaDiCaL timer interruption is assumed. Sources, cipher documents, markers, and register entries were not modified.

Reproduce from the repository root using bundled Python 3.12 with `/private/tmp/hcsolve-pysat` and `/private/tmp/hcsolve-z3`: `python3 batches/r396-mixed-cadical-sol61/run.py`, then `glucose.py`, `deep.py`, or `fixture.py` from the same batch.
