# HCP 1159 (cpc_1915-11-_HU_Mezokovesd_HU_Szomolya_szomolya-45): a love verse in number-letters to Margitka Sziber

Human solver: Tomáš Pavuk

**Status: deciphered (125 of 126 cipher signs; one blotted sign left undecoded, one letter supplied by emendation); independent review 1 verdict ACCEPT, no change to the reading.** Report dated 2026-11-02.

## Origin and context

The cryptogram is record 1159 of the HC Portal (https://crypto.hcportal.eu/dashboard/cryptograms/1159), portal name cpc_1915-11-_HU_Mezokovesd_HU_Szomolya_szomolya-45, from Tobias Schrödel's cryptographic postcards collection (private collection). When captured on 2026-11-02 the portal listed it as **Not solved**, tagged Postcard, T. Schrödel Collection, category Substitution, language Unknown, sender Unknown, recipient Margitka Sziber, with no transcription or solution attached. The portal links a HistoCrypt article (https://ecp.ep.liu.se/index.php/histocrypt/article/view/166). That article was not consulted, so it is not known whether it discusses this card.

The card belongs to a series sent from Mezőkövesd to Szomolya in north-east Hungary during the First World War. The portal name gives November 1915. The postmark does not confirm this: only "ME..." and a digit or two can be seen.

The picture side shows a couple with roses and carries no writing. All writing is on the address side: a heading in digits, four open lines, a dashed rule, the digit block, and an open close. The address reads **Tek. / Rózsa reményű / Sziber Margitka / kisasszonynak / Szomolya / u. p. Bogács / Borsod m.**

![Address side with all the writing (source/address-large.jpg)](../source/address-large.jpg)

![Picture side, no writing (source/picture-large.jpg)](../source/picture-large.jpg)

## Method

The cipher was transcribed by hand from the highest-resolution original available, in enlarged crops. No OCR was used. The key was not reconstructed on this card. It is the family key of the Mezőkövesd cards, fixed on sister cards (hcp-1174, 1178, 1179, and the tables of hcp-1163, 1164, 1166, 1168, 1169), and applied here without change. The values `4.` = gy and `1,` = b are not in the hcp-1174 table but stand on several of the other sister tables.

The signs run on with no word division, so the word division, line breaks and punctuation of the verse below are editorial. Transcription by the card's rows, with X for the blotted sign, each row followed by its decoding:

```text
heading  2. 3 1: 7, 8 1. 3, 4, 1 8, 7 1' 8
         édesmargitkám
row 1    3. 1: 3 3 8, 0, 5, 1: 8 1: 7 2. 9 1: 7,
         veddtölemeképes
row 2    5, 1. 9 0 8,
         lapot
row 3    7, 3. 2. 5, 1: 8, 1 7. 8, 1. 7. 1 3. 1: 8 1: 8,
         svéletisztaszivemet
row 4    2. 3, 8, 1: 3 5, 1' 4, 0 5, 2. 3, 8, 1: 3 2. 4, 1. 9,
         értedlágolértedégaz
row 5    8 1 4, 1. 7, 1 3, 1: 5, 6, 1: 8 8, 1: 8 1: 8,
         migasirelnemtemet
row 6    8, 1' 3. 0 5, 1, 1. 6, 1. 3. 1' 4. 1. 8 6, 1: 7 1: 8
         távolbanavágyamnekem
row 7    5 1. 8, 1: 1 7, 1 8, 8, X 3. 0 5, 6, 1' 5, 3. 1: -
         hateisittXvolnálve-
row 8    5, 1: 8
         lem
```

In review, a separate agent made its own crops, transcribed all rows before comparing, and decoded them with its own script. Its 125 signs agree with the solver's sign for sign, including the row breaks.

The reader can reproduce the decoding from the repository root with `python3 -I ciphers/hcp-1159/work/decode.py`. The open text is hard-coded in that script, so the command proves only the decoding of the cipher signs.

## Key

Monoalphabetic substitution (MASC). Each letter is one digit with or without a mark, and the mark is part of the sign. Only the 23 signs attested on this card are listed. Vowel length is not always marked, and Hungarian digraphs have a single sign.

| sign | letter | sign | letter | sign | letter |
|---|---|---|---|---|---|
| 0 | o | 2. | é | 6, | n |
| 0, | ö, ő | 3 | d | 7 | k |
| 1 | i, í | 3, | r | 7, | s |
| 1. | a | 3. | v | 7. | sz |
| 1: | e | 4, | g | 8 | m |
| 1' (high dot) | á | 4. | gy | 8, | t |
| 1, | b | 5 | h | 9 | p |
| | | 5, | l | 9, | z |

## Plaintext

Square brackets mark text enciphered on the card. (n) marks a letter that is not on the card.

```text
[Édes Margitkám]

Kérlek írd meg, hogy megkaptad-e a levelet, mert küldtem benne a számbetűket is.

[Vedd tőlem e képes lapot
s véle tiszta szívemet
érted lá(n)gol, érted ég az,
míg a sír el nem temet.
Távolban a vágyam nekem,
ha te is itt volnál velem.]

Mindnyájatokat csókollak. Sz. Á.
Írjál.
```

**English**

[Sweet Margitka]

Please write and tell me whether you got the letter, because I also sent the number-letters in it.

[Take this picture card from me, / and with it my pure heart; / it flames for you, it burns for you, / until the grave buries it. / Far away is my longing; / if only you too were here with me.]

I kiss you all. Sz. Á. Write.

Address: To the honourable / "Rose-hoped" Miss Margitka Sziber / Szomolya / post office Bogács / Borsod county.

**Slovak**

[Moja sladká Margitka]

Prosím, napíš mi, či si dostala list, lebo som v ňom poslal aj číselné písmená.

[Prijmi odo mňa túto pohľadnicu / a s ňou moje čisté srdce; / pre teba plane, pre teba horí, / kým ho hrob nepochová. / V diaľke je moja túžba; / keby si aj ty bola tu so mnou.]

Bozkávam vás všetkých. Sz. Á. Napíš.

Adresa: Ctenej / „ružovonádejnej“ slečne Margitke Sziberovej / Szomolya / pošta Bogács / župa Borsod.

The Slovak "poslal" assumes a male writer. That fits the family's signature but is not shown on this card.

The open line about the "számbetűk" (number-letters) refers to the cipher itself: the writer sent them in a letter.

The epithet "Rózsareményű", written in two parts on the card, is the one unusual word. It is a playful honorific, literally "of rose hope", apparently formed like "szépreményű" ("of fair hope"). This gloss is the solver's reading; no printed parallel is known to it.

## What remains uncertain

- **lá(n)gol.** The card has `5, 1' 4, 0 5,`, literally "lágol", with a clear gap and no `6,`. The printed "lángol" is an emendation resting on sense alone, supported by the parallel "ég" ("burns").

![The word lágol: no n between á and g (work/crops/z_lagol.png)](../work/crops/z_lagol.png)

- **Blotted sign after "itt".** A smeared sign with a clear comma follows `1 8, 8,`. Its body looks like an 8 written over or wiped, so it may be an abandoned third `8,`, but this cannot be proved. It is left undecoded. "itt" is complete without it, and the line reads and scans.

![The blotted sign after itt (work/crops/z_blot.png)](../work/crops/z_blot.png)

- **"az" at the end of row 4.** The last sign is `9,`: closed head, one straight stem, no lower loop, unlike the two-loop 8s nearby. `8,` would give "égat", no word. Shape and sense agree, but the word division "ég az" is editorial.
- **Verse line 5.** "Távolban a vágyam nekem" is loose as verse, though every sign is clean. The link with the last line is editorial punctuation.
- **Stray strokes.** A horizontal line runs between physical rows 5 and 6, under "ír el" and above part of the "Távolban" row. It crosses no sign and decodes to nothing; its meaning, if any, is unknown. A similar flourish stands above "Mindnyájatokat". A hyphen stands at the row break inside "ve-lem".

![The stray line between rows 5 and 6 (work/crops/z_stray.png)](../work/crops/z_stray.png)

- **Open text.** In "megkaptad-e a levelet" the "a" looks deformed by the tail of the g above. In "számbetűket" the accent and double dots partly merge, and "szám" + "betű" is the only sense found.
- **Signature.** A stroke stands over the A here, so the report prints Sz. Á. The same initials are reported as Sz. A. on hcp-1175, 1176 and 1179; those cards were not re-examined. hcp-1174 is signed Árpád, which would fit Á., but nothing on this card names him, so this is only a hypothesis.
- **Date and source.** The portal's 1915-11 is not confirmed by the postmark. A printed source for the verse was not traced.

## Why the reading is believed correct

- The key was fixed on other cards and applied without change. All 125 readable signs give continuous Hungarian, with one missing letter and no substitute value.
- The text is verse in lines of 7 to 8 syllables with exact rhyme: szívemet / temet and nekem / velem.
- The 13-sign heading equals the heading of hcp-1174.
- "Vedd tőlem e képes lapot" ("take this picture card from me") fits the card it is written on, and the couple with roses fits the love verse.

## Review summary

The independent reviewer (a separate Claude Opus 5.5 agent) tried to refute the reading. It re-ran the command, transcribed and decoded the card independently, checked the disputed signs on enlargements, compared the key with the family tables, and checked the open text and the address. Verdict: **ACCEPT**. It left four minor findings, all addressed, and none changed the reading:

1. The stray line had been placed between the wrong rows. It stands between physical rows 5 and 6.
2. "lá(n)gol" is now called an emendation.
3. The address and the epithet "Rózsareményű" are now translated and glossed.
4. The Sz. Á. / Sz. A. inconsistency stays disclosed, with the Árpád link marked as a hypothesis.

Not verified: the date, whether the HistoCrypt article discusses this card, what the blotted sign was, and what the stray line means.
