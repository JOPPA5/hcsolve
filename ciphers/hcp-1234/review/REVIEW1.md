ACCEPT

# Review 1 of HCP1234 (Claude Opus 5.5, 2026-11-02)

The reading stands. I tried to refute it and could not: every row and the stamp box read the same on my own crops, the family key covers the whole text, and the verse rhymes on its own. Five minor disclosure points remain. None changes a word of the plaintext.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1234/work/decode.py` prints OK for all four hashes, 449 signs, and literal rows identical to the block in SOLUTION.md. The normalized text is the same as `work/normalized.txt` and SOLUTION.md.
2. **Independent reading and decoder.** I re-read all 20 rows and the 6 stamp rows on my own 3x to 6x contrast-boosted crops of the hires address scan (`review/work/crop.py`, `crop2.py`, `crop3.py`, `review/work/crops/`) and wrote them down by sign class in `review/work/my_reading.txt`. `review/work/my_decode.py` decodes them with the classes in `ciphers/hcp-1216/work/graphic-key.json` (read-only) and compares them with the solver's ledger. All 26 rows agree. The one reported DIFF, row 6, is my script's artefact: I coded ő as a marked o and the comparison flattens it differently; the signs are the same. This reading was not blind, because I had seen the solver's text first.
3. **Key consistency and coverage.** All 449 tokens map to a family class; no new sign value appears. Three of the 449 are Latin letters (A, N, L), disclosed as such. The h/p sign and the d sign stay distinct on this card (tick right against tick left). The 20 cross signs split as 17 z and 3 u (tudatom, ugy, csupan), and every one yields the only available word. I kept them unsplit in my reading, which confirms the solver's item 7: those calls come from sense.
4. **Overwritten signs, at 6x (`b5`, `b6`, `b8`, `b12`).**
   - Row 5, s of sikerült: a heavy right bowl with an inner stroke and a slash, as disclosed. Shape alone would not give s; *nem sikerült hazamenni* does.
   - Row 6, ő: loop with a heavy double mark. Fits.
   - Row 7, p of párat: long stroke, left hairline, short right tick. It is the h/p sign; p from sense.
   - Row 8, h of lehetek: long stroke with right tick under a blot at upper left. Disclosed.
   - Row 12, s of szégyen: a heavy overwritten sign beside a separate cross, which I read as s + z. *Szégyen* is the only sense, as disclosed.
   - Row 19, final ss: brown bowl, then a purple overwritten bowl. Disclosed.
5. **Language and context.** The text is natural early-20th-century Hungarian: an opening note, then a rhymed love verse (*erény / szerény*, *szeress / lehess*), the triad *hit, remény, szeretet*, and the closing formula known from the family. Name and addressee fit HCP1216. The Hungarian, English and Slovak agree in sense. The spelling repairs in item 10 are real writer's habits and are all bracketed or listed. The count claims hold: *hogy* ×5, *boldog* ×2, *szeretet* ×2, *imádója Feri* ×2.
6. **Unenciphered parts.** The address reads as claimed. The printed verse reads as claimed, including *fejthetné*, except for finding 1. Postmark: see finding 5.
7. **Sources.** SOURCES.md and metadata show no attached solution. Nothing in the directory suggests a published solution was used; this rests on those files and the orchestrator's register check, as I searched nothing further.

## Findings

1. **minor: printed verse line 1 silently corrected.** On `crops/verse.png` the print appears to read *tikom*, while line 2 clearly has *titkon*. SOLUTION.md gives *titkom* with no note. Say that the print shows *tikom* (apparent misprint), normalized to *titkom*.
2. **minor: a mark on the card is not disclosed.** Row 19 has a long single dash between *te* and *boldog* (`crops/dash.png`). It is much longer than any bar of a/e, stands alone and is not in the ledger. It is not a letter of the sentence, but item 11 mentions only commas and full stops. Record it as a dash with no letter value.
3. **minor: stamp row 3, third-to-last signs rest partly on sense.** In *össze* (`crops/st3b.png`) the second of the two bowls has a straight rising left stroke and looks close to the chevron v of S4 (*sziv-*); the z and e after it nearly touch. *Össze* is certain from *kösse össze*, and the ledger is right, but the uncertainties do not list this call.
4. **minor: ledger flags without a matching uncertainty.** The ledger header says a `!` sign is "read per SOLUTION.md uncertainties", but `o!` (row 14, csokot) and `d!` (row 14, adsz) are not listed there. Both are merely heavy and legible on my crops, so either add one line or drop the flags.
5. **minor: date.** SOLUTION.md is right to say the year was not read with confidence. On the rotated crop (`crops/pmdate.png`) DEC 16 is clear, and the digit just before DEC looks like a 1 with the same foot as the 1 of 16, which would suit a year ending in 1 rather than the 1913 of the portal file name. I could not read the other digits, so this is not proof. The report should give 1913 as the portal's date only, not as read from the card, and mention the doubt.

## What I could not verify

- The year on the postmark, and the place of the second postmark (GY... legible; the solver's GYÖ is plausible).
- Whether the verse comes from a known source; not searched.
- Identity of this Feri with the Feri of other family cards.
- Blind independence: both the solver's reading and mine started from the family key, and I saw the solver's text first. The u/z calls, the h/p calls and the overwritten signs are decided by word sense in both readings.
- Acute ticks were spot-checked only; they do not affect the reading.
