# HCP 1151 (cpc_1916-05-13_HU_Mezokovesd_HU_Szomolya_szomolya-35): a Hungarian love letter from Árpád to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered in full (574 cipher signs, 120 words; 569 signs by the table and 5 by word sense); independent review 1 verdict REVISE, all findings addressed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1151 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1151), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). Neither solver nor reviewer read it, so we cannot say whether it discusses this card.

It is a picture postcard with a view of a waterfall. The picture side has no writing. On the message side only the place and date, **Mezőkövesd, 1916. V/13**, and the address are in clear: **Őnagysága / Sziber Margitka / Kisasszonynak / Szomolya / (u. p. Bogács.) / (Borsod m.)**. Everything else is a block of digits with small marks in red ink. The green printed "Impart" and "1386" belong to the publisher and are not cipher. The postmark cannot be read on the scan, so the date rests on the written one.

The card belongs to the Mezőkövesd series (hcp-1135 to 1179), sent to Margitka Sziber in the village of Szomolya in 1915 and 1916. Earlier cards of the series gave a digit-plus-mark alphabet, on hcp-1174 (fullest table), 1178 and 1179. This card had no earlier work in this repository. The whole of it was done by Claude Opus 5.5.

![Message side with the digit cipher (source/address-large.jpg)](../source/address-large.jpg)

![Picture side: waterfall view, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The solver transcribed all rows by hand from enlarged crops of the un-converted scan, with no OCR. It started from the key of hcp-1174. The opening "Édes Margitkám" confirmed that key at once. The remaining signs came from context: `6` = j (hónapja), `4` = f (fel, fogom), and the dotted signs `4.` gy (hogy), `5.` ly (melynek), `6.` ny (lányka), `8.` ty (kártyát). Mistaken first readings were corrected on the enlargements, for example meghányamtam to meghányattam after a second comma was seen under an 8.

The cipher has no word divisions; the divisions below are editorial. The reviewer read every row again on the scan and decoded the signs with its own script, ignoring the solver's word list.

## Key

Monoalphabetic substitution (register label MASC). Each letter is one digit with an optional mark. The key does not separate o/ó, ö/ő, i/í or ü/ű. The writer always crosses his 7.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `3` | d | `6` | j |
| `0,` | ö, ő | `3,` | r | `6,` | n |
| `1` | i, í | `3.` | v | `6.` | ny |
| `1.` | a | `4` | f | `7` | k |
| `1:` | e | `4,` | g | `7,` | s |
| `1'` (high dot) | á | `4.` | gy | `7.` | sz |
| `1,` | b | `5` | h | `8` | m |
| `:1` | ü, ű | `5,` | l | `8,` | t |
| `2,` | cs | `5.` | ly | `8.` | ty |
| `2.` | é | `9` | p | `9,` | z |

On this card a dot on the base of a single letter gives its digraph (g/gy, l/ly, n/ny, t/ty, s/sz). This is not family-wide: hcp-1178 and 1179 file `5.` as plain l, and hcp-1179 files `8.` as "t?". Here all 30 `5,` signs are l and the two `5.` stand exactly at the ly of melynek and fogoly, while `8.` occurs once. This evidence is thin. If `5.` were plain l, the text would only be spelled melnek, fogol, with the same words.

## Plaintext

Ciphertext as transcribed, row by row. Row H is the heading; | is an editorial word division; = and - at a row end are the writer's hyphen; ~x marks a sign read by word sense.

```text
H 2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
01 5~l 1. 9 0 3 1. 8, | 8 1: 4, 7 1. 9 8, 1. 8 | 8 1: 5. 6, 1: 7 | 1 4, 1. 9, 1' 6, | 8 1: 4, 0, 3, :1 5, =
02 8, 1: 8 | 5 1 7. | 5 0 4. | 6, 1: | 8 1 7 0 3, | 8 1' 3, | 1: 4. | 5 0 6, 1. 9 6 1. | 5 0 4. | 6, 1: 8
03 7 1. 9 8, 1. 8 | 8, 0, 5, 5, 1: 3 | 8 0 7, 8, | 9 1: 3 1 4, | 2. 3, 8, 1: 7, 1 8, 5, 1: 7 | 5 0 4.
04 2, 1. 7 | 1. | 6 0, 3. 0, | 5 0 6, 1. 9 | 0, 8, 0, 3 1 7 2. 6, | 7, 0 3, 0 9, 6, 1. 7 | 5 0 5, 6, 1. 9
05 6, 1: 8 | 8 1: 4. 1: 7 | 4 1: 5, | 8 1: 3, 8, | 8 0 7, 8, | 4 0 4, 0 8 | 5, 1: 3. 1: 8, 1: 8, 6, 1 | 8 1. 4, 1. =
06 8 1. 8, | 8, 0 3,~v 1' 1, 1,~b 1' | 2. 3, 8, 1: 7, 1 8, 5, 1: 7 | 5 0 4.
07 8 1: 4, 5 1' 6. 1. 8, 8, 1. 8 | 1. | 7 1' 3, 8. 1' 8, | 6 0 5,
08 1, 1: 7. 2. 5, 8, | 8 1: 4, 8 0 6, 3 8, 1. | 1. 7. 8, | 1 7, | 5 0 4.
09 3. 1. 5, 1. 7 1 | 7 0, 9, :1 5, :1 6, 7 | 4 0 4, 0 5. | 2. 7,
10 6, 1. 4. 0 6, | 6 0 | 3 0 5, 4, 1. | 3. 1. 6, | 6, 1 6, 2, | 7, 1: 8 1
11 1, 1. 6 1. | 9 2. 6, 9, 1: | 3. 1. 6, | 1: 5, 2. 4, | 2. 7, | 7 1. 9 8, -
12 1 7, | 8 1: 4, 8 0 6, 3 8, 1. | 5 0 4. | 6, 1: 8 | 7, 0 7 1'
13 7 1. 9 0 7 | 8, 0, 5, 1: | 5 1 3, 8, | 2. | 1 4, 1. 9, | 1 7,
14 5, 1: 8, | 8 1: 3, 8, | 2. 9 1: 6, | 8 1. | 7 1. 9 8, 1. 8
15 8, 0, 5, 1: | 7 2. 8, | 5, 1. 9 0 8, | 1: 4. 1 7 1: 8,
16 1. 9 1' 8 6, 1. 7 | 1 3, 6 1. | 8 1' 7, 1 7 1. 8,
17 8 1: 4, | 1: 4, 2. 7. | 2, 1. 5, 1' 3 6, 1. 7 | 1 3, 6 1.
18 5 0 4. | 1: 4, 2. 7. 7, 2. 4, 1: 7, | 7. 1 1, 2. 3, 1 1' =
19 1, 1. | 3. 1. 6,
20 5 1: 4. 1: 6, | :1 5, 0, 7 | 3. 0, 5, 4. 1, 1: | 6, 2. 9, 1: 7
21 1: 5, 5, 1' 8, 0 7 | 1. | 8 1: 7, 7. 1: 7, 2. 4, 1, 1:
22 0 8,~t 8,~t | 5, 1. 7 1 7 | 1: 4. | 7. 0, 7 1: | 5, 1' 6. 7 1.
23 1: 9, | 2. 6, | 5, 1: 5, 7 1: 8 | :1 3 3. 0, 7, 7, 2. 4, 1:
24 7, 0 7 7. 0 3,
25 0, 5, 1: 5, | 2. 7,
26 2, 0 7 0 5, | 7. 1: 3, 1: 8, 0,
27 5 :1 | 7 1: 3 3. 1: 7, 1: 3 | 1' 3, 9 1' 3
```

Hungarian text, spelled as on the card. Word division and commas are editorial.

Mezőkövesd, 1916. V/13.

Édes Margitkám!

Lapodat megkaptam, melynek igazán megörültem, hisz hogy ne, mikor már egy hónapja hogy nem kaptam tőlled. (Most pedig értesítlek, hogy csak a jövő hónap ötödikén soroznak.) Holnap nem megyek fel, mert most fogom levetetni magamat. Továbbá értesítlek, hogy meghányattam a kártyát, jól beszélt: megmondta aszt is, hogy valaki közülünk fogoly és nagyon jó dolga van, nincs semi baja, pénze van elég és kapt is. Megmondta, hogy nem soká kapok tőle hírt, é igaz is let, mert épen ma kaptam tőle két lapot, egyiket apámnak írja, másikat meg egész családnak, írja hogy egészséges, Szibériába van.

Hegyen ülök, völgybe nézek,
ellátok a messzeségbe,
ott lakik egy szőke lányka,
ez én lelkem üdvössége.

Sokszor ölel és csókol szerető hű kedvesed Árpád

Normal forms of the writer's spellings: tőlled = tőled, aszt = azt, semi = semmi, kapt = kap, é = és, let = lett, Szibériába van = Szibériában van.

**English translation**

Sweet Margitka! I received your card and was truly glad of it, and why would I not be, when it has been a month now since I had one from you. (And now I inform you that they will conscript only on the fifth of next month.) Tomorrow I am not going up, because I am about to have my photograph taken. Further, I inform you that I had the cards thrown for me, and they spoke well: they also told that one of us is a prisoner and is doing very well, nothing is wrong with him, he has enough money and also gets some. They told that I would soon have news from him, and that came true too, for just today I got two cards from him, one written to my father, the other to the whole family; he writes that he is healthy and is in Siberia.

I sit on a hill, I look into the valley, / I see far into the distance; / there lives a blonde girl, / this is the salvation of my soul.

Many times your loving, faithful sweetheart Árpád embraces and kisses you.

**Slovak translation**

Moja sladká Margitka! Dostal som tvoj lístok a naozaj som sa mu potešil, ako by aj nie, keď už mesiac nič neprišlo od teba. (A teraz ti oznamujem, že odvod bude až piateho budúceho mesiaca.) Zajtra hore neprídem, lebo sa práve idem dať odfotografovať. Ďalej ti oznamujem, že som si dal vyložiť karty a povedali dobre: povedali aj to, že jeden z nás je v zajatí a má sa veľmi dobre, nič mu nechýba, peňazí má dosť a aj dostáva. Povedali, že čoskoro dostanem od neho správu, a aj sa to splnilo, lebo práve dnes som od neho dostal dva lístky, jeden píše môjmu otcovi, druhý celej rodine; píše, že je zdravý a je na Sibíri.

Sedím na vrchu, hľadím do doliny, / vidím do diaľky; / tam býva plavovlasé dievčatko, / to je spása mojej duše.

Mnohokrát ťa objíma a bozkáva tvoj milujúci, verný milý Árpád.

## Reproduction

From the repository root: `python3 -I ciphers/hcp-1151/work/decode.py`. It checks the hashes of the scans, decodes every sign of work/transcription.txt with the table, stops on any disagreement with the stated reading, and prints the counts and the full text.

## Uncertainties

No word or clause is unread. Five signs are read by word sense:

- **Lapodat:** the first sign is a bare `5` (h), and the key would give "hapodat". It is the only l of the card with no mark.
- **továbbá (two signs):** the mark after the 3 is a short comma, so the table gives r, and v is taken by sense. The sixth sign is retouched and lies between `1,` and `5,`; b is taken by sense. This is the weakest word of the card, although "Further, I inform you" fits well.
- **ott (two signs):** heavy ink; the shapes look like 8 with commas, and the line needs t.

Other points:

- **kapt is:** the card has a hyphen after the t at the row end, literally "kapt-" / "is". Whether he means "gets" or "got" money is open; the letters are clear.
- **é igaz is let:** the first sign is clearly `2.`, with no s, taken as a slip for "és".
- **ez én lelkem:** the division is editorial. "ezén" would need a wrong long vowel.
- **Writer's marks that are not signs:** the exclamation mark after the heading, the curved brackets around the conscription sentence, a tall slash in row 18, a lone closing bracket before Árpád, and two small strokes under the `1:` of levetetni. A pale uncrossed 7-shaped stroke after Árpád is taken as a flourish; this cannot be proved.
- **Reading order:** the dashed frame around the signature is read last. Reading across would spoil the verse, though the letters stay the same.
- **Interpretation:** "meghányattam a kártyát" as having one's fortune told by cards, and "soroznak" as conscription, are linguistically sound and fit the context, but have no outside confirmation. The card does not say who the prisoner is.

## Review summary

A separate Claude Opus 5.5 agent reviewed the solution. It ran the command, wrote its own decoder, read every row on the scan at up to 6x, and judged the language and translations. It confirmed the reading and returned verdict **REVISE** with seven findings. All were accepted, and the message did not change:

1. and 2. "ellatok" and "soka" carry a high dot, not a foot dot, so the card has the correct ellátok and soká. The false spelling errors were removed.
3. The first 7 of szőke does have its dot, merged with the crossbar, so this sign moved from "by sense" to "as read".
4. The mark in továbbá is a comma in shape, so it is now counted as read by sense. The total stays 5.
5. The conflict of `5.` and `8.` with the filed readings of hcp-1178 and 1179 was not disclosed. It is now, and a loose signature claim was corrected.
6. "ezén" was redivided as "ez én", and both translations were adjusted.
7. The writer's hyphen, brackets, exclamation mark and slash are now recorded.

The reviewer could not verify the postmark, and neither agent read the HistoCrypt article.

## Sources

- Portal record: https://crypto.hcportal.eu/dashboard/cryptograms/1151
- Sister cards in this repository: ciphers/hcp-1174, hcp-1178, hcp-1179
- Scans and hashes: ciphers/hcp-1151/SOURCES.md
