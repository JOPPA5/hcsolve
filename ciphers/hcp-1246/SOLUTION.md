# HCP1246 — Feri to Jolánka Tóth: gossip, Pest visit, a better suit

**Status: complete; the whole card reads. One verb form (`jöm`, row 23) stays ambiguous between two senses and one phrase (*állású r[u]hát*, row 25) is an interpretation. Review 1 (REVISE) addressed below.** Claude Opus 5.5, 2026-11-01. No earlier work exists on this number. The portal shows *Not solved* with no transcription or solution; no published solution was found. The key is transferred from the finished family cards (HCP1216 and siblings); the transcription and reading of this card are new. The ledger was read knowing the family's hand and vocabulary, so it is not blind.

Card: picture postcard no. 3244, printed verse "Oh csak még egyszer összejönnénk"; addressed in clear to Tóth Jolánka, Jász-Árokszállás; postmark 1913 September (portal name: `cpc_1913-09-`). Only the two ciphertext blocks below are enciphered; the printed verse and address are not.

## Cipher type and key

*Type note (2026-11-03): register type changed to MASC + Steganography, because part of the message (7 cipher rows) is written in the stamp box, under the now-lifted stamp.*

Hungarian, simple monoalphabetic substitution with invented graphic signs, the Jolánka family key (HCP1216, 1212, 1213, 1217, 1218, 1243, 1301), unchanged. Every sign class is used with its family value; no new sign was needed.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | section mark | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c | three short strokes | m | gamma/corner | t |
| long stroke + tick | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | tall stroke + tick | h / p | low descender | y |
| open hooked loop | g | crossed curve | i | crossed diagonal with tail | z |
| inverted T | j | | | | |

Digraphs are written as letter pairs on this card (`gy` = g+y, `sz` = s+z, `cs` = c+s); dots over o/u give ö/ü. ly is written j (`mijen`, `ijesmit`, `gujas`), as in *ojan* on HCP1216.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1246/work/decode.py
```

It checks the SHA-256 of the two source scans and the two originals in `work/hires/`, decodes the manual sign ledger `work/ledger.txt` (28 rows, 1 row up the right edge, 7 rows in the stamp box), and prints the normalized text `work/normalized.txt`.

## Literal decipherment (h = the h/p sign)

```
01 imadotedesegyetlenreme        15 megysemireakormajdfelhagy
02 nyembecsesleveveletmeg        16 veleenmarnemtartomerdemes
03 kahtammitköszönökszehen       17 nekf[o]glalkoznivele.edesem
04 edesemazertnemharagszom       18 örömemfejezemkihogy
05 agujasrahogyaztbeszelte       19 felfogjönnihestreaztnem
06 mocsarnenekmerttudomhogy      20 iskeligernemhogyfelkere
07 mijenamoczarnehogykonnyen     21 semazelsöalkalommal
08 lehetugratniamoczarnet        22 megfogomlatogatniir
09 esörülhaijesmithaldereme      23 jamegmikorjömenagaelötnincs
10 lemjolankamedesazijenbesze    24 semimititkomakorraakarok
11 deknemzavarjakboldogsagunkat  25 jobbalasurhatvennimerttu
12 esnemhiszelijesmittanacso     26 domhogyarokonsagjobbanmegneziazembertedesemazt
13 lomhogycsakegeszhidegenvisel  27 nekelmondanommaganakhogymegegylahjatsemolvas
14 kedjenelötteeshalatjhogynem   28 taavatatlakezcsakenistenveleedesemaboldogvi
                                 29 szontlatasra (up the right edge)
stamp box: hükedves / seferi / csokol / jaszam / talan / szor / feri
```

## Hungarian (normalized; [..] = letters not on the card; {..} = literal form kept, sense uncertain)

Imádott édes egyetlen reményem! Becses levelét megkaptam, mit köszönök szépen. Édesem, azért nem haragszom a Gulyásra, hogy azt beszélte Mocsárnénak, mert tudom, hogy milyen a Mocsárné, hogy könnyen lehet ugratni a Mocsárnét, és örül, ha ilyesmit hall. De remélem, Jolánkám édes, az ilyen beszédek nem zavarják boldogságunkat, és nem hisz el ilyesmit. Tanácsolom, hogy csak egész hidegen viselkedjen előtte, és ha látja, hogy nem megy semmire, akkor majd felhagy vele. Én már nem tartom érdemesnek foglalkozni vele. Édesem, örömem fejezem ki, hogy fel fog jönni Pestre. Azt nem is kell ígérnem, hogy felkeresem az első alkalommal, meg fogom látogatni. Írja meg, mikor {jöm}. Én [m]aga előtt nincs semmi titkom. Akkorra akarok jobb állású r[u]hát venni, mert tudom, hogy a rokonság jobban megnézi az embert. Édesem, azt ne[m] kell mondanom magának, hogy még egy lapját sem olvasta avatatla[n] kéz, csak én. Isten vele, édesem, a boldog viszontlátásra.

Stamp box: Hű kedvese Feri. Csókolja számtalanszor Feri.

## English

My adored, sweet, only hope! I received your esteemed letter, for which I thank you kindly. Darling, I am not angry with Gulyás for having told that to Mrs Mocsár, because I know what Mrs Mocsár is like, that she is easily teased, and she is glad when she hears such things. But I hope, my sweet Jolánka, such talk does not disturb our happiness, and that you do not believe such things. I advise you to behave quite coolly in front of her, and when she sees she gets nowhere, she will give it up. I no longer think it worth bothering with her. Darling, I express my joy that you will come up to Pest. I need not even promise that I will look you up at the first opportunity, I will visit you. Write when {you are coming / I should come}. I have no secrets from you. By then I want to buy a better suit (literally *jobb állású ruha*, "better-fitting"? reading uncertain), because I know the relatives look a person over more closely. Darling, I need not tell you that not one of your cards has been read by an uninitiated hand, only by me. God be with you, darling, until a happy meeting again.
Stamp box: Your faithful sweetheart Feri. Feri kisses you countless times.

## Slovak

Moja zbožňovaná, sladká, jediná nádej! Váš vzácny list som dostal, za čo pekne ďakujem. Drahá, nehnevám sa na Gulyása, že to povedal Mocsárovej, lebo viem, aká je Mocsárová, že sa dá ľahko doberať a teší sa, keď počuje niečo také. Ale dúfam, moja sladká Jolánka, že také reči nenarušia naše šťastie a že niečomu takému neveríte. Radím Vám, aby ste sa pred ňou správali celkom chladne, a keď uvidí, že ničoho nedosiahne, tak s tým prestane. Ja už nepovažujem za hodné zaoberať sa ňou. Drahá, vyjadrujem radosť, že prídete hore do Pešti. Ani Vám nemusím sľubovať, že Vás pri prvej príležitosti vyhľadám, navštívim Vás. Napíšte, kedy {prídete / mám prísť}. Pred Vami nemám nijaké tajomstvá. Dovtedy si chcem kúpiť lepší oblek (doslova azda „lepšie padnúci“, čítanie neisté), lebo viem, že príbuzní si človeka lepšie obzrú. Drahá, nemusím Vám hovoriť, že ani jeden Váš lístok nečítala nepovolaná ruka, iba ja. S Bohom, drahá, do šťastného zvidenia.
V poli na známku: Váš verný milý Feri. Bozkáva Vás nespočetnekrát Feri.

## Uncertainties

1. **Row 28 `avatatla kez`** = *avatatla[n] kéz* ("uninitiated hand"), a set phrase, found in review. The fifth sign of the row is cut by the card's lower edge: two strokes are visible, so a is possible, and only the phrase settles it (a third stroke off the card cannot be excluded). The n of *avatatlan* is not on the card: section mark k follows a directly. *kéz* has its accent tick over the three bars. "Cards" assumes *lap* = postcard; it could mean "page".
2. **Row 25 `alasurhat`**, normalized *állású r[u]hát*, is an interpretation: the signs a l a s u r h a t are clear, the u of *ruhát* is taken as omitted, and "better-fitting" is my reading of *jobb állású*, which no sister card or period dictionary confirms. The context (relatives will look him over) fits clothes. Alternatives not excluded.
3. **Row 23 `jömenagaelöt`**: after jö stand two very heavily over-inked strokes and one light one, and the following e is over-inked too: this spot was reworked, so the stroke count (read as m) is less firm than elsewhere. The literal `jöm` is kept in the normalized text as *{jöm}*: it could be *jön* ("when you are coming", she being the one who comes to Pest) or a slip for *jöjjek* ("when I should come"); nothing on the card gives -jjek. *én [m]aga előtt* is taken as a broken construction (= *nekem maga előtt*, "I, before you, have no secrets"); the m of *maga* is not on the card.
4. **Row 5 `gujasra`** = *Gulyásra*: taken as a surname; the common noun "herdsman" is possible. Mocsárné is spelled two ways, `mocsar-` (row 6) and `mocz ar-` (rows 7, 8). The m of *Moczárnét* in row 8 is blotted but its three strokes are visible.
5. **Row 17 `f[o]g`**: the sign after f is under an ink blot; o is a **restoration** (*foglalkozni*, the only letter making a word).
6. **Row 20 first sign**: blotted crossed curve, i, from shape and *is*. **Row 27** the a of *lapját* has two visible bars under the portal stamp, a third cannot be excluded (é would be the writer's form). **Row 7** *könnyen*: no dots seen.
7. **Right edge (row 29)**: read after rotating; `sz` is faint and crossed by the address flourish, and a large right-angled stroke at the corner is read as a flourish of the address or a false start and given no value. `viszontlátásra` starts at the end of row 28.
8. **Writer's spellings normalized**: *imadot* → imádott, *levevelet* → levelét (dittography), *mocsarnenek* → Mocsárnénak, *halatj* → ha látja (a omitted), *hal* → hall, *hiszel* → hisz el, *semire* → semmire, *akor* → akkor, *felfog jönni*, *kel igernem* → kell ígérnem, *felkere-sem* across rows 20-21 = felkeresem, *semimi* → semmi (repeat), *akorra* → akkorra, *nekel* → ne[m] kell (m omitted), *ijesmit* → ilyesmit, *hükedves|se* (s doubled across rows S1-S2) → kedvese. After review 1 I re-read the three-stroke groups of *semire* (row 15) and the row of *semimi* (row 24) on 2-6x crops, and *levevelet* (row 2) and *halatj* (row 14): these spellings stand as written. Accents are mostly faint and are supplied. The h/p call rests on word sense throughout (*kaptam, szépen, Pestre, lapját* = p; *hogy, haragszom* = h). d in *hal de* (row 9) and *érdemes* is a heavy d with its tick.
9. Reading order of the stamp box is taken top to bottom; *Feri* occurs twice there (rows S2, S7).

## Why it is correct

- The family key, unchanged, turns all 28 rows, the edge row and the stamp box into Hungarian with no unused sign and no unread word group.
- The text is coherent connected prose over 29 rows, with the family's formal address, its closing formulas and signature Feri (as on HCP1216), and its ly→j habit.
- Repeated words decode alike at distant places: *hogy* ×9, *édesem* ×4, *Moczárné/Mocsárné* ×3, *ijesmit* ×2, *mert tudom* ×2, *nem* ×7.
- No published solution was used.

## Response to review 1

Verdict REVISE. All eight findings are accepted; the key and the reading stand. I checked each on my own crops of `work/hires/*_adr.jpg` (autocontrast, 2-6x), not only the reviewer's.

1. **Row 28 *avatatla[n] kéz*: fixed.** My crop of the row start shows t a | a v, then the sign cut by the edge with two strokes visible, then t a t l a k. Ledger sign 5 is now A, marked as resting partly on the phrase. All translations, Uncertainty 1 and the status line are rewritten. The split `-k ez` is dropped. The card now counts as complete.
2. **Row 14 *előtte* dropped: fixed.** The crop confirms k e d j e n e l ö t t e e s. Restored in the Hungarian, English and Slovak.
3. **Row 27 `mondanom`: fixed.** On `review/work/z27.jpg` the sign after d a n is an undotted loop with no cross, O; the dot below it belongs to row 28. Ledger corrected. The "superfluous m" note is gone, and *nekel* is now *ne[m] kell*.
4. **Row 12 `tanacsolom`: fixed.** `review/work/z12.jpg` shows two bars under the gamma's arm; ledger E → A. Removed from the spelling list. As the reviewer asked, I re-read the other doubtful items in the list (*semire*, *semimi*, *levevelet*, *halatj*): each is written as listed, and no further ledger change results.
5. **Row 23 `jöm`: fixed.** Now shown as *{jöm}* in the normalized text with both senses in the translations; Uncertainty 3 is rewritten, including the over-inking.
6. **Normalization: fixed.** *felkeresem* with one s; *hükedves|se* and *mocsarnenek* are now listed.
7. **Slovak: fixed.** *do šťastného zvidenia*, *na Gulyása*.
8. **Row 25: kept as a caveat.** I have no better reading; the English and Slovak now mark it as uncertain, and Uncertainty 2 says that nothing confirms the sense.

`python3 -I ciphers/hcp-1246/work/decode.py` was re-run after the fixes: all 4 hash checks are OK and the literal rows match the block above.

## Stamp-box message (2026-11-03)

Stamp-box audit (Claude Opus 5.5, 2026-11-03). The stamp has been lifted; the box (dotted frame, top right of the address side) holds 7 short rows in the same green ink and the same cipher signs, no plain Hungarian. Checked on new red-channel crops at 3x of `work/hires/*_adr.jpg` (`work/stamp-2026-11-03/`). Every sign agrees with ledger rows S1-S7, which `work/decode.py` already covers; the script was re-run today unchanged and passes. Nothing new had to be read and nothing in the box is unread.

- Literal: `hükedves / seferi / csokol / jaszam / talan / szor / feri`
- Hungarian: Hű kedvese Feri. Csókolja számtalanszor Feri.
- English: Your faithful sweetheart Feri. Feri kisses you countless times.
- Slovak: Váš verný milý Feri. Bozkáva Vás nespočetnekrát Feri.

Because writing was hidden under the stamp, the card is typed **MASC + Steganography** (register entry changed today; the key and the reading are unchanged).
