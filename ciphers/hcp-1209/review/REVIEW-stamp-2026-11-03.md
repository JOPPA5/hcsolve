CORRECTIONS

# Review of the stamp-box message, hcp-1209 (2026-11-03)

Reviewer: Claude Opus 5.5, working on its own. I made my own crops from `work/hires/cpc_1914-11-23_HU__HU_Budapest_jolanka-56_adr.jpg` (3421x2176) with `review/work/stamp-2026-11-03/rc.py` and `rc2.py`: the box at 2x in RGB and red; rows 1-6 at 4x in RGB, red and green-minus-red; sheets for rows 3-5 in R, G, B and differences; and 6x red crops of the hidden zones in rows 3 and 4 (`z_r3mid.png`, `z_r4mid.png`). I read the crops by eye before comparing them with the claim. I changed none of the solver's files.

## What I confirm

- **Something is written under the stamp.** The stamp has been lifted. Its orange corners (top left, bottom left) and its perforation outline are still there, and a blue-green triangle ghost lies over rows 3-5. Six rows of green cursive fill the stamp place, in the same ink and hand as the letter. So the card does use steganography: a message written under the stamp.
- **The box holds no cipher signs.** It is plain Hungarian cursive, and none of the Jolánka graphic signs appear. The main text (left side, read on the overview `overview.png`) is also plain Hungarian cursive.
- Row 1 reads `[c]sokol`. The first letter is under the orange corner; only a lead-in stroke shows.
- Row 2 reads `szerető`, clear. The ő is written with two dots or strokes.
- Row 3: I see `v`, then `ő` (two dark accent marks), then inside the ghost one large closed round loop, then `g` (bowl with a descender), `e` and a hyphen, all clear. The pattern is `vő ? ? ge-`.
- Row 4: I see `n` (clear, two humps), then a dark knot under the ghost, then `e` (clear), then a small bowl and a tall rising stroke, which fit this writer's `d` as in *Ferikéd*. The pattern is `n ? ed`.
- Row 5: two loops on the left (ő/ö-like), a gap of ghost, then a T-like tall letter, `e`, and a stroke. I agree this row is **unread**. I could not get a word out of it in any channel.
- Row 6 reads `Ferikéd`, clear, with the accent.
- **Type:** the solver did **not** apply "MASC + Steganography", and that is correct. The card has no substitution cipher anywhere, so the MASC part would be false. Writing under the stamp exists, but on this card it is the only concealment, and it is in plain text. There is no `register-entry.txt` and no report, which is consistent with that.

## Differences / corrections

1. **(minor) The restoration goes beyond the one-letter rule.** *vőlegényed* restores three signs in one word: `l` and `e` in row 3, and `y` in row 4. The second `é` accent is also not seen. My 6x red crop of row 3 shows one round closed loop. I cannot tell whether it is an `l` loop or an `e`/`o` bowl, and it is not clear there is room for two letters. In my 6x crop of row 4, the zone between `n` and `e` is a dark knot with no visible y-descender. The word is the natural fit for `vő??ge-n?ed` after *szerető*, and the solver does call it "probable, not certain". But under the standard (only one physically hidden letter may be restored), this should be presented as a **conjecture**, for example `vő[??]ge-n[?]ed (conj. vőlegényed)`, not as a reading with restored letters.
2. **(minor) The literal transcription adds an accent the card does not show.** Row 1 shows `sokol`; I see no accent over the first o. The literal line should read `[c]sokol`, with *csókol* only in the normalized text.
3. **(minor) SOLUTION.md contradicts itself.** The older parts of the file were not updated:
   - the "Plain text" block still has `Stamp place: [c]sókol / szerető / [?]ő[?]e- / [?]e[?]l / [?][?]te[?] / Ferikéd`;
   - the "Uncertain" bullet still says *szerető vőlegényed* "is not claimed".

   The new section claims it as probable. One of the two should be brought in line with the other, preferably the old lines to the new section with the conjecture marking from finding 1. Row 4's literal `[?]e[?]l` in the old line should also become `n[?]ed`, because `n` and `d` are visible.

## Not verified

- Row 5 (one or two words before *Ferikéd*). I could not read it.
- Whether the round loop in row 3 is `l` or `e`.
- Whether anything is written under the orange corner remnants beyond the `c` of row 1.
