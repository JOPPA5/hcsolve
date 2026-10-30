REVISE

# Review 1 of HCP1310 (Claude Opus 5.5, reviewer, 2026-10-30)

The reading stands: a Hungarian letter from Feri to Jolánka Tóth in the family key. I could not refute it. One ledger sign is wrong, one sign in the open word should be settled, the claim that no sister card helps is false, and one word is wrongly normalized. All are concrete fixes and none changes the story.

## What I verified and how

- **Solver's command.** `python3 -I ciphers/hcp-1310/work/decode.py` passes all four SHA-256 checks. Its output is identical to the literal rows, stamp rows, address line and normalized text in SOLUTION.md.
- **Independent decode.** `review/work/indep_decode.py` holds my own sign-by-sign reading of the 21 main rows (332 signs) in my own notation, with the key rebuilt from the HCP1216 sign classes. It differs from the solver's ledger at exactly two signs: row 13 and row 18 (findings 1 and 2).
- **Transcription against pixels.** I read all 21 rows, the stamp block and the address line on my own 7x crops of the hires address scan (`review/work/crops.py`, `review/work/zoom.py`), plus zooms of the disputed signs (`review/work/z_*.png`, `z_sheet.png`, `z_sheet2.png`).
- **Key coverage.** All 23 sign classes are used and no sign falls outside the key. The key matches HCP1216: h is tall + short, d is short + tall, n is two strokes.
- **Stamp block.** It is upright as the solver says: ⊥ is j and the rows give *csókja / idra*. Rotating it is wrong. The block looks inverted only at thumbnail size.
- **Disclosed readings confirmed on pixels:** the 5-form k in row 7 (uncertainty 3); the t of *távolból* with the a-bar crossing it (4); the two nearly equal strokes of *kedvesed* (5); the blotted sixth sign of *szeretetel* (6); and the pink blot under the wave in row 21 (9).
- **Other sign checks.** Row 9 `szalas` has two bars after the wave; the two marks below them are the ö accent of row 10. Row 10 *de* has a short left stroke and a tall right stroke, so it is d. Rows 18–21 are as printed.
- **Language and context.** This is real period Hungarian, with this writer's usual dropped letters. The stock phrases *egyetlen reményem* and *a távolból* match HCP1216 and HCP1305. Gyöngyös, Visznek and Árokszállás are coherent neighbours. Dateline, postmarks and the plaintext address agree.
- **Sources.** The portal capture shows Not solved with nothing attached. I found no sign of an undisclosed published solution. The picture side is a printed song card with no cipher.

## Findings

1. **major: row 13, last sign but one, is e, not a; the ledger and uncertainty 7 are wrong.** The sign after the section mark has three bars (`z_r13end.png`, first panel of `z_sheet.png`: bars at three levels, the third short and low, aligned under the other two). The row reads `meolyaneberekel`, not `...ekal`. Fix ledger row 13 to `S E ~`. Remove "`-kal` for *-kel* in row 13" from uncertainty 7, because this is no misspelling. The writer's real a-for-e slips (*kadvasse*, *kedvas*, *hükadve*) stand. This is the one place where a mis-transcription was explained as a writer's habit.

2. **major: row 18, the ninth sign is n on the strength of the pixels, and the claim of no sister match is false.**
   - **The sign.** It is two strokes standing together on the baseline, the left longer (`z_r18h.png`). The h of this card (rows 2, 7, 14) has its short tick at the top right. So this is `darasztin`, not `daraszti{h|n}`, and the "false start" alternative in uncertainty 1 should go.
   - **The sister card.** NOTES.md says sister SOLUTION.md files have no match. In fact `ciphers/hcp-1305/SOLUTION.md` row 5 reads `mulatharasztin`, normalized there as *mulat parasztin[?]*. It has the same eight letters after the first sign, the same -n ending, and the same *mulat-* context (*Hogy mulat ...?* / *Jó mulatást kívánok ...*). The solver's search evidently tried only `darasz`.
   - **The difference.** The first sign differs. HCP1310 has d (short + tall, `z_r18start.png`); HCP1305 has h/p (tall + short, its `work/crops/x5.png`). The two signs are the same strokes in opposite order, so a slip by the writer in one of them is plausible.
   - **Fix.** Record the cross-reference. Give the word as a likely place or jocular locative, for example *Darasztin* / *Harasztin* ("at Haraszt[i]"), marked as a hypothesis. Translate it as such rather than leaving it blank. Do not change the d in the ledger; this is a normalization question. I could not confirm the place name.

3. **minor: row 9, *meg rá is* should be *még rá is*.** A clear acute stands over the e (`z_r9acute.png`, third panel of the sheet), and *még rá is* ("even fired on it") is the idiom. The English and Slovak translations already say "even", so only the normalized text and uncertainty 8 are wrong. Fix `work/normalized.txt`, SOLUTION.md, and the listed `megrais → meg rá is`.

4. **minor: two undisclosed or understated pixel calls.**
   - Stamp row 5, first sign: only a single thick stroke is visible (`z_s5.png`), not a short h-like two-stroke form. The h of *hű* rests entirely on word sense and should be listed as such.
   - Row 11, the t of *volt*: the gamma has a doubled stroke under its top bar, so it leans towards F (`z_r11T.png`). It is t on word sense and is not disclosed.

5. **minor: the pencil note can be taken further.** At zoom (`z_pencil.png`) it starts *sziv...*, then a capital J-like form, and ends in *...ák hoz*. *Szívem Jolánkához* ("to my heart's Jolánka") is a plausible reading. It remains a hypothesis and nothing depends on it.

6. **minor: uncertainty 1 ("All signs are legible, but I find no secure word") and NOTES.md need updating after finding 2.** "Whole message read, one word unresolved" stays fair only if it says the word now has a sister parallel.

## What I could not verify

- The word *Darasztin* / *Harasztin* as an actual place or nickname, and whether d or h is the intended first letter.
- The events reported on the card, and whether Visznek lies strictly "between" Gyöngyös and Jászárokszállás. I had no map source; "near" is safe, and "between" should be softened.
- The corner mark at bottom right. It is compact and blotted, and "7/27" is no more than a guess; the solver marks it uncertain, which is enough.
- The middle of the pencil note.
