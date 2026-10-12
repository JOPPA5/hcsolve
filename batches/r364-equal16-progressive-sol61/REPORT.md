# Corrected equal16 progressive R triple

No historical key was recovered. All14 legal **progressive** alignments n,n+1,n+2, n1–14 without wrap, are exact **UNSAT** for three ordinary irregular columnar stages of width16, corrected EXCUV/EXCVU as a finite ciphertext union, omitted original group3 ITPKA, and the visible reply's64-letter four-sentence-X template with a fifthX at any boundary.

This is a genuinely separate remaining case from `batches/r364-equal16-corrected-sol61`, whose16 constant common alignments were already tested. It does not repeat the obsolete ERCUV-input test, change glyphs by expected prose, or exclude unequal-width R, other preparation or another plaintext.

## Blind control recovery

Three fresh independently shuffled key triples use the same65-letter quote-pattern preparation, with extraX at0,37,64. The input files contain only the64-letter template, two finite U/V ciphertext alternatives and the legal progressive family; **true n and keys are absent**.

`run.py` searches the declared n1–14 cases in ascending order and selects the first SAT witness. The full blind witness is saved and hashed before its quarantined truth file is read for audit. It recovers hidden n10,1,14 respectively. All three return the exact planted65-letter plaintext and ciphertext alternative, with complete independent physical-position encoding and inverse column filling. Every earlier tested n for that fixture is exact UNSAT, not a timeout. Complete trials, witnesses, audits and hashes are preserved.

Individual successful SAT checks took1.59,0.34,0.96s. The total blind search also includes the preceding failed rank cases. Alignment was supplied as an enumerated **case condition**, never selected using its planted value. These controls establish recovery for the tested fixtures, not uniqueness of all possible keys or insertion positions.

## Exact mechanics and finite audit

The engine is byte-identical to the faithful pruned equal16 engine. At N65 =4*16+1, physical column0 is the only long column. Each stage's supplied case rank fixes its complete length pattern, so exact-cover choices are restricted to actual chunk boundaries. In the progressive family the three patterns differ as specified; complete original coverage and rank constraints remain.

An independent audit enumerates all56 insertion/keyset combinations for the analogous N7/w3 progressive1,2,3 family. All20 positive and same-inventory negative cases, including unknownX insertion and U/V union, agree. This is a finite-domain mechanical audit, not exhaustive enumeration of historical16-column permutations.

## Conditional target results and limits

All14 corrected target cases finish in0.08–2.62s, with zero SAT and zero UNKNOWN. Every case simultaneously admits both EXCUV and EXCVU; no expected plaintext selects U/V. The source-motivated fixed-endX preparation is included as a subset of free insertion and needs no redundant rerun.

This closes only the stated equal16 progressive/no-wrap branch. Common equal16 negatives are documented separately. Arbitrary independent alignment ranks, wrapping conventions, unequal widths21/19/20, another preparation/indicator omission, remaining source alternatives and another plaintext are not excluded. The quoted reply is visibly published on the cover and is a disclosed known-plaintext hypothesis, not an AI decipherment.

## Reproduction

From repository root:

```
python3 batches/r364-equal16-progressive-sol61/generate.py
python3 batches/r364-equal16-progressive-sol61/audit.py
python3 batches/r364-equal16-progressive-sol61/run.py
```

Generation is deterministic with fresh seeds617364161901–903. `run.py` resumes saved trials and does not restart completed attacks. Existing Z3 at `/private/tmp/hcsolve-z3` is required. Scripts/models, complete trials, independent checks and source hashes remain in this batch. Original sources, cipher files, state markers, watchers and reviewers were unchanged by the searches.
