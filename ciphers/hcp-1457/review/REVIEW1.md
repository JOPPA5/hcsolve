ACCEPT

# Review 1 – HCP 1457 (pc_hcp_138), Falmouth postcard to Miss E. E. Edwards, 6 Mar 1903

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-30. Solution under review: SOLUTION.md as handed over with DONE1.

## Verdict in one paragraph

The reading is correct. The address-side strokes are standard International Morse (tall = dash, short = dot). I re-read every line of the scan from my own crops and found the stroke groups the solver transcribed. My own decoder gives the same 93 letters: *AM SORRY YOU HAD SUCH A FIT OF THE GRUMBLES. HOPE BETTER NOW. MY COLD RATHER BAD TODAY. NASTY COUGH. HEAPS OF LOVE ILLIE.* The picture-side margin is a pig-Latin variant (onset + "a"). Encoding the claimed English forward reproduces every word I read on the pixels, all 13 of them. Only two letters (C of COLD, Y of MY) and one margin letter ("you") depend on context, and the solver discloses all three. No blockers or majors were found. The minor points below are for the report and register entry.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1457/work/decode.py` (from the repo root): both SHA-256 checks pass (`OK`). The output matches the plaintext claimed in SOLUTION.md word for word.
2. **Independent Morse decode.** `review/work/indep.py` builds its own Morse table from the code list in alphabet order, without reusing decode.py. It decodes `work/transcription-morse.txt`: same 9 lines, `letter groups: 93`. Every group is a valid Morse code, so nothing is left over.
3. **Transcription against the scan, sign by sign.** I made my own crops at 3–8× (`review/work/crop.py`, outputs `review/work/r1–r4.png`, `l1–l9.png`, `l1b.png`, `l3b.png`, `l5c.png`, `l9w.png`) and read them with no reference to the solver's crops:
   - L1: check-mark + two tall (AM), three short (S), three tall (O), two short-tall-short shapes (R R), tall-short-tall-tall (Y), three tall (O), short-short-tall (U). ✓
   - L2: four short (H), check (A), tall+2 short (D); 3 short, ..-, -.-., 4 short (SUCH); check (A); ..-., .., tall (FIT). ✓
   - L3: three light tall (O), ..-. (F); T H E; then at 6× `lh` = --. (G), `vh` = .-. (R), ..- (U), two tall (M), tall + three short (B), .-.. (L), short (E), three short (S): GRUMBLES. ✓
   - L4: HOPE BETTER NOW, followed by the slanted dash + dot "/." mark. ✓
   - L5: two tall (M), the N-shape + tall (Y), the overwritten sign (C, see finding 1), three tall (O), .-.. (L), -.. (D), RATHER. ✓
   - L6: BAD TODAY NASTY, with λ = -. for N and tall + 3 short for B. ✓
   - L7: λλ = -.-. (C), O, U, `lh` = --. (G), four short (H), "/." mark. ✓
   - L8: HEAPS OF LOVE: the end "|||·u|·" = O, ...-, E. ✓
   - L9: I checked a wide crop (x 150–300) for any sign before the signature and found nothing. The line reads `.. .-.. .-.. .. .` + dot = ILLIE. The two short strokes at the start are clear. ✓
4. **Margin (picture side).** I cut the margin out and rotated it myself (`review/work/margin.py` → `mg0–mg2.png`, plus `ouya.png` at 8×). My literal reading: *Anyma ankstha orfa P.C. istha orningma. Aveha / Ou?a eensa attha iewva eba-orefa. Ery va ettypra.* `review/work/pigcheck.py` encodes the claimed English ("onset to end + a", syllable-wise for *be-fore*). All 15 tokens agree with my reading (the "?" counts as a wildcard).
5. **Plaintext and context.** The text is idiomatic Edwardian English postcard style: the clipped "Am sorry…", "Hope better now", "Heaps of love". The date, Falmouth postmark, March weather (cold, cough), and the comment on the Cornish view on the front are consistent. Morse used as a private postcard cipher and pig Latin are both well-attested for the period.
6. **Sources and honesty.** The portal status was "Not solved" with no attached transcription or solution (SOURCES.md, metadata.md). The solver states that the transcriptions are its own. I found no use of any published solution. The credit section truthfully separates the GPT capture/triage (no reading) from Claude's decipherment.

## Findings

1. **minor – L5 "C" of COLD is read from context, not from the pixels.** At 8× (`review/work/l5c.png`) the sign is a light inverted V (two tall legs) with a dark short V written over its middle. Taken in spatial order (left tall leg, dark short down, dark short up, right tall leg), the pixels read as `-..-` = X just as easily as `-.-.` = C. SOLUTION.md uncertainty 3 already calls this the weakest letter and says it rests on context. Because "MY ?OLD RATHER BAD TODAY. NASTY COUGH" forces COLD, the reading stands. The report should say plainly that the letter is a correction whose stroke order cannot be read, and that C is restored from context.
2. **minor – L5 "Y" of MY rests on counting a full-height diagonal as a dot.** The N-shape (`l5c.png`) is tall | full-length diagonal | tall, followed by a separate tall stroke. Elsewhere on the card a dot is a short stroke, so treating this diagonal as a dot breaks the solver's own visual rule. Read literally, the strokes give `----` or `---`+`-` (not a letter / OT). Uncertainty 2 discloses this. Keep that disclosure in the report.
3. **minor – margin "Ou[y]a".** At 8× (`review/work/ouya.png`) the middle of the word lies under the descender of the *y* of "Anyma". I cannot see a separate *y*. The visible shape could equally be taken as "Ooka/Aoka". The [y] is a context restoration, and SOLUTION.md (uncertainty 6, `[y]` in the transcription) marks it as one. Nothing to fix. I note it here only to confirm that the disclosure is accurate.
4. **minor – presentation of the script output.** The "Full plaintext" line from decode.py has no sentence break after GRUMBLES or TODAY, and it prints "before." with a full stop. SOLUTION.md explains both as editorial. The report should show the literal text (with the card's own stops only) separately from the normalised translation so the reader can tell them apart.
5. **minor – register/report typing.** The portal lists the card as "Substitution; Monoalphabetic", "Language: Unknown". The established systems are **Morse code written as strokes** (address side) and a **pig-Latin variant** (margin), and the language is English. The register `type` and the report should say this, not repeat the portal category.

## What I could not verify

- The clear-text address street ("4 Hatham(?) Road") and the identity of "Illie" / E. E. Edwards. Neither affects the decipherment.
- Whether the writer meant "Illie" or slipped for Lillie/Ellie. The strokes clearly give ILLIE, and the solver correctly does not restore anything.
- Only the 1024×674 portal scans were available. A higher-resolution scan might settle the stroke order of the overwritten C (finding 1).
