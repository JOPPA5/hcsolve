REVISE

# Review 1 — HCP 1538 / pc_hcp_219 (Pepouš to Anna Tichá, 22 Sep 1903)

Reviewer: Claude Opus 5.5, 2026-10-29. Round 1 (marker DONE1).

## Summary

The decipherment is correct. It uses the Anna Tichá family monoalphabetic key, and the
completed Czech reading in the "Completion and handover" section is supported by the
pixels. My own crops confirm the main finding of the completion: the printed stem was
there before the writing, the writer left a gap at it, and rows M01–M05, M08 and M09
lose no letters there. The verdict is REVISE, not ACCEPT, for two reasons. First, the
reproducible record (transcript, decoder, literal output, counts, status header) still
describes the old partial state and does not match the claimed reading. Second, the
transcript leaves out one clearly visible cipher glyph in M04.

## What I verified and how

1. **Solver command.** I ran
   `/Users/tomaspavuk/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 ciphers/hcp-1538/work/decode.py`.
   It passes its own checks (30 hashes, 494 positions) and prints the **old partial**
   literal text (`dovolene ne [G03]`, `pro[C01]zeti`, `[U01][G10]tom`, G01–G10
   placeholders). Saved in `review/work/solver_cmd_out.txt`.
2. **Independent decoder.** `review/work/indep_decode.py` takes the family key from
   `ciphers/hcp-1545/work/key.json` (plus the y=J, H=CH and shallow v=F aliases) and
   applies it to the `manual_cipher` strings in `work/transcript.json`, ignoring the
   solver's key and units. All glyphs map; none is unmapped. Apart from the placeholder
   formatting, the letters are identical to the solver output
   (`review/work/indep_record.txt`). With `--corrected` it applies the corrections and
   restorations I checked on the pixels (M03 n5, C01 = r84, [O], [OS], [A]). It then
   gives the coherent Czech in `review/work/indep_corrected.txt`, which matches the
   completion's editorial text.
3. **Pixels.** I rotated `source/picture.jpg` 90° to upright (`review/work/up.png`) and
   made enlarged crops at 4–8x:
   - `stemA.png` and `stemB.png` (rows M01–M09 at the stem). Every row stops cleanly
     at the left edge of the stem and resumes at its right edge. No ink shows on or
     through the stem, and the signs on both sides are complete (`th6r1 | 84cd5g`,
     `n6 | 75t4m6`, `n5 | c5`, `q5 75m | d5p5`, `t2c4 | s5832`, `d4 | b6n5d…`,
     `c4 | d3`). Confirmed: G01–G05, G08 and G09 hide nothing.
   - **M06 / G06:** `y4m5r` ends at the edge of the stem. [O] in JINEH[O] is a
     restoration and is disclosed as one.
   - **M07 / G07:** `cb385sm` ends at the stem. On the right a rising stroke is visible
     before `4`, which fits the ascender of `d`. SPOLEČN[OS]TI is a restoration and is
     disclosed as one; the Czech is certain ("ve společnosti pana děkana").
   - **M03** (`m03.png`): the sign before the gap is a one-humped `n`, the same form as
     in `n6` (MÁ) in the row above. It differs from the two-humped `m` in `t3f385m5`
     three signs earlier. So it is **cipher n = M → "mé"**, as the completion proposes,
     and the recorded `m5` ("ne") is a transcription error.
   - **M08 / C01** (`m08.png`): `bh3r84q5d4` can be read sign by sign. The `r8` is only
     slightly heavier ink and is not cancelled. PROHLÍŽETI is visible and not forced
     from context. The `q` here is the same "9"-shaped Z as in `fqt1` (vždy) in M04
     (`m04b.png`).
   - **S01 / G10** (`g10.png`, `srows.png`, rotated 180°): `q685q4 m` is followed by a
     faint, partly covered sign at the edge of the yellow flower, then `d3n`. The m-form
     reading (N) and the [A] restoration give "záleží na tom". This is supported but
     partly contextual, and it is disclosed.
   - Sample of ordinary rows I checked sign by sign: M01 start, M04 left, M07/M08 left,
     M10, M11 and S01–S04 (`m01a.png`, `m04.png`, `m07m08left.png`, `m10m11.png`,
     `srows.png`). Apart from Finding 2, all agree with the transcript.
4. **Key coverage.** Every transcribed glyph is in the family key. Unused key entries
   are not counted as evidence. The key matches the other cards of the family (for
   example hcp-1545).
5. **Language and context.** The text is natural Czech of around 1903 (`pro vždy`,
   `prohlížeti`, `báti`, `psánko`, `tisíc upřímných pus`). The writer is Pepouš and the
   recipient Anna Tichá, a teacher in Žirovnice u Počátek, the same as on the sister
   cards. The content is plausible: a holiday spent with a dean, a Cecilian concert, and
   a quarterly account in late September (the end of a quarter). 22 Sep 1903 was a
   Tuesday, so "Thursday evening or Friday morning" fits. The address side is plain text.
6. **Sources and credit.** The family key and the published partial study by
   M. Egorov are credited in SOURCES.md and SOLUTION.md. No portal solution was
   attached. The earlier GPT work and the Claude completion are labelled as such.

## Findings

1. **major — the reproducible record does not match the claimed reading.**
   `work/transcript.json`, `work/decode.py`, `decoded-literal.txt` and
   `indexed-units.tsv` still hold the pre-completion state. The record has `m5` (NE) in
   M03, `{C01}` in M08, the U01 ambiguity, and G01–G10 as unknown spans. The single
   command in SOLUTION.md therefore does not produce the full plaintext that is claimed.
   The header of SOLUTION.md ("PARTIAL candidate… not a complete solution… ten dark
   spans…") and the Uncertainties section contradict the completion section, which says
   "complete reading". Fix: correct M03 to `n5` and replace C01 with `r84`. Settle U01
   as `m`. Mark G01–G05, G08 and G09 as empty gaps (no letters). Encode [3], [3c] and
   [6] as bracketed restorations so they stay visibly separate from read signs.
   Recompute the counts. Make the decoder emit the completed literal text. Rewrite the
   header and the Uncertainties section to match.
2. **major — a visible glyph is missing from the M04 transcript.** M04 begins
   `c4s, fqt4d…` (`review/work/m04a.png`, 8x). There are three distinct signs before the
   comma: `c`, `4`, and a raised `s` (the same form as `s` in `s5832` = CELOU). The
   transcript has only `c4,`. Read literally, `nemu-|c4s` gives NEMUSIC, the writer's
   rendering of *nemusíš*. The sister card with Pepouš's family writes *těšíš* as
   `d5c4s` (TESIC), so this is the writer's habit. The completion's editorial text
   already says "nemusíš", but the record and the literal output say `nemusi`. Add the
   unit and keep the literal NEMUSIC, with a note. This also changes the total
   positions.
3. **minor — word division at M07.** The pixels show a small gap or comma mark between
   `f5` and `cb385sm` ("ve | společnosti"). The record joins them as `vespolec…`. The
   editorial text has it right; the literal record should keep the visible separation,
   or note it.
4. **minor — wording of the restorations.** The completion table calls U01 "settled"
   because `m` = N. The glyph's form supports m, but "na tom" also relies on context.
   Say both. Likewise, say that the `d` in M07 is only partly visible (an ascender).
   Both restorations are otherwise properly disclosed.
5. **minor — `vzdit`.** `fqt4d` really has `4` (I), not `1` (Y). Keeping it literal is
   correct. The report should state that the editorial *vždyť* is normalised from it.

## What I could not verify

- Whether any letters are physically under the printed stem in M06, M07 or S01. Only
  the scan exists. The restorations [O], [OS] and [A] rest on edge traces and Czech
  grammar.
- The portal pages themselves. I relied on the solver's saved metadata. I did not
  re-check the register or the published Egorov study.
