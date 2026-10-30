REVISE

# Review 1 – HCP 1571 / pc_hcp_252 (Anna Tichá family, Pepouš → Anna, 20 Dec 1902)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Role: reviewer, round 1.

## Summary

The reading is correct in substance: a fixed-key monoalphabetic substitution (the Anna Tichá / Pepouš family key, with a marked r-sign for CH) yields a coherent Czech love letter that fits the card's date (Christmas greeting, "svátky", 20/XII.1902), the recipient (Anna Tichá, teacher in Žirovnice) and the sender signature (Pepouš) known from the sister cards. I checked the transcription against my own enlarged crops of the scan and found one word where the transcription does not follow the pixels (R09 ZDA, which reads KDY on the card), plus a missing-háček note. These need correcting before FINAL, but the reading as a whole stands.

## What I verified and how

1. **Reproduction command** (from repo root):
   `/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -I ciphers/hcp-1571/work/decode.py`
   It prints the 13-row literal block, identical to the SOLUTION.md block, with PASS lines (475 active units, 8 CH, 483 letters, 22 labels).
2. **Key**: `work/key.json` is the same as `ciphers/hcp-1520/work/key.json` and `ciphers/hcp-1545/work/key.json` (only the label for J differs: `y` here, `7` in 1545; it is the same 7-shaped sign). It is the established family key, credited as such. This is not a new key.
3. **Independent decode**: `review/work/indep_decode.py` (my own hard-coded key table, read separately from the solver's code) applied to the `cipher` strings in `work/transcription.json`: all 13 rows reproduce the claimed plaintext, 475 units in total, no sign outside the key. So the key covers the whole transcribed ciphertext.
4. **Transcription vs scan**: `review/work/crops.py` rotates `source/picture.jpg` 90° clockwise (674×1024) and makes 4× crops of every row (`review/work/R01_0.png` … `R13_1.png`). I also made 6–12× zooms and contrast panels for specific signs (`R11verb.png`, `R03mid.png`, `R10_0.png`, `R05a.png`, `R09zda_hi.png`, `gq_compare.png`, `R02bych.png`, `R12.png`, `R13.png`). I read R01–R13 sign by sign. Ordinary rows R01, R02, R03, R04, R05, R06, R07, R08, R10, R11, R12, R13 agree with the transcription, apart from findings 1–2.
5. **The flagged/corrected points**:
   - R11 `h3q5qf2s586` ROZEZVUCELA: on the pixels, units 3 and 5 are the same closed-head "9"-shaped sign (q/Z) and differ from the open g/K in SKVOSTNOU on the same row; unit 8 is the angular s/C; unit 7 is a clear `2` (U). **ROZEZVUCELA = rozezvučela** (from "rozezvučet") is correct, grammatical Czech. The solver's correction of the earlier ROZEKVUTELA is supported by the pixels and not forced.
   - R03 `nm5` MNE: a narrower n-sign followed by a wider m-sign is visible; MNE is right.
   - R10 `6md48g5n`: the third sign is the top-barred d (same as the final sign of TAKOVYMTO), so the literal ANTILKEM is correct. The writer's slip for *andílkem* is correctly marked as editorial.
   - R05 `d5c4s` TESIC: the last sign is the angular s (C). The literal is right; *těšíš* is editorial and is disclosed.
   - R11 underlined `d4` = TI (for *ty*): visible, disclosed.
   - R13 `f5sm5 df2y b5b32c` VECNE TVUJ PEPOUS: confirmed.
6. **Language/context**: the text is fluent Czech of c. 1900 (*přijeti s metlou*, *hodný shon*, *psánko*, *dušičko*, *děvenko*). It mentions spending the holidays in Prague and the office (*úřad*), which matches the other Pepouš cards. Andělka is a plausible person or pet name. No date or place conflicts.
7. **Sources**: the solver discloses that the family key was known in advance (hcp-1520, Maxim Egorov's partial study, pc199 reference). The portal shows no target-specific solution, and none was used.

## Findings

1. **[major] R09 "ZDA" does not match the scan; the card reads `gt1` = KDY.**
   Transcription: R09 `... t5m. qt6 n4 bc...` → "ZDA MI POSLES". In my crops (`review/work/R09zda.png`, `R09zda_hi.png`, panel `gq_compare.png`):
   - the first sign has the open head and looped tail of g/K. It matches g in JAK (R06 `y6g`), PSANKO (R09 `bc6mg3`) and AVSAK (R04 `6fc6g`), not the closed "9" of q/Z in ZA (R01) / PRAZE (R06);
   - the last sign is a clear `1` (Y), like the final `1` in CELY (`s581`) on the same row, not the looped `6` (A).
   The literal is therefore `gt1` = **KDY**: "Kdy mi pošleš slíbené psánko?" ("When will you send me the promised letter?"). This is just as idiomatic, and better than *zda*. The solver's reading changes two signs to fit an expected word. Fix the cipher string, the literal, the editorial text, the Slovak translation ("Kedy mi pošleš…"), and the positions/hash records. The unit count stays at 475.
2. **[minor] R02 BYCH: the r-sign has no visible háček.** In `review/work/R02bych.png` the third sign of `p1r` is a plain r. No mark is visible, while the other seven CH signs (R03 ABYCH, R04 VLASTNICH/SVYCH, R05 MYCH, R12 ×3) clearly carry one. Reading it as CH (BYCH) is right from context, but the literal is `p1r` (BYH). SOLUTION.md says all CH units are "marked". Record this as a writer's omission and a disclosed editorial CH, not as a marked unit.
3. **[minor] The bounded alternatives are over-hedged.** ROZEZVECELA (U/E at global 398) has no support on the pixels (the sign is a clear `2`). ROZEZVUCELA is also the grammatical form, so the report can drop this alternative or state it as not supported. MME as an alternative to MNE can be handled the same way.
4. **[minor] Attribution in SOLUTION/NOTES is unclear.** The documents talk about "root", "collaborator" and "helper" but never name the model(s) that did the reading. When writing the report and register entry, state truthfully who did the work (e.g. the GPT solver vs Claude), as the README requires.

## What I could not verify

- The family key's origin, beyond its agreement with the sister cards; I did not re-derive it.
- The postmark dates on the address side (not used).
- I checked every row at 4×, but at sign-by-sign high zoom only the flagged words and a sample. Very faint signs under the printed wheel (R08–R09 overlap area) may hold other small errors of the kind in finding 1. The solver should re-check R08–R09 against the pixels when fixing finding 1.

## Verdict

REVISE. The decipherment is correct and complete. Finding 1 (ZDA → KDY) must be corrected in all records, and finding 2 must be disclosed, before FINAL.
