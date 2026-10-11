# Myszkowski dictionary transposition scout

No target is deciphered. This restricted single-transposition family ties equal keyword letters to the same rank and reads their columns together by rows, from left to right within each rank. Single-letter ranks read whole columns. The input grid is filled by rows without padding. This differs from standard unique-rank columnar transposition.

The declared keyword list contains12,866distinct rank patterns derived only from normalized forms and lemmas in frozen Slovak TRAIN data, lengths3–24 with repeated letters. No target word, plaintext or published target solution supplies a keyword. Four independent genuine held-out plaintext controls of55/65/115/400letters recover the whole text as the highest language score. Their random TRAIN keywords are included in the declared dictionary by construction; this is dictionary coverage, not unrestricted random-rank recovery. Exact whole-text inversion/reencryption checks are preserved.

Twenty actual cases cover whole forward/reverse literal bodies of363/393/369/345/396/367/374/371/399/395. Numeric administrative headers are explicitly excluded where present; no five-letter group or indicator is removed. Nonalphabetic marks become erasures, preserving position. All20leading texts are incoherent. 399 duplicates already solved391 as disclosed elsewhere; no391plaintext was read and no historical novelty is claimed.

Independent verification reconstructs positions by sorting row/column pairs inside tied groups, rather than importing the runner encoder. It checks480complete candidate bijections/inverses/encodings and recomputes frozen4/5scores. Results in verification.json. Finite dictionary failure excludes no unknown keyword, other rank pattern, double transposition or different preparation.

Primary algorithm source and worked-example discrepancies are preserved in SOURCES.md/primary-vector.json. The PDF text reconstruction of the95-letter FICTION example differs at one R/T and PAPILLA at one S/O; these unresolved printed/OCR discrepancies are disclosed rather than corrected to claim an exact primary vector. Fresh controls validate the implementation of the stated tied-column convention.

Reproduce from repo root: `c++ -O3 -std=c++17 batches/myszkowski-main/search.cpp -o batches/myszkowski-main/search` then `python3 batches/myszkowski-main/run.py`. Full keyword signatures, keys and whole texts are preserved. No source edit, solution, marker, watcher or register entry.
