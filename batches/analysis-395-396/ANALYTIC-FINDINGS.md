# Conditional parameter analysis for 395/396

GPT-6 Astra, 2026-10-11. Read-only with respect to all cipher directories. No plaintext solution is claimed.

## Strongest header observations

1. Native image crops show **9285**, not R285. Its first glyph has the closed loop and curved lower tail of 9, visibly distinct from the capital R in SIDOR. The latter comparator and header crops are retained here.
2. Suffixes 285 and 55 agree exactly with the transcribed ciphertext lengths. Prefix semantics remain unknown.
3. **The published worked R/XQ example contradicts treating the prefix as alignment or indicator position in general.** Figure 5, PDF page 8 / printed page 28, has alignment n=7 (all three grid headers begin 7), insertion position ip=5 according to the accompanying description, 55 payload letters, 60 transmitted letters, and a handwritten final header **360**. Its grid widths are **21,19,20**, so prefix 3 also is not its first-stage width. A code/key identifier or day remains possible; no claim establishes either.
4. Figure 7, PDF page 10, has further compound headers: Rome R690 with 90 letters, Madrid185 with 85, Sofia R2100 with 100, Bucharest `jún285` with85. The Bucharest rendering motivates a date/key-period interpretation, but is not by itself proof. Its285 is 2+85, unlike395's9+285.
5. The parent independently reports the original80214 portal record as dated August2. If396 retransmits precisely that original, prefix7 is not its original day2. The scan's reference to checking and resending old text does not establish whether the old ciphertext or just old plaintext was resent. Shared dispatch date therefore does not establish shared daily keys.

## Conditional indicator constraints

Run `python3 batches/analysis-395-396/indicator_constraints.py`. It models each letter as belonging to one digit column, with at most three letters per digit, using the paper's encoding n→five digits.

**Assumptions:** faithful transcription; R/XQ method; shared re-encryption table; and the unproved header interpretation n395=9,n396=7. Under these assumptions54 pairs of group positions pass. If both messages additionally use the **same** indicator position, only position8 survives: SKRUT in395, DWJPM in396. Their partial table is s/j→9,k/p→0,r/m→1,u→2,t→3,d→7,w→8. Allowing independent positions gives19 possible395 groups when396 group8 is fixed. This is a conditional consistency result, not parameter recovery; Figure5 is important counterevidence to the header interpretation on which it depends.

Without fixing n,396 groups2,7,9,10 cannot encode any n=1..22 in the transcribed C version. For group7 CSCNU the same C occupies positions1 and3; a two-digit n has a nonzero first digit but zero in position3, while a one-digit n has all different digits. The existing O alternative removes that contradiction; consistency alone is not grounds to change the transcription.

## Published example table

Figure2, PDF page3 / printed page23: 1:XUF;2:RN;3:YZW;4:ED;5:BA;6:QCI;7:JOP;8:KG;9:HVL;0:SMT. Its heading says effective from1 July1939 until revoked. It is **an example from a manual, not an established key for the1944 targets**. `example-table-check.json` applies it transparently; no group in either transcript encodes n1..22 under this table. No example-key decryption is represented as a target solution.

`check_paper_example.py` is a tentative transcription of the handwritten grids retained for inspection. It is not a validated known-answer test: handwritten letters/indicator reading are not fully resolved. The visual widths, first rank7, header360 and insertion location suffice for the parameter counterexample above.

## Message length and segmentation

Removing one group from395 leaves280 letters, exceeding the paper's stated250-letter R message range. That is evidence against a strict one-block reading of the described practice, but columnar transposition mathematically works at280; a recommendation violation, variant, transcription error or different method remains possible. The image has no obvious section delimiter. A two-block explanation would require two indicators (payload275), not simply280. If each block must contain at least50 payload letters, a conventional255+30 transmitted split cannot fit; a230+55 split (225+50 payload) can. There is no evidence selecting such a boundary. Test any split with explicit per-block indicators and minimum lengths; do not silently concatenate independently encrypted blocks.

## Joint shared-key control experiment

`python3 batches/analysis-395-396/joint_control.py` compiles `joint_r.cpp` and plants paired280/50-letter messages using common base rank permutations, independently rotated to n9/n7. It supports arbitrary comma-separated stage widths, row-wise fill, rank-order column output, and reverse stage order on decryption. One hundred random roundtrips are asserted per attack call. The variant where stage alignments increment n,n+1,n+2 is not implemented.

The planted text comes from the already archived Slovak training corpus, so scoring conditions are optimistic. Planting uses RNG seed981234; search uses395396. An initial draft reused the seed, which exposed the answer in the initial restart; this was detected, fixed, and all stored reported results regenerated with independent seeds.

- One stage, width16,360,000 proposed mutations: exact recovery of both280 and50 letters; found/true score866.183.
- Three stages, unequal widths16,17,18,360,000 proposed mutations: **failed**;21/280 and5/50 correct characters; found score−148.884 versus true866.183.

The current joint optimizer therefore has **no demonstrated ability to break triple R/XQ**, even in favorable controls. No triple target search was run and no target conclusion follows from this failure. The model alone is not an effective attack.

## Provenance

`context-paper.pdf`: downloaded2026-10-11 from https://ep.liu.se/ecp/171/004/ecp2020_171_004.pdf after a restricted-network attempt failed. Antal, Zajac and Grošek, HistoCrypt2020, printed pages21–30. Rendered pages3,8,10 retained for reading the tables/examples. This is methodological context, not a published solution to395/396. Native target source images were only read; all crops and scripts are in this batch directory.
