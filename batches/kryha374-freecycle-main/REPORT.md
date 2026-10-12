# HCP374 context: alternative cycle displacement

Published Solved373 remains archival context for unresolved374; no new373 solution is claimed. All source words, amended/unamended D, natural J/I, optional Q wrappers, source glyph53 L/I and90 E/A, and omit0/5 branches are explicitly preserved. There are12 distinct preparations after deduplication.

The earlier ring model fixed the full-cycle advance to179 (23 modulo26). This extension asks whether another constant cycle residue could fit the stated prefix with arbitrary permutation alphabets and unrestricted per-position displacement K. It does not enforce a physical wheel or establish Madrid's machine.

The first implementation with an unknown cycle variable failed a fresh97-letter blind control within10s; no target was run under that failed implementation. Its controls/log are preserved as variable-D-*. A fixed-residue implementation separately calibrated residues0,2,13,23. Residue2 and23 controls returned complete matching encoders; residues0 and13 timed out10s. A separate unused-alphabet ordering symmetry reduction also timed out30s on both failed controls; it did not run targets. These are solver limits, not ciphertext exclusions.

The successfully calibrated NEW residue2 class yielded4896 exact UNSAT cases in43.90s:12 preparations ×2 alignments ×4 glyph branches ×51 periods2..52. No SAT or UNKNOWN. Independent recurrence-based forward and inverse checks verify every fitted character of both positive controls; control-audit.json. The target test uses only residue2, not the failed0/13 classes.

Multiplication of P,O,K and the cycle residue by a unit modulo26 preserves permutation alphabets and the entire encryption. Consequently residue2 represents all nonzero even residues except13 (i.e. those with gcd(residue,26)=2). The ordinary unit-residue class is equivalent to23 and was tested separately in earlier batches. Residue0 and13 remain outside this calibrated target test. A different preparation, source error, framing or noncyclic stepping also remains open. No key was recovered for374.

Reproduce: `python3 batches/kryha374-freecycle-main/run_fixed.py` followed by `python3 batches/kryha374-freecycle-main/audit.py`. The failed variable-D and degenerate calibrations have separate scripts and logs. No sources, markers, reviewer or register entries changed.

## Completion of degenerate-cycle calibrations

The audited finite-active-coordinate helper subsequently removes unusedalphabet symmetry without changing the algebraic family. The originalD0/D13 matched controls, previouslyUNKNOWN10/30s, nowSAT by exact26- and13-assignment spaces;D2/D23controls alsopass. Separate recurrence encoder/inverse checks verify97/97/96/96characters respectively; finite-controls.json andfinite-control-audit.json. No truekeysenterfit, and rawringuniquenessisnotclaimed.

Afterpositivecalibration, NEW residue0 and13 sourcecases werecompleted:9792exactUNSAT,zeroSAT/UNKNOWN,in207.33s. Twelvepreparations,omit0/5,fourglyphbranches,periods2..52areexplicitlyenumerated foreachresidue. These are the two previouslyuntested residueclasses,not repeats ofD2targetcases. Originalfailedcontrol/timeoutsarepreserved. Reproducewithfinish_degenerate.py; resultsdegenerate-actual.json/degenerate-summary.json.

Underarbitrarypermutationrings, multiplicationbyunitsmod26 groupscycle residues into fourclasses representedby0,2,13,23. This batchnowexcludesallfourclasses onlyforitsstatedsourcepreparations,glyphs,periods,omit0/5,andconstantcyclic stepping,usingtheearlierordinary179/unit-classsourcechecksasattributedseparateresults. Other offsets, errors, transformationsorirregular steppingremainopen. No physicalwheel identificationornew374plaintextfollows.
