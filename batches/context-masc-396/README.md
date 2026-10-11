# Explicit context-crib MASC test of HCP396

No plaintext recovered. This is an independent main-solver context hypothesis test, not published-solution lookup. The preserved portal metadata says request for repetition; the scan refers to another telegram. Neither supplies the encrypted body verbatim. phrases.json records33 entries (32 distinct) plausible request/digit formulations written by the solver; none is asserted present. A potential single indicator group, C/O reading and reversal are explicit separate conditions. No immutable source was altered.

A bijective repeated-letter-pattern check considers every offset of every phrase in the whole55-character body and every one-group omission. It finds84 compatible phrase/offset/reading conditions, largely short fragments and variants of the same mapping. Every incompatible match is excluded only under the exact literal phrase, transcript and unchanged-order monoalphabetic transform. Compatibility is no proof that the phrase occurs.

The locked engine adapts batches/short-masc/mono.cpp with credit in its source:32 deterministic random bijective completions per conditional mapping,20000 proposals each, full frozen Slovak TRAIN3/4/5gram score .15/.4/.8. All crib mapping entries remain locked; the previous blind unlocked stage is disabled. No other target wording is supplied. Unused mappings are arbitrary completions and are not identified.

Known-plaintext calibration deliberately supplies ONE15-character substring, offset5, of each of the previously genuine heldout Slovak55/65 controls. It does not use the planted key or any other truth in optimization. These are reused controls, not fresh independent blindness. The65 control recovers entire text at rank0; the55 control fails, consistent with its unusual historical title and earlier scoring/search failure. This is a limited conditional calibration, not general short-Slovak recovery.

All84 actual compatible conditions were attempted.172 distinct full candidate keys/texts independently decode and re-encrypt the respective entire literal/conditional input, and preserve every locked crib mapping. Leading complete texts were inspected; none is coherent. Familiar supplied phrases are forced by construction and therefore carry no independent evidence for decipherment. The failed55 control and finite phrasing forbid a MASC-family exclusion. No solution, marker, reportPDF or register entry.

Reproduce from root:

```
clang++ -O3 -std=c++17 batches/context-masc-396/locked.cpp -o batches/context-masc-396/locked
python3 batches/context-masc-396/run.py
python3 batches/context-masc-396/targets.py
```

Full source context: ciphers/hcp-396/source/metadata.md; method/encoder credit: batches/short-masc/README.md and mono.cpp. Frozen model provenance: batches/scoring-sol61/. Controls and172 fullactual keys/texts saved in controls.json and targets.json. All transformations verified by the independent Python assertions in run.py.
