# HCP374 — recovered body and working physical key

The 80-letter encrypted body is recovered under a mixed-ring programmable Kryha model, accepted by Claude Opus5.5 in REVIEW1.md. KIDAH is the indicator shared with373, associated with the same starting selected stop and displacement. How its letters encode that setting remains open. The reviewed reading preserves two garbled letters and carries source35 M/N explicitly. Final four Xs agree with the X sentence-end/padding practice observed in the held-out373body. Some alphabet labels unused by this body remain a canonical completion, rather than recovered historical settings. Content and working key are verified; the indicator's coding is not reconstructed.

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

The tail crib binds19 input labels and all26 output labels. Held-out MADRID in public373 resolves M to24. X at19 is supported by sentence breaks and terminalXX in the decoded373body outside the fitted tail. Unused F/G/J/Q/W positions4/9/15/18/22 complete a permutation but are not historically recovered. None occurs in374's reviewed decoded body.

## Source reading and literal plaintext

No transcription was attached to374. An independent image reading was frozen before consulting the transferred key or decoded374 text. It gives:

```
KIDAH CRTGS BVBPT ILOIQ SPQHQ NZYHI QLXUM
AIPOT KBCEY HVUIU QOQPM TLIJV ABAVE KZAXI
MLEMP QXMJC JSLWF
```

Image evidence prefers G/Q/V at source positions9/25/60, correcting the older C/O/Y working reading. The new GPT reader reads M at35 where the older reading and Claude's independent pre-key reading had N. The faint final glyph has ambiguous right strokes/shoulders, so neither reader is presented as pixel certainty. Review1 recommends N as default because the independent earlier reading and published word agree. The quoted blind GPT reading remains unchanged above; `work/transcription-collated.txt` now uses QLXUN, with QLXUM explicitly available as an alternative. Source bytes are unchanged. Pixel crops and the pre-decode GPT reading remain in `batches/kryha374-key-transfer-main/independent-source-read/`; the complete DONE1 default is archived in `work/round1-default-M/`.

The exact reviewed default body, spaced for reading, is:

```
A UPOZORNUIE SPANLELSKE PROTIBODAVKY UZ PEVNE KUPENE
NA ZAKLADE POVODNYCH CIEN CELULOZY XXXX
```

Reading source35 as M changes PROTIBODAVKY to PROTIBODVVKY. Both complete80-letter bodies encode back exactly to their respective readings. We retain source21 S and source32 L: they decrypt as L and B where the same key reads I and D in the corresponding words of373. Both independent source readings agree on S/L. These are garbles in this copy, not evidence against the recovered key. We do not change those source characters to W and A merely to obtain the expected words; their exact encryption/transmission/typing cause is unresolved.

The intelligible content, **restored using the already published373draft**, is:

> A upozorňuje: španielske protidodávky sú už pevne kúpené na základe pôvodných cien celulózy.

The original draft wording is “a upozorňuje španielské protidodávky už pevne kúpené na základe pôvodných cien celulózy.” The first displayed sentence adds punctuation and an implicit verb for readability; it is not the literal machine output. J→I preparation explains UPOZORNUIE. English translation: “And points out that the Spanish counter-deliveries have already been firmly purchased on the basis of the original cellulose prices.” The literal source discrepancies and hypothetical XXXX are not hidden by this translation.

## Reproduction

From repository root, one read-only command produces the entire encrypted-body plaintext:

```sh
python3 ciphers/hcp-374/work/decrypt.py
```

The script verifies the immutable source JPEG hash and the source-bound manual-reading hash, then loads that reading and the saved key. It does not perform OCR. It prints retained KIDAH separately and all80 decoded letters. `--alternate-35-m` selects the disclosed other reading; the old `--alternate-35-n` remains an explicit N selector. `--json` prints coverage and uncertainty fields. Encoding includes the unchanged framing prefix, so85/85 source-reading characters round trip; only80/85 are claimed deciphered. `python3 ciphers/hcp-374/work/verify.py` independently uses absolute wheel coordinates and wrap counts, rather than the decoder's adjacent-edge walk.

## Evidence and limits

The source tail before final padding is186letters. The known-plaintext attack preserves source words, J/I and an optional proper-name-Q hypothesis, searches all offsets and periods2–52, and omits only declared uncertain glyph equations while retaining their press indices. It finds one witness in94,656 cases: naturalJ→I, noQ, offset462, period23. Its183 nonerased equations fit exactly. Three fresh physical controls recover complete186/188-character ciphertexts without true ring/mask hints. Source504 remains the only literal-tail mismatch; a later, explicitly nonblind pixel reinspection supports A over the saved E. No source bytes are corrected.

An independent physical DP and a separate coordinate-translation audit both give exactly one23-stop realization with arc sum179. For374, all598 phase/displacement combinations were compared using only bound alphabet positions. Before the new image reading, phase3/shift8 matched71 of76 published suffix letters; the next candidate matched only21. The new independent glyph reading supplies the complete named body above. Exact round trips alone are not evidence of language: the independent crib fit, physical mask, held-out contextual coherence and explicit source discrepancies support the interpretation together.

Reports: `batches/kryha373-tail-sliding-sol61/REPORT.md`, `batches/kryha373-physical-tail-sol61/REPORT.md`, and `batches/kryha374-independent-key-sol61/REPORT.md`. Earlier failed350-ring transfers used a different ring hypothesis and remain in NOTES/work; they do not contradict this newly recovered Madrid key.

The strongest held-out check is the rest of373: the same rings/stops read its entire645-letter body as running Slovak, from ROESNER MADRID OZNAMIL through CIEN CELULOZYXX. That includes459 letters outside the186-letter fitted tail, with cardinal number words and X at sentence boundaries. Claude independently reproduced this. `python3 ciphers/hcp-374/work/heldout373.py` saves no files by default and reproduces the source-hash-bound check. It preserves the given collation, canonical rare labels and literal garbles; it does not certify every image glyph, turn the initialKIDAH into plaintext, or claim new373content. The X sentence boundaries and terminalXX support the XXXX in374 as observed preparation practice.

The repeated content begins at the word boundary A UPOZORNUJE and is76 letters plus4X, hence16 groups. The requested last15 cipher groups would cut into that opening word under the same body decode. Expanding to a word boundary and repadding explains the extra group; this is an inference about the operator's choice, not a documented instruction.

The updated review confirms the indicator relationship: both ciphertexts begin KIDAH, both body starts use selected-stop ordinal0 (physical zero-based hole34, human hole35) and displacement1. In373 the repeated sentence occupies source letters573–648, after567 body emissions; in374 it is enciphered afresh at body emission0. The corresponding76 ciphertext letters have zero agreements, while74/76 plaintext letters agree. This is re-encipherment from the common starting state, not a literal resend of old cipher groups. `work/indicator-comparison.json` records both source slices, positions and measured counts. KIDAH's actual letter-to-setting mapping cannot be reconstructed from this one repeated indicator value.

Remaining limits are that indicator coding, unused input labels, source35 M/N and the exact causes of the two copy garbles. The historical indicator procedure and independently certified full373source collation are not established. No register entry is written: the content is already public and review explicitly leaves eligibility for a key-recovery entry to the human. Review1 accepts this body/working-key result and requires no second round.

## Response to review 1

Verdict ACCEPT, six minor findings, no second round required. The ring arrays, physical stops and displacement remain unchanged.

1. **Source35 default:** changed M to N in the reviewed working transcription, supported by the pre-key Claude reading and the published word. The newer GPT M reading remains unaltered in its blind artifact and available with `--alternate-35-m`. Ambiguous final shoulders/strokes and reader disagreement are disclosed. The DONE1 default, key, outputs and scripts are archived in `work/round1-default-M/`. The source JPEG and marker are unchanged.
2. **Held-out373:** added the reproducible645-letter body check, including459 letters outside the fit. It follows the published draft with cardinal numbers and sentence boundaries; the context is attributed and is not counted as a new373decipherment. Remaining literal source garbles/uncertified collation are distinguished from this strong key validation.
3. **X preparation:** X at19 now has observed held-out support from373's sentence boundaries and terminalXX; XXXX in374 is reported accordingly rather than as an arbitrary label chosen only from the final four coordinates.
4. **Two wrong letters:** state that SPANLELSKE/PROTIBODAVKY are garbles in this copy under the same key that reads SPANIELSKE/PROTIDODAVKY in373. Both independent readers agree on source21S/32L; neither is silently altered. The particular transmission/typing/encryption cause remains unknown.
5. **Updated indicator finding:** incorporated the human's revised review. Both immutable working ciphertexts begin KIDAH and share initial selected-stop ordinal0/displacement1. The body sentence is re-enciphered at the start in374, whereas it begins after567 emissions in373: zero cipher-letter agreements but74/76 plaintext agreements. KIDAH is now described as the shared indicator tied to this starting state. ORWKM was only a projected decode of373's prefix, as the revised review itself corrects. Exact coding of indicator letters to settings remains open; one repeated value does not establish that mapping. SOSOL in350/351 belongs to the separately recovered key.
6. **15 versus16groups:** added the measured76-letter sentence plus4X and its word-boundary explanation, explicitly an inference. No equality of the original75-byte request range and the new80-byte body is claimed.

The final report includes the original scan, the literal reviewed body, the restored public-context wording, key, held-out evidence, all limits and this review summary. No register entry is created without separate human authorization for this previously published-content key-recovery result.
