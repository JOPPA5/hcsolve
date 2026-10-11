# Independent proposed-content key audit

Both proposed full keys pass an independent physical adjacent-hole walk against the frozen `pixel-strong` source variants. The decoder reproduces each proposed raw prepared string exactly, all385 letters; an independently inverse-indexed encoder reproduces each full385-letter ciphertext exactly. A second unwrapped-coordinate calculation with the old crop key and explicit lexical relabeling produces the same strings. No plaintext cleanup or I/J merger is applied.

Each ring is a complete26-letter permutation. Each physical mask has23 distinct selected stops; consecutive adjacent walks visit all52 holes exactly once and sum to179. Starting full hole47 is exactly a rotation by3 of the previously language-recovered cropped physical masks. The first20 presses advance162, residue6, so `Pfull[k] = relabel(Pcrop[(k+162) mod26])` exactly reproduces the proposed input ring. Both output rings match the recovered output ring.

The relabeling G→X, Q→G, X→J, unused J→Q is explicitly checked. Old J occurs zero times in both full385 decoded strings, so its compensating replacement preserves a26-letter permutation without changing any observed character. This is a semantically selected rare-letter interpretation, not a uniquely selected language-model key or independent proof of the historical preparation rule.

The first5 raw decoded letters remain `usmmf` and `uitlf`. Their meaning is unresolved. The raw prepared strings contain word-internal I where an editorial reading may use J, and residual letter discrepancies; the audit does not normalize them or claim that an historical I/J rule has been established. The source variant itself has glyph uncertainties. Exact reencryption verifies consistency of the proposed key and variant, not that every glyph reading, preparation choice or historical machine attribution is proved.

Reproduce with `python3 batches/kryha-content-audit-sol61/audit.py`. Detailed step-by-step displacements/arcs, complete raw strings, comparisons and source hashes are in `verification.json` and `provenance.json`. `350-raw-prepared.txt` and `351-raw-prepared.txt` preserve exact literals; corresponding `*-reencrypted.txt` files preserve the inverse check. No cipher directory, source, marker, watcher or reviewer was changed/started.

## Revised collated default and document check

The later source-backed351 correction at one-based240 U→J was independently visually checked against the literal IIHUJ crop. With the unchanged physical/ring key, only prepared240 D→E changes, yielding LACNEISIA. The separate obscured231 L→I alternative changes only prepared231 I→S, yielding EXISTUIE. This is source collation, not physical refitting. The respective aligned-interior discrepancy counts are5 and4. Original strong outputs remain archived.

`audit_j_correction.py` records exact source/prepared edits, source crop hashes, full385 reencryption and literal alternatives. `audit_canonical.py` confirms byte-for-byte equality of the final canonical default and collated-moderate ciphertexts with independently audited variants, unchanged functional keys, successful standalone decryptor commands, exact prepared-plaintext files and exact literal385 strings in both SOLUTION drafts. Draft hashes are saved in `canonical-verification.json`.

The final drafts now explicitly identify supplied O/ΔK in the language-stage controls, one-hole mask difference0→48, nonunique semantic rare-label choices, damaged351 opening and archived/collated source variants. These descriptions agree with the saved control/search/audit evidence. This is a solver-team consistency audit, not the pending independent Claude review. First5 and the historical preparation rules remain unresolved; no source or cipher file was edited by this audit.
