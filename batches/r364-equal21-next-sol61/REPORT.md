# Equal-width21 closed-form R triple: calibration

HCP364 remains unresolved. This is a structurally different exact model at length65 and width21, where only physical columns0 and1 have four letters; the other19 have three. It is not an unsupported small-width sweep or increased timeout on the old interval model.

For physical column c with readout rank r_c, its output starts at

```
start(c) = 3*r_c + [r_0 < r_c] + [r_1 < r_c].
```

The source-grounded common alignment requires r_0 equal in all three stages; the progressive alternative uses n,n+1,n+2. n remains unknown, with no header-derived value or planted key supplied.

## Two representations

`closed.py` uses explicit ranks and inverse permutation variables with CP-SAT AddInverse. Two comparison indicators compute every start directly. Element constraints copy complete physical columns and exact intermediate inventories propagate letters. There are no general packing intervals. A supplied strategy names the common rank and each stage's second exceptional-column rank first; the default automatic portfolio does not guarantee that order for every worker.

`native.py` uses Boolean permutation matrices. A one-hot common alignment gives the first exceptional rank; independent physical-column1 selectors give the second. Prefix-before indicators gate copies at offsets0/1/2. This removes rank arithmetic and variable Elements while preserving exactly the same two-long-column formula. Intermediate inventories remain exact.

Both represent every ordinary column order in the declared common/progressive family. Sorting column ranks yields the keys; every SAT witness must independently gather all65 physical positions, match a declared ciphertext alternative and invert back to the full supplied plaintext.

## Fresh control and audit

The fresh65 control is independently encrypted from the conditional visible reply's four-sentence-X64 template plus a finalX. This fixed-end padding is a source-motivated hypothesis, not a recovered historical preparation. Three independent mixed permutations share a random unknown rank. Only plaintext/ciphertext enter the solvers; planted keys and alignment are quarantined in control-truth.json.

CP-SAT returns UNKNOWN after60.00s (484,282 branches;12,328 conflicts). The native Boolean model also returns UNKNOWN after60.02s (build0.65s). No historical target has been run under failed whole65 calibration.

Both representations independently agree with20 finite small cases against all32 admissible key triples (24common,8progressive) for the analogous two-long-column case N8,width3. Positive and same-inventory negative cases are included. These audits establish the tested small-domain mechanics, not historical-width performance.

The fixed-endX control is easier than the prior free fifth-X formulation. Even a future fixed-end target UNSAT would not exclude arbitraryX insertion, other preparation, unequal widths21/19/20 or the whole R family. A SAT key would establish a conditional known-plaintext witness, not discovery of the already visible quoted reply.

## Reproduction

```
python3 batches/r364-equal21-next-sol61/audit.py
python3 batches/r364-equal21-next-sol61/native-audit.py
python3 batches/r364-equal21-next-sol61/control.py
python3 batches/r364-equal21-next-sol61/native-control.py
python3 batches/r364-equal21-next-sol61/pattern-first-audit.py
python3 batches/r364-equal21-next-sol61/pattern-first-control.py
python3 batches/r364-equal21-next-sol61/trajectory-audit.py
python3 batches/r364-equal21-next-sol61/trajectory-control.py
```

Dependencies are the existing OR-Tools installation at `/private/tmp/hcsolve-ortools` and Z3 at `/private/tmp/hcsolve-z3`. Source encoder semantics are independently checked in `batches/r-primary-example-audit-sol61`. The neighboring one-short equal17 models by GPT-6.1 Sol were consulted by agent message for comparison; they are not copied or rerun. Cipher/source files, state markers, watchers and reviewers remain untouched.

## Forced exceptional-pattern search

A third bounded calibration explicitly sets CP-SAT FIXED_SEARCH with one worker. Shared column-zero rank and all three column-one ranks are assigned before ordinary column ranks; remaining ranks use minimum-domain selection. This searches the two-long-column patterns first instead of relying on automatic portfolio choices. It receives the same blind control pair, no planted pattern or key. Its20-case finite exhaustive audit passes. The first invocation rejected an incorrect local enum name before solving; `CHOOSE_MIN_DOMAIN_SIZE` fixed the API name. That pre-search error remains in pattern-first-control.log. The corrected fixed-pattern-first control returns UNKNOWN after60.00s (140,112 branches;45,330 conflicts).

## Closed-form occurrence trajectories

A fourth representation removes intermediate character variables entirely. Each source occurrence passes through the closed-form rank transform. Intermediate positions are AllDifferent, final domains include every observed occurrence of the same letter, and final AllDifferent preserves complete occurrence matching. Source position div/mod21 selects a rank through a21-entry Element; two comparisons add the exceptional-column offsets. This uses no packing intervals or65-entry character Elements. Repeated letters are not artificially matched to one chosen occurrence. The model agrees with the same20 finite exhaustive cases/all32 common/progressive key triples. The closed-form trajectory control also returns UNKNOWN after60.03s (905,234 branches;77,136 conflicts).

## Bounded outcome

One fresh blind65 fixed-endX control was evaluated by four substantively different representations/search strategies. None recovered a whole key: all return UNKNOWN at their60s limits. This is no negative result for the actual ciphertext or the declared family. No historical target, free-insertion target or progressively aligned full65 control was run. No repeated random restart volume or widened timeout was added.

The known quote is supplied control plaintext; no planted alignment, exceptional ranks, permutation keys or intermediate text enter a solver. All four finite model audits use the same20 small test pairs against all32 exhaustive key triples and must not be presented as80 independent tests. Completed runs leave no active search.
