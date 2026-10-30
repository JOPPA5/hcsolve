# HCP1308 — Feri to Jolánka Tóth: a rival given up, leave planned for next month

**Status: complete reading; review 1 (REVISE) addressed, one clause and six signs corrected. Solved and written 2026-10-30 by Claude Opus 5.5.** There is no earlier work on this number. The portal shows *Not solved* and attaches no transcription or solution. The orchestrator's register check (2026-10-30) found no record. No published solution was seen. The key comes from the repo's finished Jolánka cards (below); the transcription was made from this card's pixels, by hand, and was not blind to the expected Hungarian.

## Cipher type and key

Hungarian, simple monoalphabetic substitution with invented graphic signs: the "Jolánka" postcard family, same key as HCP1216, 1212, 1213, 1217, 1218, 1243, 1301 (sister cards' solutions were read; none of their text was copied). The card is enciphered without word division.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S-shape (close to the next) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (once) | three strokes | m | gamma/corner | t |
| long stroke + short tick | d (longer) / h, p (shorter) | two equal strokes | n | plain cross x | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | loop with dot | i | looped descender | y |
| reversed-s shape | g | inverted T | j | crossed diagonal | z |
| opposed bowls | cs | | | | |

*gy* is written here as g + y. Dots or a double mark over the loop or the cross give ö/ő, ü/ű. Acute accents are small ticks; they were not transcribed and are supplied in the normalization.

Layout: 26 long rows (the last three run across the whole width under the address), then up the right edge (bottom to top), then right to left along the top edge, and a separate 7-row block in the stamp field (the stamp is gone). The stamp block is written slanted.

## Reproduction (one command, from the repository root)

```sh
python3 -I ciphers/hcp-1308/work/decode.py
```

It checks the SHA-256 of both source images and both originals in `work/hires/`, decodes `work/ledger.txt` (one token per written sign, 627 signs), and prints the literal rows and `work/normalized.txt`. The ledger is a manual transcription, not OCR.

## Literal decipherment (as printed; {x} = value chosen by word sense)

```
01 szeretetedesjolankam            15 lathassamszepszemeit
02 becsessoraitmegkaptam           16 ajövöhonapabanmajd
03 mejertfogadjaköszö              17 e{n}yhebleszefor{g}alom
04 netemetedesemköszö              18 esakormajd{k}erevagyket
05 nömhogyfelha{g}yezekel          19 napszabadsagotesle
06 avetejtarsakkaltudom            20 megyekmertmegarok    
07 edesemhogymagaszeret            21 szal{a}sbaislatniaka
08 engemese{g}{y}szeretösziv       22 romegyszerlega
09 csakegygondolmindig             23 labesugy{i}sakar{e}rok
10 higyjeedesemazeletem            24 szüleimhez{i}shazameniestudjaaztmagaisede
11 tölkönyebbeneltudnek            25 semhogyhamagaeljönarokszalabolnemn{a}gyonme
12 valnimintmagatolede             26 gyekaraakörnyekcsakhamuszajezelbezarom
13 semaligvaromaztaper             27 soraimmaradokszere        (up the right edge)
14 c{z}zethogy{g}yakrabban         28 kedves{f}eri              (top edge, right to left)

Stamp field: {ü}dvoz{l}öm / tavobol / csokjaiert / va{g}yosi / righü / imadoja / feri
```

## Hungarian (normalized)

Szeretett édes Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetemet. Édesem, köszönöm, hogy felhagy ezekkel a vetélytársakkal. Tudom, édesem, hogy maga szeret engem, és egy szerető szív csak egy[re] gondol mindig. Higgye, édesem, az életemtől könnyebben el tudnék válni, mint magától, édesem. Alig várom azt a percet, hogy gyakrabban láthassam szép szemeit. A jövő hónapában majd enyhébb lesz e forgalom, és akkor majd kére[k] vagy két nap szabadságot és lemegyek, mert meg Árokszállásba is látni akarom egyszer legalább, és úgyis akarok szüleimhez is hazamenni. És tudja azt maga is, édesem, hogy ha maga eljön Árokszállásból, nem nagyon megyek arra a környék[re], csak ha muszáj. Ezzel bezárom soraim, maradok szere[tő], kedves Feri.

Stamp field: Üdvözlöm távolból. Csókjaiért vagyo[k] sírig hű imádója, Feri.

## English

My beloved sweet Jolánka! I have received your esteemed lines, for which please accept my thanks. My darling, I thank you for giving up these rivals of mine. I know, my darling, that you love me, and a loving heart thinks always of one person only. Believe me, my darling, I could part from my life more easily than from you, my darling. I can hardly wait for the moment when I may see your beautiful eyes more often. Next month this traffic will ease, and then I shall ask for about two days' leave and come down, because I want to see you at Árokszállás too, at least once, and in any case I want to go home to my parents as well. And you know yourself, my darling, that if you leave Árokszállás, I shall hardly go to that area unless I must. With this I close my lines; I remain your loving, dear Feri.

Stamp field: I greet you from afar. For your kisses I am your adorer, faithful unto the grave, Feri.

## Slovak

Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku. Drahá moja, ďakujem Vám, že ste nechali týchto sokov. Viem, drahá, že ma ľúbite, a milujúce srdce myslí stále len na jedného. Verte mi, drahá, ľahšie by som sa rozlúčil so životom než s Vami, drahá. Sotva sa dočkám chvíle, keď budem môcť častejšie vidieť Vaše krásne oči. Budúci mesiac sa táto premávka zmierni a vtedy si vypýtam asi dva dni voľna a prídem dolu, lebo Vás chcem aspoň raz vidieť aj v Árokszállási, a tak či tak chcem ísť domov aj k rodičom. A aj Vy sama viete, drahá, že ak odídete z Árokszállásu, do toho kraja veľmi nepôjdem, iba ak budem musieť. Týmto končím svoje riadky, zostávam Váš milujúci, milý Feri.

Pole známky: Pozdravujem Vás z diaľky. Za Vaše bozky som Váš ctiteľ verný až do hrobu, Feri.

## Uncertainties

Nothing is left without a value, but these points rest on word sense or are editorial:

**Signs not settled by the shape alone**

1. **g/k (the S and reversed-s shapes) are near-homographs on this card.** Word sense decides row 14 *gyakrabban* (S-like sign read g), row 17 *forgalom* (S-like read g), row 18 *kére* (a closed, 8-like form read k, the least clean of these). Row 20 *meg arok* is not among them: there the two forms stand a few signs apart and differ clearly.
2. **Rows 5 and 8, overwritten signs.** The g of *felhagy* (row 5) and the g, y of *egy* (row 8) are heavily re-inked. In row 8 the two blots show a descender shape and a looped sign but cannot be read alone; *egy* is a contextual reading.
3. **Row 14**, start: left bowl, then a heavily worked sign (a right bowl overwritten with a crossed z?), then a clear z, e, t. Normalized *percet* (old spelling *perczet*); the writer's correction is not fully clear. The preceding *per* (row 13) uses the tall+short sign read p by sense.
4. **Row 17, *enyhébb***: the sign after e is two heavy joined strokes with a bar (H-like), read n as re-inked strokes. The whole of *enyhébb lesz e forgalom* ("this traffic will ease") is my reading of the word sense. It suggests the writer worked in a transport or postal service, but the card does not say so.
5. **Row 21, *arokszalasba***: the vowel after *szal* is two bars with a blot; three bars (e) is not fully excluded by this sign alone. The same place in row 25 has two clear bars, so a is the reading.
6. **Row 23, *akar{e}rok***: between *akar* and *rok* stands a bar sign under a stain, bar count uncertain. Treated as a false start, normalized *akarok*. The loop of *úgyis* and the loop of *is* in row 24 show no dot; i by sense.
7. **Row 25, *nagyon***: the bar sign lies under the "OF" of the collector's stamp; read a by sense.
8. **Top edge, f of *Feri***: the sign is smeared and looks like a tilted cross with a closed top; f by sense (z gives no word). The whole top row is faint.
9. **Stamp row 1**: the first sign is under a blot with dots above it. **Its ü is a restoration** (only the dots survive; *üdvözlöm* is the only word found). The sixth sign is a closed loop read as a cramped l, also by sense. The final letters are tiny.
10. **Stamp row 4, *vagyo***: the g and y lie in a stain and are faint. Stamp row 5 and 7 are clear. The end of stamp row 6 (*-ja*) is a small tilted inverted T and two small bars.

**Editorial readings of what the writer wrote**

11. **Rows 20–21, *meg Árokszállásba*:** the signs read *megarok·szalasba* without any emendation (corrected after review 1; the earlier *meg a[ka]rom* is withdrawn). *meg* may be the conjunction or the verbal prefix of *látni*; the meaning hardly changes. The illative *-ba* with *látni* is the writer's form, where standard Hungarian would have *Árokszálláson*.
12. *(Withdrawn after review 1: the "Szállás / lodging" alternative falls away, since rows 20–21 spell the full town name.)*
13. **Row 25, *Árokszállásból*:** literally *arokszalabol*: only the s of *-ás-* is dropped. Rows 21 and 25 agree on the vowel. The name is written with one l in both, as is usual in this hand.
14. **Row 27–28, *maradok szere kedves Feri*:** the word stops at *szere* round the corner. *szere[tő]* is an editorial completion; *kedves[e]* ("your dear one") is possible.
15. **Omissions restored in brackets:** *egy[re]* (row 9), *kére[k]* (row 18), *környék[re]* (row 26), *vagyo[k]* (stamp). Final letters are dropped often enough in this hand that I treat them as the writer's slips.
16. **Other spellings normalized:** *szeretet* → szeretett, *mejért* → melyért, *ezekel* → ezekkel, *vetéjtárs-* → vetélytárs-, *higyje* → higgye, *könyebben* → könnyebben, *enyhebb* written with one b, *lab* → (lega)lább, *hazameni* → hazamenni, *ara* → arra, *ezel* → ezzel, *távobol* → távolból. *hónapában* (signs P A 6 A N, all clear) is kept as the writer's form, "in the month of"; standard *hónapban* is the alternative normalization and the meaning is the same. *Ó* of *hónap* is written over another sign (an inverted T).
17. **h/p and d share a stroke + tick design**, as in the family; the long/short difference decided d, and sense decided h vs p (*per*, *megkaptam*, *szép*, *nap*, *hónap*).
18. **Row 2:** the two s of *becses sorait* are written tight together and the second is slightly deformed.

**Not cipher**

19. Handwritten in plain script across the cancellation, left of the Rákospalota box, is a pen note beginning *Sze…*, partly under the box. I did not read it to the end; it is not enciphered and is not part of the message. The large U-shaped ink mark to the right of the stamp field is also not enciphered, and the right-edge rows pass under it. The round postmark shows only *JÁS…* at the top, which fits the destination town; its date is not legible, so the card is undated.
20. Plain address: Tóth Jolánka úrleánynak, Jász-Árokszállás. Boxed mark RÁKOSPALOTA. Printed picture-side verse, not cipher.

## Why I believe it is correct

- The same key taken from finished sister cards turns all 627 signs into continuous Hungarian with no unassigned sign, on a card without word division.
- The letter is consistent over its whole length, including words read independently at distant positions: *édesem* five times, *hogy* four times, *köszön-* twice, *akar-* twice, and *Feri* twice.
- Details fit the family: the addressee, the Rákospalota mark, Feri as signer (also HCP1216), the closing formula *sírig hű* (HCP1216), and the form of address (*maga*, *higgye*).
- Árokszállás, the addressee's town, appears twice in the text, spelled out in rows 20–21 and again in row 25, in sentences that need it. Neither place was forced: the first was found by reading the signs after a wrong segmentation had been corrected in review.

The honest limits are the points above, chiefly rows 8 and 17. They affect single words, not the content of the letter.

## Response to review 1

Verdict REVISE. I rechecked each point on the reviewer's enlargements (`review/work/c20.png`, `z20.png`, `a06.png`, `a14.png`, `a16.png`, `a25.png`, `z25.png`, `a26.png`) and on the row crops `L2`–`L5` in the context of the rows above and below. All five findings are accepted.

1. **Fixed (major).** `c20.png` shows, after *me*: reversed-s (g), two bars, F, loop, S (k). The earlier `K~` was wrong and the final sign is a plain k, so rows 20–21 read *mert meg·arok·szalasba·is·latni·akarom*. Ledger row 20 is now `M E G A F O K`, with no sense choice. The emendation *meg a[ka]rom* is gone, the "Szállás / lodging" discussion is withdrawn, and the normalization, English and Slovak now have Árokszállás. This was my own misreading. It was also hidden by my "weakest word" note, which treated it as a difficulty in the text.
2. **Fixed (major).** All five signs have exactly two strokes.
   - Row 6: `A`, *vetejtarsakkal*.
   - Row 14: `A`, *gyakrabban*. The third bar that seems to stand above it in `a14.png` belongs to the e at the end of row 13, as `L3.png` shows.
   - Row 16: `A`, *majd*.
   - Row 25: `A`, *arokszalabol*.
   - Row 26: `A`, *muszaj*.
   Uncertainties 5, 13 and 16 are corrected. *gyakrabben*, *mejd* and *muszej* were my misreadings, not the writer's spellings.
3. **Fixed (minor).** Row 20 is dropped from the g/k homograph list in uncertainty 1.
4. **Fixed (minor).** *hónapában* is kept as the writer's form in the normalization, with *hónapban* named as the alternative. The translation is unchanged.
5. **Fixed (minor).** Uncertainty 13 now says only the s is dropped, and "Why I believe it is correct" cites both rows 20–21 and row 25.

The sign count stays at 627, since the changes replace signs without adding or removing any. After the fixes `python3 -I ciphers/hcp-1308/work/decode.py` passes all four hash checks and prints the literal block and normalization given above. `review/work/own_decode.py` then reports only the three rows it had already explained as artefacts of its own handling of `X:d` (24, S1, S5). The reviewer's "could not verify" items remain open: the plain pen note, the date of the card, and a native speaker's judgement on the regional forms.
