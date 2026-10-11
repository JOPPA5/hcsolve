# HCP-364 — unresolved

No key has been recovered, and no command currently deciphers the message. The corrected ciphertext inventory strongly supports the visible reply as a transposition crib; inventory agreement alone does not prove the encryption mechanism or a complete solution.

The source is the Slovak diplomatic record described in `source/metadata.md`, acquired through the rendered HC Portal. Its displayed status is Not solved, with an Unsolvable tag. The scan includes an unencrypted proposed reply and outgoing ciphertext; the missing-number complaint refers to the incoming telegram, so that complaint alone is not an impossibility proof for this ciphertext.

## Literal working transcription

The original working transcription was:

```text
1170
ixrii dvsbo itpka viloo xxyen ecdie lpill
tsmnd tuute cloen sxtrd ercuu pdaot xkoms
```

The body has 70 letters. Header 1170 is preserved separately and has not been established as a key. Some I/L, M/N, C/E and U/V glyph alternatives remain; see NOTES.md. Source files are unchanged.

## Correction after the outside batch review

Claude's outside batch review identified three glyph corrections, subsequently checked against the scan: group 8 `TSNND`, group 10 `ELOEN`, and group 12 `EXCUU`, with the final two U/V glyphs ambiguous. This supersedes the corresponding readings above. The original source files remain unchanged. The earlier claim of independent agreement on the original transcription is withdrawn: it did not provide reliable confirmation of these letters.

With exactly one of group 12's last two letters read as V and group 3 `ITPKA` removed, the remaining 65-letter inventory equals the visible reply's 60 accent-free letters plus five X characters. Both UV and VU must remain possible. This is a strong known-plaintext lead, not an independently deciphered plaintext. The position of the fifth X is unknown.

All older target exclusions below refer to their stated, now superseded input branches. They do not exclude the corrected ciphertext. Fresh tests consider both U/V placements and every possible insertion position of the extra X; their evidence is recorded in `batches/r364-review-collation-sol61/`. No corrected target key has yet been verified.

## Tested hypothesis and evidence

The visible proposed reply, “Nelúštiteľné. Neudal si číslo pred textom. Viď bod tri pokynov. Uveď číslo.”, supplies a conditional crib. It is not a decipherment. Testing its 60 accent-free letters with four sentence-end X characters and one unknown filler, one removed five-letter indicator, ordinary single columnar transposition of width 2–22, forward or reversed ciphertext, and up to three substitution errors gave zero matches across 588 complete cases.

The matching-length synthetic width-21 control, including three injected errors, recovered its exact planted key. The result rejects this particular preparation under this particular single-columnar model. Other plaintext preparations, multistage systems, different plaintext and larger transcription errors remain untested.

## Reproduction

From repository root:

```sh
python3 ciphers/hcp-364/work/known_quote_test.py
```

This reproduces the control and conditional rejection in `work/known_quote_results.json`; it does not produce decrypted target plaintext. No published solution was used. No DONE or register entry has been created because the message remains unresolved.


## Continued attempts

Single-columnar tests now cover all16 subsets of optional sentence-endX markers and unknown suffix padding,9,408 cases total, without match at <=3substitutions. Run `python3 ciphers/hcp-364/work/preparation_variants.py`.

An exact Z3 model recovered independent double16/17 keys; alternative Boolean exact-cover encoding also recovered triple13/13/13 control keys. Inventory pruning then rejected rawtarget double16/17 under the fixedfour-X quote preparation, omit3 and <=3errors. It does not establish the quote as ciphertext plaintext, glyph corrections, or actual system. Search across wider double/triple families continues in batches/constraint-sol61. Full evidence and limitations are in NOTES.md. No key/targetplaintext/DONE exists.


## Exact multistage quote checks (main synthesis,2026-10-11)

IndependentBoolean exact-cover double-transposition controls passed all49ordered width16–22pairs; both targetreadings were UNSAT in all98conditional cases. Equal-width16triple with all16possible sharedrotations recovered control plaintext/keys and gave32UNSATtargets. Unrestricted13³blind control recovered keys; bothconditionaltargets UNSAT. Unrestricted11³glyphreading UNSAT, raw≤3UNKNOWN. Otherblindcontrols12/14/15 and17–22 timedout; this is a solverlimit, not ciphertext exclusion.

A distinct unequal16/17/18 sharedn11 control recovered exactkeys in59.38s. Both conditionaltargetreadings remained UNKNOWN after600s each. Exploratory equal17–22sharedn11 targetcases all12 UNKNOWN60s. Sixknown-key encoding checks SAT only validate encoding, notblindkeyrecovery and nottargetsolutions. These targettests all assume the visibleproposedreply as plaintext, omitindicatorgroup3, fixedsentenceXpreparation, and particularliteral/glyph/errorbranches. Noactualkey orplaintextwitness. Model-conditioned UNSAT is not a claim of historicalunsolvability.

Fullscripts/logs/reproduction and explicitassumptions: `batches/constraint-sol61/SUMMARY.md`, `double-sweep-tight.jsonl`, `regular13-targets.jsonl`, `sustained-unequal.jsonl`, `exploratory-equal-targets.jsonl`. Furtherlowwidthgeneric cases mayappendthere. NoDONE orregister.


Lower genericwidth extension: unrestricted equaltriple2–9 bothreadingbranches UNSAT; width10glyph UNSAT/rawUNKNOWN60s;12/14/15bothbranchesUNKNOWN60s. Nineindependentblind2–10controls pass; independentbruteforce2–4 confirms6UNSAT. Known-keyencoding checks for12–15areseparatefromblindcontrolfailures. These smallerwidthsaregenericalternatives, not documentedRwidths. Evidence: `batches/constraint-sol61/small-width-summary.json`. Assumedquoteandpreparationlimitations remain.


## Corrected-input double-columnar check

The fresh check in `batches/r364-corrected-double-sol61/REPORT.md` supersedes the older ERC-input double tests for this precise model. Both corrected EXCUV/EXCVU alternatives were encoded together, group 3 was omitted, and the fifth X could occur at any position in the four-sentence-X quote template. All 49 ordered width pairs 16–22 returned exact UNSAT in less than 1.4 seconds each. Three independently encrypted fresh blind controls recovered their full 65-letter plaintexts, with independent encoding and inversion checks.

This excludes only these two ordinary irregular columnar stages, these widths, this conditional quotation preparation and these source alternatives. It does not exclude historical R triple transposition, other preparation, or another plaintext. No key was recovered. Reproduce with `python3 batches/r364-corrected-double-sol61/run.py`.
