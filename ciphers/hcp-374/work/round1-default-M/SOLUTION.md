# HCP374 — recovered body and working physical key

The 80-letter encrypted body is recovered under a mixed-ring programmable Kryha model. The first five letters KIDAH are retained as framing; their meaning is not deciphered. The body reproduces every letter of the independent source reading, including two apparent spelling discrepancies and one disputed source glyph. Final four repeated coordinates are interpreted as X padding. Some alphabet labels unused by this body remain a canonical completion, rather than recovered historical settings. This is a disclosed partial historical claim, submitted for independent review.

## Origin and published context

HC Portal374 is Not solved: MZV80174/1944, 20 May1944, Šulík to the Slovak legation in Madrid, Slovak National Archive, MZV box42. The scan prints 85 and seventeen five-letter groups. The portal title describes a request to repeat the last15groups of80172. The recovered body is a retransmitted commercial sentence suffix; it is not an invented request phrase. The title's15groups and this body's80letters are not asserted to be identical byte ranges.

Public Solved373, MZV80172/1944, contains the original ciphertext and an archival clear-text draft. Its final sentence supplies an **attributed known-plaintext crib**. We recovered a working machine key from that context and transferred it to374; the commercial content was already published in373. We make no new373plaintext claim and no claim that374 was solved without known plaintext. All three rendered tabs and attachment URLs are recorded in `batches/solved-context-main/373/SOURCES.md`.

## Cipher and key

The key is in `work/key.json`. P and O map A–Z to numeric ring coordinates0–25. The convention is O(cipher)=P(plain)+d modulo26. Both rings use the gauge P(A)=O(A)=0; physical ring labels/handedness outside this convention are not independently measured.

```
P = 0 11 14 1 20 4 9 2 13 15 16 3 24 7 17 25 18 21 10 5 12 6 22 19 8 23
O = 0 4 1 21 8 3 19 15 13 18 25 10 22 16 2 12 5 23 7 20 11 14 17 24 9 6
```

There are23 selected stops on the52-hole wheel. Starting with this body's first letter, the **zero-based** indices are:

```
34 37 40 42 44 45 47 48 49 51 2 4 5 8 11 13 17 20 21 24 26 29 31
```

For human hole labels1–52, add one to every index. First displacement is1 modulo26, equivalent to27. After each body letter, walk the saved adjacent distances to the next selected stop; a complete revolution sums179. The physical mask is uniquely compatible with the frozen recovered displacement cycle within this geometry/convention. This is not a general uniqueness claim for all historical machines or keys.

The tail crib binds19 input labels and all26 output labels. Held-out MADRID in public373 resolves M to24. X at19 is the explicit sentence/padding hypothesis. Unused F/G/J/Q/W positions4/9/15/18/22 complete a permutation but are not historically recovered. None occurs in374's preferred decoded body.

## Source reading and literal plaintext

No transcription was attached to374. An independent image reading was frozen before consulting the transferred key or decoded374 text. It gives:

```
KIDAH CRTGS BVBPT ILOIQ SPQHQ NZYHI QLXUM
AIPOT KBCEY HVUIU QOQPM TLIJV ABAVE KZAXI
MLEMP QXMJC JSLWF
```

Image evidence prefers G/Q/V at source positions9/25/60, correcting the older C/O/Y working reading. The new reader reads M at35 where the older reader had N; both branches are retained. Source bytes are unchanged. Pixel crops, the pre-decode reading and confidence are in `batches/kryha374-key-transfer-main/independent-source-read/`.

The exact preferred body, spaced for reading, is:

```
A UPOZORNUIE SPANLELSKE PROTIBODVVKY UZ PEVNE KUPENE
NA ZAKLADE POVODNYCH CIEN CELULOZY XXXX
```

Reading source35 as N changes PROTIBODVVKY to PROTIBODAVKY. Both complete80-letter bodies encode back exactly to their respective readings. We retain source21 S and source32 L: they decrypt as L and B where the published373draft suggests I and D. We do not change those source characters to W and A merely to obtain the expected words. Whether these discrepancies arose in encryption, transmission, typing or reading is unresolved.

The intelligible content, **restored using the already published373draft**, is:

> A upozorňuje: španielske protidodávky sú už pevne kúpené na základe pôvodných cien celulózy.

The original draft wording is “a upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.” The first displayed sentence adds punctuation and an implicit verb for readability; it is not the literal machine output. J→I preparation explains UPOZORNUIE. English translation: “And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices.” The literal source discrepancies and hypothetical XXXX are not hidden by this translation.

## Reproduction

From repository root, one read-only command produces the entire encrypted-body plaintext:

```sh
python3 ciphers/hcp-374/work/decrypt.py
```

The script verifies the immutable source JPEG hash and the source-bound manual-reading hash, then loads that reading and the saved key. It does not perform OCR. It prints retained KIDAH separately and all80 decoded letters. `--alternate-35-n` selects the disclosed second reading; `--json` prints explicit coverage and uncertainty fields. Encoding includes the unchanged framing prefix, so85/85 source-reading characters round trip; only80/85 are claimed deciphered. `python3 ciphers/hcp-374/work/verify.py` independently uses absolute wheel coordinates and wrap counts, rather than the decoder's adjacent-edge walk.

## Evidence and limits

The source tail before final padding is186letters. The known-plaintext attack preserves source words, J/I and an optional proper-name-Q hypothesis, searches all offsets and periods2–52, and omits only declared uncertain glyph equations while retaining their press indices. It finds one witness in94,656 cases: naturalJ→I, noQ, offset462, period23. Its183 nonerased equations fit exactly. Three fresh physical controls recover complete186/188-character ciphertexts without true ring/mask hints. Source504 remains the only literal-tail mismatch; a later, explicitly nonblind pixel reinspection supports A over the saved E. No source bytes are corrected.

An independent physical DP and a separate coordinate-translation audit both give exactly one23-stop realization with arc sum179. For374, all598 phase/displacement combinations were compared using only bound alphabet positions. Before the new image reading, phase3/shift8 matched71 of76 published suffix letters; the next candidate matched only21. The new independent glyph reading supplies the complete named body above. Exact round trips alone are not evidence of language: the independent crib fit, physical mask, held-out contextual coherence and explicit source discrepancies support the interpretation together.

Reports: `batches/kryha373-tail-sliding-sol61/REPORT.md`, `batches/kryha373-physical-tail-sol61/REPORT.md`, and `batches/kryha374-independent-key-sol61/REPORT.md`. Earlier failed350-ring transfers used a different ring hypothesis and remain in NOTES/work; they do not contradict this newly recovered Madrid key.

Remaining limits are the framing meaning, the X-padding interpretation, the unused input labels, source35 M/N and the two other literal word discrepancies. The exact historical indicator procedure and a fully certified650-letter373decryption are not established. No register entry is written for this partial, published-context-derived claim. Independent review is pending.
