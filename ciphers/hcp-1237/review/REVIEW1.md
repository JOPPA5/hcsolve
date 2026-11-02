ACCEPT

# Review 1 of HCP1237 (Claude Opus 5.5, reviewer, 2026-11-02)

The reading stands. I tried to break it on the pixels and did not succeed. Only minor disclosure and notation points remain. They can be fixed in the response without a new review round.

## What I verified and how

1. **Command.** `python3 -I ciphers/hcp-1237/work/decode.py` from the repo root. All four SHA-256 checks passed, and the output matches the literal rows and the normalized text in SOLUTION.md.
2. **Independent transcription.** `review/work/my_signs.txt` is my own transcription of all 28 rows, in shape symbols rather than letters. I read it from my own crops of the hires address side (`review/work/crops.py`, `zoom.py`: L*.png at 2x, z*.png at 3-4x, stamp.png at 3x). It was not blind, because I knew the claimed text.
3. **Independent decoder.** `review/work/indep_decode.py` applies the HCP1216 key to my transcription and compares with `work/ledger.txt`. There are 435 signs. The only differences are rows 06, 09, 10 and 14, where I keep the one sign as h and the solver takes p by sense (pedig, lapokat, panasza, kapom). Those four are the disclosed h/p calls, and all give the only possible word. Every sign has a key value except the disclosed S5 blot, and no value is adapted to this card.
4. **Normalization diff.** The same script aligns the literal text with `work/normalized.txt`. Apart from finding 2, every edit is disclosed in Uncertainties 1, 2, 3 and 11.
5. **Key.** Compared with the HCP1216 table and ledger: same classes. The stroke order of d (short then long) against h/p (long then short) holds on this card wherever I checked it (kedves, edesem, erdekli, harmadikat, ido, kedvesse against hogy, higgye, lehet, het, hu).
6. **Sign-level checks on the zooms:**
   - Row 18 *a gyász*: z18.png shows two bars before and after the gy, with no third bar, and a joined s + z. Clean.
   - Row 10 *panasza*: z10.png shows p, a, n, a (squeezed but two bars), s, z. Clean.
   - Row 12 *harmadikat*: z12.png shows three strokes, two bars, short + long, crossed curve. Clean.
   - Row 7 *mozdu*: three separate strokes, so *hoz* is excluded. The final X is over-inked over a pale underlayer and crossed by the postmark (z7.png). u rests on the word, as disclosed.
   - Row 15 `T N`: z15.png shows two slanted strokes under the gamma's arm. They are n in shape, not a bars. The solver's description is exact, and the word stays an emendation.
   - Row 11 *j*, row 14 *k*, row 19 *gy*, row 20 *z*: the blots are as described. In each case the sign shape remaining is compatible and the sense decides, as disclosed.
   - Row 22 *marado*: the d carries extra barbs on the long stroke (z22a.png), but no extra letter is visible. The k of *maradok* and the g of *sírig* are really absent.
   - Stamp rows: *üdvöz|löm a|távol|ból hű|kedve* are clear (stamp.png). The last sign is one blotted X-like mass, as disclosed.
7. **Whole card.** The text runs from the left block through the bottom line to *feri* and the stamp box, and no row is left over. The picture side has only the printed poem "Fecském hova szállsz?" and no handwriting, as claimed.
8. **Language.** The text is continuous, natural period Hungarian in the formal *maga* register and fits the Feri to Jolánka correspondence: *sírig hű kedvese, Feri*, and *higgyje el* with the same j as HCP1216 row 5. The word count of unclear items is two: *[a]kkor* and the end of S5. Each is an isolated word, and the rest of the clause reads, so the card counts as complete under the run's rule. English and Slovak translations match the Hungarian.

## Findings

1. **minor: visible accents missing from the ledger.** The ledger header says `:m` marks a visible accent, but three clear marks are unrecorded:
   - two marks over the o of `osze` (row 15; z14.png, upper right, above the o);
   - two dots over the o of `jon` (row 16);
   - a tick over the e of `es` (row 16; z15.png, lower left).
   These support the reading, and the first is direct evidence for *ö* in *összejön*. Uncertainty 3 argues only from the o form. Add the marks and cite them.
2. **minor: one normalization not listed.** Row 4 has literal `eset`, normalized *esett*. It is missing from the writer's-spellings list in Uncertainty 11.
3. **minor: notation of `[a]kkor`.** The normalized form brackets only the a, but the n to k change is also an editorial correction. Uncertainty 2 discloses it. A form such as `[a]‹n›kor` or a note in the plaintext would show it where the reader sees the word.
4. **minor: "Over the stamp" is not established.** No stamp remains over these rows. Only a torn remnant stays at the top of the box, and the rows lie below it inside the area it would have covered. The rows were more probably under the stamp, as on HCP1216, or simply in the stamp box. "In the stamp area" is safe wording. The translations and the literal block should use it too.

## What I could not verify

- The date: the postmarks are not legible to me either, so 1912-06-30 rests on the portal file name, as disclosed.
- Whether the article cited on the portal (HistoCrypt) contains a solution of this card: I did not read it. The portal attaches none.
- Whose mourning is meant, and the exact words of Jolánka's letter behind *nem érdekli*: the card does not say. The solver marks both as inferred.
