# HCP 1146 (cpc_1916-04-14_HU_Mezokovesd_HU_Szomolya_szomolya-28): love verses in a digit cipher on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: deciphered in full. All 311 cipher signs are read: 306 cleanly by the key, 3 by word sense and 2 through a stroke overlap. Independent review 1 gave REVISE; its four findings are addressed, changing one word and adding the open date line.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1146 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1146), portal name cpc_1916-04-14_HU_Mezokovesd_HU_Szomolya_szomolya-28, from Tobias Schrödel's cryptographic postcards collection (private collection). When it was captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard and T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). Neither solver nor reviewer checked whether it discusses this card.

It is a picture postcard showing a couple in a garden, with nothing written on the picture side. The whole message is on the address side in blue copying pencil, and it is mostly digits with some Hungarian words in clear. The last line, below the signature, gives place and date in open script: **Mezőkövesd. 1916. IV/14**. The postmark date is illegible. 14 April 1916 was a Friday, nine days before Western Easter on 23 April, which fits the message exactly.

The open address reads: **Őnagysága / Szépreményü / Sziber Margitka / kis-asszonynak / Szomolya / u. p. Bogács. / (Borsod m.)**, that is, "Her Ladyship, the promising Miss Margitka Sziber, Szomolya, post office Bogács, Borsod county". This was wartime north-east Hungary. The card belongs to a correspondence from Mezőkövesd to Margitka Sziber, 1915 to 1916, in which hcp-1174, 1178 and 1179 use the same digit alphabet and the writer signs Árpád.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scan enlarged 2 to 5 times. No OCR was used and the portal supplied no transcription.

The key was transferred from the finished card hcp-1174 and extended here. The hcp-1174 table read the opening at once (`Édes Margitkám! Értesítlek ...`). Signs missing from that table were recovered on this card: `.1` from húsvétkor, mulattatlak and hű; `6` from majd and járok; `4.` from hogy, megyek and elhagyott; `6.` from lányka; `8.` from kártya; `4` from fel. A dot on 4, 6 and 8 gives the palatal partner (gy, ny, ty), which emerged as a regular system and was not assumed. The word kártya shows the key is not being fitted to the text: the solver first typed it as kárta, and the sign forced the y.

To reproduce the decoding, run this from the repository root:

```text
python3 -I ciphers/hcp-1146/work/decode.py
```

The script checks the SHA-256 of all four scans, decodes each word of work/transcription.txt, asserts each against its reading, and prints the text. The open words are hard-coded there, so the command tests the cipher part only.

## Key

Monoalphabetic substitution (MASC). One letter is a digit with an optional mark, Hungarian digraphs have one sign, and words are not always separated. The card does not distinguish o/ó, ö/ő, i/í, or u/ú, so those accents in the plaintext are editorial.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `6.` | ny (new) |
| `0,` | ö, ő | `2.` | é | `7` | k |
| `1` | i, í | `3` | d | `7,` | s |
| `1.` | a | `3,` | r | `7.` | sz |
| `1:` | e | `3.` | v | `8` | m |
| `1'` (high dot) | á | `4` | f | `8,` | t |
| `1,` | b | `4,` | g | `8.` | ty (new) |
| `:1` (dots left) | ü | `4.` | gy (new) | `9` | p |
| `.1` (dot left) | u, ú, ű (new) | `5` | h | `9,` | z |
| `6` | j (new) | `5,` | l | `6,` | n |

## Ciphertext

The signs as transcribed, grouped by the plaintext word they give:

```text
T   2. 3 1: 7, / 8 1. 3, 4, 1 8, 7 1' 8
A   2. 3, 8, 1: 7, 1 8, 5, 1: 7 / 5 0 4. / 3. 1. 7, 1' 3, 6, 1. 9 /
    6, 1: 8 / 8 1: 4. 1: 7 / 4 1: 5, / 8 1. 6 3 / 2, 1. 7 /
    5 .1 7, 3. 2. 8, 7 0 3, / 8 1' 3, / 5 1' 5 1. /
    1 7, 8, 1: 6, 6, 1: 7 / 6, 1: 8 / 8 1: 7, 7. 1: / 3. 1. 6,
P   8 0 7, 8, / 1: 4. 1: 1, 1: 8, / 6, 1: 8 / 1 3, 0 7 / 8 1. 6 3 /
    7. 0 3. 1. 5, / 8, 0, 1, 1, 1: 8,
B   1. 3 1 4, / 1 7, / 3. 1: 3, 7, 1: 2, 7 2. 7 7 1: 5, /
    8 .1 5, 1. 8, 8 1. 8, 5, 1. 7
V1  1 8, 8, / 1: / 3. 1' 3, 0 7, 1, 1. 6, / 6 1' 3, 0 7
V2  6, 1 6, 2, / 1 8, 8, / 1. / 5, 1: 5, 7 1: 8
V3  6, 1' 5, 1. 3
V4  7. 1: 3, 1: 5, 8 1: 8 / 7. 1: 6, 8, 1: 8
V7  1: 5, 5 1. 4. 0 8, 8, / 3. 1. 4. 0 7 / 8 2. 4, 1 7
V8  3. 1. 4. / 3. 1: 5, 1: 8 / 8 0 7, 8, 1. 6,
V9  1: 3, 1: 8, 5, 1: 7 / 7. 1 3. 1: 8 1, 0, 5,
V10 2. 5, 1: 7 / 5, 1' 6. 7
V11 7. 1' 9, 7. 0 3,
V12 1 7, 8 2. 8, 5, 1 / 1: / 7 1' 3, 8. 1.
C   :1 3 3. 0, 9, 0, 5, / 7, 0 7 7. 0 3, / 0, 5, 1: 5, / 2. 7, /
    2, 0 7 0 5, / 5 .1 / 7 1: 3 3. 1: 7, 1: 3 / 1' 3, 9 1' 3
```

## Plaintext

Square brackets mark text enciphered on the card; the rest is open script. Parentheses are marks on the card, written as two curved strokes. `adig` is a one-d spelling of addig.

```text
[Édes Margitkám]!

[Értesítlek hogy vasárnap nem megyek fel majd csak húsvétkor
már hála istennek nem messze van] ([most egyebet nem írok majd
szóval többet]) [adig is versecskékkel mulattatlak]

[Itt e városban járok],
De [nincs itt a lelkem],
Ott maradt az [nálad],
Én [szerelmem szentem].

Ezer ember jár az utcán,
Vagy több is tán e városban,
S én [elhagyott vagyok mégis],
Mert hisz nem [vagy velem mostan].

Sz[eretlek szívemből],
Érted [élek lányk]a,
Elmondottam [százszor] is,
S [ismétli e kártya].

[üdvözöl sokszor ölel és csókol hű kedvesed] ([Árpád])
Mezőkövesd. 1916. IV/14
```

## English translation

Sweet Margitka! I let you know that I am not coming up on Sunday, only at Easter, which, thank God, is not far off now (I write nothing else now, more later by word of mouth). Until then I will entertain you with little verses.

Here in this town I walk, / but my soul is not here, / it stayed there with you, / my love, my saint.

A thousand people walk the street, / perhaps more in this town, / and yet I am forsaken, / for you are not with me now.

I love you from my heart, / for you I live, girl, / I have said it a hundred times, / and this card repeats it.

Greets you many times, embraces and kisses you your faithful sweetheart (Árpád)

Mezőkövesd, 14 April 1916

## Slovak translation

Sladká Margitka! Oznamujem ti, že v nedeľu neprídem hore, až na Veľkú noc, ktorá, vďaka Bohu, už nie je ďaleko (teraz nepíšem nič iné, neskôr poviem ústne viac). Dovtedy ťa budem zabávať veršíkmi.

Tu v tomto meste chodím, / ale moja duša tu nie je, / zostala tam u teba, / moja láska, moja svätá.

Tisíc ľudí chodí po ulici, / azda aj viac v tomto meste, / a ja som predsa opustený, / lebo teraz nie si so mnou.

Ľúbim ťa zo srdca, / pre teba žijem, dievča, / povedal som to už stokrát, / a táto pohľadnica to opakuje.

Mnohokrát ťa pozdravuje, objíma a bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 14. apríla 1916

## What remains uncertain

Five signs are not clean readings:

- `hála`: no comma is visible under the second 5, so as written the sign is h. The phrase `hála istennek` ("thank God") makes l certain.
- `mulattatlak`, sixth sign: blurred and k-shaped, read as `8,` by sense.
- `mulattatlak`, last two signs: this small word is squeezed under `adig is versecskékkel`, and commas from that row run into it. Taken alone the two signs look like `4.` and a barred 4, which give no word. The upper strokes line up with the descending commas of the row above, leaving `1.` and `7`. The commas of `3,` and `7,` in versecskékkel rest on the same reading of the overlap.
- `mégis`, last sign: a blotted, overwritten loop with a comma stroke after it. It is not a clean 7, and the reading `7,` rests on the word and the verse.

Smaller points:

- The open words `Ezer` and `Vagy` have their first letters over printed text. `Ezer` is by sense.
- `szóval` in the bracket is taken as "by word of mouth"; it could also be the filler "so". The first bracket mark could be a long comma, so the bracket itself is an editorial layout.
- In `hű` the sign `.1` stands for ű, although the family's `:1` is ü. So `.1` covers more than plain u here.
- In `hogy` the mark on the 4 is a short low dash, taken as the dot.
- The mark after `százszor is` and short strokes in the right margin near rows 9 to 12 are unexplained. They form no clause and are treated as punctuation or strays.
- The signs `6.`, `8.` and `4` occur once each. Each gives a clear word, but none is repeated on this card.
- hcp-1179 reads a dotted 8 as a variant of t in `kar[t?]im`. This card suggests dotted 8 is ty, but that card was not reworked.

## Why the reading is believed

- A key from another card read the opening with no change, and 306 of 311 signs decode cleanly into Hungarian.
- The new signs recur in unrelated words where they occur more than once, and the dotted set gy, ny, ty is regular.
- The verses rhyme (lelkem / szentem, városban / mostan, lányka / kártya), and enciphered and open words join grammatically across every switch. Examples are `De [nincs itt a lelkem]` and `Sz[eretlek]`.
- `városban` in the first stanza agrees with the same word in open script in the second.
- The content fits the card's own date line, the recipient and the sister cards, where `Árpád`, `csókol` and `Édes Margitkám` recur.

No published solution was found or used.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) ran the decoder, wrote its own decoder with its own key table, and checked every cipher row against its own 2x to 5x crops. Apart from the corrections below, its reading agreed word for word. Its verdict was **REVISE**, with four findings:

1. **Major, fixed.** The word first read `városian` is `városban`: a separate comma stands under the 1, making the sign `1,` = b. The line became "Here in this town I walk", replacing a strained "in town fashion".
2. **Major, fixed.** The first handover said the card had no written date. The open line `Mezőkövesd. 1916. IV/14` below the signature was overlooked; it is now in the text and translations.
3. **Minor, fixed.** The address has `Szépreményü` with two dots and is now printed as written.
4. **Minor, fixed.** The headline count of 308 by the table is now 306 clean, 3 by sense and 2 through an overlap.

The reviewer could not read the postmark date either. It also did not check the HistoCrypt article.
