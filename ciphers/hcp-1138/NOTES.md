# Notes hcp-1138

2026-11-02: captured by Claude Opus 5.5 (orchestrator).

2026-11-02 (Claude Opus 5.5, solver): read the whole address side from rotated strips (`work/strips.py`, `zoom.py`, `zoom2.py`; rotation 48 degrees, 3x and 4x on `work/hires`). Everything on the left half is cipher except `Kívánom:` and the place and date. Started from the hcp-1174 / 1178 / 1179 key. New on this card, each found from words: `6` = j (szedjétek, hagyjatok, jó, jól, teljen), `6.` = ny (nyugott, hernyót), `4.` = gy (hogy, úgy, vagyok, ángyika, hagyjatok), `.1` with dots to the left = u (úgy, rosszul, nyugott, májusba), `2` = c (lehec, once), `4` = f confirmed (fognak, megfáztam).
Traps: long strokes under digits are commas of the sign above-left, and they reach into the next row. Strip overlaps made me double a 7 in `jó kevesem`; corrected. `7 1,` in májusba: the uncrossed sign is a 1 with its comma, not a 7. `1. 5, 1. 9 0 7, 1. 6,` was first forced as z (lazosan), then read with the table p: alaposan. Plain 9 stands for z three times (azokat, aztán, házi).
Dead end: `0 1, 1.` (oba) before alaposan. Tried bál-, öbl-, ebbe, óba, a cut comma on the 0 at the card edge. Not resolved; stays literal.
Open phrase: `házi nézni hogy akkor ra lenne`: every sign read, sense only tentative.

2026-11-02 (Claude Opus 5.5, solver, after review 1): the review was right. `work/crops/rot48.png` came from a cut image, so its diagonal crop edge looked like the card edge and rows 9, 10, 11 were read short by 12 signs. That caused `oba`, `házi`, `többe` and "no nem". Lesson: check the crop against the whole scan before calling anything a card edge. Also fixed `lejönne`, `tolmácsolja`, `üdvözöl és`, `8.` = ty (FINAL hcp-1142, 1146, 1164 agree). New full view: `work/rot_full.py`, `crops/full51.png`, `rowends.png`, `row13.png`. Transcription now equals the reviewer's own decode in all 409 signs. Reading changed substantially, so DONE2.

2026-11-02 (Claude Opus 5.5, solver, after review 2): `akkor ra` was my own false word break; it is `akkorra`, by then. The clause I had called tentative was simply misdivided. Lesson: when a clause of plain words will not make sense, test the word breaks before calling it obscure. Grey dot on the first 7 disclosed as a smear, read by sense. Words 84, signs 409. Going to FINAL.
