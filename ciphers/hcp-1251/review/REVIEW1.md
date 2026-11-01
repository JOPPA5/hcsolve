REVISE

# Review 1 of HCP1251 (Claude Opus 5.5, reviewer, 2026-11-01)

The reading stands as a whole: this is Feri's Easter 1914 letter to Jolánka Tóth, Hungarian, in the family key. The ledger is not a faithful sign record in two places, though. Row 4 has two signs that are not on the card and omits one that is. Row 26 has one invented sign, which then generated a false restoration. All fixes are small and none changes the sense of the letter.

## What I verified and how

- Ran `python3 -I ciphers/hcp-1251/work/decode.py`. All 4 hashes are OK, it prints 772 signs, and the output equals the literal table and the normalized text in SOLUTION.md.
- Independent decode: `python3 -I ciphers/hcp-1251/review/work/indep.py`. My own sign-class transcription of rows 1, 4, 5, 12, 15, 18, 20, 26 (first part) and 28 was decoded with HCP1216's `graphic-key.json`, not this card's key, then diffed with the ledger. Rows 1, 5, 12, 18, 28 agree exactly. The only differences are findings 1–3 below.
- Read all 28 rows and the stamp box from the un-converted original on my own 2–4× crops (`review/work/c/`, made by `review/work/crop.py`). Every restoration (uncertainties 6–13) was examined at 4×. For row 4 I separated green ink from black postmark ink (`review/work/c/l4m.png`, `g4.png`, `review/work/gf.py`).
- Context: the card is cancelled BUDAPEST 914 APR 12, and 12 April 1914 was Easter Sunday. The address in clear reads Szép reményű / Tóth Jolánka / úrleánynak / Jászárokszállás. The picture side has no cipher by the solver's account; I did not re-inspect it beyond confirming the cipher lies on the address side.
- Language: natural early-20th-century Hungarian with the writer's real spelling habits, a coherent argument and the family's formulae. It is not words forced onto noise. Portal status and the absence of a published solution are stated, and I found no sign that one was used.

## Findings

1. **major: row 4 end, `lahobe` is wrong; the card has `lapot`.** After the h/p sign and the o loop (with its right arm) there is one more sign, a gamma. Its stem rises to the right at about x 1620–1640, y 355–370 and its top bar runs right under the black "D" of the postmark to about x 1670 (y 335). The colour separation `review/work/c/l4m.png` shows it unbroken. Nothing follows it; there is no six and no bars in row 4. The row-5 `ybe` sits lower in the same area and must not be confused with it. So the ledger's `b e` are not on the card, and they are not marked restored. SOLUTION.md's "there is no t between them that I can see" and its "loose preverb" explanation are refuted. Fix: row 4 `…egylahot`; normalize *egy lapot múlt levelére Jászberénybe*; delete `lapo for lapot` and *lapo[t] be*, and correct the key note listing *lapo* as a chevron-l example only if needed. *Múlt* then needs no *be*, and the sentence becomes plain grammatical Hungarian.

2. **major: row 26, a phantom second k; *ked[v]esem* is an artefact.** Crop `review/work/c/r26.png` shows `g a n a k e d e s` with a single section-mark S between the two-bar sign and the three-bar sign, so literal `maganakedesem` = *magának, édesem*. The ledger's `maganakkedesem` adds a sign that does not exist, and the restoration *ked[v]esem* ("my dear") plus the spelling note `kedesem for kedvesem` rest on it. Fix the ledger, normalized text and all three translations ("my sweet" / "zlatko"), and remove the note. The word *édesem* in this card is then simply one more instance of the writer's standard address.

3. **minor: two "writer's spellings" are a/e choices made against the pixels.**
   - Row 15: after the v in *szét-vál-* the sign is clearly two bars (`review/work/c/r15.png`), so `szetvalasszon`. *szétvélasszon* is not the writer's spelling.
   - Row 20: after the six there are two bars and a small dot below them (`review/work/c/r20.png`), so `barmijen` or at most an e with a stunted third bar. *bérmijen* should not be listed as a spelling on the card.
   Change the ledger (row 15) and list row 20 under the a/e uncertainty.

4. **minor: the key claim "the hooked g sign also stands for k in *kívánok, fogok, eltartsak*" is unsupported.** All three final signs are the ordinary section-mark S with a left foot (`review/work/c/kiv.png`, `r27e.png`, `k_tartsak.png`). Compare the true hooked g immediately before in *fo-g-ok*. Delete the variant from SOLUTION.md and key.json. Only the large S for g at the start of row 22 needs keeping (and row 16's large double-looped g in *drágám*, which is not noted).

5. **minor: row 13 is under-described.** There are two overwritten blocks, not one: the z with bars struck over its right side, then a separate box of several strokes closed by top and bottom bars (`review/work/c/r13.png`). *Szabad* is safe from sense and `6 = d`, but the ledger gives only one `[a]`. Say that the block is a correction and that which strokes are the intended a cannot be determined.

6. **minor: the stamp box's *vele édesem* is compressed.** The literal `{e}ledese[m]` gives normalized *vele, édesem* only if {e} is dropped and one e serves both *vele* and *édesem*. That is reasonable for a faded line but should be stated, since uncertainty 13 calls {e} only an "extra bar sign".

7. **minor: "repeated words" counts in "Why it is correct" are wrong.** The ledger and `normalized.txt` have *hogy* ×6, not ×10, and *édesem* ×4, not ×6 (×5 after finding 2). Correct them.

8. **minor: smaller disclosure points.**
   - Row 10 *ünnepeket*: the fourth of the four strokes carries a horizontal top bar, so it looks like a stroke plus gamma (`review/work/c/r10.png`). *nn* rests on word sense; say so.
   - Row 10 *jö*: the accent is a dot plus a longer tick and may be ő. *a jő húsvét* would need no omitted *-vő*. Note it as an alternative.
   - Row 10 *hu[s]vet*: the sign is better than stated. The crop shows a right bowl under the postmark, not a "cross-like" shape, so it can be `s` as a weak reading rather than sense only.
   - Row 25 *édes[em]*: the literal *édes* could stand as written; the restoration is optional.
   - Sister support: HCP1263 and HCP1272 have no FINAL marker, so do not lean on them as finished cards for Ilonka and Berény.

9. **minor: the reproduction command does not apply a key.** `work/ledger.txt` is already in plaintext letters and `decode.py` only validates and prints it, so `key.json` is descriptive. Say this plainly in SOLUTION.md, or transcribe signs by class as HCP1216 does.

## Restorations confirmed

- Row 6 *m[a]jd*: green traces of two bars on the ring. Supported.
- Row 9 *ne[k]e-*: green traces under the ring, position fits; I cannot see the shape. Correctly disclosed.
- Row 9 end {o}: a loop with an arm. Disclosed, reasonable.
- Row 23 *ad[o]m*: blot where o is expected, followed by three strokes. Supported, and no alternative found.
- Row 24 *a vagyon*: two bars crossed by a water run that continues through neighbouring rows. It is not an r.
- Row 27 *anyi[t]*: stem and start of the top bar of a gamma show at the edge, so slightly better than "stem only".
- Row 28 *szenyen*: signs confirmed. The *sze[ré]nyen* / *szegényen* choice is disclosed.
- Stamp S1 *[is]tenve*: `t e n v e` is clear. *[is]* lies in the space under the stamp fragment and is honestly marked as a restoration from formula. S3–S7 agree with my reading, S5 *ra* faint, S7 *fer* with i lost.

## Could not verify

- The two signs of S1 *[is]*, the final m of S2, *-ja* of S6 and the i of S7, which are hidden or lost.
- The k in row 9 (hidden under the ring; only sense supports it).
- The intended letter within the row 13 correction.
- Whether row 2's heavy sign in *kaptam* and row 7's sign in *sietek* are t by shape; both are disclosed as sense calls and I agree with the words.

## After the fixes

No re-review should be needed if the changes are limited to the above: they correct three or four letters and add no new reading. The register type would be MASC with a key-transfer role. HCP1251 is not listed in `register-exclusions.json`.
