# HCP 1308 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-80): Feri to Jolánka Tóth

Human solver: Tomáš Pavuk

**Status: deciphered in full (627 of 627 written signs; a few signs rest on word sense and are listed below); independent review 1 verdict REVISE, findings addressed.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1308 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1308), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-80, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, date and language unknown, recipient Tóth Jolánka, with no transcription or solution attached. A check of the AI Decipherment Register on the same day found no record for it, and no published solution was seen.

The picture side is a tinted studio photograph of a couple with a bouquet, with the printed caption Édes párom szállj velem… ("My sweet partner, fly with me…") and a printed four-line verse. It carries no cipher.

The whole message is on the address side, written in invented signs without word division:

- 26 long rows, of which the last three run across the full width of the card under the address;
- one row up the right edge, read bottom to top;
- one row along the top edge, read right to left;
- seven short slanted rows in the stamp field (the stamp itself is gone).

The plain address reads Tóth Jolánka úrleánynak, Jász-Árokszállás ("to Miss Jolánka Tóth, Jász-Árokszállás"). The card carries a boxed RÁKOSPALOTA mark, as do its sister cards, and a round postmark of which only JÁS… can be made out. The date is not legible, so the card is undated.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side with the cipher text, the boxed Rákospalota mark and the stamp field (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to the "Jolánka" family: cipher postcards to Jolánka Tóth in the same system, among them HCP 1212, 1213, 1216, 1217, 1218, 1243 and 1301, already deciphered in this repository. HCP 1216 is also signed Feri and has the same closing formula, sírig hű.

## Method

The key was **transferred from the finished sister cards**, chiefly HCP 1216; this is not a new key recovery. No text from a sister card was copied.

The transcription is **manual**. The solver read every row from enlarged crops of the unconverted original scan, one token per written sign, in a sign ledger (work/ledger.txt). No OCR was used. The reading was not blind to the expected Hungarian. A short script (work/decode.py) checks the hashes of the source images, applies the key to the ledger and prints the result:

```
python3 -I ciphers/hcp-1308/work/decode.py
```

The layout had to be worked out first. The right-edge row must be turned 270 degrees (a first attempt at 90 degrees came out upside down), the top row runs right to left, and the stamp block has to be turned about 12 degrees.

## Key

Simple monoalphabetic substitution with invented graphic signs. The names are conventional descriptions of the handwritten shapes.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| two bars | a | S-shape (close to the next) | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl | c (once) | three strokes | m | gamma/corner | t |
| long stroke + short tick | d (longer); h, p (shorter) | two equal strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross | f | loop with dot | i | looped descender | y |
| reversed-s shape | g | inverted T | j | crossed diagonal | z |
| opposed bowls | cs | | | | |

The digraph gy is written as g + y. Dots or a double mark over the loop or the cross give ö/ő, ü/ű. Acute accents are small ticks; they were not transcribed and are supplied in the normalization.

## Plaintext

Literal decipherment, one line per written row. {x} marks a value chosen by word sense.

```
01 szeretetedesjolankam
02 becsessoraitmegkaptam
03 mejertfogadjaköszö
04 netemetedesemköszö
05 nömhogyfelha{g}yezekel
06 avetejtarsakkaltudom
07 edesemhogymagaszeret
08 engemese{g}{y}szeretösziv
09 csakegygondolmindig
10 higyjeedesemazeletem
11 tölkönyebbeneltudnek
12 valnimintmagatolede
13 semaligvaromaztaper
14 c{z}zethogy{g}yakrabban
15 lathassamszepszemeit
16 ajövöhonapabanmajd
17 e{n}yhebleszefor{g}alom
18 esakormajd{k}erevagyket
19 napszabadsagotesle
20 megyekmertmegarok
21 szal{a}sbaislatniaka
22 romegyszerlega
23 labesugy{i}sakar{e}rok
24 szüleimhez{i}shazameniestudjaaztmagaisede
25 semhogyhamagaeljönarokszalabolnemn{a}gyonme
26 gyekaraakörnyekcsakhamuszajezelbezarom
27 soraimmaradokszere        (up the right edge)
28 kedves{f}eri              (top edge, right to left)

Stamp field: {ü}dvoz{l}öm / tavobol / csokjaiert / va{g}yosi / righü / imadoja / feri
```

Normalized Hungarian (word division, accents and spelling are editorial; square brackets mark letters the writer left out):

Szeretett édes Jolánkám! Becses sorait megkaptam, melyért fogadja köszönetemet. Édesem, köszönöm, hogy felhagy ezekkel a vetélytársakkal. Tudom, édesem, hogy maga szeret engem, és egy szerető szív csak egy[re] gondol mindig. Higgye, édesem, az életemtől könnyebben el tudnék válni, mint magától, édesem. Alig várom azt a percet, hogy gyakrabban láthassam szép szemeit. A jövő hónapában majd enyhébb lesz e forgalom, és akkor majd kére[k] vagy két nap szabadságot és lemegyek, mert meg Árokszállásba is látni akarom egyszer legalább, és úgyis akarok szüleimhez is hazamenni. És tudja azt maga is, édesem, hogy ha maga eljön Árokszállásból, nem nagyon megyek arra a környék[re], csak ha muszáj. Ezzel bezárom soraim, maradok szere[tő], kedves Feri.

Stamp field: Üdvözlöm távolból. Csókjaiért vagyo[k] sírig hű imádója, Feri.

## Translation

**English.** My beloved sweet Jolánka! I have received your esteemed lines, for which please accept my thanks. My darling, I thank you for giving up these rivals of mine. I know, my darling, that you love me, and a loving heart thinks always of one person only. Believe me, my darling, I could part from my life more easily than from you, my darling. I can hardly wait for the moment when I may see your beautiful eyes more often. Next month this traffic will ease, and then I shall ask for about two days' leave and come down, because I want to see you at Árokszállás too, at least once, and in any case I want to go home to my parents as well. And you know yourself, my darling, that if you leave Árokszállás, I shall hardly go to that area unless I must. With this I close my lines; I remain your loving, dear Feri.

Stamp field: I greet you from afar. For your kisses I am your adorer, faithful unto the grave, Feri.

**Slovak.** Moja milovaná, sladká Jolánka! Vaše vzácne riadky som dostal, za čo prijmite moju vďaku. Drahá moja, ďakujem Vám, že ste nechali týchto sokov. Viem, drahá, že ma ľúbite, a milujúce srdce myslí stále len na jedného. Verte mi, drahá, ľahšie by som sa rozlúčil so životom než s Vami, drahá. Sotva sa dočkám chvíle, keď budem môcť častejšie vidieť Vaše krásne oči. Budúci mesiac sa táto premávka zmierni a vtedy si vypýtam asi dva dni voľna a prídem dolu, lebo Vás chcem aspoň raz vidieť aj v Árokszállási, a tak či tak chcem ísť domov aj k rodičom. A aj Vy sama viete, drahá, že ak odídete z Árokszállásu, do toho kraja veľmi nepôjdem, iba ak budem musieť. Týmto končím svoje riadky, zostávam Váš milujúci, milý Feri.

Pole známky: Pozdravujem Vás z diaľky. Za Vaše bozky som Váš ctiteľ verný až do hrobu, Feri.

## What remains uncertain

Every sign has a value, but these points do not rest on the shape alone.

- **g and k** are near-homographs on this card. Word sense decides gyakrabban (row 14), forgalom (row 17) and kére (row 18, the least clean).
- **Row 8, egy:** two heavily re-inked blots; the word is a contextual reading. The g of felhagy (row 5) is also heavily inked, though its descender fits.
- **Row 14, start:** the c-z-z cluster is overwritten. percet (old spelling perczet) is reasonable, but the correction is not fully legible.
- **Row 17, enyhébb:** the sign after e is two heavy joined strokes, read n only because the phrase needs it. enyhébb lesz e forgalom ("this traffic will ease") is itself a reading from sense. It suggests work in a transport or postal service, but the card does not say so.
- **Row 21:** the vowel of -szalasba carries a blot; the same place in row 25 has two clear bars.
- **Row 23:** a bar sign under a stain between akar and rok is treated as a false start. The i of úgyis and of is (row 24) shows no dot.
- **Row 25, nagyon:** the bar sign lies under the collector's stamp.
- **Top edge:** the f of Feri is smeared; f by sense.
- **Stamp field:** the first sign is a blot with dots above it, so the ü of üdvözlöm is a restoration, and its l is cramped. The g and y of vagyo are faint.
- **Editorial completions:** szere[tő] at the corner (kedves[e] is also possible), egy[re], kére[k], környék[re], vagyo[k].
- **Spelling:** the writer's forms are normalized where they differ, for example mejért, vetéjtárs-, higyje, könyebben, hazameni, and Árokszállásból written with its s dropped. hónapában is kept as written; hónapban is the alternative. Neither solver nor reviewer has a native speaker's judgement on the regional forms.

Not read: a plain-script pen note beginning Sze… to the left of the Rákospalota box, partly hidden by it. It is not enciphered. The large U-shaped ink mark to the right of the stamp field is not cipher either.

## Review

An independent Claude Opus 5.5 reviewer reran the command, compared the key with the sister cards, read all rows sign by sign from its own crops and decoded them with its own script. Its reading was made after seeing the ledger, so it was not blind. The verdict was **REVISE**: the key, language, addressee and content stood, but six signs were wrong.

![Row 20 enlarged: after "me" stand the reversed-s (g), two bars, F, loop and S (k), the start of the town name (review/work/c20.png)](../review/work/c20.png)

What changed because of the review:

- **Rows 20–21 were mis-segmented.** The solver had read me{k}arok and Szállásba, and had to emend the first to meg a[ka]rom. The signs in fact give meg Árokszállásba, so the emendation and the "Szállás / lodging" discussion were dropped. Only this clause changed in meaning.
- **Five two-bar signs (a) had been read as three bars (e)**, in rows 6, 14, 16, 25 and 26. The words vetélytársakkal, gyakrabban, majd, Árokszállásból and muszáj are therefore spelled normally or more nearly so. Several supposed spelling oddities were the solver's misreadings, not the writer's.
- **Smaller corrections:** hónapában is kept as the writer's form, and row 20 left the list of sense-based g/k calls.

The solver checked each point on the enlargements and accepted all five findings. After the corrections the reviewer's own decoding differs from the ledger only in three rows where its script handles the dots of ü differently, so no reading is in dispute. As the changes were confined to these points, no second review round was held.
