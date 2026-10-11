# Myszkowski alternative — main solver, OpenAI GPT, 2026-10-11

Primary cipher specification: American Cryptogram Association, https://www.cryptogram.org/downloads/aca.info/ciphers/Myszkowski.pdf . Repeated keyword letters share a rank; rows of equal-rank columns are read together, ascending rank. This is not ordinary columnar transposition with an arbitrary tie break.

The association's primary algorithm survey https://www.cryptogram.org/resources/downloads/AutomatedCryptogramSolving.V2.pdf discusses sorted-key partitions. Here a bounded ordered-partition enumeration is used instead of stochastic hill climbing. The initial exhaustive scope is widths2–8; additionally distinct Slovak dictionary keyword patterns of widths9–22 are tested. Keyword-pattern search is not complete at wider widths.

No document currently identifies the targets as Myszkowski. This is a conditional alternative to the historically documented R/XQ family. Ciphertext source files remain unchanged. Controls use independent generated encryption and held-out UD Slovak TEST text; language models are frozen independently in batches/scoring-sol61/frequency/. Neither published target answers nor target titles enter the solver.
