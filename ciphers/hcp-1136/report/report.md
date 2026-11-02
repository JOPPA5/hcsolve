# HCP 1136 (cpc_1916-03-24_HU_Mezokovesd_HU_Szomolya_szomolya-24): a love verse in digits on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: all 291 cipher signs are deciphered (289 by the key as written, 2 by word sense, each alone inside a clear word); independent review 1 verdict ACCEPT, no sign value or word changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1136 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1136), portal name cpc_1916-03-24_HU_Mezokovesd_HU_Szomolya_szomolya-24, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not read** for this card, so "no published solution found" means only that the portal attaches none. The whole reading here was made from the card.

The card was sent in wartime, from Mezőkövesd to the village of Szomolya in north-east Hungary. It is dated in clear **Mezőkövesd, 1916. III/24.** The postmark shows Mezőkövesd, year 916 and day 24; the month is damaged and is consistent with MÁR. The address is in clear: **Őnsg. / Szépreményű / Sziber Margitka / kisasszonynak / Szomolya / (Borsod m.) u. p. Bogács**, "To the promising young lady Margitka Sziber, Szomolya, post office Bogács". Őnsg. is an abbreviated title, read as written.

The card belongs to a correspondence with Margitka Sziber in the same digit cipher (hcp-1174, 1178, 1179 and others). Unlike those sisters, where only key words are enciphered inside open Hungarian, here almost the whole message is in cipher. Only the address, the date and a few letters at the beginning and end of verse lines are in clear. The sender signs as Árpád, as on hcp-1174. Nothing more is known about him. The picture side shows a couple with flowers and has no writing.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, sign by sign, from the un-converted high-resolution scan, enlarged. No OCR was used.

The key was **transferred**, not recovered from nothing: the starting point was the table of the finished card hcp-1174, with `1,` = b from hcp-1179. A sign is a digit plus its mark, so a comma, a dot or a colon belongs to the sign and is not punctuation. The first test word, `8 0 7, 8,` = most, read at once, and so did the opening `Édes Margitkám!`, the same 13 signs as on hcp-1174.

Four signs were new and were fixed on this card:

- `6` = j, by majd (twice), Minjárt, átadják
- `4.` = gy, by hogy, megyek, egy. In hogy and megyek the mark is a short dash, in egy a dot.
- `4` = f, by fel only
- `6.` = ny, by annyi only

No value of the key on the finished cards hcp-1174, 1178, 1179 had to be changed. The card has 291 cipher signs of 28 kinds and 21 letters in clear.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1136/work/decode.py`. It checks the scan hashes, decodes every sign and asserts each line against the stated reading. The address and date are hard-coded there.

## Key

Monoalphabetic substitution (MASC), one sign per letter or Hungarian digraph. The writer leaves spaces between words. The cipher does not distinguish o from ó, ö from ő, i from í or ü from ű, but it has separate signs for a and á and for e and é. Signs marked with a star are new to this card.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2,` | cs | `5,` | l |
| `0,` | ö, ő | `2.` | é | `6` (star) | j |
| `1` | i, í | `3` | d | `6,` | n |
| `1.` | a | `3,` | r | `6.` (star) | ny |
| `1:` | e | `3.` | v | `7` | k |
| `1'` (high dot) | á | `4` (star) | f | `7,` | s |
| `:1` (dots at left) | ü, ű | `4,` | g | `7.` | sz |
| `1,` | b | `4.` (star) | gy | `8` | m |
| `9` | p | `5` | h | `8,` | t |
| `9,` | z | | | | |

## Ciphertext

Transcription line by line. Words are separated by `/`, and `=x` is a letter in clear. Square brackets mark the two signs read by sense.

```text
2. 3 1: 7, / 8 1. 3, 4, 1 8, 7 1' 8
8 0 7, 8, / 7 :1 5, 0, 6, 0, 7, / 1 3, 6, 1 / 3. 1. 5, 0 8
6, 1 6, 2, / 2, 1. 7 / 1. 6, 6. 1 / 5 0 4. / 7. 0 8 1, 1. 8, 0 6,
4 1: 5, / 8 1: 4. 1: 7 / 2. 7, / 1. 7 7 0 3, / 8 1. 6 3
7 1: 8, 1: 2, 7 2. 6, / 7, 0 7 1. 8, / 1, 1: 7. 2. 5, 4, 1: 8, :1 6, 7
1. 3 3 1 4, / 1 7, / 1 3, 0 7 / 1: 4. / 7 1 7, / 3. 1: 3, 7, 1: 8,
=M 1 7 0 3, / 1: 9, 8, / 1. / 5, 1. 9 0 8
=H 1 3, 8, 1: 5, 1: 6, / 8 1: 4, 5, 1' 8, 8, 1. =m
=G =o 6, 3 0 5, 1. 8, 1, 1. / 2. 3 1: 7,
=M 1 6, 6 1' 3, 8, / 6, 1: 7 1: 3 / 7. 1' 6, 8, 1. =m
=G =o =n 3 0 5, 8, 1. 8 / 8 1. 6 3 / 0, 3, :1 5, [7.]
=H =a / 1' 8, 1. 3 6 1' 7 / 6, 1: 7 1: 3
=S / 3. 2. 4, 8, 1: 5, 1: 6, / 1, 0 5, 3 0 4, 7, 1' 4,
=F =o =g =t =a / =e =l / 7. 1 3. 1: 8 1: =t
:1 3 3. 0, 9, 0, 5, 3. 1: / 0, 5, 1: 5, 2. 7, 7, 1: 5,
2. 7, / 7, 0 7 / 2, 0 7 7 1. 5, / 8 1. 3, 1. 3 [0] 7
7. 1: 3, 1: 8, 0, / 7 1: 3 3. 1: 7, 1: 3 / 2. 7,
5 :1 / 1 8 1' 3 0 3 / 1' 3, 9 1' 3
```

## Plaintext

Spelling as written. The long vowels ó, ő, í, ű are restored from the sense, because the cipher does not mark them. Punctuation is the editor's, because a comma on the card is part of a sign. `ketecskén` (standard kettecskén), `Minjárt` (mindjárt) and `Gondolatba` (gondolatban) are the writer's forms.

```text
Édes Margitkám!
Most különös írni valóm nincs, csak annyi, hogy szombaton
fel megyek és akkor majd ketecskén sokat beszélgetünk.
Addig is írok egy kis verset.

I
Mikor ezt a lapom
Hirtelen megláttam,
Gondolatba édes
Minjárt neked szántam.

II
Gondoltam — majd örülsz,
Ha átadják neked,
S végtelen boldogság
Fogta el szívemet.

Üdvözölve öleléssel és sok csókkal maradok
szerető kedvesed és hű imádód (Árpád)

Mezőkövesd, 1916. III/24.
```

## English translation

Sweet Margitka of mine!
I have nothing special to write now, only that on Saturday I am coming up, and then the two of us will have a long talk. Until then I am writing a little verse.

I. When I suddenly saw this card of mine, in my thoughts, sweet one, I at once meant it for you.

II. I thought: how glad you will be when they hand it to you, and endless happiness seized my heart.

Greeting you with an embrace and many kisses, I remain your loving sweetheart and faithful adorer (Árpád)

Mezőkövesd, 24 March 1916.

## Slovak translation

Moja sladká Margitka!
Teraz ti nemám čo zvláštne napísať, len toľko, že v sobotu prídem hore a potom sa spolu vo dvojici veľa pozhovárame. Dovtedy ti píšem malý verš.

I. Keď som zrazu uvidel túto svoju pohľadnicu, v myšlienkach, moja sladká, som ti ju hneď určil.

II. Pomyslel som si: ako sa potešíš, keď ti ju odovzdajú, a nekonečné šťastie sa zmocnilo môjho srdca.

S pozdravom, objatím a mnohými bozkami zostávam tvoj milujúci milý a verný ctiteľ (Árpád)

Mezőkövesd, 24. marca 1916.

## Why the reading is believed correct

- A key built on other cards (24 of the 28 kinds of sign here) decodes the card into continuous Hungarian without any change of value.
- The text is coherent: a short note announcing a Saturday visit, an announced verse (`egy kis verset`) that then follows, and a closing formula.
- The verse has two numbered stanzas, rhymes (megláttam / szántam, neked / szívemet), and **each of the 8 lines has exactly 6 syllables**, for example Hir-te-len meg-lát-tam. The reading was not built to fit this, so it is a strong independent check. An arbitrary reading would not scan.
- The letters in clear join the decoded signs into words: `=M 1 7 0 3,` Mikor, `=H 1 3, 8, ...` Hirtelen, `=F =o =g =t =a` Fogta.
- The signature decodes to Árpád, as on hcp-1174; it was decoded, not assumed.

## What remains uncertain

1. **örülsz, last sign.** After the l stands a cancelled, cross-hatched blot, then a clear 7 with a comma-shaped mark at its lower right that has two small ticks. As drawn it is nearer `7,` (s) than `7.` (sz). It is read as sz by sense (`majd örülsz`, "you will be glad"). The word is not in doubt.
2. **maradok, the o.** The sign is a filled slanted blob with a small light gap at the foot, not readable as any sign. The o is a restoration by sense from the normal close `csókkal maradok`, "I remain".
3. **megláttam, the end.** After `1.` stands an inked-over shape that in form is a figure 8, so it looks like the cipher sign `8` = m, followed by cursive m strokes in clear. The likely account is that the writer put the cipher m and then wrote over or beside it in clear, but others are possible. One m results either way, and the word does not change.
4. **Dot height on á.** In imádód and the second á of Árpád the dot stands about two thirds up the stem and is classed as high. Read as `1.` the words would only lose the accent.
5. **The first sign of imádód** is slightly blurred; no dot is seen.
6. **A stray closing bracket.** On the card a `)` stands directly after imádód, before `(Árpád)`, with no opening bracket before it. It has no letter value and the plaintext leaves it out.
7. **`4` and `6.` occur once each** on this card (fel, annyi), and both are secure from sense. Their other attestation, on hcp-1143, has the same solver and date, so it is not independent.

The identity of Árpád and which Saturday is meant are not known. 24 March 1916 was a Friday, so it may be the next day or a later Saturday.

![The cancelled blot, the 7 and its mark at the end of örülsz (review/work/z_blot.png)](../review/work/z_blot.png)

![The end of megláttam: 1., the inked-over 8, the m strokes in clear and the hook (review/work/z_tam.png)](../review/work/z_tam.png)

## Review

An independent reviewer (a separate Claude Opus 5.5 agent) ran the command, decoded the card with its own script and its own statement of the key (326 letters, identical), and read all 18 lines sign by sign from its own enlargements of the high-resolution scan. It found no disagreement in any sign value. It also noted the 6-syllable metre. Verdict: **ACCEPT**, with four minor points, all taken over. **No sign value and no word of the plaintext changed.**

1. The stray `)` after imádód had not been disclosed. It now is.
2. `4` = f had been credited to the unfinished analysis of hcp-1175, whose notes do not say that. The value now rests on `fel` on this card alone.
3. The end of megláttam was under-described. It is now described as above.
4. The metre was added to the argument for the reading.
