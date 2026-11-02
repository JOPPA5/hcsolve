# HCP 1137 (cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39): Árpád's cipher card to Margitka from Kis Terenne

Human solver: Tomáš Pavuk

**Status: deciphered in full (373 of 373 cipher signs; 370 give their letter as written, 3 lack their mark and 1 word omits a letter, all four corrected by word sense). Independent review 1 verdict REVISE, findings addressed, cipher reading unchanged.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1137 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1137), portal name cpc_1916-06-10_HU_Mezokovesd_HU_Szomolya_szomolya-39, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, recipient Margitka Sziber, with no transcription or solution attached.

The card is a wartime picture postcard. The picture side shows printed roses, with a faint printed signature at the left edge and no handwriting. On the other side the place and date are open: **Kis Terenne, 1916 VI 10** (10 June 1916). The modern name of the place is Kisterenye, and the postmark reads KISTERENYE, with a date consistent with JUN 10, 1916, as far as legible. The portal file name says Mezokovesd, but this card was written and posted at Kis Terenne. The open address reads **Őnagysága. / Sziber Margitka / Kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács.** ("Her Ladyship Miss Margitka Sziber, Szomolya, Borsod county, post office Bogács").

Everything else on the message side is in digits, 21 rows of them, apart from the open letters `Érte` that begin the first word of the message. Pencil rules divide the prose, the verse and the close; the last two rows run along the bottom edge beneath the address. The card belongs to the correspondence of the writer Árpád with Margitka Sziber, 1915 to 1916; finished cards hcp-1174, 1178 and 1179 hold the cipher key. Card hcp-1150 is from the same place with the same layout.

![Address and message side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan (3468 by 2298 pixels) enlarged 2 to 5 times; no OCR was used. Where signs lie under the brown collection stamp or the postmark ring, pencil was separated from stamp by colour.

The key of the finished cards decoded the heading at once as Édes Margitkám. The open `Érte` then gave `-sítlek`, and the prose supplied the missing signs from its own words: `4.` = gy (hogy, vagyok, gyakran), `6.` = ny (Terenyén, leány), `6` = j (újságot, eljöttem), `.1` = u (kúthoz, újságot, tudok, szervusz), `9.` = zs (rózsaszál). Each of these holds in every occurrence on the card.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1137/work/decode.py`. The script checks the hashes of the scans, decodes every sign as written, asserts each word and prints the text. The open text is hard-coded there.

## Key

Monoalphabetic substitution (MASC), Hungarian, one sign per letter or digraph. A sign is a digit with an optional mark, and the mark belongs to the sign. Length is shown only for a/á and e/é. The 30 signs below are all that occur on the card. Crossed 7s and flagged 5s carry no meaning. The signs labelled "this card" are not on the finished key cards; they were established here independently and also occur, with the same values, on unreviewed sister cards.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `3` | d | `6.` | ny (this card) |
| `0,` | ö, ő | `3,` | r | `7` | k |
| `1` | i, í | `3.` | v | `7,` | s |
| `1.` | a | `4` | f | `7.` | sz |
| `1:` | e | `4,` | g | `8` | m |
| `1'` (high dot) | á | `4.` | gy (this card) | `8,` | t |
| `1,` | b | `5` | h | `9` | p |
| `.1` (dot left) | u, ú (this card) | `5,` | l | `9,` | z |
| `:1` (two dots left) | ü, ű | `6` | j (this card) | `9.` | zs (this card) |
| `2,` | cs | `6,` | n | | |
| `2.` | é | | | | |

## Transcription

The signs exactly as written, grouped by words and by the lines of the text. A word split at a line end on the card (Tere-nyén, találkoz-tam, Szent-kúthoz) is kept whole here.

```text
2. 3 1: 7,  /  8 1. 3, 4, 1 8, 7 1' 8
7, 1 8, 5, 1: 7  /  5 0 4.  /  8 1' 3,  /  1 8, 8,  /  3. 1. 4. 0 7  /  8, 1: 3, 1: 6. 2. 6,
8 2. 4,  /  3, 0 9, 1' 3. 1. 5,  /  6, 1: 8  /  8, 1. 5, 1' 5, 7 0 9, 8, 1. 8
5, 1: 5 1: 8,  /  5 0 4.  /  1: 5, 8 1: 4. 1: 7  /  1.  /  7. 1: 6, 8,
7 .1 8, 5 0 9,  /  1 7,  /  1: 4. 1: 1,  /  .1 6 7, 1' 4, 0 8,  /  6, 1: 8  /  8, .1 3 0 7
1 3, 6, 1  /  7. 1: 3, 3. .1 7.
1: 5, 5 1: 3, 3. 1. 3  /  1.  /  3, 0 9. 1 7. 1' 5,  /  1 7,
5 1.  /  8 1: 4, 2, 1 9 8, 1:  /  8 1' 3,  /  1.  /  3 2. 3,
1: 5, 5 1: 3, 3. 1. 3  /  1.  /  5, 1: 1' 6.  /  1 7,  /  5 0 4. 5 1.
6, 1: 8  /  4 0 3,  /  1, 1: 6, 6, 1:  /  8 1' 3,  /  1.  /  3. 2. 3,
:1 3 1:  /  1. 9,  /  2. 6,  /  3, 0 9. 1. 7. 1' 5, 1. 8
8 1: 5, 1: 4,  /  1' 4. 1, 1. 6,  /  1' 9 0 5, 0 8
4 0 3, 3,  /  1.  /  3. 2. 3, 1:  /  1.  /  1, 1. 1, 1' 8 6, 1. 7
8 1: 3, 8,  /  5 1 7.  /  4. 1. 7 3, 1. 6,  /  2, 0 7 0 5 0 8
1. 9, 2. 3, 8,  /  5 0 4.  /  1: 5, 6 0, 8, 8, 1: 8
7. 1: 3, 1: 7, 7,  /  2, 1. 7  /  8, 0 3. 1' 1, 1, 3, 1.
8 1: 3, 8,  /  8 2. 4,  /  3. 1 7, 7. 1. 8, 2. 3, 1: 7
1 7, 8 2. 8,  /  5 0 9, 9, 1' 3  /  5 1' 6. 7 1.
7. 1' 8, 1. 5, 1. 6, 7. 0 3,  /  0, 5, 1: 5,  /  2. 7,  /  2, 0 7 0 5,
1.  /  8, 1' 3. 0 5, 1, 0 5,
5 :1  /  1 8 1' 3 0 3  /  1' 3, 9 1' 3
```

## Plaintext

Square brackets show what is enciphered on the card. Commas and sentence breaks are editorial.

Kis Terenne, 1916 VI 10

[Édes Margitkám]!

Érte[sítlek hogy már itt vagyok Terenyén, még Rózával nem találkoztam, lehet hogy elmegyek a Szent-kúthoz is, egyeb újságot nem tudok írni, szervusz]

[Elhervad a rózsaszál is, / Ha megcsípte már a dér, / Elhervad a leány is, hogyha / Nem for[r] benne már a vér.]

[Üde az én rózsaszálam, / Meleg ágyban ápolom, / Forr a vére a babámnak, / Mert hisz gyakran csókolom.]

[Azért, hogy eljöttem, szeress csak továbbra, / Mert még visszatérek ismét hozzád, lányka.]

[Számtalanszor ölel és csókol a távolból hű imádód, Árpád]

## English translation

My sweet Margitka! I let you know that I am already here in Terenye; I have not yet met Róza; perhaps I will also go to the Szentkút (the Holy Well); I can write no other news; bye.

The rose too withers once the frost has nipped it; the girl too withers if the blood no longer boils in her.

Fresh is my rose; I tend her in a warm bed; my sweetheart's blood boils, for I kiss her often.

Though I have gone away, go on loving me, for I will yet come back to you again, girl.

Countless times your faithful adorer embraces and kisses you from afar, Árpád

(`Meleg ágyban` also suggests `melegágy`, a garden hotbed, which suits the rose image.)

## Slovak translation

Moja sladká Margitka! Oznamujem ti, že už som tu v Terenyi; s Rózou som sa ešte nestretol; možno pôjdem aj k Svätej studni (Szentkút); iné novinky ti napísať neviem; servus.

Aj ruža zvädne, keď ju zasiahne mráz; aj dievča zvädne, ak v ňom už nevrie krv.

Svieža je moja ruža, opatrujem ju v teplej posteli; mojej milej vrie krv, veď ju často bozkávam.

Hoci som odišiel, ľúb ma ďalej, lebo sa k tebe ešte vrátim, dievčatko.

Nespočetnekrát ťa z diaľky objíma a bozkáva tvoj verný ctiteľ, Árpád

## Uncertainties

Four words do not come out of the table as written. The words themselves are certain:

1. `rózsaszál`: a plain 1 with no dot, so the table gives `rózsiszál`. The same stem has `1.` in `rózsaszálam`.
2. `csókolom`: the 5 has no comma, so the table gives `csókohom`. The rhyme with `ápolom` fixes the word.
3. `lányka`: the 5 has no comma, so the table gives `hányka`, not a word. Of the four, this rests most on sense; the same writer uses `lányka` in verse on hcp-1150 (as filed there).
4. `számtalanszor`: the m is omitted. The card has an ordinary `8,` = t, so the table gives `szátalanszor`. It is the writer's usual closing.

Other points:

- Writer's forms are kept: `egyeb` (normal `egyéb`), `for` with one r (normal `forr`), and `Értesítlek` without the linking vowel (normal `értesítelek`), which this writer also uses on other cards. He spells the place `Terenne` in clear and `Terenyén` in cipher.
- `9.` = zs rests on one stem, twice, on this card; it contrasts with `9,` = z in `Rózával`.
- Long hooks after `írni`, `kúthoz is` and `imádód` are taken as commas. The hook on the last 3 of `Árpád` is taken as the same flourish; as a comma it would make the sign r, which gives no name.
- Hyphens at line ends inside a word are word-break marks; the one after `ápolom` is a dash.
- `a távolból` is a short row above the last row, read after `csókol` as an insertion. It could stand elsewhere in the closing sentence; no word changes.
- `Szent-kúthoz` is read as the pilgrimage place Szentkút (Mátraverebély), near Kisterenye. That geography is general knowledge, not on the card. Róza is unknown.
- The verses may be a printed or folk rhyme; no source was identified.
- The postmark date is only partly legible.
- No published solution of this card was found. Of the article the portal links (Schrödel, "Cryptographic postcards", HistoCrypt 2021) only the landing page was seen, which has no decipherments, so a published reading cannot be fully excluded.

## Why the reading is believed correct

A key built on other cards decodes 370 of 373 signs as written into continuous Hungarian prose and two rhymed quatrains (dér / vér, ápolom / csókolom) plus a couplet, with nothing fitted to the text. The whole message is enciphered, so there was no open context to bend the key to. Terenyén agrees in place with the open heading and the postmark, and Margitkám and Árpád agree with the rest of the correspondence.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) typed its own transcription of all 21 rows from its own crops, with its own key table. It agreed with the solver on all 373 signs, the only differences being four placeholder tokens the solver had used where the reviewer gave what is on the card. It confirmed the difficult signs at 3 to 6 times enlargement, the consistency of all 30 signs, and the agreement with the finished key cards. The verdict was **REVISE** with six findings:

1. The open place name had been given as `Kisterenye`; the card has `Kis Terenne`. Corrected.
2. `számtalanszor` had been described as one sign standing for m and t; it is an ordinary `8,` with the m omitted. Corrected.
3. The sign count of 33 included placeholders; the card has 30 distinct signs. Corrected, and the script now asserts it.
4. The five signs called new also occur on unreviewed sister cards. Now stated.
5. Small points had gone unmentioned: the hook on `Árpád`, the `Tere-nyén` hyphen, the dash after `ápolom`, and the form `Értesítlek`. Now disclosed.
6. Translations: `Margitkám` now has its possessive ("My sweet Margitka", "Moja sladká Margitka"), and the note on `melegágy` was added.

No sign or letter of the cipher reading changed. After the changes the reviewer's own script agrees with the final transcription in every token.

The review could not verify every digit of the postmark, a printed source for the verses, or the full text of the linked article, and it relied on the sister tables as filed without rereading those cards.
