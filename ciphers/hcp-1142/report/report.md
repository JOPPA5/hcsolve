# HCP 1142 (cpc_1906--_HU_Mezokovesd_HU_Szomolya_szomolya-41): a love verse in numbers to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: the cipher is deciphered in full (210 of 210 signs); independent review 1 verdict REVISE, findings addressed.** One open word at the foot is unsure in spelling but secure in sense. Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1142 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1142), part of Tobias Schrödel's collection of cryptographic postcards (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article; it was not checked for this card, so we cannot say whether it discusses it.

The card is addressed in open writing to **Tek. Szépreményü Sziber Margitka kisasszonynak (Szomolya.) u. p. Bogács (Borsod m.)**: "To the Honourable, the promising Miss Margitka Sziber, Szomolya, post office Bogács, Borsod county", in north-east Hungary. It belongs to a series of cards from Mezőkövesd to Szomolya, in the same hand and cipher, many of them signed Árpád or Sz. A.; the dated cards of the series are from 1915 and 1916.

This card has no written date. The purple round stamp shows BORSOD and the year 1906; the lower arc may read ...GYE, so it may be a county seal and 1906 a seal year, not a posting date. The grey postmark cannot be read. No date is established. The picture side has only a printed tinted photograph and publisher's marks.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The whole message is enciphered except two closing lines. The solver read every row from the high-resolution scan at 2 to 5 times enlargement and wrote the signs into a transcription; no OCR was used. Decoding starts from the key reconstructed on finished sister cards hcp-1174, 1178 and 1179. That key opened the card at once (`Kedves Margitkám`, `a lapodat megkaptam`). Six signs missing or tentative on those tables got their values from words on this card, and a seventh (`5.`) is discussed below. Word divisions are the solver's. The reproduction command, run from the repository root, is:

```
python3 -I ciphers/hcp-1142/work/decode.py
```

It checks the hashes of the scans, decodes the transcription, compares each line with the stated reading and prints the open lines, which are hard-coded.

Transcription (`|` divides words, `----` marks the ruled lines around the couplet):

```
7 1: 3 3. 1: 7, | 8 1. 3, 4, 1 8, 7 1' 8
1. | 5, 1. 9 0 3 1. 8, | 8 1: 4, 7 1. 9 8, 1. 8
1. 8 1: 5. 6, 1: 7 | 6, 1. 4. 0 6, | 8 1: 4,
0, 3, :1 5, 8, 1: 8 | 3. 1. 7, 1' 3, 6, 1. 9 | 5 1.
6 0 | :1 3 0, | 5, 1: 7. | 4 1: 5, 8 1: 4. 1: 7
----
1. 7. 8, | 8 0 6, 3 6 1. | 7. 1 3. 1: 8 6, 1: 7
8 1 6, 3 1: 6, 1 7 | 3. 1: 3, 2. 7, 1:
8, 1: | 3. 1. 4. | 1. | 3. 1 5, 1' 4, 6, 1. 7
5, 1: 4, 7. 1: 1, 1, | 8, 1: 3, 1: 8 8, 2. 7, 1:
----
1: | 7 1' 3, 8. 1' 6, | 9 1 2 1 6. | 5 1: 5. | 3. 1. 6,
6, 1: 8 | 7, 0 7 1. 8, | 1 3, 5 1. 8, 0 7
:1 3 3. 0, 9, 0, 5, 5, 1: 7 | 7, | 1. 7 1 | 3. 0 5,
8, 1. 8
8, 1: 6, 2. 7 1: 3 | 1. 9, | 8 1. 3, 1. 3 0 7
```

## Key

Monoalphabetic substitution of Hungarian letters. Each letter is one sign: a digit, or a digit with a mark. A comma, dot or colon is part of the sign. The key does not separate o/ó, ö/ő or i/í.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| `0` | o, ó | `2` | c | `5.` | ly (l on finished cards) |
| `0,` | ö, ő | `2,` | cs | `6` | j |
| `1` | i, í | `2.` | é | `6,` | n |
| `1.` | a | `3` | d | `6.` | ny |
| `1:` | e | `3,` | r | `7` | k |
| `1'` (high dot) | á | `3.` | v | `7,` | s |
| `:1` (dots left) | ü | `4` | f | `7.` | sz |
| `1,` | b | `4,` | g | `8` | m |
| `9` | p | `4.` | gy | `8,` | t |
| `9,` | z | `5` | h | `8.` | ty |
| | | `5,` | l | | |

The card has 210 cipher signs, 30 distinct, all in the table. New against the finished tables, and fixed by this card's words: `2` = c (piciny), `4` = f (felmegyek), `4.` = gy (nagyon), `6` = j (jó), `6.` = ny (nagyon, piciny), `8.` = ty (kártyán). A wrong value gives no word in these places.

`5.` conflicts with the finished cards hcp-1178 and 1179, which give it as plain l. The card cannot separate l from ly: `amelynek` and `hely` here are the normal spellings of what this writer could spell `amelnek` and `hel`. The words are the same either way.

## Plaintext

Enciphered part (line breaks of the verse, punctuation and capitals are editorial):

**Kedves Margitkám!**

**A lapodat megkaptam, amelynek nagyon megörültem. Vasárnap ha jó üdő lesz, felmegyek.**

**Aszt mondja szívemnek mindenik verése:**

**Te vagy a világnak legszebb teremtése.**

**E kártyán piciny hely van, nem sokat írhatok.**

**Üdvözöllek, s aki voltam tenéked, az maradok.**

Open text at the foot:

**Számtalanszor csókollak mindanyájatokat (?),** (Sz. A.)

Spellings as on the card: `aszt` (azt), `üdő` (idő, a dialect form, also on sister cards), `mindenik` (each one), `tenéked` (older form of neked). Accents on `jó`, `üdő`, `szívemnek` and `írhatok` are supplied, because the key has none. `mindanyájatokat` is printed as the card seems to show it; it is a form of `mindnyájatokat`.

The ruled lines above and below the couplet set the verse off. Both pairs rhyme in the cipher: verése / teremtése and írhatok / maradok.

### English translation

Dear Margitka of mine! I received your card, which made me very glad. On Sunday, if the weather is good, I will come up.

Each of its beats says this to my heart:

You are the most beautiful creation in the world.

There is little room on this card, I cannot write much.

I greet you, and what I have been to you, that I will remain.

Countless times I kiss you all. (Sz. A.)

### Slovak translation

Drahá moja Margitka! Tvoj lístok som dostal a veľmi ma potešil. V nedeľu, ak bude pekné počasie, prídem hore.

Každý jeho úder hovorí môjmu srdcu:

Ty si najkrajšie stvorenie sveta.

Na tomto lístku je málo miesta, veľa napísať nemôžem.

Pozdravujem ťa, a čím som ti bol, tým ostanem.

Nespočetnekrát vás všetkých bozkávam. (Sz. A.)

## What remains uncertain

- **The foot word `mindanyájatokat` (?).** This is open writing, not cipher. `mind` and `-tokat` are clear, and the next letters are a clear a, n and a descender, so the card is not spelled `mindny...`. The middle has an a-like letter with a blotted side, an open c-like letter under an acute, a second descender with a tick near it, an o/a-like letter and a short stroke. We cannot match every stroke, and there are one or two more than this form needs. The sense "all of you" is secure: `-tokat` is the second-person plural accusative ending, `csókollak` needs a second-person object, and the phrase stands on sister cards hcp-1152, 1154, 1157 and 1172.
- **Last sign of `maradok`.** A 7 with a wedge below it. The wedge might be a comma, giving s, and it does not settle the matter graphically. The word stands on sense: `marados` is no word here.
- **`8.` in `kártyán`.** The dot has a thin pen drag under the next sign. At high enlargement it is a dot with a tail, not a comma, and plain `8` gives no word.
- **`5.`** is l or ly (see Key).
- **`Sz. A.`** The signature stands in a loop; the capital looks like A, and K was discussed on hcp-1178. The series signs the name Árpád in cipher.
- **The couplet** may be a quotation or popular verse; no source was looked for. `mindenik verése` is read as "each of its beats"; `szívemnek` could also be the possessor, "each beat of my heart says this".
- **Date:** not established. The stamp middle and the grey postmark could not be read.

## Why the reading is trusted

One fixed key turns all 210 signs into continuous grammatical Hungarian with no gap. The rhyme verése / teremtése played no part in setting any value or reading, so it is independent support; írhatok / maradok is weaker, because `maradok` itself rests on sense. Recipient, address, closing formula, hand and the spellings `aszt` and `üdő` match the sister cards, and the Sunday visit fits hcp-1174.

## Review and what changed

An independent reviewer (a separate Claude Opus 5.5 agent) reran the command, wrote its own decoder with a separately typed table, and checked every row of the transcription against its own crops of the scan. It found no wrong sign and returned **REVISE** with five minor findings. None changed the transcription or the key values.

- **Foot word.** The first print, `mindnyájatokat`, was a normalised form. The text now gives the form seen, with its doubt.
- **`5.`** The conflict with finished cards was not stated; it is now, and `5.` no longer counts as part of a palatal pattern.
- **Independence.** The claim that both rhymes were independent was too strong, and the status of the sister cards was out of date. Both are corrected.
- **`maradok`.** The solution no longer leans towards a flourish; it says the wedge is open and the word stands on sense.
- **Seal.** The note that 1906 may be a seal year was added.
