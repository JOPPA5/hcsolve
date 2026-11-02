# HCP 1168 (cpc_1916-01-30_HU_Mezokovesd_HU_Szomolya_szomolya-16): Árpád writes to Margitka about money, shoes and a verse

Human solver: Tomáš Pavuk

**Status: deciphered in full (365 of 365 cipher signs; 358 by the table as written, 7 resting on word sense); one word, keves, has two possible normal forms; independent review 1 verdict ACCEPT, no letter of the reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1168 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1168), portal name cpc_1916-01-30_HU_Mezokovesd_HU_Szomolya_szomolya-16, from Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166); it was not checked for this card, so whether it treats this card is unknown. No published solution was found in this repository or on the portal.

It is a picture postcard with a portrait of a young woman. A small open note on the picture side gives place and date: **Mezőkövesd, 1916, I 30,** (30 January 1916). The address is open: **Őnsg. / Szépreményű / Sziber Margitka / urleánynak / Szomolya / (Borsod m.) u. p. Bogács** ("To the promising Miss Margitka Sziber, Szomolya, Borsod county, post office Bogács"). Mezőkövesd and Szomolya are close to each other in Borsod county, northern Hungary. The postmark shows JAN; its place fits Mezőkövesd, but its day and year are not clearly struck, so the year comes from the written dates.

The card belongs to a series of Mezőkövesd cards to Margitka Sziber from 1915 and 1916, written in a digit cipher (HCP 1135 to 1179). Cards of the series often encipher only key words inside plain Hungarian. On this card nearly the whole message is enciphered, and only three lines of a four-line verse are mainly open, so it supplies letters that the finished sister cards HCP 1174, 1178 and 1179 lacked.

![Picture side as scanned; the note runs up the left edge (source/picture-large.jpg)](../source/picture-large.jpg)

![Address side: cipher text at the left and along the foot, the verse below it, open address at the right (source/address-large.jpg)](../source/address-large.jpg)

## Method

The transcription is manual, made by the solver (Claude Opus 5.5) from the un-converted original scan at 2x and 4x enlargement. The card has no word divisions; the spaces in the transcription are editorial. The portal supplied no transcription. No earlier work on this number existed.

The starting point was the table already reconstructed on the finished sister cards HCP 1174, 1178 and 1179. That table alone produced most of the text at once (Édes Margitkám, bocsás meg, ritkán írok). The remaining values came from words with a single gap: anyagi viszonyok, nyolc, jobban, hogy, egy, kilenc, krajcár, Anyukád, hozzájutni. Each new sign recurs in several words, so none depends on one word.

The command `python3 -I ciphers/hcp-1168/work/decode.py`, run from the repository root, checks the hashes of the scans, decodes every sign of the transcription, stops if the letters differ from the stated reading, and prints the text.

## Key

Monoalphabetic substitution (register label MASC), Hungarian, with a figure-plus-mark alphabet. A letter is a digit plus an optional mark, and the mark changes the letter. Hungarian digraphs have one sign. The vowels a/á and e/é are separated; the other long and short vowels are not. Values in bold are new on this card; `4` = f was tentative on HCP 1175 and is confirmed here.

| Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|
| `0` | o, ó | `2` | **c** | `5` | h |
| `0,` | ö, ő | `2,` | cs | `5,` `5.` | l |
| `1` | i, í | `2.` | é | `6` | **j** |
| `1,` | b | `3` | d | `6,` | n |
| `1.` | a | `3,` | r | `6.` | **ny** |
| `1:` | e | `3.` | v | `7` | k |
| `1'` (high dot) | á | `4` | f | `7,` | s |
| `.1` (dot on the left) | **u** | `4,` | g | `7.` | sz |
| `:1` (dots on the left) | ü | `4.` | **gy** | `8` | m |
| `9` | p | `9,` | z | `8,` | t |

The transcribed signs, row by row (L01 to L16 the letter, SIG the signature, V2 and V4 the enciphered verse parts, L21 the closing line along the foot; a bar marks an editorial word space, = a line-end hyphen):

```text
L01 2. 3 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
L02 1, 0 2, 1' 7, | 8 1: 4, | 5 0 4. | 1 6. 1: 6, | 3, 1 8, =
L03 7 1' 6, | 1 3, 0 7 | 3 1: | 8 0 7, 8, | 1. 9, | 1. 6. 1. =
L04 4, 1 | 3. 1 7. 0 6. 0 7 | 6, 1: 8 | 4 1 9, 1: 8, 1 7
L05 7 1 | 6 0 1, 1, 1. 6, | 6, 1: 8 | 8, 1: 5 1: 8, :1 6, 7
L06 3, 0 5, 5, 1. | 5 0 4. | 1. 5 0 9, | 1. | 9 1' 3, | 7 3, 1' 6 =
L07 2 1' 3, 5 0 9, | 0 5. 1. 6, | 6, 1: 5 1: 9, 1: 6, | 5, 1: =
L08 5 1: 8, | 5 0 9, 9, 1' 6 .1 8, 6, 1 | 1. 8 1 8,
L09 7 1: 3. 1: 7, | 1. 6. .1 7 1' 3 | 1 3 1: | 1. 3 0 8,
L10 7 1 5, 1: 6, 2 | 7 0 3, 0 6, 1' 8, | 8 1' 3, | 6, 1 6, 2,
L11 1, 1: 5, 0, 5, 1: | 8 1: 3, 8, | 6. 0 5, 2 | 7 0 3, 0 6, 1.
L12 7 1: 5, 5, 1: 8, | 1. | 2 1 9 0, 3, 1: | 1. 9, | 8 1' 6,
L13 1. 9, | 1: 4. | 7 0 3, 0 6, 1' 1, 0 5, | 1. 9, | 1. 3 0 7, 1' =
L14 4, 0 8 1. 8, | 4 1 9, 1: 8, 8, 1: 8 | 8 2. 4, | 8 0 7, 8,
L15 1 7, | 8, 1. 3, 8, 0 9, 0 7 | 1: 4. | 9 1' 3, | 7 3, 1. 6 2 1' 3, =
L16 3, 1. 5,
SIG 1' 3, 9 1' 3
V2 8 1. 4, 1. 8 1. 8,
V4 8 1: 4, 2, 0 7 0 5, 6 1. 8 | 1. 6 7 1. 3 1. 8,
L21 7, 0 7 7. 0 3, | .1 3 3. 9 9, 9 5, 3. 1: | 2. 7, | 2, 0 7 0 5, 3. 1. | 8 1. 3, 1. 3 0 7 | 7. 1: 3, 1: 8, 0, | 7 1: 3 3. 1: 7, 1: 3 | 1. | 7 1 3, 1 4,
```

## Plaintext

Hungarian, spelling as written. Square brackets mark text that is enciphered on the card; the rest is open.

Mezőkövesd, 1916, I 30,

[Édes Margitkám!]

[Bocsás meg, hogy inyen ritkán írok, de most az anyagi viszonyok nem fizetik ki jobban, nem tehetünk rólla, hogy ahoz a pár krájcárhoz olan nehezen lehet hozzájutni, amit keves Anyukád ide adot, kilenc koronát már nincs belőle mert nyolc korona kellet a cipőre az mán az egy koronából az adóságomat fizettem még most is tartozok egy pár krajcárral]

) ([Árpád]) 1916, I/30

Saját kis versembe zárni

Szeretném én [magamat]

Hogy mikor ajkad elszavalja,

[Megcsókoljam - ajkadat]

[Sokszor üdvözölve és csókolva - maradok szerető kedvesed a sírig]

Normal spelling of the forms that differ: bocsáss, ilyen, róla, ahhoz, olyan, adott, kellett, már (mán is colloquial), adósságomat. The punctuation of the money passage is editorial, since none is enciphered.

### English translation

Sweet Margitka! Forgive me for writing so rarely, but just now money matters do not pay any better; we cannot help it that those few kreuzers are so hard to come by. Of what your [dear?] mother gave here (or: of the little that your mother gave here), nine crowns, there is nothing left, because eight crowns were needed for the shoes, and with the one crown left I paid my debt, and even now I still owe a few kreuzers. (Árpád) 1916, I/30

I would like to shut myself up in my own little verse, so that when your lips recite it I may kiss your lips.

Greeting and kissing you many times, I remain your loving sweetheart until the grave.

### Slovak translation

Sladká Margitka! Odpusť, že píšem tak zriedka, ale teraz finančné pomery nevyplácajú lepšie; nemôžeme za to, že k tým pár grajciarom sa tak ťažko dá dostať. Z toho, čo tvoja [drahá?] mama sem dala (alebo: z toho mála, čo tvoja mama sem dala), deväť korún, už nič nezostalo, lebo osem korún bolo treba na topánky a tou jednou korunou som zaplatil svoj dlh, a ešte aj teraz dlhujem pár grajciarov. (Árpád) 1916, I/30

Rád by som sa uzavrel do vlastného veršíka, aby som, keď ho tvoje pery zarecitujú, pobozkal tvoje pery.

Mnohokrát ťa pozdravujem a bozkávam a zostávam tvoj milujúci milý až do hrobu.

## What remains uncertain

Seven signs rest on word sense:

1. **üdvözölve (three signs).** The two ö signs first looked like plain `9` (p). Enlarged, their tails have a separate notched head, unlike the true `9` of pár, so they are most likely `0,` with the comma touching. The first sign has a lower left dot and a blob that may be the upper dot of `:1`; a plain `.1` = u cannot be fully excluded, but the word needs ü.
2. **sírig.** The first sign is a plain crossed 7 (k) with no comma, which gives kirig, not a word. The reading s is by sense; kedvesed a sírig is a stock ending.
3. **csókolva.** The first sign is a filled ink blot with a clear comma and a tail that fits 2.
4. **koronából.** The sign is probably a serifed `1,` (b); `7,` (s) would give no word. Marked out of caution.
5. **adóságomat.** The sign is a 1 with one dot set rather low, and the line-end hyphen lies at its foot where the lower dot of `1:` would be. á is confirmed by the word.

Other points:

- **keves.** The signs are clear: `7 1: 3. 1: 7,`. Both normal forms need a slip: kedves ("dear") drops a d, and kevés ("little") uses `1:` for é, though this writer writes é with `2.` in Édes, és and még. The sense favours kedves, but it is not settled. Only one word of the translation depends on it.
- **inyen** for ilyen: the sign `6.` is clear, so this is a slip or a dialect form. **olan** for olyan may be no oddity at all: by the pattern of the dotted signs (g/gy, n/ny, s/sz), `5.` could stand for ly. But `5.` is plain l on HCP 1178 and 1179, and it occurs only once here, so this is unproved.
- **elszavalja** is open text. The l and j share one long stroke, and the stroke above it is a comma from the cipher line above.
- A closing bracket stands after krajcárral with no opening one, and a dot stands above the `5,` of csókolva. Neither is explained, and neither changes the reading.
- The verse may be quoted or the writer's own; it does say saját ("my own"). No printed source was searched outside the repository.
- The money passage has no enciphered punctuation, so the clause division is an interpretation. The sums fit it: 9 crowns = 8 for shoes + 1 for the debt.

## Why the solution is believed correct

One table decodes all 365 signs into continuous Hungarian of the period, and the text is long enough that such a fit cannot arise by chance. The content checks itself: 9 crowns from the mother, 8 for shoes, 1 for a debt. The open verse confirms the cipher, since the enciphered magamat and ajkadat complete its rhyme and ajkadat repeats the open ajkad. Recipient, town, date range, salutation and the signature Árpád agree with HCP 1174. Kreuzers and crowns fit 1916.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) tried to refute the solution. It ran the command, wrote its own decoder sharing no code with the solver's (same letters, 31 distinct signs, 365 tokens), and read every cipher row on its own crops of the original scan, finding no disagreement with the transcription. It checked the doubtful places at 4x to 8x. Its verdict was **ACCEPT** with six minor findings, none changing a letter:

1. A cross-reference for keves pointed to the wrong item. Fixed.
2. The solution wrongly said only a/á were separated; e/é are too. This changes the keves argument: both readings need a slip. Corrected.
3. olan may be simply olyan, with `5.` as ly. Added as an open alternative.
4. The ö signs of üdvözölve are not really plain 9. The note was rewritten and the claimed "9 for ö" habit was dropped from the evidence.
5. The count of new values was inconsistent. It is five, plus `4` confirmed.
6. The dot in adóságomat is lower than usual and the sign rests partly on sense. It is now tagged, which raised the sense-read signs from 6 to 7.

The picture-side date was also corrected to its written commas. The reviewer could not verify the HistoCrypt article, the postmark year or a printed source for the verse; these stay open.
