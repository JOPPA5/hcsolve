REVISE

# Review 1 of hcp-1340 (pc_hcp_21) — Claude Opus 5.5, 2026-10-30

The reading stands. Key, transcription and sense all survived my attempt to refute them. One concrete fix is needed: the first word of the plaintext is silently altered by a hard-coded table, against the solution's own "spelling as ciphered" claim. The remaining items are minor.

## What I verified and how

1. Command from SOLUTION.md: `python3 -I ciphers/hcp-1340/work/decode.py` ran from the repo root. All four source hashes passed (also recomputed separately with shasum). Output matches the claimed plaintext apart from the disclosed editorial points and finding 1. 347 signs, 23 token types, as claimed.
2. Independent decryption: `review/work/mine.txt` is my own transcription in glyph notation, typed from my crops (not blind: I had already read the solver's file). `review/work/decode_rev.py` uses its own key, leaves 0 as "d or t", and compares each word with the solver's output. Result: 347 signs, 36 zeros, same 16 blocks and word counts. Only 4 words differ: `libste` (finding 1), and `kältet`, `bräutchen`, `nett`, which are the disclosed e-for-ä and Z points.
3. Pixels: every row of both text sides read at 4x from the hires originals (`review/work/adr_r*.png`, `pic_*.png`, 16 blocks, no block skipped). Contested signs at 6-8x (`review/work/z_*.png`): hae, both Z signs, Bräutchen, war (adr8 and corner), geküsst, Gruss. The heart-emblem "muss" at 4x (`adr_r13_0.png`): M, 5, a 7 through the emblem, a second 7, full stop; both 7s are visible, as the solver says. Nothing is restored from context there.
4. Key coverage: every sign I read has one value, except 0 (d/t, disclosed). No sign is unread except the faint stroke under Z in adr8, which is disclosed.
5. Language: real, informal German of a south-west German writer, 1905, with consistent private spellings (wider, Dinstag, get, kome, bekomen). No forced words.
6. Context: 8 June 1905 was a Thursday (computed), so Dinstag and Freitag fit. Postmark Schönwald (Baden) 9.6.05 and addressee Rosa read on the card. Triberg lies next to Schönwald. The plain Kurrent text agrees: "Gruss Euer Hermann", family greetings, Fräulein Rosa, Villa Waldlust, Schönwald.
7. Sources: portal status Not solved, no attachment (metadata.md). No other cipher's metadata or solution in the repo mentions Duffuer/Duffner, Schönwald or Bubi. 1340 is not in skip.txt or register-exclusions.json. No sign of a published solution being used, and I searched no further than the repo.

## Findings

1. **major — undisclosed restoration in the first word.** The card has 3 2 /· 7 0 # (`review/work/adr_r01_0.png`), which is l-i-b-s-t-e: no # after the 2. SOLUTION.md prints "Liebste" under the heading "spelling as ciphered", and uncertainty 5 does not list it. The change comes from the closed word list in decode.py: `"LIBSDE":"liebste"`, which inserts a letter the key does not produce. The literal form fits the writer's habit of dropping the e of ie (wider, Dinstag), so it should stand as "Libste". Fix: change the table to "libste" and the plaintext to match, add it to uncertainty 5.
2. **minor — decode.py's table can change more than d/t.** It replaces the entire word whenever D occurs, so the command does not show what the key yields. Besides finding 1 it also turns NEDZ into nett, and writes ä for e. Those two are disclosed, but the table should only choose d or t, and any other editing should be visible in SOLUTION.md or in a separate step. I found no further hidden changes in the table: the comparison in item 2 covers every word.
3. **minor — left margin misread (context only).** It reads "Frohes Wiedersehen!", not "Liebes Wiedersehen!" (`review/work/z_leftmargin.png`). The solver marked it uncertain and it is outside the cipher, but it will reach the report, so correct it. The large pen flourish above "Fräulein" on the address side is not mentioned; it has no bearing on the reading.
4. **minor — uncertainty 8 overstates a doubt.** The "side branch" on the second 7 of Gruss is the ordinary crossbar of the 7; the second 7 of Kuss shows the same mark (`z_gruss.png`, `pic_marg1.png`). The double 7 is sound in both words.
5. **minor — A/B difference is not always visible.** In adr8 "war" the left mark of the a sign merges with the tail of the W (`z_war.png`), and in the corner "war" it is only a small kink on the slash (`z_corner.png`). Those two rest on the word as well as the glyph. Add a line to the key note. The reading is not in doubt.
6. **minor — blotted sign not disclosed.** The 0 in Bräutchen has a heavily inked left side (`z_braeut.png`). I see no bar through it, and K would give no word, so 0 stands, but it belongs in the uncertainties.

## Solver's disclosures I checked and agree with

- hae: 1, ·/·, # at 8x (`z_hae.png`); no b sign. Correctly not restored in the transcription.
- Z: the same looped sign with a foot, after 0, in Schatz and in nett (`z_schatz.png`, `z_nett.png`). "nett" is literally "netz", as disclosed. The separate faint stroke beneath is really there and unexplained.
- geküsst has two ticks on the 5 and two 7s (`z_gekuesst.png`). Gruss and Kuss have no ticks.
- Liebste/Rosa: the ticks stand between the two words; R on Rosa is the sensible assignment.
- P and V occur once each.

## What I could not verify

- My transcription was not blind, since I read the solver's file first.
- The meaning of the faint stroke under Z in adr8.
- Whether Bubi is Hermann, and whether the couple were engaged (the solver marks both as inference).
- The word "Eltern" in the plain text, read only at low magnification. It is context only.
- Whether a solution of this card has been published outside the repo; I did not search the web. The orchestrator's register check found none.
- The order of the picture-side blocks; the sense does not depend on it.
