REVISE

# Review 1 — HCP1543 / pc_hcp_224 (Anna Tichá family, 17.VIII.1903)

Reviewer: Claude Opus 5.5, 2026-10-29. Scripts and crops: `review/work/`.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1543/work/decode.py` runs and prints
   `CHECKS OK: 14 rows; 359 transcribed units ...`. Its output matches
   `work/plaintext.txt`, but that output still contains `HRA[UNK1]E` and
   `SRDE[UNK2]KO` (see finding 2).
2. **Independent decode.** `python3 -I review/work/mydecode.py work/transcription.json`
   applies the family key (same table as hcp-1545 family: 1Y 2U 3O 4I 5E 6A 8L bP cS
   dT fV gK hR mN nM pB qZ rH sC tD y/7 J, H/ř CH) to every row of the record. All
   14 rows reproduce the solver's literal plaintext. 359 units, 0 unmapped signs.
   The key covers the whole record and gives continuous, idiomatic 1903 Czech
   (nedoručovalo, rmoutí mne, stůně, sodovou vodou, šetři se, vyřiď ... poroučení).
   Date, Prague/Jindřichův Hradec, Janková (the host named on the address side) and
   the signature Pepouš all fit the family. Not a forced reading.
3. **Scan checks** (own crops from `source/picture.jpg`, rotated 90° clockwise,
   4–8× LANCZOS: `review/work/upright.png`, `r01.png`, `r04.png`, `r06.png`, `u1.png`,
   `u2.png`, `r01name.png`, `zctrl.png`, `c_controls.png`, `R02a/b.png`, `R05a.png`,
   `R07b.png`, `lower.png`). Rows R02, R04 (outside the blot), R05, R06 (outside the
   blot), R07 (second half), R10–R14 agree sign by sign with the record. I found one
   omitted sign in R01 (finding 1).
4. No published solution for this card was found or claimed. The family key comes
   from earlier cards and Egorov's partial study, and that is credited.

## Findings

**1. (major) R01: a sign is missing from the name. It reads ANIČKO, not ANIKO.**
At 8× (`review/work/r01name.png`) the word is `6 m 4 s g 3`, not `6m4g3`.
Between the `4` (I) and the looped `g` there is a narrow upright sign with a small
top hook. It is the family `s` = C, the same shape as the C in R03 `fs5h6` (VCERA),
R04 `fs5h6`/`f5s5h` and R05 `m5t3h2s3` (`review/work/c_controls.png`, `R05a.png`).
With it the word is ANICKO, i.e. *Aničko*, the normal vocative of *Anička* for
Anna Tichá. That also removes the stated g/K-vs-q/Z doubt: ANIČKO needs K, and
ANIČZO is not Czech. The record needs a fix: R01 cipher `6m4sg3`, plaintext ANICKO,
unit count 360, positions.csv, plaintext.txt, hashes, and the uncertainty item 1
and the editorial/Slovak texts ("Rozmilá má Aničko").

**2. (major) The "complete reading" is not reproduced by the single command or the
record.** The 2026-10-29 completion section promotes the card to complete
(HRADCE, SRDEČKO). But `work/transcription.json`, `work/plaintext.txt` and
`decode.py` output still print `[UNK1]`/`[UNK2]`. The header and the earlier
sections still say "substantial partial decipherment". SOLUTION.md must have one
consistent status. The command must output the plaintext being claimed, with
restorations marked in it, for example `HRA{D}[C]E` / `SRDE[Č]KO`, or a stated
convention.

**3. (major) R06 `SRDE?KO`: the stated basis for C is wrong. The C is a contextual
restoration, not a read sign.** At 8× (`review/work/u2.png`) the sign between `5`
and `g3` is a heavy closed round bowl. A long oblique stroke runs through it from
upper right to below the baseline (like `ø`). The family C (`s`) on this card is a
narrow upright stroke with a small hook and no bowl (finding 1 controls). The
solver says "Its bowl and hook are those of the family `s` (C)", but the sign does
not show this. It looks like an overwritten or struck sign. *srdéčko* is almost
certain from context and fits one sign position, so keep it. Label it as an
editorial restoration (`SRDE[Č]KO`), not as a reading "from the sign's shape". The
háček interpretation of the stroke is speculative. Delete it or mark it as such.

**4. (minor) R04 HRADCE: D is supported, C is a restoration and correctly
disclosed.** At 8× (`review/work/u1.png`) a crossed, looped `t` (= D, same form as
`t3c58` DOSEL in the same row) is visible right after `rh6`. It is followed by a
dark blot about one sign wide and then `5`. The solver states that C is only the
letter that makes the town name. That is fair. Show it in the literal output as a
restoration (finding 2).

**5. (minor) Editorial inconsistencies.** The completion text has *poroučení*,
the earlier section *poručení*. The cipher is PORUCENI, so use *poručení* (or note
the normalisation). The completion has *srdéčko* in Czech, the literal is SRDECKO.
That is fine, but say the é is editorial. Two different Slovak translations stand
side by side. Keep one. "Velectěná" etc. on the address side is fine.

**6. (minor) Unit counts and the uncertainty list need updating** after
findings 1–3 (360 read units incl. the restored C's). Some of the prose about
"361 record slots" and "less-secure g/K" will be obsolete.

## What I could not verify

- The cipher content under the two blots: no stroke-level recovery of the C in
  HRA D?E or of the struck sign in SRDE?KO was possible at the available
  resolution (1024×674 JPEG).
- I did not sign-check every row. Rows R03, R08, R09 and the first half of R07
  were only checked at 2× overall view (R09 is crossed by background art). My
  independent decode checks the record, not the pixels, of those rows.
- Accent marks over CH/PUS in R07/R09 were not interpreted, the same as the solver.

## Summary

The decipherment (Anna Tichá family key, Czech, Pepouš → Anna Tichá, 1903) is
correct, and the key covers the whole text. Before FINAL: add the missed C in the
name (ANIČKO), regenerate record/command/plaintext so they match the claimed
complete reading with restorations marked, and relabel the R06 Č (and R04 C) as
contextual restorations.
