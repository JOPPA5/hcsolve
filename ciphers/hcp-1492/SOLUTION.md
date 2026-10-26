# HCP 1492 / pc_hcp_173 — revised numeric postscript

All **40 numeric cipher positions** decode with the direct alphabet **1=A, 2=B, …, 26=Z**. Review 1 confirmed the original four lines and identified an omitted separate `24 24 24.` group, now included. This revision addresses every requested record correction.

## Plaintext

```text
DEAR CHICKEN
HOW- ARE YOU?
LOTS OF LOVE
FLOSSIE
X X X.
```

The dash after HOW and question mark after YOU are on the card. Spaces are editorial word segmentation; dots separating numeric letters are retained in the diplomatic ciphertext rather than printed between plaintext letters. The separate three-X group ends with a written dot.

Readable interpretation: “Dear Chicken, how are you? Lots of love, Flossie. XXX.” Chicken is an affectionate term of address, not replaced by a personal name. XXX is usually read here as kisses; the literal key output is three Xs.

Slovak: „Miláčik [doslova kuriatko], ako sa máš? Veľa lásky, Flossie. Tri bozky [interpretácia XXX].“

## Origin, key and reproduction

The rendered portal was Not solved on 2026-10-26. All three tabs and both source scans were captured; no supplied transcript or solution. Catalogue date 1911-06-11, Europe, private collection; sender Flossie and recipient J. Stalland are portal metadata. The written dateline appears 10-6-11, the postmark JUN11. The ordinary cursive letter, postal/date numerals, address and separate dealer-like notes are outside the encrypted count. The picture is a landscape with no observed cipher.

The complete key is the ordinary 26-letter alphabet with A=1 through Z=26, no offset or exceptions. From the repository root:

```sh
python3 ciphers/hcp-1492/work/decode.py
```

`work/transcription.txt` is the manually read value/word list. `work/transcription-diplomatic.txt` records the card's punctuation. The script verifies immutable source hashes, confirms the two records have identical values, applies the direct key and prints all 40 letters with the recorded source punctuation. It does not perform OCR or independently validate a pencil stroke.

## Evidence and limits

One key decodes the entire numeric postscript, including the separate three 24s. The3 and 8 of CHICKEN are clearly divided by a dot. The actual image-quality caveat is the first 12 in LOTS: the 1 partly overlaps the inverted JUN postmark, but the visible stroke and2 support 12; the reviewer independently read the same value. Doubled19 in FLOSSIE is retained.

The decoded name agrees with the ordinary signature and catalogue sender; this does not identify a historical person. The top-corner dealer-like mark is not securely attributed. No published target plaintext was used and no priority follows from a register snapshot. No unresolved numeric value remains after correction; review's required record changes are addressed. No FINAL or register entry is created in this pass.

## Response to review 1

Review: `review/REVIEW1.md`, Claude Opus 5.5, 2026-10-26, verdict REVISE. The reviewer confirmed the original 37 values and required the omitted three-value group plus record corrections. The review explicitly states no further round is needed after those corrections. Source and review files remain unchanged.

1. **Missing group / coverage (major coverage, minor meaning): addressed.** Reinspected the original address scan and `review/work/x24_big.png`. The separate `24 24 24.` below the printed heading is in the same pencil/orientation as the message. Added all three values to `work/transcription.txt` and the diplomatic record; decoder, plaintext, translation and report now include **X X X.** The encrypted numeric count is **40**, not37. Kisses are the contextual meaning, not additional numeric letters.
2. **Punctuation (minor): addressed.** Added `work/transcription-diplomatic.txt`, preserving numeric dots, dash after `8.15.23`, and the question mark after `25.15.21`. `work/punctuation.json` records the dash and question mark as source marks, and the decoder now prints **HOW- ARE YOU?** The question mark is no longer described as editorial. Letter-separating numeric dots are not inserted between plaintext letters; the original numeric punctuation remains inspectable in full.
3. **3.8 description (minor): addressed.** Removed the inaccurate close-writing/38 warning. The original and `review/work/nL_big.png` show a clear separating dot between 3 and 8. No invented value38 is needed.
4. **Overlapped12 (minor): addressed.** The first 12 of LOTS is partly crossed by the inverted JUN postmark. Its1 has an obscured upper portion; the visible lower stroke and clear 2 support 12, also independently read in review. This physical overlap is now the stated image-quality caveat, replacing the unsupported3/8 warning.

The A1Z26 key and the first 37 decoded letters are unchanged. Regenerated `work/plaintext-check.txt`; the command verifies40 values and agreement of diplomatic/normalised numeric records. Source hashes establish integrity, not OCR correctness. Report source is `report/report.md`; PDF verification and final state marking remain with the root solver.


## Finalization - 2026-10-26

The coordinating solver verified the item-by-item review response, reran the
corrected decoder with original-source hash checks, and produced the report
PDF. All rendered pages were visually inspected after final typography
corrections. The review explicitly permits closure after the specified local
corrections without another round. Remaining reading uncertainties are
preserved; no new independent ACCEPT verdict is claimed.

The local register-entry.txt is prepared with solver TODO because no solver
name was supplied for the entry. Nothing was submitted externally. Original
source files and review files were left unchanged. FINAL records closure
after these review conditions and report checks.
