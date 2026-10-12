# HCP364: direct triple-key endpoint constraints

The target remains unresolved. This batch tests a new exact representation for three ordinary irregular columnar transpositions at the primary worked-example widths 21/19/20. It does not repeat a width sweep or increase the prior solver budget. The plaintext visible on the cover is a disclosed conditional known-plaintext lead, not a newly deciphered message.

## New representation

Each physical column selects one admissible start of its complete 3- or 4-letter chunk. Exact-cover constraints pack each intermediate stream without overlaps or omissions. Both intermediate character arrays and letter-occurrence trajectory variables are eliminated.

For each source letter and first-stage selected start, its first output position is fixed. Each second-stage selected start then fixes its third physical column and row. A direct Boolean clause permits only third-stage starts placing this letter at a matching final ciphertext occurrence. The fresh65 case uses 3,373 start selectors and 201,921 forward endpoint clauses.

The substantive second version adds reverse endpoint support: a third-stage start and second-stage interval covering its source position permit only first-stage starts that reach the same known source letter. This adds 208,467 clauses in the fresh full-alphabet control. These are redundant constraints for propagation, not a relaxed or altered cipher model.

The source-grounded third version additionally imposes one common **unknown** readout rank for physical column zero, as in the primary R alignment convention. Selected intervals advance a boundary rank by one, and all three physical column-zero starts share a rank variable. The control is generated with this convention but its planted rank is not supplied. It does not assume the target header fixes n=11 or any other value.

## Controls and boundaries

- Fresh independent full-alphabet65 control, arbitrary unknown21/19/20 keys: forward formulation UNKNOWN after60s (build12.99s).
- Same preserved fixture, new reverse-support algorithm: UNKNOWN after60s (build28.32s). No truth key supplied.
- Fresh independently encrypted quote-pattern65 control, unknown generic triple keys: UNKNOWN after60s (build49.82s).
- Fresh independently encrypted quote-pattern65 R control, common unknown alignment: UNKNOWN after60s (build36.02s).

Both unrestricted representations agree with independent exhaustive encryption over all288 key triples in20 small7-letter cases. The common-rank representation agrees with all24 admissible triples in20 separate small cases. Positive and same-inventory negative cases are included. These audits test the model in the finite small domain; they do not prove useful search performance at historical widths.

Fresh quote controls use the prior64-letter four-sentence-X template with one extraX at an independently chosen position. Their prepared plaintext is supplied in full, making them easier than the target's unknown fifthX insertion. A successful known-insertion control alone would not silently validate an unknown-insertion target model.

No historical target was submitted before a positive matching control. UNKNOWN is neither UNSAT nor evidence against historical R, the quote interpretation, or another preparation. Cipher sources and state markers remain untouched. Root independently confirmed the rendered portal status Not solved/Unsolvable on2026-10-11; this status permits investigation and is not a cryptanalytic result.

## Reproduction and credits

From repository root:

```
python3 batches/r364-triple-next-sol61/small-audit.py
python3 batches/r364-triple-next-sol61/reverse-small-audit.py
python3 batches/r364-triple-next-sol61/r-small-audit.py
python3 batches/r364-triple-next-sol61/controls.py
python3 batches/r364-triple-next-sol61/reverse-control.py
python3 batches/r364-triple-next-sol61/quote-control.py
python3 batches/r364-triple-next-sol61/r-control.py
python3 batches/r364-triple-next-sol61/rank-small-audit.py
python3 batches/r364-triple-next-sol61/rank-control.py
python3 batches/r364-triple-next-sol61/linked-rank-small-audit.py
python3 batches/r364-triple-next-sol61/linked-r-control.py
```

Requires the existing local Z3 installation at `/private/tmp/hcsolve-z3`. Fixtures and planted keys are saved separately; search runners receive plaintext/ciphertext and declared structural assumptions only. A SAT witness is explicitly gathered through all physical columns and independently inverted over every position before acceptance.

Primary encoder semantics were independently verified against HistoCrypt2020 Figure5 in `batches/r-primary-example-audit-sol61`. Prior exact-cover formulations and failed Hungarian/trajectory searches were read in `batches/r364-primary-sol61`, `batches/r364-key-search-sol61` and `batches/r364-coordinate-main`. Corrected EXCUV/EXCVU and free fifthX double-width16..22 exclusions remain in `batches/r364-corrected-double-sol61`; this batch makes no new double or triple exclusion.

## Incremental alignment partition

A native finite-domain SAT version retains one compiled model and tests each of19 possible shared ranks with independent Boolean assumptions,8s per rank, preserving learned clauses across cases. This is a source-grounded decomposition rather than extending one monolithic timeout. The native interface initially rejected a bit-vector equality used directly as an assumption before any search; Boolean guard implications replaced it. The corrected incremental version again passes20 finite small cases against all24 common-rank triples. The original rejected run is preserved in rank-control.log. The corrected control search in rank-control-native.log returned UNKNOWN for every rank1–19 at8s each (152.09s total; build38.81s). This is no negative result for any rank.

## Explicit physical-column-zero start/rank support

The common-rank formulation linked column-zero starts to rank only through boundary increments. A direct redundant relation was therefore added: for each selected physical-column-zero start a and shared zero-based rank r, require a = q*r + k, where k is a feasible number of other long columns preceding column zero. Complete boundary-rank increments remain in place; the new relation is necessary propagation, not a substitute for exact rank. The linked version passes the same20-case exhaustive24-key aligned audit. The matchedR control in linked-r-control.log returned UNKNOWN after60.02s (build29.25s). No target was run.

Correction to progress interpretation: the fresh matchedR control starts N in both plaintext and ciphertext. The target's N/I contradiction at rank1 does not apply to that control. An earlier progress message incorrectly described its rank1 timeout as failure to propagate an easy contradiction; that interpretation is withdrawn. The direct rank/start link is independently valid as necessary redundancy, without that diagnostic claim.

## Final bounded outcome

No full65-letter control witness was recovered by the forward endpoint formulation, mirrored support, common unknown alignment, incremental rank partition, or explicit rank/start support. Thus this branch has no justification for a target key search. All failures remain UNKNOWN, no actual key/plaintext is claimed, and no model family is excluded. The model audits establish correctness only in their finite small domains. No identical annealing restart or width sweep was added. Completed runs leave no active search process.
