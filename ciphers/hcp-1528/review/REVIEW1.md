REJECT

# Review 1 — HCP 1528 (pc_hcp_209), Anna Tichá / Pepouš family

Reviewer: Claude Opus 5.5, 2026-10-29. Round 1 (marker DONE1).

The key is correct and most of the card reads as claimed. But rows R12–R14 are
transcribed wrongly in the solver's record. The claimed plaintext contains words
that are **not on the card** ("SVYM ZLATUCKOVI", "JAKY", "KDE BY", "?ARMOUTIS").
The pixels say "ZE SVIN OPET TAKOVY / LISTEK, JAKO POSLEDNE, KTERY MNE /
ZARMOUTIL". On top of that, the single reproduction command does not produce the
completed reading that DONE1 hands over. The plaintext must be re-transcribed and
checked again (DONE2). It cannot be accepted with a list of local fixes.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1528/work/decode.py` runs (exit 0). Its output
   is saved in `review/work/solver_decode_output.txt`. It prints the **old partial record**
   with gaps [U1]–[U8], plus "SVYM ZLATUCKOVI", "KDE BY MNE" and "[U6]ARMOUTIS". The
   "Completion and handover" readings (BYLO, BYLA BY MNE, HEZKY SE VE SVINECH BAV…,
   VYRID PROSIM SLECNA JANKOVA, PORUCENI NEPOSLI, Z/I/K) are given only as prose in
   SOLUTION.md. They are not in `work/transcription.json` or in the command's output.
2. **Independent decoder.** `review/work/review_decode.py` uses a key typed in by hand and
   my own sign-by-sign transcription of all 18 rows, read from 3–6x crops of
   `source/picture.jpg`. Its output is in `review/work/review_decode_output.txt`. It covers
   about 564 key signs. Only a few are unsecured, and two places are hidden under the
   engraving.
3. **Crops checked** (all in `review/work/`): r5_6, u7, i_ctrl, j_ctrl, q_ctrl, r7_9,
   u3_hezky, u3_end, r10_12, r10, r11, r12, r12a, r12b, r13, r14, r13_18, r16, r04a, r02b,
   krku.

My reading (literal base letters, editorial spacing):

```
VRELY DIK ZA DRAHY LISTEK. POSLECHL JSEM SVE SRDECKO A ZUSTAL JSEM
JESTE DOMA. JE MI JIZ O HODNE LEPE, AVSAK DOSUD PLICE A KRK? NE-
JSOU UPLNE V PORADKU. V PONDELI ZEPTAM SE LEKARE, ZDA MI DOVOLI
JIZ JITI DO URADU. JO MI NYNI NEMOC VERUSE NEVHOD. ABY ME SRDECKO
STONALO KE MNE, BYCH ZA ZADNOU CENU NECHTEL. I? BYL BYCH SI VSAK PRAL
KDYZ MNE TAK HLAVA BOLELA, ABY MNE [..] BYLO ME SRDECKO ASPON
NA CHVILI PRISLO, POLOZILO SVOU RUCKU
NA HLAVU, BYLA BY MNE JISTE BOLESTI
PRESTALA. HEZKY SE VE SVINECH BAV[..]
A VYRID, PROSIM, SLECNA JANKOVA
ME UCTIVE PORUCENI. NEPOSLI
MI VSAK ZE SVIN OPET TAKOVY
LISTEK, JAKO POSLEDNE, KTERY MNE
ZARMOUTIL. SRDECNY POZDRAVA
TISIC DLOUHYCH, VASNIVYCH PUS
POSILA TI TVUJ PEPOUS,
KTERY STALE VRELE
VZPOMINA.
```

“…Nepošli mi však ze Svin opět takový lístek jako posledně, který mne zarmoutil.”
This sentence is fully coherent, and it continues the Sviny theme of R09. The address
side (Trhové Sviny) and Slečna Janková in R10 support it too.

## Findings

1. **blocker — R12 is wrong. "SVYM ZLATUCKOVI" is not on the card.** The record has
   `n4 fc6g {U8}5 cf1n q86d2sg3f4`. The scan (r12.png, r12a.png, r12b.png) clearly shows
   `n4 fc6g q5 cf4m 3b5d d6g3f1`, which reads MI VSAK ZE SVIN OPET TAKOVY. There is no
   sequence `q86d2sg3f4` anywhere in R12. The editorial "ke svým [= svému] zlatoučkovi"
   and its interpretation of an "affectionate" term are therefore invented. They are not a
   misreading of an ambiguous sign. The third sign of `cf4m` has the 4/I form (as in
   `n4`), not the 1/Y form at the end of `d6g3f1`.
2. **blocker — R13 and R14 are wrong.** The record has `84cd5g, 76g1 b3c85tm5, gt5 p1 nm5`
   (JAKY … KDE BY MNE). The scan (r13.png) shows `84cd5g, 76g3 b3c85tm5, gd5h1 nm5`,
   which reads LISTEK, JAKO POSLEDNE, KTERY MNE. In R14 the record has
   `{U6}6hn32d4c` (…ARMOUTIS). The scan (r14.png) shows `q6hn32d48`, which reads
   ZARMOUTIL. The last sign is 8/L, not c/S. The editorial "kde bys mne zarmoutíš" is a
   grammar-forced reading of a misread row.
3. **major — U8 resolved wrongly.** The handover weakly prefers KE (g/K). The sign before
   `5` in R12 (r12a.png) is the open-topped "9" form of q/Z, as in `q6` ZA in R01
   (q_ctrl.png). It is not the closed-loop g of `fc6g` right next to it. So it reads ZE,
   which is required by "ze Svin". U6 is likewise q/Z (ZARMOUTIL), as the solver
   concluded, but the word ending is wrong (finding 2).
4. **major — The reproduction command does not produce the handed-over solution.**
   README step 4 requires a single command that produces the full plaintext. `decode.py`
   still reads the 492-unit partial `transcription.json` with eight gaps and prints the old
   errors. None of the completions are encoded. The solver must update
   `transcription.json` and positions, and the hashes the decoder checks, so that the
   command prints the final reading.
5. **minor — R16 TVOJ should be TVUJ.** In `df?7` (r16.png) the sign has the looped
   z-like form of 2/U, as in `2sd4f5` (R11) and `t832r1ř` (R15). It is not the 3/O form of
   `b3c486` in the same row. The SOLUTION claim that the source "has a 3/O rather than the
   2/U" is not supported. Reading TVUJ (tvůj).
6. **minor — Sviny location.** The handover says Sviny is "a small town near Veselí nad
   Lužnicí". The address side of this card names Trhové Sviny, which is near České
   Budějovice. "Ve Svinech" / "ze Svin" refers to the town where the addressee is staying.
   The context sentence must be corrected.
7. **minor — Disclosed restorations that may stand, but must be labelled in the
   record.** U3 BAV[ILA]: the visible ink ends `p6f`, and the rest is under the tree
   (u3_end.png). The ending is unknown: bavila, bavíš and others are possible, so it must
   stay a marked restoration. U3 HEZKY: the two middle signs (u3_hezky.png) sit on dark
   engraving. q+g is plausible but not certain. U1: only `p183` (BYLO) is visible after the
   foliage blot. Nothing proves the blot hides no sign. U7 "I": the sign is small and
   partly in foliage (u7.png). Its shape fits the 4/I form better than the long-descender
   7/J (i_ctrl.png), so I is acceptable as probable. U2 `p186 p1 nm5` and U4/U5 are
   legible and confirmed.
8. **minor — R02 "KRKU".** The last sign of `ghg?` (krku.png) is a g-like sign with a
   trailing hook. It is not a clear 2/U loop. Flag it as uncertain (KRK + ?) and do not
   assert KRKU.
9. **minor — Stale text.** SOLUTION.md still contains the "PARTIAL … No DONE … warranted"
   preamble, the old editorial texts and the Slovak translation (with ZLATUCKOVI, KDE BY,
   [U#] gaps). These contradict the handover. The final SOLUTION must have one consistent
   plaintext, translation and uncertainty table.

## Confirmed as correct

- The key (family key from HCP 1520–1525, credited to earlier cards and to the published
  generic partial key of M. Egorov) decodes every sign I read. No sign needs a new
  assignment.
- R01–R11 and R15–R18 match my reading, apart from the details in findings 5, 7 and 8.
  Sample rows R01, R02, R04, R05 and R13–R18 were checked sign by sign.
- The signature PEPOUS, the date 5 Dec 1903, the recipient Anna Tichá, the reference to
  Slečna Janková (who matches the address side) and Sviny all fit the context. This is
  real Czech of the period.
- Source disclosure: the prior published partial key is credited. The portal shows no
  solution attached, and pc209 is absent from the published family readings according to
  SOURCES.md.

## Could not verify

- I did not re-open the live portal or Egorov's page; I relied on SOURCES.md.
- Signs hidden under foliage (U1 blot, end of R09) cannot be read from this scan.
- Diacritics are not transcribed by the solver, and I did not check them.
