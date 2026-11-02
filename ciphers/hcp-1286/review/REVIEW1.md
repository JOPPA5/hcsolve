REVISE

# Review 1 of HCP1286 (Claude Opus 5.5, 2026-11-02)

The key, the identification (Jolánka family, Feri to Jolánka Tóth) and most of the reading stand. Three things do not: the card is not complete by this project's standard, because the row 7/8 clause is unread in substance; the poem opens with a misread word; and the ledger does not contain the signs behind the claimed row 8. The status must drop to partial unless row 7 gets a real reading. On the present text no register entry should be written.

## What I verified and how

- `python3 -I ciphers/hcp-1286/work/decode_rev2.py` ran; the three hashes are OK and the output is as quoted in SOLUTION.md.
- Independent decode: `review/work/check.py` rebuilds the key from the table in `ciphers/hcp-1216/SOLUTION.md`, decodes `work/ledger-rev2.txt` and aligns it with `work/normalized-rev2.txt`. The key covers every token. 616 tokens, 16 marked hidden (2.6%). The alignment shows every place where the normalized text has letters the ledger lacks; findings 3, 4 and 5 come from it. (`isten` shows an `s` insert there only because my script has no entry for the token `S`.)
- Own crops from `work/hires/...adr.jpg`: `review/work/crop.py` (colour), `review/work/sat.py` (violet channel), output in `review/work/c/`, at 2x to 8x.
- Sign by sign: rows 1 to 4, 7, 8, 14, 16 to 20, 22 to 24, 26, 27 and all stamp rows S1 to S9. Rows 5, 6, 9 and 11 only for their restorations.
- Picture side: viewed. Printed verse and photograph, no cipher.

Confirmed on the pixels: row 16 `külvesben` is nine clean signs, with the dot over the u visible; row 14 `lehe e`, no t sign; row 3, row 22, rows 23 and 24, row 27 up to `feri` along the bottom edge; stamp rows `n vele`, `esemma`, `doksze`, `töked`, `es9efe`, `ricsoko`, `lomszam`, `talaszor`, X. `vala|mi`: the sign before the final bars is a wave cut by the cancel line, acceptable as l.

## Findings

1. **Major: row 7/8 is an unread clause, and the card is not complete.** The offered text "hogy bájos az, és szebb oly valami, hogy még ők, édesem, feljönnek Pestre" is not idiomatic Hungarian, and the translation "lovelier still is such a thing" is filler, not sense. SOLUTION.md itself gives two opposite meanings (bájos, bajos), an undecided word division and an alternative `megy ő kedesem`. That is a clause without an established meaning, not an isolated word. With `külvesben` on row 16 the card has two un-understood places, so the rule for an alone word does not apply. Fix: state the status as partial and give row 7 to `valami` as signs read, sense open, unless a real reading is found. No register entry on this text. The surrounding sense (news from Sándor's that they may come up to Pest) is secure from rows 9 to 15.

2. **Major: the `y` of `oly` has no place on the card.** The ledger has `[Y]` between l and v, and SOLUTION.md says it would lie at the postmark rim at hires x about 975. The rim is at about x 1112, and x 975 is between the second b and the o. At the rim (`review/work/c/y1.png`) the wave l runs up to the rim and its rising tail continues on the far side at about x 1120 to 1135. The v starts at about x 1147. There is no room and no trace of a sign. The card reads `szebb olva?a|mi`, without y. Fix: remove `[Y]` from the ledger and `oly` from the text. This weakens the sense further and may help a new reading (`ol va la mi`, undivided).

3. **Major: ledger row 8 omits three signs, so the command does not produce the claimed text.** Ledger: `M I H O G? O K E D ...`, literal output `mihogokedesem`; normalized: `mi, hogy még ők, édesem`. On the card (`c/d.png`, `c/e.png`) the row runs: m, i, h, o, g + y (the same two-part hogy as row 2), m (three strokes at hires about x 530), e (bars under 14), then the hook/descender under the J, o, k. The signs exist and the reading of `hogy me..` is right, but the ledger must be corrected: `M I H O GY M E G? O K E D E ) E M + E L`. As it stands the normalized text has `gy m e` with no source in the command output.

4. **Major: row 18 is `ha`, not `de`.** The first word of the verse is ledgered `D E`. The sign (`c/z1.png`) is a long stroke with a separate short tick to its right, the h/p form, as in `hoz` (row 22), `kep` (row 19) and `szep` (row 23). The d on this card has the tick on the left, at the top of the stroke, as in `boldog` (row 23) and `dest de` (row 17). The next sign is two dark bars, that is a; a very faint mark below them is separate and may be a stray or the top of row 19. So the verse is `Ha magamba vagyok, fölidézem képed`, "When I am alone, I call up your image", which is also the only reading that makes verse sense. English and Slovak need the same change (`Keď som sám`). If the solver keeps three bars for the second sign, the call `he` still cannot be `de`.

5. **Minor: row 17 ledger and spellings.** The card has one t: `S ≡ Γ ö F`, literal `ketöre`, not `kettöre` (`c/r17.png`). Remove one T from the ledger and add this to the spelling list. The missing j of `monda`/`mondja` is also not listed under uncertainty 10.

6. **Minor: under-stamp brackets.** `szám[ta]lanszor` is wrong: the card has `szám|talaszor`, so the supply is `számtala[n]szor`. The supplied `ma[ra]dok`, `sze[re]tő` and `ked[v]ese` are not discussed in Uncertainties. Rows S3 and S4 begin right at the torn edge of the surviving stamp fragment, so `ra` and `re` were probably lost at the row start, like `[Iste]` and `[éd]`, and are not spelling omissions. Say which is meant. In row S2 the first visible sign is a three-bar e at the tear, consistent with `[ed]esem`.

7. **Minor: "two questions" = two verses is not coherent.** Verse 1 asks nothing. The two questions are the two `Mikor` lines, each ending in `?`, both under numeral 2. The key-section bullet and uncertainty 7 should say so, or leave the role of the numerals open. "Each verse of 2 ends in a plain ?" is right.

8. **Minor: restorations rest on context, as disclosed, and I could not confirm them on the pixels.** Row 6 `hal[lott]am`: in colour and violet-channel crops (`c/r6.png`, `c/v6.png`) the signs under the dome are not legible. Row 5 `S[a]ndor`: name supplied by sister cards. Row 9 `[r]e hát így`: strokes are there and the count fits, but no sign is individually provable under the frames. Row 11: h and the t arm beside the 0 appear, the a does not. All are disclosed; keep them as word sense and do not describe the signs as seen in "Why it is correct".

9. **Minor: the plain-text address side is not recorded.** The handwriting (`Szépreményű`, `Tóth Jolánka`, `úrleánynak`, place name) belongs in SOLUTION.md and in the report. The brief applies to the whole card.

## Not verified

- Rows 10, 12, 13, 15, 21 and 25 were looked at, not checked sign by sign. I found nothing against them.
- I did not find a reading for `külvesben` or for row 7. `különben` and `küldök` do not fit the signs.
- I did not recheck the portal live for a published solution; I rely on `source/metadata.md` and the orchestrator's register check.
- The final bars of row 18's second sign: two is my call; the third faint mark cannot be excluded.
