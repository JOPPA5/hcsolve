ACCEPT

# Review 1 — hcp-1386 (pc_hcp_67), Caesar −1 postcard, 26 Nov 1907

Reviewer: Claude Opus 5.5, 2026-10-30. Solver's files and `source/` untouched; my work is in `review/work/`.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1386/work/v2/decode.py` (repo root) runs, reports hashes OK, and prints
   `MY OWN [E. L.] BOY / THANKS-VERY / MUCH FOR LETTER / TO—DAY MY / [N. & L.] FROM YOUR / OWN [E. L.] GIRL / "VERY VIRED"`,
   62 enciphered letters + 6 literal abbreviation letters. Identical to the plaintext table in SOLUTION.md.
2. **Independent transcription and decode.** I rotated `source/address.jpg` myself (`review/work/rot.png`) and made
   4–5× line crops (`review/work/L1.png`, `L23.png`, `L4.png`, `L5.png`, `L6.png`, `L7.png`, overview `msg2x.png`).
   My own reading, decoded by my own script `review/work/my_decode.py` (`python3 -I review/work/my_decode.py`):
   ```
   Nz. Pxo. [E. L.] Cpz.  -> MY. OWN. [E. L.] BOY.
   uibolt-wfsz.           -> THANKS-VERY.
   nvdi gps. mfuufs       -> MUCH FOR. LETTER
   Up-Ebz. Nz.            -> TO-DAY. MY.
   [N. & L.] gspn. zpvs.  -> [N. & L.] FROM. YOUR.
   Pxo. [E. L.] Hjsm      -> OWN. [E. L.] GIRL
   "wfsz. wjsfe."         -> "VERY. VIRED."
   enciphered letters: 62
   ```
   This matches the solver letter for letter. Every enciphered token on the card is covered by the single −1 shift.
3. **Pixel checks of the completions (2026-10-29 additions).**
   - `Cpz` (BOY), line 1 (`L1.png`): C with loop, p with descender, z – clear.
   - `N. & L.` (`L5.png`): N with a dot, a crossed ampersand/x-like sign, then a cursive L – reading as transcribed; kept literal and disclosed.
   - Second `E. L.` (`L6.png`): same E and L forms as in line 1 – clear.
   - Final word (`L7.png`): five signs; the first is built like this writer's w (tall stroke closing into a loop, identical to the w of `wfsz` just before it), not like his u (tall stroke + arch, as in `uibolt`, `L23.png`). j is a slanted descender as in `Hjsm`; s, looped f, e are clear. I agree the literal decode is VIRED and that TIRED (`ujsfe`) is a conjecture; the solver discloses this and does not substitute it in the output. The older WISE reading is correctly rejected.
   - Ordinary rows sampled sign by sign: `uibolt-wfsz`, `nvdi gps. mfuufs`, `Up—Ebz. Nz.`, `gspn. zpvs.`, `Hjsm` – all agree with the transcription.
4. **Context.** 26 Nov 1907 was a Tuesday (checked with Python `datetime`), agreeing with the plain heading "C. H. Tuesday" and the postmark WIMBORNE NO 26 07. The phrasing ("My own … boy", "from your own … girl", "many thanks … to-day") matches accepted sister cards of the same couple (hcp-1390, 1397) and the shorthand `N. & L.` also occurs on hcp-1403. Period English, natural sweetheart-card register.
5. **Sources/credit.** Portal status Not solved, no attached solution; no published solution used. Earlier GPT work and the Claude completion are credited separately.

## Findings

1. **Final word VIRED not a word (minor, disclosed).** The pixels support w, so the literal decode is VIRED; TIRED is a plausible writer's slip but stays a conjecture. The solver handles this correctly. The report should keep VIRED as read and TIRED as probable, and must not present "very tired" as a certain reading.
2. **Abbreviations E. L. / N. & L. unexpanded (minor, disclosed).** Correct to keep literal. Note for the report: sister card hcp-1387 has a parallel slot ("My own D.g boy … your own D.g girl"), so the slot is a term of endearment, but E. L. remains unexpanded; no change needed.
3. **Farm name (minor).** SOLUTION.md says the farm name is "uncertain". On this card's address (`review/work/rot.png`, `msg2x` region of the address) the name reads plainly as "Stokelake Farm", as on hcp-1387, 1388, 1397, 1403. Could be stated as "Stokelake Farm (as on sister cards)". Outside the cipher; does not affect the reading.
4. **Weekday check not mentioned (minor).** The solution could add that 26 Nov 1907 was a Tuesday, matching the heading – a small extra confirmation.

## What I could not verify

- Whether the writer intended TIRED (a slip) or something else by `wjsfe`; no second occurrence on the card.
- The meaning of E. L. and N. & L. and whether they are shifted at all.
- The heading initial C vs G (outside the cipher).
