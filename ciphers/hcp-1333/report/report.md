# HCP 1333 (pc_hcp_14): a Portuguese love note from Triz to Quinito

Human solver: Tomáš Pavuk

**Status: deciphered in full (197 of 197 cipher signs, four of them physically obscured and restored); independent review 1 verdict REVISE, all findings addressed, plaintext unchanged.** Report dated 2026-10-30.

## Origin and context

The cryptogram is record 1333 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1333), portal name pc_hcp_14, part of the HCPortal collection of cryptographic postcards. When it was captured on 2026-10-30 the portal listed it as **Not solved**, tagged Postcard, HCPortal collection, category Substitution, date 1913-06-12, language Unknown, location Europe, sender Unknown, recipient Joaquin Picciochi Garcia, with no transcription or solution attached.

It is a picture postcard with a painted landscape: a house by the water under bare autumn trees. The picture has no writing on it. The message is on the address side, in fourteen cipher lines left of the printed divider, under the plain date **Atalaya, 12-6-913** (12 June 1913).

The address is in clear: **Ex.mo Sr. Joaquim Picciochi Garcia, Entroncamento.** (the portal spells the first name Joaquin). The card carries a Portuguese 1-centavo Ceres stamp with a partly legible cancellation. Atalaia and Entroncamento are neighbouring places in central Portugal. The publisher's lines "W. R. B. & Co., Vienne" and "Serie Nr. 22-12" are printed over parts of the writing, which matters below.

![Address side, with the date, the cipher text, the clear address and the HCPortal watermark (source/address-large.jpg)](../source/address-large.jpg)

![Picture side (source/picture-large.jpg)](../source/picture-large.jpg)

A sister card, HCP 1332 (pc_hcp_13, Atalaya, 12-12-1912), is addressed to the same man and uses the same script, the pet name Quinito and the signature "tua Triz". It was used here only as a check on sign shapes and names.

## Method

No earlier work exists on this number. Claude Opus 5.5 transcribed the card sign by sign from the un-converted original scan at 4–7× (no OCR, no supplied transcription) and recorded each sign with its class and the letter chosen.

The clear date and address gave the language: Portuguese. A repeated group gave the first foothold: Π R O with T X L U T U X reads "meu coração" (my heart), which fixes T = c, U = a, X = o. The pattern F U O L U L R F then gives "saudades", and U F T Q H T X E X L U F gives "às cinco horas". From there the text ran on: "tenho de ir passeiar", "ao sol posto já devemos cá estar", "um beijo ao Luizito". One stall was instructive: with U = a alone, card line 6 made no sense until the ending "-elmente" showed "provavelmente", so the a-sign also stands for v. Word gaps stay as in plaintext, which is why so short a text could be read at all.

In review a separate agent worked from its own crops of the original scan, typed its own class transcription, decoded it with its own script and listed every letter option of each word. It typed its transcription after seeing the solver's, so its zero differences are a check against the pixels rather than a blind second reading.

## Key

Simple substitution with invented, Greek-looking signs. The codes are conventional names for handwritten shapes. There are 19 sign classes.

| Code | Shape | Plain | Code | Shape | Plain |
|---|---|---|---|---|---|
| U | u-shape with thin lead-in | a, v | F | rho | s |
| W | w-shape, heavy first stroke | g, q | I | Lambda, strokes meet near the top | t |
| O | plain o | u | V | long stroke with small foot | l |
| X | cross | o | E | Sigma | h |
| R | hooked r-shape | e | S | large looped S | b |
| Q | head with right tick, curved tail | i | s | small s | z |
| 9 | closed head, straight tail | p | Z | zeta with right tick | j |
| L | tall lambda with ascender | d, r | H | theta | n |
| P | double stroke with overbar | m | T | T with overbar | c, ç |
| N | the same with a linking stroke | m | | | |

Four classes hold two letters. The writer may have meant d and r as separate signs, as on the sister card, but they could not be separated reliably here. The letters f, k, w, x and y do not occur.

![The sixteen i and p signs: ten i with a right tick and curved tail, six p without the tick (work/resp/Q2.png)](../work/resp/Q2.png)

## Plaintext

Ciphertext by sign code, card line by card line (a space is a word gap of this edition, "-" is a hyphen on the card, "!" marks an obscured sign):

```text
01 WOQHQIX LX PRO TXLUTUX
02 HUX URHEUF VXWX
03 UF TQHTX EXLUF 9XL-
04 WOR IRHEX LR QL 9UF-
05 FRQUL TXP U NUPU
06 9!LXUUURVNRHIR 9U-
07 LU X VUWUL HXUX
08 U!X FXV 9XFIX ZU LRUR-
09 PXF TU RFIUL OP
10 SRQZX UX VOQsQIX
11 FUOLULRF U VUOLU
12 R 9UOVX R OP USLU-
13 TX LU IOU ILQs UIR- 
14 VX!W!X UPXLFQIX
```

Decoded, card line by card line:

```text
quinito do meu coraçao
nao venhas logo
as cinco horas por-
que tenho de ir pas-
seiar com a mama
provavelmente pa-
ra o lagar novo
ao sol posto ja deve-
mos ca estar um
beijo ao luizito
saudades a laura
e paulo e um abra-
ço da tua triz ate-
logo amorsito
```

Portuguese, with accents, punctuation and capitals added by the editor:

**Quinito do meu coração. Não venhas logo às cinco horas porque tenho de ir passeiar com a mamã, provavelmente para o lagar novo. Ao sol posto já devemos cá estar. Um beijo ao Luizito, saudades à Laura e Paulo e um abraço da tua Triz. Até logo amorsito.**

English translation: **Quinito of my heart. Do not come at five o'clock later on, because I have to go for a walk with mama, probably to the new oil mill. By sunset we should be back here. A kiss to Luizito, regards to Laura and Paulo, and a hug from your Triz. See you later, little love.**

Slovak translation: **Quinito môjho srdca. Nechoď potom o piatej, lebo musím ísť na prechádzku s mamou, pravdepodobne k novému lisu na olej. Pri západe slnka by sme už mali byť tu. Bozk Luizitovi, pozdravy Laure a Paulovi a objatie od tvojej Triz. Do skorého videnia, láska moja.**

## Reproduction

From the repository root:

```text
python3 -I ciphers/hcp-1333/work/decode.py
```

The script checks the SHA-256 hashes of the scans, checks every token of work/transcription.txt against work/key.json, and prints the text and the sign counts. The transcription records the letter chosen in each two-letter class, so this proves consistency, not the choice itself.

## Uncertainties

- **Two-letter classes.** 69 of the 197 signs sit in a class with two letters (U 38, L 19, T 7, W 5). Each was chosen by the word it makes. The chosen words were the only running Portuguese sense found; "lauda" for "laura", for example, is a word but makes no sense here, and the sister card has Laura.
- **L and I** are not cleanly separated. Most t are a plain Lambda, but tua, ate and amorsito come close to L, so the 10 I signs also lean partly on sense.
- **Four obscured signs**, marked "!". The first sign of card line 8 (a of "ao") is blotted and overprinted "W."; the second and third signs of card line 14 (o, g of "logo") lie under "Serie Nr. 22-12"; the head of the first sign of card line 6 (p of "provavelmente") lies under the printed "&", with its tail visible. "Até logo" and "provavelmente" require them, and the visible traces fit.
- **N** looks like P with a stroke linking its two stems; taking it as a form of m rests on shape and sense.
- **Marks.** One above the p of "pas-" has no known meaning. Others fit a tilde or accent, but the card does not mark every accent ("não").
- **Persons and places.** Luizito, Laura and Paulo are not identified. "Triz" as a short form of Beatriz is an inference. "Lagar novo" may be a place name.
- **Word division** is editorial: the card's spacing is irregular.

## Review summary

An independent Claude Opus 5.5 reviewer ran the command, checked the signs against the scans at 3–6× with an ink-colour separation of the hidden places, and found no wrong letter and no forced passage. It confirmed the language and the context and returned **REVISE**, because the key, not the reading, needed work. Its six findings and what changed:

1. q was filed under the a-sign; it shares the sign of g. Moved to W.
2. i and p are two signs. All 16 examples were examined and the split holds (see the figure above). The solver had earlier tested the wrong feature.
3. The count of context-dependent signs was wrong and the L/I overlap undisclosed. The count is now 69 and the overlap is stated. The d/r division of the sister card shows as a tendency here, but not firmly enough to split the class.
4. The two j signs Y and Z were compared and are one sign.
5. The table and the data disagreed on ç. Aligned.
6. The extent of the search for a published solution was not stated. It now is: the portal page and the AI Decipherment Register check of 2026-10-30, and no separate web search.

No letter of the plaintext changed in review. The review also could not identify the persons, or separate d from r on this card, and it ran no web search of its own.

## Sources

- HC Portal record 1333: https://crypto.hcportal.eu/dashboard/cryptograms/1333 (metadata and both scans, captured 2026-10-30; hashes in SOURCES.md).
- Sister card HCP 1332 in this repository, for sign shapes and names only.
- No published solution was used.
