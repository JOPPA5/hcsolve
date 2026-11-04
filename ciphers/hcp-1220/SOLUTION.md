# HCP1220 — Feri to Jolánka Tóth: thanks for her letter, going home this afternoon

**Status: complete reading; review 1 verdict ACCEPT, no change to the reading (corrections to labelling and marks only, see the last section).** Written 2026-11-02 by Claude Opus 5.5.

Credit: transcription and decipherment of this card by Claude Opus 5.5, 2026-11-02; there is no earlier work on this number. The key was transferred unchanged from the finished Jolánka cards (HCP1216 with its legend, also 1212, 1213, 1217, 1218, 1243, 1301), solved by the OpenAI GPT solver and completed by Claude Opus 5.5. The portal shows status Not solved and attaches no transcription or solution; the orchestrator's register check (2026-11-02) found no record of this card. The stamp-box note was read with the parallel on sister card HCP1234 in view (see uncertainty 1).

## Cipher type and key

Hungarian (portal language "Unknown" is resolved), simple monoalphabetic substitution with invented graphic signs (the Jolánka postcard family). Sign classes as in HCP1216 and HCP1234; no new letter value was needed:

Type note (2026-11-03): register type is now **MASC + Steganography**, because a message (plain Hungarian, signed feri in cipher signs) is hidden in the stamp box under the lifted stamp.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma/corner | t |
| long stroke + short tick on the LEFT | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright or tilted cross | f | tall stroke + tick on the RIGHT | h / p | low descender | y |
| hook with descender | g | dotted crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | (gy = g + y, sz = s + z, two signs) | | | |

Dots over o/u give ö/ü, not always written; no acute tick is written on any cipher sign of this card. Card-specific form: the s sign is three times written as a closed narrow loop (token `s^`), always at a word edge.

The address and the stamp-box note are in plain Latin script; only the 12 main rows and the name at the foot of the stamp box are ciphered.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1220/work/decode.py
```

It checks the SHA-256 of both source scans and both hires originals, decodes the hand-made sign ledger `work/ledger.txt` (13 rows; 177 written signs: 176 letters and one unassigned mark), prints the literal rows, the plain stamp note and the normalized text. The ledger is a manual transcription (not OCR, not blind: the reader knew the key). `work/unmix.py` separates the purple ink from the blue printed stamp imprint for the stamp box.

## Literal decipherment (spaces editorial; h = h/p sign)

```
01 szeretet edes jolan
02 kam becses sorait
03 megkahtam mely
04 nagyon koszönök
05 igen örülök hogy uj
06 ra olvashhatom
07 sorait d{?}elutan
08 megyek haza most
09 mast nem irhatok
10 mert keves idom
11 van viszontlatas
12 ra hü kedvesse feri
stamp box, plain script: hit remény / és szere- / tet kös- / se [öss]ze / sziv[ün]- / [ket]
stamp box foot, cipher signs: feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Becses sorait megkaptam, mely[et] nagyon köszönök. Igen örülök, hogy újra olvashatom sorait. Délután megyek haza. Most mást nem írhatok, mert kevés időm van. Viszontlátásra! Hű kedvese, Feri.

Under the stamp: Hit, remény és szeretet kösse [öss]ze szív[ünket]. Feri. (Brackets: supplied from the formula on HCP1234; the traces are only compatible.)

Address (plain): Szépreményű Tóth Jolánka úrleánynak, Jász-Árokszállás.

## English

My beloved sweet Jolánka! I have received your dear lines, for which I thank you very much. I am very glad that I can read your lines again. This afternoon I am going home. I cannot write anything else now, because I have little time. Until we meet again! Your faithful sweetheart, Feri.

Under the stamp: May faith, hope and love bind our hearts together. Feri.

Address: To the promising young lady Jolánka Tóth, Jászárokszállás.

## Slovak

Moja milovaná, sladká Jolánka! Vaše milé riadky som dostal, za ktoré veľmi ďakujem. Veľmi sa teším, že môžem znova čítať Vaše riadky. Popoludní idem domov. Teraz nemôžem napísať nič iné, lebo mám málo času. Dovidenia! Váš verný milý, Feri.

Pod známkou: Nech viera, nádej a láska spoja naše srdcia. Feri.

Adresa: Sľubnej slečne Jolánke Tóthovej, Jászárokszállás.

## Stamp-box message (2026-11-03)

Stamp-box audit by Claude Opus 5.5 on the hires original, crops in `work/stamp-2026-11-03/` (`box.png` 2x colour, `box_top*.png` and `box_bot*.png` 3x, `_g` = green channel, where the purple ink is dark and the blue imprint pale). The stamp is lifted; only its green lower strip with `FIL` survives. Under it is writing in **both** modes: six short rows in plain Hungarian script, then the name in the card's cipher signs.

- Literal (brackets = letters supplied from the HCP1234 formula, traces only compatible): `hit remény / és szere- / tet kös- / se [öss]ze / sziv[ün]- / [ket]` + cipher `feri` (literal signs `fari`, see uncertainty 2).
- Normalized Hungarian: Hit, remény és szeretet kösse [öss]ze szív[ünket]. Feri.
- English: May faith, hope and love bind our hearts together. Feri.
- Slovak: Nech viera, nádej a láska spoja naše srdcia. Feri.

My own look agrees with the earlier reading and changes no letter. Read from the pixels: `hit remény`, `és szere-`, `tet kös-`, `se`, `ze`, `sziv`, the n of `-ün-`, the hyphen dot, and the cipher `feri`. Not read from the pixels alone: `öss` in row 4 (arches over the printed wreath), the ü of row 5 (a tall stroke there is the z descender from the row above), and the last row `ket` (a peak and a k-like trace, merged with the strokes of the cipher name). These are supplied from the same writer's formula on HCP1234. Whether ink remains under the surviving `FIL` strip is unknowable. The stamp text is read by eye; `work/decode.py` is unchanged.

## Uncertainties

1. **Stamp-box note, plain script, rows 3 to 6 (the weakest part of the card).** The writing was hidden under the stamp, runs over the blue printed imprint, and the stamp's removal damaged the area above its bottom strip. The green strip with the denomination `FIL` is the surviving lower part of the stamp, and it may still cover ink. Rows 1 to 2 (`hit remény / és szere-`) and `tet` are clear on the ink-separated crop (`work/crops/un_pur.png`), and review 1 found `kös-` legible on its own ink map. The rest was read with the wording of HCP1234 ("kösse össze szívünket") in mind, and I first misread it without that parallel:
   - `kös-`: tall loop, bowl, o, s. I first read `alkos-`, but the "A" beside it is the blue imprint, not ink, and `alkos- / se` makes no word. Dots of ö are not seen. A large ink dot and a wedge stand left of the k with no letter value.
   - `se össze`: s, e are clear; the z and e are clear; the middle (`öss`) is a run of arches over the wreath and is compatible with, not independently legible as, those letters.
   - `szivün-`: s, z, i are clear; `v`, `ü`, `n` are heavily inked and overlapped; dots of ü are not seen. The tall stroke that looks like a d in this row is the descender of the z of the row above. The thick mark at the end is a hyphen, as in rows 2 and 3, so the word runs on.
   - `[ket]`: the last row starts with a peak-shaped letter, a small speck and a letter compatible with a cursive t, which merges with the heavy strokes above it. None of the three is firm; they are read by the word.
   Taken alone, rows 4 to 6 would not fix the wording; the supplied letters are in brackets in the literal block and the Hungarian text. The stamp note sits outside the ciphertext claim, and its meaning repeats a formula of the same correspondent.
2. **Row 13 `feri`** (foot of the stamp box): a thick diagonal cross, two bars, F-like, and a dotted sign damaged at the edge. The cross has the shape of u; it is read f as the name (compare the tilted f of HCP1216 item 5), and the middle sign shows two bars where e has three, so the signs taken literally give `fari` (ledger token `e!`). e signs with a nearly lost third bar occur elsewhere on this card (row 2 `becses`). The name is a word-sense call, not a clean sign match.
3. **Row 7 `d{?}elutan`**: between d and e stands a small, raised, heavily blotted x-shaped mark, smaller than the letters. It has no value in `délután`; I treat it as a blotted false start or possibly a spoiled acute, and drop it. No other word results if it is read u or f. The e itself has three plain bars and no tick.
4. **Row 11 blot**: the sign after `viszon` is a black blot with F-like arms (r shape). It is read t by the word `viszontlátás`, probably overwritten. Restoration by word sense.
5. **Row 12 first f** is a blotted star; read f as the cross sign by the name. **Row 5 first i** is a heavy blot with its dot visible. **Row 5 ü of `örülök`** is a heavy star-shaped overwrite with a thin earlier arc to its left; the dots and the hooked arm still give ü.
6. **Row 6 `olvashhatom`**: two complete h/p signs are written; normalized `olvashatom` (dittography). 
7. **Row 3 `megkahtam`**: h/p sign read p by the word `megkaptam`. Other h/p signs (`hogy`, `haza`, `irhatok`, `hü`, `olvas-hatom`) are read h by the word.
8. **Word-sense calls on d/n and spelling:** the d of `edes`, `kedvesse`, `idom`, `delutan` has its tick on the left and is distinct from n here. Writer's spellings normalized: `szeretet` → szeretett, `mely` → melyet (bracketed, grammar repair), `koszönök` → köszönök (the first ö has no dots on the card), `uj` → új, `idom` → időm (no double mark seen on the o), `kedvesse` → kedvese (doubled s, two signs clearly written), `hü` → hű. Long vowels of the cipher rows are unmarked and their accents are supplied (`edes`, `delutan`, `keves`, `irhatok` and others).
9. **Closed s:** three signs (row 1 first and before `jolan`, row 2 end of `becses`) are closed loops like o rather than the open bowl used elsewhere on the card. o would give no word in any of the three places (`ozeretet`, `edeo`, `becseo`). This is a call by word sense.
10. **Date:** the receiving cancel at the top, turned round, shows `DEC` and `27`, which agrees with the -12-27 in the portal filename: 27 December, year unread. The second cancel is not read beyond isolated characters.
11. The pencil line along the top edge ("Jász Árokszállás Hungary") is a later note in another hand, not part of the message. The picture side (a hussar and a girl) has only the printed number 2541 and a small publisher's mark, no writing.

## Why it is correct

- The family key, unchanged, turns all 176 letter signs into continuous Hungarian with no free choice beyond the listed points. Long words read straight from the signs include `örülök`, `olvashatom` (after the doubled h), `délután` (accent supplied) and `kedvese`. `megkaptam` needs the h/p call (uncertainty 7), `viszontlátásra` needs the restored t (uncertainty 4), and `köszönök` lacks the dots on its first vowel.
- The opening `szeretet édes Jolánkám`, closing `viszontlátásra ... kedvese Feri` and the recipient match the family; the cipher addressee `Jolán-kám` agrees with the plain address `Tóth Jolánka`.
- The message is coherent and ordinary: thanks, gladness, going home, no time.
- Dots fall only on vowels that are ö, ü or ű in the words (`örülök`, `köszönök` twice, `hű`), without being used in the reading.

## Response to review 1

Verdict ACCEPT. I rechecked each pixel claim on the review crops or new crops of the hires scan. No letter value of the reading changed.

1. **Row 7 acute: fixed.** `review/work/blot7.png` shows three plain bars and no tick. The ledger now has `e`, the literal row prints `delutan`, the "Why it is correct" list is corrected, and uncertainty 3 offers the spoiled acute. **The same error was in row 10, which the review did not list:** on `work/crops/r10_kevesz.png` the second e of `keves` also has three plain bars and no tick, so I removed that acute too. The dot below the first e belongs to the i of row 11. No cipher sign on this card now carries an acute, and the key note says so.
2. **Row 13 second sign: fixed.** Now `e!` in the ledger; `work/crops/stamp_strip.png` shows two bars. The printed value stays e, and uncertainty 2 gives the literal `fari`.
3. **Sister-guided stamp wording: fixed.** `work/plain-note.txt`, `work/normalized.txt` and this file now print `se [öss]ze`, `sziv[ün]-`, `[ket]`. I bracketed slightly more than the review's example: `öss`, because my own uncertainty 1 calls it only compatible, and the t of the last row, because I withdraw "the t is clear" and the crop shows it merged with the strokes above.
4. **Row 5 overwrite: fixed.** Added to uncertainty 5; `review/work/blot5.png` confirms the overwrite, and the dots and hooked arm still give ü.
5. **"Why it is correct": fixed.** Reworded; the h/p call, the restored t and the undotted vowel are now stated, and the accent bullet is limited to dots.
6. **Date: fixed.** `review/work/pm_110.png` shows `DEC` and `27`. Uncertainty 10 now says 27 December, year unread.
7. **Bottom of the stamp box: fixed.** `work/crops/stamp_strip.png` shows the green strip with `FIL`; uncertainty 1 says it is the surviving part of the stamp and may cover ink.

The count "177 signs decoded" is also corrected: 176 letters and one unassigned mark, as the review noted. `work/decode.py` now reports both numbers.
