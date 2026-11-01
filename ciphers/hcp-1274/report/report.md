# HCP 1274 (cpc_--_HU__HU_Jasz Arokszalas_jolanka-73): Feri to Jolánka Tóth, the reunion must wait a week

Human solver: Tomáš Pavuk

**Status: deciphered in full (338 signs read, 2 struck by the writer and left unread). Independent review 1 verdict ACCEPT; four minor findings addressed, no decoded letter changed.** Report dated 2026-11-01.

## Origin and context

The cryptogram is record 1274 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1274), portal name cpc_--_HU__HU_Jasz Arokszalas_jolanka-73, part of Tobias Schrödel's collection of cryptographic postcards (private collection). When it was captured on 2026-11-01 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language and sender unknown, recipient Tóth Jolánka, with no transcription or solution attached. The portal links a HistoCrypt article, which was not read for this work, so we cannot say whether it publishes this card. No published solution was found on the portal or in this repository.

The picture side is a tinted romantic photograph: a young woman with lilac in the foreground, and in an oval behind her a man with a bouquet. It carries a printed Hungarian text and no handwriting: *Sirassatok engem orgonavirágok...* and *Megyek, megyek messze földre! Elbujdosok, eltávozok mindörökre:* ("Weep for me, lilac flowers... I go, I go to a far land! I wander off, I go away for ever:").

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

The address side is written in red ink. The plain address reads *Szépreményű Tóth Jolanka úrleánynak, Jász-Árokszalás*, that is Miss Jolánka Tóth in Jászárokszállás, Hungary. In the stamp box stands a plain text: *csokolom szam talan szor sirig hü Feri* ("I kiss you countless times, faithful unto the grave, Feri"). The left part of the card and the long strip along the bottom hold the cipher, 22 rows without word division. No date can be read on the card.

![Address side: 19 rows at the left, three more at the bottom right past the divider, plain address, plain text in the stamp box (source/address-large.jpg)](../source/address-large.jpg)

The card belongs to a family of cipher postcards to Jolánka Tóth, several of them signed Feri and finished in this repository (for example HCP 1216, 1212, 1213, 1217, 1218, 1243, 1301). The earlier solving of that family was done by an OpenAI GPT solver and by Claude Opus 5.5. No earlier work existed on this number.

## Method

This card was read with a **known, transferred key**; it is not a new key recovery. The transcription is manual: the solver read every row from enlarged crops of the un-converted scan and recorded one token per written sign in `work/ledger.txt`. No OCR was used. A script checks the SHA-256 of the four image files and decodes the ledger:

```sh
python3 -I ciphers/hcp-1274/work/decode.py
```

Rows 18 and 19 share the bottom left, and rows 20 to 22 stand at the bottom right past the divider. The first readings needed two repairs, both by rereading: row 13 divides as *azt a boldogságot*, and the bottom left holds two rows rather than one.

In review a second agent cropped the scan itself, typed its own shape-by-shape reading of all 22 rows and decoded it through a map built from the family key file, not through the solver's script. 21 of 22 rows matched exactly; the one difference is the last sign of row 19 (see Uncertainties). The reviewer had read the solver's text first, so this was not a blind transcription.

## Key

Monoalphabetic substitution with invented graphic signs. Vowels with accents use the same sign with marks above it. The cipher has no word division.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| two bars | a | section mark / loop with hook | k | F-like | r |
| six | b | wave | l | right bowl | s |
| left bowl + right bowl | cs | three short strokes | m | gamma | t |
| short stroke + long stroke | d | two short strokes | n | plain cross | u |
| three bars | e | cursive loop | o | chevron | v |
| upright cross + | f | long stroke + short stroke | h | dotted crossed curve | i |
| open loop with descender | g | inverted T | j | low descender | y |
| joined loop + descender | gy | crossed diagonal with tail | z | | |

Two marks over o or u give ö, ő or ü, and a tick gives an acute accent. All 338 signs fall in these classes and no letter class is new to this card. The d and h descriptions are this card's own hand. All 5 h signs are tall+short, which the family key records as p or as the h/p near-homograph, so **h rests on word sense**: *pogy*, *pét*, *pasztani* are no words.

## Plaintext

Literal decipherment, row by row (`[x]` = a sign struck by the writer):

```text
01 kedvesjolankam          12 telenel[x]halaszta
02 sajnala[x]ttalkeltu     13 niaztaboldogsagot
03 datnomhogyaviszont      14 melyetoldalamel
04 latásörömeitkeny        15 leélvezhettemvol
05 telenvagyokegyhet       16 namulassonjolede
06 telodabhasztani         17 semésgoljöramaki
07 edesemmostcsinalunk     18 mégakordogozikmikot
08 aröföskeskereskedö      19 sétalnikelene
09 nekberendezestesma      20 istenveleedesem
10 keletvolnakeszlen       21 üdvözölveatavol
11 niemiatvagyokkeny       22 bol
```

Normalized Hungarian (square brackets mark letters the writer left out, or a false start):

Kedves Jolánkám! Sajnálattal kell tudatnom, hogy a viszontlátás örömeit kénytelen vagyok egy héttel odább ha[la]sztani. Édesem, most csinálunk a rőfös [kes] kereskedőnek berendezést, és ma kellett volna kész lenni, emiatt vagyok kénytelen elhalasztani azt a boldogságot, melyet oldala mellé élvezhettem volna. Mulasson jól, édesem, és go[ndo]ljö[n] rám, aki még akkor do[l]gozik, mikor sétálni kellene. Isten vele, édesem! Üdvözölve a távolból.

Stamp box (plain): Csókolom számtalanszor. Sírig hű Feri.

**English.** Dear Jolánka of mine! I am sorry to have to tell you that I am forced to put off the joys of our reunion by a week. My darling, we are now making the fittings for the draper, and it should have been finished today; that is why I am forced to postpone the happiness I could have enjoyed at your side. Have a good time, my darling, and think of me, who am still working when one ought to be out for a stroll. Farewell, my darling! Greetings from afar.

Stamp box: I kiss you countless times. Faithful unto the grave, Feri.

**Slovak.** Milá moja Jolánka! S ľútosťou Vám musím oznámiť, že radosti zo stretnutia som nútený o týždeň odložiť. Drahá, teraz robíme zariadenie pre obchodníka s látkami a dnes to malo byť hotové, preto som nútený odložiť to šťastie, ktoré som si mohol užiť po Vašom boku. Dobre sa zabávajte, drahá, a myslite na mňa, ktorý ešte pracujem aj vtedy, keď by sa malo ísť na prechádzku. S Bohom, drahá! Pozdrav z diaľky.

V rámčeku na známku: Bozkávam Vás nespočetnekrát. Do hrobu verný Feri.

## Uncertainties

Every sign is transcribed as written. The points below are calls that rest on word sense or on the writer's spelling; none changes the sense of the message.

- **Row 3, first sign:** two tall strokes, the second a little longer. Read d because *tu|datnom* is the only word.
- **Row 3, *a* before *viszont*:** a top bar and a blot; *hogy a viszontlátás* gives the reading.
- **All h signs:** word-sense calls against p (see Key).
- **Row 6, *hasztani*:** every sign is clear; *ha[la]sztani* is an emendation. Rows 12 and 13 spell the word in full.
- **Row 8, *kes*:** clearly written, with a three-bar e, so not *kis*. Probably a false start, left out of the translation. In *rőfös* ö and ő are not told apart by the signs.
- **Row 17, *goljö rám*:** every sign is clear. *go[ndo]ljö[n]*, standard *gondoljon* ("think"), is supplied on sense. This is the word most short of letters (four); the clause around it reads.
- **Row 18, *dogozik* and *mikot*:** normalized *dolgozik* and *mikor*. The last sign of *mikot* is t as written, with no mid-bar; *mikor* is an emendation.
- **Row 19, last sign:** a top bar and one kinked lower stroke, so a three-bar e with the lower bars run together, or a two-bar a as a slip. *kellene* stands either way.
- **Rows 10–11, *keszlen|ni*:** read *kész lenni*; there is no u sign, so not *készülni*.
- **Rows 14–15, *oldala mel|le*:** literally *mellé* ("to your side") where *mellett* ("at your side") is expected; the translation follows the expected sense. *oldalam mellé* ("to my side") is not excluded, since the m may be shared.
- **Struck and stray marks:** the writer cancelled a word-sized scribble in row 2 and an A-shaped sign in row 12; neither can be read beneath the strokes. The second ö of *örömeit* (row 4) is overwritten. A narrow pale loop after the first i of row 11 and a stray dot near the row 11 n match no key class and are treated as stray marks.
- **Unverified:** what the *berendezés* job actually was, beyond the plain sense, and whether the HistoCrypt article treats this card.

The single-consonant spellings (*kel*, *kelene*, *keletvolna*, *emiat*, *akor*, *odab*) are the writer's habit, shared with the family, and are normalized.

## Review summary

The reviewer tried to refute the solution and returned **ACCEPT**. Besides the independent decode described above, it checked all 340 ledger tokens against the family classes, checked each disclosed uncertainty on enlarged crops, confirmed the plain address and stamp text, and judged the text to be continuous period Hungarian with real, correctly used words (*rőfös kereskedő*, *berendezés*, *kénytelen*, *viszontlátás*) and a concrete, coherent excuse.

Its four findings were all minor, and all concern disclosure:

1. The last sign of row 19 was ledgered as e without comment. Now marked as a word-sense call.
2. The h/p call was not disclosed. Now stated under the key.
3. A pale loop in row 11, a stray dot and the overwritten ö of row 4 were not mentioned, against the claim that nothing was left over. Now listed, and the claim softened.
4. The list of uncertainties was inconsistent about which words lack letters and which normalized form is used. Now corrected, and the *kis* alternative dropped.

No decoded letter and no sentence of the translation changed as a result.
