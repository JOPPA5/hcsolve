ACCEPT

# Review 1 — HCP 1498 / pc_hcp_179 (round DONE1)

Reviewer: claude-opus-5-5, 2026-10-26. Short version: **the decipherment is correct.** I read the 18 Pigpen signs myself from `source/address-large.jpg` and got exactly the solver's tokens: `LATE, TONIGHT, DARLING`. The only findings are small corrections to the record.

## What I verified and how

1. **The documented command.** `python3 -I ciphers/hcp-1498/work/decode.py` exits 0, the source hashes match, and the output is byte-identical to `work/plaintext.txt` (`diff` empty). 18 glyphs.
2. **Independent decoder.** `review/work/decode_review.py` is my own geometric Pigpen key: cells 1–9 row by row, dot = second letter, wedges = S–Z. It does not use the solver's code. `review/work/reading_review.txt` holds my sign-by-sign reading, made from the crops before I compared it with the solver's. It decodes to `LATE / TONIGHT / DARLING` (`reading_review_decoded.txt`). Converted to the same notation (`convert_solver.py` → `solver_converted.txt`), the solver's transcription is **token-identical** to mine (`diff` empty). The key is a fixed 26-letter table, so no sign can take two values, and every one of the 18 signs is covered.
3. **Transcription against the scan.** Crops are `review/work/z_line.png` (5×) and `z_w1b.png`, `z_w1c.png`, `z_w2.png`, `z_w3.png` (12–16×).
   - LATE: `[·` `⅃` `V·` `L`. The V has a clear dot at its apex (`z_w1c.png`), so it is T, not S.
   - TONIGHT: `V·` `⊓` `·ㄱ` box `]` `]·` `V·`. The G (5th sign) is undotted and the H (6th) is dotted, which matches the repeated letter pair.
   - DARLING: `⊔·` `⅃` `Γ·` `[·` box `·ㄱ` `]`.
   - Commas between the words are visible.
4. **Rest of the card.** I checked the top lines, the left margin, the vertical PS along the divider and the address panel (`z_rest_top.png`, `z_margins.png`, `z_ps.png`). Everything else is ordinary cursive. There are no further cipher signs, so the claim that the three words are *the entire* cipher passage holds.
5. **Context.** The cursive reads *"… did you see L.A.? Don't be LATE, TONIGHT, DARLING, if you can help it. I think Elsie is coming with us …"*. The cipher words fit grammatically and in tone. The card begins "Dear Ernest", is signed "Yours etc Maud", and is addressed to `Mr E. Mobsby, 9 Carden Rd, Peckham, S.E.`. It uses the same key, hand, addressee and address as HCP 1497.
6. **Prior solutions.** The files show no sign that a published solution was used.

## Findings

1. **minor — address misread.** `metadata.md` and `SOLUTION.md` give "9 Ewerdon Rd [provisional]". The card reads **9 Carden Rd** (clear in the full image; same street, written in full, on HCP 1497).
2. **minor — sender/recipient left unreconciled.** The solver records the catalogue's "sender Ernest" next to "Dear Ernest … Maud" but does not draw the obvious conclusion. Ernest is the **recipient** (Mr E. Mobsby), and the writer signs herself Maud. The report should say that the catalogue sender field appears to be wrong, without claiming more about who these people were.
3. **minor — first sign of LATE.** The `[·` touches the final `e` of the cursive *be*. The shape and dot are readable at 16×, but this sign is less clean than the rest and could be mentioned as the one slightly crowded sign. Saying that no uncertain symbol remains is otherwise fair.
4. **minor — what the command proves.** `decode.py` decodes the solver's manual transcription. As the solver says, this checks the mapping, not the pixels. That is acceptable for a hand-drawn Pigpen card. Point 3 above is the pixel check.

## What I could not verify

- The postmark date: at this resolution I cannot confirm the catalogue date 1905-01-13 from the cancel.
- Historical identities of Maud and E. (Ernest) Mobsby.
- Whether a decipherment has been published elsewhere. I relied on the solver's statement and register snapshot.
