# HCP1314: card to Tóth Jolánka, 20 March 1913 (PARTIAL)

**Status: PARTIAL (revised 2026-11-02, still partial; see the Revision section at the end). No complete decipherment. Not handed to review, no marker, no register entry.** Claude Opus 5.5, 2026-10-30 and 2026-11-02. There is no earlier work on this number; the portal shows Not solved with no attached solution, and no published solution of this card was found.

## Cipher type and key

Hungarian simple monoalphabetic substitution with invented graphic signs: the Jolánka family, same key as finished cards hcp-1216, 1301, 1243, 1217. The key table is in `ciphers/hcp-1216/SOLUTION.md`. It decodes the opening of this card into fluent Hungarian without change.

## What is read

Literal letters, from the pixels of `work/hires/*adr.jpg`. Word division, accents and spellings in the normalized line are editorial. [?] means an unread sign.

```
01 szerettedesjo          (row split: exact t count to be checked)
02 lankambecsessorait
03 megkaptammel[?][?]nagyonko[?]
04 szonok. [struck-out word, unread] ... oru
05 lokhogyijenhuhozam
06 igazanboldoglesz
07 e[k?] ... ferfi a k [?] [?] [?] t fele
08 segenek szol[g?][a?]tni ...
09 csakenlennekaz[?]mi...za.
```

Normalized, firm part: *Szeretett édes Jolánkám! Becses sorait megkaptam, mel[yet] nagyon kö[szö]nök. [...] örülök, hogy ilyen hű hozzám. Igazán boldog leszek ...* then *... feleségének ...* and *csak én lennék az ...*

English: My beloved sweet Jolánka! I received your esteemed lines, for which I thank you very much. [...] I am glad that you are so faithful to me. I will be truly happy ... to his wife ... if only I were the ...

Slovak: Moja milovaná sladká Jolánka! Vaše vzácne riadky som dostal, za čo Vám veľmi ďakujem. [...] Teší ma, že ste mi taká verná. Budem naozaj šťastný ... jeho manželke ... keby som len ja bol ten ...

Isolated words below that, all tentative and not part of a claim: row 11 *les, hogy nem fog*; row 12 *nem baj, már*; row 16 *Jolánkám*; rows 19-20 *mos[t?] valamelyik ... üzenje meg*.

## Uncertain or unread

- Row 3: the two signs after *mel* are unread (smudged); *melyet* is only a context suggestion.
- Row 3 to 4: *köszönök* is read, but the sign before the line break is a blurred mark at the divider.
- Row 4: one word is struck out and unread, and the words after it, before *örülök*, are unread.
- Row 5: *hű*: the double mark on the u is not confirmed; the h/p call in *hű* and *hogy* rests on word sense.
- Rows 7-8: *férfiak*, *szolg-* and the signs around them are not settled. No reading of the sentence is claimed.
- Rows 10, 12-18, 20-22: not read sign by sign (faint pencil, blot in row 10).

## Reproduction

No full-plaintext command exists yet, because there is no complete ledger. Draft: `ciphers/hcp-1314/work/ledger-draft.txt`.

## Why the part read is believed

The transferred key, unchanged, yields continuous idiomatic Hungarian in rows 1-6, with this family's greeting and its writer's spellings (j for ly, single for double consonants).

## Revision 2026-11-02

Second attempt ordered by the human; Claude Opus 5.5. No sign ledger from 2026-10-30 was trusted. New crops: `work/rev2.py` (rotation -1.2 deg, red-weighted channel, flat-field, 1 px blur, gamma), output in `work/rev2/` (block, row strip and tile crops at 2 to 5.5x). Row labels below use the y position in the original scan, because the old row numbers drifted. Hand and key were compared with hcp-1216.

Result: the card does **not** meet the completeness rule. Several new word readings, none closing a whole clause. All items below are tentative letter strings from the pixels, with the word sense stated; they are not a continuous text.

| y (px) | literal signs as read now | suggested words | what the call rests on |
|---|---|---|---|
| ~1065 (old row 11) | l e s h o g y n e m f o g ... | les, hogy nem fog | signs clear up to fog; what follows is unread. The sign before l is not established |
| ~1145 (old row 12) | ... n e m b a j m a r {h/d} o l | nem baj, már dol- | d rather than h rests on word sense only |
| next strip | g o z ? k, then x g y | -goz?k (dolgozik?), úgy | the sign between z and k has no visible dot, so i is a word-sense guess; x g y = úgy is also tentative |
| next strip, right | {n/h} e t e g ... | beteg? not claimed | first sign unclear; b is not seen |
| ~1235 | n e m m e g y | nem megy | signs clear (two-stroke n, three-bar e, three-stroke m) |
| ~1325 | r e t t e m v o l ... | not resolved | old "retten / volna" not confirmed; n a after l is not seen |
| ~1415 | j o l a n k a m | Jolánkám | signs clear, as in row 1. What follows is unread |
| ~1505 | f e l v e {h} e cs ... | fel ve-? | no word claimed |
| ~1595 | a z t i r t a {h} o g y m a j {d/h} z r | azt írta, hogy majd ... | azt írta hogy reads well; majd rests on word sense for the last sign; z r unexplained |
| ~1685 | m o ? v a l a m e j i k ? n a ? t o | ... valamelyik ... | valamejik fits the writer's j for ly; the signs after k give no word. Old "mos[t?]" and "na[p?]" are withdrawn as unproved |
| ~1775 | ü z e n j e m e g ... | üzenje meg | the opening x is read as ü; dots not clear. After it possibly hogy, unconfirmed |
| ~1860 | ... e r r e a z e r t k e r e m e r | ... erre azért kérem, ... | azért kérem is new; the word start of the row (k o s ? ...) is unread, one patch is smudged |

Possible sense of the new pieces only: "... that he will not ... no matter, already ... working(?) ... does not go ... my Jolánka ... wrote that ... some ... let her send word ... therefore I ask ..." Slovak: "... že nebude ... nevadí, už ... pracuje(?) ... nejde ... moja Jolánka ... napísala, že ... nejaký ... nech odkáže ... preto prosím ...". These are fragments, not a translation.

Still unread after this revision:

- Row 3: the two smudged signs after *mel*; row 3 to 4 the blurred sign in *kö[szö]nök*.
- Row 4: the struck-out word (a heavy line through the signs; only isolated strokes show) and the word after it.
- Rows 7-8 around the *fér-* and *feleségének* passage: no sentence, *szol-* unresolved.
- Row 9-10: the blot at about x 1300-1400 hides signs; the passage after *csak én lennék az* does not read (visible a k g i b, no word claimed). No restoration is made, because no single letter gives a word.
- Rows at y 1145-1505: joins between the fragments above, and the ends of the y 1325, 1415 and 1505 rows.
- Rows at y 1685-1950: the ends of rows, the start of y 1860, and the last row. No signature was read; the stamp area and the right edge gave nothing new.

There is still no full-plaintext command, because no complete ledger exists. Draft ledger: `work/ledger-draft.txt` (old); the table above replaces it where they differ.
