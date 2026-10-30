ACCEPT

# Review 1 — HCP 1021 (reviewer: Claude Opus 5.5, 2026-10-30)

Claim under review: standard Pigpen, German, cipher line along the top of the picture side written
with the card turned 180°; plaintext `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS` =
"Radfahren soll leben! All Heil! Gruß".

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1021/work/solve_1021.py` → SHA256 of picture.jpg,
   address.jpg and metadata.md OK; prints `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS`, the same as
   SOLUTION.md. The script's key is the textbook Pigpen (A–I plain grid, J–R dotted grid, X with
   S top/V-shape, T left, U right, V bottom). I checked the GRID order against the standard layout:
   correct.
2. **Independent transcription and decode.** I made my own crops (`review/work/crops.py`,
   `review/work/glyphs.py`): top strip x60–870, y5–60 of `source/picture.jpg`, rotated 180°,
   autocontrast, 4x; and one 6x tile per glyph using the GPT geometry boxes (`sheet0-2.png`),
   plus a 10x tile of glyph 26 (`g26.png`). I transcribed each sign from these tiles by the walls
   present and the presence of an inner dot, and decoded with my own script
   (`review/work/my_decode.py`, cell position derived from the wall set, not from the solver's
   shape names). Output: `RAD[x]FAREN SOLL LEBEN ALL HEIL GRUS` — identical.
3. **Sign-by-sign check (all 29 positions, not a sample).** On the rotated tiles:
   R(29) ⌜ with clear inner dot; A(28) ⌟; D(27) ⊐ with a dot *outside* its open lower-left side;
   26 cancelled by a heavy X; F(25) ⊏; A(24) T-shape; R(23) ⌜ with inner dot; E(22) □;
   N(21) □ with dot; S(20) V; O(19) ⊏ with inner mark; L(18,17,16) ⌞ with dot, each clear;
   E(15) □; B(14) ⊔; E(13) □; N(12) □ with clear dot; A(11) T-shape; L(10,9) ⌞ with dot;
   H(8) ⊓; E(7) □; I(6) ⌜, the blob sits on the corner junction, not inside; L(5) ⌞ with dot;
   G(4) ⌝ with an ink blot above, outside the cell; R(3) ⌜ with dot; U(2) <; S(1) V; then a long
   vertical end stroke. Every dot/no-dot decision I could see agrees with the solver.
4. **Orientation.** In the rotated view the signs stand on the printed frame line and the five
   dividers are commas descending below the line, as claimed. Read in the stored orientation the
   same key yields no words. The 180° turn is a single, natural parameter, not a fitted one.
5. **Coverage / consistency.** All 28 uncancelled signs are decoded by one key; no sign is left
   out or reassigned. Repeats are consistent: ⌞· = L ×6 (the solution text says "five times" for
   SOLL/LEBEN/ALL/HEIL, but L stands at 18, 17, 16, 10, 9, 5 = six times;
   see finding 4), □ = E ×4, □· = N ×2, ⌜· = R ×3, V = S ×2.
6. **Language and context.** "Radfahren soll leben! All Heil! Gruß" is idiomatic period German;
   "All Heil!" was the standard greeting of German cyclists' associations around 1900. Spellings
   *Radfaren* (or h hidden under the cancelled sign) and *Grus* are ordinary informal spellings.
   The margin date in the right column reads "R. 11.III.01" on my crop (`margin_date.png`),
   consistent with the 13 Mar 1901 postmark and a Roggenburg sender.
7. **Prior publications.** `grep` of the Schrödel 2021 paper text (`../hcp-1081/work/schrodel-2021.txt`)
   for Roggenburg / Weyarn / Radfahr / All Heil / Schmid: no hits. The portal page had no attached
   solution. No other cipher directory contains this plaintext. Nothing suggests an undisclosed
   published solution.
8. **Credit.** SOLUTION.md credits the earlier GPT (GPT-6 Astra / GPT-6.1 Sol) geometry work and
   the Claude Opus 5.5 decipherment truthfully, consistent with NOTES.md.

## Findings

1. **minor — T-shaped A (glyphs 11, 24) rests on context.** On my tiles both are clearly a
   vertical with a horizontal joining at roughly two-thirds height and the vertical continuing
   below — a sideways T, not a ⌟. A = ⌟ written carelessly is the only reading that gives words
   (ALL, FAREN) and glyph 28 is a normal ⌟ in the same word, so the reading is sound; the solver
   discloses this (Uncertainty 2). The report should show the two shapes side by side with
   glyph 28 so a reader can judge.
2. **minor — cancelled glyph 26 unreadable.** On a 10x tile the underlying sign cannot be
   identified (the X covers it completely). The solver correctly omits it and discloses that an
   H is only a guess. No action needed beyond keeping that wording.
3. **minor — stray dots at 27 and 4.** I agree both marks lie outside the cell (27: outside the open
   side; 4: above the top bar). Disclosed; keep it in the report.
4. **minor — count wording.** "⌞· = L five times (SOLL, LEBEN, ALL, HEIL)" undercounts: L occurs at
   glyphs 18, 17, 16, 10, 9, 5 = six times. Fix the number.
5. **minor — "All Heil" context unsourced.** The cyclists'-greeting explanation is general knowledge,
   which is labelled as such; a citation (e.g. to the Deutscher Radfahrer-Bund greeting) in the
   report would help, but is not required.
6. **minor — metadata for the report/register.** The portal lists language "Unknown"; the report
   should state German. The register `type` should be the standard Pigpen designation used for
   other standard-Pigpen cards in this repo (e.g. hcp-1476/1497/1498), for consistency.

## What I could not verify

- The identity of the cancelled sign 26.
- The cursive pencil text in the left, right and bottom margins was not transcribed by either of us
  (only the date "R. 11.III.01" was checked); it is outside the claim and may contain the actual
  message to Fräulein Schmid.
- Only the portal scan resolution (1024×678) was available; the original card could not be examined.
