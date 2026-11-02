REVISE

# HCP1292, review round 1 (Claude Opus 5.5, reviewer)

The family key and the bulk of the reading stand. The story is genuine: a railwayman's letter about wine, falling asleep on the brake, and a denial about a railwayman's daughter. Three passages are wrongly parsed or misread, and one of them reverses the sense of a sentence. All three fixes are concrete, so this is REVISE, not REJECT. The fixes also appear to remove the "one open word" as claimed and replace it with a different one (finding 3).

## What I verified and how
- Ran `python3 -I ciphers/hcp-1292/work/decode.py`. The three hashes are OK and the output equals `work/ledger.txt` and `work/normalized.txt`. The command only prints the manual ledger. It does not decode from sign tokens, so it proves no decipherment by itself (the README's source-plus-key command is met only in that weak sense).
- Own crops from the hi-res address scan: `review/work/crop.py` (red channel, autocontrast, 1 to 8x), outputs a1-a4, b1-b3, c1-c5, d1-d4, e1-e3, f1-f2, g1-g4, s.
- Read all 31 rows and the 9 stamp rows at about 3.4x, and every disputed spot at 5 to 8x.
- Independent script `review/work/indep.py`: my own sign tokens for the disputed rows (8, 20 end, 21, 28 end, 29, 30, 31) through my own key dictionary built from the HCP1216 table, printing `megát`, `hogy`, `jelhogysemifélvasutasnak`, `becsületszavaénel`, `lötem`, `fomszorol`, `szorornidecsak`, `szavát`.
- The same script aligns the ledger with the normalized text and lists every divergence. Key coverage: every ledger letter is in the key.
- Picture side: print only, "Két szív ha földobog" and the verse; no cipher. Confirmed. Address: Szépreményü / Tóth Jolánka / úrleánynak / Jász Árokszállás, plain hand. Confirmed. No portal solution exists; no sign of a published source.

Confirmed on pixels: `vasutasnak` (row 21: plain x, two bars after t, unambiguous); `a lanyorol` (row 22, F = r); `elaludtam a féken`; `ér semmit` (row 26); `remél|hetam hetek` (row 20, self-correction, plausible); undotted o in row 20 `hogy` before `jel` (crop e1), so the slip for `higy` stands as disclosed; row 8 signs m e g á t (crop g3: three bars, then two bars with acute); stamp block `isten vele édesem marakto vebra is kedves|se és sirig hű imadoja feri` (crop s).

## Findings

1. **major: row 28-29 is misdivided, and the meaning is reversed.** The solver normalizes `szavaénel|lötem` as "az ön becsületszavánál előttem" and admits "the -é- is an unexplained extra sign". The signs are clear (crops b3, d1, f2): sz a v a é n e l | l ö t e m. Without changing any sign this reads **"az ön becsületszava én előttem"**: "de annál többet ér az ön becsületszava én előttem", "but all the more is your word of honour worth before me". It is the exact counterpart of the preceding "nem vesztettem el becsületemet ön előtt". Only the doubled l at the row break is a slip. The solver's reading needs a dropped sign value and a changed case ending, and it makes him rate his honour above hers, the opposite sense. Fix the normalized text, English, Slovak and the "Why it is correct" claim.

2. **major: row 30, the sign before `de` is a dotted i, not o, and the claim "checked, undotted" is wrong.** At 8x (crop g1) a dot of the same pale ink as the sign stands directly above it. The sign has the same form as the i of row 21 (crop e3): the stem rises above the junction of the tail, whereas o runs from the top of the loop into the tail. So the row is `szororni de csak`, not `szororno de csak`. This destroys the "no de" interjection and the solver's statement "no separate main verb", "no sign is unread here". With fo[go]m the row has the future construction **fogom + infinitive in -ni**. The verb the solver's notes say is missing is there.

3. **major: the word `szororni` is the real open word and must be declared.** The clause is "ezt a levelet fo[go]m szóról ... -ni, de csak esküvője napján". A plausible hypothesis is that it is a garbled "sorolni" (recite, list): "I shall recite this letter word by word, but only on your wedding day", which is a coherent threat and fits *szóról*. NOTES rejected sorolni because "l is not F". That objection holds at sign level: the written sign is F, and the writer also adds sz. So this needs an r-for-l slip and is not proved. Present it as a marked conjecture, or leave the word open with the clause otherwise read; do not keep "szóra, no de". The existing normalization turns F into a and silently deletes `or`, as the alignment in `indep.py` shows (`or` -> `a`). As a single unresolved word in a clause that otherwise reads, it does not by itself make the card partial.

4. **major: row 8 `megát` is not an un-understood word; the sentence was cut in the wrong place.** Read with the preceding clause: **"hogy el kell vesztenem magát, édes. Én is borban kerestem a vigasztalást"**: "that I must lose you, sweet. I too sought consolation in wine". *Magát* is the formal "you", the object of *vesztenem*; the card uses the formal address throughout. The stray "[Megát?], édes, én is" clause disappears. The e-for-a slip is directly supported on this card by `fejdalmat` (row 6, three bars for á), and by `kifajezni` and `keres|tam` for the reverse confusion. Note that the solver's cited parallel `szevét` is itself wrong (finding 5). Adopt it, marked as a normalization of e to a.

5. **minor: row 31 is `szavát`, not `szevét`.** Crop d4 shows two bars in both vowel positions (with an ink blot on the first; the second has an acute). `work/ledger.txt` and the "Smaller points" list are wrong; the normalized word is unchanged.

6. **minor: the row 21 and 23 m's are word-sense restorations and should say so plainly.** The third stroke of `se{m}i` is a pale slanted mark exactly on the vertical stain that runs down through rows 21 and 22 (crops c3, e2, e3); it may be ink but cannot be told from the stain. Row 23's first sign is under a blot with two strokes visible. The solver states both, but the summary "sign-level corrections ... that the key already defines" overstates row 21. The reading *semmiféle* itself is safe.

7. **minor: ledger details.** Row 28 appears to have a single 6 (crop b2), so `töbet`, not `többet`. Stamp rows 5-6 write `kedves|se` with s twice; the normalized *kedvese* silently drops one (not in the slip list). Add both to the disclosed slips.

8. **minor: reproduction.** `decode.py` prints letters only. Acceptable given manual reading, but SOLUTION should keep saying so; add the corrected rows to the ledger rather than only to the normalized text.

## Corrected passages I propose (for the solver to judge)
- "... az a tudat, hogy el kell vesztenem magát, édes. Én is borban kerestem a vigasztalást ..."
- "... nem vesztettem el becsületemet ön előtt, de annál többet ér az ön becsületszava én előttem."
- "Hogyha esetleg cserbe hagy, ezt a levelet fo[go]m szóról [szororni: sorolni?], de csak esküvője napján ..."

## What I could not verify
- The intended verb in row 30; `szororni` is not attested as a word.
- The blacked-out word in row 25 (agreed, unrecoverable).
- The stain-covered signs listed by the solver (rows 2, 4, 9, 17, 27) are consistent with word sense but are not independently provable.
- I did not compare handwriting with other Feri cards. The date is unknown; the partial postmark (…GALÁNTA) gives no year.
- My sign-by-sign check of ordinary rows was by eye on crops, not a blind second transcription of the whole card.
