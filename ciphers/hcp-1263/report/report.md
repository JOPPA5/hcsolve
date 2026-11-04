# HCP 1263 (cpc_1913--_HU__HU_Jasz Arokszalas_jolanka-109): "we are not going to Berény", Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (357 signs, 2 of them restored from word sense); independent review 1 verdict ACCEPT; no decoded letter changed in review, one normalized word did.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1263 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1263), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Tóth Jolánka, with no transcription or solution attached. The year 1913 comes from the file name; the Budapest postmark shows "913".

The picture side is a tinted commercial card, series number 3747/48. A young man sits writing by a lamp, a woman's portrait floats behind him, and the card carries a printed Hungarian poem headed *Sokszor úgy szeretnék sírni...* ("So often I would like to cry..."). Someone has added a red mark on the woman's hair.

The address side reads in plain writing *Szépremény[ű] Tóth Jolánka úrleánynak, Jász-Árokszállás* ("To Miss Jolánka Tóth", in Jászárokszállás, Hungary; the first word is only partly clear). The cipher fills the left half in 21 rows and continues in 7 small rows inside a pink-ruled box at the stamp position, with green stamp remnants at its edge. The box holds the closing and the signature.

![Address side: 21 cipher rows at the left, 7 more rows in the stamp box, the plain address at the right (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, as scanned sideways (source/picture-large.jpg)](../source/picture-large.jpg)

The card belongs to the family of cipher postcards addressed to Jolánka Tóth, signed Feri and all using one key. This card was read with a **known, transferred key** from finished cards in this repository (HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). It is not a new key recovery. No published reading of this card was found or used; the AI Decipherment Register had no record of it on 2026-11-01.

## Method

The transcription is **manual**. The solver cut 2.5× to 5× crops of the high-resolution original scan and read every sign in order into a ledger (`work/ledger.txt`), one token per written sign. No OCR was used. The family key then turned the ledger into text with no change and no leftover sign.

Several first readings were corrected on enlargement, always by rereading shapes, never by altering the key. The chevron with a cross through it is a second form of z (*bízom*, *számta-*, *lanszor*). The plain chevron is v, which gave *várva várt*. In row 8 the sign after the h shape has three bars, so it is *De* and not *Ha*.

In review a second agent cut its own crops, read all 28 rows in its own shape names and decoded them with its own script (`review/work/indep_decode.py`). Of 28 rows, 25 were identical; the three differences are the word-sense calls listed under Uncertainties.

## Key

**Cipher type: MASC + Steganography** (updated 2026-11-03). The closing and signature are hidden in cipher in the stamp box, under the stamp, which has since been lifted.

Monoalphabetic substitution with invented graphic signs. The names below are conventional labels for the handwritten shapes.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | S-shape or closed 8-form | k | F-like | r |
| six | b | wave | l | right bowl | s |
| opposed bowls | cs | three short strokes | m | gamma | t |
| long + short stroke ("4") | d | two short strokes | n | plain cross x | u |
| three bars | e | cursive loop, closed or open | o | chevron | v |
| upright or tilted cross | f | tall stroke + short | h / p | low looped descender | y |
| open loop with descender | g | dotted crossed curve | i | crossed diagonal or chevron-crossed form | z |
| inverted T | j | | | | |

Dots over o and u give ö and ü. Gy is written as two signs (g + y). Acutes are marked only sometimes. Numerals stay in clear in this family. The signs for d, p and h are near-homographs: on this card d and p both have the tick on the left, and h has it on the right.

## Plaintext

Literal decipherment, row by row. `[a]` marks a rubbed sign restored from the word.

```text
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

Normalized Hungarian (word division, accents, punctuation and the repair of the writer's slips are editorial):

**Szeretett édes egyetlen reményem! Várva várt sorait megkaptam, melyet köszönök. Sajnálatomat fejezem ki, hogy nem megyünk Berénybe. De önre bízom a dolgot. Majd küldök Ilonkának egyet ebből a fényképemmel ellátott levelezőlapból, és megírom, hogy magának nincs kedve most lemenni. Édesem, egyenlőre még nem megy le, de vagy 3 hét múlva lemegyek. Majd holnap bővebben írok, mert ma sürgős dolgom van.**

**Stamp box: Isten vele, édesem! Csókolom számtalanszor. Feri**

English translation: **My beloved sweet only hope! I have received your long-awaited lines, for which I thank you. I express my regret that we are not going to Berény. But I leave the matter to you. I will send Ilonka one of these postcards bearing my photograph, and I will write that you do not feel like going down now. My darling, for the time being [he/she] is not going down yet, but in about 3 weeks I will go down. Tomorrow I will write in more detail, because today I have urgent business.**

**Stamp box: God be with you, my darling! I kiss you countless times. Feri**

Slovak translation: **Moja milovaná, sladká, jediná nádej! Vaše dlho očakávané riadky som dostal, za čo ďakujem. Vyjadrujem poľutovanie, že nejdeme do Berénya. Ale nechávam tú vec na Vás. Pošlem Ilonke jednu z týchto pohľadníc s mojou fotografiou a napíšem, že sa Vám teraz nechce ísť dolu. Drahá moja, zatiaľ ešte nejde dolu, ale asi o 3 týždne pôjdem dolu ja. Zajtra napíšem podrobnejšie, lebo dnes mám súrne povinnosti.**

**V rámčeku na známku: S Bohom, moja drahá! Bozkávam Vás nespočetnekrát. Feri**

The formal address (*sorait, önre, magának*) and the closing *Isten vele ... Csókolom számtalanszor* are this family's usual phrases, and *egyetlen reményem* also opens HCP 1216.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1263/work/decode.py
```

The script uses only the Python standard library and writes no files. It checks the SHA-256 hashes of the four scans, decodes the manual ledger `work/ledger.txt`, prints the 21 main rows and 7 stamp rows and prints `work/normalized.txt`. It does not read the image; the transcription step is manual and was checked independently in review.

## Uncertainties

Signs restored because they are physically obscured:

- **Row 19, *holn[a]p*:** rubbed and blotted with a pink halo; two or three bars cannot be told apart. *Holnap* needs a.
- **Row 21, *v[a]n*:** a clean top bar and then three close strokes, so the sign looks retraced or overwritten. a comes from sense.

Calls that rest on word sense, not on shape alone:

- **Row 17, the digit 3.** A flat-topped sign read as a numeral in clear; in shape it stands near the s sign, but *s hét* gives no sense. This is the weakest point of the card. Another small number is not fully excluded, and the sentence survives either way.
- **d versus p.** Both have the tick on the left, so the word decides (*édes, majd, kedve, dolgot* against *kaptam, képem, lap, holnap*).
- **Row 8, *De*.** Shape h, so literally *he*; HCP 1216 writes the d of *de* the same way, and *he* is no word. The next sign has three bars, which excludes *ha*.
- **Stamp row 6, *lanszor*.** The last sign has no crossbar, a gamma by shape, so literally *lanszot*. *Számtalanszor* fixes r.
- **Stamp row 5, *számta*.** The fifth sign looks as much like r as t.
- **Stamp row 7, *Feri*.** The first sign looks like the plain x, u by shape, so literally *ueri*. The f rests on the family signature, and the i shows no dot.

Editorial repairs of the writer's slips (each sign is transcribed as written):

- **Row 1** *szereret* for *szeretett*, with a doubled *re* and one t.
- **Row 6** *refezem*, normalized to *fejezem*. The signs are clear, the literal form is no word, and *sajnálatomat fejezem ki* is a stock phrase. This is an interpretation of a misspelling.
- *sajnaltomat* → sajnálatomat; *ebölafeny|kepemelelatot* → ebből a fényképemmel ellátott; *mot* → most; *bovebbe* → bővebben; *dogom* → dolgom. *Egyenlőre* is kept as a common variant of *egyelőre*.

Writer's corrections on the card: in row 7 the ü of *megyünk* is a dark x with two dots over a pale e, and the following n lies over a pale sign closest to the closed k. The writer possibly first wrote *megyek* ("I am going") and changed it to "we are going". The e is seen; the k is only likely. In row 16 the m of the second *megy* has a deformed middle stroke.

Open points of content:

- **Berény** is read clearly and is probably Jászberény, near the addressee's town, but the card says only Berény.
- The subject of *nem megy le* (row 16) is not stated. The verb may be formal "you" or a third person.
- *Ilonka* is not identified. The sentence break around row 9 (*... a dolgot. Majd küldök*) is editorial.
- The man on the picture side is probably a stock model. It is unknown whether the "postcard bearing my photograph" is this one.
- Day and month of the postmarks are not read, and the left postmark is unread.
- The HistoCrypt paper linked on the portal was not read for a reading of this card.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer ran the reproduction command, made its own crops and transcription, decoded them with its own script, checked coverage and all restorations on the pixels, and tried and rejected fuller readings *most* (row 14) and *dolgom* (row 21) as written. It found no wrong word in the literal reading. Its six findings were minor, and all were accepted:

- ***bővebben* for *bővebbet*.** The writer's own phrase on HCP 1252, 1255, 1266 and 1294. The normalized text and both translations changed; the literal text did not.
- **Stamp row 6.** The last sign is now disclosed as a word-sense call. Checking the same crop also led to restating *Feri* as one.
- **Row 7 undertext.** Now given as a possible *megyek* changed to *megyünk*.
- **Row 21.** The sign is described as retraced, not as a blot.
- **Photograph.** The argument from the picture side was dropped.
- **Slovak grammar.** *jednu z týchto pohľadníc* corrected.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1263, General, Description and Attachments tabs, captured 2026-11-01: https://crypto.hcportal.eu/dashboard/cryptograms/1263 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3849/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_pic.jpg and https://api.hcportal.eu/media/3850/cpc_1913--_HU__HU_Jasz-Arokszalas_jolanka-109_adr.jpg, with their large conversions (see SOURCES.md).
- Family key: ciphers/hcp-1216 and the other Jolánka cards in this repository, earlier work by the OpenAI GPT solver and Claude Opus 5.5.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-01.
