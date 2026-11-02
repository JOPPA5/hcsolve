# HCP 1163 (cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20): a suitor's love verses in digits on a Hungarian postcard

Human solver: Tomáš Pavuk

**Status: deciphered in full (391 of 391 cipher signs; 390 by the key as seen, 1 by word sense); independent review 1 verdict REVISE, findings addressed, no word of the reading changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1163 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1163), portal name cpc_1916-02-26_HU_Mezokovesd_HU_Szomolya_szomolya-20, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it treats it. No published solution of this card was found or used.

The card is a picture postcard of a young couple, sent in wartime from Mezőkövesd to the village of Szomolya in north-east Hungary. The picture side carries no cipher. On the message side everything is in figures except the date line, **Mezőkövesd, 1916. II/26.** The open address reads **Őnagysága / Szépreményű / Sziber Margitka / kisasszonynak / (Borsodmegye) / Szomolya / u. p. (Bogács.)**, that is "Her Ladyship, the promising Miss Margitka Sziber, Borsod county, Szomolya, post office Bogács". The postmark shows Mezőkövesd rim letters, but its date is not legible, so the written date is relied on.

The card belongs to the correspondence to Margitka Sziber, cards hcp-1135 to 1179 of the portal. Hcp-1174, 1178 and 1179 use the same digit cipher, there mostly for single words inside open Hungarian. Here the writer enciphered the whole message.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan enlarged 2 to 6 times. No OCR was used. The key of the earlier cards hcp-1174, 1178 and 1179 was the starting point. It gave **Édes Margitkám** in the first row at once. The rest of the card was then read sign by sign, and the signs not yet in the key were fixed from words: `hogy` gave gy, `cédulát` gave c and u, `felelj` gave j, `enyém` gave ny. This is therefore a transferred key extended by this card, not a new key recovery.

The cipher has no regular word gaps, so word boundaries are editorial. Marks written high on the 5 are part of how this writer forms the 5; only the comma below changes it.

The decoding can be reproduced from the repository root with `python3 -I ciphers/hcp-1163/work/decode.py`. It checks the scan hashes, decodes every sign by the fixed key with no per-word exceptions, and asserts that the stated reading equals the decode letter by letter, with only vowel length folded. The accented reading is hard-coded in the script, and that check is what ties it to the decode.

## Key

Monoalphabetic substitution (register label MASC). Each letter is one digit or a digit with a mark, and the mark is part of the sign. Comma, dot and colon are therefore not punctuation. Five signs are new on this card (`.1`, `2`, `4.`, `6`, `6.`), and `4`, tentative on an earlier card, is confirmed. There are 30 distinct signs in 391 positions.

| sign | letter | | sign | letter | | sign | letter |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | | `2.` | é | | `6,` | n |
| `0,` | ö, ő | | `3` | d | | `6.` | ny (new) |
| `1` | i, í | | `3,` | r | | `7` | k |
| `1.` | a | | `3.` | v | | `7,` | s |
| `1:` | e | | `4` | f (confirmed) | | `7.` | sz |
| `1'` (dot at upper right) | á | | `4,` | g | | `8` | m |
| `:1` (two dots at left) | ü, ű | | `4.` | gy (new) | | `8,` | t |
| `.1` (one dot at left) | u, ú (new) | | `5` | h | | `9` | p |
| `1,` | b | | `5,` | l | | `9,` | z |
| `2` | c (new) | | `6` | j (new) | | | |
| `2,` | cs | | | | | | |

The two left-dot forms split exactly by sound, 7 of 7. In the figure the upper row shows csütör, küldtem, cédu, tudom and the lower row úgy, üdvözölve, hűséges. In csütör and küldtem the upper dot touches the flag of the 1, which makes it look forked.

![The left-dot signs at about 5x (work/crops/u_split_from_review.png)](../work/crops/u_split_from_review.png)

## Plaintext

Ciphertext as transcribed, one line per card row. `5~l` marks the one sign read by sense.

```text
L0: 2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8
L1: 2. 3, 8, 1: 7, 1 8, 5, 1: 7 5 0 4. 2, :1 8, 0, 3,
L2: 8, 0, 7 0, 6, 7 :1 5, 3 8, 1: 8 1: 4. 2 2. 3 .1
L3: 5, 1' 8, 6, 1: 8 8, .1 3 0 8 8 1: 4, 7 1. 9 8, 1. 3
L4: 1: 5 1. 1 4, 1: 6, 1. 7 7 0 3, 1 3, 3 8 1: 4,
L5: 2. 7, 4 1: 5, 1: 5, 6 3. 1. 5, 1. 8 1 8, 1. 8, 1. 3,
L6: 8, 1. 5, 8 1' 3, 0 5, 1. 9, 8, 1' 6, 1 3, 6 1' 5,
L7: 7, 0 7 1. 8,
V1: 1, 0 5, 3 0 4, 2, 1. 7 .1 4. 5, 1: 5 1: 8, 1: 7 2. 6,
V2: 5 0 4. 5 1. 8, 1: 5, 1: 7. 1: 5, 1. 9, 1: 6. 2. 8
VI1: 6, 1: 8 7. 1: 3, 1: 8, 1: 7 8 1' 7, 8, 2, 1. 7 8, 2. 4, 1: 3
VI2: 2, 0 7 7 1. 5, 8, 1: 7. 1: 7 3, 1' 9 1: 2, 2. 8, 1: 8,
B1: 5 0 4. 5 1. 3, 1' 3 4, 0 6, 3 0 5, 0 7
B2: 1, 0 5, 3 0 4, 7, 1' 4, 0 8 1' 5, 8 1.
B3: 1 7, 8, 1: 6, 1: 8 5 1. 1: 4. 7 0 3,
B4: 1: 9, 3. 1. 5, 0 3, 1. 3. 1' 5, 6, 1.
B5: 5 0 4. 5 1. 8 1. 4, 1. 8 2. 6, 1. 7
B6: 8 0 6, 3 5 1. 8, 6, 1' 5, 1. 7 8, 2. 4, 1: 3
B7: 8 1: 4, 1' 5, 3 1. 6, 1' 8 2. 3, 8, 1:
B8: 1. 6, 1. 4. 8 1 6, 3 1: 6, 7, 2. 4, 1: 8,
E1: 7. 1' 8 8, 1. 5, 1. 6, 7. 0 3, 2, 0 7 0 5, 3. 1. 2. 7,
E2: :1 3 3. 0, 9, 0, 5~l 3. 1: 8 1. 3, 1. 3 0 7 5 :1 7, 2. 4, 1: 7,
E3: 7 1: 3 3. 1: 7, 1: 3 2. 7, 1 8 1' 3 0 3 ( 1' 3, 9 1' 3 )
```

Hungarian text. All of it is enciphered except the date. Punctuation is editorial, except the `!` after the salutation and after `Istenem` and the stop after `enyém`. V and VI are Roman numerals on the card.

```text
Édes Margitkám!

Értesítlek, hogy csütörtökön küldtem egy cédulát, nem tudom megkaptad-e.
Ha igen, akkor írd meg és felelj valamit a tartalmáról, aztán írjál sokat.

V   Boldog csak úgy lehetek én,
    hogyha te leszel az enyém.
VI  Nem szeretek mást, csak téged,
    csókkal teszek rá pecsétet.

Hogyha rád gondolok: boldogságom álma!
Istenem! ha egykor ez valóra válna.
Hogyha magaménak mondhatnálak téged,
megáldanám érte a nagy mindenséget.

Számtalanszor csókolva és üdvözölve maradok
hűséges kedvesed és imádód (Árpád)

Mezőkövesd, 1916. II/26.
```

## Translation

**English.** Sweet Margitka! I let you know that on Thursday I sent a slip of paper; I do not know whether you received it. If so, then write and tell me, and answer something about its contents, and then write a lot.

V. I can be happy only if you will be mine. VI. I love no one else but you; with a kiss I set a seal on it.

When I think of you: the dream of my happiness! My God! if only this came true one day. If I could call you my own, I would bless the whole universe for it.

Kissing and greeting you countless times, I remain your faithful sweetheart and adorer (Árpád). Mezőkövesd, 26 Feb 1916.

**Slovak.** Moja sladká Margitka! Oznamujem ti, že vo štvrtok som poslal lístok; neviem, či si ho dostala. Ak áno, tak mi to napíš a odpovedz niečo k jeho obsahu, a potom píš veľa.

V. Šťastný môžem byť len tak, ak budeš moja. VI. Nemilujem nikoho iného, len teba; bozkom na to dávam pečať.

Keď na teba myslím: sen môjho šťastia! Bože môj! keby sa to raz stalo skutočnosťou. Keby som ťa mohol nazývať svojou, požehnal by som zaň celý vesmír.

Nespočetnekrát ťa bozkávam a pozdravujem a zostávam tvoj verný milý a ctiteľ (Árpád). Mezőkövesd, 26. 2. 1916.

## What supports the reading

All 391 signs decode by one table into fluent Hungarian of the period, with no per-word exceptions. The verses rhyme (én / enyém, téged / pecsétet, álma / válna, téged / mindenséget). The signature Árpád and the words csókolva, kedvesed and számtalanszor come out of the same sign strings as on sister cards. 26 February 1916 was a Saturday, so "on Thursday" points two days back. The new sign values `4.` and `6` recur correctly in other words. `2`, `4` and `6.` occur once each and have no independent check, but each is fixed by a word that leaves no alternative.

## Uncertainties

No word is unread. The open points are at sign level:

1. **`üdvözölve`, the 5.** The comma is not visible, so the key alone gives `üdvözöhve`. A stroke near it is the long tip of the 7 in the row below. This is the only sign fixed by sense alone.
2. `hűséges`, final `7,`: the comma seems merged into the hooked tail of the 7. Sense needs s.
3. `lehetek`: the first e lies under a blot, but the stem and both dots show through.
4. `1'`: the dots are sometimes at mid-height (tartalmáról, mondhatnálak, megáldanám, Árpád). They stand above the place of the `1.` dot, so I read á, partly by sense.
5. `csütörtökön`: a small high dash on the first 0 is taken as a flourish.
6. `mindenséget`: a very small dot after the 3 is not counted. As a sign mark it would give v, `minvenséget`. It is far smaller than the writer's real dots.
7. `imádód`: a long thin stroke runs from under the last 3 across the opening bracket. It lacks the place and hook of a sign comma, and `3,` (r) would give no word. It may be a free comma or a slip.
8. `téged` in verse VI stands raised at the row end. It is read as the overflow of `Nem szeretek mást, csak`, which gives both the sense and the rhyme.
9. The marks after `gondolok` look like the top of a dashed frame line, not a colon. The colon in the text is editorial.
10. Small marks at row ends are read as punctuation and hyphens, and dashed underlines and rule lines as ornament.
11. `Cédula` may be a note, a slip or a ticket; the card does not say which. Why the verses are numbered V and VI is unknown; they may continue a numbering on an earlier message, but that is a guess.
12. Spelling: the key has one sign each for o/ó and i/í, so long marks in the reading (for example `valóra`, `csókkal`, `írjál`) are editorial.
13. A faint printed publisher's line and a triangle with 143 under the last rows could not be read. They are printed matter, not part of the message.
14. Whether the one-dot sign `.1` also occurs on the sister cards was not checked.

## Review and what changed

An independent Claude Opus 5.5 agent read all 23 rows from its own enlargements, without word division, and decoded them with its own table. All 391 positions were compared and row lengths agreed. It found no wrong word and confirmed the translations. Its verdict was **REVISE**, and the solver accepted all six findings:

1. **Major.** The first version claimed that `:1` stood for ü and u alike. The card has two signs: one dot for u, ú and two dots for ü, ű. The sign `.1` was added, three positions in the transcription were corrected, and the checking script no longer folds u into ü. The words did not change, and they now come directly from the decode.
2. The first word of the address is `Őnagysága`, not `Önagysága`.
3. The stroke near the 5 of `üdvözölve` comes from `kedvesed`, not `hűséges`, and shows no comma.
4. The `:` after `gondolok` is no longer claimed as on the card.
5. Three undisclosed marks were added to the uncertainties: the dot in `mindenséget`, the stroke in `imádód`, and the dashed lines.
6. Small factual slips were corrected, in the count of `5 0 4.`, the count of distinct signs and the control claim.

The reviewer could not verify the HistoCrypt article, the postmark date or the publisher's line, and neither could the solver.
