ACCEPT

# Review 1 – hcp-1469 (pc_hcp_150), Reg to Gertrude Forrest, 11 Nov 1907

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. The solution under review is credited
in SOLUTION.md to the OpenAI GPT solver (source capture and triage, 2026-10-26, no key) and to
Claude Opus 5.5 as solver (key, transcription, reading, 2026-10-30). This review was done
independently of that solver session, working only from the files in this directory.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1469/work/decode.py`: source hashes OK (3 files),
   and the output matches the plaintext in SOLUTION.md (B01–B13 and T1–T7) word for word. The only
   difference is the upper-case `R` the decoder uses to flag the two "dRedful" readings, which
   SOLUTION.md explains.
2. **Independent decoder.** `python3 -I review/work/indep.py work/transcription.txt` has its own key
   table and parser and gives the same 20 lines. Totals: **456 sign tokens and 120 words**. Every
   token maps to a letter, so there are no unknown signs. One sign gives one letter, apart from
   the caret (n/w), which is disclosed. Checked against `/usr/share/dict/words`, every word is
   in the dictionary except plain inflections (cleared, makes, sends, signals, journeys, has,
   dearest, goodbye) and the disclosed spelling *dredful*.
3. **Transcription against the scan.** I made my own crops at 4–10x in `review/work/`
   (`b1`–`b12.png`, `b12a.png`, `b13.png`, `b13a.png`, `t1.png`, `t2.png`, `t1r.png`, `t2m.png`,
   `t3l.png`, `t3b.png`, `up.png`, `now_T2.png`). Then I read them sign by sign:
   - The body lines B01–B06 and B09–B13 match the transcription. This includes the dot letters in
     *girlie*, *half*, *shall*, *clearing*, *either*, *glad*, *foggy*, *signals*, *think* and
     *together*, and the forms ⊢⊐ in *up* (B13, checked at 10x).
   - All seven top-margin lines match: *a good bit … decent day* (T1, which runs on to the right
     above "CARD"), *goodbye … now to wait* (T2), *i hope i have a* (T3), *letter from home
     tonight* (T4), *reg sends you dredful lots* (T5), *of love … your* (T6) and *own boy reg*
     (T7). The text order body → top margin is the only one that reads on. Like the solver, I
     found no inverted text.
   - *dredful* (B05, T5): on the crops the second sign is plainly the caret, the same as in *and*
     and *own*. It is not the 7-shape used for r. Since the same spelling occurs twice, the
     solver's explanation (the writer's habit or slip) holds.
4. **Key and context.** The key is a simple invented-sign monoalphabet: e/g/h/i as dot groups,
   n and w on one sign, no x or z. It covers the whole text. The language is natural English of
   the period ("clearing out", "dreadful glad", "fog signals", "only four days now to wait").
   The names, date and places agree with the card itself: the date 11.11.07 is written on the
   card, the postmark is London (11 … 07), and the address is Miss Gertrude Forrest, West Bank,
   Eastfield Road, Westbury-on-Trym, Bristol. The portal metadata gives the date as 1907-11-11 and
   the recipient as Gertrude Forrest. The portal marks the card "Not solved", no transcription or
   solution is attached, and the orchestrator's register check found no prior record. I found no
   sign that a published solution was used.

## Findings

1. **minor – sign count is overstated.** "Why I believe it is correct" says "about 500 signs".
   The transcription has 456 sign tokens (120 words). Please give the actual number.
2. **minor – the over-printed word is described wrongly.** Uncertainty 5 says the w of *now* (T2)
   is written "over the printed crest of The Wellington Series". The crest is about 200 px further
   left, around x≈420, and it lies under *only* in T2 (`review/work/t2m.png`). The w of *now* is
   at about x≈620, y≈60. There it is a dark, blotted caret over the grey watermark band, not over
   anything printed (`review/work/now_T2.png`). The reading *now* is not affected; only the
   description needs fixing.
3. **minor – the claim about how the key was found cannot be reproduced.** SOLUTION.md and NOTES
   rest the "found statistically" argument on a quadgram hill-climb run on a first transcription.
   That transcription and the model were deleted or kept only in scratch. This does not weaken
   the reading, which checks itself through 120 coherent English words. Still, the report should
   either keep the artefact or say plainly that the step is not reproducible.
4. **minor – the n/w ambiguity is only partly tested.** The solver says carets for n and w show
   no stable difference. I saw none either at this resolution (for example *own* in B01 has two
   identical carets). The point is disclosed and every w reading is forced by context, so no
   change is required. A short note in the report that this was checked would help.

## What I could not verify

- Only the 1024 × 674 px scan exists. A few dot groups are faint, for example the e's in
  *together* and the G/H orientation in some words. I read them at 4–10x and the transcription
  is consistent with what I saw, but at this resolution the dot orientation alone does not
  settle every case. Context does.
- I did not read every one of the 456 signs at 10x. B07–B08 and the rest of B10 I checked at 4x
  only; they are consistent with the transcription.
- I could not identify the writer "Reg" or the recipient outside the card.
