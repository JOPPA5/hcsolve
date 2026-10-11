# AMSCO dictionary transposition scout

No target decipherment. The cipher fills row-ordered cells with alternating single/double letters, then reads whole physical columns in unique numeric keyword order. Equal keyword letters receive stable left-to-right ranks. Four explicit conventions cover continuous cell parity or alternating row starts, each beginning with a single or double cell. Equivalent conventions for odd widths are allowed but are not independent evidence.

The frozen TRAIN-only12,866repeated-keyword list is reused from the Myszkowski experiment; all standard numeric ordering here resolves ties uniquely. This is a finite dictionary subset, not exhaustive arbitrary numeric keys. Four fresh genuine55/65/115/400held-out controls use independent dictionary keywords and the four respective cell conventions; all recover complete plaintext as highest score. No planted key enters scoring or selection, but the declared dictionary includes those control keywords by construction.

Twenty whole literal streams (forward/reverse of363/393/369/345/396/367/374/371/399/395) each scan all four cell conventions. Numeric administrative headers are explicitly excluded where present, with no group omission. Marks become phase-preserving erasures. Every winning complete text remains incoherent. The solved391duplicate relation for399 remains disclosed; no391plaintext was consulted.

Independent verification reconstructs row cells from explicit parity and sorts them by numeric key rank/row. It checks480complete position bijections, encodings and inverses, then recomputes frozen4/5scores, in verification.json. This verifies candidates, not their linguistic correctness. Finite dictionary failure excludes no other key, preparation, multi-stage system or cipher family.

Algorithm provenance and the two parity conventions are in SOURCES.md. Reproduce: `c++ -O3 -std=c++17 batches/amsco-main/search.cpp -o batches/amsco-main/search` followed by `python3 batches/amsco-main/run.py` from the repository root. Full parameters, signatures, candidate keys/texts and corpus hashes are preserved. No source edit, solution marker, watcher or register entry.
