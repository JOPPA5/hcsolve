REVISE

# Review 1 — HCP 1531 (pc_hcp_212), Anna Tichá / Pepouš card, 11 Nov 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29. Round 1, against DONE1.

## Summary

The reading is correct in substance. The card uses the known Anna Tichá / Pepouš
family key, and it gives a coherent Czech letter from 1903: an apology for the late
reply, a migraine, then flu ("malá chřipka") on Sunday and Monday, work piling up,
a letter already being written, and greetings and kisses from Pepouš. The key matches
`ciphers/hcp-1545/work/key.json` exactly. It also covers every assigned unit.

Concrete fixes are still needed:

- The deliverables contradict each other. The header still says PARTIAL, and the
  transcription and the single command still print `□` twice. Only the completion
  section claims the reading is complete.
- One completion decision (R05) is wrong at the pixel level. The fix makes the text
  better.
- Several sign labels in the transcription do not match the pixels.

## What I verified and how

1. **Solver command.** I ran `python3 ciphers/hcp-1531/work/decode.py` (exit 0). It
   passed its hash, round-trip and inventory checks, with 383 positions: 381
   assigned and 2 unresolved. The output is identical to the `plaintext` fields of
   `work/transcription.json`, and to the "Literal Czech base text" block. It still
   contains `V□EREJSKA` and `PSAN□`. So it does **not** produce the plaintext claimed
   in the "Completion and handover" section.
2. **Independent decode.** `review/work/indep_decode.py` holds its own copy of the key
   table and decodes the `cipher` strings of `work/transcription.json`. All 17 rows
   match the solver's plaintext (383 units). The key is identical to the family key
   in hcp-1545.
3. **Pixels.** I made 3x crops of all 17 rows (`review/work/R01.png`…`R17.png`) with
   `review/work/rows.py`, from the solver's boxes plus a margin. I made 6–10x zooms
   of every disputed word, plus side-by-side comparison panels
   (`review/work/panel-R05.png`, `panel-R16.png`, `panel-R16b.png`, `panel-R10q.png`)
   with `review/work/panel.py`. The panels use the original pixels, autocontrast
   only. There is also a local background-normalised view of the shadowed R12
   opening (`review/work/R12-open-localnorm.png`).
   I read these rows sign by sign:
   - R01, R02, R03, R05, R07, R09, R10, R13, R14, R15, R16 and R17 in full.
   - R04, R06, R08, R11 and R12 at the 3x row level.
   Apart from the findings below, every sign I checked matches the transcription.
4. **Language and context.** The text is natural Czech of the period: *musil*,
   *poněvadž*, *ulehnouti*, *srdéčko*, *nesčíslněkráte*, *vřelou pusu*. The ordinary
   date 11./XI.1903 matches the illness narrative ("v sobotu… do včerejška… v neděli
   a v pondělí"). The address is Anna Tichá, teacher in Žirovnice near Počátky, which
   is the same recipient as the rest of the family. The sender PEPOUS(E) also matches
   the family.
5. **Disclosure.** The published partial family key by Maxim Egorov is credited. The
   key transfer is presented as known-key application. No published plaintext for
   this card is claimed or used. Earlier GPT and later Claude work is distinguished.

## Findings

1. **[major] R05 position 2 is the writer's C sign, not 1/Y. The "writer's slip" claim
   is wrong.**
   Evidence is in `review/work/panel-R05.png`, and also `R05-vYe.png`, `R05-byla.png`,
   `R08-velice.png` and `R10-praci.png`:
   - The disputed sign is a peaked "Λ" with a left leg and no foot stroke.
   - It is the same form as the writer's `s` (C) in VELICE (R08, `f584s5`) and in
     PRACI (R10, `bh6s4`).
   - The writer's `1` (Y) in BYLA (R05) and DRAHY (R01) is a different form: an
     upright stem with a flag and a flat foot.
   The completion compared the sign only with the "C" in NEOCISLNE. That sign is
   actually a `c` form (see finding 4), which explains the mistake.
   Fix:
   - Transcribe `fs5h57cg6` → VCEREJSKA (*do včerejška*), a direct reading with no
     slip.
   - Update `transcription.json` and the literal text.
   - Remove the "writer's slip" statement from SOLUTION and the report.

2. **[major] The deliverables are internally inconsistent.**
   - The header still says "PARTIAL… two remain □".
   - `work/transcription.json`, `work/decode.py` output and the literal base text
     still show both unknowns as `□`.
   - The "Completion and handover" section claims a complete reading: VYEREJSKA and
     PSANI.
   - The editorial Czech and Slovak are given twice, in two versions.
   The README requires one command that produces the full plaintext. At present it
   produces the partial one. Fix:
   - Update the transcription: R05-2 → `s` per finding 1, and R12-5 → `4`, marked as
     a contextual restoration.
   - Make the command print the final literal text, with the restoration marked, for
     example `PSAN[I]`.
   - Replace the stale header and duplicate text blocks with one current version.

3. **[minor] The R12 PSAN□ restoration is described inaccurately. It is a restoration,
   not a reading.**
   Evidence is in `R12-open.png`, `R12-open-contrast.png`, `R12-open-localnorm.png`
   and `R11-13-left.png`. After `m`, inside the photo's shadow:
   - There is a closed bowl with a **long** descender reaching into R13's line. It is
     not a "short descending stroke".
   - A further faint oval follows before `75`.
   - Under the shadow the form looks more like the bowl-plus-descender `q`/`g` than
     the writer's y-shaped `4`. Compare `4` in `74q` on the same row and in PRACI.
   - It cannot be excluded that two signs stand there.
   PSANÍ is the natural contextual reading: a neuter noun is needed for "je již
   rozepsáno", and a letter fits. Fix: label it explicitly as a restoration from
   context, not as a visual identification consistent with `4`. Note the possible
   extra sign in the uncertainty list.

4. **[minor] R16 NEOCISLNE: the shapes at positions 3–4 are labelled wrongly.**
   Evidence is in `review/work/panel-R16.png`, `panel-R16b.png` and
   `R16-signs3-6.png`.
   - The 4th sign of the word is an open-right `c` with a closed top. It is the same
     form as the `c` (S) in TISIC (R14) and the 6th sign of the same word. It is not
     the writer's `s` (C), which is the "Λ" or "ↄ" form.
   - The 3rd sign is 3-like, but it could also be the writer's hooked "ↄ" `s`.
   - So the literal is `m5[3|s]c4c8m5`, which reads NEOSISLNE or NECSISLNE. It is
     not `m53s4c8m5`.
   - The sister card hcp-1532, by the same writer with the same phrase, has
     `m5cs4c8m5` = NESCISLNEKRATE.
   The intended word is clearly *nesčíslněkráte*, so the translation stands. Fix:
   - Correct the shape labels, or mark positions 3–4 as uncertain.
   - Cite hcp-1532.
   - Drop the editorial form "neočíslně", which is not a Czech word; the editorial
     text should read *nesčíslněkráte*.

5. **[minor] R13 ODESLU, 3rd sign (`5`/E) is in shadow and looks 6-like.**
   Evidence: `review/work/R13-open.png`. The sign has a rising left stroke and a
   bottom loop, like the writer's `6`. E (*odešlu*) is the only sensible reading. Fix:
   list it among the shadow-affected signs as a context-supported reading. The
   solver notes the shadow but does not single out this sign.

6. **[no change needed, confirmed] ZAHRNIT.** In R10 the prefinal sign of the first
   word is the same form as the final `4` of PRACI on the same row, and it differs
   from the `2` of KTEROU. The literal ZAHRNIT (for *zahrnut*) is correctly retained
   and disclosed. The first sign of the word matches the closed-bowl `q` of R11 `q6`
   better than the looped `g`, so it supports Z (`panel-R10q.png`).

## What I could not verify

- I could not resolve the shadowed R12 sign or signs after PSAN beyond doubt. No
  enhancement shows clear strokes.
- I read R04, R06, R08, R11 and R12 at row level, not sign by sign at 6x+.
- I did not re-inspect the portal or check worldwide publications. I rely on the
  orchestrator's register check (2026-10-29) and the solver's SOURCES.md.
- I did not fully check the Slovak translation for idiom.
