REVISE

# Review 1 of hcp-1152 (Claude Opus 5.5, reviewer, 2026-11-02)

The decipherment stands. All 118 cipher signs, the key and the enciphered sentence survived an attempt to refute them. One word of the open verse is mistranscribed (`keblem` for `kebelem`) and has to be corrected in `SOLUTION.md` and `work/decode.py`. After that fix, and the small disclosures in findings 2 to 6, the card can close without another round. A re-review is not needed unless the reading changes.

## What I verified and how

- Command: `python3 -I ciphers/hcp-1152/work/decode.py` ran. Hashes OK, 118 signs, 114 by table, 4 by sense. Its output matches the plaintext in `SOLUTION.md`. Note that it only asserts the cipher words; the open text is hard-coded, as the solution says.
- Independent transcription: I read all 8 cipher lines sign by sign from my own 2.5x crops of the hires scan (`review/work/crop.py`, `a1.png` to `a6.png`), before comparing with the solver's lines. Then `review/work/mydec.py` decoded my list with the raw key and no sense repair. Result:

      fedves magitkám
      mi van veled hogy nem
      irsz hik talán csak nem
      haragkol csak ugyan ir
      jál kedves kérlek
      szépen ne kom?ricsd a szi
      vemet én úgyis irok
      mindig

  That is 118 signs, the same count, with no sign disagreeing with the solver's transcription. The only non-words are the three disclosed dotless or odd signs and the blot. Every mark that changes a value (comma, dot, colon, high dot, left dot, left dash) was checked against the crop.
- Key: every value agrees with hcp-1174 (table), hcp-1168 (`.1` = u) and hcp-1170 (`-1` = ú). The whole ciphertext is covered, 25 sign types. No value was invented for this card.
- Picture side: portrait only, no writing, on both scans.
- Claimed restorations and odd signs at 8x (`blot.png`, `k.png`):
  - `Kedves`, first sign: confirmed as an odd closed 4-like form with a bar, with a dark spot in the loop. Not a clean 7. The word is fixed by the second occurrence in line 5.
  - `hisz`, `haragszol`: confirmed. Crossed 7 with no dot anywhere near it.
  - `komorícsd`: the blot is a solid slanted oval, the same size and tilt as the `0` just before it, with no counter visible. The preceding 8 is also filled in, with its lower bowl partly open. Reading the blot as `0` is a restoration from sense plus shape, and it is disclosed as one. I found no better word: `komorítsd` fits `a szívemet`, and `2, 3` is clean, as is `3,` right after the blot.
  - `írjál`: confirmed. `1 3,` plus hyphen at the margin, then plain `6`, `1` with one high dot, `5,`.
  - `ugyan`, `úgyis`: left dot and left dash are both on the card.
  - `Magitkám`: confirmed, no `3,` between `1.` and `4,`.
  - Word gaps: the division `csak ugyan` is real on the card.
- Plain language: the cipher part is natural Hungarian of the period and runs on into the clear `még többet ez után`. Spelling such as `csak ugyan`, `irok`, `komorícsd` is a plausible writer's habit, and each is disclosed.
- Open text and address: read line by line at 2.5x (`b1.png` to `b6.png`, `lehel.png`, `sorv.png`, `mind.png`, `szepr.png`). `Tek.`, `Szépreménnyü`, `Sziber Margitka`, `kisasszonynak`, `Szomolya`, `u. p. Bogács`, `Sz. A.` and the pencil `1915 XII 5` all confirmed. All verse lines confirmed except as in findings 1 and 2.
- Sister claims: `Sz. A.` is on hcp-1176, 1179 and in the notes of hcp-1175. The `.1` and `-1` citations are true. Metre and rhyme of the poem were checked by counting syllables.
- Sources: the portal captures in `source/metadata.md` give no solution. `SOURCES.md` lists all four scans. A search of `ciphers/*/SOLUTION.md` shows no other card with this poem.

## Findings

1. **Major: `keblem` is a misreading of `kebelem`.** Crop `review/work/keb.png` shows k-e-b-e-l-e-m: two tall strokes after the k, b and then l, with a full `e` between them. The form printed has one letter too few. The word also decides the stanza: `Tikkadt mező a kebelem` has 8 syllables like the other three lines, while `keblem` gives 7, and `kebelem` rhymes fully with `szerelem`. Fix it in the plaintext and in the hard-coded verse in `work/decode.py`. The meaning and the translations do not change. It is an open-text error, not a cipher error.
2. **Minor: `hintani` and the metre are not reported.** The pixels (`hint.png`) do look like hint-a-n-, with no dot seen on a final i, so the printed form may be right as a reading. But `Csókot hintani ajakadra` has 9 syllables against 8 in every other line of the poem, and the note in Uncertainties offers only `hinteni`, which also has 9. Say that the line is one syllable long as read, that the expected metrical form would be the short `hintni`, and that the final i has no visible dot. Do not change the reading unless the pixels support it.
3. **Minor: "the words are certain" overclaims for one word.** The Uncertainties section says all four sense-read signs sit in words that are certain from the other letters. That is right for `Kedves`, `hisz` and `haragszol`. For `komorícsd`, item 4 itself says it is the only word found to fit, which is weaker. Word the opening sentence and the matching line in "Why I believe it is correct" so that the restoration is excepted.
4. **Minor: two `1.` marks are not quite dots.** In line 4 the marks after `1` in `haragszol` (second sign) and `ugyan` (third sign) are elongated, comma-like ticks (`a3.png`, `a4.png`). `1,` is b on hcp-1168, so read strictly these could be taken for that sign. The sense is unambiguous and I read them as `1.` too, but they are table reads only by judgement and deserve one line, as with the other sign-shape notes. The count of 114 may stay.
5. **Minor: the translations normalise `leheletét`.** The Hungarian has the third-person possessive (`its/her breath`), and both translations print `your sweet breath` (`tvoj sladký dych`) without saying so. The verse sets `ajakadra` (your lips) against it, so the shift may be forced by the rhyme with `betegét`, but this is a note the reader needs. Add it to Uncertainties.
6. **Minor: one citation is loose.** `mindnyájatokat` is said to stand on hcp-1157, 1169 and 1170. hcp-1169 has `mindnyájatoknak` (same stem, other case). Correct the list.

## What I could not verify

- The postmark. The stamp shows a heavy 9, a D or 0, N, C and a 5, overprinted and rotated; I could not get a date from it. The date rests on the pencil note and the portal file name, as the solution says. The note's digits share the writer's forms (long-flagged 1, 5 with a detached bar), which supports his hand but does not prove it.
- Whether the HistoCrypt article discusses this card, and whether the poem is printed elsewhere. Both are disclosed as unchecked. I did not check them either.
- The sense of `nem érkeztem`. "I had no time" is plausible regional usage and is labelled an interpretation. I have no period source for it.
- `sivó` against `sívó`: I see a dot, not an accent, on the i, which fits the printed form, but the meaning "barren" for this form is not independently confirmed.
