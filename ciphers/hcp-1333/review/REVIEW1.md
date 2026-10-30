REVISE

# Review 1 of hcp-1333 (pc_hcp_14) — Claude Opus 5.5 as reviewer, 2026-10-30

The reading stands: I found no wrong letter and no forced passage in the 197 signs. The key as written does not stand. It merges signs that the card and sister card hcp-1332 distinguish, and the solver's uncertainty statement rests on that merge. These are concrete, small fixes (finding 1 is the only one that must change files beyond SOLUTION.md prose). No change to the plaintext is expected.

## What I verified and how

- Command: `python3 -I ciphers/hcp-1333/work/decode.py` ran clean, hashes OK, 197 signs, 14 lines. Output equals the claimed plaintext, apart from the accents and punctuation SOLUTION.md declares editorial.
- Independent script: `review/work/indep.py` holds my own glyph-class transcription (no letters), decodes it with my own map, and enumerates every letter option of each polyvalent word. Result: 14 lines, 197 signs, 0 lines differing from the solver's class sequence; class counts match.
  Limit: I typed it after reading the solver's transcription, so it is a check against the pixels, not a blind reading. The zero difference is weaker evidence than it looks.
- Pixels: from `work/hires/pc_hcp_14_adr.JPG` I made 3x crops of the card lines (`review/work/s*.png`, `line*.png`, `over.png`), 6x crops with blue-minus-red ink separation of the hidden signs (`sep.py`, `L14start*.png`, `L8start*`, `L6start*`) and 5x comparison sheets (`qg.png`, `ip.png`). Lines 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14 were checked sign by sign in whole or in the crops listed; lines 2 and 5 mostly from `over.png` and partial crops.
- Word ambiguity: of all class-to-letter options in `indep.py`, the chosen words are the only Portuguese sense I can find in running text. "lauda" for "laura" is a word but makes no sense here, and sister 1332 has Laura. "separ" for "seiar" is not a word.
- Language and context: idiomatic Portuguese of the period; "passeiar" is an acceptable old spelling; "lagar", "ao sol posto", "tenho de ir" all natural. Date line 12-6-913 and address (Joaquim Picciochi Garcia, Entroncamento) read correctly in clear and match the portal (which spells him Joaquin). Atalaia and Entroncamento are neighbouring places. Sister 1332: same recipient, Quinito, Laura, Luizito, amorsito, tua Triz.
- Restorations, all marked `!` in the transcription and disclosed:
  - Line 8, first sign (a of "ao"): blotted, printed "W." over it, but the lead-in, blot and right hump are visible and fit U. Fair.
  - Line 14, signs 2 and 3 (o, g of "logo"): under the print. At 6x a cross is partly visible under "rie" (arm ends at lower left and lower right, upper arm by the "r"), and under "Nr." two heavy parallel strokes with a following stroke fit W. The solver is if anything too cautious; marking them as restored is correct. The ink separation is weak (ink and print overlap), so W rests on shape plus "ate logo".
  - Line 6, first sign under "&": closed head and long tail visible, fits p.
- Sources: no sign of a published solution in the files; portal status Not solved, nothing attached. The 1332 use is disclosed.

## Findings

1. **major: q is filed under the wrong sign class.** The key puts q in U (a, q, v) and g alone in W. On the card, the q of "Quinito" (line 1) and of "que" (line 4) match the W of "logo" (line 2) and "lagar" (line 7), not U. `review/work/qg.png`, left to right: q, q, g, g, then a. The first four have two heavy parallel down strokes; the a has a thin lead-in and one heavy stroke. Sister 1332 lists exactly this sign for q and g ("ω-like, heavy first stroke"), so the shared sign was available. Line 4 q is partly under "Vienne" but its heavy stem is visible.
   Fix: change the 2 tokens U.q to W.q in `work/transcription.txt`, update `work/key.json` and the table: W = g, q; U = a, v. Recount the context-dependent signs.
2. **minor: i and p are probably two signs, and the solver's counterexample does not hold.** SOLUTION.md says the open/closed Q difference fails "in Quinito". The difference to test is the one in 1332: i has a curved tail, p a straight one, not open versus closed. In `review/work/ip.png` both i of Quinito, the i of "Triz" and of "amorsito" all have a head with a right tick and a curved tail. The p's I looked at (por, pas, provavelmente, Paulo) have longer, straighter tails. I sampled these rather than measuring all 16 Q signs. Fix: inspect all 16 and split the class if it holds, or state why it does not. No reading changes either way.
3. **minor: "75 of 197 signs depend on context" is both too high and too low.** Too high because of findings 1 and 2. Too low because L and I are not cleanly separated either, and this is undisclosed. The r of "amorsito" (line 14) is a short stroke with a foot and its t is the taller sign (`s15_2.png`), the reverse of the table's "short slanted stroke" for I; t in "-mente" (line 6) is tall too. Sister 1332 has d, r and t as distinct signs; the solver did not test that for d/r. I could not separate d and r on this card from the crops either. Fix: disclose L/I overlap in Uncertainties and describe I as a stroke with a foot.
4. **minor: Y and Z are compared with nothing.** Uncertainty 6 leaves j open. Sister 1332 has a single ζ for j. Fix: compare and say so; probably one sign.
5. **minor: table and data disagree.** The table gives T = c, ç but key.json gives only c, and the transcription has T.c for the ç of "coração"/"abraço". Harmless; align them.
6. **minor: SOLUTION.md says "No web search" is nowhere stated for this card.** It says no published solution "was found", without saying how far anyone looked. State the extent of the search, as 1332 does.

## Could not verify

- Who Triz, Luizito, Laura and Paulo were, and whether "lagar novo" is a place name.
- The exact shapes of signs 2 and 3 of line 14, beyond compatibility.
- d against r as separate signs on this card.
- Whether the mark over "pas-" means anything.
- Whether any other edition of this card has been published; I ran no web search. The orchestrator's register check is the only one I rely on.
