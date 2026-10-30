ACCEPT

# Review 2 — HCP 1403 (pc_hcp_84)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Round 2, state DONE2.

## Summary

The round-2 solution fixes both reading errors raised in REVIEW1. Line 1 is now `Nz. Pxo. E. l. Cpz.` (MY OWN [E. L.] BOY). Line 4 is now `mfuufs` (LETTER). The closing is
`Nz. N. & L. Zpvs. [Pxo] / E. l. Hjsm` (MY [N. & L.] YOUR [OWN] [E. L.] GIRL).
The key is Caesar with decryption by −1. I re-checked every corrected sign on fresh enlarged crops. The reading stands, and all
uncertainties (the literal abbreviations, the probable `Nz` in the closing, the restored [OWN]) are disclosed.
Only presentation issues remain, all minor.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1403/work/decode.py` ran and the source hashes passed. Its output matches the
   round-2 table in SOLUTION.md line by line. It reports 41 shifted letters in the body and 10 in the closing.
2. **Independent decoder.** `review/work/r2/indep2.py` is my own Caesar −1 code, applied to my own reading of the shifted
   words. It gives MY OWN BOY / I AM SO SORRY / I CAN'T WRITE / LETTER / "TO-NIGHT" / MY YOUR / GIRL,
   which is 51 shifted letters (= 41 + 10, matching the solver). It also confirms that 1908-02-07 was a Friday (heading "C. H. Friday",
   postmark WIMBORNE 10 PM FE 7 08).
3. **Pixels.** I made new crops from `review/work/rot.png` with autocontrast, enlarged 4–6× (`review/work/r2/`):
   - `line1.png` and `line1c.png`: N-z, P-x-o, then a cursive E with a dot, a separate tall l with a dot, then a looped C and p, followed by
     the final z (visible on the unenlarged rot.png). There is no f/b/s, so `E. l. Cpz` is confirmed.
   - `line4.png`: a lead-in m, a long descending f, two minim pairs (uu), a second long f, and a small detached
     s with a period, giving `mfuufs`. Confirmed.
   - `line5.png`: `up-ojhiu`. Confirmed (sample of an ordinary row).
   - `close1.png` and `close1a.png`: the first token is an N followed by a small r/z-like sign and a dot, so `Nz` is plausible but
     not certain, as the solver says. Then come `N.`, an ampersand, `L.`, and `2pvs` = `Zpvs` (clear), followed by a faint
     P-like diagonal and a long thin stroke. Nothing legible beyond that, so restoring it as [OWN] is correct.
   - `close2.png` and `close2w.png`: an E-shaped sign (reversed-3 form), a tall l, then `Hjsm`. These are written over the printed
     publisher line, but the letters are distinct.
4. **Key coverage.** Every alphabetic token outside the literal abbreviation groups decodes under −1. No
   token needs another value.
5. **Language and context.** The language is ordinary Edwardian English. "Can't write letter to-night" drops the article,
   which matches the same writer's "thanks very much for letter" on hcp-1386. The pairing of the Boy salutation with the Girl signature, and the
   addressee Mr W. Abbott, Stokelake Farm, Chudleigh, S. Devon, fit the sister cards hcp-1386…1407.
6. **Honesty.** The portal status was Not solved, with no attached transcription or solution. The key is credited as a sister-card
   hypothesis. The earlier GPT work and the Claude completion are separated into their own sections.

## Findings

### 1. Superseded text is still at the top of SOLUTION.md. Severity: minor
The first sections still show `Efbs`/DEAR, `npsf`/MORE, "40 letters", "Gender and identity are not
established", and "YOUR OWN" without brackets. The round-2 section says it supersedes them, which is acceptable. However,
the report and the register entry must use only the round-2 reading.

### 2. The final "Reading:" line in decode.py is hard-coded. Severity: minor
The last plaintext line printed by `decode.py` is a fixed string. It is not built from `transcription.json`, so it would
not change if the transcript changed. The per-line output above it is computed, and it agrees with that string.

### 3. Notation is inconsistent between the body and the closing. Severity: minor
The body writes `{E.} {l.}` but the closing writes `E. l.`, and SOLUTION.md also uses "El." and "E. L.". These all refer to the same group.
A single notation is recommended in the report. In the closing the dots after E and l are not clearly visible on my
crops, so this group is a reading by analogy with line 1. That is fine, but it could be stated.

## Could not verify

- The meaning of `E. L.` and `N. & L.`, and whether they are plain or shifted. They are reported literally, which is correct.
- The faint word after YOUR. [OWN] is a contextual restoration only and is labelled as such.
- Whether the first token of the closing is `Nz` (MY) or `Nr`. It is marked as probable.
