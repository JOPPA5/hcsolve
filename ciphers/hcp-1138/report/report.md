# HCP 1138: Árpád writes to Margitka in a digit cipher, Mezőkövesd, 17 March 1916

Human solver: Tomáš Pavuk

**Status: deciphered in full (409 of 409 cipher signs, 84 words, no unread word or clause); review 1 and review 2 both REVISE, all findings addressed, no further round needed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1138 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1138), portal name cpc_1916-03-17_HU_Mezokovesd_HU_Szomolya_szomolya-23, from Tobias Schrödel's collection of cryptographic postcards. When it was captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article, which was not read for this work. No published solution of this card was seen.

The card is a picture postcard with printed roses, signed C. Klein; nothing is written on the picture side. On the address side, turned about 50 degrees so that the rows run level, the left half holds the message in digits with marks. The only writing in clear there is `Kívánom:` ("I wish:"), the place and date `Mezőkövesd, 1916. III/17.`, and the address: `Őnagysága. / Rózsareményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács / Borsod m.` ("To her ladyship, Miss Margitka Sziber of rosy promise, Szomolya, post office Bogács, Borsod county"). A 5-fillér stamp carries a postmark partly hidden under it; it agrees with the written date as far as it can be read, which is a weak check.

The card is one of a series from Mezőkövesd to Margitka Sziber in Szomolya, 1915 to 1916, in Hungarian. The writer signs Árpád in cipher, here as on HCP 1174. A digit-plus-mark key for the series was reconstructed earlier on HCP 1174, 1178 and 1179. All of those solutions are the work of the same AI model as this one.

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side as scanned (source/address-large.jpg)](../source/address-large.jpg)

![Address side rotated so the rows run level, from the high-resolution original (report/address-level.jpg, reduced from work/crops/full51.png)](address-level.jpg)

## Method

The transcription is manual, made from the un-converted high-resolution scan, rotated and enlarged 3x to 5x. A sign is a digit plus a mark. The commonest mark is a comma: a long stroke running down-left from under the digit, often into the next row. That is the main trap on this card, because the strokes look as if they belong to the row below. Word divisions are not shown in the digits with any reliability, so they are the solver's.

Key recovery: `Édes Margitkám!` opens the card with the same 13 signs as HCP 1174, and the family table then gives most of the text. The remaining signs came from words on this card and recur: `6` = j in szedjétek, hagyjatok, jó, jól, teljen, május, tolmácsolja; `6.` = ny in nyugott, hernyót; `4.` = gy in hogy, úgy, vagyok, ángyika, hagyjatok; `.1` = u in úgy, rosszul, nyugott, május, kapuba. `2` = c occurs once (lehec). `8.` = ty also occurs once here, in `kártyámon`; it rests on that word, on the dot pattern (a dot gives the palatal partner: g and gy, n and ny, t and ty) and on FINAL sister cards HCP 1142 (`kártyán`), 1146 (`kártya`) and 1164 (`kártyát`).

## Key

Monoalphabetic substitution, register type MASC. Each sign stands for one Hungarian letter or digraph; i/í, o/ó, ö/ő and u/ú share a sign, while a and á, e and é have separate signs.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2.` | é | `6` | j |
| `0,` | ö, ő | `2` | c | `6,` | n |
| `1` | i, í | `3` | d | `6.` | ny |
| `1.` | a | `3,` | r | `7` | k |
| `1:` | e | `3.` | v | `7,` | s |
| `1'` (high dot) | á | `4` | f | `7.` | sz |
| `.1` (dot to the left) | u, ú | `4,` | g | `8` | m |
| `:1` (dots to the left) | ü | `4.` | gy | `8,` | t |
| `1,` | b | `5` | h | `8.` | ty |
| `2,` | cs | `5,` | l | `9` | p |
| | | | | `9,` | z |

Three plain 9s are read as z, against the table; see Uncertainties.

## Ciphertext

Signs as transcribed, in reading order; `/` separates the words as divided by the solver. The card has no such separators.

```text
2. 3 1: 7, / 8 1. 3, 4, 1 8, 7 1' 8
2. 3, 8, 1: 7, 1 8, 5, 1: 7 / 5 0 4. / 8 1' 6 .1 7, 1, 1. / 4 0 4, 6, 1. 7
7, 0 3, 0 9, 6, 1 / 3 1: / 2, 1. 7 / 1. 9 0 7 1. 8, / 1. 7 1 7 / 8 2. 4, / 6, 1: 8
3. 0 5, 8, 1. 7 / 7, 0 3, / 1. 5, 1. 8, 8, / 8, 1: 5 1' 8, / 8 0 7, 8, / 8 1' 3,
6. .1 4, 0 8, 8, / 5, 1: 5 1: 2 / 2. 3 1: 7, / 3 1: / 8 0 7, 8, / 8 1' 3, / 6, 1:
7. 1: 3 6 2. 8, 1: 7 / 5, 1: / 1. / 5 1: 3, 6. 0 8, / 5 1. 4. 6 1. 8, 0 7 / .1 4.
8 1 6, 3 1: 6, 8, / 1. 9 8, 1' 6, / .1 4. / 3. 0 5, 6, 1. / 6 0 / 7 1: 3. 1: 7, 1: 8
5 1. / 8 1' 3, / 8 0 7, 8, 1. 6, 1' 1, 1. / 5, 1: 6 0, 6, 6, 1: / 1' 6, 4. 1 7 1.
5 1' 9 1. 8, / 6, 2. 9, 6, 1 / 5 0 4. / 1. 7 7 0 3, 3, 1. / 5, 1: 6, 6, 1: / 3 1:
8 0 7, 8, / 8, 0, 1, 1, 1: 8, / 6, 1: 8 / 1 3, 0 7 / 8 1: 3, 8, / 3, 0 7, 7. .1 5,
3. 1. 4. 0 7 / .1 4. / 3. 1: 7. 1: 8 / 2. 7. 3, 1: / 0 8, 8, / 1. / 7 1. 9 .1 1, 1.
1. 5, 1. 9 0 7, 1. 6, / 8 1: 4, 4 1' 9, 8, 1. 8
7 1' 3, 8. 1' 8 0 6, / 1: / 7 1 7, / 3. 1 3, 1' 4, / 8, 0 5, 8 1' 2, 0 5, 6 1.
2. 3, 9, 1: 5, 8 1: 8
(clear) Kívánom:
8 1 6, 3 1: 6, / 0 3, 1' 3 / 1. / 8, 1' 3. 0 5, 1, 1. 6, / 6 0 5, / 8, 1: 5, 6 1: 6,
8 0 7, 8, / :1 3 3. 0, 9, 0, 5, / 2. 7, / 7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, / 2, 0 7 0 5,
7. 1: 3, 1: 8, 0, / 7 1: 3 3. 1: 7, 1: 3 / 1' 3, 9 1' 3
(clear) Mezőkövesd, 1916. III/17.
```

## Plaintext

Hungarian, spelling as on the card. Everything is enciphered except `Kívánom:`, the place and the date. Capitals and punctuation are editorial. The `)` signs are the writer's, and close phrases with no opening bracket.

**Édes Margitkám!**

**Értesítlek hogy májusba fognak sorozni de csak azokat akik még nem voltak sor alatt tehát most már nyugott lehec édes de most már ne szedjétek le a hernyót hagyjatok úgy mindent) aztán úgy volna jó ke(d)vesem ha már mostanába lejönne ángyika házat nézni hogy akkorra lenne) de most többet nem írok mert rosszul vagyok úgy veszem észre ott a kapuba alaposan megfáztam)**

**Kártyámon e kis virág tolmácsolja érzelmem**

**Kívánom: minden órád a távolban jól teljen!**

**Most üdvözöl és számtalanszor csókol szerető kedvesed (Árpád)**

**Mezőkövesd, 1916. III/17.**

Normal spelling of the odd forms: nyugott = nyugodt, lehec = lehetsz, ke(d)vesem = kedvesem (the d is not written), mostanába = mostanában, kapuba = kapuban (the same dropped n).

English translation:

Sweet Margitka! I inform you that they will recruit in May, but only those who have not yet been in the ranks, so now you can be at ease, sweet. But now do not pick off the caterpillars any more, leave everything as it is. Then it would be good, my darling, if ángyika (an aunt, or a sister-in-law by marriage) came down soon to look at a house, so that by then there would be one(?, the subject is unstated). But now I will not write more, because I am unwell; as I notice, I caught a bad cold there at the gate.

On my card this little flower interprets my feelings.

I wish: may every hour of yours go well in the distance!

Now your loving sweetheart greets you and kisses you countless times (Árpád)

Mezőkövesd, 17 March 1916.

Slovak translation:

Sladká Margitka! Oznamujem ti, že v máji budú odvádzať, ale len tých, čo ešte neboli na vojne, takže teraz už môžeš byť pokojná, sladká. Ale teraz už nezbierajte húsenice, nechajte všetko tak. Potom by bolo dobre, moja milá, keby už v týchto dňoch prišla dolu ángyika (teta alebo švagriná cez manželstvo) pozrieť dom, aby dovtedy nejaký bol(?, podmet nie je uvedený). Ale teraz už viac nepíšem, lebo mi je zle; ako pozorujem, tam pri bráne som sa poriadne prechladil.

Na mojej pohľadnici tento kvietok tlmočí moje city.

Želám si: nech ti každá hodina v diaľke plynie dobre!

Teraz ťa pozdravuje a nespočetnekrát bozkáva tvoj milujúci milý (Árpád)

Mezőkövesd, 17. marca 1916.

Notes on the reading: `sor alatt` is the idiom for military service. Removing caterpillar nests is an early spring job, which fits the date. The `kis virág`, the little flower, is the printed rose on the picture side. The call-up in May for men not yet served fits March 1916, a young man reassuring his girl.

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1138/work/decode.py
```

The script uses only the standard library. It checks the SHA-256 hashes of the four scan files, decodes every sign of work/transcription.txt, asserts each word against the reading column, and prints the text from those words. The expected summary is `cipher signs: 409 in 84 words, 32 distinct; 3 plain 9 used as z (no comma); 1 8. = ty`. It does not read the image: the transcription step is manual, and it was checked independently in review. Lines marked open, and the address, are clear text, read and not decoded.

## Uncertainties

- **Plain 9 as z, by word sense, three times:** `azokat`, `aztán`, `házat`. No comma was found at any of the three on enlargement, by solver or reviewer. The table would give `apokat`, `aptán`, `hápat`, which are not words. The same card has 9 = p in `alaposan`, `kapuba` and `Árpád`, and the comma form in sorozni, nézni, üdvözöl, érzelmem, megfáztam. The writer seems to have dropped the comma.
- **A grey dot on the first 7 of `akkorra`.** It sits where the dot of `7.` (sz) sits, which would give `aszkorra`, no word. It is paler than the writer's dots and has a thin trail to the row below, so it is read as a smear and the sign as plain 7. This rests on word sense. Whether the mark is the writer's ink cannot be settled from the scan.
- **`akkorra lenne`:** the words are clear, but the subject is unstated. The house is the likely subject. "By then" probably means May, which is an inference.
- **`lehec`** rests on one `2` with no mark, read as a phonetic spelling of `lehetsz`. If a comma was dropped it would be `lehecs`, the same word.
- **`ke(d)vesem`:** the d is missing on the card; `kedvesed` is spelt fully in the signature. Taken as a slip.
- **Blot at the end of row 2**, after `8 1'`. `május` reads through it, with `6 .1 7,` at the start of the next row. It is most likely a heavy row-end dash; rows 7, 10 and 11 end in a thin dash of the same shape. Nothing is restored. If a sign is hidden there, the word is not `május`. The writer's dashes are loose in any case: rows 7 and 10 have them after complete words.
- **`8.` = ty** occurs once on this card; see Method.
- **Small marks:** a stray dot low left of the 1 in `már` (row 6), taken as a slip; the `7,` in `alaposan` is blotted with a blue overstroke, though its comma is clear; a small `:` with a curved rule and a dot after `megfáztam)` is not decoded; a violet pencil mark near row 12 is a later addition.
- **Who and why:** who `ángyika` is on this card, and why he stood at a gate (`ott a kapuba`), are not stated. The gloss of `ángyika` is the usual meaning of the word. Guard duty would fit the gate but is not on the card, and is not claimed.
- **Transcription checks were not blind.** The reviewer's sign-by-sign readings were made with knowledge of the solver's text, so an error shared by both is unlikely but possible.
- **`Rózsareményű`** in the address is taken as a playful title; HCP 1174 has `Szépreményű`.
- The HistoCrypt article linked by the portal was not read, so a reading of this card there cannot be excluded.

## Review summary

Two rounds of independent review by a separate Claude Opus 5.5 agent, both REVISE.

Round 1 found ten faults, and they were serious. The solver had worked from a truncated rotated image and took its diagonal cut for the card edge, so 12 signs at the ends of rows 9, 10 and 11 were missed. Corrected as a result: `oba` became `kapuba` ("at the gate"); `többe` without `nem` became `többet nem`, which reversed a clause to "I will not write more"; `házi` became `házat` ("a house"). Also fixed: `hejönne` to `lejönne`, `tolmácsolna` to `tolmácsolja`, `kártámon` to `kártyámon` with `8.` = ty, and `üdvözölés` to `üdvözöl és`. The command was changed to print the text from the decoded words, and line-end dashes were disclosed. Those changes were substantial, so the card went back for a second review.

Round 2 made its own level rotation, went through all 20 rows sign by sign, and decoded with its own table and own word divisions: all 409 signs agree. It found one real error that both sides had missed: `akkor ra` is one word, `akkorra`, "by then". That was the solver's false word break, and it removed the last clause previously marked as obscure. It also found the undisclosed grey dot on that word, an awkward Slovak word (`vzdialene`, now `v diaľke`), and the word counts to update (85 to 84). All four were accepted. No sign or key value changed in round 2. The reviewer judged no further round necessary, and the solver agreed.

The transcription, key extension, decipherment and this report are by Claude Opus 5.5. No earlier work exists on this number.

## Sources

- HC Portal record 1138, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1138 (source/metadata.md).
- Scans: https://api.hcportal.eu/media/3474/ (picture side) and https://api.hcportal.eu/media/3475/ (address side), in converted and original forms; the file names and hashes are in SOURCES.md.
- Key family: ciphers/hcp-1174, hcp-1178, hcp-1179; for `8.`: ciphers/hcp-1142, hcp-1146, hcp-1164.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked by the orchestrator on 2026-11-02: no record for this card.
