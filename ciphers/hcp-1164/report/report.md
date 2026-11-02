# HCP 1164 (cpc_1916-04-01_HU_Mezokovesd_HU_Szomolya_szomolya-26): Árpád's love verses to Margitka in a digit cipher

Human solver: Tomáš Pavuk

**Status: deciphered in full (556 of 556 cipher signs, no word unread; a few blotted signs rest on word sense, listed below); independent review 1 verdict ACCEPT, no word of the plaintext changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1164 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1164), portal name cpc_1916-04-01_HU_Mezokovesd_HU_Szomolya_szomolya-26, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. No published solution was found or used. The reading was made from the card.

The card is a wartime picture postcard sent from Mezőkövesd to the village of Szomolya in north-east Hungary. The picture shows a young couple beside a flower stand. The address is in clear: Őnsg. Szépreményű Sziber Margitka Kisasszonynak, Szomolya (Borsodm.), u. p. Bogács. The postmark reads Mezőkövesd, 1 APR; its year is not legible. The writer dates the card in clear as Mezőkövesd, 1916 IIII 1. That was a Saturday, which suits a message about the coming Sunday.

The card belongs to a group of cards to Margitka Sziber. On most of those solved so far, such as HCP 1174, 1178 and 1179, only key words are enciphered inside open Hungarian. Here almost the whole message is in cipher, on both sides. Only the address, the date and a few words and letters in verse 3 are in clear. The message is in Hungarian, although the portal says Unknown. It fills the writing space, turns up the left margin, sits in a box in the top right corner, and goes on along the long edge of the picture side.

![Address and message side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, scanned sideways, with three cipher rows along the long edge (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scans (work/hires/) enlarged several times. No OCR was used. The picture-side rows lie on a dark halftone, so contrast strips were made for them.

The starting key came from the FINAL cards HCP 1174, 1178 and 1179. The first rule of that key is that a digit and its mark make one sign, so `8` and `8,` are different letters. The heading is the same string as on HCP 1174, Édes Margitkám. The family key then gave "Vasárnap nem igen mehetek fel mert it van egy kis dolgom" at once. The remaining signs came from word sense and repeated words: `felmegyek`, `kártyát`, `üdvözlet-`, `milyen`, `olyankor`.

Several first readings were corrected on enlargements before review, each by rereading the shape: a comma that belonged to the row below in `nincs`, a star wrongly taken as a comma in `rózsák` (first read rózsás), a green printed mark taken as a dot in `nincs e`, and three strokes for four in the month.

The result can be reproduced from the repository root with `python3 -I ciphers/hcp-1164/work/decode.py`. It checks the SHA-256 of all four scans, decodes each sign of work/transcription.txt by a fixed table, stops on any mismatch with the stated word, and prints the text. Output: 556 cipher signs, 31 distinct, no unused key sign.

## Key

Monoalphabetic substitution (register type MASC). One sign stands for one letter or one Hungarian digraph. The sign is a digit plus an optional mark. Spaces fall between words. Vowel length is mostly not marked for o, i and u. The sign for ü also serves u, ú and ű, and the sign for ö also serves ő.

| Digit | No mark | Dot `.` | Comma `,` | Other |
|---|---|---|---|---|
| 0 | o, ó | | ö, ő | |
| 1 | i, í | a | b | `1:` e; `1'` (high dot) á; `:1` (dots left) ü, ű, u, ú |
| 2 | | é | cs | |
| 3 | d | v | r | |
| 4 | f | gy | g | |
| 5 | h | ly | l | |
| 6 | j | ny | n | |
| 7 | k | sz | s | |
| 8 | m | ty | t | |
| 9 | p | zs | z | |

All 31 signs occur on this card. This card adds or settles `4` f, `4.` gy, `5.` ly, `6` j, `6.` ny, `8.` ty, `9.` zs and `1,` b. The separately solved cards HCP 1165 and 1169 file `4.` gy and `6` j from other words, and HCP 1169 also `5.` ly. The commonest signs are `1:` e (57) and `1.` a (53), as expected for Hungarian.

Two limits apply. `9.` zs occurs once (`rózsák`) and `8.` ty twice (both `kártyát`), so these are thinly attested, though the words and the dot pattern support them. And `5.` is ly here, by `milyen`, `olyankor` and `oly`, whereas HCP 1178 and 1179 file the same sign as l (`a legszeb`, `csókollak`). The table holds for this card; it does not settle those two.

## Ciphertext

As transcribed. A slash separates words. Plain handwriting (M betű?, B, e, S, így?, Egy, the final t of two words, Mezőkövesd, the date) stands without marks among the signs.

```text
[ADDRESS SIDE, top block]
2. 3 1: 7, / 8 1. 3, 4, 1 8, 7 1' 8
3. 1. 7, 1' 3, 6, 1. 9 / 6, 1: 8 / 1 4, 1: 6, / 8 1: 5 1: 8, 1: 7 / 4 1: 5, / 8 1:
3, 8, / 1 8, / 3. 1. 6, / 1: 4. / 7 1 7, / 3 0 5, 4, 0 8 / 9 1: 3 1 4, / 2. 3 1: 7,
/ 1. 6. 1' 8 8 1. 5, / 1 7, / 1. 7 1. 3, 6, 2. 7 / 8 1' 3, / 1, 1: 7. 2. 5, 6, 1 / 5
1. 2, 1. 7 / 5, 1: 5 1: 8, / 1. 9, 2. 3, 8, / 4 1: 5, 8 1: 4. 1: 7 / 8 0 7, 8, / 9
1: 3 1 4, / 1 3, 0 7 / 1: 4. / 7 1 7, / 3. 1: 3, 7, 1: 8,
[Verse 1]
8 1. 3, 4, 1 8, 7 1' 6, 1. 7 / 5 1 3. 6, 1. 7 / 8, 2. 4, 1: 3
1. 3, 1. 6. 0 7, / 3. 1. 4. / 1 4, 1. 9, 1' 6,
3. 1: 3 3 / 1: / 7 1' 3, 8. 1' 8, / :1 3 3. 0, 9, 5, 1: 8, :1 5,
7, / 4, 0 6, 3 0 5, 6 / 3 3, 1' 4, 1. / 6, 2. 5 1. / 3, 1' 8
[Verse 2]
4 0 4, 1. 3 3 / 1: 9, 8, / 1. / 7 1' 3, 8. 1' 8, / 7, / 3. 1: 5, 1:
:1 3 3. 0, 9, 5, 1: 8, 1: 8 / 8 1. 3, 4, 1 8, 7 1.
6. 1 5, 6 1. 6, 1. 7 / 7 1 / 1. 1, 5, 1. 7 0 3 1, 1. 6,
9 1 3, 0 7, / 3, 0 9. 1' 7 / 5 1. 6 6, 1. 5, 3, 1.
[Verse 3]
5 0 4. / 8 1 8, / 6 1: 5, 1: 6, 8, / 1. 9, / M / betű?
2, 1. 7 / 8 1. 3, 4, 1 8, 0 8, / 6 1: 5, 1: 6, 8, 5 1: t
B 1: / 7. 2. 9 / e / 6, 2. 3. / S / 7 1 8, / 5 1 3. 6, 1. 7 / így?
Egy / 7 1 7, / 1, 1. 1, 1' 8, / 1: 4. / 7. 1: 6, 8, 1: t
[Closing]
9, 1' 3, 3. 1. / 7, 0 3, 1. 1 8 1. 8, / :1 3 3. 0, 9, 5, 1: 8, 8, 1: 5, / 2. 7, / 7,
0 7 / 2, 0 7 7 1. 5, / 8 1. 3, 1. 3 0 7
1 8 1' 3 0 / 7 1: 3 3. 1: 7, 1: 3 / 1' 3, 9 1' 3 / Mezőkövesd, / 1916 IIII 1
[Left margin, read with the card turned; inner row first, then the small dashed box]
6, 1 6, 2, / 1: / 3. 1. 5, 1. 8 1 / 1, 1. 6 0 3 / 8 1: 3, 8,
1' 5, 8 0 3 8, 1. 8 / 4 1: 5, 0, 5, 1: 3 / 2. 7, / 0 5. / 7. 0 8 0 3, :1 / 3. 0 5,
8, 1' 5,
[Top right corner, boxed]
1 3, 6 1' 5,
[PICTURE SIDE, along the long edge]
5, 1' 8, 0 3 / 8 1 5. 1: 6, / 7. 2. 9 / 1. / 9 1' 3, 0 7, / 2. 5, 1: 8,
0 5. 1. 6, 7 0 3, / 2. 3, 9, 1: 8 / 8 1. 4, 1. 8 / 1, 0 5, 3 0 4, 6, 1. 7 / 8 1 7 0
3,
1 4. / 3. 1: 5, 1: 3 / 5, 1: 5 1: 8, 1: 7 / 8, 1: / 6 0 / 7. 1 3. :1 / 1, 1. 1, :1
7,
```

## Plaintext (Hungarian, spelling as on the card)

Punctuation is mostly the writer's; line breaks in the prose and some full stops and capitals are editorial. The `)` marks are on the card. In the date no slash or full stop is on the card.

```text
Address side:

Édes Margitkám!
Vasárnap nem igen mehetek fel mert it [= itt] van egy kis dolgom pedig
édes anyámmal is akarnék már beszélni) hacsak lehet azért felmegyek)
most pedig irok egy kis verset

Margitkának hívnak téged
Aranyos vagy igazán —
Vedd e kártyát üdvözletül
S gondolj drága néha rám!

Fogadd ezt a kártyát s vele
üdvözletem Margitka.
Nyíljanak ki ablakodban
Piros rózsák hajnalra.

Hogy mit jelent az M betű?
Csak Margitot jelenthet!
Be szép e név! S kit hívnak így?
Egy kis babát egy szentet!

Zárva soraimat üdvözlettel és sok csókkal maradok
Imádó kedvesed) Árpád) Mezőkövesd, 1916 IIII 1

Left margin, written sideways, with the small dashed box:

Nincs e valami bajod mert álmodtam felőled és oly szomorú voltál.

Boxed in the top right corner: Írjál!

Picture side, along the long edge:

Látod milyen szép a páros élet.
Olyankor érzem magam boldognak mikor
így veled lehetek te jó szívű babus.
```

## English translation

Sweet Margitka! On Sunday I can hardly come up, because I have a little business here, and I would also like to speak with my mother at last; if it is at all possible I will come up anyway. And now I am writing a little verse.

They call you Margitka, / you are truly a darling. / Take this card as a greeting, / and think of me sometimes, dear!

Accept this card, and with it / my greeting, Margitka. / May red roses open / in your window by dawn.

What does the letter M mean? / It can only mean Margit! / How lovely this name is! And whom do they call so? / A little babe, a saint!

Closing my lines with greetings and many kisses, I remain your adoring sweetheart Árpád. Mezőkövesd, 1 April 1916.

Margin: Is something wrong with you? Because I dreamed about you and you were so sad.

Corner: Write!

Picture side: You see how beautiful life as a couple is. I feel happy at such times, when I can be with you like this, you good-hearted darling.

## Slovak translation

Moja sladká Margitka! V nedeľu asi nebudem môcť prísť hore, lebo tu mám nejakú robotu a aj s mamou by som sa už chcel porozprávať; ak to len trochu pôjde, predsa len prídem. A teraz ti píšem malý veršík.

Volajú ťa Margitka, / naozaj si zlatá. / Prijmi túto pohľadnicu ako pozdrav / a mysli na mňa, drahá, niekedy!

Prijmi túto pohľadnicu a s ňou / môj pozdrav, Margitka. / Nech ti v okne rozkvitnú / červené ruže do rána.

Čo znamená písmeno M? / Môže znamenať len Margitu! / Aké krásne je to meno! A koho tak volajú? / Malé dievčatko, svätú!

Končím svoje riadky s pozdravom a mnohými bozkami a zostávam tvoj zbožňujúci milý Árpád. Mezőkövesd, 1. apríla 1916.

Okraj: Nie je ti niečo? Lebo sa mi o tebe snívalo a bola si taká smutná.

Roh: Napíš!

Obrázková strana: Vidíš, aké krásne je žiť vo dvojici. Vtedy sa cítim šťastný, keď môžem byť takto s tebou, ty dobrosrdečná moja milá.

## Why the reading is believed

The whole card decodes with one fixed table, with no unknown sign and no word left over. The text is natural Hungarian of the period. All three verses scan 8/7/8/7 by the reviewer's count, and the rhymes hold (jelenthet / szentet, Margitka / hajnalra; igazán / rám is near). The writer's own clear letters confirm the cipher reading in mixed words: `jelenthe` plus a clear t, `szente` plus a clear t, and the clear "M betű" is answered by `Margitot`. Margitka is the addressee, and Árpád is the sender on the sister cards. The date agrees with the postmark, and the picture of a couple fits `páros élet`.

## What remains uncertain

No word is unread. These points rest partly on word sense or on editorial choice:

1. **bajod** (margin): the first sign is a tapered blot with a clear comma. Read `1,` b by sense; "valami bajod" is idiomatic and no other sign gives a word.
2. **mert** (margin): the last sign is a blot with a comma, on the frame line. Read `8,` t by sense.
3. **kedvesed** (closing): the third sign is a heavy closed 3 that could pass for 8 alone. 8 gives no word.
4. **babus** (picture side): one dot is seen left of the 1, where `:1` has two. The lower dot may be lost in the comma of the sign before it.
5. **látod** (picture side): the 0 is filled with ink.
6. **Írjál** (corner box): the second sign is pale with a large upper lobe that resembles 9, but `9,` gives no word. The comma is clear.
7. **rózsák**: the last 7 has no comma. The star below it is a drawing on the arrow line, separate from the 7. With a comma the word would be rózsás.
8. **Reading order of the margin** is by sense: inner row, outer row, then the small dashed box. Only this order gives a sentence, and box and margin share a dashed frame.
9. **Spellings**: `it` is one `8,`, normal form itt. `nincs e` is written as two words, normal form nincs-e.
10. **édes anyámmal** is taken as édesanyámmal, "with my mother", the writer's mother. It could mean "my dear mother" or, less likely, Margitka's mother. "hacsak lehet azért felmegyek" is colloquial.
11. **The date**: the month is four strokes between an over-line and an under-line, so IIII (April), not III. The postmark's year is not legible.
12. **Not text**: the feathered branch under verse 1 is a drawn ornament, and the small green 1315 and the green line near the left margin are printer's marks.

Not checked: whether the HistoCrypt article treats this card, and whether the verses are borrowed from a printed source.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) tried to refute the solution. It ran the command, wrote its own decoder from the table (same text, 556 signs, 31 distinct), reread the whole card against the transcription on its own crops, and checked each disclosed point on the pixels. It found no sign that differs apart from the blotted signs disclosed above. It also checked the translations. Verdict: **ACCEPT**, with three minor findings, all addressed:

1. The conflict over `5.` (ly here, l on HCP 1178 and 1179) was understated. It is now stated in full.
2. `9.` and `8.` are thinly attested. They are now named as such.
3. The date line was given as 1916. IIII/1, with punctuation that is not on the card. Rechecked on the crops; it is now given as 1916 IIII 1.

No word of the plaintext changed, and the date's meaning is the same. The reproduction command was re-run after the edit with the same counts.

## Credit

Transcription, key extension and decipherment by Claude Opus 5.5; the base key comes from Claude Opus 5.5's work on HCP 1174, 1178 and 1179. No earlier GPT work exists on this number.
