ACCEPT

# Review 1 — hcp-1073 (Hugo Carl, Aschersleben, 13.7.1910)

Reviewer: Claude Opus 5.5, 2026-11-03.

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1073/work/decode.py` from the repo root: all four
   SHA-256 checks OK; the letter-by-letter output matches the claimed plaintext and the internal assert
   passes. Note that the script prints a hard-coded word-divided plaintext and resolves sign 6 by a
   hard-coded position table; the assert makes this a consistency check, not a blind print.
2. **Independent decode.** `review/work/rev_decode.py` (run with `python3 -I`) uses my own sign reading,
   made from my own rotated crops of the hi-res address side (`review/work/msg_rot.jpg`, `l1.jpg`,
   `l4.jpg`, `l5.jpg`, `l8.jpg`, `leftedge.jpg`, `line6end.jpg`, `right_end.jpg`), and derives the digit
   values from the rule "alphabet without j, c=1", not from the solver's table. Output:

       1000 grüsse u. küsse / sendet dir / dein / dissel /
       hoffentlich hist du gesund / wenn nicht dann langweile dich /
       bitte nicht so u. denk ein / hischen an deine trude

   Identical to the solver's reading except that the rule gives h for sign 6 in "bist" and "bischen",
   which the solver disclosed as the 6 = h/b homograph. Sign counts agree with SOLUTION.md
   (3 x18, dash x16, 7 x13, 2 x11).
3. **Transcription against the scan, every line.** I read all 8 lines sign by sign on the 1.5–3x
   enlarged, rotated crops. Every token in work/transcription.txt is on the card in that order; I found
   no added, dropped or forced sign. Line 6 runs to the bottom edge of the card; my crop to the card edge
   (`line6end.jpg`) shows it ends with "2 7 +," (dich), so nothing is cut off. Specific checks:
   - "Dissel": 2, 7, two hooks with very long thin lead-in strokes, 3, 9. The hooks have the same head
     as the s-hooks in "Grüsse"/"Küsse"; the long lead-ins are only a pen flourish. s is the right call.
   - "bist": 6, 7, then one rho-like loop with descender, followed by a word separator. There is no
     separate t sign. Reading the loop as "st" is disclosed (uncertainty 3).
   - "bischen": 6, 7, an s-like sign with two dots above it, +, 3, dash. Disclosed (Sd).
   - "Bitte": a tall l-shaped stroke, clearly different from the 6 used in "bist"/"bischen". Disclosed.
   - a (inverted V) in "dann", "langweile", "an" is clearly distinct from the s-hook on the scan; the
     solver's uncertainty 2 is if anything over-cautious.
   - Hoffentlich: 6, o (written like a 0), 4, 4, 3, dash, crossed-A, 9, 7, +. Correct.
   - "du", "gesund", "u." and "Trude" carry the Kurrent u-breve; ü with two dots occurs only in
     "Grüsse" and "Küsse". The transcription matches.
4. **Key consistency and coverage.** Every sign on the message side is decoded; each recurring sign
   keeps one value across all its occurrences except the disclosed 6 = h/b. The digit rule
   (d2 e3 f4 g5 h6 i7 k8 l9) is confirmed by 8 distinct digits, which is strong evidence against a forced
   reading.
5. **Language and context.** Fluent, idiomatic German of c. 1910 ("1000 Grüsse u. Küsse",
   "langweile dich bitte nicht so", "bischen" as a common period spelling). Local delivery ("Hier") in
   Aschersleben agrees with the ASCHERSLEBEN 13.7.10 cancel. "Über den Steinen" is a real street name in
   Aschersleben; on my crop (`street.jpg`) the Kurrent "Über den" is clear and the last word fits
   "Steinen" (St ligature, then minims and n), as the solver says.
6. **Picture side.** Inspected the hi-res picture side: only the printed photograph, "Ser. 115/2" and the
   publisher mark; no handwriting in the picture or along the edges. The stamp is still on; under-stamp
   writing cannot be checked, and the solver disclosed this.
7. **Sources.** Portal status Not solved, no attached solution; I found no indication of a published
   solution being used.

## Findings

1. (minor) Header comment in work/transcription.txt says the text "runs bottom-to-top on the scan". On
   the scan it runs top-to-bottom (the "1000" is at the top of the rightmost column); the stated rotation
   (90 degrees counter-clockwise) is correct. Fix the comment.
2. (minor) Slovak translation renders "Dein Dissel" as "tvoja Dissel". The German has masculine/neuter
   "Dein", not "Deine", so the gender of the writer under that name is not established (a diminutive in
   -el is grammatically neuter or masculine). Say so in a note or use a neutral rendering; the English is
   fine.
3. (minor) decode.py resolves sign 6 by a hard-coded position table and prints a hard-coded plaintext.
   This is acceptable because the assert ties it to the decoded stream, but SOLUTION.md should say plainly
   that the b readings are word-sense resolutions inside the script (it already says so in the
   uncertainties; just mention the table).
4. (minor) For the register entry: type MASC is appropriate (no steganographic part was found on the
   visible card; the stamp is unchecked). Do not label it "MASC + Steganography" unless something is
   actually found.

No blocker or major findings.

## What I could not verify

- Whether anything is written under the stamp (stamp still attached).
- The identity of "Dissel" and "Trude" and whether they are the same person.
- "Steinen" as against another street name rests partly on the street name existing in Aschersleben;
  I did not check a 1910 address book.
