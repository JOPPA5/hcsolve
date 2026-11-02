# HCP 1148 (cpc_1916-05-09_HU_Mezokovesd_HU_Szomolya_szomolya-34): Árpád's digit-cipher card about a muddy walk home

Human solver: Tomáš Pavuk

**Status: deciphered in full (415 of 415 cipher signs; 412 by the key as written, 3 by word sense). Independent review 1 verdict REVISE, findings addressed, story and key values unchanged.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1148 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1148), portal name cpc_1916-05-09_HU_Mezokovesd_HU_Szomolya_szomolya-34, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. The whole reading here was made from the card.

The card was sent in wartime Hungary, from Mezőkövesd to the village of Szomolya in Borsod county, and is dated in clear **Mezőkövesd 1916. V/9**, 9 May 1916. That agrees with the date in the portal's file name. The postmark is too fragmentary to confirm it. The address is open: **Tek. Sziber Margitka Kisasszonynak, Borsodm., Szomolya, u.p. Bogács** ("To the esteemed Miss Margitka Sziber, Borsod county, Szomolya, post office Bogács").

The picture side is a tinted landscape with a stream and trees, scanned sideways, and has no writing. On the address side, 415 digit signs fill the left half in three blocks: a letter, a four-line verse ruled off above and below, and a closing. Apart from the place and date, the whole message is enciphered.

The card belongs to the Mezőkövesd group (hcp-1135 to 1179), a correspondence to Margitka Sziber in 1915 and 1916. Other cards in the group use the same cipher and are signed Árpád.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, made sign by sign from the un-converted high-resolution scan enlarged 1.6 to 5 times. No OCR was used.

The key was not recovered from scratch. It started from the digit-plus-mark key of the finished cards hcp-1174, 1178 and 1179, in which a digit and its mark form one sign. The first 13 signs repeat the heading `Édes Margitkám` of hcp-1174 sign for sign. The opening words of this card then read directly, and the unknown signs followed from plain words: `félhatra` confirmed `4` = f, and `egy`, `nagy`, `hogy` gave `4.` = gy. Likewise `rajta`, `jól` gave `6` = j, `annyi` gave `6.` = ny, and `cipőnk`, `arcod` gave `2` = c. The review added `.1` = u as a separate sign (see below).

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1148/work/decode.py`. It checks the scan hashes, decodes every sign of `work/transcription.txt` through the key, stops if a word does not match its stated reading, and prints the text and the sign frequencies. The place, date and address are hard-coded there. The word divisions are editorial, as the card has none.

## Key

Monoalphabetic substitution (MASC), with one sign per letter, or per digraph for cs, sz, gy and ny. There are no word divisions, and vowel length is not marked for i and o. All 30 signs occur on this card.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `1` | i, í | `2,` | cs | `6` | j (new) |
| `1.` | a | `2.` | é | `6,` | n |
| `1:` | e | `3` | d | `6.` | ny (new) |
| `1'` (high dot) | á | `3,` | r | `7` | k |
| `:1` (two dots left) | ü | `3.` | v | `7,` | s |
| `.1` (one dot left) | u, ú; also ü, ű (new) | `4` | f | `7.` | sz |
| `1,` | b | `4,` | g | `8` | m |
| `0` | o, ó | `4.` | gy (new) | `8,` | t |
| `0,` | ö, ő | `5` | h | `9` | p |
| `2` | c (new) | `5,` | l | `9,` | z |

"New" means not in hcp-1174, 1178 or 1179, the cards the key was taken from. `.1`, `4.`, `6`, `6.` and `2` also stand on other cards of the group. On this card the writer usually separates a plain 1 from a crossed 7: a 7-shaped sign with no bar is `1`, and only the barred one is `7`.

Frequency of each sign (415 in all): `.1` 9, `0` 25, `0,` 7, `1` 10, `1'` 15, `1,` 6, `1.` 30, `1:` 47, `2` 2, `2,` 5, `2.` 16, `3` 12, `3,` 27, `3.` 9, `4` 1, `4,` 7, `4.` 9, `5` 10, `5,` 24, `6` 2, `6,` 22, `6.` 1, `7` 16, `7,` 16, `7.` 7, `8` 27, `8,` 42, `9` 3, `9,` 5, `:1` 3.

## Ciphertext

Sign groups as transcribed, one card line per row. The card has no spaces between words; a space here separates signs, and `|` separates the editor's words.

```text
01 2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
02 7. 1: 3, 1: 6, 2, 2. 7, 1: 6, | 5 1. 9, 1. 2. 3, 8, :1 6, 7 | 5 1' 3, 0 8 0 3, 1. 7 0 3,
03 1 6, 3 .1 5, 8, .1 6, 7 | 2. 7, | 4 2. 5, 5 1. 8, 3, 1. | 2. 3, 8, :1 6, 7 | 5, 1: | 6, 1. 4. 0 6,
04 7, 0, 8, 2. 8, | 3. 0 5, 8, | 2. 7, | 6, 1. 4. | 7, 1' 3, | 1. | 6, 1. 3 3, 1' 4, .1 6, 7 | 8, 2. 3,
05 3 1 4, | 5, 1: 8, 8, | 3. 1 9, 1: 7, | 1. | 2 1 9 0, 6, 7
06 8 1: 4, | 1: 4, 2. 7. | 1: 5, 1' 9, 0 8, 8, | 8 0 7, 8,
07 1: 4. 2. 1, 1, | 6, 1: 8 | 8, 0, 3, 8, 2. 6, 8, | 2, 1. 7 | 1. 6,
08 6. 1 | 5 0 4. | 1: 4. | 5 1: 5, 1: 6, | 1' 8, | 1. 7 1. 3,
09 8, 1. 8 | .1 4, 3, 1. 6, 1 | 1. 9, | 1' 3, 7 0 8,
10 2. 7, | 7 1: 3, 1: 7. 8, .1 5, | 1: 7, 8, 1: 8 | 3, 1. 6 8, 1.
11 8 1' 3, | 1: 4. 1: 1, 1: 8, | 6, 1: 8 | 1 3, 0 7
12 1, 0 2, 1' 7, | 8 1: 4, | 2. 3 1: 7, | 5 1. | 3. 1. 5, 1.
13 8 1 8, | 3. 2. 8, 1: 8, 8, 1: 8 | 8 1: 3, 8, | 8, .1 3 0 8
14 5 0 4. | 6, 1: 8 | 6 0 5, | 2, 1: 5, 1: 7 1: 3
15 8, 1: 8
16 8 1 7 0 3, | 1: 4. :1 8, 8, | 3. 0 5, 8, 1' 5, | 3. 1: 5, 1: 8
17 0, 3, 0, 8 | 3. 0 5, 8, | 1. | 7. 1: 3, 1: 5, 1. 8
18 7, | 8 0 7, 8, | 5 0 4. | 1. 3, 2 0 3 | 6, 1: 8 | 5, 1' 8, 5 1. 8, 0 8
19 7. 1: 3, 1: 5, 1: 8 | 5, 1: 8, 8, | 1, .1 | 1, 1' 6, 1. 8, 0 8
20 .1 3 3. 0, 9, 0, 5, | 7. 1' 8 8, 1. 5, 1. 6, 7. 0 3,
21 9 5, 1: 5, | 2. 7, | 2, 0 7 0 5, | 5 .1 | 7 1: 3 3. 1: 7, 1: 3
22 1' 3, 9 1' 3
```

## Plaintext

Hungarian, with punctuation and word division added by the editor:

Édes Margitkám!

Szerencsésen hazaértünk. Háromórakor indultunk és félhatra értünk le. Nagyon sötét volt és nagy sár. A nadrágunk térdig lett vizes, a cipőnk meg egész elázott. Most egyébb nem történt, csak annyi, hogy egy helen [= helyen] át akartam ugrani az árkot és keresztül estem rajta. Már egyebet nem irok. Bocsás [= bocsáss] meg, édes, ha valamit vétettem, mert tudom hogy nem jól cselekedtem.

Mikor együtt voltál velem,

öröm volt a szerelem;

s most hogy arcod nem láthatom,

szerelem lett bú-bánatom.

Üdvözöl számtalanszor, ölel és csókol hű kedvesed (Árpád)

Open on the card: Mezőkövesd 1916. V/9

## English translation

Sweet Margitka of mine!

We got home safely. We set out at three o'clock and got down by half past five. It was very dark and very muddy. Our trousers got wet to the knee, and our shoes were completely soaked. Nothing else happened, except that at one spot I tried to jump over the ditch and fell across it. I will not write anything more now. Forgive me, sweet, if I did anything wrong, for I know I did not act well.

When you were together with me,

love was a joy;

and now that I cannot see your face,

love has become my grief and sorrow.

Your faithful sweetheart greets you countless times, embraces and kisses you (Árpád)

Mezőkövesd, 9 May 1916. Address: To the esteemed Miss Margitka Sziber, Borsod county, Szomolya, post office Bogács.

## Slovak translation

Moja sladká Margitka!

Šťastne sme prišli domov. Vyrazili sme o tretej a dole sme boli o pol šiestej. Bola veľká tma a veľké blato. Nohavice sme mali mokré po kolená a topánky úplne premočené. Inak sa nič nestalo, len toľko, že som na jednom mieste chcel preskočiť priekopu a spadol som cez ňu. Viac už nepíšem. Odpusť mi, milá, ak som sa niečím previnil, lebo viem, že som nekonal dobre.

Keď si bola so mnou,

radosťou bola láska;

a teraz, keď nemôžem vidieť tvoju tvár,

láska sa stala mojím žiaľom a smútkom.

Nespočetnekrát ťa pozdravuje, objíma a bozkáva tvoj verný milý (Árpád)

Mezőkövesd, 9. mája 1916. Adresa: Vážená slečna Margitka Sziberová, Boršodská župa, Szomolya, pošta Bogács.

## What remains uncertain

Three signs are set by word sense, not by the table:

1. `valamit`, third sign: a tailed sign that looks partly like a 9. It has two counters, so it is taken as a blotted 8 with its comma, `8,` = t. The reviewer supports this on the pixels.
2. `ölel`, first sign: 9-shaped with a long tail, not a clear `0,`. The same 9-shaped ö stands on hcp-1174. Since 9 alone is p, this rests on the word.
3. `szerelem` in verse line 2, the fourth e: only a low dot shows, as the sign touches the blotted 8 after it. A high dot may be hidden there. The same word in line 4 has a clean `1:`.

Readings that are by the table but partly helped by sense:

- `mert`: the first sign has a heavy, flagged top, but only `8` gives a word. The doubled t of `mert tudom` is one t for each word.
- `láthatom`: the comma of `8,` runs into the next 5, and it is assigned to the 8.
- `voltál`: a small stray dot stands low to the left of the `1'`.
- `bú-bánatom`: `bú` is read by the set phrase. The hyphen is editorial.
- Vowel marks are small. Where a dot is faint, the known word helped. This can affect a vowel, not a word.

Spellings are kept as written: `egyébb` (standard egyéb), `helen` (helyen), `bocsás` (bocsáss), `egész` for egészen, and `irok` with no accent. The words `keresztül`, `üdvözöl` and `hű` carry the one-dot `.1`, not `:1`. Either the writer's one-dot form also stands for ü, or a second dot was left out or lost. The word is the same either way. The two-dot `:1` stands only in ü words, and no u word has two dots.

A `)` stands after `cselekedtem` with no opening bracket and carries no letter. A clear `)` also stands after the signature, and a pale slanted stroke before it is probably the opening bracket, so the name is printed as `(Árpád)`, as on hcp-1143, 1146 and 1162. Other punctuation is editorial, apart from the `!` and the line-end hyphens.

Not established: whether the HistoCrypt article treats this card, the postmark date, who "we" were on the journey, and whether the verse has a printed source (none was searched for). The address word `Borsodm.` was read from the normal-size scan and not studied further.

## Why the solution is believed correct

The 30 signs decode all 415 cipher signs into continuous Hungarian, with nothing left over. 25 of the 30 values come from hcp-1174, 1178 and 1179, and the five new signs recur in plain words. The text has concrete detail (three o'clock, half past five, mud, a ditch) and a verse that rhymes (velem / szerelem, láthatom / bánatom). The recipient's name and the signature fit the correspondence, and the closing is the group's standard formula.

## Review and what changed

An independent reviewer, a separate Claude Opus 5.5 agent, ran the command, decoded the transcription with its own parser and key, and read all 22 rows from its own crops, sign by sign. It checked the key values against other cards and tried to refute the disputed readings. It confirmed the cipher, the key family and the message. Its verdict was REVISE, with three major and two minor findings, all accepted:

1. `bocses` was a misread sign. The 1 has one high dot, so it is `1'` and the word is `bocsás` (major).
2. `ölelés` was a wrong word division. It is `ölel és`, the closing formula of the group (hcp-1137, 1143, 1146, 1151, 1153, 1162), and the translations were corrected to "embraces and kisses you" (major).
3. One sign `:1` had been claimed for both u and ü. All 12 places were compared, and one-dot `.1` is a separate sign. The key gained a sign, and `indultünk` became `indultunk` (major).

![The 12 dot-left signs compared by the reviewer: two dots in hazaértünk, értünk and együtt, one dot in the rest (review/work/c/dotleft.png)](../review/work/c/dotleft.png)

4. The sign count was corrected: 30 signs with `.1`, of which 25 come from the sister cards (minor).
5. The brackets around Árpád are now disclosed, the opening one as probable (minor).

Only one word changed its letters apart from the spelling of `indultunk`. The story, the verse and the values of the existing signs did not change, so no second round was needed. The reviewer could not settle the postmark, the HistoCrypt question, the identity of "we" or a printed source for the verse.

## Credit

Key family: Claude Opus 5.5 on hcp-1174, 1178 and 1179. Transcription, key extension and decipherment of this card: Claude Opus 5.5. Independent review: a separate Claude Opus 5.5 agent. No published solution was used.
