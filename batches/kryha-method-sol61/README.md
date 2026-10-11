# Primary Kryha attack reconstruction

Scope: primary cryptanalytic methods, no HC target solutions. Sources and cipher directories are read-only; no markers, watchers or reviewer. This batch reconstructs a structural output-ring attack, not a decipherment of a historical target.

Run the independent fresh control and structural verification:

```
python3 batches/kryha-method-sol61/control_and_isomorph.py
```

Run the transferable solver alone, providing a JSON list of ciphertext strings and a hypothesized common-prefix length:

```
python3 batches/kryha-method-sol61/isomorph_solver.py batches/kryha-method-sol61/control-ciphertexts.json 40
```

The solver consumes only ciphertexts and the common-prefix hypothesis. It does not read planted plaintext, rings, mask, stop count, geometry, initial shifts or a language model. Its output is the possible normalized output rings under that hypothesis. An empty set refutes that exact hypothesis, not Kryha generally. More than three finite-field degrees of freedom is reported as underconstrained without enumeration. Normalization O[A]=0 removes global translation; multiplicative decimation ambiguity remains.
