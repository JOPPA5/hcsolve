ACCEPT

# Review 1 – HCP 1433 / pc_hcp_114 (Morse postcard, 2 Aug 1907)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Round 1, on DONE1
(`2026-10-29T22:58Z claude-opus-5-5`).

## Verdict in brief

The reading SHALL I SEE YOU TOMORROW EVE LOUIE / FONDEST LOVE is correct.
I re-read every Morse group on my own enlarged crops of the scan and got
the same 39 letters. The key is standard International Morse and covers
every group. Only minor issues remain, all about how the evidence is
described in SOLUTION.md. None of them changes the reading.

## What I verified and how

1. **Solver's command.** From the repo root I ran
   `python3 -I ciphers/hcp-1433/work/decode_full.py`. The source hashes
   matched and it printed SHALL / ISEEYOU / TOMORRO / WEVE / LOUIE /
   FONDEST / LOVE, 39 letters. This matches the plaintext claimed in
   SOLUTION.md.
2. **Independent decoder.** I wrote `review/work/decode_review.py` from
   scratch, with its own Morse table and my own row transcript. Row 5's
   mark positions are recorded in comments. Its seven output rows are
   identical to the solver's (checked with `diff`). The script also
   decodes the alternative segmentations of row 5 (see findings 1–3):
   AIOUIE, LOUSE, LOFIE and LMUIE. None of them is language.
3. **Transcription against the scan.** I rotated `source/address.jpg` by
   180° into `review/work/rot.png`, which confirms the orientation. Then I
   made 4–7x crops: `r1`–`r5`, `r5a`, `r5b`, `r5c`, `hook`, `L1`, `R1`,
   `L3`, `R3`, `BA`, `BB`, `B1` and `B2` (`.png`, all in `review/work/`).
   I also wrote a pixel map, `review/work/screen.py`, that marks dark pen
   ink, red-brown print and grey background separately. I read the groups
   mark by mark:
   - Row 1: `... / .... / .- / .-.. / .-..` = SHALL. The third dot of H
     (x≈746–756, y≈241–249) is merged with a cursive descender. The dot
     spacing (710, 726, ~746, 763) needs a dot there, so H is right. A
     3x3 px speck at (770,232) is too small and too high to be a dot.
   - Row 2: `.. / ... / . / . / -.-- / --- / ..-` = ISEEYOU.
   - Row 3: `- / --- / -- / --- / .-. / .-. / ---` = TOMORRO. The
     "short" dash of the second O (x≈746–756) is 10 px long and 5 px high,
     the same as its two companions (10–11 px). Dots are about 6x7 px and
     round, so this mark is a dash.
   - Row 4: `.-- / . / ...- / .` = WEVE.
   - Row 5, my mark inventory: dot 555, dash 573–590, then the end of the
     row-4 stroke (601,435). Next come dot 605–610, dot 625–630, a
     separator at about 642, three dashes (647–660, 670–681 and 691–702),
     a separator at 712, dot 722–729, dot 741–747, dash 761–778, and a
     separator at 795 with a blob on it. Then dot 798–806, dot 824–832,
     a separator at 835, dot 851–857, a separator at 868, and cursive.
     This gives `.-.. / --- / ..- / .. / .` = LOUIE. The third dash of O
     and both dots of U sit inside the red "(Post Office Regulation.)"
     line. On the pixel map all three are dark ink, clearly separate from
     the red print.
   - Bottom passage: `..-. / --- / -. / -.. / . / ... / -` = FONDEST and
     `.-.. / --- / ...- / .` = LOVE. Both are clean.
   - No pen mark in the Morse area is left unassigned. The cursive (from
     "My A. G. Thank you for your letter of this a.m. also for the pretty
     P.C." onward, plus the closing lines) is separate.
4. **Language and context.** "Shall I see you tomorrow eve, Louie? …
   Fondest love." is natural Edwardian English. "Eve" for evening is
   normal period usage. A 1907 private card (postmark 2 Aug 1907,
   addressed to G. Groves, Banbury) hiding a request to meet and an
   endearment in Morse is a common pattern among the hcportal Morse cards.
   Two independent passages decode cleanly, so a forced fit is very
   unlikely.
5. **Sources and credit.** The portal status was Not solved, with no
   attached transcription or solution, and none was used. The earlier GPT
   work (capture, orientation, rows 1–4, bottom passage) and the Claude
   completion of row 5 are credited truthfully in SOLUTION.md and
   NOTES.md. Row 5 was flagged as uncertain in the GPT notes and has now
   been resolved, with its reasoning disclosed.

## Findings

1. **minor – the row-5 L argument is stated as more physical than it is.**
   SOLUTION.md, uncertainty 1, says the stroke ending between `.-` and
   `..` of row 5 "belongs to row 4" because it has "the same length and
   slope as the other row-4 separators". The slope matches (about 2.2),
   but the length does not. That stroke runs from about (629,374) to
   (601,435), roughly 67 px. The next row-4 separator, between E and V,
   runs from about (668,379) to (649,421), roughly 46 px. The stroke
   reaches row-5 height and stops directly in the gap.

   The same writer elsewhere lets one long separator serve two rows:
   - Row 1's L|L stroke (top at about (916,244)) runs down to about
     (886,309) and is the only separator between `---` and `..-` in row 2.
   - In the bottom passage, the F|O separator of FONDEST continues down
     as the L|O separator of LOVE.

   So the physical evidence alone allows A / I (row 5 = AIOUIE). It is
   language, not stroke geometry, that rules this out. The conclusion (L)
   stands. Fix: state in SOLUTION.md and the report that this writer
   sometimes shares separators between rows, and that L is chosen because
   AIOUIE is not language.
2. **minor – one alternative for the blob at x≈790 is not mentioned.**
   The blob (about 8x6 px at x 787–795, y 441–447) is joined to the
   separator after U and sits on its left side. It is about 12 px above
   the row-5 dot line (y≈454–463). I agree it reads best as a pen hook.
   But if it were a dot, it could belong before the stroke (`..-.` = F,
   giving LOFIE) as well as after it (S, giving LOUSE). SOLUTION.md
   discusses only LOUSE. Add LOFIE as a rejected alternative for
   completeness.
3. **minor – how LOUIE is read stays open, and should stay open.** It is
   not certain whether LOUIE addresses the recipient (the card is
   addressed to G. Groves, and the cursive opens "My A. G.") or signs the
   Morse part. SOLUTION.md already leaves this undecided. Keep it that
   way in the report, and do not state either reading as fact.
4. **minor – the Morse positions are rough.** In `final-row-observations.json`
   (the earlier GPT map) the coordinates are approximate. It lists only one
   dot before U's dash (x=744). The actual U has two dots (about x 725 and
   744), and the solver's transcript correctly gives `..-`. The JSON is
   marked provisional, but the report should rely on the current
   transcript, not this file.

## What I could not verify

- The only scan is a 1024x674 JPEG, so dots are about 6–8 px. The higher
  resolution original was not available, and the pen hook in finding 2
  cannot be resolved better than described.
- I did not search the wider literature for a published solution beyond
  what the solver recorded. The portal shows no solution.
- I did not identify the people (G. Groves of Banbury, "A. G.", Louie).
  This does not affect the decipherment.
