ACCEPT

# Review 1 - HC Portal 1501 (pc_hcp_182) - reviewer Claude Opus 5.5 (claude-opus-5-5), 2026-10-30

Claim under review: the address side is hand-drawn International Morse (short dash = dot, long dash = dash,
small ink dot = letter gap, large blob = word gap), 33 lines, decoding to an English love letter from "George"
to "Nell" plus a P.S. at the top. Round 1 solving work is by Claude Opus 5.5; the earlier GPT solver (GPT-6 Astra /
GPT-6.1 Sol) only captured sources and noted the Morse-like look as a hypothesis, which SOLUTION.md states correctly.

## What I verified and how

1. **Solver's command.** `python3 ciphers/hcp-1501/work/decode.py` (repo root) runs, the hash checks pass, and
   the output is identical to the plaintext in SOLUTION.md (letter L9-33 and P.S. L1-8).
2. **Independent decoder.** `review/work/my_decode.py` (own Morse table, stdlib) on `work/transcription.txt`:
   `groups=265 invalid=0`. Every one of the 265 code groups maps to a letter; nothing is left over. Output
   line by line is identical to the solver's.
3. **Independent measurements.** `review/work/profile.py` (run-length widths of dark runs, R channel < 140/150, along a
   line) and `review/work/auto.py` (crude automatic classifier: width <= 12 dot, >= 15 dash, <= 3 separator,
   height >= 5 blob; line geometry taken from the solver's lines.json, nothing else). With these fixed thresholds the classifier
   matches the manual transcription exactly on L5, L14, L24, L25, L26, L30, and almost exactly on L27. The other lines differ
   where dashes are broken by the grey HCPortal watermark, the red rule or the postmark, or where marks are at
   the 12-16 px boundary. These are the cases the solver already describes as checked by eye. I did not find a disagreement that changes a letter
   apart from the ones disclosed (see findings).
4. **Visual check against the scan** (own 4x band crops `review/work/b*.png`, 5x line crops `review/work/L*.png`,
   8-10x zooms): mark by mark for L1 (YOU CAN), L7-8 (YOU KNOW), L12 (KNOW), L16 (HOPE YO; confirmed: the line begins
   with four short marks then a separator, so no "I" before HOPE), L18 (I HAD A LETTER: the dots are 10-14 px, the dashes 22-27 px, so
   relative reading is sound), L19 (FROM E JEWIT), L28 (SWETHEART), L29 (TH BEST LOVE), L33 (EST GEORGE). In all of
   these the transcription matches what is on the card, except the disclosed boundary cases below.
5. **Key coverage.** Standard International Morse, with no secret key. All 33 lines are covered; no numerals or punctuation; no invalid groups.
6. **Language and context.** The plaintext is natural, idiomatic English of the period ("just a line to let you know",
   "alive and kicking", "so long till Sunday", "with best love and kisses, yours always"). It is coherent across the
   line breaks (Y|OU, KN|OW, S|UNDAY, MI|GHT, TI|LL, WI|TH, AL|WAYS, DEAR|EST), and that coherence could hardly come from noise. Postmarks on the scan:
   "BROUGH S.O. 8.15 PM MR 2 11 YORKS" (dispatch) and "GILBERDYKE R.S.O. 6 AM MR 3 11 YORKS" (arrival); the handwritten date
   "March 1st 1911" and the address "Miss O. Davy, Gilberdyke, E. Yorks" agree with the metadata (1911-03-02) and with SOLUTION.md.
   The "P.S." in clear at the top left agrees with lines 1-8 being the postscript.
7. **Sources and honesty.** SOURCES.md and metadata record portal status "Not solved" with no attached transcription or solution.
   I found no use of a published solution. Uncertainties are listed in SOLUTION.md.

## Findings

1. **(minor) L28 "SWETHEART": by pixels the questioned mark is a dash, so the letter is a context reading.** My profile of L28:
   `217:8 227:8 240:6 251:9` (H), separator at 266, then `276:16`, separator at 299. The other dots on the line are 6-10 px
   and the dashes 17-23 px. At 8x (`review/work/L28_mid.png`) the mark is clearly longer than the H dots and close to the
   dashes. A literal reading is `-` = T, i.e. SWETHTART. SOLUTION.md discloses this as the weakest point, so this is
   not a hidden restoration. The disclosure is only in the prose, though: `work/transcription.txt` writes a plain `.` and the edited
   text gives "swe(e)theart" without marking the second E. Fix: flag the mark in the transcription (e.g. a comment
   line) and write the edited plaintext as "Swethe[?]art" or "SWETH(E)ART" with a footnote. Do the same in the report.
2. **(minor) L19 initial "E".** The isolated mark between the two blobs measures `324:12x3` in my profile. At 8x
   (`review/work/L19_jewit.png`) it looks about 8 px long, and a grey watermark stroke crosses it, which probably inflates the
   automatic width. The dots on that line are 6-10 px and the dashes 16-24 px, so E is the better reading, but T cannot be ruled out. Disclosed
   correctly; keep it as "E. (or T.) Jewit" in the report. JEWIT itself is well supported: `.--- . .-- .. -`. In my
   profile the J's third mark appears as `392:13` plus faint tail pixels at 406-412 that join it to the next segment; visually it is
   one dash. It is not a separator.
3. **(minor) L29 separator after O of LOVE.** The mark at x≈475 is `5x3`, larger than the usual separator (`2-3 px`,
   e.g. 537:3x3 on the same line) but smaller than the dot marks (7-8 px). It sits only about 4 px after the end of O's last dash
   (`review/work/L29_love.png`). The solver's reading (separator, giving V `...-`) is the only one that gives a word and is disclosed.
   Alternatively the writer simply wrote V with an overlong separator. No change needed beyond keeping the note.
4. **(minor) Intermediate-length marks are resolved only in prose.** About 20 marks of 12-16 px are classified by comparison within
   the line (listed in SOLUTION.md, point 1). I checked L18 and L33 myself and agree with the classification. Every one of them is
   either confirmed by its word or harmless. For the report, a one-line statement that dash length varies from line to line (dots 5-14 px,
   dashes 13-27 px) and that marks were read relative to their own line would help a reader who has not seen `work/`.
5. **(minor, cosmetic) The type label.** The register type should be "Morse code" (International). The unusual sign set (short/long dashes with
   dot and blob separators) is worth one sentence in the report, because the portal page shows the dots as the obvious
   "Morse dots" and a reader might otherwise expect dot = Morse dot.

No blocker and no major finding. The reading is correct.

## What I could not verify

- I did not re-check every one of the 265 groups mark by mark at high zoom. I checked ten lines visually in full and
  compared all 33 lines with an automatic classifier. Everything outside those ten lines rests on the classifier agreement
  plus the fact that every group decodes to a valid letter inside fluent English.
- The identity of "Nell" / "Miss O. Davy", "George" and "E. Jewit" (Jewitt is a common East Riding surname, but I did not confirm it).
- The original card (only the 1024 px portal scan was available); some boundary marks (findings 1-3) may be
  clearer on the physical card.

## Files

- `review/work/my_decode.py` - independent decoder
- `review/work/profile.py`, `review/work/auto.py` - independent measurement and auto-classification
- `review/work/crop.py`, `review/work/b*.png`, `review/work/L*.png` - enlarged crops used for the visual check
