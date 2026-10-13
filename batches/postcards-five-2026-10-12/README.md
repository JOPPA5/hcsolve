# Five postcards: publication audit and decipherment progress

Date: 2026-10-12. Repository remains on main. Nothing pushed.

## Current outcome

| HCP | Publication audit | Local outcome |
|---|---|---|
| 975 | Exact card and readable decipherment published by Thomas on 2016-08-17; last surname qualified | Known public key mechanically reproduced on a new manual transcription; not a new AI solution |
| 1000 | Substantial exact-item partial published on 2026-09-08; complete reading still absent there | Known key and opening fragment checked; remaining joins unresolved |
| 1243 | No exact published solution found in bounded searches | Full main-message reading with shared graphic key; overwritten sign/final spelling qualified; plain cursive stamp note not fully transcribed |
| 1301 | No exact published solution found in bounded searches | Complete main and under-stamp messages read with shared key; independent review confirmed decipherment; requested documentary corrections incorporated; PDF and local register entry prepared |
| 917 | No exact published solution found in bounded searches | Four scouts plus targeted corrected-heading crib test unresolved; source classification remains uncertain |

The live AI Register showed 37 contributions. Search by 1243, 1301, 917, 975, 1000, jolanka, fritzsalmen, heidelberg and Jessze gave zero matches. This is a bounded observation, not proof that no solution exists anywhere. All five portal pages still showed Not solved; all three tabs and both scans were inspected.

## Reproducibility and evidence boundaries

`sh batches/postcards-five-2026-10-12/reproduce.sh` rebuilds the Hungarian models and scouts and runs the two known-key examples. `prepare.py` documents the tentative graphic labels. It does not create a source transcript from guessed plaintext. The source images are immutable, while all transformations and transcriptions are in each cipher's work directory.

Hungarian model: Universal Dependencies, UD_Hungarian-Szeged, training split, NFD folded to a-z; CC BY-NC-SA 3.0. https://github.com/UniversalDependencies/UD_Hungarian-Szeged . The synthetic substitution control uses 260 letters from the separate test split and a fixed random permutation. It recovered 260/260 letters exactly (`control-check.json`). The control is modern news language, not proof of historical-target success.

Scouts: 40 restarts × 30,000 proposals per run, weighted 3/4/5-grams. Target proposal totals: HCP1243 1.2 million; HCP1301 1.2 million; HCP917 4.8 million. These budgets and top scores do not establish unsolvability. The graphic preparation is incomplete and uncertain; its own flaws may explain failed searches. This describes the initial scouts. The subsequent source-reading pass recovered HCP1301 completely and HCP1243's main message with localized qualifications; see the new verification section below. The later review confirmed both main readings. HCP1301 is closed after the explicitly permitted corrections; HCP1243 now also has a direct graphical transcript and addressed review findings.

## Public sources

- AI Register: https://ai.hcportal.eu/register/
- HCP975 exact earlier card and comments: https://scienceblogs.de/klausis-krypto-kolumne/2016/08/17/who-can-break-these-three-encrypted-postcards/ ; Thomas's key in comment 2 and reading in comment 4, both 2016-08-17.
- HCP1000 prior partial: https://crackciphers.com/problem/134/solution/1 . This source explicitly says that this card remains partial.
- Collection context: Tobias Schrödel, Cryptographic postcards, HistoCrypt 2021, https://ecp.ep.liu.se/index.php/histocrypt/article/view/166 .

## Source verification after the user asked to finish the partials

- HCP1301: 20 main rows and four rotated under-stamp rows. A Sunday schedule, invitation, and affectionate closing read coherently with one graphic alphabet. Full Hungarian text and English translation are in its SOLUTION.md.
- HCP1243: 18 working rows cover the main message and its cramped continuation. Corrected earlier misreadings, read the love verse and the instruction about a stamp-side number. The overwritten t/r and final spelling are explicitly qualified; the separate plain cursive stamp note remains incomplete.
- The two named graphic keys are identical. Commands `python3 batches/postcards-five-2026-10-12/verification/decode.py 1301` and the same with `1243` check source hashes and reproduce the manual editions. These are not automatic OCR or independent validation: tokens were serialized from hypothesis-informed visual readings. Source comparison HTML files are in each work directory.
- HCP917: corrected a heading transcription and tested a constrained KEDVES crib with 1.2 million proposals. It did not give a consistent complete body.
- HCP1000: an additional R-minus-G image enhancement did not reliably resolve missing digits. Its known public partial is not promoted to a new complete solution.

HCP1301 review corrections and PDF closure are complete; its register entry is local only. HCP1243 is now closed after its direct graphical transcript, scoped stamp note and date discrepancy were documented. HCP917 and HCP1000 were skipped at the user’s request. No register submission or push has occurred.
