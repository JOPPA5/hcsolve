REVISE

Reviewer: Claude Opus 5.5 (`claude-opus-5-5`), 2026-10-11. Round 1 of `hcp-357`.

The solver claims no solution: "No plaintext or key has been recovered." I agree with that outcome, and it must stay that way after the revision – **no register entry, and the report must say "unresolved"**. The verdict is REVISE rather than ACCEPT because two statements in the write-up are stronger than the evidence, and one piece of evidence that bears on the indicator was missed.

## What I verified

**Transcription.** I read the 17 groups independently from `source/cryptogram.jpg` and `work/body-enlarged.jpg` before comparing. My reading matches `work/transcription.txt` in all 85 letters. The two places where I would not rule out an n/m confusion are group 5 (`ddnmn`) and group 10 (`hndei`); the solver flags only the first.

**Statistics.** Recomputed: 85 letters, IC 0.05742 (full) and 0.06234 (group 3 removed). Group 3 `qcbzu` does hold the only `q`, `b` and `u` in the message. All as stated.

**Checksums.** `source/cryptogram.jpg` and `work/quadgrams.tsv` match the SHA-256 values given; the quadgram table is byte-identical to the one in `hcp-393`.

**Reproduction.** `review/work/run.sh` copies the solver's inputs and code, rebuilds and reruns everything. All eight output files are byte-identical to the ones in `work/` (see `review/work/run-output.txt`). The stored results are what the code produces.

**Cited paper.** I read section 2.2 of Antal, Zajac and Grošek (HistoCrypt 2020, pp. 22–23). It supports the solver's summary: triple columnar transposition, three daily permutations arranged by a number *n*, *n* converted to a five-letter group and inserted at a position *ip* known to both sides.

**Honesty.** No published solution is used or hidden; the portal attaches none. The best candidates are correctly described as incoherent.

## Findings

**1. The multi-stage search cannot support any conclusion – major.**
`review/work/control.py` plants three Slovak 80-letter plaintexts, encrypts them with keys *inside* the searched space, and runs the solver's own binaries.

| Cipher | Recovered | Best score found | Score of the true plaintext |
|---|---|---|---|
| single columnar, width 11 | 3 of 3 | 234.1 / 198.6 / 243.0 | 234.1 / 198.6 / 243.0 |
| two stages, width 18 | 0 of 3 | 181.6 / 187.6 / 183.5 | same as above |
| three stages, width 18 | 0 of 3 | 176.2 / 168.6 / 202.7 | same as above |

So the single-columnar search works, and its negative result is real evidence against a single columnar transposition of width 2–30 (given the transcription). The two- and three-stage search never finds a plaintext that is known to be there. Its best score on the real ciphertext, 176.7, is the same as the false optima it reaches on the controls. NOTES.md calls these runs "broad controls"; they are not evidence either way and the write-up should say that in plain words.

**2. The header is not "unknown": it is a digit followed by the letter count – major.**
Across the telegrams already transcribed in this batch:

| Cryptogram | Header | Letters in body |
|---|---|---|
| hcp-357 | 685 | 85 |
| hcp-393 | 3100 | 100 |
| hcp-396 | 755 | 55 |
| hcp-399 | 5245 | 245 |

The trailing digits equal the letter count in all four. That confirms the transcription length and leaves one leading digit (6, 3, 7, 5) unexplained. It is not the day of the month (dates are 15 March, 7 August, 7 August, 10 August).

The paper says the receiver must know the position *ip* of the indicator group. The leading digit is an obvious candidate for *ip*. For this message that would make the indicator group 6, `tooip`, not group 3.

The paper's rule constrains what an indicator can look like: a one-digit *n* gives five different digits, so five different letters; a two-digit *n* gives the digits *a b 0 a′ b′*; and the same letter always means the same digit. Checking the group at the header digit's position in each telegram, using the solvers' transcriptions:

| Cryptogram | Digit | Group at that position | Possible indicator? |
|---|---|---|---|
| hcp-357 | 6 | `tooip` | yes – repeated `o` forces *b* = 0, so *n* is a multiple of 10 |
| hcp-393 | 3 | `vbktv` | yes – e.g. *n* = 10 (digits 1 0 0 1 1) |
| hcp-399 | 5 | `orlvj` | yes – five different letters, one-digit *n* |
| hcp-396 | 7 | `cscnu` | no as transcribed; yes if the first letter is `o` (`oscnu`) |

In hcp-396 the solver had already marked the first letter of group 7 as uncertain between `c` and `o`, without knowing this constraint. The rule picks `o`.

This is consistent in four telegrams out of four, but it is weak evidence on its own: a random five-letter group passes the test fairly often. It is a hypothesis to record and test, not a result. The annealing attacks here were only run with group 3 removed and with nothing removed.

**3. The case for group 3 as the indicator is weaker than stated – minor.**
The same paper says proper nouns, abbreviations and times in the plaintext are separated by the letter Q, and sentences may end with X. A `q` in the body is therefore expected in an R/XQ message and does not point to the indicator. What remains is that group 3 holds the only `b` and `u`; in 80 letters of Slovak that is unusual but not rare. SOLUTION.md already says "neither claim is established"; NOTES.md should not present the Q/B/U observation as support without this caveat.

**4. Facts in the cited paper that the search ignores – minor.**
The paper gives a maximum password length of 22 for R and message lengths of 50 to 250 letters, and does not say the three permutations have equal length. The multi-stage search assumes equal widths 16–22. NOTES.md does disclose the equal-width limit; it should also say that the paper gives no reason to expect it.

**5. Source record is incomplete – minor.**
- `SOURCES.md` shows the saved image is the portal's `-large` conversion (1024 px wide), not the original upload. It is legible, but say so, and fetch the original if the portal offers it.
- `source/metadata.md` omits what is visible on the scan outside the cipher body: the handwritten note with the time 17.45 and the two date stamps "15. III. 1944".

## What I could not verify

- Whether the system is R/XQ at all. The letter statistics fit a transposition of Slovak text, nothing more.
- The meaning of the leading header digit.
- The transcription against the original-resolution scan, which is not in `source/`.
- Whether the message is solvable without the daily key. A triple transposition of 80 letters with unknown keys is beyond what these searches can test, and I know of no method that would do it.

## What the solver should do

1. Rewrite the "Reproducible attempts" and "Result and limits" parts of NOTES.md, and the matching sentence in SOLUTION.md, to separate the single-columnar negative (valid) from the multi-stage runs (no evidential weight), citing the control.
2. Record the header pattern and the group-6 hypothesis. Rerun at least the single-columnar attack with group 6 removed, and report the result whatever it is.
3. Fix findings 3 to 5.
4. Keep the outcome as unresolved. Write the PDF report as a record of a failed attempt; do not write `register-entry.txt`.

None of this changes the solution, so a second review round is not needed unless a plaintext turns up.
