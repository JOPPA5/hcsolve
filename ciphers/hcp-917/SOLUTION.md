# HCP917 — unresolved

The portal reports substitution, unknown language and unknown date. The picture-side writing was inspected after a 90-degree rotation. It contains digit-like, letter-like and crossed forms whose distinction is uncertain. The small handwritten address and recipient do not establish the cipher's language.

No exact prior solution was found in the AI Register or bounded name searches. The tentative working graphic transcription has 196 cells and is not an authoritative transcript. Four bounded substitution scouts were run, each with 1,200,000 proposals:

1. Hungarian forward, whole scout, seed 9171243.
2. German forward, whole scout, seed 9171244.
3. Hungarian forward, body without heading, seed 9171245.
4. Hungarian reverse, whole scout, seed 9171246.

Full best outputs and keys are preserved in `work/scout-*-result.txt`. None gives a coherent complete reading with a source-verified key. Isolated language-like fragments are not a solution. In particular, the uncertain symbol classes could have merged distinct cipher signs; these searches do not rule out a monoalphabetic cipher.

Reproduction: from the repository root, `sh batches/postcards-five-2026-10-12/reproduce.sh`. A clean held-out modern Hungarian control recovered 260/260 letters, but this validates the program on that control only. No full plaintext, complete key, DONE marker, accepted review, FINAL marker or register entry exists.

## Targeted follow-up
After correcting the heading's second graphic class and distinguishing two additional forms, a KEDVES-constrained search was run for another 1.2 million proposals (seed 9171301). It forced the greeting but did not produce a consistent body. `work/crib-recheck-result.txt` preserves the negative result. This does not validate the crib or the revised transcription; see NOTES.md. No additional decipherment is claimed.
