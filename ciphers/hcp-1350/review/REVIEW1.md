ACCEPT

# Review 1 — hcp-1350 / pc_hcp_31 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands: Caesar −1, English, "My own dearst boy what an unexpected surprise this morning both very nice your loving girl Loo". I tried to break it on the pixels and could not. Only minor issues remain. Solver was also Claude Opus 5.5, so this is not a cross-vendor check.

## What I verified and how

- **Command.** `python3 -I ciphers/hcp-1350/work/decode.py` ran: 4 hashes OK, 78 letters, output equal to the table in SOLUTION.md.
- **Independent decryption.** `review/work/dec.py` (own script, no shared code) gives the same six lines and 78 letters. Shifts 0, 2 and 25 give no text; there is no key to tune, only one shift, and it covers every letter of the transcription. The only unenciphered text is the plain date.
- **Scan, sign by sign.** Whole message from the hi-res address side, rotated 90° CCW, at 4x (`review/work/L1a…L7.png`, `crops.py`), with 5x/7x comparisons (`cmp.png`, `z3.png`). All six rows read directly. Every group matches: the long non-formula words `vofyqfdufe` (10 signs, raised final e confirmed, q and both f descenders distinct) and `npsojoh` are unambiguous.
- **`efbstu`.** Six signs. Between s and the barred t nothing descends, and the u has the same trailing curl as the u of `xibu`. Literal DEARST confirmed, kept as such.
- **Capital of `Mpp` / `mpwjoh`.** Three downstrokes on both; two on the N of `Nz` and n of `npsojoh`. The solver's count holds, though on a small margin, as disclosed.
- **Last sign of `Mpp`.** Single stem with a small right-hand curl, no f loop; same construction as the second p on hcp-1353 (`tail.png`). Signature `Mpp` matches hcp-1353, 1354 and FINAL hcp-1398.
- **`Cpui`.** Spiral-headed capital, then p, u, dotted i. BOTH is the only sense; DOTH does not fit.
- **Context.** 7 March 1907 was a Thursday (computed). Postmark at 3x: WIM… on the arc, 10 PM, MR 7, 07. Address, stamp, "Weymouth, view from Sandsfoot Castle" caption, Frith No. 52870 and pencil 4 all as stated. No writing on the picture side. Language and formulae fit the sister cards.
- **Sources.** Portal capture records no attached solution. SOLUTION.md credits sister cards as hypothesis sources and says what was taken from them. No letter is restored; the plaintext gives DEARST, not a silent DEAREST.

## Findings

1. **minor — `t` of `Tvsqsjtf` is transcribed flat, and the support is partial.** On this card the sign has a 3-shaped head (`review/work/z3.png`). hcp-1353 (`surp.png`) has the same tail and hooked foot but a barred head, not a 3-head, so the parallel covers only the lower half. It is not this writer's z either: all four z on this card (`Nz`, `Cpz`, `wfsz`, `Zpvs`) are flat-topped Z forms, which argues against SOLUTION.md's "looks like a tailed cursive z" and against an unshifted z. The sense SURPRISE is not in doubt and the anomaly is disclosed (uncertainty 2). Suggested: add the point that the four z on this card differ, and keep it listed as the one sign read from the word and not the shape.

2. **minor — two irregular signs are undisclosed.** The x of `pxo` is Y-shaped with a foot, not the open crossed x of `xibu` (`review/work/cmp.png`, top two rows): the strokes merge rather than cross. The w of `wfsz` opens with a tall stem unlike the low w of `mpwjoh` (same file) and could be taken for a b at first sight. Only OWN and VERY make sense, and `Nz. pxo.` is the same opening as hcp-1398, so the reading stands. Both should go in the uncertainties; uncertainty 5 gives the impression it is complete.

3. **minor — `efbstu` has a closer parallel than the one cited.** SOLUTION.md cites `Efbsftu` on hcp-1356. FINAL hcp-1398 has the identical `Nz. pxo. efbstu Cpz.` with the same six letters, also confirmed there by review. A repeated spelling by the same writer makes "slip" less certain than it reads; it may be a habit. Cite it. The English line silently writes "dearest" as normalised punctuation-level text; mark it `dear[e]st` as hcp-1398 does.

4. **minor — postmark over-read.** The town is given as WIMBORNE, but only WIM and traces under the stamp design are legible here. The reading is safe from hcp-1354 (same postmark form, two days earlier); say so.

5. **minor — count of uncertainties.** The status line says "Four small points", the list has six. Harmless; align when the report is written. Report should also state that the review was Claude on Claude.

## What I could not verify

- The live portal page: I relied on `source/metadata.md` and `SOURCES.md` for status and absence of a solution.
- What "both" refers to, the writer's identity, and whether Loo is a pet name. All disclosed as unknown or conjecture.
- Whether the `Tvsqsjtf` sign was meant as a t or a personal form: unresolved by shape, immaterial to the sense.
