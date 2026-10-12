# HCP364: explicit single-long16/16 stages, third width17

This new source-allowed R family is16/16/17 at N65. The first two stages each have one long physical column0, length5, and15short columns oflength4. With common unknown column-zero rankk=n−1, the long column starts at4k; shorts before it start at4rank, shorts after it at4rank+1. This explicit shared packing removes generic prefix/rank variables in both first stages. Only the width17stage needs a60-state prefix path. No intermediate plaintext character variables are used; cached endpoint support is imposed forwards and backwards.

The model has1,851selected-start Booleans,54,608forward clauses and102,178reverse clauses. This is structurally smaller than the prior unequal16/17/18 and equal21models, not a longer timeout or repeat of their input. Common alignment n is **unknown over all1..16**, with no header interpretation or planted key/rank hint. The source-primary range16–22 motivates these widths; it does not identify364'shistorical grid.

Twenty-four small tests agree with independent enumeration of all864width3/3/4key triples,72ofwhich have common alignment. Positive and same-inventory negative U/V-union observations are included. Returned witnesses independently encode correctly.

Fresh full65control seed3641616171201 uses the conditional visible four-sentence-X template plus a fixed final X, random independent keys sharing a hidden n, and an unknown U/V ciphertext alternative. **Native blind SAT10.87s recovered all three planted keys, hidden n15 and the correct alternative exactly.** Full encoder/inverse verification reproduces all65letters. Neither keys nor n were supplied to search. This is calibration of a fixed-end-X known-plaintext attack, not discovery of the visible quoted reply.

The actual corrected EXCUV/EXCVU source union, omit ITPKA, same fixed-end quotation, was then checked by one native solver retaining clauses across all16common-rank assumptions. **All16are exactUNSAT, noUNKNOWN; total solving4.57s.** No target witness was found. These results are conditional on the quotation, chosen preparation, exact source union and width order16/16/17. They exclude no other thirdwidth, mixed-stage order, progressive alignment, free fifthX or broader R family.

Original source and old batches are unchanged; cipher docs belong to root. No marker/watcher was introduced. Hashes and the full control/target/rank records are preserved. A separately owned `extension/` will test new third widths18–22 with fresh controls before any target; it does not overwrite this completed result.

Reproduce:

- `python3 batches/r364-two16-one17-sol61/audit.py`
- `python3 batches/r364-two16-one17-sol61/run.py`
- `python3 batches/r364-two16-one17-sol61/verify.py`
