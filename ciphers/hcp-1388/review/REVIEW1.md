ACCEPT

# Review 1 – hcp-1388 (pc_hcp_69)

Reviewer: Claude Opus 5.5, 2026-10-30. Round 1 (DONE1). Earlier work credited in SOLUTION.md: OpenAI GPT solver (GPT-6 Astra / GPT-6.1 Sol), 2026-10-26, partial; Claude Opus 5.5 as solver, 2026-10-29, completion.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1388/work/decode_full.py` (from repo root): "source hashes OK", 51 cipher letters, output identical to the table in SOLUTION.md:
   `My. Dearest. thanks - / for. letter it. Was / fine [**] M xx from / Your. own. Girl`.
2. **Independent decryption.** `review/work/mydecode.py` (own Caesar −1 implementation, transcription typed from my own reading of the crops; brackets passed through) gives the same four lines and the same count of 51 letters. One key covers every letter; no exceptions, no nulls.
3. **Transcription against the scan.** I rotated `source/address.jpg` 90° CCW (`review/work/rot.png`) and made my own enlargements:
   - `review/work/l12.png`, `review/work/l34.png` (3x, all four lines): Nz, Efbsftu, uibolt, gps, mfuufs, ju, Xbt, gspn, Zpvs, pxo, Hjsm all agree with the solver letter for letter. `gps`/`gspn` use the writer's 9-shaped g; `Xbt` and `Zpvs` capitals are clear.
   - `review/work/l1Nz-8x.png`: cipher N of `Nz` is a top arch, a stem and one hump.
   - `review/work/l3gjof-5x.png`: `gjof` – 9-shaped g, a j stroke with a heavy dot well above it, a small o, a looped f. The reading "fine" is supported.
   - `review/work/l3gjof-5x.png` also shows the two `[**]` marks: dense, very dark blots with spiky edges, darker than the message ink, no letter form. Reporting them literally is correct.
   - `review/work/l23mid.png` (5x) and `review/work/l3group-8x.png` (8x, autocontrast): the "N yy" group. The capital has the same build as the N of `Nz` (top loop, stem, one hump). A long diagonal runs without a break from the `j` of line-2 `ju` down through line 3, so treating it as line-2 ink is justified. To its right are a large open C-like curl on the diagonal (y no. 1, stem shared with the diagonal) and a second y (small top hook, long diagonal, small foot). The second y has the same form as the final y/x-like sign in hcp-1390's `work/line4-tail-3x.png`. `yy` → xx (kisses) is a sound reading.
4. **Language and context.** "My dearest, thanks for letter, it was fine. M xx from your own girl" is natural Edwardian English postcard style. It has the same key and closing as the sister cards hcp-1390 and hcp-1397 (to W. Abbott, Chudleigh, 1907). The plain date April 15th 1907 agrees with the postmark "10 PM AP 15 07" (visible on the rotated scan) and with the portal date.
5. **Sources/honesty.** The portal status is Not solved and no solution is attached (metadata.md, SOURCES.md). No published solution was used. The partial GPT work and the Claude completion are credited separately.

## Findings

1. **(minor) The hcp-1390 parallel is overstated.** SOLUTION.md says hcp-1390 has the same "M + yy" group ("to day. M yy/××") and that this "confirms this reading". The current hcp-1390 SOLUTION (after its review) does not say that. It reads the group after "to day" as an *unread* group: a large capital, a small raised h-like letter and a dot. It reports the following marks as y y / ×× and leaves open whether the capital M is enciphered or plain. So 1390 supports the **yy = xx (kisses)** part, but not the reading "cipher N → M". On 1388 itself the capital does match the N of `Nz`, so "N → M" can stand, but the wording should be "consistent with" and should note the difference. The two cards should also be described consistently in the report: here cipher N → M; on 1390, a capital whose cipher value is undecided.
2. **(minor) The oval in the "N yy" group is not fully accounted for.** In `review/work/l3group-8x.png` a closed oval sits at line-3 x-height, left of the long diagonal, and joins it above the diagonal's lower end. It looks like the writer's 9-shaped g more than a classic descender loop, which would be at the bottom of the j stroke. Reading it as part of the line-2 `j` is plausible but not certain. If it were a line-3 sign, the group would have four signs (e.g. N ? y y). Uncertainty 3 should also list this oval, not only the merged stem of y no. 1. It does not change the substance (M + kisses).
3. **(minor) Heading initial.** On my rotated scan the first heading initial looks like G (open top, inward bar), as hcp-1397 has it. SOLUTION.md leads with "C. H.". It is outside the cipher and already marked uncertain, but "G. H." should be the primary reading, or both should be given equally.
4. **(minor) Literal "M".** "M" before the kisses is left unexpanded. That is correct and disclosed. No action needed beyond finding 1.

No blocker or major findings. All 51 cipher letters are read, one key covers all of them, and the plaintext is coherent and fits the context.

## What I could not verify

- The meaning of "M" (initial, pet name or abbreviation) and the nature of the two dark `[**]` marks (crosses, blots or cancelled letters). Both are only visible at scan resolution (1024×674).
- Whether the oval in the group belongs to line 2 or line 3 (finding 2). A higher-resolution scan would settle it.
- The farm name and the heading initials, which are outside the cipher.
