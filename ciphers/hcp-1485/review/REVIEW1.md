ACCEPT

# hcp-1485 — Review round 1 (reviewer: Claude Opus 5.5, 2026-10-30)

## What I verified and how

1. **Solver's command.** `python3 -I ciphers/hcp-1485/work/decode.py` (from repo root):
   all three SHA-256 checks `OK`, exit code 0. The literal and the "reading" outputs
   match the plaintext in `SOLUTION.md` exactly (11 lines, the three slips shown as
   `BUT{BOT}`, `GAME{CAME}`, `YOU{YOO}`).

2. **Independent decoder.** `review/work/indep_decode.py` does not read `work/key.json`; it
   builds the key from the stated construction rule alone
   (consonants `BCDFGHJKLMNPQRSTVW`, index = side·6 + position·3 + count−1; six vowel shapes).
   `python3 -I review/work/indep_decode.py work/transcription.txt` gives the identical literal
   text. Every token in the transcription maps: 172 letters, 21 glyph types, no unmapped
   token and no residue. The key therefore covers the whole ciphertext. The rule is fully
   regular, so the key was not fitted ad hoc to the text.

3. **Transcription against the scan.** I made my own 180° copy of `source/address-large.jpg`
   (`review/work/up.png`; the question marks, commas, apostrophes and parentheses read
   correctly only in this orientation). I then checked enlarged crops (4–10×) in
   `review/work/`:
   * line 1 (`L01a/b.png`): G W E N² I E / D A R L I N G. The pale first stem has two
     low-left ticks (= G). Agrees.
   * line 2 (`l2.png`, `good.png`): …I S A G O² D G A M E F O R. Agrees.
   * line 3 (`L03a/b.png`, `bot.png`): T W O / B ☐ T / I / D O N ' T / T H I N K. The
     square in "B?T" is plainly empty at 8×, with no diagonal. The literal BOT is real.
   * line 4 (`line4.png`, `came.png`, `came2.png`): I T / B E A T S / O U R (U = square
     with `\`) / C A M E / O F. The first glyph of "CAME" has its two left ticks on the
     upper half of the stem (top and mid), unlike the low ticks of every G on the card.
     The literal C is real.
   * line 5 (`l5a/b.png`): "I N / T H E / G L O A M I N G" (A L S O. Agrees.
   * line 6 (`l6b.png`, `yoo2.png`): W H A T / D O / Y O O. The Y-square has a `/` diagonal,
     and the next two squares are empty. The literal YOO is real.
   * line 7 (`l7.png`): T H I N K / D E A R E S T ? / A R E N ' T. Agrees.
   * line 8 (`l8a.png`, `you8.png`): Y (/) O U (\) …. The second square has only faint
     background or stamp marks inside, so it is a plain O. Agrees.
   * line 9 (`game9.png`): W I T H / T H E / "G A M E"? / C A R I A D !!!. Agrees.
   * line 10 (`l10a.png`, `you10.png`): I / L O V E / Y O U / G W E N² I E / D E A R. Agrees.
   * initials (`initials.png`): circle-dot · R1b · L3b · R3t = A.M.H.L. Agrees.
   No glyph is missed, merged or added in the lines I compared. There is no
   "completion" or restoration section in this solution, and no restoration was needed:
   all glyphs are legible.

4. **Language and context.** The text is fluent Edwardian English. It fits the picture
   caption "A good game for two" (golf), and "In the Gloaming" is a real 1877 parlour
   song. "Cariad" is Welsh, which suits a card to Colwyn Bay, N. Wales. "Gwennie" fits the
   addressee "Miss G. Williams" and the plain signature "Arthur". Nothing is forced.

5. **Sister card cross-check.** `ciphers/hcp-1484/SOLUTION.md` (same addressee, same
   publisher series, 1908) independently uses the identical construction (left/right/both
   bars × top/bottom × 1–3, vowels as shapes). This corroborates the key.

6. **Honesty and sources.** The portal shows "Not solved" with no solution attached. I found
   no published solution. The credit split is stated truthfully: GPT triage on
   2026-10-26, decipherment by Claude Opus 5.5 on 2026-10-29. The three slips, the
   unexplained initials, the editorial word division and the inferred J/P/Q are all
   disclosed.

## Findings

1. **(minor) Address misread.** `SOLUTION.md` and `source/metadata.md` give the house and
   street as "Bowntree" and "Oak Road". On the scan (`review/work/address.png`, unrotated
   original) they read `"Baronhill"` and `York Road`. This agrees with the hcp-1484 solver's
   reading "Baron Hill", York Road. Correct `SOLUTION.md` and the report. `source/` stays
   untouched. The cipher is not affected.

2. **(minor) Cite the sister card as corroboration.** `NOTES.md` says hcp-1484 "should be
   tried with this key", but that card has already been deciphered with the same
   construction. Say so in `SOLUTION.md`/report as independent support for the key, and
   note there whether the slips (U without diagonal, C for G) also occur on 1484.

3. **(minor) Slip classification.** BOT, YOO and CAME are best described as "literal glyphs
   corrected in the reading". This is already how they are shown. Keep the literal forms
   visible in the report, as `decode.py` does, so the emendations stay auditable. No
   change needed beyond keeping this in the PDF.

4. **(minor) Initials A.M.H.L.** These are reported literally, which is fine. If you
   mention a conjecture (e.g. a lovers' formula such as "all my heart's love"), label it
   clearly as a guess. Otherwise leave it as unexplained.

## What I could not verify

* The postmark date (portal: "around 3.1908") from the low-resolution scan. I accept it
  only as portal metadata.
* The identities of "Arthur" and "Gwennie" (G. Williams), and the meaning of A.M.H.L.
* Tick counts are 2–4 px features at 1024 px. Each glyph I checked was unambiguous, but I
  compared lines 1–10 at line level and examined at high zoom only the slips, the Y/U
  squares, "A GOOD", the initials and the C/G glyphs. These are a sample, not every glyph
  at 10×.
