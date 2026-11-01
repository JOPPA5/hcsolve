# HCP1263 — Feri to Jolánka Tóth: "we are not going to Berény"

**Status: complete reading; review 1 verdict ACCEPT, six minor findings addressed (see the end).** Claude Opus 5.5, 2026-11-01. There is no earlier work on this number. The portal shows status *Not solved* and attaches no transcription or solution. No published solution of this card was found or used. The orchestrator's AI-register check (2026-11-01) found no record of it.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs (MASC), the Jolánka postcard family. The key is transferred unchanged from `ciphers/hcp-1216/SOLUTION.md` (also HCP1212, 1213, 1217, 1218, 1243, 1301):

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S-shape / closed 8-form | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| long + short stroke ("4") | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop, closed or open | o | chevron | v |
| upright or tilted cross | f | tall stroke + short | h / p | low looped descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal, or chevron-crossed form | z |
| inverted T | j | | | | |

Dots over o/u give ö/ü. Gy is written here as two signs (g + y). Acutes are marked only sometimes and are not carried in the literal text. Numerals stay in clear in this family (HCP1218, 1276, 1284).

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1263/work/decode.py
```

It checks the SHA-256 of the four scans, decodes `work/ledger.txt` (one token per written sign, 21 main rows plus 7 rows in the stamp box) and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription from enlarged crops of the high-resolution scan. It is not OCR.

## Literal decipherment

```
01 szereretedesegyet        12 lezölapbolesmeg
02 lenremenyemvarva         13 iromhogymaganak
03 vartsoraitmeg            14 nincskedvemotle
04 kaptammelyetkö           15 menniedesemegyen
05 szönöksajnalto           16 loremegnemmegy
06 matrefezemkihogy         17 ledevagy3het
07 nemmegyünkbereny         18 mulvalemegyek
08 bedeönrebizomadol        19 majdholn[a]pboveb
09 gotmajdküldökilon        20 beirokmertma
10 kanakegyetebölafeny      21 sürgosdogomv[a]n
11 kepemelelatotleve
stamp box: istenve | leede | semcso | kolom | szamta | lanszor | feri
```

## Hungarian (normalized)

Szeretett édes egyetlen reményem! Várva várt sorait megkaptam, melyet köszönök. Sajnálatomat fejezem ki, hogy nem megyünk Berénybe. De önre bízom a dolgot. Majd küldök Ilonkának egyet ebből a fényképemmel ellátott levelezőlapból, és megírom, hogy magának nincs kedve most lemenni. Édesem, egyenlőre még nem megy le, de vagy 3 hét múlva lemegyek. Majd holnap bővebben írok, mert ma sürgős dolgom van.

Stamp box: Isten vele, édesem! Csókolom számtalanszor. Feri

## English

My beloved sweet only hope! I have received your long-awaited lines, for which I thank you. I express my regret that we are not going to Berény. But I leave the matter to you. I will send Ilonka one of these postcards bearing my photograph, and I will write that you do not feel like going down now. My darling, for the time being [he/she] is not going down yet, but in about 3 weeks I will go down. Tomorrow I will write in more detail, because today I have urgent business.

Stamp box: God be with you, my darling! I kiss you countless times. Feri

## Slovak

Moja milovaná, sladká, jediná nádej! Vaše dlho očakávané riadky som dostal, za čo ďakujem. Vyjadrujem poľutovanie, že nejdeme do Berénya. Ale nechávam tú vec na Vás. Pošlem Ilonke jednu z týchto pohľadníc s mojou fotografiou a napíšem, že sa Vám teraz nechce ísť dolu. Drahá moja, zatiaľ ešte nejde dolu, ale asi o 3 týždne pôjdem dolu ja. Zajtra napíšem podrobnejšie, lebo dnes mám súrne povinnosti.

V rámčeku na známku: S Bohom, moja drahá! Bozkávam Vás nespočetnekrát. Feri

## Uncertainties

Restorations (signs physically obscured):

1. **Row 19 *holnap*:** the a is rubbed and blotted (pink halo, heavy lower stroke), so two or three bars cannot be told apart. *Holnap* needs a; *holnep* is no word.
2. **Row 21 *van*:** not a blot like row 19: there is no pink halo, but a clean top bar followed by three close strokes, so the sign looks retraced or overwritten. a is taken from sense; *vn* is no word. The final n is two thin, ink-starved strokes, still clearly two.

Calls resting on word sense:

3. **Row 17, the sign before *hét*:** a flat-topped bowl with a foot, read as the **digit 3** in clear. In shape it is close to the s sign, but *s hét* gives no sense here. The next sign has a small foot and a right tick, read as h, then é (acute visible) and t. *Vagy 3 hét múlva* ("in about 3 weeks") is my reading; the number itself is the weakest point of the card, and the sentence survives if it is wrong.
4. **Short + long stroke signs:** on this card d and p are both written with the tick on the left (*édes*, *majd*, *kedve*, *dolgot*; *kaptam*, *képem*, *lap*, *holnap*), so d versus p rests on the word. The tick on the right is h (*hogy*, *hét*, *holnap*), with one exception:
5. **Row 8 *De*:** the sign has the tick on the right, the h shape, as the family's d of *de* does on HCP1216. *He* is no word. The next sign has three short strokes, so e, not a; *ha önre* ("if ... you") is therefore excluded by the pixels.
6. **Row 4/5 *köszönök*:** the first k is the closed 8-form of the k sign; *köszönök* requires it.
7. **Stamp box row 5, *számta*:** the fifth sign looks as much like r (F) as t, because of the crowded bars that follow. *Számtalanszor* fixes t. **Row 6 *lanszor*:** the last sign has no crossbar, a gamma by shape, so literally *lanszot*; *számtalanszor* fixes r (ledger token R:g). **Row 7 *Feri*:** the first sign looks like the plain x (u by shape, so literally *ueri*); f rests on the family signature Feri (HCP1216 row 21) and is a word-sense call (ledger token F:x). The i touches the stamp remnant with no dot visible. **Row 1 *isten*:** no dot visible on the i.
8. **Berény** is read clearly (b e r é n y + -be). It is probably Jászberény, near the addressee's Jászárokszállás, but the card says only Berény.
9. **Subject of *nem megy le* (row 16):** the verb is third person. It may be formal "you" or a third person, who is not named. The translation leaves this open. *Ilonka* is not identified.
10. **Sentence division around row 9:** *De önre bízom a dolgot majd* or *... a dolgot. Majd küldök* are both possible; the sense barely changes.

Writer's corrections and spellings (each sign is transcribed as written, normalization is editorial):

11. **Row 7 *megyünk*:** the ü is a dark x with two dots written over a pale e, and the first stroke of n lies over a cancelled pale sign with an upper and a lower bowl, closest to the closed 8-form of k (row 4). The writer possibly first wrote *megyek* ("I am going") and changed it to *megyünk* ("we are going"). The change of e to ü is seen; the k is only likely.
12. **Row 16:** the middle stroke of m in the second *megy* is deformed into a K-like form (a correction or pen slip).
13. **Row 1:** *szereret* is written, with a doubled *re* and one t for *szeretett*. The second F is clear.
14. **Row 6 *refezem*:** the signs are clear (r e f e z e m). I normalize to *fejezem*, taking *re* as a false start and j as omitted. *Sajnálatomat fejezem ki* is a stock phrase and the literal form is not a word. This is an interpretation of a misspelling.
15. Other normalizations: *sajnaltomat* → sajnálatomat (a omitted), *ebölafeny|kepemelelatot* → ebből a fényképemmel ellátott (b, m, l, t dropped), *mot* → most (s omitted), *bovebbe* → bővebben (n omitted; the second bar group of row 20 is three bars with the lower two joined by a pen drag, and no sign for n stands there; the writer's phrase is *bővebben* on HCP1252, 1255, 1266 and 1294, and no family card has *bővebbet*), *dogom* → dolgom (l omitted; the first o is the open form also seen in *szö-*, row 5), *egyenlőre* kept (a common variant of *egyelőre*). Accents and many ö dots are not visible and are supplied.

Unenciphered parts: the address reads *Szépremény[ű] Tóth Jolánka úrleánynak, Jász-Árokszállás* (first word only partly clear). The picture side has only the printed poem *Sokszor úgy szeretnék sírni...* and a red mark on the woman's hair. The Budapest postmark shows "913"; day and month are not read, and the left postmark is unread. 1913 otherwise comes from the file name.

## Why it is correct

- The family key, not fitted to this card, turns every sign of 21 rows and the stamp box into connected Hungarian. No letter was left without a value.
- Words decode the same at separate places (*hogy* ×2, *megy-* ×3, *édesem* ×2, *majd* ×2, *le-* ×3), and the rows run on across line breaks (*kö|szönök*, *dol|got*, *Ilon|kának*, *fény|képemmel*, *leve|lezőlapból*, *le|menni*, *egyen|lőre*, *bőveb|be*).
- The phrases are the family's: formal address (*sorait, önre, magának*), *Isten vele*, *Csókolom számtalanszor*, signature Feri. *Egyetlen reményem* also appears on HCP1216.
- The content was not expected and is self-consistent, and Berény fits the addressee's region. The words *fényképemmel ellátott* stand on the signs alone. The picture side is a numbered commercial series (3747/48) with a printed poem, so the man shown is probably a stock model and gives no support; whether it shows Feri is unknown.

## Credits

Key from the finished family cards (earlier work by the OpenAI GPT solver and Claude Opus 5.5, see those directories). Transcription and decipherment of this card by Claude Opus 5.5.

## Response to review 1

Verdict ACCEPT. I checked each finding on the reviewer's crops. All six are accepted and fixed. No decoded literal letter changed.

1. *bővebbet* → *bővebben*: fixed. Six family SOLUTION files have *bővebben* (HCP1252, 1255, 1266, 1294, 1297, 1309) and none has *bővebbet*. Changed in `work/normalized.txt`, the Hungarian text, item 15 and both translations. Literal *boveb|be* is unchanged. The omitted letter is now n, not t.
2. Last sign of stamp row 6: confirmed on `review/work/crops/z_s57.png`: a curved top and no crossbar. Added to item 7 as a word-sense call. The ledger now records it as token R:g, which still decodes to r. The same crop shows the first sign of stamp row 7 as a plain x, so that call is restated too (token F:x, literally *ueri*).
3. Row 7 undertext: confirmed on `z_r7.png`: pale upper and lower bowls under the dark stroke. Item 11 now gives *megyek* changed to *megyünk* as likely, not certain.
4. Row 21: confirmed on `z_r21b.png`: no halo, a top bar and three close strokes. Item 2 corrected.
5. Photograph argument: dropped; the picture side now counts as no evidence.
6. Slovak: *jednu z týchto pohľadníc* fixed. I also changed *napíšem viac* to *napíšem podrobnejšie* to match *bővebben*.

I also noted the unread left postmark, which the reviewer listed under "could not verify". The reproduction command was re-run after these changes: all four hash checks are OK, and the literal rows are unchanged.
