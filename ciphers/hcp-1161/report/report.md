# HCP 1161 (cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12): a troubled digit letter to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered in full (217 of 217 cipher signs, 4 of them read by sense); independent review 1 verdict REVISE, all findings addressed, no change to the decoded letters.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1161 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1161), portal name cpc_1915-12-18_HU_Mezokovesd_HU_Szomolya_szomolya-12, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), which was not consulted, so it is not known whether it discusses this card.

The card belongs to a series sent from Mezőkövesd to Szomolya in north-east Hungary during the First World War, in 1915 and 1916. It is addressed in a formal hand to Tek. Szépreményű Sziber Margitka kisasszonynak, (Borsod m.) Szomolya, u. p. Bogács. A pencil note at the foot gives 1915. XII/18 Mezőkövesd, which agrees with the portal's file name; it is in a smaller hand, and it may be the writer's or a later note. The postmark shows little beyond a 5. The picture side carries only a printed photograph, a publisher's mark and the number 3398/4, with no writing.

The message is Hungarian in pencil, part in open words and part in digits. The private passages are enciphered and the sentence runs straight across the changes. The signature is Árpád, as on sister cards.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

This is a known, transferred key, not a new key recovery. The Mezőkövesd family table comes from the finished sister cards hcp-1174, 1178, 1179 and 1170. No reading of this card was supplied or consulted.

The transcription was made by hand from the highest-resolution original available, enlarged 4 to 6 times. No OCR was used. Each sign is a digit with an optional mark, and the mark belongs to the sign. Spaces on the card divide words. A script (work/decode.py) checks the scan hashes, decodes every sign and asserts each word. To reproduce from the repository root:

```text
python3 -I ciphers/hcp-1161/work/decode.py
```

The open text is hard-coded in that script, so the command reproduces only the decoding of the cipher signs.

## Key

Monoalphabetic substitution, register label MASC. Each letter is one sign. The key does not separate o from ó or i from í on this card.

| Sign | Letter | Sign | Letter | Sign | Letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `5,` | l |
| `0,` | ö | `2.` | é | `6,` | n |
| `1` | i, í | `3` | d | `6.` | ny |
| `1.` | a | `3,` | r | `7` | k |
| `1:` | e | `3.` | v | `7,` | s |
| `1'` (single high dot) | á | `4,` | g | `7.` | sz |
| `.1` (dot left) | u | `4.` | gy | `8` | m |
| `-1` (dash or dot left) | ú | `5` | h | `8,` | t |
| `1,` | b | `9,` | z | | |

Nearly all signs are on hcp-1174. `1,` = b comes from hcp-1179, and `4.`, `6.` and `-1` from hcp-1170, where each had thin support; this card confirms them (hogy, anyám, úgy). `.1` = u is confirmed in tudom, kábulva and elutasítanál. `9,` = z gains its own word, Róza. Plain `9` = p is on hcp-1173 and 1174.

## Ciphertext

The 50 enciphered words in card order, with the reading of each. `?` marks a mark hidden under an ink blot.

```text
7 1: 3 3. 1: 7,                             Kedves
8 1' 3, 4, 1 8, 7 1' 8                      Márgitkám
2. 6,                                       én
1. 7. 8,                                    aszt
7, 1: 8                                     sem
8, .1 3 0 8                                 tudom
5 0 4.                                      hogy
8 1 8,                                      mit
1 3, 8, 1. 8                                írtam
1. 7 7 0 3,                                 akkor
-1 4.                                       úgy
1: 5,                                       el
3? 0 5, 8, 1. 8                             voltam
7 1' 1, .1 5, 3. 1.                         kábulva
6, 0                                        no
8, 1: 6, 6, 2. 8                            tenném
2. 3, 8, 1: 3                               érted
5 1.                                        ha
5 1 3 1: 4, 1: 6,                           hidegen
1: 5, .1 8, 1. 7, 1 8, 1. 6, 1' 5,          elutasítanál
1: 5, 3. 1 7, 1: 5, 6, 1                    elviselni
5 1 7.                                      hisz
1 4,                                        így
7, 1 6, 2,                                  sincs
7, 1: 6, 7 1                                senki
5 1' 8,                                     hát
-1 4?                                       úgy
8 1: 4,                                     meg
7 1                                         ki
3. 0 5, 6, 1.                               volna
5 1.                                        ha
8, 1:                                       te
7, 1:                                       se
3. 0 5, 6, 1' 5,                            volnál
8 1' 3,                                     már
8 0 7, 8,                                   most
1 7,                                        is
2. 3 1: 7,                                  édes
1. 6. 1' 8                                  anyám
1 7,                                        is
8 1: 4,                                     meg
3, 0 9, 1.                                  Róza
1 7,                                        is
1 3, 8, 1. 7                                írtak
8 1' 7, 6, 1. 7                             másnak
7. 1' 8 8, 1. 5, 1. 6, 7. 0 3,              számtalanszor
0, 5, 1: 5, 5, 1: 7                         ölellek
2. 7,                                       és
2, 0 7 0 5, 5, 1. 7                         csókollak
1' 3, 9, 1' 3                               Árpád
```

## Plaintext

Hungarian; square brackets mark what is enciphered on the card.

[Kedves Márgitkám]!

Lapodat megkaptam melynek nagyon örvendek nem tudom micsoda borzasztóságot írsz, hogy volt aba a levélbe [én aszt sem tudom hogy mit írtam akkor úgy el voltam kábulva no] de az se-mi én azt bár mikor meg[tenném érted ha hidegen elutasítanál] mer én azt nem tudnám [elviselni hisz így sincs senki hát úgy meg ki volna ha te se volnál már most is édes anyám is meg Róza is írtak másnak] és én még már két lapot írtam nekik és ma se kapok választ.

[számtalanszor ölellek és csókollak] ([Árpád])

1915. XII/18 Mezőkövesd.

Spellings as written: `Márgitkám` (normally Margitkám), `aszt` (azt), `se-mi` across a line break (semmi), `mer` (mert), `aba` (abba, colloquial for abban), `bár mikor` (bármikor), `tud nám` in two parts (tudnám). Open `meg` joins cipher `tenném`.

## English translation

[Dear Margitka]! I received your card, which I am very glad of. I do not know what dreadful thing you are writing about, that was in that letter; [I do not even know what I wrote, I was so dazed then, well,] but that is nothing, I would do it [for you] any time [if you coldly rejected me], because I could not [bear it. After all, even so there is no one, so who would there be if you were no longer there. Now too my dear mother and Róza have written to others,] and I have even written them two cards already, and even today I get no reply.

[Countless times I embrace you and kiss you] ([Árpád])

1915, 18 December, Mezőkövesd.

## Slovak translation

[Drahá Margitka]! Dostal som tvoj lístok, ktorému sa veľmi teším. Neviem, akú hroznú vec píšeš, že bola v tom liste; [ja ani neviem, čo som napísal, tak som bol vtedy omámený, no] ale to nič, ja by som to [pre teba] kedykoľvek [urobil, keby si ma chladne odmietla], lebo ja by som to nedokázal [zniesť. Veď aj tak nikoho nemám, kto by teda bol, keby si už nebola ani ty. Aj teraz moja drahá matka aj Róza písali iným,] a ja som im dokonca už napísal dva lístky a ani dnes nedostávam odpoveď.

[Nespočetnekrát ťa objímam a bozkávam] ([Árpád])

1915, 18. december, Mezőkövesd.

## Uncertainties

Of 217 signs, 213 decode by the table as written. Four rest on sense:

- `így`: the mark after the 4 is a short tick, nearer a comma than a dot, so the table alone gives g. `hisz így sincs senki` fixes gy.
- `úgy` (second one, before `meg ki volna`): an ink blot with a tail running lower left covers the mark of the 4. The mark is unreadable, and gy rests purely on word sense.
- `voltam` (first one): a blot of the same kind covers the mark of the 3. The mark is unreadable, and v rests purely on word sense.
- `Árpád`: the 9 has a clear comma, so the table alone gives Árzád. This is taken as the writer's slip, and the name as certain from the sister cards.

Smaller points:

- In both `úgy` the left mark of the 1 is read as `-1`. `így` would also make sense in the second, but the mark is present.
- `Róza` is read as a name from `meg Róza is`. Who she is, is not known.
- "Wrote to others (not to me)" for `írtak másnak` is an understanding of the context; the words themselves are clean.
- `azt` in `én azt bár mikor megtenném` ("I would do it any time") has no stated object on this card. What he would do remains unexplained. The words are read; the reference is not.
- The open word `aba` stands right at the margin rule with ink spread around its last letter; the three letters are legible.
- The postmark is unusable beyond a 5, and the hand of the pencil date is unsettled.

Why the reading is secure: a key established on other cards decodes 213 of 217 signs as written into 50 Hungarian words with no gaps; long clean words such as `elutasítanál`, `számtalanszor`, `elviselni` and `hidegen` leave no freedom; the grammar runs across open and cipher boundaries (open `meg` + cipher `tenném`, open `nem tudnám` + cipher `elviselni`); and the closing words match hcp-1174.

## Review summary

An independent Claude Opus 5.5 reviewer ran the command, typed all 217 signs row by row from its own 4x to 6x crops, and decoded them with its own script and its own statement of the key. It found no difference in any position. Its verdict was **REVISE**, with five findings:

- **Major, fixed:** the open word `aba` after `volt` was missing from the transcription, which made the claim of "no unread word" false. It was added to the plaintext, script and translations. The solver then re-read every open row and found no other omission.
- **Minor, fixed:** the low dot near `kábulva` had been called stray. It is the i-dot of the open `mi` in the next row, so the sign is a clean `1'`. The count moved from 212 and 5 to 213 and 4.
- **Minor, fixed:** the two blot restorations claimed a dot that cannot be seen; they now say the mark is unreadable.
- **Minor, fixed:** the translations dropped `még` ("even").
- **Minor, fixed:** `.1` = u was wrongly called new; it was already on hcp-1135, hcp-1160 and hcp-1172.

The decoded letters did not change.

![The missed open word: "hogy volt aba", at the margin rule (review/work/o6b.png)](../review/work/o6b.png)

The reviewer could not verify the postmark, the hand of the date line or the contents of the HistoCrypt article.

![The low dot above the i of open "mi", beneath kábulva (review/work/kab.png)](../review/work/kab.png)
