# HCP 949 solver notes

2026-10-28 UTC. Solver collaborator, only this cipher. README fully read before work. User's persistent override forbids watchers/reviewers; none started. Root owns any eventual DONE. No markers, PDF or register entry created.

## Source inspection

Original scans downloaded by root after rendered all-three-tab inspection. Both viewed directly. Woman's portrait on picture side; angular cipher and ordinary cursive on address side. Cursive and cipher are oriented differently. Address names Erna Garbe in Reddelich. Source files left unchanged. Hashes are preserved in the manual inventory and verified by decoder.

Working crop `rotated.png` = original address pixels `(10,12,475,610)`, rotated90CCW, dimensions598×465. Inventory coordinates use that crop and approximate original coordinates `(475-y,12+x)`; one-pixel convention differences and loose centering are expected. The original pixels remain authoritative.

## Attempts and corrections

1. Viewed 90CCW orientation with ordinary cursive upright. Initial seven-shape pattern and greeting context suggested LIEBSTE, but shape repetition/segmentation did not support a fixed key. Rejected, not a plaintext claim.
2. Manually inventoried 35 body graphic units (including three detached short strokes), plus five margin forms. Created arbitrary-label substitution screens, same existing German4gram model and screen implementation as HCP1017, without plaintext input. Direct best `tzweisteboomungodellinerschateandis`; reversed best `adinserschabendtteilungollveradempr`. Neither is a reading or evidence that the true text is absent.
3. Agent962 independently reported the standard omitted-J pair-filled family. Tested generic pair/block alphabets, alphabet shifts/reversal, grid/X dihedral orientations and sequence direction:26,112 cases. Initial best pair180+reversal gave a conspicuous HASTDUDICHGUTAMMUS prefix. This actual scan was then rechecked in the correct orientation.
4. Found an implementation error: the 25-letter alphabet's unused final dotted wedge was wrapped toA by modulo. Corrected to unknown and regenerated all screen outputs. The candidate no longer wins purely by fourgram score. The clear source-supported opening remains, while the output cannot be promoted by score.
5. Rechecked the bracket immediately after central K in `ammus-controls.png`: three-sided bracket appears M, not initial Q. Updated manual inventory and reran screen/decoder. No repair to AMUSIERT.
6. Root personally viewed central and two later marked boxes and confirmed visible interior marks. Ordinary DICH has a contrasting unmarked I box. Root's agreement is shared solver work, not independent review.
7. Held-out margin turned separately (`margin-horizontal.png`): first two shapes fit GE under the same table; remaining three overlap cursive and have corner/wedge alternatives. This is a limited held-out check, not a complete word.

The finite screen covers only its listed families/orientations, and segmentation assumptions are fallible. Failure of other screens is not a general cryptanalytic exclusion.

## Residual issues

Mechanical draft: HASTDU[stroke]DICH / GUTAMMUSKMTBEKK[nonstandard dotted wedge]U[stroke]HAURF[stroke]. The B under a crossed patch is provisional. Possible intended words amüsiert and zu Hause are attractive, but they do not override dots/corners. Letter count is not finalized. Five marginal forms remain only partially classified, and a canceled hatch is not interpreted as a letter.

A generic Freimaurer-alphabet search was made; results included university teaching descriptions from Saarland/Wuppertal and a Freimaurer-Wiki variant overview. No target-specific plaintext was found or used. These search snippets supplied no assignments beyond the family already communicated by agent962. Actual search URLs: https://infolab.cs.uni-saarland.de/wp-content/uploads/2024/10/1-Freimaurer-Chiffre-Beschreibung.pdf ; https://ddi.uni-wuppertal.de/files/hashed/81f540a81c87a51706b521052c9c3788/substitution-m-freimaurer-station.pdf ; https://www.freimaurer-wiki.de/index.php/Geheimschrift . No local source file or external solution was imported.

## 2026-10-30 UTC – re-check by Claude Opus 5.5 (solver role, orchestrated run, no watcher)

Re-read every sign from fresh enlarged crops of `source/address.jpg` (crop (375,20,480,610) rotated 90° clockwise, 6–16x; margin crop (150,5,480,80) rotated 180°). Key = the omitted-J pair-filled Pigpen already recorded in SOLUTION.md (┘ A/B, ⊔ C/D, └ E/F, ⊐ G/H, □ I/K, ⊏ L/M, ┐ N/O, ⊓ P/Q, ┌ R/S; V T/U, > V/W, < X/Y, Λ Z).

Literal sign-by-sign reading (dot = dotted form):

- Short line: ⊐· ┘ ┌· V ⊔· V· ⊔· □ ⊔ ⊐· , = **HAST DU DICH,** (sound).
- Long line: ⊐ V· V ┘ ⊏· ⊏· V· ┌· ⊡ ┌· V | ┘·(with an x-hatch over/below it) └ ⊡ [⊏· or ⊡, right wall hidden under cursive "Erna"] Λ· V· [short dash] ⊐· ┘ V· ┌ └· [short dash]
  = **GUT AMMUSKST B(?)E K M/K [dotted Λ] U HAURF**.
  Correction to the earlier inventory: the sign after the central ⊡ is a dotted ┌ (= S); its "foot" is only the pen start, the bottom wall of ⊏ is absent. So AMMUSK**S**T, not AMMUSKMT.
- Top margin (read upright after a 180° turn, a full stop after the last sign): ⊐ └ [# cancel hatch] ⊐· └· ┐ . = **GE # HFN.** The thin line through the 4th sign is a cursive hairline, not a wall; the dot is clearly inside └ (F).

Interpretation attempt. The cursive body says "Muß noch anfragen ob du gut nach Hause gekommen bist", so a cipher sentence about having enjoyed oneself and about "zu Hause" fits the context. With the writer's dots taken as unreliable on three cells only (└ E/F, □ I/K, ┌ R/S) and a dotted Λ taken as Z, the text could be "HAST DU DICH, GUT AMMÜSIRT BEI K./M. ZU HAUSE … GEHEN." But that needs at least six dot errors (I→K twice, R→S once, S→R once, E→F twice), an unexplained extra dot on Λ, and the sign after BE(I) is M or K. The same cells are dotted correctly elsewhere on the card (I in DICH, S in HAST/AMMUS, E in BE/GE), so this is not a consistent alternate key but ad-hoc correction. Under the task standard ("do not force words onto noise", restorations only for physically hidden signs) this is NOT a complete reading.

Status: partial. Secure: HAST DU DICH, GUT AM(M)ÜS… ; the rest is a complete literal transliteration whose plaintext requires assumed writer errors. No marker created.
