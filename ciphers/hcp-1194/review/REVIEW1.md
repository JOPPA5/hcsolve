ACCEPT

# Review 1 — hcp-1194 (Claude Opus 5.5, reviewer, 2026-11-03)

## What I verified and how

1. Ran the command from SOLUTION.md: `python3 -I ciphers/hcp-1194/work/decode.py`. The three SHA-256 checks print OK and the output is exactly the claimed text (HERZ. DANK FUR BRIEF. ERWARTE FEILERN / ANGESAGTEN. / INNIGEN GRUSS U. KUSS / STIMMUNG ANHALTEND. / DEI(N) RASA).
2. Made my own transcription from the un-converted original `work/hires/..._pic.jpg` (rotated +90°, crops 2–5x in `review/work/`: seg0–seg3.png for every row, l2start.png, l4start.png, feilern.png, erwarte.png, erwarte2.png, anhaltend.png, sig.png, sig_start.png), with my own sign labels, and decoded it with an independent script `review/work/rev_decode.py` (`python3 -I ciphers/hcp-1194/review/work/rev_decode.py`). Result: the same plaintext, 82 enciphered signs, all covered by the key; no sign left unmapped.
3. Sign-by-sign checks of the disputed points on the pixels:
   - FEILERN, 5th sign (feilern.png): a stem with a single hook at the top bending right and down. It matches the L of ANHALTEND (anhaltend.png) and differs clearly from T, which is an up-arrow with barbs on both sides (ERWARTE, ANHALTEND, ANGESAGTEN, STIMMUNG). L is a pixel reading, not a guess. All seven signs F E I L E R N are clear.
   - W of ERWARTE (erwarte2.png): a very heavy stem with two up-right branches. It has the same shape as the F signs (BRIEF, FEILERN, FÜR), only darker. So W does not have a sign of its own, and the solver says correctly that W rests on word sense.
   - First sign of line 2 (l2start.png): a faint diagonal-plus-stem A, visible next to the "SuS B." publisher logo. Accepted.
   - First signs of line 4 (l4start.png): the bolt S at the edge is partly cut but recognisable, then a T up-arrow and I, M, M, U, N, G. STIMMUNG stands.
   - Signature (sig_start.png): crossbar D, cross E, stem I, then a sign written over by a caret-like Λ above a cross-like sign; then R, A, S, A. DEIN as a correction is plausible and disclosed. RASA is reported literally.
4. Key consistency: each letter has one shape across independent words (G flag in ANGESAGTEN/INNIGEN/GRUSS/STIMMUNG; D in DANK/ANHALTEND/DEIN; K in DANK/KUSS; S bolt in ANGESAGTEN/GRUSS/KUSS/STIMMUNG/RASA; U as Γ/Π in FÜR/GRUSS/U./KUSS/STIMMUNG). The key is a MASC with an invented, rune-like alphabet.
5. Address side (review/work/adr_small.png): plain Kurrent address "Wolgeboren Herrn Anton Schönfelder, Wien IV, Favoritenplatz 7, Th. 29", Tepl 17.6.(19)00 postmark, Wien arrival 19.6.00. The stamp is intact. No cipher and nothing else hidden that can be seen. On the picture side, the only writing besides the cipher is the printed "Franz. Künstler Karten No 3" and the "SuS B." logo.
6. Language: telegraphic German love-card style, plausible for 1900. HERZ, DANK FÜR BRIEF, INNIGEN GRUSS U. KUSS, STIMMUNG ANHALTEND are idiomatic.
7. Published solution: the portal has no solution attached and status Not solved. I found none in SOURCES.md either, and the solver discloses its search.

## Findings

1. (minor) SOLUTION.md says "18 signs, 18 letters, one sign per letter". In fact W is not a separate sign: it is the F shape written heavily (key.json lists f2bold, f2 and f2heavy). The key has 17 distinct shapes for 18 letters, and W/F is a homograph resolved by sense. Uncertainty 2 already says this, but the summary line should match it.
2. (minor) "FEILERN ... angesagten" is the one word/clause whose meaning is a hypothesis (the surname Feiler with the old -n accusative, "as announced"). The signs are certain. Under the run rules a single un-understood word is acceptable, and the solver discloses it. The report should keep the literal reading and present the interpretation as tentative.
3. (minor) Signature "DEIN RASA": if Rasa is a woman's name (the card is a love/friendship card to a man), the expected form is "Deine". The overwritten 4th sign might hide something other than a plain N (for example an attempted correction). This does not change the reading, but it is worth one sentence in the uncertainties. The translation's "Tvoj/Tvoja" already hedges on the gender.
4. (minor) The plaintext in the command output has U for Ü (FUR). This is disclosed (uncertainty 5); the report should show "für".

No blocker or major issues. For the register entry the type label is MASC. The steganography note in the user's request concerns the Jolánka series. On this card the stamp is intact and I found no writing under the stamp or in the picture, so "MASC + Steganography" is not warranted here.

## What I could not verify

- What lies under the stamp (not visible in the scan).
- Who "Feiler" and "Rasa" are; I found no external source.
- The sister card hcp-1195 was not compared sign by sign (out of scope; the solver also did not use it).
