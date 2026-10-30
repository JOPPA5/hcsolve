REVISE

# Review 1 of hcp-1368 (pc_hcp_49), reviewer Claude Opus 5.5, 2026-10-30

**Summary.** The Caesar -1 reading of all the running words stands: MY OWN ... BOY / POST CARDS / TO DAY VERY / NICE / YOUR OWN ... GIRL. I tried to break it and could not. The solution's treatment of the abbreviation group does not hold up. The first initial is written as M on this card, not N. The trailing `t` cannot be a shifted plural on a group declared unshifted. The card's own sign forms point to `M. & L.t`, which under the same key gives L. & K.S, very probably "love and kisses". This is a concrete fix to the transcription, the plaintext line and the translations, so the verdict is REVISE, not ACCEPT.

## What I verified and how

1. **Solver command.** `python3 -I ciphers/hcp-1368/work/decode.py` ran. Source hashes OK. Output matches the plaintext table in `SOLUTION.md`, with 42 enciphered and 6 literal letters.
2. **Independent decode.** `review/work/decode_indep.py` holds tokens typed from my own crops and does not read the solver's files. It gives MY OWN BOY POST CARDS TO DAY VERY NICE S YOUR OWN GIRL, 42 letters. Count confirmed by hand.
3. **All 26 shifts.** Against a small vocabulary of the card's words, shift 1 hits 13 of 13 tokens and every other shift hits at most 1 (same script). That vocabulary is drawn from the reading itself, so the result is a sanity check, not an independent proof. The real support is that POST, CARDS, VERY and NICE are not formula words.
4. **Sign-by-sign check on the hi-res original.** `work/hires/pc_hcp_49_adr.JPG`, rotated 90 degrees anticlockwise. Crops at 3x, 6x and 8x with autocontrast are in `review/work/` (`c_L*.png`, `z_*.png`, `cmp_N_rev.png`, scripts `crop.py` to `crop4.py`). Results:
   - `Nz`, `Pxo` (twice), `Cpz`, `up`, `Ebz`, `wfsz`, `zpvs`: clear. The x of `Pxo` and the E of `Ebz` are unambiguous.
   - `qptu`: clear. The u is two thin minims in dry pen and the t has a long bar.
   - `dbset` (`z_dbset.png`): real, not forced. Next to `work/crops/w4.png` of hcp-1378, the same s with hooked top and base stroke runs into the pointed e. The t stem then rises, with a detached bar to its right. "dbeu-" is a tempting first look, but the structure matches CARD(S).
   - `ojdf` (`z_ojdf.png`): very pale but all four signs are visible. The d stem clearly rises above its bowl, so it is d, not a. The f has a tall top and looped descender. The blot at the top of the descender is the ink drop the solver reports.
   - `Hjsm` (`c_L7.png`, `z_sm.png`): H and s clear. The slash with hook is the j. Three minims follow, so m.
   - Heading `G. H. Friday` and date `July 26th 07`: plain and clear. The G has a descending foot (`z_head.png`), so G is preferred over C.
   - No sign on the message side is left out of the transcription.
5. **Context.** `datetime.date(1907,7,26)` is a Friday, agreeing with the heading. Postmark reads BORNE / 10 PM / JY 26 / 07, address reads Mr W. Abbott, Stokelake Farm, Chudleigh, Devon. Picture side reads "The Choir, West, Westminster Abbey", with no writing.
6. **Key coverage.** One shift covers every token marked as cipher. Plain parts are the heading and date, as on sister cards. The group `N. L.` / `N. & L.` is the exception (findings 1 to 3).
7. **Restorations.** None claimed and none found. There is no "completion" or "response to review" section, and all work is by one solver on 2026-10-30.
8. **Published solution.** None used or disclosed. The portal has no attached solution (`source/metadata.md`). I did not search the web myself.

## Findings

1. **Major: the trailing `t` is explained in a way that contradicts the treatment of the group.** Uncertainty 1 decodes `t` to S and reads `N. & L.s`, a plural, while the same section and the key section keep `N. & L.` as unshifted literal letters. A plural on an unshifted abbreviation would be written `s`. The ink is an unmistakable `t` (`z_L.png`). So `t` as a shifted S implies the letters before it are shifted too, or else `t` is not a plural. The solver lists this as "role not settled" but does not state the contradiction, and the printed English "N. & L.[s]" hides it. The bracketed S also mixes two regimes in one token.
   *Fix:* state that S and literal `N. & L.` cannot both hold, and decode the whole group as one unit (see finding 2).

2. **Major: the first initial is M on this card, not N, and the group probably means LOVE & KISSES.** `cmp_N_rev.png`, `z_amp_N.png`: the N of `Nz` has hook, stem and one leg. All three group initials (salutation, `& L`, closing) have hook, stem and two further downstrokes, the last short. Uncertainty 2 says "one or two arches vary" and picks N, but on this card they do not vary at random: all the group initials are three-stroke and the one word initial is two-stroke. The same M/N distinction was made on hcp-1347 (uncertainty 3).
   Read as `M. & L.t`, the group is the initial, initial and final letter of `Mpwf & Ljttft`. Under the unchanged key that gives L. & K.S, and LOVE AND KISSES is spelled in full (`Mpwf boe. Ljttft.`) on hcp-1362, a card of the same writer (same "G. H." heading, DONE1, not yet reviewed), and hcp-1348 has the same phrase. It would also explain why `t` follows the group, and it reads naturally: "Very nice. L. & K.s. Your own ... girl". The same slot on hcp-1402 ("My N. & L. from your own N. L. girl") would become "My L. & K. from ...".
   This is my hypothesis, not proved, and "L. & K.s = love and kisses" is an expansion. It is still a better account than an unexplained literal group plus a stray S, and it removes uncertainty 1.
   *Fix:* transcribe `M. & L.t` and `M. L.` (or justify N against the crops), report the shifted value L. & K.S with the proposed expansion marked as inference, and carry the other group (`M. L.` shifted L. K., meaning unknown) as enciphered-unresolved or literal, saying which and why. Do not retro-edit sister cards from here.

3. **Minor: the second initial in `N. L.` is normalised to L.** In the salutation and closing (`c_L2b.png`, `c_L6b.png`) the sign is a stem with a small foot or bowl, which by shape is h or b rather than the L of the `& L` group. Sister cards report this slot as `N. h.` (hcp-1349, 1366, 1371). The solver discloses the differing forms ("k-like", "b-like") but does not mention the h reading, and "read L by the sister formula" is a choice from context. The `& L` sign itself (`z_L.png`), with head stroke, stem and foot, is acceptably L, though the upper loop belongs to the f descender of `wfsz` above, as the solver says.
   *Fix:* name the alternative h.

4. **Minor: the "42/42" and "no adjustment" claim counts the disputed `t`.** That token has no word value in the printed plaintext, so the firm figure is 41 of 42 until finding 1 is resolved. It is also unjustified to state "6 abbreviation letters kept literal" as a clean split while the group's status is open.

5. **Minor: "accepted" overstates some sister cards.** The Origin section lists hcp-1400 among "accepted Caesar cards" and uncertainty 3 uses it to support `dbset`. Its `SOLUTION.md` is headed "Partial; no DONE1" and it has no markers. hcp-1396, cited for `M & L.s`, has no markers either. Within the cited range 1386 to 1407, hcp-1389, 1391, 1394, 1396 and 1400 have no FINAL. hcp-1378 is DONE1 / REVIEWED1 ACCEPT but has no FINAL. CARDS still stands on this card's own pixels and hcp-1378.
   *Fix:* cite only what is actually reviewed.

## What I could not verify

- The meaning of the group: "love and kisses" is an inference from hcp-1362 and hcp-1348, not stated on this card. The meaning of the separate `M. L.` group (shifted L. K.) is unknown.
- That all of the correspondence shares this abbreviation. I checked the sign forms only on this card, plus the crops named above from hcp-1378 and hcp-1402.
- The identity of the writer and of "G. H.". The town is inferred as Wimborne from the part BORNE plus sister postmarks.
- Which post cards are meant in "Post cards to-day".
