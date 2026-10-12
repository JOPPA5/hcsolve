# Independent physical-wheel validation of373 published tail

GPT-6.1 Sol,2026-10-12. Published Solved373 supplies known contextual plaintext for unresolved374; this is not a new discovery of its message content. The generic mixed-ring tail witness `../kryha373-tail-sliding-sol61/SAT-(2, 462, 23).json` is held completely frozen: P/O ring positions,23 schedule residues, and beta. No word, glyph, key or physical distance is changed to obtain this fit.

**Exactly one ordered23-hole mask fits the known179-distance52-hole wheel:**

`26 29 31 34 37 40 42 44 45 47 48 49 51 2 4 5 8 11 13 17 20 21 24`

These are zero-based physical hole indices, in positive cyclic order from the fitted tail's first stop. Initial relative displacement beta17. Input/output rings and K are fully preserved in summary.json; P[letter] and O[letter] map alphabet indices to physical slots. P[A]=O[A]=0 is the recovered two-ring gauge, not a claim about historical alphabet positioning.

Adjacent stop arc distances:

`11 7 10 10 10 7 8 3 6 4 3 7 12 7 3 10 11 6 14 10 3 10 7`

They sum179 exactly. The forward residue constraints are K[j+1]−K[j] modulo26 and final K[0]+179−K[22] modulo26. All minimum positive residues are positive and already sum179, so adding even one26-distance lift would violate one physical revolution. General DP nevertheless enumerates all52 starts and all monotonic23-stop paths ending after exactly52 adjacent edges. An independent coordinate-translation audit of the minimal residues obtains precisely the same single mask. This uniqueness is relative to this geometry, sign convention and frozen K; it is not a general historical key-uniqueness claim. Reversing both unrestricted mixed rings is the familiar equivalent gauge/direction model, not a second recovered positive mask for the unchanged rings.

The independent encoder physically walks adjacent wheel edges to the next selected stop. It reproduces **all186 positions of the generic encrypted tail**, and encodes/inverts all183 nonerased source positions exactly. Among all186 literal source positions there is only one mismatch: source504 literalE versus predictedA, already in the declared watermark erasure set. Erased478/479 happen to match. Consequently literal186 reencryption/inversion is **not** claimed as exact. The archive/source remains unchanged; masks.json retains literal cipher, predicted physical cipher, literal decoded text, published prepared text and every mismatch. The fit begins at zero-based source offset462 (one-based463), not at source start. A full650 source/preparation check remains the parent's independent task.

This validates a concrete programmable physical-wheel realization of the frozen generic tail key. It does not establish message-first phase, the meaning of initial symbols, exact numeral/quotation preparation, every rare ring label, or transfer to374. Input labels unused by the fitted tail are recorded in independent-coordinate-audit.json; the saved full permutation completes them, but this fit alone does not independently recover their names. The generic solver's control calibration is preserved in its original batch and is not repeated here.

Reproduce:

```sh
python3 batches/kryha373-physical-tail-sol61/run.py
```

DP enumeration/results, exact whole186 physical walk, input hashes and source geometry are retained. Only wheel52.json distances are used. No cipher/source/docs/markers/reviewer/watch modifications occurred; the failed366/368browser path was stopped. No pending process remains.
