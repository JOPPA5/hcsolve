# HCP364: corrected unequal16/17/18 branch

This records a previously untested source-corrected branch. The old sustained600-second tests used ERCUV/ERCUU; they do not cover the independently collated EXC prefix. This batch uses **EXCUV/EXCVU as a finite union**, removes group3ITPKA, and preserves the64-character four-sentence-X reply template. The fifth added X is initially free at every boundary. The template already contains a lexical X in TEXTOM; literal X counts must distinguish that from markers/padding.

Widths are16/17/18, constant alignment11 in all three stages. **n=11 is an explicit chosen hypothesis, not an inference from1170.** The visible reply itself remains a conditional plaintext hypothesis. Source trailing U/V glyphs are ambiguous; inventory-compatible model alternatives do not establish which glyph was printed. Source pixels and canonical transcription are unchanged. Input/provenance: `source-inputs.json`, derived from `batches/r364-review-collation-sol61/variants.json`.

The eager exact-cover engine is faithfully copied from the corrected insertion/variant solver, with its valid first-stage single-long-column packing pruning. At65letters,width16 has one long physical column0; its declared rank fixes the chunk boundaries. This is a logical restriction of the standard row-write/column-read procedure, not a planted key. No old control keys were supplied as hints or seeds.

An independent small unequal-width audit covers16cases, widths2/3/4, both n1/n2, unknown inserted X and a U/V variant union. Every SAT/UNSAT result agrees with direct enumeration of168 insertion/key triples. Returned witnesses independently re-encrypt. Records: `small-audit.json`.

Fresh control seed364617181201 uses the same quote template, a hidden insertedX position37, freshly generated aligned keys and an unknown ciphertext alternative formed by swapping one U and V. The solver receives neither true keys nor insertion/variant choice. **Free-X control UNKNOWN120.02s**: no free-X target was launched. This does not exclude that family.

A fresh restricted control, seed364617181202, fixes the extra X at the end as part of the model. The keys and correct U/V alternative remain unknown. **SAT68.04s recovered all three planted keys, all65plaintext letters and the correct ciphertext alternative exactly.** `verify.py` independently reproduces the complete cipher and inverse and confirms literal key equality. This is positive calibration only for the fixed-end-X subset; it does not calibrate recovery of a freely placed X.

The gated actual corrected EXCUV/EXCVU union, omitITPKA, widths16/17/18, n11, **fixed-end X**, returned **UNKNOWN180.12s**. No witness or key was found; no second-witness search was needed. This is not UNSAT and excludes neither this subset nor other X positions, alignments, widths, preparation or plaintext. The full free-X actual branch remains untested because its fresh calibration failed.

The source-corrected branch is now recorded distinctly from the old wrong-ERC tests. No ordinary keyword/lexical grid, source change, marker or watcher was introduced. Cipher NOTES/SOLUTION receive this bounded result after the report; no new decipherment is claimed.

Reproduce:

- `python3 batches/r364-corrected-unequal-sol61/audit.py`
- `python3 batches/r364-corrected-unequal-sol61/run.py`
- `python3 batches/r364-corrected-unequal-sol61/verify.py`

Full independent truth/control/target records and SHA-256 hashes are preserved in this batch.
