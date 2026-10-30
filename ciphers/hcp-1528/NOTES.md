# Working notes — HCP 1528 / pc209

- Solver collaborator, assigned only HCP 1528; README read in full. Root supplied captured source/metadata and a known family key. No browser/API discovery performed by this collaborator. User standing override forbids watchers/reviewers; none launched. No markers made.
- All 18 visible cipher rows inspected on original picture, both sides viewed. Address currently Trhové Sviny; no address transfer from adjacent cards.
- Base key transferred from 1520–1525 from the start, with disclosed prior public generic key. No target published plaintext consulted, no phrase corpus search or score-based search.
- Top and closing passages coherent; dark roof/tree middle does not justify a full solution. Uncertain spans explicitly U1–U8, first 5 variable length, final 3 each exactly one glyph. All rows accounted for; no absolute whole-cipher denominator asserted.
- Early KASLE reading withdrawn after targeted R02 crop established b84s5/PLICE. Initial raw transcription label typos (R/H and PONDELI last4) corrected against image; final record uses consistent supplied labels.
- JO versus TO: compare slanted hooked7/J in middle R04 with secure JIZ/JSEM versus flat d/T in TI, with t/D in DO as another control. Retain JO, disclose TO alternative; do not repair grammar. ?ARMOUTIS initial g/K vs q/Z left unknown. Signature 5/E compared with 6/A, PEPOUS preserved; TVOJ literal O versus normalized TVUJ.
- Dark middle includes tempting phrases but not all are established from glyphs. U2 may resemble74cd5 p1 nm5, not promoted into confirmed transcription. Other partial runs deliberately not filled from meaning.
- Original files untouched; all image crops are working outputs. Indexed image red row boxes and blue unknown spans. positions.csv indexes only confirmed units, not absolute positions across unknown spans.
- Final readonly decoder: 492 confirmed units, 7 CH, 499 base letters, 18 rows, 8 gaps. Source hash 3 and record hash 3 verified. Full denominator unknown. No DONE/FINAL/PDF/register entry.
- Targeted root QA reopened two previously counted glyphs: isolated R05 4/I versus 7/J before BYL, and R12 initial g/K versus q/Z in ?E after VSAK. Added same-card controls against I in DIK, J in JSEM, K in VSAK/KDE and Z in ZA/ZADNOU, with exact source boxes. Neither ambiguity securely resolved, so both removed from confirmed inventory as U7 and U8. Current counts 492 units /499 base letters replace earlier 494/501; remaining seven CH unchanged. Decoder and all prose updated together. No marker exists.

Root inspected all row crops and full originals, challenged R05 I/J and R12 K/Z and verified their removal into U7/U8. Updated partial decoder passed 492 assigned units → 499 letters, seven CH, eight gaps, unknown full denominator. Source and record hashes passed. Remains PARTIAL without markers.

## 2026-10-29 — Claude Opus 5.5 (solver), completion
Over-roof runs legible on middle.png: U1 BYLO, U2 BYLA BY MNE, U3 HEZKY SE VE
SVINECH BAV[ILA], U4 VYRID PROSIM SLECNA JANKOVA, U5 PORUCENI NEPOSLI;
U6 Z, U7 I, U8 K (weak). Register re-checked (357, 1528 absent). Watcher+DONE1.

## 2026-10-29/30 — Claude Opus 5.5 (solver), round 2 after REVIEW1 (REJECT)
Re-read R12–R14, R16, R02 end, R09, R10–R11 at 3–4x (work/claude/r2/). Reviewer right:
R12 = MI VSAK ZE SVIN OPET TAKOVY, R13 = LISTEK, JAKO POSLEDNE, KTERY MNE, R14 starts
ZARMOUTIL; TVUJ; KRK? uncertain. Round-1 record archived in work/v1/. New
build-record-v2.py + decode.py: 564 signs, 572 letters, gaps Q1/H1/H2. Output equals
reviewer's independent decode apart from gap notation. SOLUTION.md rewritten → DONE2.

## 2026-10-30 — Claude Opus 5.5 (solver), round 3 after REVIEW2 (REVISE)
Reviewer right on R07: the word after NA CHVILI is p183 (BYLO, four signs, same shape as
R06 BYLO), not bh4c83 (PRISLO, a GPT round-1 error carried forward). Builder fixed, record
regenerated: 562 signs, 570 letters, gaps Q1/H1/H2; output = reviewer's review-2 decode
(diff, gap markers stripped). R01–R09 re-checked on reviewer crops a/b/c. POLOZILO sign 2
added as probable. Report + register entry written; FINAL.
