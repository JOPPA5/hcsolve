REVISE

# Review 1 — HCP 1539 / pc_hcp_220 (reviewer: Claude Opus 5.5, 2026-10-29)

## Summary

The key (Anna Tichá / Pepouš family key) is right and the content is right:
Pepouš thanks Anna for her card, asks whether his two cards of the 2nd and 3rd
went missing, and says he has been asked to play violin at an academy in Vamberk
in memory of bandmaster Vyskočil. **But the manual transcription has at least five
errors that my enlarged crops show directly.** These change the literal output in
four places. The solver's last section also adds two editorial forms that the
pixels do not support ("Ela", "Výškocil"/"bratr"). The reading stands, but the
transcription and SOLUTION.md need to be corrected before FINAL.

## What I verified and how

1. Ran the command from SOLUTION.md
   (`.../python3 ciphers/hcp-1539/work/decode.py`). It passes its hash checks and
   prints exactly the literal output claimed in SOLUTION.md (13 rows, 404 indexed
   positions, 2 alternatives). As the solver says, this only shows the manual
   record is self-consistent. It does not check the pixels.
2. Wrote an independent decoder, `review/work/decode_review.py`, with the key
   typed in separately, and ran it on `work/transcription.txt`
   (`review/work/my_output.txt`). The output is identical, and no symbol is
   unmapped, so the key covers the whole record. The key matches
   ciphers/hcp-1545/work/key.json. The labels differ but the classes are the same:
   here `y` is the family's 7/J sign, and `H` is the ř-shaped CH sign.
3. Rotated source/picture.jpg upright myself (`review/work/upright.png`) and made
   my own 3–16x crops in review/work/. I checked every row against the
   transcription at 3x. I checked these spots sign by sign at 6–16x: rows 1–2
   start, `c n1n`, `c3`, row 4 `spolu…`, the row 8 given name, row 9
   `bratra nac`, row 11, and the signature.
4. Checked the published-source disclosure in SOURCES.md and SOLUTION.md: the
   family key from Maxim Egorov's partial study and the earlier cards is credited.
   No published solution of this card is claimed or known.

## Findings

1. **[major] Row 2: `c m4n` ("s nim") is misread. The card has `c n1n` = S MYM.**
   (review/work/r2_snim_z.png, r2_mid.png)
   - The first sign after `c` is the two-hump n-shape with an entry hook (label
     `n` → M). It is the same sign as in `n5` (MĚ) and `n5c4s5` (MĚSÍCE) in the
     same and the next row. It is not the three-hump `m` (→ N) of `tm5cm4`.
   - The middle sign is the flat-footed `1` (→ Y). It is identical to the final
     sign of `qdh6d481` (ZTRATILY), the word right after it, and not to the `4`
     (→ I) inside that word.
   - Literal: **s mym** → "lístek, jenž křižoval s mým", i.e. "crossed with mine".
     That is better Czech and resolves the "antecedent of s ním" problem raised
     in the first editorial section.
   - The 2026-10-29 section already writes "s mým [literal: s nim]". That presents
     a correct literal reading as an editorial emendation of a wrong one.
2. **[major] Row 4: a sign is missing in SPOLU(U)ČINKOVAL.** (review/work/r4_spolu.png)
   - The card shows `cb3822s4mg3f68` with **two** `2` signs, so it reads
     SPOLUUCINKOVAL (spoluúčinkoval).
   - The transcription has `cb382s4mg3f68`, so the glyph count of 404 is also off.
     The solver's note that `spolucinkoval` is kept "without silently adding
     another U" is answering an omission in its own transcription, not the
     writer's spelling.
3. **[major] Row 8: the given name has four signs, not three, and "Ela" is not supported.**
   (review/work/name16_rgb.png, name16_red.png, rows9_11.png)
   - In the red channel, which removes most of the green tree, the name is
     clearly `8 ? 8 6`: an 8, a closed-loop sign, a second 8, and a 6.
   - The inventory records only `{5|8} 8 6`. The 2026-10-29 argument "8/L gives
     Lla, impossible, so Ela" rests on this wrong count.
   - The second sign looks most like `3` (→ O), which gives **LOLA** Beranová.
     `5` (→ LELA) cannot be fully excluded at this resolution.
   - Either way, ELA is not visible and must not be adopted. Re-segment this
     name and report it as L[O?]LA, with the uncertainty on the second sign.
4. **[major] Row 9: `ph6dh6 m6s` should be `ph6dh6m5s` = BRATRANEC.**
   (review/work/r9_nac.png, r9_bratranec_rgb.png, r9_compare.png)
   - The sign after `m` has a vertical stem, a flat top bar running right, and a
     lower bowl. That is the `5` form, as in `m5n3r8` (NEMOHL) in the same row
     (see the side-by-side in r9_compare.png).
   - It does not have the tall curved ascender of the two `6` signs in
     `ph6dh6` just before it.
   - The gap before `m` is no wider than the gaps between other letters.
   - Literal: **bratranec** (cousin), so "bratranec Vyskočil".
   - The 2026-10-29 editorial "bratr [literal BRATRA NAC]" drops a syllable that
     is on the card. It must be withdrawn. At minimum, record `{5|6}` with 5
     preferred.
5. **[minor] Row 11: the third sign of `m5q2s6cdm4n` is `c`, not `q`.** (review/work/r11.png)
   - The sign is the same open C-shape as in `c5` (SE) just before it. There is
     no 9-shaped z with a descender.
   - Literal: **nesucastnim**, a phonetic s for z in nezúčastním. Report it as a
     writer's spelling, as is already done for SO.
6. **[minor] The 2026-10-29 editorial contains unsupported forms.**
   - "Výškocil" / "Výškocila": the cipher gives VYSKOCIL(A). Nothing on the card
     supports ý or š, and the earlier editorial "Vyskočil" was right.
   - "Ela": see finding 3. "bratr": see finding 4.
   - The editorial has to be rebuilt from the corrected literal text. Also merge
     the two conflicting editorial readings and the Slovak translation into one
     consistent version.
7. **[minor] Confirmed as claimed. No action needed.**
   - Signature `b5b32c` = PEPOUS: the 2nd sign is a plain 5 with no c-hook
     (review/work/sig10.png).
   - `c3` = SO is clearly 3. Keep it as a writer's slip.
   - Rows 1, 3, 5–7, 10, 12 and 13 match the transcription at 3x.
   - Address side and date are unciphered.
8. **[minor] Status wording.** Once findings 1–5 are fixed, the only open point
   should be the second sign of the given name. "Complete reading" and "404
   glyphs" will need updating, and inventory.json and transcription.txt
   regenerated, so the single command reproduces the corrected text.

## Corrected literal text (reviewer's reading, for the solver to verify)

```
srdecny dik za dnesni listek, jenz krizoval
s mym. ztratily so opravdu oba me listky ze
dne druheho a tretiho tohoto mesice?
byl jsem vyzvan, abych spoluucinkoval na housle
pristi mesic ve vamberku, kde bude usporadana
akademie na pamatku zemreleho kapelnika
vyskocila, pri niz ma ucinkovati tez
pani maturova a pianistka l{o|e}la beranova
a bratranec vyskocil. nemohl jsem vsak nic
urciteho slibiti a nejspise,
ze se nesucastnim.
tisic pus zasila ti pepous. vyrid
prosim slecne jankove me poruceni.
```

## What I could not verify

- The source image is only 674x1024 px. My preference for `3` over `5` in the
  name (finding 3) and for `5` over `6` in BRATRANEC (finding 4) is a judgement
  on a few pixels per stroke. The count of four signs in the name is clear.
- I did not identify the persons (Vyskočil, Maturová, Beranová) or the Vamberk
  academy from historical sources.
- The postmarks on the address side were not transcribed (the solver discloses
  this too).
