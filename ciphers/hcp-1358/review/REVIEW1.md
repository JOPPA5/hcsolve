ACCEPT

# Review 1 of hcp-1358 (pc_hcp_39), reviewer Claude Opus 5.5, 2026-10-30

The reading stands. Caesar -1 gives "My own dearest boy, this is something new and one of my favourite hymns. Love from yours, Girl." I tried to break it on the pixels and could not. Only minor issues remain.

## What I verified and how

- **Solver command.** `python3 -I ciphers/hcp-1358/work/decode.py` ran cleanly, hashes passed, and the output matches the table in SOLUTION.md.
- **Independent decode.** `review/work/independent.py` holds my own transcription, typed sign by sign from my crops, and uses its own shift code. Word divisions and all 74 letters match the solver's rows once stops are removed. Across all 26 shifts, shift 1 puts 63 letters into recognised words; the next best shift puts 2. The 11 letters outside are `oz` and `gpwpvsjuf`, the two disclosed slips.
- **Letter count.** 74 enciphered letters confirmed: 15 + 18 + 10 + 14 + 13 + 4 by line.
- **Transcription against the scan.** I rotated the un-converted original `work/hires/pc_hcp_39_adr.JPG` 90 degrees counter-clockwise and cropped every row at 3x (`review/work/r1a` to `r6b`), then the contested signs at 4-7x (`z_*`, `y_*`). All 6 rows were read, not a sample. There are no "Completion" or "Response to review" sections; this is the first round.
- **Slips, on the pixels.**
  - `oz`: the first sign is a closed hollow loop, the same form as the o of `Pxo` (`z_oz.png`). It is not an n. The literal NY is correct and is disclosed.
  - `gpwpvsjuf`, second sign: bowl with a stem both above and below the line (`z_gpw.png`), the same build as the p of `Cpz` and `pof`. The b of `boe` (`y_boe.png`) and of `Efbsftu` (`y_efb.png`) has an ascender only. So it is p, and the literal FOVOURITE is correct and disclosed.
- **u/h.** The first sign of `uijt` (`z_uijt.png`) is a tall stroke with an arch. It matches his word-initial u on hcp-1386 (`compare_u_w.png`, `thanks.png`). The dots over the i and j of `uijt` are clearly visible and confirm the word.
- **Other flagged signs, all confirmed.**
  - `Tpnfuijoh`: line 1 descenders cross it, but all nine signs and the two dots can be separated.
  - `Iznot`: third sign is arch, stroke and short leg (`z_iznot.png`).
  - `Zpvst`: s and t are joined, with a detached hooked bar and a stop (`z_zpvst.png`).
  - `Hjsm`: H with crossbar, undotted long j, s, m (`z_hjsm.png`).
  - `Efbsftu`: the x-like crossing is the f passing through the line, the same f form as in `ofx`, `Mpwf` and `pof`.
- **Whole card.** The picture side (`pic_small.png`) has no handwriting. Its printed verse is "We love the place, O God", credited to W. Bullock and Sir H. W. Baker. The rest of the address side is plain: Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. No ciphertext is left out.
- **Language and context.** This is natural period English, a sweetheart postcard, and the content suits the printed hymn card. The opening `Nz. Pxo. Efbsftu Cpz.` also occurs on hcp-1357 (same couple, same Tuck series 5534, postmark 22 March 1907), though that card has not been reviewed yet.
- **Sources.** The portal has no attached solution. SOLUTION.md says no separate web search was run, which is an honest statement of the limit. I found no sign of an unattributed source.

## Findings

1. **minor. The "Why it is correct" section slightly overstates the independence of the letters.** It says one shift gives English for all 74 letters apart from two slips. But the final sign of `Tpnfuijoh` and the first sign of `uijt` have the same form, so the h/u choice on them comes from the word (`r2a`, `r2b`). The third sign of `Iznot` also fits n only on the word. Uncertainties 3 and 5 disclose this, so the reading is unaffected. Say that at least these three signs are settled by context.
2. **minor. Date.** The stroke before the 8 joins it as a lead-in (`z_date2.png`), with no separate 1. So the hand alone reads 8th, and 18th rests on the postmark and the portal. On the postmark I see MR, a clear 1 and a broken second digit that merges with the stamp design (`z_pm.png`, `y_pm.png`). I cannot confirm 18 there, and the postmark year falls off as a bare arc. The strokes after the date are not a secure 1907 (`y_year.png`); hcp-1357 writes the year as "07", so "19[07]" in `transcription.json` assumes four digits nobody has read. Uncertainty 8 is honest about most of this. Change the wording to "year not read; 1907 from portal", and keep the "(dated March, 1907)" line labelled as portal-derived.
3. **minor. Slip in a citation.** Uncertainty 2 says "`Cpz`-line `boe`", but `boe` is on row 3, not the `Cpz` row. The claim itself holds.
4. **minor, optional. Context not used.** hcp-1357, four days later on the same Tuck series, says "this will make the pair for album". That fits "something new" here. The report could mention this, marked as context only, since hcp-1357 has not been reviewed yet.

## Could not verify

- The day (8th or 18th) and the year from the card itself. The portal's 1907-03-18 is neither confirmed nor refuted by the postmark I can see.
- The portal's reason for that date.
- Whether a printed or web solution exists elsewhere. I ran no web search, and the orchestrator's register check covers only the AI register.
- The hymn attribution beyond the printed credit on the card.
