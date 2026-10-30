REVISE

# Review 1: HCP1570 / pc_hcp_251 (Pepouš to Anna Tichá, 27 Dec 1902)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Independent review. I changed none of the solver's files and nothing in source/. My scripts and crops are in `review/work/`.

## Summary

The cipher is the Anna Tichá / Pepouš family key, a simple substitution with a CH sign, and it decodes the card into coherent Czech of 1902. The overall reading stands. In the passage that the "Completion and handover" section relies on (R08 to R11), I re-read the signs at 5 to 10x and found **four transcription errors**. Three of them were explained away as the writer's "spelling anomalies" or "editorial" repairs, but the pixels show something else. The k-shaped sign also occurs a second time on this card, which contradicts the completion's claim that it is unique here. These are concrete fixes and do not change the solution as a whole, so the verdict is REVISE.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1570/work/decode.py` exits 0. It prints the 15-row literal text exactly as it appears in SOLUTION.md and reports 523 slots = 522 mapped + 1 `{U1}`.
2. **Independent decode.** `review/work/mydecode.py` is my own table, written from the SOLUTION key, plus `G` for the k-shaped sign. Applied to `work/transcription.txt`, it reproduces the solver's plaintext letter for letter, with U1 as g. All 523 slots are covered and no sign class is left unused. The key matches `ciphers/hcp-1545/work/key.json` (the `7` glyph is labelled `y` here, so J is the same).
3. **Transcription against the scan.** I rotated the picture side 90° counter-clockwise (674×1024) with `review/work/crop.py`. I read all 15 rows at 2x (`row1.png`–`row15.png`) and compared them with `work/transcription.txt` one word at a time. Every disputed sign got a 5–10x crop or a same-card comparison panel (`panel.py`):
   - `k-vs-g.png`: the R08 sign in SVA?ROVA, the R11 U1, the looped g in ACKOLIV, and TISICERY.
   - `U1-10x.png` and `follower-vs-1-4.png`: the sign after U1 against clear `1` (TISICERY, NYBRZ) and `4` (HOSTINCI, ACKOLIV).
   - `R09-TRI-10x.png` and `R09.png`: the word the solver reads as TVE.
   - `JSME-vs-JSEM.png`: R10 against R09.
   - `STRAVILI-10x.png`, `stravili-mid.png`, `R04-DLOUHYM-8x.png`, `R02-right.png` (METLOU), `R12-mid.png`.
4. **Corrected decode.** `review/work/reviewer-transcription.txt` applies my four corrections (findings 1–4). `reviewer-plaintext.txt` is its decode with the same table. Lines 8–11 then read:
   `svagrova je churava a, ackoliv / jsem mel jeste tri pozvani, nesel jsem nikam, / nybrz stravili jsme vecer ten jeste s dvema / kolegy v hostinci ...`
   This is fully regular Czech. The "anomalies" SVAKROVA and STRAVILI disappear, and so does the "writer's spelling kolegi".
5. **Context.** The metadata (Czech, 27 Dec 1902, recipient Anna Tichá, Pelhřimov) agrees with the ordinary *Veselé vánoce!* and the date 27/XII 1902 on the card. The text is about Christmas Eve, which fits. The names Anička and Pepouš and the closing fit the family. The published generic key (Maxim Egorov) and the earlier GPT solver work are credited. No published solution of this card was used.

## Findings

1. **[major] R08 SVAKROVA is a mis-transcription: the sign is the k-shaped G, so the word is SVAGROVA (švagrová).**
   Evidence: `review/work/k-vs-g.png` and `R08-left.png`. The 4th sign of `cf6?h3f6` has an ascender with a loop and a kicked leg. It is identical in form to U1 in R11. It is clearly different from the looped-descender `g` (K) on the same row in ACKOLIV (`6sg384f`) and in DIK and ANICKO.
   The solver transcribed it as `g`, then presented "K→G in SVAKROVA" as a spelling repair. The completion section says "None of the family cards has a G sign" and "the sign occurs only here". Both statements are wrong. The sign occurs twice on this card, and hcp-1541 (SVAGRA), hcp-1553 (TELEGRAMY) and hcp-1554 (TELEGRAM) use the same k-shaped G.
   Fix: transcribe a distinct class (e.g. `G`) at R08 and R11, add G to the local key as a family extension with these cross-references, remove the K→G editorial note, and correct the class counts (g/K drops by one).

2. **[major] R09 "df5" = TVE is wrong; the source has `d h 4` = TŘI ("tři pozvání", three invitations).**
   Evidence: `R09-TRI-10x.png` and `R09.png`. The second sign is a short h/R with a hump and no descender. It is not the tall looped f/V with a long descender seen in POZVANI on the same row, or in R14 `df5r3` = TVEHO, which really is TVE. The third sign is the crossbar `4` (I), not `5` (E).
   The SOLUTION states that TVE was confirmed by "root" on control panels, but the pixels do not support that.
   Consequence for the meaning: "although I still had three invitations, I went nowhere". This sentence must be corrected in the editorial Czech, the translation and the report.

3. **[major] R10 "yc5n" (JSEM) is wrong; the source has `y c n 5` = JSME, so "strávili jsme" is regular Czech.**
   Evidence: `JSME-vs-JSEM.png`. R10 shows 7-c-n-5. R09's JSEM shows 7-c-5-n. The final I of STRAVILI (`cdh6f484`, confirmed in `STRAVILI-10x.png`) is therefore the correct plural ending, "nýbrž strávili jsme večer ten…" ("we spent the evening…"). It is not a stray letter.
   Fix: correct the transcription, remove the editorial deletion of I, and drop STRAVILI from the anomaly list.

4. **[major] R11 U1 is assigned without the follow-up check: the sign after U1 is most likely `1` (Y), not `4` (I), giving KOLEGY.**
   Evidence: `follower-vs-1-4.png` and `U1-10x.png`. The follower is a slanted stroke with a lead-in and a closed foot. This matches `1` in TISICERY and NYBRZ. It lacks the open left arm and flat crossbar of this hand's `4` (HOSTINCI, ACKOLIV, STRAVILI).
   I rate this reading probable rather than certain, because the bottom of the sign is faint over the printed background. The solver's completion presents KOLEGI as "the writer's own spelling". That claim rests on a 4/I reading the solver never checked.
   Fix: re-read the sign with same-card controls. If it is 1/Y, the literal text is KOLEGY. Either way, disclose the remaining uncertainty.

5. **[minor] The G assignment for U1 is correct in substance but rests on the wrong argument.**
   The completion argues from word fit ("the only Czech word that fits") and claims the sign is unique. The stronger evidence is visual: the same sign occurs in SVAGROVA on this card, and the same k-shaped G is attested on hcp-1541, 1553 and 1554. Moreover, `decode.py` and the literal text still print `{U1}`, so the single reproduction command does not produce the claimed complete plaintext. After finding 1 is fixed, G should be a key entry used by the command.

6. **[minor] Undisclosed overwritten signs.**
   R04 DLOUHYM (`R04-DLOUHYM-8x.png`): the sign read as `1` (Y) is overwritten, with a 1/4-like form over another stroke. R10 STRAVILI: the `8` (L) is noticeably darker, apparently retraced. Neither changes the reading, but they are writer corrections and should be noted as such. The rest of the SOLUTION repeatedly claims that "no correction" was found.

7. **[minor] Stale and contradictory status text.**
   SOLUTION.md opens with "partial solver candidate … not … review", then has a completion section that declares the reading complete. NOTES.md is written as concatenated words without spaces and is hard to audit. The report should describe one current state.

## Checked and found sound

- METLOU (R02 `n5d832`, `R02-right.png`): n/M, 5/E, barred d/T, 8/L, 3/O, 2/U all match the controls. Broom is the correct reading.
- VZPOMELA (R12 `fqb3n586`): the n/M is followed directly by 5/E, so an N really is missing in the source. The editorial *vzpomněla* is acceptable and disclosed.
- The six CH units. TEN (R10 `d5m`), DVEMA (R10 `tf5n6`), TVEHO (R14) and the rest of rows 1–7 and 12–15 agree with the scan.
- The ordinary *Veselé vánoce!* and 27/XII 1902 are correctly excluded from the cipher.

## What I could not verify

- Whether the sign after U1 is certainly 1/Y. It is probable but not certain, given the faint ink over the printed background.
- I did not re-segment and re-count every one of the 523 slots. I compared all rows word by word at 2x and zoomed only where a reading looked doubtful. There may be further single-sign slips in rows that decode to plausible Czech.
- I did not check the fine q/Z versus g/K distinction at every occurrence. I checked VZPOMELA, VZPOMINA, TEZ and KAZIS for contextual consistency only.
- The portal pages themselves; I relied on `source/metadata.md`.
