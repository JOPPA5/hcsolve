ACCEPT

# Review 1 — HCP1453 / pc_hcp_134 (American Morse postcard, Washington D.C., 11 June 1906)

Reviewer: Claude Opus 5.5 (claude-opus-5-5), 2026-10-29.

## What I verified and how

1. **Solver command.** `python3 ciphers/hcp-1453/work/decode.py` (also run with `-I`): source
   hashes pass, 137 letters, output identical to the claimed plaintext:
   `I GOT IN A HOLE AND HAD TO SELL THAT ORCHESTRA CARTOON / FOR A DOLLAR WENT OUT TO
   BROOKLAND YESTERDAY PM I HAVE / BEEN WEARING A SKULL CAP WONT HAVE THE NERVE TO WEAR IT AT HOME`.
2. **Independent decoder.** `review/work/indep_decode.py` with my own American (railroad) Morse
   table (spaced O `. .`, R `. ..`, C `.. .`, Y `.. ..`, Z `... .`, long-dash L, P `.....`,
   F `.-.`, J `-.-.`, Q `..-.`, X `.-..`) decodes `work/transcript.json` to the same 137 letters.
   The solver's key matches standard American Morse; every code in the transcript is a valid
   American-Morse letter; no unmapped symbols.
3. **Transcription vs. scan, sign by sign.** I made my own 5x Lanczos crops of all three columns
   (`review/work/c1a…c3c.png`) and 8x crops of the cancelled box and terminal dots
   (`review/work/cancelled8x.png`, `terminal8x.png`) from `source/picture.jpg` (1024x674).
   I read **every** box of all three columns against the transcript, not a sample:
   I / GOT / IN / A / [cancelled] / HOLE / AND / HAD / TO / SELL / THAT / ORCHESTRA / CARTOON;
   FOR / A / DOLLAR / WENT / OUT / TO / BROOKLAND / YESTERDAY / PM / I / HAVE;
   BEEN / WEARING / A / SKULL / CAP / WONT / HAVE / THE / NERVE / TO / WEAR / IT / AT / HOME.
   All rows agree with the transcript. Diagnostic distinctions are visible on the pixels: the
   spaced-dot O/R/C/Y rows (e.g. ORCHESTRA `. .` / `. ..` / `.. .`; YESTERDAY first and last
   rows `.. ..`), the long dashes of L (HOLE, SELL, DOLLAR, BROOKLAND, SKULL) clearly about twice
   the length of T dashes (GOT, IT, AT), F `.-.` in FOR, P as five dots in PM and CAP, K `-.-`
   in BROOKLAND and SKULL. International Morse would not give this text (e.g. `. .` would be EE).
4. **Restorations / completions.** The main 137 letters contain no inserted or guessed letters.
   The 2026-10-29 "Completion and handover" section adds two things, judged on the pixels:
   - *Cancelled box* (col. 1, between A and HOLE): at 8x it shows a dot or two and a dark dash run
     under dense diagonal hatching; nothing is legible. The solver reads nothing from it — correct.
   - *Terminal dots*: two rows of large dots, upper `●  ●●`, lower `● ● ●`. My crop shows the same.
     The solver's `check-terminal-scope.py` and `measure-terminal-pixels.py` run and reproduce the
     reported gap ratios (upper 2.19–2.21 ~ control R 2.06–2.28; lower ~1.12 ~ control S ~0.81).
     `. ..` / `...` = **R S** in American Morse is a sound reading of the marks.
5. **Language and context.** Natural colloquial American English of the period ("got in a hole",
   "p.m.", "skull cap"). Brookland is a real neighbourhood of Washington D.C., matching the
   handwritten "Washington, D.C., June 11 '06", the Treasury Building picture and the Washington
   postmark on the address side. Addressee Carl Schmitt, Warren, Ohio, matches metadata.
   American (landline) Morse is exactly what a US writer in 1906 would know.
6. **Honesty.** The portal showed no solution; SOURCES.md cites only a generic American-Morse
   table (Friedman, Military Cryptanalysis) and discloses a Smithsonian page not used. I found no
   sign of an undisclosed published solution.

## Findings

1. **minor — SOLUTION.md is internally inconsistent about status.** The header still says
   "solver reading, not independently reviewed. No DONE1 or FINAL ... not an accepted complete
   solution", and the middle sections end "Overall status remains partial" / "No DONE marker is
   warranted", while the final section says "complete reading, handed to review (DONE1)". The
   solver should rewrite the header to the current status and mark the earlier sections as
   history, so a reader of the report is not confused.
2. **minor — the single command does not produce the claimed full reading.** `decode.py` still
   prints "Excluded: ... terminal oversized dots (possible R S)" and decodes only 137 letters, while
   the final claimed text ends "— R. S.". Either add the terminal rows to the transcript as a
   separately labelled signature item decoded by the same key, or state plainly that R S is
   decoded by `check-terminal-scope.py`.
3. **minor — R S as "the writer's initials as a signature" is stated more firmly than the evidence.**
   The glyph reading R S is well supported, and its position (end of the message, set apart, larger)
   makes a signature the most likely function, but this is interpretation and should be labelled
   "probably initials/signature". The remark "the dots are larger only because they sit alone in
   the corner" is speculation and should be dropped or softened; enlarged dots are equally
   consistent with a deliberate signature flourish. The note that an R. Schmitt is "possible but
   not claimed" is fine; do not let the report imply an identified sender.
4. **minor — cancelled box.** "The writer struck out a false start" is a reasonable inference,
   but the report should say the cancelled marks are illegible and unread (as the earlier sections
   do), not only that they are "not part of the message".
5. **minor — word-division/editorial marks.** WONT -> "Won't", PM -> "p.m." and sentence punctuation
   are editorial; already disclosed. Keep that disclosure in the PDF.

No blocker or major findings: the reading is correct and covers every legible cipher position.

## What I could not verify

- The cancelled box's original contents (illegible under hatching at the available 1024 px
  resolution; no higher-resolution scan exists in source/).
- Whether R S are the sender's initials or who the sender was; the metadata gives Sender: Unknown.
- The specific "orchestra cartoon" and the sale; no external record checked.
- Exact postmark date digits on the address side are low-resolution; the handwritten date is
  consistent with them as far as legible.
