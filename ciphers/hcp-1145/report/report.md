# HCP 1145 (cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17): an enciphered Hungarian love letter to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered in full (385 cipher signs, 381 by the key as written, 4 by word sense); independent review 1 verdict ACCEPT, no decoded letter changed.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1145 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1145), portal name cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, main category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was **not checked** for this card, so it is not known whether it discusses it. The whole reading here was made from the card.

The card went from Mezőkövesd to the village of Szomolya in north-east Hungary during the First World War. The date is in clear, **Mezőkövesd, 1916, II/12.**, a Saturday, and the postmark shows FEB 12 (its year digits are overstruck and are not relied on). The address, also in clear, reads **Őnsg. / Szépreményű Sziber Margitka kisasszonynak, / Borsod m. / Szomolya, / u. p. (Bogács)**, "To the promising young lady Margitka Sziber, Borsod county, Szomolya, post office Bogács". `Őnsg.` is an abbreviated title, read as written. The picture side shows a man at a window handing roses to a girl and has no writing apart from the collection stamp.

Unlike its sisters HCP 1174 and 1178, where only key words are in digits inside open Hungarian, this card has its whole message enciphered: twenty rows of digits with commas, dots and colons. It belongs to one correspondence, in which a suitor signing himself Árpád writes to Margitka. HCP 1174, dated three days later (Tuesday 15 February 1916), apologises for not coming, which fits the Sunday visit promised here.

![Message and address side (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no cipher text (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The transcription is manual, from the un-converted high-resolution scan enlarged 4 to 10 times. No OCR was used and the portal supplied no transcription. A digit together with its mark is one sign, so the first task was to see each mark. The card gives no reliable word gaps, so the word divisions come from the decoder's reading.

The key of HCP 1174, 1178 and 1179 was the starting point. The card's first 13 signs are the same heading as on HCP 1174 (Édes Margitkám), and the old values read most of the text at once. Four signs had no value yet and came from words on this card: `4.` = gy (hogy), `6` = j (jöjjön), `6.` = ny (anyám) and `4` = f (felmegyünk). `1,` = b comes from HCP 1179 and is confirmed here by legalább, többet, ébren and eszemben. The verses rhyme (levelet / tégedet, gyötrelem / szerelem, ébren / eszemben), and the rhymes were not used to build the key. This key does not match the provisional values in the partial notes on HCP 1175 (`4.` = l and `1` = é there).

## Key

Monoalphabetic substitution (MASC): each letter is one digit plus an optional mark. Hungarian digraphs have one sign. Long and short vowels share a sign, except a/á and e/é.

| Sign | Plain | Sign | Plain | Sign | Plain | Sign | Plain |
|---|---|---|---|---|---|---|---|
| `0` | o, ó | `1,` | b | `3.` | v | `6` | j |
| `0,` | ö, ő | `2,` | cs | `4` | f | `6,` | n |
| `1` | i, í | `2.` | é | `4,` | g | `6.` | ny |
| `1.` | a | `3` | d | `4.` | gy | `7` | k |
| `1:` | e | `3,` | r | `5` | h | `7,` | s |
| `1'` (high dot) | á | `9` | p | `5,` | l | `7.` | sz |
| `:1` (dots at left) | ü, u | `9,` | z | `8` | m | `8,` | t |

## Ciphertext

As transcribed, one sign per token. `;` here only separates words as read; `-` is a line-end hyphen on the card; `x>y` means the card shows x and it is read as y by word sense.

```text
2. 3 1: 7, ; 8 1. 3, 4, 1 8, 7 1' 8 !
2. 3, 8, 1: 7, 1 8, 5, 1: 7 ; 5 0 4. ; 5 1. 2, 1. 7 ; 5, 1: - 5 1: 8, ;
3. 1. 7, 1' 3, 6, 1. 9 ; 4 1: 5, 8 1: 4. :1 6, 7 ; 9 1 7, 8, 1' 3>3. 1.
5, ) ; 7. 1: 3, 1: 8, 8, 1: 8 ; 3. 0 5, 6, 1. ; 5 1. ; 8 2. 4, ; 1. 3 3
1 4, ; 0 8, ; 5, 1: 8, ; 3. 0 5, 6, 1. ; 2. 3 1: 7, ; 1. 6. 1' 8 ; 6, 1:
8 ; 1 7, ; 4, 0 6, 3 0 5, 8, 1. 8 ; 5 0 4. ; 5 1. 9, 1. ; 6 0, 6 6 0, 6,
; 5, 1: 4, 1. 5, 1' 1, 1, ; 6, 1. - 4. 0 8, ; 6, 2. 9, 1: 8, ; 3. 0 5,
6, 1. ; 8 1 7 0 3, ; 1, 1: 8, 0 9 - 9 1. 6, 8, 1. 8 ; 3. 0 5, 6, 1. ; 1.
9, ; 1. 6 8, 0 6, ) ; 6, 0 3 1: ; 1: 9, 8, ; 8 0 7, 8, ; 5 1. 3 6 :1 7 ;
8 1. 6 3 ; 7. 0 3>3. 1. 5, ; 8, 0, 1, - 1, 1: 8,
8, 1 8, 7 0 6, ; 1 3, 0 7 ; 2, 1. 7 ; 5, 1: 3. 1: 5, 1: 8,
8, 1 8, 7 0 6, ; 7. 1: 3, 1: 8, 5, 1: 7 ; 8, 2. 4, 1: 3 1: 8, .
6, 1 6, 2, 1: 6, ; 6, 1. 4. 0 1, 1, ; 4. 0, 8, 3, 1: 5, 1: 8
8 1 6, 8, ; 1. ; 8, 1 8, 7 0 5, 8, ; 7. 1: 3, 1: 5, 1: 8
1. 7 1' 3, ; 1. 5, 3. 1. ; 1. 7 1' 3, ; 2. 1, 3, 1: 6,
8 1 6, 3 1 4, ; 8, 1: ; 3. 7.>1. 4. ; 1. 9, ; 1: 7. 1: 8 1, 1: 6, .
7, 0 7 7. 0 3, ; 0, 5, 1: 5, - 3. 1: ; 2. 7, ; 2, 0 7 0 5, - 3. 1. ; 8
1. 3, 1. 3 0 7 ; 5 :1 7, 2. 4, 1: 7, ; 7 1: 3 3. 1: 7, 1: 8 ; 2. 7, ; 1
8 1' 3 0 3 ) ; ( 1' 3>3, 9 1' 3 )
```

## Plaintext (Hungarian)

Accents, capitals and most punctuation are editorial. The spelling is the writer's; [ ] shows letters he wrote single.

Mezőkövesd, 1916, II/12.

Édes Margitkám!

Értesítlek, hogy hacsak lehet, vasárnap felmegyünk Pistával. Szerettem volna, ha még addig ot[t] let[t] volna édes anyám, nem is gondoltam, hogy haza jöjjön. Legalább nagyot nézet[t] volna, mikor betoppantam volna az ajtón. No de ezt most hadjuk [= hagyjuk], majd szóval többet;

Titkon írok csak levelet, / Titkon szeretlek tégedet. / Nincsen nagyobb gyötrelem, / Mint a titkolt szerelem.

I → Akár alva, akár ébren, / Mindig te vagy az eszemben.

Sokszor ölelve és csókolva maradok hűséges, kedvesem, és imádód (Árpád)

## English translation

Mezőkövesd, 12 February 1916. Sweet Margitka of mine! I let you know that, if at all possible, we are coming up on Sunday with Pista. I would have liked my mother to have stayed there until then; I did not even think she would come home. At least she would have been quite astonished when I walked in at the door. But let us leave this now, more by word of mouth;

Only in secret I write a letter, / in secret I love you. / There is no greater torment / than a hidden love.

I → Whether asleep or awake, / you are always on my mind.

Embracing and kissing you many times, I remain faithful, my sweetheart, and your adorer (Árpád)

## Slovak translation

Mezőkövesd, 12. 2. 1916. Moja sladká Margitka! Oznamujem ti, že ak to len pôjde, v nedeľu prídeme hore s Pištom. Bol by som rád, keby tam moja mama ešte dovtedy zostala, ani som si nemyslel, že pôjde domov. Aspoň by sa bola poriadne začudovala, keby som vkročil do dverí. Ale nechajme to teraz, viac osobne;

Len tajne píšem list, / tajne ťa ľúbim. / Niet väčšieho trápenia / než utajená láska.

I → Či v spánku, či bdiac, / stále si mi na mysli.

Mnohokrát ťa objímam a bozkávam a zostávam verný, moja milá, a tvoj ctiteľ (Árpád)

## Reproduction

From the repository root:

```sh
python3 -I ciphers/hcp-1145/work/decode.py
```

The script checks the SHA-256 of all four scans, decodes work/transcription.txt with the key, asserts every word against the stated reading, and prints the counts, the raw decode and the text. It reports 385 cipher signs, 28 distinct, 74 words, 4 read by sense. The assertion folds accents, so it tests letters only. The formatted text is hard-coded after the assertion, and the date and address are clear text. The script does not read the images; the transcription is manual and was checked sign by sign in review.

## Uncertainties

Four signs are read by sense. Each is marked `x>y` in the transcription.

- **vagy.** The middle sign shows `7.` (a crossed 7 with its dot), with an overwriting and a grey smear above it. The key alone gives vszgy, not a word. It is taken as a slip or correction for `1.`. The word is fixed by the verse and its metre.
- **Pistával.** The sign is a plain `3` with no dot, giving Pistádal. Pistádal for Pistáddal ("with your Pista") is a real alternative, compare Angyukádal on HCP 1178. It changes only whose Pista is meant.
- **szóval.** Also a plain `3`, giving szódal, which makes no sense here. The writer seems to drop the dot of `3.` before `1.` in -val, which is the reason for preferring Pistával above.
- **Árpád.** The boxed signature shows `1' 3 9 1' 3`, a plain `3` with no comma, giving Ádpád. It is read as Árpád because HCP 1174 has `1' 3, 9 1' 3`. The box and its brown line may be a later or separate addition.

Other points:

- **kedvesem.** The card has this form, not the kedvesed of HCP 1174. The parse "I remain faithful, my sweetheart, and your adorer" and its commas are editorial. The alternative is a slip for kedvesed, "your faithful sweetheart". The letters do not change either way.
- **Two signs rest on one word each.** `4` = f occurs only in felmegyünk and `6.` = ny only in anyám. Both words are secure in context, while `4.` (7 times) and `6` (6 times) recur in unrelated words.
- **hadjuk** is a phonetic spelling of hagyjuk. Its `:1` has the upper dot merged with the flag of the 1. `:1` serves for u here as well as ü. ott, lett and nézett are written with a single t, which is his habit.
- **Close calls.** `0,` beside a long comma can look like `9` at low zoom, but at 5x the sign and comma are separate in többet and gyötrelem. There is a short dash under the first sign of kedvesem. It looks like part of the broken dashed row above the date and not the dot of `7.`, so the sign is read as `7` = k.
- **The context of the mother sentence is thin.** The card does not say whose mother is meant, whose visit it was, or where "there" is. édes anyám is read as "my mother", and "up" fits Szomolya as on HCP 1174.
- **The margin mark.** A roman I with an arrow stands at the couplet. Its meaning is unproven. HCP 1174 marks its couplet with II, so it may number a series.
- **Marks with no cipher value.** The broken row of short dashes above the date is read as a ruled line. The red 3526 2 is a printed publisher number.
- **Not established.** Whether the HistoCrypt article discusses this card, whether the verses have a printed source (none was found), and the year on the postmark.

## Review summary

Reviewer: a separate Claude Opus 5.5 agent, round 1, verdict **ACCEPT**. The reviewer tried to refute the reading and failed. It ran the reproduction command, recomputed the hashes, read all cipher rows from its own 4x crops and decoded them with its own script and separately entered key. The result was 385 signs and no token differences from the solver's "as seen" tokens. That transcription was made after seeing the solver's, so it is a sign-by-sign check and not a blind one. The reviewer confirmed that every row is accounted for, that the four read-by-sense signs look as disclosed, that no sign value conflicts with the FINAL sister cards, and that 12 February 1916 was a Saturday.

Its three findings were all minor and concerned the write-up:

- **Recurrence claim.** The solution said all four new signs recur in several words. `4` and `6.` occur once each. This is corrected and stated above.
- **kedvesem.** The translation took hűséges with kedvesem and left the sentence broken. The English and Slovak now follow the parse above, and the alternative kedvesed is stated.
- **Semicolon.** The writer's semicolon after többet was not recorded in the transcription as claimed. Its dot stands above the comma of the final `8,`. The transcription now has a comment line saying so.

No decoded letter changed as a result of the review.

## Sources

- HC Portal record 1145, General, Description and Attachments tabs, captured 2026-11-02: https://crypto.hcportal.eu/dashboard/cryptograms/1145 (source/metadata.md).
- Picture side: https://api.hcportal.eu/media/3495/conversions/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_pic-large.jpg, original https://api.hcportal.eu/media/3495/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_pic.jpg
- Message and address side: https://api.hcportal.eu/media/3496/conversions/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr-large.jpg, original https://api.hcportal.eu/media/3496/cpc_1916-02-12_HU_Mezokovesd_HU_Szomolya_szomolya-17_adr.jpg
- Family key: ciphers/hcp-1174, hcp-1178 and hcp-1179 in this repository.
- AI Decipherment Register (https://ai.hcportal.eu/register/), checked 2026-11-02: no record for this card.
